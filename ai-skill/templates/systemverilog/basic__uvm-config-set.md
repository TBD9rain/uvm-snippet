---
id: "basic__uvm-config-set"
source_file: "systemverilog/basic.snippets"
triggers: ["config"]
description: "UVM Config Set"
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
  - name: "HIER_PATH"
    tabstop: 3
    default: "hier_path"
  - name: "VAR_NAME"
    tabstop: 4
    default: "var_name"
---

```systemverilog
uvm_config_db #({{INT}})::set({{TAB_2}}, "{{HIER_PATH}}", "{{VAR_NAME}}", {{VAR_NAME}});
```
