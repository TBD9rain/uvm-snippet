---
id: "basic__fork-block"
source_file: "systemverilog/basic.snippets"
triggers: ["fork "]
description: "fork block"
category: systemverilog
ultisnips_flags: "rbA"
author: "TBD9rain"
placeholders:
  - name: "TAB_1"
    tabstop: 1
    choices: ["join", "join_any", "join_none"]
    default: "join"
---

```systemverilog
fork
    
{{TAB_1}}
```
