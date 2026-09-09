# AI-friendly UVM template format

The files under this directory are generated from the UltiSnips `*.snippets`
sources in this repository by [`ai-skill/script/convert_ultisnips.py`](../script/convert_ultisnips.py).
They exist so that an AI agent (or any tool) can read a template, understand its
customisation points from structured metadata, and fill them in — without having
to interpret Vim/UltiSnips expansion semantics.

**Do not edit generated files by hand.** Edit the `.snippets` source (or the
converter) and re-run `python ai-skill/script/convert_ultisnips.py`.

## Layout

```
ai-skill/templates/
├── FORMAT.md            # this document (hand-written, not generated)
├── manifest.json        # index of every generated template
├── systemverilog/*.md   # one file per SystemVerilog snippet block
├── tcl/*.md             # QuestaSim TCL flow snippets
└── make/*.md            # Makefile snippet(s)
```

One snippet block becomes one `.md` file. When a source file holds a single
block the file is named after the source stem (e.g. `agent.snippets` →
`systemverilog/agent.md`). When a source file holds several blocks, each file is
named `<stem>__<description-slug>.md` (e.g. `basic__uvm-component.md`).

## File structure

Each template is YAML frontmatter followed by one fenced code block:

```markdown
---
id: agent
source_file: systemverilog/agent.snippets
triggers: ["Agent", "Agt"]
description: "UVM Agent"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "AGENT"
    tabstop: 1
    default: "Agent"
  - name: "PARAMS_2"
    tabstop: 2
    default: " #(\n    {{TAB_3}}\n)"
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{AGENT}}{{PARAMS_2}} extends uvm_agent;
    ...
```
```

Template bodies are indented with **4 spaces** (the converter expands the source
tabs). The one exception is the `make` category, whose recipe lines keep the
literal tabs GNU make requires.

## Frontmatter fields

| field | meaning |
|-------|---------|
| `id` | unique identifier; also the file name (without `.md`) |
| `source_file` | originating `.snippets` path, relative to the repo root |
| `triggers` | one or more editor trigger words the block responded to |
| `description` | human description carried over from the snippet |
| `category` | `systemverilog` \| `tcl` \| `make` |
| `ultisnips_flags` | original UltiSnips option letters, kept for traceability |
| `author` | copied from the source file header, when present |
| `placeholders` | ordered list of every customisation point (see below) |

## Placeholder syntax

Everything an author would fill in appears in the body as `{{NAME}}`. Names are
stable and reused: if the same value occurs in several places (a class name in
its declaration, its constructor, and its message IDs) the **same** `{{NAME}}`
appears at every site, so setting it once is enough.

Names are derived deterministically from the source:

* a tabstop whose default is a bare identifier → that identifier upper-cased
  (`${1:Agent}` → `{{AGENT}}`, `${12:cfg}` → `{{CFG}}`);
* a tabstop whose default is a parameter port block `#(...)` → `{{PARAMS_<n>}}`;
* any other tabstop (empty, multi-line, or a choice list) → `{{TAB_<n>}}`.

### Placeholder metadata

Each `placeholders` entry may carry:

* `tabstop` — the original UltiSnips tabstop number.
* `default` — the suggested value. It may itself contain `{{...}}` markers
  (e.g. an optional parameter block that nests another placeholder). An empty or
  omitted default means "fill this in".
* `choices` — a fixed set of allowed values; `default` is the first one.
* `derived` / `rule` / `note` — see below.

### Derived placeholders

Two placeholders are computed rather than free-form; they capture logic the
original snippets expressed with embedded Python:

* **`{{PARAM_SUFFIX}}`** — expands to `_param` when the associated parameter
  placeholder is non-empty (i.e. the class is parameterised), otherwise empty.
  It is what turns `` `uvm_component_utils `` into `` `uvm_component_param_utils ``.
  Its `rule` names the parameter placeholder it depends on.
* **`{{PKG_NAME}}`** — the package name, which defaulted to the source file's
  base name in the original snippet.

## How to fill a template

1. Read `manifest.json` to locate the template(s) you need by `id`, `triggers`
   or `category` — avoid loading every file.
2. Read the chosen `.md`; take the placeholder list from the frontmatter.
3. Substitute every `{{NAME}}` in the body:
   * use the caller-provided value, else the `default`, else (for a choice) the
     first `choices` entry;
   * resolve `{{PARAM_SUFFIX}}` and `{{PKG_NAME}}` per their rules;
   * a placeholder left with an empty value simply collapses to nothing.
4. The fenced code block's language tag indicates the target file type.
