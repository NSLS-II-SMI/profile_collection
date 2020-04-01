from ophyd import Signal

def gisaxs_scan(dets=[pil300KW, pil1M],
                trajectory='None',
                measurement_time=1,
                number_images=1,
                user_name='GF',
                md = None
                ):

    #Pull out the motor names from a cycler
    #ToDo: This can be improved
    motor_names = []
    for trajs in trajectory:
        for traj in trajs.items():
            if traj[0].name not in motor_names:
                motor_names.append(traj[0].name)

    # Check if what is planned is doable
    try:
        motor_names
        [det for det in dets]
    except:
        raise Exception('Motors or detectors not known')


    # Fixed values. If this values change over a scan, possibility to transform in ophyd signal and record over a scan
    base_md = {'plan_name': 'gi_scan',
               'geometry': 'reflection',
               'detectors': [det.name for det in dets],
               'user_name': user_name,
               'motor_scanned': motor_names,
               'exposure_time': measurement_time,
               'number_image': number_images,
               }

    base_md.update(md or {})

    all_detectors = dets  # Start a list off all the detector to trigger
    all_detectors.append(xbpm2)  # add all the values to track  for analysis
    all_detectors.append(xbpm3)  # add all the values to track  for analysis
    all_detectors.append(ring.current)  # add all the values to track  for analysis

    sd.baseline = []  # Initializatin of the baseline
    SMI.update_md()  # update metadata from the beamline


    # Update metadata for the detectors
    if 'pil300KW' in [det.name for det in dets]:
        all_detectors.append(waxs)  # Record the position of the WAXS arc and beamstop
        sd.baseline.append(smi_waxs_detector)  # Load metadata of WAXS detector in the baseline

    if 'pil1M' in [det.name for det in dets]:
        SMI_SAXS_Det()  # Update metadata from the beamline
        # Nothing added as detector so far since the saxs detector is not moved but anything could be implemented
        sd.baseline.append(smi_saxs_detector)  # Load metadata of SAXS detector in the baseline

    if 'rayonix' in [det.name for det in dets]:
        print('no metadata for the rayonix yet')


    # Update metadata for motors not used in baseline and add the motor as detector if so
    all_detectors.append(piezo) if 'piezo' in motor_names else sd.baseline.append(piezo)
    all_detectors.append(stage) if 'stage' in motor_names else sd.baseline.append(stage)
    all_detectors.append(prs) if 'prs' in motor_names else sd.baseline.append(prs)
    all_detectors.append(energy) if 'energy' in motor_names else sd.baseline.append(energy)
    all_detectors.append(waxs) if 'waxs' in motor_names else sd.baseline.append(waxs)
    all_detectors.append(ls) if 'ls' in motor_names else sd.baseline.append(ls)


    '''
    if 'piezo' in [motor_names]:
        all_detectors.append(piezo)
    else:
        sd.baseline.append(piezo)

    if 'stage' in [motor_names]:
        all_detectors.append(stage)
    else:
        sd.baseline.append(stage)

    if 'prs' in [motor_names]:
        all_detectors.append(prs)
    else:
        sd.baseline.append(prs)

    if 'energy' in [motor_names]:
        all_detectors.append(energy)
    else:
        sd.baseline.append(energy)

    if 'waxs' in [motor_names]:
        all_detectors.append(waxs)
        else:
        sd.baseline.append(waxs)
    '''

    sample_na = Signal(name='sample_name', value = 'test')
    all_detectors.append(sample_na)

    #Set exposure time
    det_exposure_time(measurement_time, number_images * measurement_time)

    bec.disable_plots()
    yield from bp.scan_nd(all_detectors, trajectory, md=base_md)
    bec.enable_plots()

    print('GISAXS scan with metadata done')

















