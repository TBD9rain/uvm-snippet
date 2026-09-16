# uvm-snippet

A [UltiSnips](https://github.com/SirVer/ultisnips) snippet library for building
**UVM (Universal Verification Methodology)** testbenches in SystemVerilog, plus
companion snippets for QuestaSim simulation/report scripts and a Makefile-driven
simulation flow.

The snippets expand into ready-to-fill skeletons for every layer of a UVM
environment — transactions, sequences, drivers, monitors, agents, scoreboards,
reference models, coverage collectors, environments and tests — so a complete,
consistently-structured testbench can be scaffolded in minutes.

The same library is also published in an AI-friendly form under
[`ai-skill/`](ai-skill/), so an AI agent (or any tool) can scaffold the same
testbench programmatically without interpreting Vim/UltiSnips expansion
semantics. See [AI-friendly templates](#ai-friendly-templates-ai-skill) below.

## Features

- **Full UVM component set** — one snippet per verification component, all
  following a single naming and structure convention.
- **Building-block macros** — TLM-1 ports/exports/imps, `uvm_config_db` get/set,
  factory `create`, field-automation macros and `uvm_info/warning/error/fatal`
  reporting.
- **General SystemVerilog helpers** — class/interface skeletons, `rand`/`randc`
  variables, `mailbox`, `fork`/`for`/`assert`, `function`/`task`, functional
  coverage (`covergroup`/`coverpoint`/`cross`/`bins`) and `bind`.
- **Simulation flow** — QuestaSim UVM simulation and report `tcl` scripts and a
  QuestaSim 2026.2 Makefile (Windows).

## Requirements

- [Vim](https://www.vim.org/) (or Neovim) with the
  [UltiSnips](https://github.com/SirVer/ultisnips) plugin installed.
- A completion/trigger key configured for UltiSnips (see `:help UltiSnips`).

## Installation

UltiSnips loads snippet files from directories listed in
`g:UltiSnipsSnippetDirectories`. Point it at (or symlink/copy this repository
into) one of those directories. For example:

```vim
" Load snippets from a custom directory
let g:UltiSnipsSnippetDirectories = ['UltiSnips', 'path/to/uvm-snippet/ultisnips']
```

The UltiSnips sources live under `ultisnips/`, grouped by filetype directory
(`systemverilog/`, `tcl/`) plus the top-level Makefile snippets
(`make.snippets`), matching UltiSnips' per-filetype loading. The SystemVerilog
snippets `extends verilog`, so any Verilog snippets in your setup remain
available.

## Repository Structure

```
uvm-snippet/
├── ultisnips/                  UltiSnips sources (Vim)
│   ├── systemverilog/          SystemVerilog / UVM snippets (one file per component)
│   ├── tcl/                    QuestaSim simulation & report script snippets
│   └── make.snippets           QuestaSim UVM simulation Makefile
└── ai-skill/                   AI-friendly, generated form of the same library
    ├── script/                 convert_ultisnips.py (UltiSnips → Markdown converter)
    └── templates/              generated Markdown templates + manifest.json
```

### SystemVerilog snippets (`systemverilog/`)

| File                   | Trigger(s)                         | Provides |
| ---------------------- | ---------------------------------- | -------- |
| `basic.snippets`       | `class`, `port`, `imp`, `config`, `field`, `msg`, `function`, `covergroup`, `bind`, … | UVM class/object skeletons, TLM-1 communication, `uvm_config_db`, factory create, field-automation macros, message macros, and general SystemVerilog constructs |
| `interface.snippets`   | `interface`                        | Interface with clocking block and driver/monitor/DUT modports |
| `package.snippets`     | `package` / `pkg`                  | UVM component package with ordered component includes and the sequencer specialization |
| `transaction.snippets` | `Txn` / `Transaction`, `do_`       | Transaction item plus `do_copy`/`do_compare`/`convert2string`/`do_print` reloads |
| `sequence.snippets`    | `Seq` / `Sequence`                 | UVM sequence and virtual sequence |
| `sequencer.snippets`   | `Sqr` / `Sequencer`                | Sequencer as an extended class or as a type specialization (typedef), plus a virtual sequencer |
| `driver.snippets`      | `Drv` / `Driver`                   | UVM driver |
| `monitor.snippets`     | `Mon` / `Monitor`                  | UVM monitor |
| `agent.snippets`       | `Agt` / `Agent`                    | UVM agent |
| `model.snippets`       | `Mdl` / `RefMdl` / `Model`         | UVM reference model |
| `scoreboard.snippets`  | `Scb` / `Scoreboard`               | UVM scoreboard |
| `faultinjector.snippets` | `FI` / `FaultInjector`           | Fault injector component |
| `coverage.snippets`    | `Cov` / `CoverageCollector`        | UVM coverage collector |
| `config.snippets`      | `Cfg` / `Config`                   | UVM configuration object |
| `environment.snippets` | `Env` / `Environment`              | UVM environment and integrated environment |
| `test.snippets`        | `Test`                             | UVM test, extendable base test, and scoreboard-verification test |
| `testbench.snippets`   | `testbench`                        | Top-level UVM testbench module |

### Simulation snippets (`tcl/`, `make.snippets`)

| File                          | Trigger      | Provides |
| ----------------------------- | ------------ | -------- |
| `tcl/questa_2024.2_sim.snippets` | `simulate` | QuestaSim 2024.2.1 UVM simulation script |
| `tcl/questa_10.6c_sim.snippets`  | `simulate` | QuestaSim 10.6c UVM simulation script |
| `tcl/questa_rpt.snippets`        | `report`   | QuestaSim UVM report script |
| `make.snippets`                  | `makefile` | QuestaSim 2026.2 UVM simulation Makefile (Windows) |

## Component Naming Convention

The component snippets and the `package` snippet share one short-name convention,
so a generated package wires the pieces together out of the box:

| Short name | Component            |
| ---------- | -------------------- |
| `Config`   | Configuration object |
| `Txn`      | Transaction          |
| `Sqr`      | Sequencer (extended class in its own file, or a typedef in the package) |
| `Drv`      | Driver               |
| `Mon`      | Monitor              |
| `Agt`      | Agent                |
| `RefMdl`   | Reference model      |
| `Scb`      | Scoreboard           |
| `ScbFI`    | Scoreboard fault injector |
| `Cov`      | Coverage collector   |
| `Env`      | Environment          |
| `Seq`      | Sequence             |
| `Test`     | Test                 |

## Usage

1. Open a SystemVerilog source file (or a `tcl`/Makefile for the simulation
   snippets).
2. Type a snippet trigger (for example `Drv` for a driver, or `Txn` for a
   transaction) and expand it with your UltiSnips trigger key.
3. Tab through the placeholders to fill in names, parameters and body.

A typical bottom-up flow: scaffold the `interface`, then `Txn` → `Sqr`/`Seq` →
`Drv`/`Mon` → `Agt` → `RefMdl`/`Scb`/`Cov` → `Env` → `Test`, collect them with the
`package` snippet, wrap everything in a `testbench` top module, and drive it with
the QuestaSim `simulate`/`report` scripts or the generated Makefile.

## AI-friendly templates (`ai-skill/`)

The `ai-skill/` directory holds an AI-consumable form of the exact same library.
It exists so that an AI agent, or any non-Vim tool, can read a template,
understand its customisation points from structured metadata, and fill them in —
without having to interpret UltiSnips expansion semantics.

```
ai-skill/
├── script/
│   └── convert_ultisnips.py   UltiSnips → Markdown converter
└── templates/
    ├── FORMAT.md              full description of the template format
    ├── manifest.json          index of every generated template
    ├── systemverilog/*.md     one file per SystemVerilog snippet block
    ├── tcl/*.md               QuestaSim TCL flow templates
    └── make/*.md              Makefile template
```

Key points:

- **Generated, not hand-written.** Every file under `ai-skill/templates/` is
  produced from the `ultisnips/*.snippets` sources. The `ultisnips/` files remain
  the single source of truth; do not edit generated templates by hand.
- **One block, one file.** Each snippet block becomes one Markdown file: YAML
  frontmatter (triggers, description, category, and an ordered list of
  placeholders) followed by a single fenced code block whose customisation points
  use a uniform `{{PLACEHOLDER}}` marker syntax.
- **`manifest.json` is the index.** A tool can locate templates by `id`,
  `triggers` or `category` from the manifest, then read only the files it needs
  rather than loading every template.

To regenerate the templates after changing a `.snippets` source or the converter,
run from the repository root:

```sh
python ai-skill/script/convert_ultisnips.py
```

For the complete format specification — placeholder naming rules, derived
placeholders, and how to fill a template — see
[`ai-skill/templates/FORMAT.md`](ai-skill/templates/FORMAT.md).

## Author

TBD9rain

---

*This repository is a snippet collection — a Vim/UltiSnips form under `ultisnips/`
and an AI-friendly form under `ai-skill/`; it does not itself compile or simulate
any RTL. The generated code targets the UVM class library and, for the simulation
flow, Siemens QuestaSim.*
