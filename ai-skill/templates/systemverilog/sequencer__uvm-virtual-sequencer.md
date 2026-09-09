---
id: "sequencer__uvm-virtual-sequencer"
source_file: "systemverilog/sequencer.snippets"
triggers: ["Sqr", "Sequencer"]
description: "UVM Virtual Sequencer"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "VIRTUALSEQUENCER"
    tabstop: 1
    default: "VirtualSequencer"
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
  - name: "SQR0"
    tabstop: 6
    default: "Sqr0"
  - name: "PARAMS_7"
    tabstop: 7
    default: " #({{TAB_8}})"
  - name: "TAB_8"
    tabstop: 8
  - name: "SQR0_9"
    tabstop: 9
    default: "sqr0"
  - name: "SQR1"
    tabstop: 10
    default: "Sqr1"
  - name: "PARAMS_11"
    tabstop: 11
    default: " #({{TAB_12}})"
  - name: "TAB_12"
    tabstop: 12
  - name: "SQR1_13"
    tabstop: 13
    default: "sqr1"
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{VIRTUALSEQUENCER}}{{PARAMS_2}} extends uvm_sequencer;

    `uvm_component{{PARAM_SUFFIX}}_utils({{VIRTUALSEQUENCER}}{{PARAMS_4}})

    {{SQR0}}{{PARAMS_7}} {{SQR0_9}};
    {{SQR1}}{{PARAMS_11}} {{SQR1_13}};

    function new(string name="{{VIRTUALSEQUENCER}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction
endclass
```
