#!/bin/bash

cp -v smi_config.csv ~/.ipython/profile_${TEST_PROFILE}/smi_config.csv

mkdir ~/.ipython/profile_${TEST_PROFILE}/startup/
cp -v startup/intepolation_db_sdd2.txt ~/.ipython/profile_${TEST_PROFILE}/startup/intepolation_db_sdd2.txt
