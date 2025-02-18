print(f"Loading {__file__}")

from ophyd import (
    ProsilicaDetector,
    ImagePlugin,
    EpicsSignal,
    ROIPlugin,
    TransformPlugin,
    ProcessPlugin,
    OverlayPlugin,
    ProsilicaDetectorCam
)
from ophyd import Component as Cpt
from nslsii.ad33 import SingleTriggerV33, StatsPluginV33

class ProsilicaDetectorCamV33(ProsilicaDetectorCam):
    """This is used to update the Standard Prosilica to AD33. It adds the
process
    """
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

    def set_primary_roi(self, num):
        st = f"stats{num}"
        self.hints = {"fields": [getattr(self, st).total.name]}
        self.read_attrs = [st]


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

# OnAxis camera
OAV = StandardProsilicaV33('XF:12IDC-BI{Cam:SAM}', name='OAV')
OAV.stage_sigs[OAV.cam.trigger_mode] = 'Fixed Rate' # was OFF
OAV_writing = StandardProsilicaWithTIFFV33('XF:12IDC-BI{Cam:SAM}', name='OAV_writing', asset_path='webcam-1')

# Hex (top) camera
OAV2 = StandardProsilicaV33('XF:12IDC-BI{Cam:HEX}', name='OAV2')
OAV2.stage_sigs[OAV.cam.trigger_mode] = 'Fixed Rate' # was OFF
OAV2_writing = StandardProsilicaWithTIFFV33('XF:12IDC-BI{Cam:HEX}', name='OAV2', asset_path='webcam-2')

# Configure FS Camera
FS = StandardProsilicaV33("XF:12IDA-BI{Cam:FS}", name="FS")
FS.stage_sigs[FS.cam.trigger_mode] = 'Fixed Rate' # was OFF
FS_writing = StandardProsilicaWithTIFFV33("XF:12IDA-BI{Cam:FS}", name="FS", asset_path="webcam-3")

# Configure WBS Camera
WBS = StandardProsilicaV33('XF:12IDA-BI{Cam:WBStop}', name='WBStop')
WBS.stage_sigs[WBS.cam.trigger_mode] = 'Fixed Rate' # was OFF
WBS_writing = StandardProsilicaWithTIFFV33("XF:12IDA-BI{Cam:WBStop}", name="WBStop", asset_path="webcam-4")

# Configure VFM Camera
VFM = StandardProsilicaV33('XF:12IDA-BI{Cam:VFM}', name='VFM')
VFM.stage_sigs[VFM.cam.trigger_mode] = 'Fixed Rate' # was OFF
VFM_writing = StandardProsilicaWithTIFFV33("XF:12IDA-BI{Cam:VFM}", name="VFM", asset_path="webcam-5")


all_standard_pros = [OAV, OAV_writing, OAV2, OAV2_writing, FS, FS_writing, VFM, VFM_writing, WBS, WBS_writing]

for camera in all_standard_pros:
    camera.read_attrs = ['stats1', 'stats2', 'stats3', 'stats4', 'stats5']
    # camera.tiff.read_attrs = []  # leaving just the 'image'
    for stats_name in ['stats1', 'stats2', 'stats3', 'stats4', 'stats5']:
        stats_plugin = getattr(camera, stats_name)
        stats_plugin.read_attrs = ['total']
    #The following line should only be used when running AD V33
    camera.cam.ensure_nonblocking()
    camera.stage_sigs[camera.cam.trigger_mode] = 'Fixed Rate'

for camera in [OAV_writing, OAV2_writing, FS_writing, WBS_writing, VFM_writing]:
    camera.read_attrs.append('tiff')
    camera.tiff.read_attrs = []
    camera.cam.ensure_nonblocking()
    # When reading switch to mono colour mode
    #camera.cam.stage_sigs['color_mode'] = 'Mono'
