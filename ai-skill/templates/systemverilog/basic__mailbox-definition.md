---
id: "basic__mailbox-definition"
source_file: "systemverilog/basic.snippets"
triggers: ["mailbox "]
description: "mailbox definition"
category: systemverilog
ultisnips_flags: "rbA"
author: "TBD9rain"
placeholders:
  - name: "MB_NAME"
    tabstop: 0
    default: "mb_name"
  - name: "DATA_TYPE"
    tabstop: 1
    default: "data_type"
---

```systemverilog
mailbox #({{DATA_TYPE}}) {{MB_NAME}};
```
