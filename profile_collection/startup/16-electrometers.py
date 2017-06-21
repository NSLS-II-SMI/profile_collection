from ophyd import EpicsMotor, EpicsSignal, Device, Component as C

import time as ttime  # tea time
from datetime import datetime
from ophyd import (ProsilicaDetector, SingleTrigger, TIFFPlugin,
                   ImagePlugin, StatsPlugin, DetectorBase, HDF5Plugin,
                  AreaDetector, EpicsSignal, EpicsSignalRO, ROIPlugin,
                   TransformPlugin, ProcessPlugin)
from ophyd.areadetector.cam import AreaDetectorCam
from ophyd.areadetector.base import ADComponent, EpicsSignalWithRBV
from ophyd.areadetector.filestore_mixins import (FileStoreTIFFIterativeWrite,
                                                 FileStoreHDF5IterativeWrite,
                                                 FileStoreBase, new_short_uid)
from ophyd import Component as Cpt, Signal
from ophyd.utils import set_and_wait


# quick edit just to get the crrent PVs into BS, ED11mar17
# file should eventually have currents and other PVs for all electrometers,
# with indication of their permanent name assignments

#Prototype new electrometer, currently looking at XBPM2.
#ch1,2,3,4 = pads 2,3,5,4 respectively; thick active area
XBPM2ch1 = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}Current1:MeanValue_RBV', name='XBPM2ch1')
XBPM2ch2 = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}Current2:MeanValue_RBV', name='XBPM2ch2')
XBPM2ch3 = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}Current3:MeanValue_RBV', name='XBPM2ch3')
XBPM2ch4 = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}Current4:MeanValue_RBV', name='XBPM2ch4')

# this doesn't work, because the PV names do not end in .VAL ??
# full PV names are given in the above.

