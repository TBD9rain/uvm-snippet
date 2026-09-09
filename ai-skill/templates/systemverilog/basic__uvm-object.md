---
id: "basic__uvm-object"
source_file: "systemverilog/basic.snippets"
triggers: ["class"]
description: "UVM Object"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "OBJECT"
    tabstop: 1
    default: "Object"
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
class {{OBJECT}}{{PARAMS_2}} extends uvm_object;

    `uvm_object{{PARAM_SUFFIX}}_utils({{OBJECT}}{{PARAMS_4}})

    //----------
    //  Variable
    //----------



    //--------
    //  Method
    //--------

    function new(string name="{{OBJECT}}");
        super.new(name);
    endfunction
endclass
```
