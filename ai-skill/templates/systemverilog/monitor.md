---
id: "monitor"
source_file: "systemverilog/monitor.snippets"
triggers: ["Mon(itor)?"]
description: "UVM Monitor"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "MONITOR"
    tabstop: 1
    default: "Monitor"
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
  - name: "CONFIG"
    tabstop: 9
    default: "Config"
  - name: "PARAMS_10"
    tabstop: 10
    default: " #({{TAB_11}})"
  - name: "TAB_11"
    tabstop: 11
  - name: "CFG"
    tabstop: 12
    default: "cfg"
  - name: "DUT_IF"
    tabstop: 13
    default: "dut_if"
  - name: "PARAMS_14"
    tabstop: 14
    default: " #({{TAB_15}})"
  - name: "TAB_15"
    tabstop: 15
  - name: "TAB_16"
    tabstop: 16
    default: "vif.valid !== 1'b1"
  - name: "TAB_17"
    tabstop: 17
    choices: ["posedge", "negedge"]
    default: "posedge"
  - name: "TAB_18"
    tabstop: 18
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{MONITOR}}{{PARAMS_2}} extends uvm_monitor;

    `uvm_component{{PARAM_SUFFIX}}_utils({{MONITOR}}{{PARAMS_4}})

    //  variable definition
    typedef {{TXN}}{{PARAMS_7}} TXN;

    {{CONFIG}}{{PARAMS_10}} {{CFG}};

    virtual {{DUT_IF}}{{PARAMS_14}}.mon_mp vif;

    uvm_analysis_port #(TXN) ap;

    function new(string name="{{MONITOR}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_10}})::get(this, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{MONITOR}}", "configuration is not set.")
        end
        vif = {{CFG}}.vif;

        ap = new("ap", this);
    endfunction

    task main_phase(uvm_phase phase);
        TXN txn;

        forever begin
            sample_txn(txn);
            ap.write(txn);
        end
    endtask

    task sample_txn;
        output TXN txn;

        txn = TXN::type_id::create("txn");

        //  sample until the condition holds (use "===" / "!==")
        while ({{TAB_16}}) begin
            @({{TAB_17}} vif.clk);
        end
        txn.timestamp = vif.clk_cnt;
        @({{TAB_18}} vif.clk);
    endtask
endclass
```
