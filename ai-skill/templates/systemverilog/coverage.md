---
id: "coverage"
source_file: "systemverilog/coverage.snippets"
triggers: ["Cov(Col|erageCollector)?"]
description: "UVM Coverage Collector"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "COVERAGECOLLECTOR"
    tabstop: 1
    default: "CoverageCollector"
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
  - name: "TXN"
    tabstop: 6
    default: "Txn"
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{COVERAGECOLLECTOR}}{{PARAMS_2}} extends uvm_component;

    `uvm_component{{PARAM_SUFFIX}}_utils({{COVERAGECOLLECTOR}}{{PARAMS_4}})

    typedef {{TXN}} T;

    //  variable definition
    uvm_blocking_get_port #(T) imon_getp;
    T tc_txn;

    //  coverage group definition
    

    function new(string name="{{COVERAGECOLLECTOR}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        imon_getp = new("imon_getp", this);
    endfunction

    task main_phase(uvm_phase phase);
        forever begin
            imon_getp.get(tc_txn);
        end
    endtask
endclass
```
