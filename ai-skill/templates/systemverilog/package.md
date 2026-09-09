---
id: "package"
source_file: "systemverilog/package.snippets"
triggers: ["package", "pkg"]
description: "UVM Component Package Definition"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "PKG_NAME"
    tabstop: 1
    derived: true
    note: "defaults to the snippet source file base name"
---

```systemverilog
package {{PKG_NAME}};

`include "uvm_macros.svh"
import uvm_pkg::*;

`include "Config.sv"

`include "Txn.sv"
`include "Sqr.sv"
`include "Drv.sv"
`include "Mon.sv"
`include "Agt.sv"
`include "RefMdl.sv"
`include "Scb.sv"
`include "ScbFI.sv"
`include "Cov.sv"
`include "Env.sv"
`include "Seq.sv"
`include "Test.sv"

endpackage
```