def expert_gisaxs_scan(dets=[pil300KW, pil1M],
                       sam_name=['test'],
                       motors=[[waxs.arc], [piezo.th]],
                       motor_range=[[0, 13, 3], [0.1, 0.2, 3]],
                       measurement_time=1,
                       number_images=1,
                       user_name='IC',
                       realignement=[False],
                       x_trans=[0],
                       scan_type='linspace',  # list
                       md=None):
    # Check if what is planned is doable
    motor_names = [motor for moto in motors for motor in moto]
    try:
        motor_names
        [det for det in dets]
    except:
        raise Exception('Motors or detectors not known')

    # If this values change over a scan, possibility to transform in ophyd signal and record over a scan
    base_md = {'plan_name': 'gi_scan',
               'detectors': [det.name for det in dets],
               'user_name': user_name,
               'motor_scanned': [motor.name for motor in motors],
               'exposure_time': measurement_time,
               'number_image': number_images,
               'realignement': realignement,
               'x_trans': x_trans,
               }
    base_md.update(md or {})

    all_detectors = dets  # Start a list off all the detector to trigger
    all_detectors.append([xbpm2, xbpm3, ring.current])  # add all the values to track  for analysis
    sd.baseline = []  # Initializatin of the baseline
    SMI.get_md()  # update metadata from the beamline

    # Update metadata for the detectors
    if 'pil300KW' in [det.name for det in dets]:
        all_detectors.append(WAXS)  # Record the position of the WAXS arc and beamstop
        sd.baseline.append(smi_waxs_detector)  # Load metadata of WAXS detector in the baseline

    if 'pil1M' in [det.name for det in dets]:
        SMI_SAXS_Det()  # Update metadata from the beamline
        # Nothing added as detector so far since the saxs detector is not moved but anything could be implemented
        sd.baseline.append(smi_saxs_detector)  # Load metadata of SAXS detector in the baseline

    if 'rayonix' in [det.name for det in dets]:
        print('no metadata for the rayonix yet')

    # Update metadata for motors not used and add the motor as detector if so
    # ToDo: what other values do we need to track, lakeshore and ...
    if 'piezo' in [motor_names]:
        all_detectors.append(piezo)
    else:
        sd.baseline.append(piezo)

    if 'stage' in [motor_names]:
        all_detectors.append(stage)
    else:
        sd.baseline.append(stage)

    if 'prs' in [motor_names]:
        all_detectors.append(prs)
    else:
        sd.baseline.append(prs)

    if 'energy' in [motor_names]:
        all_detectors.append(energy)
    else:
        sd.baseline.append(energy)

    # Control if the input values are correct or if anything missing ...
    # ToDo: How to handle all the other parameters: check if it is a list, or len!=1 if so assertions needed plus assigned values
    #  Realignement and xtrans

    assert (len(motor_names) == len(motor_range),
            f'Number of motor range ({len(motor_range)}) is different from number of motors ({len(motor_names)})')
    motor_dic = {}
    for (motor, motor_ran) in zip(motors, motor_range):
        assert (len(motor_ran) == 3, f'Motor range ({motor_ran}) expect 3 values but only ({len(motor_ran)}) given')
        motor_dic = motor_dic + {motor.name: {motor_ran[0], motor_ran[1], motor_ran[2]}}

    if len(sam_name) != 1 and '.x' not in motor_names:
        raise Exception('There should be only one sample name since x is not scanned')
    elif len(sam_name) == 1 and '.x' in motor_names:
        motor_name = [motor for motor in motor_names if '.x' in motor][0]
        sam_name = [[sam_name]] * list(motor_dic[motor_name])[2]
    elif len(sam_name) != 1 and '.x' in motor_names:
        motor_name = [motor for motor in motor_names if '.x' in motor][0]
        assert (len(sam_name) == list(motor_dic[motor_name])[2],
                f'Number of sample({len(sam_name)}) is different from the ({list(motor_dic[motor_name])[2]}) x position given')

    # Create signal for exposure_time, sample_name
    # Record motor position as detector if moved and as baseline if not

    for i, (mot_pos, sam_nam) in enumerate(zip(motor_range, sam_name)):
        yield from bps.mv(mot_name, mot_pos)

        if i == 0 or reali:
            alignement_gisaxs(angle=alphai)
            if motor is 'th':
                yield from bps.mvr(piezo.th, mot_pos)
                sample_name = name_fmt.format(sample=sam_nam, motor=mot_pos)
            else:
                yield from bps.mvr(piezo.th, alphai)
                sample_name = name_fmt.format(sample=sam_nam, ai=alphai, motor=mot_pos)

        sample_id(user_name=user_name, sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.scan(dets, waxs, *waxs_arc)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)


