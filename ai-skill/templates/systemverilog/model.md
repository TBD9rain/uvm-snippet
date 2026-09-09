---
id: "model"
source_file: "systemverilog/model.snippets"
triggers: ["Mdl", "RefMdl", "Model", "ReferenceModel"]
description: "UVM Reference Model"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "MODEL"
    tabstop: 1
    default: "Model"
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
  - name: "INTXN"
    tabstop: 6
    default: "InTxn"
  - name: "PARAMS_7"
    tabstop: 7
    default: " #({{TAB_8}})"
  - name: "TAB_8"
    tabstop: 8
  - name: "OUTTXN"
    tabstop: 9
    default: "OutTxn"
  - name: "PARAMS_10"
    tabstop: 10
    default: " #({{TAB_11}})"
  - name: "TAB_11"
    tabstop: 11
  - name: "CONFIG"
    tabstop: 12
    default: "Config"
  - name: "PARAMS_13"
    tabstop: 13
    default: " #({{TAB_14}})"
  - name: "TAB_14"
    tabstop: 14
  - name: "CFG"
    tabstop: 15
    default: "cfg"
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{MODEL}}{{PARAMS_2}} extends uvm_component;

    `uvm_component{{PARAM_SUFFIX}}_utils({{MODEL}}{{PARAMS_4}})

    //  variable definition
    typedef {{INTXN}}{{PARAMS_7}} ITXN;
    typedef {{OUTTXN}}{{PARAMS_10}} OTXN;

    {{CONFIG}}{{PARAMS_13}} {{CFG}};

    uvm_blocking_get_port #(ITXN) imon_getp;
    uvm_blocking_put_port #(OTXN) scb_putp;

    function new(string name="{{MODEL}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_13}})::get(this, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{MODEL}}", "configuration is not set.")
        end

        imon_getp = new("imon_getp", this);
        scb_putp = new("scb_putp", this);
    endfunction

    task main_phase(uvm_phase phase);
        ITXN mon_txn;
        OTXN exp_txn;

        forever begin
            imon_getp.get(mon_txn);
            ref_proc(mon_txn, exp_txn);
            scb_putp.put(exp_txn);
        end
    endtask

    task ref_proc(
        const ref ITXN in_txn,
        output OTXN out_txn);

        out_txn = OTXN::type_id::create("out_txn");
    endtask
endclass
```
