print(f"Loading {__file__}")

from ophyd import EpicsMotor, EpicsSignal, Device, Component as C

import time as ttime  # tea time
from datetime import datetime
from ophyd import (
    ProsilicaDetector,
    SingleTrigger,
    TIFFPlugin,
    ImagePlugin,
    DetectorBase,
    HDF5Plugin,
    AreaDetector,
    EpicsSignal,
    EpicsSignalRO,
    ROIPlugin,
    TransformPlugin,
    ProcessPlugin,
    MarCCDDetector,
)
from ophyd.areadetector.cam import AreaDetectorCam
from ophyd.areadetector.base import ADComponent, EpicsSignalWithRBV
from ophyd.areadetector.filestore_mixins import (
    FileStoreTIFFIterativeWrite,
    FileStoreHDF5IterativeWrite,
    FileStoreBase,
    new_short_uid,
)

from ophyd.areadetector.base import EpicsSignalWithRBV as SignalWithRBV
from ophyd import Component as Cpt, Signal
from ophyd.utils import set_and_wait

from ophyd.areadetector.cam import MarCCDDetectorCam
from nslsii.ad33 import StatsPluginV33 as StatsPlugin


# White Beam Stop camera ROI detectors
WBScamroi1 = EpicsSignal("XF:12IDA-BI{Cam:WBStop}Stats1:Total_RBV", name="WBScamroi1")
WBScamroi2 = EpicsSignal("XF:12IDA-BI{Cam:WBStop}Stats2:Total_RBV", name="WBScamroi2")
WBScamroi3 = EpicsSignal("XF:12IDA-BI{Cam:WBStop}Stats3:Total_RBV", name="WBScamroi3")
WBScamroi4 = EpicsSignal("XF:12IDA-BI{Cam:WBStop}Stats4:Total_RBV", name="WBScamroi4")
# Fluorescent Screen camera ROI detectors
FScamroi1 = EpicsSignal("XF:12IDA-BI{Cam:FS}Stats1:Total_RBV", name="FScamroi1")
FScamroi2 = EpicsSignal("XF:12IDA-BI{Cam:FS}Stats2:Total_RBV", name="FScamroi2")
FScamroi3 = EpicsSignal("XF:12IDA-BI{Cam:FS}Stats3:Total_RBV", name="FScamroi3")
FScamroi4 = EpicsSignal("XF:12IDA-BI{Cam:FS}Stats4:Total_RBV", name="FScamroi4")
# VFM camera ROI detectors
VFMcamroi1 = EpicsSignal("XF:12IDA-BI{Cam:VFM}Stats1:Total_RBV", name="VFMcamroi1")
VFMcamroi2 = EpicsSignal("XF:12IDA-BI{Cam:VFM}Stats2:Total_RBV", name="VFMcamroi2")
VFMcamroi3 = EpicsSignal("XF:12IDA-BI{Cam:VFM}Stats3:Total_RBV", name="VFMcamroi3")
VFMcamroi4 = EpicsSignal("XF:12IDA-BI{Cam:VFM}Stats4:Total_RBV", name="VFMcamroi4")
# HEX camera ROI detectors
HEXcamroi1 = EpicsSignal("XF:12IDC-BI{Cam:HEX}Stats1:Total_RBV", name="HEXcamroi1")
HEXcamroi2 = EpicsSignal("XF:12IDC-BI{Cam:HEX}Stats2:Total_RBV", name="HEXcamroi2")
HEXcamroi3 = EpicsSignal("XF:12IDC-BI{Cam:HEX}Stats3:Total_RBV", name="HEXcamroi3")
HEXcamroi4 = EpicsSignal("XF:12IDC-BI{Cam:HEX}Stats4:Total_RBV", name="HEXcamroi4")

