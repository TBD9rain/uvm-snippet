---
id: "test__uvm-test-to-verify-scoreboard"
source_file: "systemverilog/test.snippets"
triggers: ["Test"]
description: "UVM Test to Verify Scoreboard"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "TEST"
    tabstop: 1
    default: "Test"
  - name: "BASETEST"
    tabstop: 2
    default: "BaseTest"
  - name: "CFG"
    tabstop: 3
    default: "cfg"
---

```systemverilog
class {{TEST}} extends {{BASETEST}};

    `uvm_component_utils({{TEST}})

    //  variable definition
    function new(string name="{{TEST}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        {{CFG}}.fault_inject_en = 1;

        //  simulation exit due to too many errors
        uvm_report_server::get_server().set_max_quit_count(0);
        set_report_verbosity_level_hier(UVM_LOW);
    endfunction

    virtual function void report_phase(uvm_phase phase);
        uvm_report_server rpt_ser;
        int err_num;

        rpt_ser = get_report_server();
        err_num = rpt_ser.get_severity_count(UVM_ERROR);

        if (err_num == 0) begin
            $write("\n");
            $write("=======================\n");
            $write("Scoreboard Test failed.\n");
            $write("=======================\n");
            $write("\n");
        end
        else begin
            $write("\n");
            $write("==========================\n");
            $write("Scoreboard Test completed.\n");
            $write("==========================\n");
            $write("\n");
        end
    endfunction
endclass
```
