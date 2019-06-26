print(f'Loading {__file__}')

from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner

class CRL(Device):
    lens1 = Cpt(EpicsMotor, 'L1}Mtr')
    lens2 = Cpt(EpicsMotor, 'L2}Mtr')
    lens3 = Cpt(EpicsMotor, 'L3}Mtr')
    lens4 = Cpt(EpicsMotor, 'L4}Mtr')
    lens5 = Cpt(EpicsMotor, 'L5}Mtr')
    lens6 = Cpt(EpicsMotor, 'L6}Mtr')
    lens7 = Cpt(EpicsMotor, 'L7}Mtr')
    lens8 = Cpt(EpicsMotor, 'L8}Mtr')
    lens9 = Cpt(EpicsMotor, 'L9}Mtr')
    lens10 = Cpt(EpicsMotor, 'L10}Mtr')
    lens11 = Cpt(EpicsMotor, 'L11}Mtr')
    lens12 = Cpt(EpicsMotor, 'L12}Mtr')
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')
    ph = Cpt(EpicsMotor, 'Ph}Mtr')
    th = Cpt(EpicsMotor, 'Th}Mtr')


crl = CRL('XF:12IDC-OP:2{Lens:CRL-Ax:', name='crl')

# aperture motors, see 10-slits.py

# Note: focus related code is in CSS only at this time


#Check if CRL's are in to determine if low divergence or micro-focusing

def crl_state():
    for crl_le in [crl.lens1, crl.lens2, crl.lens3, crl.lens4, crl.lens5,
                   crl.lens6, crl.lens7, crl.lens8, crl.lens9, crl.lens10,
                   crl.lens11, crl.lens12]:
            
        if abs(crl_le.position) < 4:
            crl_state = 'mic_foc'
            break
        else:
            crl_state = 'low_div'
    return crl_state
            
        
        

