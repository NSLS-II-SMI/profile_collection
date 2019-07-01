print(f'Loading {__file__}')

from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt
# things to read at begining and end of every scan
sd.baseline = [energy, pil1m_pos, stage, prs, piezo]

# this is the default list for %ct
# BlueskyMagics.detectors = [FS]

def sample_id(*, user_name, sample_name, tray_number=None):
    RE.md['user_name'] = user_name
    RE.md['sample_name'] = sample_name
    if tray_number is None:
        RE.md.pop('tray_number', None)
    else:
        RE.md['tray_number'] = tray_number
    if tray_number is None:
        fname = f"{user_name}_{sample_name}"
    else:
        fname = f"{user_name}_{sample_name}_{tray_number}"
    # DIRTY HACK, do not copy
    pil1M.cam.file_name.put(fname)
    pil1M.cam.file_number.put(1)
    pil300KW.cam.file_name.put(fname)
    pil300KW.cam.file_number.put(1)    
    rayonix.cam.file_name.put(fname)
    rayonix.cam.file_number.put(1)    
    

def proposal_id(cycle_id,proposal_id):
    RE.md['proposal_id'] = proposal_id
    RE.md['cycle_id'] = cycle_id
    # 2018-04-10: Maksim asked Tom about why this 'put' does not create the folder,
    # Tom suggested to ask PoC to update AD installation.
    import stat
    
    newDir = "/GPFS/xf12id1/data/images/users/" + str(cycle_id) + "/" + str(proposal_id) + "/MAXS"
    #newDir = "/GPFS/xf12id1/data/images/users/{proposal_id}/MAXS"
    try:
        os.stat(newDir)
    except FileNotFoundError:
        os.makedirs(newDir)
        os.chmod(newDir, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)
    
    newDir = "/GPFS/xf12id1/data/images/users/" + str(cycle_id) + "/" + str(proposal_id) + "/1M"
    try:
        os.stat(newDir)
    except FileNotFoundError:
        os.makedirs(newDir)
        os.chmod(newDir, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)
    newDir = "/GPFS/xf12id1/data/images/users/" + str(cycle_id) + "/" + str(proposal_id) + "/300KW"
    try:
        os.stat(newDir)
    except FileNotFoundError:
        os.makedirs(newDir)
        os.chmod(newDir, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)
        
    newDir = "/GPFS/xf12id1/analysis/" + str(cycle_id) + "/" + str(proposal_id)
    try:
        os.stat(newDir)
    except FileNotFoundError:
        os.makedirs(newDir)
        os.chmod(newDir, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)
    
    pil1M.cam.file_path.put(f"/ramdisk/images/users/{cycle_id}/{proposal_id}/1M")
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/{cycle_id}/{proposal_id}/300KW")
    rayonix.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/{cycle_id}/{proposal_id}/MAXS")

def beamline_mode(mode=None):
    allowed_modes = ['sulfur', 'hard']
    assert mode in allowed_modes, f'Wrong mode: {mode}, must choose: {" or ".join(allowed_modes)}'
    if mode == 'hard':
        hfm.y.move(3.4) #3.6 for Rh stripe 11.6 for Pt
        hfm.x.move(-0.0)
        hfm.th.move(-0.1746) #-0.1746 for Rh stripe
        vfm.x.move(3.9)
        vfm.y.move(-3)
        vfm.th.move(-0.216)
        vdm.x.move(4.5)
        vdm.th.move(-0.2174)
        vdm.y.move(-2.44)
    elif mode == 'sulfur':
        hfm.y.move(-12.4)
        hfm.x.move(-0.055)
        hfm.th.move(-0.1751)
        vfm.x.move(-11.7)
        vfm.y.move(-4.7)
        vfm.th.move(-0.35)
        vdm.x.move(-11.7)
        vdm.th.move(-0.36)
        vdm.y.move(-2.014)


def fly_scan(det, motor, cycle=1, cycle_t=10, phi = -0.6):
    start = phi +10
    stop = phi-10
    acq_time = cycle * cycle_t
    yield from bps.mv(motor, start)
    #yield from bps.mv(attn_shutter, 'Retract')
    det.stage()
    det.cam.acquire_time.put(acq_time)
    print(f'Acquire time before staging: {det.cam.acquire_time.get()}')
    st = det.trigger()
    for i in range(cycle):
        yield from list_scan([], motor, [start, stop, start])
    while not st.done:
        pass
    det.unstage()
    print(f'We are done after {acq_time}s of waiting')
    #yield from bps.mv(attn_shutter, 'Insert')

