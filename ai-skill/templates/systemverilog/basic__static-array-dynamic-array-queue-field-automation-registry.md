---
id: "basic__static-array-dynamic-array-queue-field-automation-registry"
source_file: "systemverilog/basic.snippets"
triggers: ["field"]
description: "Static Array/Dynamic Array/Queue Field Automation Registry"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "TAB_1"
    tabstop: 1
    choices: ["sarray", "array", "queue"]
    default: "sarray"
  - name: "TAB_2"
    tabstop: 2
    choices: ["int", "object", "string"]
    default: "int"
  - name: "ARG"
    tabstop: 3
    default: "arg"
  - name: "UVM_ALL_ON"
    tabstop: 4
    default: "UVM_ALL_ON"
---

```systemverilog
`uvm_field_{{TAB_1}}_{{TAB_2}}({{ARG}}, {{UVM_ALL_ON}})
```
