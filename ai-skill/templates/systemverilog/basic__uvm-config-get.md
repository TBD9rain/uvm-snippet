---
id: "basic__uvm-config-get"
source_file: "systemverilog/basic.snippets"
triggers: ["config"]
description: "UVM Config Get"
category: systemverilog
ultisnips_flags: "w"
author: "TBD9rain"
placeholders:
  - name: "INT"
    tabstop: 1
    default: "int"
  - name: "TAB_2"
    tabstop: 2
    choices: ["this", "null"]
    default: "this"
  - name: "VAR_NAME"
    tabstop: 3
    default: "var_name"
---

```systemverilog
uvm_config_db #({{INT}})::get({{TAB_2}}, "", "{{VAR_NAME}}", {{VAR_NAME}});
```
