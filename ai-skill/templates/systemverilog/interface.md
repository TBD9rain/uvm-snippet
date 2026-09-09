---
id: "interface"
source_file: "systemverilog/interface.snippets"
triggers: ["interface"]
description: "interface definition"
category: systemverilog
ultisnips_flags: "bw"
author: "TBD9rain"
placeholders:
  - name: "IF_NAME"
    tabstop: 1
    default: "if_name"
  - name: "PARAMS_2"
    tabstop: 2
    default: " #()"
  - name: "CLK"
    tabstop: 3
    default: "clk"
  - name: "RST_N"
    tabstop: 4
    default: "rst_n"
  - name: "TAB_5"
    tabstop: 5
    choices: ["posedge", "negedge"]
    default: "posedge"
---

```systemverilog
interface {{IF_NAME}}{{PARAMS_2}} (
    input logic {{CLK}},
    input logic {{RST_N}});

    //  DUT IO port
    logic data_in_vld;
    logic [ 7: 0] data_in;

    logic data_out_vld;
    logic [ 7: 0] data_out;

    //  clock counter for time stamp
    longint unsigned clk_cnt = 0;

    always_ff @({{TAB_5}} {{CLK}}) begin
        clk_cnt <= clk_cnt + 1;
    end

    clocking cb @({{TAB_5}} {{CLK}});
        output data_in_vld;
        output data_in;
    endclocking

    //  driver
    modport drv_mp (
        clocking cb,
        input {{RST_N}});

    //  monitor
    modport mon_mp (
        input {{CLK}},
        input {{RST_N}},

        input data_in_vld,
        input data_in,

        input data_out_vld,
        input data_out,

        input clk_cnt);

    //  DUT
    modport dut_mp (
        input {{CLK}},
        input {{RST_N}},

        input data_in_vld,
        input data_in,

        output data_out_vld,
        output data_out);
endinterface
```
