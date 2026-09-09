---
id: "basic__uvm-tlm-1-fifo"
source_file: "systemverilog/basic.snippets"
triggers: ["fifo"]
description: "UVM TLM-1 FIFO"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "ANALYSIS"
    tabstop: 1
    default: "_analysis"
  - name: "INT"
    tabstop: 2
    default: "int"
  - name: "FIFO"
    tabstop: 3
    default: "fifo"
---

```systemverilog
uvm_tlm{{ANALYSIS}}_fifo #({{INT}}) {{FIFO}};
```
