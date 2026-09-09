---
id: "questa_10.6c_sim"
source_file: "tcl/questa_10.6c_sim.snippets"
triggers: ["simulate"]
description: "QuestaSim 10.6c UVM simulation script"
category: tcl
ultisnips_flags: "ab"
author: "TBD9rain"
placeholders:
  - name: "TAB_2"
    tabstop: 2
    default: "100"
  - name: "TB_NAME"
    tabstop: 3
    default: "tb_name"
  - name: "BASETEST"
    tabstop: 4
    default: "BaseTest"
  - name: "TAB_5"
    tabstop: 5
    default: "D:/questasim64_10.6c"
---

```tcl
#========================================
#   QuestaSim 10.6c UVM Simulation Script
#========================================

#------------------
#   Define Variable
#------------------

# when sim_time == 0, run all
set sim_time    {{TAB_2}}

set tb_module   {{TB_NAME}}
set uvm_test    {{BASETEST}}
set randseed    0
set onfinish    stop

# UVM-1.2 file path
set questa_home {{TAB_5}}
set uvm_lib_dir $questa_home/uvm-1.2
set uvm_src_dir $questa_home/verilog_src/uvm-1.2/src
set uvm_dpi_lib $uvm_lib_dir/win64/uvm_dpi


#-------------------------
#   Prepare for Simulation
#-------------------------

# quit simulation
quit -sim
# clear commands
# .main clear

# delete previous temporary data directory
if {[file exists work]} {
    file delete -force work
}

# create directory for temporary data
vlib work

# map logical library and directory
vmap uvm-1.2 $uvm_lib_dir
vmap work ./work


#---------------
#   Compile Code
#---------------

# "-sv": explicitly compile systemverilog files
# "-sv12compat": be compatible with IEEE Std 1800-2012
# "+cover=bcefst": enable code coverage measurement

# "+incdir+<directory>": specify directories to search "`include" files
# "+define+<marco_name>[=<macro_text>]": define or override a macro

vlog -work work\
    +cover=bcefst\
    -f src_filelist.txt

vlog -work work\
    -sv -sv12compat\
    +incdir+$uvm_src_dir\
    -L uvm-1.2\
    -f tb_file_list.txt

if {$sim_time <= 0} {
    vopt -64 -O4 -L uvm-1.2 $tb_module -o opt_tb
} else {
    vopt -64 -O4 -L uvm-1.2 +acc $tb_module -o opt_tb
}


#-------------------
#   Start Simulation
#-------------------

# "-nodpiexports": disable C wrapper code generation for DPI export

# "-coverage": enable functional coverage measurement
# "-coverstore cov_db": add coverage data to coverage manage directory
# "+UVM_TESTNAME=<testname>": designate test to run
# "-uvmtestname": use testname and random seed to name coverage file
# "-sv_seed <int>": assign randomization seed
# "-onfinish stop": use $stop when $finish

# "-G<param_name>=<param_value>": to assign or override a parameter

# "-L <device_lib>": for post simulation and timing simulation
# "-sdftyp <sdf_file>": for timing simulation
# "+transport_int_delays" and "+transport_path_delays" for timing simulation
# "+typdelays" or "+maxdelays" or "+mindelays" for timing simulation

vsim -lib work\
    -L uvm-1.2\
    -sv_lib $uvm_dpi_lib\
    -nodpiexports\
    -coverage\
    -coverstore cov_db\
    +UVM_TESTNAME=$uvm_test\
    -uvmtestname\
    -sv_seed $randseed\
    -onfinish $onfinish\
    opt_tb\
    -t 1ps -l sim.log


#-----------------
#   Run Simulation
#-----------------

set UserTimeUnit ns
if {$sim_time <= 0} {
    run -all
    simstats
} else {
    # add waveform
    if {[file exists wave.do]} {
        do wave.do
    }

    # run set interval
    run $sim_time

    # set step run length
    set RunLength 1000

    # wave window display adjustment
    wave zoom full
    configure wave -timelineunits ns
}

```
