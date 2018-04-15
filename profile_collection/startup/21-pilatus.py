from ophyd import ( Component as Cpt, ADComponent, Device, PseudoPositioner,
                    EpicsSignal, EpicsSignalRO, EpicsMotor,
                    ROIPlugin, StatsPlugin, ImagePlugin,
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

class PilatusDetectorCam(PilatusDetectorCam):
    file_path = Cpt(SignalWithRBV, 'FilePath', string=True)
    file_name = Cpt(SignalWithRBV, 'FileName', string=True)
    file_template = Cpt(SignalWithRBV, 'FileName', string=True)        
    file_number = Cpt(SignalWithRBV, 'FileNumber')

class PilatusDetector(PilatusDetector):
    cam = Cpt(PilatusDetectorCam, 'cam1:')
    

class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
    ...


class Pilatus(SingleTrigger, PilatusDetector):
    tiff = Cpt(TIFFPluginWithFileStore,
               suffix="TIFF1:",
               write_path_template="/GPFS/xf12id1/data/PLACEHOLDER",  # override this on instances using instance.tiff.write_file_path
               root='/GPFS',
               reg=db.reg)

    roi1 = Cpt(ROIPlugin, 'ROI1:')
    roi2 = Cpt(ROIPlugin, 'ROI2:')
    roi3 = Cpt(ROIPlugin, 'ROI3:')
    roi4 = Cpt(ROIPlugin, 'ROI4:')

    stats1 = Cpt(StatsPlugin, 'Stats1:', read_attrs=['total'])
    stats2 = Cpt(StatsPlugin, 'Stats2:', read_attrs=['total'])
    stats3 = Cpt(StatsPlugin, 'Stats3:', read_attrs=['total'])
    stats4 = Cpt(StatsPlugin, 'Stats4:', read_attrs=['total'])

    over1 = Cpt(OverlayPlugin, 'Over1:')

    def set_primary_roi(self, num):
        st = f'stats{num}'
        self.hints = {'fields': [getattr(self, st).total.name]}
        self.read_attrs = [st, 'tiff']
        
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


