#!/bin/bash
WSTL_HOME=/Users/roederc/work/git_clad/healthcare-data-harmonization
cd $WSTL_HOME
PROJECT_HOME=/Users/roederc/work/git_clad/data_structures_languages/
pwd
gradle :runtime:run --debug -q --args="-m $PROJECT_HOME/wstl/all_in_one.wstl -i $PROJECT_HOME/input_json/all_in_one.json"

