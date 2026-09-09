---
id: "config"
source_file: "systemverilog/config.snippets"
triggers: ["Cfg", "Config"]
description: "UVM Configuration Object"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "CONFIG"
    tabstop: 1
    default: "Config"
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
  - name: "DUT_IF"
    tabstop: 6
    default: "dut_if"
  - name: "PARAMS_7"
    tabstop: 7
    default: " #({{TAB_8}})"
  - name: "TAB_8"
    tabstop: 8
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{CONFIG}}{{PARAMS_2}} extends uvm_object;

    `uvm_object{{PARAM_SUFFIX}}_utils({{CONFIG}}{{PARAMS_4}})

    //----------
    //  Variable
    //----------

    //  virtual interface
    virtual {{DUT_IF}}{{PARAMS_7}} vif;

    //  drive enable
    uvm_active_passive_enum drv_en = UVM_ACTIVE;

    //  result check enable
    bit scb_en = 0;

    //  fault inject enable
    bit fault_inject_en = 0;

    //  coverage collect enable
    bit cov_en = 0;

    //  reference latency
    int unsigned ref_latency = 0;


    //--------
    //  Method
    //--------

    function new(string name="{{CONFIG}}");
        super.new(name);
    endfunction
endclass
```
