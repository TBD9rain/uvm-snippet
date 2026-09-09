---
id: "sequence__uvm-virtual-sequence"
source_file: "systemverilog/sequence.snippets"
triggers: ["Seq(uence)?"]
description: "UVM Virtual Sequence"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "VIRTUALSEQUENCE"
    tabstop: 1
    default: "VirtualSequence"
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
  - name: "SEQUENCER"
    tabstop: 6
    default: "Sequencer"
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
  - name: "SEQ0"
    tabstop: 13
    default: "Seq0"
  - name: "PARAMS_14"
    tabstop: 14
    default: " #({{TAB_15}})"
  - name: "TAB_15"
    tabstop: 15
  - name: "SEQ0_16"
    tabstop: 16
    default: "seq0"
  - name: "SEQ1"
    tabstop: 17
    default: "Seq1"
  - name: "PARAMS_18"
    tabstop: 18
    default: " #({{TAB_19}})"
  - name: "TAB_19"
    tabstop: 19
  - name: "SEQ1_20"
    tabstop: 20
    default: "seq1"
  - name: "SQR0"
    tabstop: 21
    default: "sqr0"
  - name: "SQR1"
    tabstop: 22
    default: "sqr1"
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{VIRTUALSEQUENCE}}{{PARAMS_2}} extends uvm_sequence;

    `uvm_object{{PARAM_SUFFIX}}_utils({{VIRTUALSEQUENCE}}{{PARAMS_4}})

    //  handler to sequencer
    `uvm_declare_p_sequencer({{SEQUENCER}}{{PARAMS_7}})

    {{CONFIG}}{{PARAMS_10}} {{CFG}};

    function new(string name="{{VIRTUALSEQUENCE}}");
        super.new(name);
    endfunction

    virtual task pre_start();
        super.pre_start();

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_10}})::get(p_sequencer, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{VIRTUALSEQUENCE}}", "configuration is not set.")
        end
    endtask

    virtual task body();
        {{SEQ0}}{{PARAMS_14}} {{SEQ0_16}};
        {{SEQ1}}{{PARAMS_18}} {{SEQ1_20}};

        {{SEQ0_16}} = {{SEQ0}}{{PARAMS_14}}::type_id::create("{{SEQ0_16}}");
        {{SEQ1_20}} = {{SEQ1}}{{PARAMS_18}}::type_id::create("{{SEQ1_20}}");

        {{SEQ0_16}}.start(p_sequencer.{{SQR0}});
        {{SEQ1_20}}.start(p_sequencer.{{SQR1}});
    endtask
endclass
```
