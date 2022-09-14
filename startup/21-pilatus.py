print(f"Loading {__file__}")

from ophyd import (
    Component as Cpt,
    ADComponent,
    Device,
    PseudoPositioner,
    EpicsSignal,
    EpicsSignalRO,
    EpicsMotor,
    ROIPlugin,
    ImagePlugin,
    TransformPlugin,
    SingleTrigger,
    PilatusDetector,
    OverlayPlugin,
    FilePlugin,
)

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
import pandas as pds


class PilatusDetectorCamV33(PilatusDetectorCam):
    """This is used to update the Pilatus to AD33."""

    wait_for_plugins = Cpt(EpicsSignal, "WaitForPlugins", string=True, kind="config")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stage_sigs["wait_for_plugins"] = "Yes"

    def ensure_nonblocking(self):
        self.stage_sigs["wait_for_plugins"] = "Yes"
        for c in self.parent.component_names:
            cpt = getattr(self.parent, c)
            if cpt is self:
                continue
            if hasattr(cpt, "ensure_nonblocking"):
                cpt.ensure_nonblocking()

    file_path = Cpt(SignalWithRBV, "FilePath", string=True)
    file_name = Cpt(SignalWithRBV, "FileName", string=True)
    file_template = Cpt(SignalWithRBV, "FileName", string=True)
    file_number = Cpt(SignalWithRBV, "FileNumber")


class PilatusDetector(PilatusDetector):
    cam = Cpt(PilatusDetectorCamV33, "cam1:")


class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
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

        cam_dtype = self.data_type.get(as_string=True)
        type_map = {'UInt8': '|u1', 'UInt16': '<u2', 'Float32':'<f4', "Float64":'<f8', 'Int32':'<i4'}
        if cam_dtype in type_map:
            ret[key].setdefault('dtype_str', type_map[cam_dtype])


        return ret



class Pilatus(SingleTriggerV33, PilatusDetector):
    tiff = Cpt(
        TIFFPluginWithFileStore,
        suffix="TIFF1:",
        # write_path_template="/GPFS/xf12id1/data/PLACEHOLDER",  # override this on instances using instance.tiff.write_file_path
        write_path_template="/ramdisk/PLACEHOLDER",
        root="/",
    )

    roi1 = Cpt(ROIPlugin, "ROI1:")
    roi2 = Cpt(ROIPlugin, "ROI2:")
    roi3 = Cpt(ROIPlugin, "ROI3:")
    roi4 = Cpt(ROIPlugin, "ROI4:")

    stats1 = Cpt(StatsPluginV33, "Stats1:", read_attrs=["total"])
    stats2 = Cpt(StatsPluginV33, "Stats2:", read_attrs=["total"])
    stats3 = Cpt(StatsPluginV33, "Stats3:", read_attrs=["total"])
    stats4 = Cpt(StatsPluginV33, "Stats4:", read_attrs=["total"])

    over1 = Cpt(OverlayPlugin, "Over1:")
    trans1 = Cpt(TransformPlugin, "Trans1:")

    threshold = Cpt(EpicsSignal, "cam1:ThresholdEnergy")
    energy = Cpt(EpicsSignal, "cam1:Energy")
    gain = Cpt(EpicsSignal, "cam1:GainMenu")
    apply = Cpt(EpicsSignal, "cam1:ThresholdApply")

    threshold_read = Cpt(EpicsSignal, "cam1:ThresholdEnergy_RBV")
    energy_read = Cpt(EpicsSignal, "cam1:Energy_RBV")
    gain_read = Cpt(EpicsSignal, "cam1:GainMenu_RBV")
    apply_read = Cpt(EpicsSignal, "cam1:ThresholdApply_RBV")

    def set_primary_roi(self, num):
        st = f"stats{num}"
        self.read_attrs = [st, "tiff"]
        getattr(self, st).kind = "hinted"

    def apply_threshold(self, energy=16.1, threshold=8.0, gain="autog"):
        if 1.5 < energy < 24:
            yield from bps.mv(self.energy, energy)
        else:
            raise ValueError(
                "The energy range for Pilatus is 1.5 to 24 keV. The entered value is {}".format(
                    energy
                )
            )

        if 1.5 < threshold < 24:
            yield from bps.mv(self.threshold, threshold)
        else:
            raise ValueError(
                "The threshold range for Pilatus is 1.5 to 24 keV. The entered value is {}".format(
                    threshold
                )
            )

        # That will need to be checked and tested
        if gain == "autog":
            yield from bps.mv(self.gain, 1)
        elif gain == "uhighg":
            yield from bps.mv(self.gain, 3)
        else:
            raise ValueError(
                "The gain used is unknown. It shoul be either autog or uhighg"
            )
        yield from bps.mv(self.apply, 1)

    def read_threshold(self):
        return self.energy_read, self.threshold_read, self.gain_read


