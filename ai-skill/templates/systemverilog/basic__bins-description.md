---
id: "basic__bins-description"
source_file: "systemverilog/basic.snippets"
triggers: ["bins"]
description: "bins description"
category: systemverilog
ultisnips_flags: "bw"
author: "TBD9rain"
placeholders:
  - name: "TAB_1"
    tabstop: 1
    choices: ["bins", "ignore_bins", "illegal_bins"]
    default: "bins"
  - name: "BIN_NAME"
    tabstop: 2
    default: "bin_name"
---

```systemverilog
{{TAB_1}} {{BIN_NAME}} = {};
```
