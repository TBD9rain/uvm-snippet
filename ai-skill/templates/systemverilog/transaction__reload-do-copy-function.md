---
id: "transaction__reload-do-copy-function"
source_file: "systemverilog/transaction.snippets"
triggers: ["do_"]
description: "Reload do_copy function"
category: systemverilog
ultisnips_flags: "Abr"
author: "TBD9rain"
placeholders:
  - name: "TXN"
    tabstop: 1
    default: "Txn"
---

```systemverilog
virtual function void do_copy(uvm_object rhs);
    //  called by copy() function

    {{TXN}} rhs_;
    if(!$cast(rhs_, rhs)) begin
        `uvm_fatal("{{TXN}}", "do_copy type conversion failed.")
    end

    super.do_copy(rhs);

    //  this class property copy
    
endfunction
```
