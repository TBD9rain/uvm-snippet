---
id: "basic__function-skeleton"
source_file: "systemverilog/basic.snippets"
triggers: ["function"]
description: "function skeleton"
category: systemverilog
ultisnips_flags: "A"
author: "TBD9rain"
placeholders:
  - name: "AUTOMATIC"
    tabstop: 1
    default: "automatic "
  - name: "VOID"
    tabstop: 2
    default: "void"
  - name: "FUNC_NAME"
    tabstop: 3
    default: "func_name"
---

```systemverilog
function {{AUTOMATIC}}{{VOID}} {{FUNC_NAME}};

endfunction
```
