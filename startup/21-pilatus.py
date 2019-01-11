print(f'Loading {__file__}')

from ophyd import ( Component as Cpt, ADComponent, Device, PseudoPositioner,
                    EpicsSignal, EpicsSignalRO, EpicsMotor,
                    ROIPlugin, ImagePlugin,
                    SingleTrigger, PilatusDetector,
                    OverlayPlugin, FilePlugin)

from ophyd.areadetector.filestore_mixins import FileStoreTIFFIterativeWrite
from ophyd.areadetector.cam import PilatusDetectorCam
from ophyd.areadetector.detectors import PilatusDetector
from ophyd.areadetector.base import EpicsSignalWithRBV as SignalWithRBV

from ophyd.utils import set_and_wait
from databroker.assets.handlers_base import HandlerBase
import os
import bluesky.plans as bp
import time
from nslsii.ad33 import StatsPluginV33
from nslsii.ad33 import SingleTriggerV33


class PilatusDetectorCamV33(PilatusDetectorCam):
    '''This is used to update the Pilatus to AD33.'''

    wait_for_plugins = Cpt(EpicsSignal, 'WaitForPlugins',
                           string=True, kind='config')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stage_sigs['wait_for_plugins'] = 'Yes'

    def ensure_nonblocking(self):
        self.stage_sigs['wait_for_plugins'] = 'Yes'
        for c in self.parent.component_names:
            cpt = getattr(self.parent, c)
            if cpt is self:
                continue
            if hasattr(cpt, 'ensure_nonblocking'):
                cpt.ensure_nonblocking()

    file_path = Cpt(SignalWithRBV, 'FilePath', string=True)
    file_name = Cpt(SignalWithRBV, 'FileName', string=True)
    file_template = Cpt(SignalWithRBV, 'FileName', string=True)        
    file_number = Cpt(SignalWithRBV, 'FileNumber')

class PilatusDetector(PilatusDetector):
    cam = Cpt(PilatusDetectorCamV33, 'cam1:')
    

class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
    ...


class Pilatus(SingleTriggerV33, PilatusDetector):
    tiff = Cpt(TIFFPluginWithFileStore,
               suffix="TIFF1:",
               write_path_template="/GPFS/xf12id1/data/PLACEHOLDER",  # override this on instances using instance.tiff.write_file_path
               root='/GPFS')

    roi1 = Cpt(ROIPlugin, 'ROI1:')
    roi2 = Cpt(ROIPlugin, 'ROI2:')
    roi3 = Cpt(ROIPlugin, 'ROI3:')
    roi4 = Cpt(ROIPlugin, 'ROI4:')

    stats1 = Cpt(StatsPluginV33, 'Stats1:', read_attrs=['total'])
    stats2 = Cpt(StatsPluginV33, 'Stats2:', read_attrs=['total'])
    stats3 = Cpt(StatsPluginV33, 'Stats3:', read_attrs=['total'])
    stats4 = Cpt(StatsPluginV33, 'Stats4:', read_attrs=['total'])

    over1 = Cpt(OverlayPlugin, 'Over1:')

    def set_primary_roi(self, num):
        st = f'stats{num}'
        self.read_attrs = [st, 'tiff']
        getattr(self, st).kind = 'hinted'


pil1M = Pilatus("XF:12IDC-ES:2{Det:1M}", name="pil1M") #, detector_id="SAXS")
pil1M.set_primary_roi(1)

pil300KW = Pilatus("XF:12IDC-ES:2{Det:300KW}", name="pil300KW") #, detector_id="WAXS")
pil300KW.set_primary_roi(1)

pil1M.tiff.write_path_template = '/GPFS/xf12id1/data/1M/images/%Y/%m/%d/'
pil300KW.tiff.write_path_template = '/GPFS/xf12id1/data/300KW/images/%Y/%m/%d/'


pil1mroi1 = EpicsSignal('XF:12IDC-ES:2{Det:1M}Stats1:Total_RBV', name='pil1mroi1')
pil1mroi2 = EpicsSignal('XF:12IDC-ES:2{Det:1M}Stats2:Total_RBV', name='pil1mroi2')
pil1mroi3 = EpicsSignal('XF:12IDC-ES:2{Det:1M}Stats3:Total_RBV', name='pil1mroi3')
pil1mroi4 = EpicsSignal('XF:12IDC-ES:2{Det:1M}Stats4:Total_RBV', name='pil1mroi4')

pil300kwroi1 = EpicsSignal('XF:12IDC-ES:2{Det:300KW}Stats1:Total_RBV', name='pil300kwroi1')
pil300kwroi2 = EpicsSignal('XF:12IDC-ES:2{Det:300KW}Stats2:Total_RBV', name='pil300kwroi2')
pil300kwroi3 = EpicsSignal('XF:12IDC-ES:2{Det:300KW}Stats3:Total_RBV', name='pil300kwroi3')
pil300kwroi4 = EpicsSignal('XF:12IDC-ES:2{Det:300KW}Stats4:Total_RBV', name='pil300kwroi4')

def det_exposure_time (t):
    pil1M.cam.acquire_time.put(t)
    pil300KW.cam.acquire_time.put(t)
    rayonix.cam.acquire_time.put(t)
    
def det_next_file (n):
    pil1M.cam.file_number.put(n)
    pil300KW.cam.file_number.put(n)    
    rayonix.cam.file_number.put(n) 

class FakeDetector(Device):
    acq_time = Cpt(Signal, value=10)

    _default_configuration_attrs = ('acq_time', )
    _default_read_attrs = ()

    def trigger(self):
        st = self.st = DeviceStatus(self)

        from threading import Timer

        self.t = Timer(self.acq_time.get(), st._finished)
        self.t.start()
        return st

fd = FakeDetector(name='fd')

pil1M.stats1.kind = 'hinted'
pil1M.stats1.total.kind = 'hinted'
pil1M.cam.ensure_nonblocking()

pil300KW.stats1.kind = 'hinted'
pil300KW.stats1.total.kind = 'hinted'
pil300KW.cam.ensure_nonblocking()

