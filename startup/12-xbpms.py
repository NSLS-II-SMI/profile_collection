print(f'Loading {__file__}')

from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner

# xbpm2 positioner shortcut for scans 5 april 2017

# Note: this class isn't really different from APER ifle only motor axes
# are here. But I can imagine inputting numerical values pertaining 
# to each diamond, or special in/out or quad1/quad2 commands that would
# be specific to the xbpms.

# need to verify the PVs, only xbpm2 was checked:

class XBPM(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')

xbpm1_pos = XBPM('XF:12IDA-BI:2{XBPM:1-Ax:', name='xbpm1_pos')
xbpm2_pos = XBPM('XF:12IDA-BI:2{XBPM:2-Ax:', name='xbpm2_pos')
xbpm3_pos = XBPM('XF:12IDB-BI:2{XBPM:3-Ax:', name='xbpm3_pos')

# need work to input elecetrometer current PVs - what headers needed?

xbpm3y = EpicsSignal('XF:12IDB-BI:2{EM:BPM3}PosY:MeanValue_RBV', name='xbpm3y')

#Prototype new electrometer, currently looking at XBPM2.
#ch1,2,3,4 = pads 2,3,5,4 respectively; thick active area






