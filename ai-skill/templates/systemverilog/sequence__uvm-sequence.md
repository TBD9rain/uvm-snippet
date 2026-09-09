---
id: "sequence__uvm-sequence"
source_file: "systemverilog/sequence.snippets"
triggers: ["Seq(uence)?"]
description: "UVM Sequence"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "SEQUENCE"
    tabstop: 1
    default: "Sequence"
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
  - name: "SEQUENCER"
    tabstop: 7
    default: "Sequencer"
  - name: "PARAMS_8"
    tabstop: 8
    default: " #({{TAB_9}})"
  - name: "TAB_9"
    tabstop: 9
  - name: "CONFIG"
    tabstop: 10
    default: "Config"
  - name: "PARAMS_11"
    tabstop: 11
    default: " #({{TAB_12}})"
  - name: "TAB_12"
    tabstop: 12
  - name: "CFG"
    tabstop: 13
    default: "cfg"
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{SEQUENCE}}{{PARAMS_2}} extends uvm_sequence #(.REQ ({{TXN}}));

    `uvm_object{{PARAM_SUFFIX}}_utils({{SEQUENCE}}{{PARAMS_5}})

    //  handler to sequencer
    `uvm_declare_p_sequencer({{SEQUENCER}}{{PARAMS_8}})

    {{CONFIG}}{{PARAMS_11}} {{CFG}};

    function new(string name="{{SEQUENCE}}");
        super.new(name);
    endfunction

    virtual task pre_start();
        super.pre_start();

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_11}})::get(p_sequencer, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{SEQUENCE}}", "configuration is not set.")
        end
    endtask

    virtual task body();
        REQ txn;

        txn = REQ::type_id::create("txn");
        //  transaction send request
        start_item(txn);
        //  transaction prepare

        //  transaction send
        finish_item(txn);
    endtask
endclass
```
