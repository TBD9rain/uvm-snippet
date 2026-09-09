---
id: "basic__singular-enum-field-automation-registry"
source_file: "systemverilog/basic.snippets"
triggers: ["field"]
description: "Singular Enum Field Automation Registry"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "ENUM_TYPE"
    tabstop: 1
    default: "enum_type"
  - name: "ARG"
    tabstop: 2
    default: "arg"
  - name: "UVM_ALL_ON"
    tabstop: 3
    default: "UVM_ALL_ON"
---

```systemverilog
`uvm_field_enum({{ENUM_TYPE}}, {{ARG}}, {{UVM_ALL_ON}})
```
