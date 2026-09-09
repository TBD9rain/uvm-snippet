---
id: "basic__for-iteration"
source_file: "systemverilog/basic.snippets"
triggers: ["for "]
description: "for iteration"
category: systemverilog
ultisnips_flags: "rbA"
author: "TBD9rain"
placeholders:
  - name: "I"
    tabstop: 1
    default: "i"
  - name: "TAB_2"
    tabstop: 2
    default: "0"
---

```systemverilog
for (int {{I}} = 0; {{I}} < {{TAB_2}}; {{I}}++) begin
    
end
```
