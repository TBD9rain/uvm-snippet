---
id: "agent"
source_file: "systemverilog/agent.snippets"
triggers: ["Agent", "Agt"]
description: "UVM Agent"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "AGENT"
    tabstop: 1
    default: "Agent"
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
  - name: "SQR"
    tabstop: 13
    default: "Sqr"
  - name: "PARAMS_14"
    tabstop: 14
    default: " #({{TAB_15}})"
  - name: "TAB_15"
    tabstop: 15
  - name: "DRV"
    tabstop: 16
    default: "Drv"
  - name: "PARAMS_17"
    tabstop: 17
    default: " #({{TAB_18}})"
  - name: "TAB_18"
    tabstop: 18
  - name: "MON"
    tabstop: 19
    default: "Mon"
  - name: "PARAMS_20"
    tabstop: 20
    default: " #({{TAB_21}})"
  - name: "TAB_21"
    tabstop: 21
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{AGENT}}{{PARAMS_2}} extends uvm_agent;

    `uvm_component{{PARAM_SUFFIX}}_utils({{AGENT}}{{PARAMS_4}})

    //  variable definition
    typedef {{TXN}}{{PARAMS_7}} TXN;

    {{CONFIG}}{{PARAMS_10}} {{CFG}};

    {{SQR}}{{PARAMS_14}} sqr;
    {{DRV}}{{PARAMS_17}} drv;
    {{MON}}{{PARAMS_20}} mon;

    uvm_analysis_port #(TXN) ap;

    function new(string name="{{AGENT}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_10}})::get(this, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{AGENT}}", "configuration is not set.")
        end
        is_active = {{CFG}}.drv_en;

        if (is_active == UVM_ACTIVE) begin
            sqr = {{SQR}}{{PARAMS_14}}::type_id::create("sqr", this);
            drv = {{DRV}}{{PARAMS_17}}::type_id::create("drv", this);
            uvm_config_db #({{CONFIG}}{{PARAMS_10}})::set(this, "sqr", "{{CFG}}", {{CFG}});
            uvm_config_db #({{CONFIG}}{{PARAMS_10}})::set(this, "drv", "{{CFG}}", {{CFG}});
        end
        mon = {{MON}}{{PARAMS_20}}::type_id::create("mon", this);
        uvm_config_db #({{CONFIG}}{{PARAMS_10}})::set(this, "mon", "{{CFG}}", {{CFG}});
        ap = new("ap", this);
    endfunction

    function void connect_phase(uvm_phase phase);
        super.connect_phase(phase);

        if (is_active == UVM_ACTIVE) begin
            drv.seq_item_port.connect(sqr.seq_item_export);
        end
        mon.ap.connect(ap);
    endfunction
endclass
```
