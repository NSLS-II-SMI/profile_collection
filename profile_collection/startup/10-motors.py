from ophyd import EpicsMotor, Device, Component as C

mtr = EpicsMotor('XF:12IDC-OP:2{Lens:CRL-Ax:L1}Mtr', name='lens')


# class Gantry(Device):
#    x = C(EpicsMotor, 'AX3}')


# g = Gantry('basepv', name='gantry')

class CRL(Device):
    lens1 = C(EpicsMotor, 'L1}Mtr')
    lens2 = C(EpicsMotor, 'L2}Mtr')
    lens3 = C(EpicsMotor, 'L3}Mtr')
    lens4 = C(EpicsMotor, 'L4}Mtr')
    lens5 = C(EpicsMotor, 'L5}Mtr')
    lens6 = C(EpicsMotor, 'L6}Mtr')

crl = CRL('XF:12IDC-OP:2{Lens:CRL-Ax:', name='crl')
