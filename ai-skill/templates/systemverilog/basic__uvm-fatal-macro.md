---
id: "basic__uvm-fatal-macro"
source_file: "systemverilog/basic.snippets"
triggers: ["msg", "message"]
description: "UVM Fatal Macro"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "ID"
    tabstop: 1
    default: "ID"
  - name: "TAB_2"
    tabstop: 2
    default: "\"{{MESSAGE}}\""
  - name: "MESSAGE"
    tabstop: 3
    default: "message"
---

```systemverilog
`uvm_fatal("{{ID}}", {{TAB_2}})
```
