---
id: "basic__uvm-component"
source_file: "systemverilog/basic.snippets"
triggers: ["class"]
description: "UVM Component"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "COMPONENT"
    tabstop: 1
    default: "Component"
  - name: "PARAMS_2"
    tabstop: 2
    default: " #(\n    {{TAB_3}}\n)"
  - name: "TAB_3"
    tabstop: 3
  - name: "PARAMS_4"
    tabstop: 4
    default: " #({{TAB_5}})"
  - name: "TAB_5"
    tabstop: 5
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{COMPONENT}}{{PARAMS_2}} extends uvm_component;

    `uvm_component{{PARAM_SUFFIX}}_utils({{COMPONENT}}{{PARAMS_4}})

    //----------
    //  Variable
    //----------



    //--------
    //  Method
    //--------

    function new(string name="{{COMPONENT}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction
endclass
```
