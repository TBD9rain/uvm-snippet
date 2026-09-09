---
id: "basic__associated-array-field-automation-registry"
source_file: "systemverilog/basic.snippets"
triggers: ["field"]
description: "Associated Array Field Automation Registry"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "VALUE_TYPE"
    tabstop: 1
    default: "value_type"
  - name: "KEY_TYPE"
    tabstop: 2
    default: "key_type"
  - name: "ARG"
    tabstop: 3
    default: "arg"
  - name: "UVM_ALL_ON"
    tabstop: 4
    default: "UVM_ALL_ON"
---

```systemverilog
`uvm_field_aa_{{VALUE_TYPE}}_{{KEY_TYPE}}({{ARG}}, {{UVM_ALL_ON}})
```
