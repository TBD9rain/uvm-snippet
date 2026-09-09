---
id: "basic__bind-construct"
source_file: "systemverilog/basic.snippets"
triggers: ["bind"]
description: "bind construct"
category: systemverilog
ultisnips_flags: "rbA"
author: "TBD9rain"
placeholders:
  - name: "TARGET_INST_HIER_PATH"
    tabstop: 1
    default: "target_inst_hier_path"
  - name: "BIND_ELEMENT"
    tabstop: 2
    default: "bind_element"
  - name: "PARAMS_3"
    tabstop: 3
    default: " #({{TAB_4}})"
  - name: "TAB_4"
    tabstop: 4
  - name: "TAB_5"
    tabstop: 5
  - name: "TAB_6"
    tabstop: 6
    default: " (\n\n)"
---

```systemverilog
bind $root.{{TARGET_INST_HIER_PATH}} {{BIND_ELEMENT}}{{PARAMS_3}} {{TAB_5}}{{TAB_6}};
```
