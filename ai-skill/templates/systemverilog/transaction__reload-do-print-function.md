---
id: "transaction__reload-do-print-function"
source_file: "systemverilog/transaction.snippets"
triggers: ["do_"]
description: "Reload do_print() function"
category: systemverilog
ultisnips_flags: "Abr"
author: "TBD9rain"
placeholders: []
---

```systemverilog
virtual function void do_print(uvm_printer printer);
    //  called by sprint()

    printer.m_string = convert2string();
endfunction
```
