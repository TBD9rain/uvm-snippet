---
id: "sequencer__uvm-sequencer-type-specialization"
source_file: "systemverilog/sequencer.snippets"
triggers: ["Sqr", "Sequencer"]
description: "UVM Sequencer Type Specialization"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "TXN"
    tabstop: 1
    default: "Txn"
  - name: "PARAMS_2"
    tabstop: 2
    default: " #({{TAB_3}})"
  - name: "TAB_3"
    tabstop: 3
  - name: "SEQUENCER"
    tabstop: 4
    default: "Sequencer"
---

```systemverilog
typedef uvm_sequencer #(.REQ ({{TXN}}{{PARAMS_2}})) {{SEQUENCER}};
```
