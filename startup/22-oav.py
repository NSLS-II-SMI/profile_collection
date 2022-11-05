from contextlib import nullcontext
import time as ttime  # tea time
from types import SimpleNamespace
from datetime import datetime
from ophyd import (ProsilicaDetector, SingleTrigger, TIFFPlugin,
                   ImagePlugin, StatsPlugin, DetectorBase, HDF5Plugin,
                   AreaDetector, EpicsSignal, EpicsSignalRO, ROIPlugin,
                   TransformPlugin, ProcessPlugin, Device, DeviceStatus,
                   OverlayPlugin, ProsilicaDetectorCam)

from ophyd.status import StatusBase
from ophyd.device import Staged
from ophyd.areadetector.cam import AreaDetectorCam
from ophyd.areadetector.base import ADComponent, EpicsSignalWithRBV
from ophyd.areadetector.filestore_mixins import (FileStoreTIFFIterativeWrite,
                                                 FileStoreHDF5IterativeWrite,
                                                 FileStoreBase, new_short_uid,
                                                 FileStoreIterativeWrite)
from ophyd import Component as Cpt, Signal
from ophyd.utils import set_and_wait
from pathlib import PurePath

from collections import OrderedDict

from nslsii.ad33 import SingleTriggerV33, StatsPluginV33, CamV33Mixin

class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
    """Add this as a component to detectors that write TIFFs."""
    ## LUTZ THIS MAY BE BROKEN NUKE IF XRAY EYES DO NOT WORK
    def describe(self):
        ret = super().describe()
        key = self.parent._image_name
        color_mode = self.parent.cam.color_mode.get(as_string=True)
        if color_mode == 'Mono':
            ret[key]['shape'] = [
                self.parent.cam.num_images.get(),
                self.array_size.height.get(),
                self.array_size.width.get()
                ]

        elif color_mode in ['RGB1', 'Bayer']:
            ret[key]['shape'] = [self.parent.cam.num_images.get(), *self.array_size.get()]
        else:
            raise RuntimeError("SHould never be here")

        cam_dtype = self.parent.cam.data_type.get(as_string=True)
        type_map = {'UInt8': '|u1', 'UInt16': '<u2', 'Float32':'<f4', "Float64":'<f8'}
        if cam_dtype in type_map:
            ret[key].setdefault('dtype_str', type_map[cam_dtype])


        return ret


