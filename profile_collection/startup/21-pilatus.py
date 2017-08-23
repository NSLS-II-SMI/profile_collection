from ophyd import ( Component as Cpt, ADComponent,
                    EpicsSignal, EpicsSignalRO,
                    ROIPlugin, StatsPlugin, ImagePlugin,
                    SingleTrigger, PilatusDetector,
                    OverlayPlugin, FilePlugin)

from ophyd.areadetector.filestore_mixins import FileStoreTIFFIterativeWrite

from ophyd.utils import set_and_wait
from filestore.handlers_base import HandlerBase
import fabio
import os


class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
    ...


class Pilatus(SingleTrigger, PilatusDetector):
    tiff = Cpt(TIFFPluginWithFileStore,
               suffix="TIFF1:",
               write_path_template="/data/PLACEHOLDER",  # override this on instances using instance.tiff.write_file_path
               root='/data',
               fs=db.fs)

    roi1 = Cpt(ROIPlugin, 'ROI1:')
    roi2 = Cpt(ROIPlugin, 'ROI2:')
    roi3 = Cpt(ROIPlugin, 'ROI3:')
    roi4 = Cpt(ROIPlugin, 'ROI4:')

    stats1 = Cpt(StatsPlugin, 'Stats1:')
    stats2 = Cpt(StatsPlugin, 'Stats2:')
    stats3 = Cpt(StatsPlugin, 'Stats3:')
    stats4 = Cpt(StatsPlugin, 'Stats4:')

    over1 = Cpt(OverlayPlugin, 'Over1:')


pil1M = Pilatus("XF:12IDC-ES:2{Det:1M}", name="pil1M", detector_id="SAXS")
pil300KW = Pilatus("XF:12IDC-ES:2{Det:300KW}", name="pil300KW", detector_id="WAXS")
pil1M.tiff.write_path_template = '/data/1M/images/'
pil300KW.tiff.write_path_template = '/data/300KW/images/'
