import time as ttime
import os
from ophyd import (PVPositioner, EpicsSignal, EpicsSignalRO, EpicsMotor,
                   Device, Signal, PseudoPositioner, PseudoSingle)
from ophyd.utils.epics_pvs import set_and_wait
from ophyd.ophydobj import StatusBase, MoveStatus
from ophyd.status import DeviceStatus
from ophyd import Component as Cpt
from ophyd import Component
from scipy.interpolate import InterpolatedUnivariateSpline
from epics import (caput, caget)
print(f'Loading {__file__}')



ring_current = EpicsSignalRO('SR:C03-BI{DCCT:1}I:Real-I', name='ring_current')
ring_ops = EpicsSignal('SR-OPS{}Mode-Sts', name='ring_ops', string=True)
mstr_shutter_enable = EpicsSignalRO('SR-EPS{PLC:1}Sts:MstrSh-Sts', name='mstr_shutter_enable')
ivu_permit = EpicsSignalRO('XF:12ID-CT{}Prmt:Remote-Sel', name='ivu_permit')
smi_shutter_enable = EpicsSignalRO('SR:C12-EPS{PLC:1}Sts:ID_BE_Enbl-Sts', name='smi_shutter_enable')

from bluesky.suspenders import SuspendFloor, SuspendBoolLow, SuspendBoolHigh
susp_beam = SuspendFloor( ring_current, 100, resume_thresh= 397 )
RE.install_suspender( susp_beam )

susp_smi_shutter = SuspendFloor( smi_shutter_enable, 0.1, resume_thresh= 0.9 )
RE.install_suspender( susp_smi_shutter )

#RE.install_suspender( susp_fe_shutter



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
    setpoint = Cpt(EpicsSignalOverridePrec, '-Ax:Gap}-Mtr-SP')
    readback = Cpt(EpicsSignalOverridePrecRO, '-Ax:Gap}-Mtr.RBV')
    stop_signal = Cpt(EpicsSignal, '-Ax:Gap}-Mtr.STOP')
    actuate = Cpt(EpicsSignal, '-Ax:Gap}-Mtr-Go')
    actuate_value = 1
    done = Cpt(EpicsSignalRO, '-Ax:Gap}-Mtr.MOVN')
    done_value = 0

    # correction function signals, need to be merged into single object
    #corrfunc_en = Cpt(EpicsSignal, '-MtrC}EnaAdj:out')
    #corrfunc_dis = Cpt(EpicsSignal, '-MtrC}DisAdj:out')
    #corrfunc_sta = Cpt(EpicsSignal, '-MtrC}AdjSta:RB')

    permit = Cpt(EpicsSignalRO, 'XF:12ID-CT{}Prmt:Remote-Sel',
                 name='permit',
                 add_prefix=())

    # brake status
    # brake_on = Cpt(EpicsSignalRO, '-Mtr:2}Rb:Brk')
    def set(self, new_position, **kwargs):
        if np.abs(self.position - new_position) < .2:
             return DeviceStatus(self, done=True, success=True)
        return super().set(new_position, **kwargs)

    def move(self, new_position, moved_cb=None, **kwargs):
        print(np.abs(self.position - new_position),  .2, self.position, new_position)
        if np.abs(self.position - new_position) < .2:
             if moved_cb is not None:
                 moved_cb(obj=self)
             return DeviceStatus(self, done=True, success=True)
        return super().move(new_position, moved_cb=moved_cb, **kwargs)

    def stop(self, *, success=False):
        if self.permit.get():
            super().stop(success=success)


class IVUBrakeCpt(Component):
    def maybe_add_prefix(self, instance, kw, suffix):
        if kw not in self.add_prefix:
            return suffix

        prefix = instance.prefix
        ''.join(instance.prefix.partition('IVU:1')[:2]) + '}'
        return prefix + suffix


class InsertionDevice(EpicsMotor):
    brake = IVUBrakeCpt(EpicsSignal,
                        write_pv='BrakesDisengaged-SP',
                        read_pv='BrakesDisengaged-Sts')

    def move(self, *args, **kwargs):
        set_and_wait(self.brake, 1)
        return super().move(*args, **kwargs)


'''
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
'''
