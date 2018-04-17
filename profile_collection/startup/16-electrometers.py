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
import bluesky.plans as bp

# quick edit just to get the crrent PVs into BS, ED11mar17
# file should eventually have currents and other PVs for all electrometers,
# with indication of their permanent name assignments

#Prototype new electrometer, currently looking at XBPM2.
#ch1,2,3,4 = pads 2,3,5,4 respectively; thick active area

#Lakeshore SP for temerpature

ls_temp1 = EpicsSignal('XF:12IDC:LS336:TC1:OUT1:SP', name='ls_temp1')



class XBPM(Device):
    ch1 = Cpt(EpicsSignal,'Current1:MeanValue_RBV')
    ch2 = Cpt(EpicsSignal, 'Current2:MeanValue_RBV')
    ch3 = Cpt(EpicsSignal, 'Current2:MeanValue_RBV')
    ch4 = Cpt(EpicsSignal, 'Current2:MeanValue_RBV')
    sumX = Cpt(EpicsSignal, 'SumX:MeanValue_RBV')
    sumY = Cpt(EpicsSignal, 'SumY:MeanValue_RBV')
    posX = Cpt(EpicsSignal,'PosX:MeanValue_RBV')
    posY = Cpt(EpicsSignal,'PosY:MeanValue_RBV')

xbpm1 = XBPM('XF:12IDA-BI:2{EM:BPM1}', name='xbpm1')
xbpm2 = XBPM('XF:12IDA-BI:2{EM:BPM2}', name='xbpm2')
xbpm3 = XBPM('XF:12IDB-BI:2{EM:BPM3}', name='xbpm3')

'''
XBPM2ch1 = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}Current1:MeanValue_RBV',
                       name='XBPM2ch1')
XBPM2ch2 = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}Current2:MeanValue_RBV',
                       name='XBPM2ch2')
XBPM2ch3 = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}Current3:MeanValue_RBV',
                       name='XBPM2ch3')
XBPM2ch4 = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}Current4:MeanValue_RBV',
                       name='XBPM2ch4')
XBPM2sumY = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}SumY:MeanValue_RBV', name='XBPM2sumY')
XBPM2sumX = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}SumX:MeanValue_RBV', name='XBPM2sumX')

XBPM2posX = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}PosX:MeanValue_RBV', name='XBPM2posX')
XBPM2posY = EpicsSignal('XF:12IDA-BI:2{EM:BPM2}PosY:MeanValue_RBV', name='XBPM2posY')
'''



# this doesn't work, because the PV names do not end in .VAL ??
# full PV names are given in the above.

class Keithly2450(Device):
    run = Cpt(EpicsSignal, 'run')
    busy = Cpt(EpicsSignalRO, 'busy')
    reading = Cpt(EpicsSignalRO, 'reading')

    send_done = Cpt(EpicsSignal, 'send_done')

    send_pgm = Cpt(EpicsSignal, 'send_pgm.AOUT')
    send_prt = Cpt(EpicsSignal, 'send_prt.AOUT')
    send_stb = Cpt(EpicsSignal, 'send_stb.SCAN', string=True)
    # calc_done = Cpt(EpicsSignalRO, 'calc_done')
    # fast_thold = Cpt(EpicsSignalRO, 'fast_thold')
    # parse_cmd = Cpt(EpicsSignalRO, 'parse_cmd')
    # fast_done = Cpt(EpicsSignalRO, 'fast_done')

    _default_read_attrs = ('reading', )
    _default_configuration_attrs = ('send_pgm', 'send_prt',
                                    'send_stb')

    def trigger(self):
        st = DeviceStatus(self)

        def keithy_done_monitor(old_value, value, **kwargs):
            if old_value == 1 and value == 0:
                st._finished()
                self.busy.clear_sub(keithy_done_monitor)

        self.busy.subscribe(keithy_done_monitor, run=False)
        self.run.put(1)
        return st


keithly2450 = Keithly2450('XF:12IDA{dmm:2}:K2450:1:', name='keithly2450')

hfmcurrent = EpicsSignal('XF:12IDA{dmm:2}:K2450:1:reading', name='hfmcurrent')
