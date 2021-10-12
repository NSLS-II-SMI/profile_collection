print(f'Loading {__file__}')

import time as ttime
import numpy as np
from ophyd.status import SubscriptionStatus
from ophyd.mca import EpicsMCA
from ophyd import (Component as Cpt, Device, EpicsSignal, EpicsSignalRO,
                   EpicsSignalWithRBV, DeviceStatus, Signal)
from ophyd.device import (BlueskyInterface, Staged)


class AmptekMCA(EpicsMCA):
    # TODO: fix upstream
    preset_real_time = Cpt(EpicsSignal, '.PRTM')
    preset_live_time = Cpt(EpicsSignal, '.PLTM')
    elapsed_real_time = Cpt(EpicsSignalRO, '.ERTM')
    elapsed_live_time = Cpt(EpicsSignalRO, '.ELTM')

    # acquiring_status = Cpt(EpicsSignalRO, '.ACQG')

    check_acquiring = Cpt(EpicsSignal, 'CheckACQG')
    client_wait = Cpt(EpicsSignal, 'ClientWait')
    collect_data = Cpt(EpicsSignal, 'CollectData')
    enable_wait = Cpt(EpicsSignal, 'EnableWait')
    erase = Cpt(EpicsSignal, 'Erase')
    erase_start = Cpt(EpicsSignal, 'EraseStart')
    read_signal = Cpt(EpicsSignal, 'Read')
    read_callback = Cpt(EpicsSignal, 'ReadCallback')
    read_data_once = Cpt(EpicsSignal, 'ReadDataOnce')
    read_status_once = Cpt(EpicsSignal, 'ReadStatusOnce')
    set_client_wait = Cpt(EpicsSignal, 'SetClientWait')
    start = Cpt(EpicsSignal, 'Start')
    status = Cpt(EpicsSignal, 'Status')
    stop_signal = Cpt(EpicsSignal, 'Stop')
    when_acq_stops = Cpt(EpicsSignal, 'WhenAcqStops')
    why1 = Cpt(EpicsSignal, 'Why1')
    why2 = Cpt(EpicsSignal, 'Why2')
    why3 = Cpt(EpicsSignal, 'Why3')
    why4 = Cpt(EpicsSignal, 'Why4')


channels = np.linspace(0, 8191, 8192)
energy_channels = -165.83 + 3.134 * channels - 7.2124E-5 * channels**2 + 8.89825E-9 * channels**3
# amptek_energy = Signal(name='amptek_energy', value=energy_channels)

class Amptek(Device):
    mca = Cpt(AmptekMCA, 'mca1')
    dwell = Cpt(EpicsSignal, 'Dwell')
    energy_channels = Cpt(Signal, value=energy_channels)
    

class AmptekSoftTrigger(BlueskyInterface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._status = None
        self._acquisition_signal = self.mca.erase_start

        self.stage_sigs[self.mca.stop_signal] = 1
        
        self._count_signal = self.mca.preset_real_time
        self._count_time = None
        
        # Set kinds
        self.kind = 'hinted'
        self.mca.kind = 'hinted'
        self.mca.rois.kind = 'hinted'
        self._starting = None

    def stage(self, *args, **kwargs):
        # Set the labels for the count field to appear in the LiveTable, etc.
        # It's done here as it's the best place to read actual values from the label field
        # in case it's changed after the initialization of the object.
        for num in (0, 1, 2, 3, 4):
            roi_n = getattr(self.mca.rois, f'roi{num}')
            roi_n = getattr(self.mca.rois, f'roi{num}')
            roi_n.kind = 'hinted'
            roi_n.count.kind = 'hinted'
            label = roi_n.label.get()
            if label:
                roi_n.count.name = label
                for cpt in roi_n.component_names:
                    if cpt != 'count':
                        getattr(roi_n, cpt).name = f'{label}_{cpt}'
            else:
                roi_n.kind = 'normal'
                roi_n.count.kind = 'normal'

        super().stage(*args, **kwargs)
        if self._count_time is not None:
            self.stage_sigs[self._count_signal] = self._count_time

    def trigger(self, *args, **kwargs):
        "Trigger one acquisition."
        if self._staged != Staged.yes:
            raise RuntimeError("This detector is not ready to trigger."
                               "Call the stage() method before triggering.")

        def callback(value, old_value, **kwargs):
            print(f'  {self.name} old value {old_value} --> new_value {value}')
            if int(round(old_value)) == 1 and int(round(value)) == 0:
                if self._starting or self._starting is None:
                    self.starting = False
                    return True
                else:
                    self.starting = True
                return False

        status = SubscriptionStatus(self.mca.when_acq_stops, callback, run=False)
        print(f'  !!! attempting to put to {self._acquisition_signal.pvname} value 1')
        # ttime.sleep(0.1)
        timeout = 10  # s
        self._acquisition_signal.put(1)

        print(f'  !!! sleeping 0.1s after putting')
        t0 = ttime.time()
        print(f'Start waiting at {ttime.ctime(t0)}...')
        while True:
            ttime.sleep(0.01)
            if int(round(self.mca.when_acq_stops.get())) == 1:
                print(f'Success, {self.mca.when_acq_stops.pvname} was set to 1. Waited for {ttime.time() - t0}s.')
                break
            else:
                if ttime.time() - t0 > timeout:
                    print(f'Waited for {timeout}s, but the signal {self.mca.when_acq_stops.pvname} did not change. Attempting again.')
                    self._acquisition_signal.put(1)
                    break

        return status

    @property
    def count_time(self):
        '''Exposure time, as set by bluesky'''
        return self._count_time

    @count_time.setter
    def count_time(self, count_time):
        self._count_time = count_time


class SMIAmptek(AmptekSoftTrigger, Amptek):
    def __init__(self, prefix, *, read_attrs=None, configuration_attrs=None,
                 **kwargs):
        if read_attrs is None:
            read_attrs = ['mca.spectrum']

        if configuration_attrs is None:
            configuration_attrs = ['mca.preset_real_time',
                                   'mca.preset_live_time',
                                   ]

        super().__init__(prefix, read_attrs=read_attrs,
                         configuration_attrs=configuration_attrs, **kwargs)

amptek = SMIAmptek("XF:12IDC-ES:2{Det-Amptek:1}", name="amptek")
amptek.energy_channels.kind = 'normal'
