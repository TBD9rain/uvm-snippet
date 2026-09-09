---
id: "sequencer__uvm-sequencer"
source_file: "systemverilog/sequencer.snippets"
triggers: ["Sqr", "Sequencer"]
description: "UVM Sequencer"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "SEQUENCER"
    tabstop: 1
    default: "Sequencer"
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
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{SEQUENCER}}{{PARAMS_2}} extends uvm_sequencer #(.REQ ({{TXN}}));

    `uvm_component{{PARAM_SUFFIX}}_utils({{SEQUENCER}}{{PARAMS_5}})

    function new(string name="{{SEQUENCER}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction
endclass
```
