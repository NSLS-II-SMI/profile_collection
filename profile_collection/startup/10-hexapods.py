from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner


class STG(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')
    th = Cpt(EpicsMotor, 'theta}Mtr')
    ph = Cpt(EpicsMotor, 'phi}Mtr')
    ch = Cpt(EpicsMotor, 'chi}Mtr')


class SMPL(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')
    al = Cpt(EpicsMotor, 'alpha}Mtr')
    az = Cpt(EpicsMotor, 'azimuth}Mtr')
    ka = Cpt(EpicsMotor, 'kappa}Mtr')


class HEXAPOD(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')
    a = Cpt(EpicsMotor, 'A}Mtr')
    b = Cpt(EpicsMotor, 'B}Mtr')
    c = Cpt(EpicsMotor, 'C}Mtr')

stage = STG('XF:12IDC-OP:2{HEX:Stg-Ax:', name='stage')
sample = SMPL('XF:12IDC-OP:2{HEX:Sam-Ax:', name='sample')
hp140 = HEXAPOD('XF:12IDC-OP:2{HEX:140-Ax:', name='hp140')
hp430 = HEXAPOD('XF:12IDC-OP:2{HEX:430-Ax:', name='hp430')



