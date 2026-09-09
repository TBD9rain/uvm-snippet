---
id: "basic__task-skeleton"
source_file: "systemverilog/basic.snippets"
triggers: ["task"]
description: "task skeleton"
category: systemverilog
ultisnips_flags: "A"
author: "TBD9rain"
placeholders:
  - name: "AUTOMATIC"
    tabstop: 1
    default: "automatic "
  - name: "TASK_NAME"
    tabstop: 2
    default: "task_name"
---

```systemverilog
task {{AUTOMATIC}}{{TASK_NAME}};

endtask
```
