---
id: "basic__uvm-tlm-1-analysis-communication"
source_file: "systemverilog/basic.snippets"
triggers: ["analysis"]
description: "UVM TLM-1 Analysis Communication"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "TAB_1"
    tabstop: 1
    choices: ["port", "export"]
    default: "port"
  - name: "INT"
    tabstop: 2
    default: "int"
  - name: "AP"
    tabstop: 3
    default: "ap"
---

```systemverilog
uvm_analysis_{{TAB_1}} #({{INT}}) {{AP}};
```
