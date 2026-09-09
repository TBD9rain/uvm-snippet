---
id: "faultinjector"
source_file: "systemverilog/faultinjector.snippets"
triggers: ["FaultInjector", "FI"]
description: "Fault Injector"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "FAULTINJECTOR"
    tabstop: 1
    default: "FaultInjector"
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
class {{FAULTINJECTOR}}{{PARAMS_2}} extends uvm_component;

    `uvm_component{{PARAM_SUFFIX}}_utils({{FAULTINJECTOR}}{{PARAMS_4}})

    //  variable definition
    typedef {{TXN}}{{PARAMS_7}} TXN;

    uvm_analysis_imp #(TXN, {{FAULTINJECTOR}}{{PARAMS_4}}) imp;
    uvm_analysis_port #(TXN) ap;

    function new(string name="{{FAULTINJECTOR}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        imp = new("imp", this);
        ap = new("ap", this);
    endfunction

    virtual function void fault_inject(TXN txn);
    endfunction

    virtual function void write(TXN txn);
        TXN insert_txn;

        insert_txn = TXN::type_id::create("insert_txn");
        insert_txn.copy(txn);

        fault_inject(insert_txn);

        ap.write(insert_txn);
    endfunction
endclass
```
