#!/bin/bash
WSTL_HOME=/Users/roederc/work/git_clad/healthcare-data-harmonization
cd $WSTL_HOME
PROJECT_HOME=/Users/roederc/work/git_clad/data_structures_languages/
pwd
gradle :runtime:run -q --args="-m $PROJECT_HOME/wstl_codelab/codelab.wstl -i $PROJECT_HOME/wstl_codelab/codelab.json"

