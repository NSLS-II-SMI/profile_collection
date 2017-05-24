from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner

class DCM(Device):
    gap = Cpt(EpicsMotor, 'm66')
    pitch = Cpt(EpicsMotor, 'm67')
    roll = Cpt(EpicsMotor, 'm68')
    bragg = Cpt(EpicsMotor, 'm65')
    x = Cpt(EpicsMotor, 'm69')

dcm = DCM('XF12ID:', name='dcm')


# DCM motor shortcuts. Early scans used the names at right (p2h, etc).
dcm_gap = dcm.gap  # Height in CSS # EpicsMotor('XF12ID:m66', name='p2h')
dcm_pitch = dcm.pitch  # pitch in CSS # EpicsMotor('XF12ID:m67', name='p2x')
dcm_roll = dcm.roll  # Roll in CSS # EpicsMotor('XF12ID:m68', name='p2r')
bragg = dcm.bragg  # Theta in CSS  # EpicsMotor('XF12ID:m65', name='bragg')
dcm_x = dcm.x  # E Mono X in CSS

bragg.read_attrs = ['user_readback']
