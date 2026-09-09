---
id: "basic__singular-variable-field-automation-registry"
source_file: "systemverilog/basic.snippets"
triggers: ["field"]
description: "Singular Variable Field Automation Registry"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "TAB_1"
    tabstop: 1
    choices: ["int", "object", "string", "real", "event"]
    default: "int"
  - name: "ARG"
    tabstop: 2
    default: "arg"
  - name: "UVM_ALL_ON"
    tabstop: 3
    default: "UVM_ALL_ON"
---

```systemverilog
`uvm_field_{{TAB_1}}({{ARG}}, {{UVM_ALL_ON}})
```
