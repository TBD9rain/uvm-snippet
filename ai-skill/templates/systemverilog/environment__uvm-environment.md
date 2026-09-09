---
id: "environment__uvm-environment"
source_file: "systemverilog/environment.snippets"
triggers: ["Env(ironment)?"]
description: "UVM Environment"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "ENVIRONMENT"
    tabstop: 1
    default: "Environment"
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
  - name: "INAGT"
    tabstop: 16
    default: "InAgt"
  - name: "PARAMS_17"
    tabstop: 17
    default: " #({{TAB_18}})"
  - name: "TAB_18"
    tabstop: 18
  - name: "OUTAGT"
    tabstop: 19
    default: "OutAgt"
  - name: "PARAMS_20"
    tabstop: 20
    default: " #({{TAB_21}})"
  - name: "TAB_21"
    tabstop: 21
  - name: "COV"
    tabstop: 22
    default: "Cov"
  - name: "PARAMS_23"
    tabstop: 23
    default: " #({{TAB_24}})"
  - name: "TAB_24"
    tabstop: 24
  - name: "MDL"
    tabstop: 25
    default: "Mdl"
  - name: "PARAMS_26"
    tabstop: 26
    default: " #({{TAB_27}})"
  - name: "TAB_27"
    tabstop: 27
  - name: "SCB"
    tabstop: 28
    default: "Scb"
  - name: "PARAMS_29"
    tabstop: 29
    default: " #({{TAB_30}})"
  - name: "TAB_30"
    tabstop: 30
  - name: "SCBFI"
    tabstop: 31
    default: "ScbFI"
  - name: "PARAMS_32"
    tabstop: 32
    default: " #({{TAB_33}})"
  - name: "TAB_33"
    tabstop: 33
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{ENVIRONMENT}}{{PARAMS_2}} extends uvm_env;

    `uvm_component{{PARAM_SUFFIX}}_utils({{ENVIRONMENT}}{{PARAMS_4}})

    //  variable definition
    typedef {{INTXN}}{{PARAMS_7}} ITXN;
    typedef {{OUTTXN}}{{PARAMS_10}} OTXN;

    {{CONFIG}}{{PARAMS_13}} {{CFG}};

    {{INAGT}}{{PARAMS_17}} i_agt;
    {{OUTAGT}}{{PARAMS_20}} o_agt;
    {{COV}}{{PARAMS_23}} cov;
    {{MDL}}{{PARAMS_26}} mdl;
    {{SCB}}{{PARAMS_29}} scb;
    {{SCBFI}}{{PARAMS_32}} fi;

    bit scb_en = 0;
    bit fault_inject_en = 0;
    bit cov_en = 0;
    int unsigned ref_latency = 0;

    uvm_tlm_analysis_fifo #(ITXN) cov_sti_fifo;
    uvm_tlm_analysis_fifo #(ITXN) mdl_sti_fifo;
    uvm_tlm_analysis_fifo #(ITXN) scb_sti_fifo;
    uvm_tlm_analysis_fifo #(OTXN) scb_obs_fifo;
    uvm_tlm_fifo #(OTXN) scb_exp_fifo;

    function new(string name="{{ENVIRONMENT}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_13}})::get(this, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{ENVIRONMENT}}", "configuration is not set.")
        end
        scb_en = {{CFG}}.scb_en;
        fault_inject_en = {{CFG}}.fault_inject_en;
        cov_en = {{CFG}}.cov_en;
        ref_latency = {{CFG}}.ref_latency;

        i_agt = {{INAGT}}{{PARAMS_17}}::type_id::create("i_agt", this);
        uvm_config_db #({{CONFIG}}{{PARAMS_13}})::set(this, "i_agt", "{{CFG}}", {{CFG}});

        if (cov_en) begin
            cov = {{COV}}{{PARAMS_23}}::type_id::create("cov", this);
            cov_sti_fifo = new("cov_sti_fifo", this);
        end

        o_agt = {{OUTAGT}}{{PARAMS_20}}::type_id::create("o_agt", this);
        uvm_config_db #({{CONFIG}}{{PARAMS_13}})::set(this, "o_agt", "{{CFG}}", {{CFG}});

        if (!scb_en) begin
            return;
        end

        mdl = {{MDL}}{{PARAMS_26}}::type_id::create("mdl", this);
        scb = {{SCB}}{{PARAMS_29}}::type_id::create("scb", this);
        uvm_config_db #({{CONFIG}}{{PARAMS_13}})::set(this, "mdl", "{{CFG}}", {{CFG}});
        uvm_config_db #({{CONFIG}}{{PARAMS_13}})::set(this, "scb", "{{CFG}}", {{CFG}});

        if (fault_inject_en) begin
            fi = {{SCBFI}}{{PARAMS_32}}::type_id::create("fi", this);
        end

        mdl_sti_fifo = new("mdl_sti_fifo", this);
        scb_sti_fifo = new("scb_sti_fifo", this);
        scb_obs_fifo = new("scb_obs_fifo", this);
        scb_exp_fifo = new("scb_exp_fifo", this, ref_latency);
    endfunction

    function void connect_phase(uvm_phase phase);
        super.connect_phase(phase);

        if (cov_en) begin
            i_agt.ap.connect(cov_sti_fifo.analysis_export);
            cov.imon_getp.connect(cov_sti_fifo.blocking_get_export);
        end

        if (!scb_en) begin
            return;
        end

        i_agt.ap.connect(mdl_sti_fifo.analysis_export);
        mdl.imon_getp.connect(mdl_sti_fifo.blocking_get_export);

        i_agt.ap.connect(scb_sti_fifo.analysis_export);
        scb.imon_getp.connect(scb_sti_fifo.nonblocking_get_export);

        if (fault_inject_en) begin
            o_agt.ap.connect(fi.imp);
            fi.ap.connect(scb_obs_fifo.analysis_export);
        end
        else begin
            o_agt.ap.connect(scb_obs_fifo.analysis_export);
        end
        scb.omon_getp.connect(scb_obs_fifo.blocking_get_export);

        mdl.scb_putp.connect(scb_exp_fifo.blocking_put_export);
        scb.mdl_getp.connect(scb_exp_fifo.nonblocking_get_export);
    endfunction
endclass
```
