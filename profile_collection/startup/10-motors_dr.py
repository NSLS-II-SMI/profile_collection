from ophyd import EpicsMotor, Device, Component as C

# create super user status if desired to hide motors
# supe = 1
# if (supe) 
#  mtr = EpicsMotor('XF12ID:m67', name='p2x')

class CRL(Device):
    lens1 = C(EpicsMotor, 'L1}Mtr')
    lens2 = C(EpicsMotor, 'L2}Mtr')
    lens3 = C(EpicsMotor, 'L3}Mtr')
    lens4 = C(EpicsMotor, 'L4}Mtr')
    lens5 = C(EpicsMotor, 'L5}Mtr')
    lens6 = C(EpicsMotor, 'L6}Mtr')

crl = CRL('XF:12IDC-OP:2{Lens:CRL-Ax:', name='crl')

#crl.lens1

lens = EpicsMotor('XF:12IDC-OP:2{Lens:CRL-Ax:L1}Mtr', name='lens')



p2x = EpicsMotor('XF12ID:m67', name='p2x')

# RE(bp.scan([], crl.lens1, -5, 5, 50))

#class SLIT(Device):
#	top = sdkfsjd
#	bot = asldkajsd
#	left = sldkfjs
#	right = aslkdas

#WBSlit = SLIT('PV.....

#WBslit.top

#SSA = SLIT('PVada;sd

#SSA.top