def scan_gi_1motor_waxsscan(dets = [pil300KW, pil1M], sam_name=['test'], motor = 'energy', motor_range=[16000, 16100, 16200], waxs_arc = [0, 13, 3], t = 1, user_name = 'IC', reali = False, alphai = 0.15):
    det_exposure_time(t,t) 
    
    if motor is 'energy':
        name_fmt = '{sample}_ai{ai}deg_{motor}eV' 
        mot_name = energy
    elif motor is 'x':
        name_fmt = '{sample}_ai{ai}deg_x{motor}'
        mot_name = piezo.x
    elif motor is 'y':
        name_fmt = '{sample}_ai{ai}deg_y{motor}'
        mot_name = piezo.y
    elif motor is 'th':
        name_fmt = '{sample}_ai{motor}deg'
        mot_name = piezo.th
    else:
        raise Exception('unknown motor')

    if len(sam_name) == 1:
        sam_name = sam_name * len(motor_range)
    elif len(sam_name) != len(motor_range):
        raise Exception('Sample name length different from the number of motor positions')

    for i, (mot_pos, sam_nam) in enumerate(zip(motor_range, sam_name)):
        yield from bps.mv(mot_name, mot_pos)
        
        if i == 0 or reali:
            alignement_gisaxs(angle = alphai)
            if motor is 'th':
                yield from bps.mvr(piezo.th, mot_pos)
                sample_name = name_fmt.format(sample=sam_nam, motor=mot_pos)
            else:
                yield from bps.mvr(piezo.th, alphai)
                sample_name = name_fmt.format(sample=sam_nam, ai=alphai, motor=mot_pos)
        
        sample_id(user_name=user_name, sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.scan(dets, waxs, *waxs_arc)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)
    
    
    
        
def scan_trans_1motor_waxsscan(dets = [pil300KW, pil1M], sam_name=['test'], motor = 'energy', motor_range=[16000, 16100, 16200], waxs_arc = [0, 13, 3], t = 1, user_name = 'IC'):
    det_exposure_time(t,t) 
    
    if motor is 'energy':
        name_fmt = '{sample}_{motor}eV' 
        mot_name = energy
    elif motor is 'x':
        name_fmt = '{sample}_x{motor}'
        mot_name = piezo.x
    elif motor is 'y':
        name_fmt = '{sample}_y{motor}'
        mot_name = piezo.y
    else:
        raise Exception('unknown motor')

    if len(sam_name) == 1:
        sam_name = sam_name * len(motor_range)
    elif len(sam_name) != len(motor_range):
        raise Exception('Sample name length different from the number of motor positions')

    for mot_pos, sam_nam in zip(motor_range, sam_name):
        yield from bps.mv(mot_name, mot_pos)
        sample_name = name_fmt.format(sample=sam_nam, motor=mot_pos)
        sample_id(user_name=user_name, sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.scan(dets, waxs, *waxs_arc)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)
    
    
def scan_trans_1motor(dets = [pil300KW, pil1M], sam_name='test', motor = 'energy', motor_range=[16000, 16100, 16200], t = 1, user_name = 'IC', num=1):
    det_exposure_time(t,t) 
    
    if motor is 'energy':
        name_fmt = '{sample}_{motor}eV' 
        mot_name = energy
    elif motor is 'x':
        name_fmt = '{sample}_x{motor}'
        mot_name = piezo.x
    elif motor is 'y':
        name_fmt = '{sample}_y{motor}'
        mot_name = piezo.y
    else:
        raise Exception('unknown motor')
        
    if len(sam_name) == 1:
        sam_name = sam_name * len(motor_range)
    elif len(sam_name) != len(motor_range):
        raise Exception('Sample name length different from the number of motor positions')
           
           
    for mot_pos, sam_nam in zip(motor_range, sam_name):
        yield from bps.mv(mot_name, mot_pos)
        sample_name = name_fmt.format(sample=sam_nam, motor=mot_pos)
        sample_id(user_name=user_name, sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=num)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)
        

