---
id: "scoreboard"
source_file: "systemverilog/scoreboard.snippets"
triggers: ["Scb", "Scoreboard"]
description: "UVM Scoreboard"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "SCOREBOARD"
    tabstop: 1
    default: "Scoreboard"
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
class {{SCOREBOARD}}{{PARAMS_2}} extends uvm_scoreboard;

    `uvm_component{{PARAM_SUFFIX}}_utils({{SCOREBOARD}}{{PARAMS_4}})

    //  variable definition
    typedef {{INTXN}}{{PARAMS_7}} ITXN;
    typedef {{OUTTXN}}{{PARAMS_10}} OTXN;

    {{CONFIG}}{{PARAMS_13}} {{CFG}};

    uvm_nonblocking_get_port #(ITXN) imon_getp;
    uvm_blocking_get_port #(OTXN) omon_getp;
    uvm_nonblocking_get_port #(OTXN) mdl_getp;

    int unsigned ref_latency = 0;

    function new(string name="{{SCOREBOARD}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_13}})::get(this, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{SCOREBOARD}}", "configuration is not set.")
        end
        ref_latency = {{CFG}}.ref_latency;

        imon_getp = new("imon_getp", this);
        omon_getp = new("omon_getp", this);
        mdl_getp = new("mdl_getp", this);
    endfunction

    task main_phase(uvm_phase phase);
        ITXN itxn;
        OTXN otxn;

        ITXN sti_itxn;
        OTXN exp_otxn;
        OTXN obs_otxn;

        forever begin
            obs_otxn = OTXN::type_id::create("obs_otxn");
            omon_getp.get(otxn);
            obs_otxn.copy(otxn);

            if (imon_getp.try_get(itxn)) begin
                sti_itxn = ITXN::type_id::create("sti_itxn");
                sti_itxn.copy(itxn);
            end
            else begin
                `uvm_fatal("{{SCOREBOARD}}", "no input for DUT output.")
            end

            if (mdl_getp.try_get(otxn)) begin
                exp_otxn = OTXN::type_id::create("exp_otxn");
                exp_otxn.copy(otxn);
            end
            else begin
                `uvm_fatal("{{SCOREBOARD}}", "no expected output for DUT output.")
            end

            value_check(sti_itxn, exp_otxn, obs_otxn);
            latency_check(sti_itxn, obs_otxn);
        end
    endtask

    function void value_check(const ref ITXN sti_itxn, const ref OTXN exp_otxn, const ref OTXN obs_otxn);
        bit txn_equal;

        txn_equal = exp_otxn.compare(obs_otxn);
        if (txn_equal) begin
            `uvm_info("{{SCOREBOARD}}", "expected output and actual output match.", UVM_MEDIUM)
        end
        else begin
            `uvm_error("{{SCOREBOARD}}", "expected output and actual output mismatch.")
        end

        if ((get_report_verbosity_level() == UVM_DEBUG) || (!txn_equal)) begin
            `uvm_info("{{SCOREBOARD}}", "DUT input:", UVM_NONE)
            sti_itxn.print();
            `uvm_info("{{SCOREBOARD}}", "DUT expected output:", UVM_NONE)
            exp_otxn.print();
            `uvm_info("{{SCOREBOARD}}", "DUT observed output:", UVM_NONE)
            obs_otxn.print();
        end
    endfunction

    function void latency_check(const ref ITXN sti_itxn, const ref OTXN obs_otxn);
        longint unsigned dut_latency;

        dut_latency = obs_otxn.timestamp - sti_itxn.timestamp;
        if (dut_latency == ref_latency) begin
            `uvm_info("{{SCOREBOARD}}", "DUT latency is as expected.", UVM_MEDIUM)
        end
        else begin
            `uvm_error("{{SCOREBOARD}}", "DUT latency is not as expected.")
            `uvm_info("{{SCOREBOARD}}", $sformatf("expected latency is %0d clocks.", ref_latency), UVM_NONE)
            `uvm_info("{{SCOREBOARD}}", $sformatf("actual latency is %0d clocks.", dut_latency), UVM_NONE)
        end
    endfunction
endclass
```
