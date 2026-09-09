---
id: "driver"
source_file: "systemverilog/driver.snippets"
triggers: ["Drv", "Driver"]
description: "UVM Driver"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "DRIVER"
    tabstop: 1
    default: "Driver"
  - name: "PARAMS_2"
    tabstop: 2
    default: " #(\n    {{TAB_3}}\n)"
  - name: "TAB_3"
    tabstop: 3
  - name: "TXN"
    tabstop: 4
    default: "Txn"
  - name: "PARAMS_5"
    tabstop: 5
    default: " #({{TAB_6}})"
  - name: "TAB_6"
    tabstop: 6
  - name: "CONFIG"
    tabstop: 7
    default: "Config"
  - name: "PARAMS_8"
    tabstop: 8
    default: " #({{TAB_9}})"
  - name: "TAB_9"
    tabstop: 9
  - name: "CFG"
    tabstop: 10
    default: "cfg"
  - name: "DUT_IF"
    tabstop: 11
    default: "dut_if"
  - name: "PARAMS_12"
    tabstop: 12
    default: " #({{TAB_13}})"
  - name: "TAB_13"
    tabstop: 13
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{DRIVER}}{{PARAMS_2}} extends uvm_driver #(.REQ ({{TXN}}));

    `uvm_component{{PARAM_SUFFIX}}_utils({{DRIVER}}{{PARAMS_5}})

    //  variable definition
    {{CONFIG}}{{PARAMS_8}} {{CFG}};

    virtual {{DUT_IF}}{{PARAMS_12}}.drv_mp vif;

    function new(string name="{{DRIVER}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_8}})::get(this, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{DRIVER}}", "configuration is not set.")
        end
        vif = {{CFG}}.vif;
    endfunction

    task reset_phase(uvm_phase phase);
        phase.raise_objection(this);
        phase.drop_objection(this);
    endtask

    task pre_main_phase(uvm_phase phase);
        phase.raise_objection(this);
        while(vif.rst_n !== 0) begin
            @vif.cb;
        end
        phase.drop_objection(this);
    endtask

    task main_phase(uvm_phase phase);
        forever begin
            seq_item_port.get_next_item(req);
            drive_req(req);
            seq_item_port.item_done();
        end
    endtask

    task drive_req(REQ txn);
    endtask
endclass
```
