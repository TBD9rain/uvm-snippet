---
id: "basic__uvm-tlm-1-analysis-implementation"
source_file: "systemverilog/basic.snippets"
triggers: ["analysis"]
description: "UVM TLM-1 Analysis Implementation"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "INT"
    tabstop: 1
    default: "int"
  - name: "CLASS"
    tabstop: 2
    default: "class"
  - name: "IMP"
    tabstop: 3
    default: "imp"
---

```systemverilog
uvm_analysis_imp #({{INT}}, {{CLASS}}) {{IMP}};
```
