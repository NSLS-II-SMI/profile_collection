from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner
import pandas as pds
import os
import time
print(f'Loading {__file__}')

class PIL1MBS(Device):
    x = Cpt(EpicsMotor, 'IBB}Mtr')
    y = Cpt(EpicsMotor, 'IBM}Mtr')
    x_other = Cpt(EpicsMotor, 'OBB}Mtr')
    y_other = Cpt(EpicsMotor, 'OBM}Mtr')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x_center = None
        self.y_center = 13.1
        
pil1m_bs_rod = PIL1MBS('XF:12IDC-ES:2{BS:SAXS-Ax:', name='detector_saxs_bs_rod')


class SAXSPindiode(Device):
    x = Cpt(EpicsMotor, 'OBB}Mtr')
    y = Cpt(EpicsMotor, 'OBM}Mtr') 

pil1m_bs_pd = SAXSPindiode( 'XF:12IDC-ES:2{BS:SAXS-Ax:', name = 'detector_saxs_bs_pindiode' )


def beamstop_save():
    '''
    Save the current configuration
    '''
    #TODO: Do a list of a what motor we need to be stored
    #TODO: Add the pindiode beamstop to be read

    SMI_CONFIG_FILENAME = os.path.join(get_ipython().profile_dir.location,
                                       'smi_config.csv')


    #Beamstop position in x and y
    bs_pos_x = pil1m_bs_rod.x.position
    bs_pos_y = pil1m_bs_rod.y.position
    
    pdbs_pos_x = pil1m_bs_pd.x.position
    pdbs_pos_y = pil1m_bs_pd.y.position
    
    #collect the current positions of motors
    current_config = {
    'bs_pos_x'  : bs_pos_x,
    'bs_pos_y'  : bs_pos_y,
    'pdbs_pos_x'  : pdbs_pos_x,
    'pdbs_pos_y'  : pdbs_pos_y,
    'time'      : time.ctime()}
    
    current_config_DF = pds.DataFrame(data=current_config, index=[1])

    #load the previous config file
    smi_config = pds.read_csv(SMI_CONFIG_FILENAME, index_col=0)
    smi_config_update = smi_config.append(current_config_DF, ignore_index=True)

    #save to file
    smi_config_update.to_csv(SMI_CONFIG_FILENAME)
    global bsx_pos, bsy_pos, pdbsx_pos, pdbsy_pos
    bsx_pos, bsy_pos, pdbsx_pos, pdbsy_pos = beamstop_load()
    print(bsx_pos, bsx_pos, bsy_pos, pdbsx_pos, pdbsy_pos)


def beamstop_load():
    '''
    Save the configuration file
    '''
    SMI_CONFIG_FILENAME = os.path.join(get_ipython().profile_dir.location,
                                       'smi_config.csv')
    #collect the current positions of motors
    smi_config = pds.read_csv(SMI_CONFIG_FILENAME, index_col=0)
    
    bs_pos_x = smi_config.bs_pos_x.values[-1]
    bs_pos_y = smi_config.bs_pos_y.values[-1]
    pdbs_pos_x = smi_config.pdbs_pos_x.values[-1]
    pdbs_pos_y = smi_config.pdbs_pos_y.values[-1]
    #positions
    return bs_pos_x, bs_pos_y, pdbs_pos_x, pdbs_pos_y

bsx_pos, bsy_pos, pdbs_pos_x, pdbs_pos_y = beamstop_load()
