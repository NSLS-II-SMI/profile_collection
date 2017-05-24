import time as ttime
import os
from ophyd import (PVPositioner, EpicsSignal, EpicsSignalRO, EpicsMotor,
                   Device, Signal, PseudoPositioner, PseudoSingle)
from ophyd.utils.epics_pvs import set_and_wait
from ophyd.ophydobj import StatusBase, MoveStatus
from ophyd import Component as Cpt
from scipy.interpolate import InterpolatedUnivariateSpline


ring_current = EpicsSignalRO('SR:C03-BI{DCCT:1}I:Real-I', name='ring_current')


class EpicsSignalOverridePrecRO(EpicsSignalRO):
    def __init__(self, *args, precision=4, **kwargs):
        self._precision = precision
        super().__init__(*args, **kwargs)

    @property
    def precision(self):
        return self._precision

class EpicsSignalOverridePrec(EpicsSignal):
    def __init__(self, *args, precision=4, **kwargs):
        self._precision = precision
        super().__init__(*args, **kwargs)

    @property
    def precision(self):
        return self._precision



class UndulatorGap(PVPositioner):
    # positioner signals
    setpoint = Cpt(EpicsSignalOverridePrec, '-Mtr:2}Inp:Pos')
    readback = Cpt(EpicsSignalOverridePrecRO, '-LEnc}Gap')
    stop_signal = Cpt(EpicsSignal, '-Mtr:2}Pos:STOP')
    actuate = Cpt(EpicsSignal, '-Mtr:2}Sw:Go')
    actuate_value = 1
    done = Cpt(EpicsSignalRO, '-Mtr:2}Sw:Serv-On')
    done_value = 0

    # correction function signals, need to be merged into single object
    corrfunc_en = Cpt(EpicsSignal, '-MtrC}EnaAdj:out')
    corrfunc_dis = Cpt(EpicsSignal, '-MtrC}DisAdj:out')
    corrfunc_sta = Cpt(EpicsSignal, '-MtrC}AdjSta:RB')

    # brake status
    # brake_on = Cpt(EpicsSignalRO, '-Mtr:2}Rb:Brk')

ivugap = UndulatorGap('SR:C12-ID:G1{IVU:1', name='ivugap',
                read_attrs=['readback', 'setpoint'],
                configuration_attrs=['corrfunc_sta',
                                     'corrfunc_dis',
                                     'corrfunc_en'])

class UndulatorElev(PVPositioner):
    # positioner signals
    setpoint = Cpt(EpicsSignalOverridePrec, '-Mtr:1}Inp:Pos')
    readback = Cpt(EpicsSignalOverridePrecRO, '-LEnc}VOffset')
    stop_signal = Cpt(EpicsSignal, '-Mtr:1}Pos:STOP')
    actuate = Cpt(EpicsSignal, '-Mtr:1}Sw:Go')
    actuate_value = 1
    done = Cpt(EpicsSignalRO, '-Mtr:1}Sw:Serv-On')
    done_value = 0

ivuelev = UndulatorElev('SR:C12-ID:G1{IVU:1', name='ivuelev',
                read_attrs=['readback', 'setpoint'],
                configuration_attrs=[])






