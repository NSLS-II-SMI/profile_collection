print(f'Loading {__file__}')

from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner

class MIR(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    th = Cpt(EpicsMotor, 'P}Mtr')

hfm = MIR('XF:12IDA-OP:2{Mir:HF-Ax:', name='hfm')
vfm = MIR('XF:12IDA-OP:2{Mir:VF-Ax:', name='vfm')
vdm = MIR('XF:12IDA-OP:2{Mir:VD-Ax:', name='vdm')

# The associated slits are coded in 10-slits.py

# See also 11-bimorphs.py (to be developed)

# Does the bounce-down mirror (attocube ctrl) have EPICS implementation yet?

