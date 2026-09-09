#!/usr/bin/env python3
"""Convert UltiSnips UVM snippets into AI-friendly Markdown templates.

The UltiSnips ``*.snippets`` files in this repository are written for Vim's
UltiSnips plugin. That format (tabstops ``${1:default}``, mirrors ``$1``,
choices ``${1|a,b|}`` and Python interpolation ``` `!p ...` ```) is convenient
for interactive expansion inside an editor, but awkward for an AI agent to read
and fill programmatically.

This script parses every snippet block and emits, under ``ai-skill/templates/``:

  * one Markdown file per snippet block, with YAML frontmatter describing the
    trigger(s), description and placeholder metadata, and a fenced code block
    whose body uses a single, uniform ``{{PLACEHOLDER}}`` marker syntax;
  * a ``manifest.json`` index of every generated template.

Design principles
-----------------
* **Deterministic** - a recursive-descent parser turns each body into an AST,
  so nested tabstops, literal ``{ }`` (SystemVerilog concatenations, covergroups)
  and escaped ``\\$`` / ``` \\` ``` are all handled correctly.
* **No silent loss** - only the two Python interpolation forms that actually
  occur in this library are recognised. Any other ``` `...` ``` block, or any
  unparseable construct, raises ``Unhandled`` and aborts the run rather than
  dropping semantics quietly.

Run from anywhere:  ``python ai-skill/script/convert_ultisnips.py``
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths and per-category settings
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent.parent  # third_party/uvm-snippet
SNIPPETS_DIR = REPO_ROOT / "ultisnips"
OUT_DIR = REPO_ROOT / "ai-skill" / "templates"
GENERATED_SUBDIRS = ("systemverilog", "tcl", "make")

# Fenced-code language per category (category is the top-level folder within
# the ultisnips/ source tree, or "make" for the top-level make.snippets file).
FENCE_LANG = {"systemverilog": "systemverilog", "tcl": "tcl", "make": "makefile"}


class Unhandled(Exception):
    """Raised when a snippet contains a construct this converter does not model."""


# ---------------------------------------------------------------------------
# AST node shapes (plain tuples, tagged by their first element)
# ---------------------------------------------------------------------------
#   ('lit', text)          literal text
#   ('mirror', n)          $n              (reuse of tabstop n's value)
#   ('tabempty', n)        ${n}            (tabstop with no default)
#   ('tab', n, sub_ast)    ${n:default}    (default parsed recursively)
#   ('choice', n, [opts])  ${n|a,b,c|}
#   ('cursor',)            $0              (final cursor - dropped on render)
#   ('py_cond', n, then)   `!p snip.rv='<then>' if t[n] else ''`  (conditional literal)
#   ('py_pkg',)            `!p ... os.path.splitext(fn) ... `


def _find_closing_backtick(s: str, start: int) -> int:
    j = s.find("`", start)
    if j == -1:
        raise Unhandled(f"unterminated backtick interpolation near: {s[start:start + 40]!r}")
    return j


def _find_matching_brace(s: str, brace_idx: int) -> int:
    """Return the index of the ``}`` matching the ``{`` at ``brace_idx``.

    Tracks nested braces (so ``${1:${2:x}}`` and literal ``{ }`` in the default
    are balanced) and skips over backtick interpolation spans.
    """
    depth = 0
    i = brace_idx
    n = len(s)
    while i < n:
        c = s[i]
        if c == "\\" and i + 1 < n and s[i + 1] in "`$\\":
            i += 2
            continue
        if c == "`":
            i = _find_closing_backtick(s, i + 1) + 1
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise Unhandled(f"unbalanced ${{...}} near: {s[brace_idx:brace_idx + 40]!r}")


def _parse_interp(code: str):
    c = code.strip()
    if not c.startswith("!p"):
        raise Unhandled(f"non-Python interpolation not supported: `{code}`")
    body = c[2:].strip()
    if "os.path.splitext(fn)" in body:
        return ("py_pkg",)
    # General "conditional literal" form:  snip.rv = '<then>' if t[N] else '<else>'
    # (covers both the `_param` utils suffix and the `: ` coverpoint-label separator).
    m = re.match(
        r"""snip\.rv\s*=\s*(['"])(?P<then>.*?)\1\s+if\s+t\[(?P<n>\d+)\]"""
        r"""\s+else\s+(['"]).*?\4\s*$""",
        body,
    )
    if m:
        return ("py_cond", int(m.group("n")), m.group("then"))
    raise Unhandled(f"unhandled Python interpolation: `{code}`")


def _parse_tabstop(inner: str):
    mc = re.match(r"^(\d+)\|(.*)\|$", inner, re.S)
    if mc:
        return ("choice", int(mc.group(1)), mc.group(2).split(","))
    md = re.match(r"^(\d+):(.*)$", inner, re.S)
    if md:
        return ("tab", int(md.group(1)), parse(md.group(2)))
    mb = re.match(r"^(\d+)$", inner)
    if mb:
        return ("tabempty", int(mb.group(1)))
    raise Unhandled(f"unhandled tabstop: ${{{inner}}}")


def parse(s: str):
    """Parse an UltiSnips body fragment into a list of AST nodes."""
    nodes = []
    buf: list[str] = []
    i, n = 0, len(s)

    def flush():
        if buf:
            nodes.append(("lit", "".join(buf)))
            buf.clear()

    while i < n:
        c = s[i]
        # Escapes: \` \$ \\  -> emit the second char literally.
        if c == "\\" and i + 1 < n and s[i + 1] in "`$\\":
            buf.append(s[i + 1])
            i += 2
            continue
        # Backtick interpolation.
        if c == "`":
            j = _find_closing_backtick(s, i + 1)
            flush()
            nodes.append(_parse_interp(s[i + 1:j]))
            i = j + 1
            continue
        if c == "$":
            # ${<digit>...} is a tabstop; ${<letter>...} (e.g. Tcl/Make ${VAR})
            # and $<letter> (e.g. $sformatf, $(MAKE_VAR)) are literal text.
            if i + 2 < n and s[i + 1] == "{" and s[i + 2].isdigit():
                j = _find_matching_brace(s, i + 1)
                flush()
                nodes.append(_parse_tabstop(s[i + 2:j]))
                i = j + 1
                continue
            m = re.match(r"\$(\d+)", s[i:])
            if m:
                num = int(m.group(1))
                flush()
                nodes.append(("cursor",) if num == 0 else ("mirror", num))
                i += m.end()
                continue
            buf.append("$")
            i += 1
            continue
        buf.append(c)
        i += 1

    flush()
    return nodes


# ---------------------------------------------------------------------------
# Placeholder naming and rendering
# ---------------------------------------------------------------------------


def _upper_name(ident: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", ident).strip("_").upper()
    return s or "TAB"


def _slugify(text: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return s or "snippet"


def _simple_ident(ast) -> str | None:
    """If ``ast`` is exactly one literal that is a bare identifier, return it."""
    if len(ast) == 1 and ast[0][0] == "lit":
        text = ast[0][1].strip()
        if re.fullmatch(r"[A-Za-z_]\w*", text):
            return text
    return None


def _is_pkg_default(ast) -> bool:
    return len(ast) == 1 and ast[0][0] == "py_pkg"


def _starts_with_param_block(ast) -> bool:
    return bool(ast) and ast[0][0] == "lit" and ast[0][1].lstrip().startswith("#(")


def collect_defs(nodes, defs):
    """Walk the AST collecting, per tabstop number, its default AST / choices."""
    for node in nodes:
        tag = node[0]
        if tag == "tab":
            _, num, sub = node
            d = defs.setdefault(num, {})
            d.setdefault("default_ast", sub)
            collect_defs(sub, defs)
        elif tag == "choice":
            _, num, opts = node
            defs.setdefault(num, {}).setdefault("choices", opts)
        elif tag in ("mirror", "tabempty"):
            defs.setdefault(node[1], {})


def assign_names(defs):
    """Assign a placeholder name to every tabstop number, keeping them unique."""
    names: dict[int, str] = {}
    used: set[str] = set()
    for num in sorted(defs):
        d = defs[num]
        ast = d.get("default_ast")
        if ast is not None and _is_pkg_default(ast):
            name = "PKG_NAME"
        elif ast is not None and (ident := _simple_ident(ast)):
            name = _upper_name(ident)
        elif ast is not None and _starts_with_param_block(ast):
            name = f"PARAMS_{num}"
        else:
            name = f"TAB_{num}"
        if name in used:  # keep names unique within a snippet
            name = f"{name}_{num}"
        used.add(name)
        names[num] = name
    return names


def render(nodes, names, derived, expand_tabs=True) -> str:
    out: list[str] = []
    for node in nodes:
        tag = node[0]
        if tag == "lit":
            # Expand tab indentation to 4 spaces, except for Makefiles, whose
            # recipe lines require a literal tab (caller passes expand_tabs=False).
            out.append(node[1].replace("\t", "    ") if expand_tabs else node[1])
        elif tag == "cursor":
            pass  # drop the final-cursor marker
        elif tag in ("mirror", "tabempty", "tab", "choice"):
            out.append("{{" + names[node[1]] + "}}")
        elif tag == "py_cond":
            _, num, then = node
            ref = names.get(num, f"TAB_{num}")
            dname = "PARAM_SUFFIX" if then == "_param" else f"{ref}_SEP"
            derived[dname] = {"ref": ref, "then": then}
            out.append("{{" + dname + "}}")
        elif tag == "py_pkg":
            derived["PKG_NAME"] = True
            out.append("{{PKG_NAME}}")
        else:  # pragma: no cover - defensive
            raise Unhandled(f"unknown AST node: {node!r}")
    return "".join(out)


# ---------------------------------------------------------------------------
# Snippet-file parsing
# ---------------------------------------------------------------------------

SNIP_RE = re.compile(
    r'^snippet\s+(?:"([^"]*)"|(\S+))(?:\s+"([^"]*)")?(?:\s+(\S+))?\s*$'
)


def parse_triggers(raw: str, flags: str):
    """Split a regex-alternation trigger (``Agt|Agent``) into a list."""
    if "r" in flags and "|" in raw and re.fullmatch(r"[\w|]+", raw):
        return [t for t in raw.split("|") if t]
    return [raw]


def read_header(lines):
    author = None
    for line in lines:
        if line.startswith("snippet "):
            break
        m = re.match(r"#\s*Author\s*:\s*(.+?)\s*$", line)
        if m:
            author = m.group(1)
    return author


def parse_file(path: Path):
    """Yield one dict per snippet block found in ``path``."""
    lines = path.read_text(encoding="utf-8").splitlines()
    author = read_header(lines)

    i, n = 0, len(lines)
    while i < n:
        m = SNIP_RE.match(lines[i])
        if not m:
            i += 1
            continue
        raw_trigger = m.group(1) if m.group(1) is not None else m.group(2)
        description = m.group(3) or ""
        flags = m.group(4) or ""
        body_lines = []
        i += 1
        while i < n and lines[i].rstrip() != "endsnippet":
            body_lines.append(lines[i])
            i += 1
        if i >= n:
            raise Unhandled(f"{path.name}: 'snippet {raw_trigger}' missing endsnippet")
        i += 1  # consume 'endsnippet'

        yield {
            "raw_trigger": raw_trigger,
            "triggers": parse_triggers(raw_trigger, flags),
            "description": description,
            "flags": flags,
            "body": "\n".join(body_lines),
            "author": author,
        }


# ---------------------------------------------------------------------------
# Frontmatter / Markdown emission
# ---------------------------------------------------------------------------


def _yaml_list(items):
    return "[" + ", ".join(json.dumps(x) for x in items) + "]"


def build_placeholders(defs, names, derived, expand_tabs=True):
    """Produce the ordered placeholder metadata list for the frontmatter."""
    entries = []
    for num in sorted(defs):
        d = defs[num]
        name = names[num]
        entry = {"name": name, "tabstop": num}
        if "choices" in d:
            entry["choices"] = d["choices"]
            entry["default"] = d["choices"][0] if d["choices"] else ""
        else:
            ast = d.get("default_ast")
            if name == "PKG_NAME":
                entry["derived"] = True
                entry["note"] = "defaults to the snippet source file base name"
            elif ast is not None:
                rendered = render(ast, names, {}, expand_tabs)
                if rendered:
                    entry["default"] = rendered
        entries.append(entry)

    for dname in sorted(derived):
        info = derived[dname]
        ref, then = info["ref"], info["then"]
        if dname == "PARAM_SUFFIX":
            rule = f"\"_param\" if {ref} is set (class is parameterized), else \"\""
        else:
            rule = f"\"{then}\" if {ref} is set, else \"\""
        entries.append({"name": dname, "derived": True, "rule": rule})
    return entries


def render_frontmatter(meta, placeholders):
    lines = ["---"]
    lines.append(f"id: {json.dumps(meta['id'])}")
    lines.append(f"source_file: {json.dumps(meta['source_file'])}")
    lines.append(f"triggers: {_yaml_list(meta['triggers'])}")
    lines.append(f"description: {json.dumps(meta['description'])}")
    lines.append(f"category: {meta['category']}")
    lines.append(f"ultisnips_flags: {json.dumps(meta['flags'])}")
    if meta.get("author"):
        lines.append(f"author: {json.dumps(meta['author'])}")
    if placeholders:
        lines.append("placeholders:")
        for p in placeholders:
            lines.append(f"  - name: {json.dumps(p['name'])}")
            if "tabstop" in p:
                lines.append(f"    tabstop: {p['tabstop']}")
            if "choices" in p:
                lines.append(f"    choices: {_yaml_list(p['choices'])}")
            if "default" in p:
                lines.append(f"    default: {json.dumps(p['default'])}")
            if p.get("derived"):
                lines.append("    derived: true")
            if "rule" in p:
                lines.append(f"    rule: {json.dumps(p['rule'])}")
            if "note" in p:
                lines.append(f"    note: {json.dumps(p['note'])}")
    else:
        lines.append("placeholders: []")
    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def category_of(path: Path) -> str:
    rel = path.relative_to(SNIPPETS_DIR)
    return rel.parts[0] if len(rel.parts) > 1 else "make"


def main() -> int:
    sources = sorted(SNIPPETS_DIR.rglob("*.snippets"))
    if not sources:
        print("error: no .snippets files found", file=sys.stderr)
        return 1

    # Start from a clean slate for generated content (leave FORMAT.md intact).
    for sub in GENERATED_SUBDIRS:
        shutil.rmtree(OUT_DIR / sub, ignore_errors=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    used_bases: dict[str, set] = {}
    total = 0

    for src in sources:
        rel = src.relative_to(SNIPPETS_DIR).as_posix()
        category = category_of(src)
        lang = FENCE_LANG.get(category, "")
        blocks = list(parse_file(src))
        multi = len(blocks) > 1
        stem = src.stem

        for block in blocks:
            total += 1
            ast = parse(block["body"])
            defs: dict[int, dict] = {}
            collect_defs(ast, defs)
            names = assign_names(defs)
            derived: dict = {}
            # Makefiles need literal tabs; everything else uses 4-space indent.
            expand_tabs = category != "make"
            body = render(ast, names, derived, expand_tabs)
            placeholders = build_placeholders(defs, names, derived, expand_tabs)

            base = f"{stem}__{_slugify(block['description'])}" if multi else stem
            seen = used_bases.setdefault(category, set())
            unique, k = base, 2
            while unique in seen:
                unique = f"{base}-{k}"
                k += 1
            seen.add(unique)

            meta = {
                "id": unique,
                "source_file": rel,
                "triggers": block["triggers"],
                "description": block["description"],
                "category": category,
                "flags": block["flags"],
                "author": block["author"],
            }
            frontmatter = render_frontmatter(meta, placeholders)
            content = f"{frontmatter}\n\n```{lang}\n{body}\n```\n"

            out_path = OUT_DIR / category / f"{unique}.md"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")

            manifest.append({
                "id": unique,
                "file": out_path.relative_to(OUT_DIR).as_posix(),
                "triggers": block["triggers"],
                "description": block["description"],
                "category": category,
                "placeholders": [p["name"] for p in placeholders],
            })

    manifest.sort(key=lambda e: (e["category"], e["id"]))
    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )

    print(f"Converted {total} snippet block(s) from {len(sources)} file(s).")
    print(f"Wrote {len(manifest)} template(s) + manifest.json to {OUT_DIR}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