def det_exposure_time(exp_t, meas_t=1):
    pil1M.cam.acquire_time.put(exp_t)
    pil1M.cam.acquire_period.put(exp_t + 0.001)
    pil1M.cam.num_images.put(int(meas_t / exp_t))
    pil300KW.cam.acquire_time.put(exp_t)
    pil300KW.cam.acquire_period.put(exp_t + 0.001)
    pil300KW.cam.num_images.put(int(meas_t / exp_t))
    pil900KW.cam.acquire_time.put(exp_t)
    pil900KW.cam.acquire_period.put(exp_t + 0.001)
    pil900KW.cam.num_images.put(int(meas_t / exp_t))
    # rayonix.cam.acquire_time.put(exp_t)
    # rayonix.cam.acquire_period.put(exp_t+0.01)
    # rayonix.cam.num_images.put(int(meas_t/exp_t))

    # See if amptek is connected
    try:
        amptek.mca.preset_real_time.put(exp_t)
    except:
        print("amptek disconnected")


def det_next_file(n):
    pil1M.cam.file_number.put(n)
    pil300KW.cam.file_number.put(n)
    # rayonix.cam.file_number.put(n)


class FakeDetector(Device):
    acq_time = Cpt(Signal, value=10)

    _default_configuration_attrs = ("acq_time",)
    _default_read_attrs = ()

    def trigger(self):
        st = self.st = DeviceStatus(self)

        from threading import Timer

        self.t = Timer(self.acq_time.get(), st._finished)
        self.t.start()
        return st


fd = FakeDetector(name="fd")


#####################################################
# Pilatus 1M definition

pil1M = Pilatus("XF:12IDC-ES:2{Det:1M}", name="pil1M")  # , detector_id="SAXS")
pil1M.set_primary_roi(1)

pil1M.tiff.write_path_template = (
    pil1M.tiff.read_path_template
) = "/nsls2/data/smi/legacy/results/raw/1M/%Y/%m/%d/"
# pil1M.tiff.write_path_template = pil1M.tiff.read_path_template = '/nsls2/data/smi/assets/default/%Y/%m/%d/'

# pil1M.tiff.write_path_template = pil1M.tiff.read_path_template = '/nsls2/data/smi/legacy/results/raw/1M/%Y/%m/%d/'

pil1mroi1 = EpicsSignal("XF:12IDC-ES:2{Det:1M}Stats1:Total_RBV", name="pil1mroi1")
pil1mroi2 = EpicsSignal("XF:12IDC-ES:2{Det:1M}Stats2:Total_RBV", name="pil1mroi2")
pil1mroi3 = EpicsSignal("XF:12IDC-ES:2{Det:1M}Stats3:Total_RBV", name="pil1mroi3")
pil1mroi4 = EpicsSignal("XF:12IDC-ES:2{Det:1M}Stats4:Total_RBV", name="pil1mroi4")

pil1M.stats1.kind = "hinted"
pil1M.stats1.total.kind = "hinted"
pil1M.cam.num_images.kind = "config"
pil1M.cam.ensure_nonblocking()


class PIL1MPositions(Device):
    x = Cpt(EpicsMotor, "X}Mtr")
    y = Cpt(EpicsMotor, "Y}Mtr")
    z = Cpt(EpicsMotor, "Z}Mtr")


pil1m_pos = PIL1MPositions("XF:12IDC-ES:2{Det:1M-Ax:", name="detector_saxs_pos")

for detpos in [pil1m_pos]:
    detpos.configuration_attrs = detpos.read_attrs


#####################################################
# Pilatus 300kw definition

# pil300KW = Pilatus("XF:12IDC-ES:2{Det:300KW}", name="pil300KW")  # , detector_id="WAXS")
# pil300KW.set_primary_roi(1)


