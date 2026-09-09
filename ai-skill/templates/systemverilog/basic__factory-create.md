---
id: "basic__factory-create"
source_file: "systemverilog/basic.snippets"
triggers: ["=\\s+create"]
description: "Factory Create"
category: systemverilog
ultisnips_flags: "rA"
author: "TBD9rain"
placeholders:
  - name: "CLASS"
    tabstop: 1
    default: "Class"
  - name: "PARAMS_2"
    tabstop: 2
    default: " #({{TAB_3}})"
  - name: "TAB_3"
    tabstop: 3
  - name: "NAME"
    tabstop: 4
    default: "name"
  - name: "TAB_5"
    tabstop: 5
    default: ", this"
---

```systemverilog
= {{CLASS}}{{PARAMS_2}}::type_id::create("{{NAME}}"{{TAB_5}});
```