manual_PID_disable_pitch = EpicsSignal('XF:12IDB-BI:2{EM:BPM3}fast_pidY_incalc.CLCN', name='manual_PID_disable_pitch')
manual_PID_disable_roll = EpicsSignal('XF:12IDB-BI:2{EM:BPM3}fast_pidX_incalc.CLCN', name='manual_PID_disable_roll')

def feedback(action=None):
    allowed_actions = ['on', 'off']
    assert action in allowed_actions, f'Wrong action: {mode}, must choose: {" or ".join(allowed_actions)}'
    if action == 'off':
        manual_PID_disable_pitch.set('1')
        manual_PID_disable_roll.set('1')
    elif action == 'on':
        manual_PID_disable_pitch.set('0')
        manual_PID_disable_roll.set('0')
        
        
        
        
        
        

def read_current_config_position(): 
    current_config = {
        'config_names':   'current',
        'hfm_y'     :   hfm.y.position,
        'hfm_x'     :   hfm.x.position,
        'hfm_th'    :   hfm.th.position,
        'vfm_y'     :   vfm.y.position,
        'vfm_x'     :   vfm.x.position,
        'vfm_th'    :   vfm.th.position,
        'vdm_y'     :   vdm.y.position,
        'vdm_x'     :   vdm.x.position,
        'vdm_th'    :   vdm.th.position,
        'ssa_h'     :   ssa.h.position,
        'ssa_hg'    :   ssa.hg.position,
        'ssa_v'     :   ssa.v.position,
        'ssa_vg'    :   ssa.vg.position,
        'cslit_h'   :   cslit.h.position,
        'cslit_hg'  :   cslit.hg.position,
        'cslit_v'   :   cslit.v.position,
        'cslit_vg'  :   cslit.vg.position,
        'eslit_h'   :   eslit.h.position,
        'eslit_hg'  :   eslit.hg.position,
        'eslit_v'   :   eslit.v.position,
        'eslit_vg'  :   eslit.vg.position,
        'crl_lens1' :   crl.lens1.position,
        'crl_lens2' :   crl.lens2.position,
        'crl_lens3' :   crl.lens3.position,
        'crl_lens4' :   crl.lens4.position,
        'crl_lens5' :   crl.lens5.position,
        'crl_lens6' :   crl.lens6.position,
        'crl_lens7' :   crl.lens7.position,
        'crl_lens8' :   crl.lens8.position,
        'dsa_x'     :   dsa.x.position,
        'dsa_y'     :   dsa.y.position,
        'energy'    :   energy.energy.position,
        'dcm_height':   dcm_config.height.position,
        'dcm_pitch' :   dcm_config.pitch.position,    
        'dcm_roll'  :   dcm_config.roll.position,     
        'dcm_theta' :   dcm_config.theta.position,
        'dcm_harmonic': dcm.target_harmonic.value,
        'ztime'     :   time.ctime()
    }
    return current_config                                                                                              
 
    
def create_config_mode(mode_name):
    SMI_CONFIG_FILENAME = '/home/xf12id/smi/config/smi_setup.csv'

    #collect the current positions of motors
    new_config = read_current_config_position()
    
    new_config_DF = pds.DataFrame(data=new_config, index=[1])
    new_config_DF.at[1, 'config_names']=mode_name

    #load the previous config file
    smi_config = pds.read_csv(SMI_CONFIG_FILENAME)
    smi_config_update = smi_config.append(new_config_DF, ignore_index=True, sort=False)

    #save to file
    if mode_name not in smi_config.config_names.values:
        smi_config_update.to_csv(SMI_CONFIG_FILENAME, index=False)
    else: raise Exception('configuration already existing')


def compare_config(mode_name):
    SMI_CONFIG_FILENAME = '/home/xf12id/smi/config/smi_setup.csv'
    smi_config = pds.read_csv(SMI_CONFIG_FILENAME)
    smi_config = pds.DataFrame(data=smi_config)

    #collect the current positions of motors
    current_config = pds.DataFrame(data=read_current_config_position(), index=[1]).sort_index(axis=1)

    if mode_name not in smi_config.config_names.values:
        raise Exception('configuration not existing')
    else:
        new_config = smi_config[smi_config.config_names==mode_name]
    
    for current_con, new_con, ind in zip(current_config.iloc[0], new_config.iloc[0], new_config):
        if current_con != new_con:
            print('difference in %s: the current value is %s, the new one is %s'%(ind, current_con, new_con))
    

