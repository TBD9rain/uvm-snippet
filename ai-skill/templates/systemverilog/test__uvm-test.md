---
id: "test__uvm-test"
source_file: "systemverilog/test.snippets"
triggers: ["Test"]
description: "UVM Test"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "TEST"
    tabstop: 1
    default: "Test"
  - name: "CONFIG"
    tabstop: 2
    default: "Config"
  - name: "PARAMS_3"
    tabstop: 3
    default: " #({{TAB_4}})"
  - name: "TAB_4"
    tabstop: 4
  - name: "CFG"
    tabstop: 5
    default: "cfg"
  - name: "ENV"
    tabstop: 6
    default: "Env"
  - name: "PARAMS_7"
    tabstop: 7
    default: " #({{TAB_8}})"
  - name: "TAB_8"
    tabstop: 8
  - name: "SEQUENCE"
    tabstop: 9
    default: "Sequence"
  - name: "PARAMS_10"
    tabstop: 10
    default: " #({{TAB_11}})"
  - name: "TAB_11"
    tabstop: 11
---

```systemverilog
class {{TEST}} extends uvm_test;

    `uvm_component_utils({{TEST}})

    //  variable definition
    {{CONFIG}}{{PARAMS_3}} {{CFG}};

    {{ENV}}{{PARAMS_7}} env;

    function new(string name="{{TEST}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_3}})::get(this, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{TEST}}", "configuration is not set.")
        end
        uvm_config_db #({{CONFIG}}{{PARAMS_3}})::set(this, "env", "{{CFG}}", {{CFG}});

        env = {{ENV}}{{PARAMS_7}}::type_id::create("env", this);

        //  global timeout watchdog; 0 disables the timeout (runs until objections drop)
        uvm_root::get().set_timeout(0);
        //  simulation exit due to too many errors
        //  UVM 1.1d uses `get_server()`, UVM 1.1 uses `get()`
        uvm_report_server::get_server().set_max_quit_count(20);

        set_report_verbosity_level_hier(UVM_DEBUG);
    endfunction

    virtual task main_phase(uvm_phase phase);
        {{SEQUENCE}}{{PARAMS_10}} seq;

        phase.raise_objection(this);

        //  control sequence start
        seq = {{SEQUENCE}}{{PARAMS_10}}::type_id::create("seq");
        seq.start(env.i_agt.sqr);

        //  delay before drop objection
        phase.phase_done.set_drain_time(this, 1000ns);
        phase.drop_objection(this);
    endtask

    virtual function void report_phase(uvm_phase phase);
        uvm_report_server rpt_ser;
        int err_num;

        super.report_phase(phase);

        rpt_ser = get_report_server();
        err_num = rpt_ser.get_severity_count(UVM_ERROR);

        if (err_num) begin
            $write("\n");
            $write("============\n");
            $write("Test failed.\n");
            $write("============\n");
            $write("\n");
        end
        else begin
            $write("\n");
            $write("============\n");
            $write("Test passed.\n");
            $write("============\n");
            $write("\n");
        end
    endfunction
endclass
```
