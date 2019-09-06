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
import pandas as pds


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
               #write_path_template="/GPFS/xf12id1/data/PLACEHOLDER",  # override this on instances using instance.tiff.write_file_path
               write_path_template="/ramdisk/PLACEHOLDER",
               root='/')

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

#pil1M.tiff.write_path_template = '/GPFS/xf12id1/data/1M/images/%Y/%m/%d/'
pil1M.tiff.write_path_template = '/ramdisk/1M/images/%Y/%m/%d/'
pil1M.tiff.read_path_template = '/GPFS/xf12id1/data/1M/images/%Y/%m/%d/'
pil300KW.tiff.write_path_template = '/GPFS/xf12id1/data/300KW/images/%Y/%m/%d/'
pil300KW.tiff.read_path_template = '/GPFS/xf12id1/data/300KW/images/%Y/%m/%d/'


pil1mroi1 = EpicsSignal('XF:12IDC-ES:2{Det:1M}Stats1:Total_RBV', name='pil1mroi1')
pil1mroi2 = EpicsSignal('XF:12IDC-ES:2{Det:1M}Stats2:Total_RBV', name='pil1mroi2')
pil1mroi3 = EpicsSignal('XF:12IDC-ES:2{Det:1M}Stats3:Total_RBV', name='pil1mroi3')
pil1mroi4 = EpicsSignal('XF:12IDC-ES:2{Det:1M}Stats4:Total_RBV', name='pil1mroi4')

pil300kwroi1 = EpicsSignal('XF:12IDC-ES:2{Det:300KW}Stats1:Total_RBV', name='pil300kwroi1')
pil300kwroi2 = EpicsSignal('XF:12IDC-ES:2{Det:300KW}Stats2:Total_RBV', name='pil300kwroi2')
pil300kwroi3 = EpicsSignal('XF:12IDC-ES:2{Det:300KW}Stats3:Total_RBV', name='pil300kwroi3')
pil300kwroi4 = EpicsSignal('XF:12IDC-ES:2{Det:300KW}Stats4:Total_RBV', name='pil300kwroi4')

def det_exposure_time(exp_t, meas_t=1):
    pil1M.cam.acquire_time.put(exp_t)
    pil1M.cam.acquire_period.put(exp_t+0.002)
    pil1M.cam.num_images.put(int(meas_t/exp_t))
    pil300KW.cam.acquire_time.put(exp_t)
    pil300KW.cam.acquire_period.put(exp_t+0.002)
    pil300KW.cam.num_images.put(int(meas_t/exp_t))
    rayonix.cam.acquire_time.put(exp_t)
    rayonix.cam.acquire_period.put(exp_t+0.01)
    rayonix.cam.num_images.put(int(meas_t/exp_t))
    
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


def beamstop_save():
    '''
    Save the current configuration
    '''
    #TODO: Do a list of a what motor we need to be stored
    #TODO: Add the pindiode beamstop to be read

    SMI_CONFIG_FILENAME = os.path.join(get_ipython().profile_dir.location,
                                       'smi_config-test.csv')


    #Beamstop position in x and y
    read_bs_x = yield from bps.read(pil1m_bs.x)
    bs_pos_x = read_bs_x['pil1m_bs_x']['value']
    
    read_bs_y = yield from bps.read(pil1m_bs.y)
    bs_pos_y = read_bs_y['pil1m_bs_y']['value']
    
    
    
    #collect the current positions of motors
    current_config = {
    'bs_pos_x'  : bs_pos_x,
    'bs_pos_y'  : bs_pos_y,
    'time'      : time.ctime()}
    
    current_config_DF = pds.DataFrame(data=current_config, index=[1])

    #load the previous config file
    smi_config = pds.read_csv(SMI_CONFIG_FILENAME, index_col=0)
    smi_config_update = smi_config.append(current_config_DF, ignore_index=True)

    #save to file
    smi_config_update.to_csv(SMI_CONFIG_FILENAME)
    global bsx_pos, bsy_pos
    bsx_pos, bsy_pos = beamstop_load()
    print(bsx_pos)


def beamstop_load():
    '''
    Save the configuration file
    '''
    SMI_CONFIG_FILENAME = os.path.join(get_ipython().profile_dir.location,
                                       'smi_config-test.csv')
    #collect the current positions of motors
    smi_config = pds.read_csv(SMI_CONFIG_FILENAME, index_col=0)
    
    bs_pos_x = smi_config.bs_pos_x.values[-1]
    bs_pos_y = smi_config.bs_pos_y.values[-1]
    #positions
    return bs_pos_x, bs_pos_y

bsx_pos, bsy_pos = beamstop_load()

