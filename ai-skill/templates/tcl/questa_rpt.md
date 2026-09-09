---
id: "questa_rpt"
source_file: "tcl/questa_rpt.snippets"
triggers: ["report"]
description: "QuestaSim UVM Report Script"
category: tcl
ultisnips_flags: "Ab"
author: "TBD9rain"
placeholders: []
---

```tcl
#==============================
#   QuestaSim UVM Report Script
#==============================


#-------------------------
#   Prepare for Simulation
#-------------------------

# quit simulation
quit -sim
# clear commands
# .main clear


#----------------------------
#   Generate Summary Database
#----------------------------

vcover merge -out sum.ucdb cov_db


#--------------------------------
#   Generate HTML Coverage Report
#--------------------------------

vcover report -details -html -htmldir cov_rpt_html sum.ucdb


#------------------------
# Remove Summary Database
#------------------------

file delete -force sum.ucdb

```
