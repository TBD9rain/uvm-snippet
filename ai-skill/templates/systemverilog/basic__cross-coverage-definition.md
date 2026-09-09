---
id: "basic__cross-coverage-definition"
source_file: "systemverilog/basic.snippets"
triggers: ["cross"]
description: "cross coverage definition"
category: systemverilog
ultisnips_flags: "bw"
author: "TBD9rain"
placeholders:
  - name: "LABEL"
    tabstop: 1
    default: "label"
  - name: "TAB_2"
    tabstop: 2
    default: "var_or_label0, var_or_label1"
  - name: "LABEL_SEP"
    derived: true
    rule: "\": \" if LABEL is set, else \"\""
---

```systemverilog
{{LABEL}}{{LABEL_SEP}}cross {{TAB_2}} {
    //  bins definition
}
```