class TIFFPluginEnsuredOff(TIFFPlugin):
    """Add this as a component to detectors that do not write TIFFs."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stage_sigs.update([('auto_save', 'No')])

class ProsilicaDetectorCamV33(ProsilicaDetectorCam):
    '''This is used to update the Standard Prosilica to AD33. It adds the
process
    '''
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

# class StandardProsilica(SingleTrigger, ProsilicaDetector):
#     image = Cpt(ImagePlugin, 'image1:')
#     stats1 = Cpt(StatsPlugin, 'Stats1:')
#     stats2 = Cpt(StatsPlugin, 'Stats2:')
#     stats3 = Cpt(StatsPlugin, 'Stats3:')
#     stats4 = Cpt(StatsPlugin, 'Stats4:')
#     stats5 = Cpt(StatsPlugin, 'Stats5:')
#     trans1 = Cpt(TransformPlugin, 'Trans1:')
#     roi1 = Cpt(ROIPlugin, 'ROI1:')
#     roi2 = Cpt(ROIPlugin, 'ROI2:')
#     roi3 = Cpt(ROIPlugin, 'ROI3:')
#     roi4 = Cpt(ROIPlugin, 'ROI4:')
#     proc1 = Cpt(ProcessPlugin, 'Proc1:')
#     over1 = Cpt(OverlayPlugin, 'Over1:')

#     # This class does not save TIFFs. We make it aware of the TIFF plugin
#     # only so that it can ensure that the plugin is not auto-saving.
#     tiff = Cpt(TIFFPluginEnsuredOff, suffix='TIFF1:')

#     @property
#     def hints(self):
#         return {'fields': [self.stats1.total.name]}

class StandardProsilicaV33(SingleTriggerV33, ProsilicaDetector):
    cam = Cpt(ProsilicaDetectorCamV33, 'cam1:')
    image = Cpt(ImagePlugin, 'image1:')
    stats1 = Cpt(StatsPluginV33, 'Stats1:')
    stats2 = Cpt(StatsPluginV33, 'Stats2:')
    stats3 = Cpt(StatsPluginV33, 'Stats3:')
    stats4 = Cpt(StatsPluginV33, 'Stats4:')
    stats5 = Cpt(StatsPluginV33, 'Stats5:')
    trans1 = Cpt(TransformPlugin, 'Trans1:')
    roi1 = Cpt(ROIPlugin, 'ROI1:')
    roi2 = Cpt(ROIPlugin, 'ROI2:')
    roi3 = Cpt(ROIPlugin, 'ROI3:')
    roi4 = Cpt(ROIPlugin, 'ROI4:')
    proc1 = Cpt(ProcessPlugin, 'Proc1:')
    over1 = Cpt(OverlayPlugin, 'Over1:')

    # This class does not save TIFFs. We make it aware of the TIFF plugin
    # only so that it can ensure that the plugin is not auto-saving.
    tiff = Cpt(TIFFPluginEnsuredOff, suffix='TIFF1:')

    @property
    def hints(self):
        return {'fields': [self.stats1.total.name]}


# class StandardProsilicaWithTIFF(StandardProsilica):
#     tiff = Cpt(TIFFPluginWithFileStore,
#                suffix='TIFF1:',
#                write_path_template='/nsls2/data/chx/legacy/data/%Y/%m/%d/',
#                root='/nsls2/data/chx/legacy/data')

class StandardProsilicaWithTIFFV33(StandardProsilicaV33):
    tiff = Cpt(TIFFPluginWithFileStore,
               suffix='TIFF1:',
               write_path_template='/nsls2/data/smi/legacy/data/%Y/%m/%d/',
               root='/nsls2/data/smi/legacy/data')
               #root='/XF11ID/data')


OAV = StandardProsilicaV33('XF:12IDC-BI{Cam:SAM}', name='OAV')
OAV.stage_sigs[OAV.cam.trigger_mode] = 'Fixed Rate' # was OFF
OAV_writing = StandardProsilicaWithTIFFV33('XF:12IDC-BI{Cam:SAM}', name='OAV')

OAV_writing.tiff.write_path_template = '/nsls2/data/smi/legacy/results/raw/OAV/%Y/%m/%d/'
OAV_writing.tiff.read_path_template = '/nsls2/data/smi/legacy/results/raw/OAV/%Y/%m/%d/'
OAV_writing.tiff.reg_root = '/nsls2/data/smi/legacy/results/raw/OAV/'

all_standard_pros = [OAV, OAV_writing,
                     ]

for camera in all_standard_pros:
    camera.read_attrs = ['stats1', 'stats2', 'stats3', 'stats4', 'stats5']
    # camera.tiff.read_attrs = []  # leaving just the 'image'
    for stats_name in ['stats1', 'stats2', 'stats3', 'stats4', 'stats5']:
        stats_plugin = getattr(camera, stats_name)
        stats_plugin.read_attrs = ['total']
    #The following line should only be used when running AD V33
    camera.cam.ensure_nonblocking()
    camera.stage_sigs[camera.cam.trigger_mode] = 'Fixed Rate'

#OAV.stage_sigs[OAV.cam.trigger_mode] = 'Fixed Rate'
#OAV_writing.stage_sigs[OAV_writing.cam.trigger_mode] = 'Fixed rate'

for camera in [OAV_writing]:
    camera.read_attrs.append('tiff')
    camera.tiff.read_attrs = []
    camera.cam.ensure_nonblocking()
    #camera.cam.stage_sigs['color_mode'] = 'Mono'