def update_config_mode(mode_name, motor_name, motor_value):
    SMI_CONFIG_FILENAME = '/home/xf12id/smi/config/smi_setup.csv'
    smi_config = pds.read_csv(SMI_CONFIG_FILENAME)
    smi_config = pds.DataFrame(data=smi_config)
    
    if mode_name not in smi_config.config_names.values:
        raise Exception('configuration not existing')
    else:
        print('OK')
        #Select the row
        upd_config = smi_config[smi_config.config_names==mode_name]
        print(upd_config)
        print('OK1')
        upd_config[motor_name]= motor_value
          
        #Erase the configuration and save the new one
        smi_config_update = smi_config[smi_config['config_names']!=mode_name]
        
        #Save the new one
        smi_config_update = smi_config_update.append(upd_config, ignore_index=True)
        smi_config_update.to_csv(SMI_CONFIG_FILENAME, index=False)
  


def move_new_config(mode_name):
    SMI_CONFIG_FILENAME = '/home/xf12id/smi/config/smi_setup.csv'

    # load the previous config file
    smi_config = pds.read_csv(SMI_CONFIG_FILENAME, index_col=0)
    current_config = read_current_config_position()
    '''
    if mode_name in smi_config['mode']:
        smi_new_config = smi_config[mode_name]
    else: raise Exception('Unknown configuration')
    '''
    print('Are you sure you really want to move to %s configuration?'%mode_name)
    response = input('    Are you sure? (y/[n]) ')
        
    if response is 'y' or response is 'Y':
        print('it will move in the future')
    else:
        print('No move was made.')

    '''
    energy.target_harmonic(smi_new_config['dcm_harmonic'])
    energy.move(smi_new_config['energy'])
    
    yield from bps.move(hfm.y,  smi_new_config['hfm_y'])
    yield from bps.move(hfm.x,  smi_new_config['hfm_x'])
    yield from bps.move(hfm.th, smi_new_config['hfm_th'])
    yield from bps.move(vfm.y,  smi_new_config['vfm_y'])
    yield from bps.move(vfm.x,  smi_new_config['vfm_x'])
    yield from bps.move(vfm.th,  smi_new_config['vfm_th'])
    yield from bps.move(vdm.y,  smi_new_config['vdm_y'])
    yield from bps.move(vdm.x,  smi_new_config['vdm_x'])
    yield from bps.move(vdm.th,  smi_new_config['vdm_th'])
    
    yield from bps.move(dcm_config.pitch,  smi_new_config['dcm_pitch'])
    yield from bps.move(dcm_config.roll,  smi_new_config['dcm_roll'])
    yield from bps.move(dcm_config.height,  smi_new_config['dcm_height'])
    yield from bps.move(dcm_config.theta,  smi_new_config['dcm_theta'])
    
    yield from bps.move(ssa.h,  smi_new_config['ssa_h'])
    yield from bps.move(ssa.hg,  smi_new_config['ssa_hg'])
    yield from bps.move(ssa.v,  smi_new_config['ssa_v'])
    yield from bps.move(ssa.vg,  smi_new_config['ssa_vg'])

    yield from bps.move(crl.lens1,  smi_new_config['crl_lens1'])
    yield from bps.move(crl.lens2,  smi_new_config['crl_lens2'])
    yield from bps.move(crl.lens3,  smi_new_config['crl_lens3'])
    yield from bps.move(crl.lens4,  smi_new_config['crl_lens4'])
    yield from bps.move(crl.lens5,  smi_new_config['crl_lens5'])
    yield from bps.move(crl.lens6,  smi_new_config['crl_lens6'])
    yield from bps.move(crl.lens7,  smi_new_config['crl_lens7'])
    yield from bps.move(crl.lens8,  smi_new_config['crl_lens8'])
    
    yield from bps.move(cslit.h,  smi_new_config['cslit_h'])
    yield from bps.move(cslit.hg,  smi_new_config['cslit_hg'])
    yield from bps.move(cslit.v,  smi_new_config['cslit_v'])
    yield from bps.move(cslit.vg,  smi_new_config['cslit_vg'])
    yield from bps.move(eslit.h,  smi_new_config['eslit_h'])
    yield from bps.move(eslit.hg,  smi_new_config['eslit_hg'])
    yield from bps.move(eslit.v,  smi_new_config['eslit_v'])
    yield from bps.move(eslit.vg,  smi_new_config['eslit_vg'])
    yield from bps.move(dsa.x,  smi_new_config['dsa_x'])
    yield from bps.move(dsa.y,  smi_new_config['dsa_y'])
    '''

