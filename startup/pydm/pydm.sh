#! /bin/bash

. /opt/conda/etc/profile.d/conda.sh
conda activate pydm

cd $(dirname $0)
echo "PyDM .ui files dir": $(pwd)
for motor in '{"MOTOR": "XF:12IDC-ES:2{WAXS:1-Ax:Arc}Mtr"}' \
             '{"MOTOR": "XF:12IDC-OP:2{HEX:PRS-Ax:Rot}Mtr"}'; do
    echo "Starting $motor..."
    pydm --hide-nav-bar -m "$motor" inline_motor.ui > /dev/null 2>&1 &
done