# pil300KW.tiff.write_path_template = (
#     pil300KW.tiff.read_path_template
# ) = "/nsls2/xf12id2/data/300KW/images/%Y/%m/%d/"
# # pil300KW.tiff.write_path_template = pil300KW.tiff.read_path_template = '/nsls2/data/smi/legacy/results/raw/300KW/%Y/%m/%d/'

# pil300kwroi1 = EpicsSignal(
#     "XF:12IDC-ES:2{Det:300KW}Stats1:Total_RBV", name="pil300kwroi1"
# )
# pil300kwroi2 = EpicsSignal(
#     "XF:12IDC-ES:2{Det:300KW}Stats2:Total_RBV", name="pil300kwroi2"
# )
# pil300kwroi3 = EpicsSignal(
#     "XF:12IDC-ES:2{Det:300KW}Stats3:Total_RBV", name="pil300kwroi3"
# )
# pil300kwroi4 = EpicsSignal(
#     "XF:12IDC-ES:2{Det:300KW}Stats4:Total_RBV", name="pil300kwroi4"
# )

# pil300KW.stats1.kind = "hinted"
# pil300KW.stats1.total.kind = "hinted"
# pil300KW.cam.num_images.kind = "config"
# pil300KW.cam.ensure_nonblocking()
pil300KW = None

#####################################################
# Pilatus 900KW definition

pil900KW = Pilatus("XF:12IDC-ES:2{Det:900KW}", name="pil900KW")
pil900KW.set_primary_roi(1)

pil900KW.tiff.write_path_template = (
    pil900KW.tiff.read_path_template
# ) = "/nsls2/xf12id2/data/900KW/images/%Y/%m/%d/"
) = "/nsls2/data/smi/legacy/results/raw/900KW/%Y/%m/%d/"

# pil900KW.tiff.write_path_template = pil900KW.tiff.read_path_template = '/nsls2/data/smi/legacy/results/raw/900KW/%Y/%m/%d/'

pil900kwroi1 = EpicsSignal(
    "XF:12IDC-ES:2{Det:900KW}Stats1:Total_RBV", name="pil900kwroi1"
)
pil900kwroi1 = EpicsSignal(
    "XF:12IDC-ES:2{Det:900KW}Stats2:Total_RBV", name="pil900kwroi2"
)
pil900kwroi1 = EpicsSignal(
    "XF:12IDC-ES:2{Det:900KW}Stats3:Total_RBV", name="pil900kwroi3"
)
pil900kwroi1 = EpicsSignal(
    "XF:12IDC-ES:2{Det:900KW}Stats4:Total_RBV", name="pil900kwroi4"
)

pil900KW.stats1.kind = "hinted"
pil900KW.stats1.total.kind = "hinted"
pil900KW.cam.num_images.kind = "config"
pil900KW.cam.ensure_nonblocking()


# "multi_count" plan is dedicated to the time resolved Pilatus runs when the number of images in area detector is more than 1
def multi_count(detectors, *args, **kwargs):
    delay = detectors[0].cam.num_images.get() * detectors[0].cam.acquire_time.get() + 1
    yield from bp.count(detectors, *args, delay=delay, **kwargs)


class WAXS(Device):
    arc = Cpt(EpicsMotor, "WAXS:1-Ax:Arc}Mtr")
    bs_x = Cpt(EpicsMotor, "MCS:1-Ax:5}Mtr")
    bs_y = Cpt(EpicsMotor, "BS:WAXS-Ax:y}Mtr")

    def set(self, arc_value):
        st_arc = self.arc.set(arc_value)

        if self.arc.limits[0] <= arc_value <= 10.1:
            calc_value = self.calc_waxs_bsx(arc_value)

        elif 10.1 < arc_value <= 13:
            raise ValueError(
                "The waxs detector cannot be moved to {} deg until the new beamstop is mounted".format(
                    arc_value
                )
            )
        else:
            calc_value = 40
        st_x = self.bs_x.set(calc_value)
        return st_arc & st_x

    def calc_waxs_bsx(self, arc_value):
        # bsx_pos =-20.92 + 264 * np.tan(np.deg2rad(arc_value))
        # bsx_pos = -17.1 - 252*np.tan(np.deg2rad(arc_value)) # until 29-Mar-2022 when the waxs-arc failed , and MZ also raised the BS maually.
        bsx_pos = -16.64 - 252 * np.tan(np.deg2rad(arc_value))  # new zero position

        return bsx_pos


waxs = WAXS("XF:12IDC-ES:2{", name="waxs")
