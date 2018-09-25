print(f'Loading {__file__}')

from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner


class STG(Device):
    x = Cpt(EpicsMotor, 'X}Mtr', labels=['stage'])
    y = Cpt(EpicsMotor, 'Y}Mtr', labels=['stage'])
    z = Cpt(EpicsMotor, 'Z}Mtr', labels=['stage'])
    th = Cpt(EpicsMotor, 'theta}Mtr', labels=['stage'])
    ph = Cpt(EpicsMotor, 'phi}Mtr', labels=['stage'])
    ch = Cpt(EpicsMotor, 'chi}Mtr', labels=['stage'])


class SMPL(Device):
    x = Cpt(EpicsMotor, 'X}Mtr', labels=['sample'])
    y = Cpt(EpicsMotor, 'Y}Mtr', labels=['sample'])
    z = Cpt(EpicsMotor, 'Z}Mtr', labels=['sample'])
    al = Cpt(EpicsMotor, 'alpha}Mtr', labels=['sample'])
    az = Cpt(EpicsMotor, 'azimuth}Mtr', labels=['sample'])
    ka = Cpt(EpicsMotor, 'kappa}Mtr', labels=['sample'])


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

for hp in [stage, sample, hp140, hp430]:
    hp.configuration_attrs = hp.read_attrs

prs = EpicsMotor('XF:12IDC-OP:2{HEX:PRS-Ax:Rot}Mtr', name='prs')

class WAXS(Device):
    arc = Cpt(EpicsMotor, 'Arc}Mtr')

waxs = WAXS('XF:12IDC-ES:2{WAXS:1-Ax:', name='waxs')
