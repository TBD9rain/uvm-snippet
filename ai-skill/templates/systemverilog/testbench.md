---
id: "testbench"
source_file: "systemverilog/testbench.snippets"
triggers: ["testbench"]
description: "UVM testbench"
category: systemverilog
ultisnips_flags: "b"
author: "TBD9rain"
placeholders:
  - name: "DUT"
    tabstop: 1
    default: "dut"
  - name: "TAB_2"
    tabstop: 2
    default: "{{DUT}}_pkg"
  - name: "CONFIG"
    tabstop: 3
    default: "Config"
  - name: "PARAMS_4"
    tabstop: 4
    default: " #({{TAB_5}})"
  - name: "TAB_5"
    tabstop: 5
  - name: "CFG"
    tabstop: 6
    default: "cfg"
  - name: "TAB_7"
    tabstop: 7
    default: "{{DUT}}_if"
  - name: "PARAMS_8"
    tabstop: 8
    default: " #(\n    {{TAB_9}}\n)"
  - name: "TAB_9"
    tabstop: 9
  - name: "PARAMS_10"
    tabstop: 10
    default: " #(\n    {{TAB_11}}\n)"
  - name: "TAB_11"
    tabstop: 11
  - name: "TEST"
    tabstop: 12
    default: "Test"
---

```systemverilog
`timescale 1ns/1ps
`default_nettype none

module {{DUT}}_tb;

//======================
//  PARAMETER DEFINITION
//======================

localparam  CLK_HALF_PERIOD     = 10/2;


//=====================
//  PACKAGE IMPORTATION
//=====================

`include "uvm_macros.svh"
import uvm_pkg::*;

import {{TAB_2}}::*;


//=====================
//  VARIABLE DEFINITION
//=====================

bit clk = 0;
bit rst_n = 0;

{{CONFIG}}{{PARAMS_4}} {{CFG}};

{{TAB_7}}{{PARAMS_8}}
tb_if (
    .clk    (clk),
    .rst_n  (rst_n)
);


//===================
//  DUT INSTANTIATION
//===================

{{DUT}}{{PARAMS_10}}
u_dut();


//=====================
//  VERIFICATION CODING
//=====================

//  clock generator
initial begin
    forever begin
        #(CLK_HALF_PERIOD);
        clk = ~clk;
    end
end

initial begin
    rst_n = 1'b0;
    #1000;
    rst_n = 1'b1;
end

initial begin
    $write("\n*****************************\n");
    $write("Running UVM version: %s\n", `UVM_VERSION_STRING);
    $write("*****************************\n\n");
end

initial begin
    {{CFG}} = {{CONFIG}}{{PARAMS_4}}::type_id::create("{{CFG}}");
    {{CFG}}.vif = tb_if;

    uvm_config_db #({{CONFIG}}{{PARAMS_4}})::set(null, "uvm_test_top", "{{CFG}}", {{CFG}});
end

initial begin
    run_test("{{TEST}}");
end

endmodule

`default_nettype wire
```
