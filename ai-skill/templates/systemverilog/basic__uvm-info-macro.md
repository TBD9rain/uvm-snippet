---
id: "basic__uvm-info-macro"
source_file: "systemverilog/basic.snippets"
triggers: ["msg", "message"]
description: "UVM Info Macro"
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
  - name: "TAB_4"
    tabstop: 4
    choices: ["NONE", "LOW", "MEDIUM", "HIGH", "FULL", "DEBUG"]
    default: "NONE"
---

```systemverilog
`uvm_info("{{ID}}", {{TAB_2}}, UVM_{{TAB_4}})
```
