---
id: "environment__uvm-integrated-environment"
source_file: "systemverilog/environment.snippets"
triggers: ["Env(ironment)?"]
description: "UVM Integrated Environment"
category: systemverilog
ultisnips_flags: "rb"
author: "TBD9rain"
placeholders:
  - name: "ENVIRONMENT"
    tabstop: 1
    default: "Environment"
  - name: "PARAMS_2"
    tabstop: 2
    default: " #(\n    {{TAB_3}}\n)"
  - name: "TAB_3"
    tabstop: 3
  - name: "PARAMS_4"
    tabstop: 4
    default: " #({{TAB_5}})"
  - name: "TAB_5"
    tabstop: 5
  - name: "CONFIG"
    tabstop: 6
    default: "Config"
  - name: "PARAMS_7"
    tabstop: 7
    default: " #({{TAB_8}})"
  - name: "TAB_8"
    tabstop: 8
  - name: "CFG"
    tabstop: 9
    default: "cfg"
  - name: "ENV0"
    tabstop: 10
    default: "Env0"
  - name: "PARAMS_11"
    tabstop: 11
    default: " #({{TAB_12}})"
  - name: "TAB_12"
    tabstop: 12
  - name: "ENV0_13"
    tabstop: 13
    default: "env0"
  - name: "ENV1"
    tabstop: 14
    default: "Env1"
  - name: "PARAMS_15"
    tabstop: 15
    default: " #({{TAB_16}})"
  - name: "TAB_16"
    tabstop: 16
  - name: "ENV1_17"
    tabstop: 17
    default: "env1"
  - name: "VSQR"
    tabstop: 18
    default: "VSqr"
  - name: "PARAMS_19"
    tabstop: 19
    default: " #({{TAB_20}})"
  - name: "TAB_20"
    tabstop: 20
  - name: "VSQR_21"
    tabstop: 21
    default: "vsqr"
  - name: "PARAM_SUFFIX"
    derived: true
    rule: "\"_param\" if PARAMS_2 is set (class is parameterized), else \"\""
---

```systemverilog
class {{ENVIRONMENT}}{{PARAMS_2}} extends uvm_env;

    `uvm_component{{PARAM_SUFFIX}}_utils({{ENVIRONMENT}}{{PARAMS_4}})

    //  variable definition
    {{CONFIG}}{{PARAMS_7}} {{CFG}};

    {{ENV0}}{{PARAMS_11}} {{ENV0_13}};
    {{ENV1}}{{PARAMS_15}} {{ENV1_17}};

    {{VSQR}}{{PARAMS_19}} {{VSQR_21}};

    function new(string name="{{ENVIRONMENT}}", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #({{CONFIG}}{{PARAMS_7}})::get(this, "", "{{CFG}}", {{CFG}})) begin
            `uvm_fatal("{{ENVIRONMENT}}", "configuration is not set.")
        end

        {{ENV0_13}} = {{ENV0}}{{PARAMS_11}}::type_id::create("{{ENV0_13}}", this);
        {{ENV1_17}} = {{ENV1}}{{PARAMS_15}}::type_id::create("{{ENV1_17}}", this);
        uvm_config_db #({{CONFIG}}{{PARAMS_7}})::set(this, "{{ENV0_13}}", "{{CFG}}", {{CFG}});
        uvm_config_db #({{CONFIG}}{{PARAMS_7}})::set(this, "{{ENV1_17}}", "{{CFG}}", {{CFG}});

        {{VSQR_21}} = {{VSQR}}{{PARAMS_19}}::type_id::create("{{VSQR_21}}", this);
    endfunction

    function void connect_phase(uvm_phase phase);
        super.connect_phase(phase);

        {{VSQR_21}}.sqr0 = {{ENV0_13}}.i_agt.sqr;
        {{VSQR_21}}.sqr1 = {{ENV1_17}}.i_agt.sqr;
    endfunction
endclass
```
