from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as C

# class Gantry(Device):
#    x = C(EpicsMotor, 'AX3}')

class CRL(Device):
    lens1 = C(EpicsMotor, 'L1}Mtr')
    lens2 = C(EpicsMotor, 'L2}Mtr')
    lens3 = C(EpicsMotor, 'L3}Mtr')
    lens4 = C(EpicsMotor, 'L4}Mtr')
    lens5 = C(EpicsMotor, 'L5}Mtr')
    lens6 = C(EpicsMotor, 'L6}Mtr')
    lens7 = C(EpicsMotor, 'L7}Mtr')
    lens8 = C(EpicsMotor, 'L8}Mtr')
    lens9 = C(EpicsMotor, 'L9}Mtr')
    lens10 = C(EpicsMotor, 'L10}Mtr')
    lens11 = C(EpicsMotor, 'L11}Mtr')
    lens12 = C(EpicsMotor, 'L12}Mtr')
    x = C(EpicsMotor, 'X}Mtr')
    y = C(EpicsMotor, 'Y}Mtr')
    z = C(EpicsMotor, 'Z}Mtr')
    ph = C(EpicsMotor, 'Ph}Mtr')
    th = C(EpicsMotor, 'Th}Mtr')

crl = CRL('XF:12IDC-OP:2{Lens:CRL-Ax:', name='crl')




#SMI IVU23 motors

#DCM motors
p2x = EpicsMotor('XF12ID:m67', name='p2x')
p2h = EpicsMotor('XF12ID:m66', name='p2h')
bragg = EpicsMotor('XF12ID:m65', name='bragg')

#White Beam Slits motors
wbsx = EpicsMotor('XF:12IDA-OP:2{Slt:WB-Ax:Hpos}Mtr', name='wbsx')
wbsxg = EpicsMotor('XF:12IDA-OP:2{Slt:WB-Ax:Hgap}Mtr', name='wbsxg')
wbsy = EpicsMotor('XF:12IDA-OP:2{Slt:WB-Ax:Vpos}Mtr', name='wbsy')
wbsyg = EpicsMotor('XF:12IDA-OP:2{Slt:WB-Ax:Vgap}Mtr', name='wbsyg')


