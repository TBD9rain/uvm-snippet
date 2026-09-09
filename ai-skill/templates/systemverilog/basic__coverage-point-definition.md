---
id: "basic__coverage-point-definition"
source_file: "systemverilog/basic.snippets"
triggers: ["coverpoint"]
description: "coverage point definition"
category: systemverilog
ultisnips_flags: "bw"
author: "TBD9rain"
placeholders:
  - name: "LABEL"
    tabstop: 1
    default: "label"
  - name: "VAR_NAME"
    tabstop: 2
    default: "var_name"
  - name: "LABEL_SEP"
    derived: true
    rule: "\": \" if LABEL is set, else \"\""
---

```systemverilog
{{LABEL}}{{LABEL_SEP}}coverpoint {{VAR_NAME}} {
    //  bins definition
}
```