# To trigger TIFF image saving from a camera
FScamera = EpicsSignal("XF:12IDA-BI{Cam:FS}TIFF1:WriteFile", name="FScamera")
WBScamera = EpicsSignal("XF:12IDA-BI{Cam:WBStop}TIFF1:WriteFile", name="WBScamera")
VFMcamera = EpicsSignal("XF:12IDA-BI{Cam:VFM}TIFF1:WriteFile", name="VFMcamera")


class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
    def __init__(self, *args, md=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._md = md
        self._asset_path = None

    def _update_paths(self):
        self.write_path_template = self.root_path_str
        self.read_path_template = self.root_path_str

    @property
    def root_path_str(self):
        root_path = f"/nsls2/data/smi/proposals/{self._md['cycle']}/{self._md['data_session']}/assets/{self._asset_path}/%Y/%m/%d/"
        return root_path

    def stage(self):
        if self._asset_path:
            self._update_paths(self)
        return super().stage()

class HDF5PluginWithFileStore(HDF5Plugin, FileStoreHDF5IterativeWrite):
    def get_frames_per_point(self):
        return self.parent.cam.num_images.get()



class StandardProsilica(SingleTrigger, ProsilicaDetector):
    image = Cpt(ImagePlugin, "image1:")
    stats1 = Cpt(StatsPlugin, "Stats1:")
    stats2 = Cpt(StatsPlugin, "Stats2:")
    stats3 = Cpt(StatsPlugin, "Stats3:")
    stats4 = Cpt(StatsPlugin, "Stats4:")
    stats5 = Cpt(StatsPlugin, "Stats5:")
    trans1 = Cpt(TransformPlugin, "Trans1:")
    roi1 = Cpt(ROIPlugin, "ROI1:")
    roi2 = Cpt(ROIPlugin, "ROI2:")
    roi3 = Cpt(ROIPlugin, "ROI3:")
    roi4 = Cpt(ROIPlugin, "ROI4:")
    proc1 = Cpt(ProcessPlugin, "Proc1:")

    def set_primary_roi(self, num):
        st = f"stats{num}"
        self.hints = {"fields": [getattr(self, st).total.name]}
        self.read_attrs = [st]


class StandardProsilicaWithTIFF(StandardProsilica):
    tiff = Cpt(
        TIFFPluginWithFileStore,
        suffix="TIFF1:",
        md=RE.md,
#        asset_path='prosilica',  # TODO:
        write_path_template="/tmp/%Y/%m/%d/",
        read_path_template="/tmp/%Y/%m/%d/",
        root="/tmp/",
    )

    def __init__(self, *args, **kwargs):
        self.asset_path = kwargs.pop("asset_path", None)
        super().__init__(*args, **kwargs)
        self.tiff._asset_path = self.asset_path

# If asset_path is not defined, TIFFPluginWithFileStore will fall back to hardcoded paths
FS = StandardProsilica("XF:12IDA-BI{Cam:FS}", name="FS", asset_path="webcam-3")

#FS = StandardProsilica("XF:12IDA-BI{Cam:FS}", name="FS")
FS.read_attrs = ["stats1", "stats2", "stats3", "stats4", "stats5"]
FS.stats1.read_attrs = ["total"]
FS.stats2.read_attrs = ["total"]
FS.stats3.read_attrs = ["total"]
FS.stats4.read_attrs = ["total"]
FS.stats5.read_attrs = ["total"]

FS.stats2.total.kind = "hinted"
FS.stats3.total.kind = "hinted"
FS.stats5.total.kind = "hinted"
# FS.configuration_attrs = ['cam.acquire_time']

# VFM = StandardProsilica('XF:12IDA-BI{Cam:VFM}', name='VFM')
# VFM.read_attrs = ['stats1', 'stats2']
# VFM.stats1.read_attrs = ['total']
# VFM.stats2.read_attrs = ['total']
# VFM.stats3.read_attrs = ['total']
# VFM.stats4.read_attrs = ['total']
# VFM.configuration_attrs = ['cam.acquire_time']
