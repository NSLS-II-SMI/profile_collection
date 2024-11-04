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

# class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
#     """Add this as a component to detectors that write TIFFs."""

#     def __init__(self, *args, md=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._md = md
#         self._asset_path = ''

#     def describe(self):
#         ret = super().describe()
#         key = self.parent._image_name
#         color_mode = self.parent.cam.color_mode.get(as_string=True)
#         if color_mode == 'Mono':
#             ret[key]['shape'] = [
#                 self.parent.cam.num_images.get(),
#                 self.array_size.height.get(),
#                 self.array_size.width.get()
#                 ]

#         elif color_mode in ['RGB1', 'Bayer']:
#             ret[key]['shape'] = [self.parent.cam.num_images.get(), *self.array_size.get()]
#         else:
#             raise RuntimeError("SHould never be here")

#         cam_dtype = self.parent.cam.data_type.get(as_string=True)
#         type_map = {'UInt8': '|u1', 'UInt16': '<u2', 'Float32':'<f4', "Float64":'<f8'}
#         if cam_dtype in type_map:
#             ret[key].setdefault('dtype_str', type_map[cam_dtype])

#         return ret
    
#     def _update_paths(self):
#         self.write_path_template = self.root_path_str + "%Y/%m/%d/"
#         self.read_path_template = self.root_path_str + "%Y/%m/%d/"
#         self.reg_root = self.root_path_str

#     @property
#     def root_path_str(self):
#         return f"/nsls2/data/smi/proposals/{self._md['cycle']}/{self._md['data_session']}/assets/{self._asset_path}/"

#     def stage(self):
#         self._update_paths()
#         return super().stage()


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


class StandardProsilicaWithTIFFV33(StandardProsilicaV33):
    tiff = Cpt(TIFFPluginWithFileStore,
               suffix='TIFF1:',
               md = RE.md,
               write_path_template='',
               root='')

    def __init__(self, *args, asset_path, **kwargs):
        self.asset_path = asset_path
        super().__init__(*args, **kwargs)
        self.tiff._asset_path = self.asset_path

# OnAxis camera
OAV = StandardProsilicaV33('XF:12IDC-BI{Cam:SAM}', name='OAV')
OAV.stage_sigs[OAV.cam.trigger_mode] = 'Fixed Rate' # was OFF
#OAV_writing = StandardProsilicaWithTIFFV33('XF:12IDC-BI{Cam:SAM}', name='OAV')
OAV_writing = StandardProsilicaWithTIFFV33('XF:12IDC-BI{Cam:SAM}', name='OAV_writing', asset_path='webcam-1')
# OAV_writing.tiff.write_path_template = '/nsls2/data/smi/legacy/results/raw/OAV/%Y/%m/%d/'
# OAV_writing.tiff.read_path_template = '/nsls2/data/smi/legacy/results/raw/OAV/%Y/%m/%d/'
# OAV_writing.tiff.reg_root = '/nsls2/data/smi/legacy/results/raw/OAV/'

# Hex (top) camera
OAV2 = StandardProsilicaV33('XF:12IDC-BI{Cam:HEX}', name='OAV2')
OAV2.stage_sigs[OAV.cam.trigger_mode] = 'Fixed Rate' # was OFF
OAV2_writing = StandardProsilicaWithTIFFV33('XF:12IDC-BI{Cam:HEX}', name='OAV2', asset_path='webcam-2')
# OAV2_writing.tiff.write_path_template = '/nsls2/data/smi/legacy/results/raw/OAV2/%Y/%m/%d/'
# OAV2_writing.tiff.read_path_template = '/nsls2/data/smi/legacy/results/raw/OAV2/%Y/%m/%d/'
# OAV2_writing.tiff.reg_root = '/nsls2/data/smi/legacy/results/raw/OAV2/'

all_standard_pros = [OAV, OAV_writing, OAV2, OAV2_writing]

for camera in all_standard_pros:
    camera.read_attrs = ['stats1', 'stats2', 'stats3', 'stats4', 'stats5']
    # camera.tiff.read_attrs = []  # leaving just the 'image'
    for stats_name in ['stats1', 'stats2', 'stats3', 'stats4', 'stats5']:
        stats_plugin = getattr(camera, stats_name)
        stats_plugin.read_attrs = ['total']
    #The following line should only be used when running AD V33
    camera.cam.ensure_nonblocking()
    camera.stage_sigs[camera.cam.trigger_mode] = 'Fixed Rate'

for camera in [OAV_writing, OAV2_writing]:
    camera.read_attrs.append('tiff')
    camera.tiff.read_attrs = []
    camera.cam.ensure_nonblocking()
    # When reading switch to mono colour mode
    #camera.cam.stage_sigs['color_mode'] = 'Mono'
