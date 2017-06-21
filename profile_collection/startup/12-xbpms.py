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

xbpm1 = XBPM('XF:12IDA-BI:2{XBPM:1-Ax:', name='xbpm1')
xbpm2 = XBPM('XF:12IDA-BI:2{XBPM:2-Ax:', name='xbpm2')
xbpm3 = XBPM('XF:12IDB1-BI:2{XBPM:3-Ax:', name='xbpm3')

# need work to input elecetrometer current PVs - what headers needed?

#Prototype new electrometer, currently looking at XBPM2.
#ch1,2,3,4 = pads 2,3,5,4 respectively; thick active area

# bias voltage command should be limited to 2V or 0V only



### idea - put info here how to restart ioc, location of medms, etc




###
# from ophyd import EpicsMotor, EpicsSignal, Device, Component as C

# import time as ttime  # tea time
# from datetime import datetime
# from ophyd import (ProsilicaDetector, SingleTrigger, TIFFPlugin,
#                    ImagePlugin, StatsPlugin, DetectorBase, HDF5Plugin,
#                   AreaDetector, EpicsSignal, EpicsSignalRO, ROIPlugin,
#                    TransformPlugin, ProcessPlugin)
# from ophyd.areadetector.cam import AreaDetectorCam
# from ophyd.areadetector.base import ADComponent, EpicsSignalWithRBV
# from ophyd.areadetector.filestore_mixins import (FileStoreTIFFIterativeWrite,
#                                                  FileStoreHDF5IterativeWrite,
#                                                  FileStoreBase, new_short_uid)
# from ophyd import Component as Cpt, Signal
# from ophyd.utils import set_and_wait

### placeholder - fluoro screen - decide don't need
