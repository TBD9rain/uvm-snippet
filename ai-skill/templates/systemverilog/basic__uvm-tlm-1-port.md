---
id: "basic__uvm-tlm-1-port"
source_file: "systemverilog/basic.snippets"
triggers: ["port"]
description: "UVM TLM-1 Port"
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
  - name: "PORT"
    tabstop: 4
    default: "port"
---

```systemverilog
uvm{{TAB_1}}_{{TAB_2}}_port #({{INT}}) {{PORT}};
```
