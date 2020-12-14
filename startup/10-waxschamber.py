from ophyd import ( Component as Cpt,  Device,
                    EpicsSignal, EpicsSignalRO, EpicsMotor)

print(f'Loading {__file__}')

# Read the pressure from the waxs chamber
class sample_chamber_pressure(Device):
    waxs = Cpt(EpicsSignal, '{Det:300KW-TCG:7}P:Raw-I')  # Change PVs
    maxs = Cpt(EpicsSignal, '{B1:WAXS-TCG:9}P:Raw-I')  # Change PVs


chamber_pressure = sample_chamber_pressure('XF:12IDC-VA:2', name='chamber_pressure')  # Change PVs
chamber_pressure.waxs.kind = 'hinted'
chamber_pressure.maxs.kind = 'hinted'


GV7 = TwoButtonShutter('XF:12IDC-VA:2{Det:1M-GV:7}', name='GV7')



