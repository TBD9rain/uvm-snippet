---
id: "basic__coverage-model-definition"
source_file: "systemverilog/basic.snippets"
triggers: ["covergroup"]
description: "coverage model definition"
category: systemverilog
ultisnips_flags: "bw"
author: "TBD9rain"
placeholders:
  - name: "COVERGROUP_NAME"
    tabstop: 1
    default: "covergroup_name"
  - name: "TAB_2"
    tabstop: 2
    default: " ({{TAB_3}}{{TAB_4}}\n)"
  - name: "TAB_3"
    tabstop: 3
    default: "\n//  sample signal\nconst ref bit signal,"
  - name: "TAB_4"
    tabstop: 4
    default: "\n//  option or bins argument\nint arg,"
---

```systemverilog
covergroup {{COVERGROUP_NAME}}{{TAB_2}};
    //  type option
    type_option.merge_instances = 0;    //  0: weighted average; 1: merge identical bins from instances
    //  inst option
    option.auto_bin_max = 64;
    option.get_inst_coverage = 0;   //  1: enable tracking of each instance when merge_instances is set

    //  coverage point definition

    //  cross coverage definition

endgroup
```
