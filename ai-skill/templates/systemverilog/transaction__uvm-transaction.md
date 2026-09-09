---
id: "transaction__uvm-transaction"
source_file: "systemverilog/transaction.snippets"
triggers: ["Txn", "Transaction"]
description: "UVM Transaction"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "TXN"
    tabstop: 1
    default: "Txn"
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
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{TXN}}{{PARAMS_2}} extends uvm_sequence_item;

    //----------
    //  Variable
    //----------

    //  Use bit for input, logic for output

    //  time stamp
    longint unsigned timestamp = 0;


    //----------
    //  Registry
    //----------

    `uvm_object{{PARAM_SUFFIX}}_utils_begin({{TXN}}{{PARAMS_4}})
        `uvm_field_int(timestamp, UVM_ALL_ON | UVM_NOCOMPARE)
    `uvm_object_utils_end


    //--------
    //  Method
    //--------

    function new(string name="{{TXN}}");
        super.new(name);
    endfunction
endclass
```
