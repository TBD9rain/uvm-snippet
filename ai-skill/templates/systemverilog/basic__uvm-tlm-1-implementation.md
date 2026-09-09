---
id: "basic__uvm-tlm-1-implementation"
source_file: "systemverilog/basic.snippets"
triggers: ["imp"]
description: "UVM TLM-1 Implementation"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "TAB_1"
    tabstop: 1
    choices: ["", "_blocking", "_nonblocking"]
    default: ""
  - name: "TAB_2"
    tabstop: 2
    choices: ["put", "get", "peek", "get_peek"]
    default: "put"
  - name: "INT"
    tabstop: 3
    default: "int"
  - name: "CLASS"
    tabstop: 4
    default: "class"
  - name: "IMP"
    tabstop: 5
    default: "imp"
---

```systemverilog
uvm{{TAB_1}}_{{TAB_2}}_imp #({{INT}}, {{CLASS}}) {{IMP}};
```
