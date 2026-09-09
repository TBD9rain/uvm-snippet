---
id: "test__uvm-test-to-extend"
source_file: "systemverilog/test.snippets"
triggers: ["Test"]
description: "UVM Test to Extend"
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
  - name: "SEQUENCE"
    tabstop: 3
    default: "Sequence"
  - name: "PARAMS_4"
    tabstop: 4
    default: " #({{TAB_5}})"
  - name: "TAB_5"
    tabstop: 5
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

        set_report_verbosity_level_hier(UVM_LOW);
    endfunction

    virtual task main_phase(uvm_phase phase);
        {{SEQUENCE}}{{PARAMS_4}} seq;

        phase.raise_objection(this);

        //  control sequence start
        seq = {{SEQUENCE}}{{PARAMS_4}}::type_id::create("seq");
        seq.start(env.i_agt.sqr);

        //  delay before drop objection
        phase.phase_done.set_drain_time(this, 1000ns);
        phase.drop_objection(this);
    endtask
endclass
```
