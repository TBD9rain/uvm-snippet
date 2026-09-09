---
id: "basic__rand-variable-definition"
source_file: "systemverilog/basic.snippets"
triggers: ["rand "]
description: "rand variable definition"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "VAR_NAME"
    tabstop: 0
    default: "var_name"
  - name: "TAB_1"
    tabstop: 1
    default: "[{{TAB_2}}: 0]"
  - name: "TAB_2"
    tabstop: 2
    default: " 7"
---

```systemverilog
rand bit {{TAB_1}} {{VAR_NAME}};
```
