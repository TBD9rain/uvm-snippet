---
id: "transaction__reload-convert2string-function"
source_file: "systemverilog/transaction.snippets"
triggers: ["do_"]
description: "Reload convert2string() function"
category: systemverilog
ultisnips_flags: "Abr"
author: "TBD9rain"
placeholders: []
---

```systemverilog
virtual function string convert2string();
    string s = super.convert2string();

    //  this class property to string
    s = {s, $sformatf()};

    return s;
endfunction
```
