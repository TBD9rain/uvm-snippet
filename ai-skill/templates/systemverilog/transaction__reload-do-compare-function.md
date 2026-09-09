---
id: "transaction__reload-do-compare-function"
source_file: "systemverilog/transaction.snippets"
triggers: ["do_"]
description: "Reload do_compare() function"
category: systemverilog
ultisnips_flags: "Abr"
author: "TBD9rain"
placeholders:
  - name: "TXN"
    tabstop: 1
    default: "Txn"
  - name: "PROPERTY"
    tabstop: 2
    default: "property"
---

```systemverilog
virtual function bit do_compare(uvm_object rhs, uvm_comparer comparer);
    //  called by compare() function

    {{TXN}} rhs_;
    do_compare = super.do_compare(rhs, comparer);
    if(!$cast(rhs_, rhs)) begin
        `uvm_fatal("{{TXN}}", "do_compare type conversion failed.")
    end

    //  this class property compare
    do_compare &= (this.{{PROPERTY}} === rhs_.{{PROPERTY}});
endfunction
```
