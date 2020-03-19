from ophyd import ( Component as Cpt,  Device,
                    EpicsSignal, EpicsSignalRO, EpicsMotor)

print(f'Loading {__file__}')

# Read the pressure from the waxs chamber
class Waxs_chamber_pressure(Device):
    ch1_read = Cpt(EpicsSignal, '{Det:300KW-TCG:7}P:Raw-I')  # Change PVs


waxs_pressure = Waxs_chamber_pressure('XF:12IDC-VA:2', name='waxs_chamber_pressure')  # Change PVs
waxs_pressure.ch1_read.kind = 'hinted'

GV7 = TwoButtonShutter('XF:12IDC-VA:2{Det:1M-GV:7}', name='GV7')



