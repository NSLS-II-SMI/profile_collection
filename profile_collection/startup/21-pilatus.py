from ophyd import ( Component as Cpt, ADComponent,
                    EpicsSignal, EpicsSignalRO,
                    ROIPlugin, StatsPlugin, ImagePlugin,
                    SingleTrigger, PilatusDetector,
                    OverlayPlugin, FilePlugin)

from ophyd.areadetector.filestore_mixins import FileStoreTIFFIterativeWrite
from ophyd.areadetector.cam import PilatusDetectorCam
from ophyd.areadetector.detectors import PilatusDetector
from ophyd.areadetector.base import EpicsSignalWithRBV as SignalWithRBV

from ophyd.utils import set_and_wait
from databroker.assets.handlers_base import HandlerBase
import fabio
import os

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
               write_path_template="/data/PLACEHOLDER",  # override this on instances using instance.tiff.write_file_path
               root='/data',
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

pil1M.tiff.write_path_template = '/data/1M/images/%Y/%m/%d/'
pil300KW.tiff.write_path_template = '/data/300KW/images/%Y/%m/%d/'
