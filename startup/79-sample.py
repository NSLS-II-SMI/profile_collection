from ophyd import ( Component as Cpt,  Device,
                    EpicsSignal, EpicsSignalRO, EpicsMotor)

print(f'Loading {__file__}')


fshutter = EpicsMotor('XF:12IDC:2{Sh:E-Ax:Y}Mtr', name='fshutter')

#Read the pressure from the waxs chamber
class Waxs_chamber_pressure(Device):
    ch1_read = Cpt(EpicsSignal, '{Det:300KW-TCG:7}P:Raw-I') #Change PVs
    
waxs_pressure = Waxs_chamber_pressure('XF:12IDC-VA:2', name='waxs_chamber_pressure')#Change PVs 
waxs_pressure.ch1_read.kind = 'hinted'


class PIL1MPositions(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')


class PIL1MBS(Device):
    x = Cpt(EpicsMotor, 'IBB}Mtr')
    y = Cpt(EpicsMotor, 'IBM}Mtr')
    x_other = Cpt(EpicsMotor, 'OBB}Mtr')
    y_other = Cpt(EpicsMotor, 'OBM}Mtr')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x_center = None
        self.y_center = 13.1


att1_1 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-1}', name='att1_1')
att1_2 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-2}', name='att1_2')
att1_3 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-3}', name='att1_3')
att1_4 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-4}', name='att1_4')
att1_5 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-5}', name='att1_5')
att1_6 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-6}', name='att1_6')
att1_7 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-7}', name='att1_7')
att1_8 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-8}', name='att1_8')
att1_9 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-9}', name='att1_9')
att1_10 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-10}', name='att1_10')
att1_11 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-11}', name='att1_11')
att1_12 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-12}', name='att1_12')

att2_1 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-1}', name='att2_1')
att2_2 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-2}', name='att2_2')
att2_3 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-3}', name='att2_3')
att2_4 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-4}', name='att2_4')
att2_5 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-5}', name='att2_5')
att2_6 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-6}', name='att2_6')
att2_7 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-7}', name='att2_7')
att2_8 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-8}', name='att2_8')
att2_9 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-9}', name='att2_9')
att2_10 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-10}', name='att2_10')
att2_11 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-11}', name='att2_11')
att2_12 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-12}', name='att2_12')


pil1m_pos = PIL1MPositions('XF:12IDC-ES:2{Det:1M-Ax:', name='pil1m_pos')
pil1m_bs = PIL1MBS('XF:12IDC-ES:2{BS:SAXS-Ax:', name='pil1m_bs')

for detpos in [pil1m_pos]:
    detpos.configuration_attrs = detpos.read_attrs

GV7 = TwoButtonShutter('XF:12IDC-VA:2{Det:1M-GV:7}', name='GV7')



