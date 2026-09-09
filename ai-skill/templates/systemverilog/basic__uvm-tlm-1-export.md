---
id: "basic__uvm-tlm-1-export"
source_file: "systemverilog/basic.snippets"
triggers: ["export"]
description: "UVM TLM-1 Export"
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
  - name: "EXPORT"
    tabstop: 4
    default: "export"
---

```systemverilog
uvm{{TAB_1}}_{{TAB_2}}_export #({{INT}}) {{EXPORT}};
```
