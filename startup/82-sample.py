BS_POSITION_X = 1.25
BS_POSITION_Y = 13.2

class PIL1MPositions(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')


class PIL1MBS(Device):
    x = Cpt(EpicsMotor, 'IBB}Mtr')
    y = Cpt(EpicsMotor, 'IBM}Mtr')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x_center = None
        self.y_center = 13.1


att1_7 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-7}', name='att1_7')
att1_6 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-6}', name='att1_6')
att1_3 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-3}', name='att1_3')
att1_4 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-4}', name='att1_4')

pil1m_pos = PIL1MPositions('XF:12IDC-ES:2{Det:1M-Ax:', name='pil1m_pos')
pil1m_bs = PIL1MBS('XF:12IDC-ES:2{BS:SAXS-Ax:', name='pil1m_bs')

pil1m_bs.x_center = 1.25
pil1m_bs.y_center = 13.1

# Plans:
def alignment_mode():
    yield from bps.mv(att1_7, 'Insert')
    yield from bps.mv(att1_6, 'Insert')
    pos = pil1m_bs.x.position
    yield from bps.mv(pil1m_bs.x, pos+10)


def measurement_mode():
    if pil1m_bs.x_center is None:
        raise ValueError('Define pil1m_bs.x_center position')
    if pil1m_bs.y_center is None:
        raise ValueError('Define pil1m_bs.y_center position')
    yield from bps.mv(pil1m_bs.x, pil1m_bs.x_center)
    yield from bps.mv(pil1m_bs.y, pil1m_bs.y_center)
    yield from bps.mv(att1_6, 'Retract')
    yield from bps.mv(att1_7, 'Retract')


