
def expert_gisaxs_scan(dets = [pil300KW, pil1M],
                        sam_name=['test'], 
                        motors = [energy],
                        motor_range=[[16000, 16100, 16200]],
                        waxs_arc = [[0, 13, 3]],
                        measurement_time = 1,
                        number_images = 1,
                        user_name = 'IC',
                        alphai = 0.15,
                        realignement = False,
                        x_trans = None,
                        scan_type = 'Default',
                        md = None):


    #Check if what is planned is doable
    try:
        [motor for motor in motors]
        [det for det in dets]
    except:
        raise Exception('Motors or detectors not known')

    #If this values change over a scan, possibility to transform in ophyd signal and record over a scan
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

    all_detectors = dets    #Start a list off all the detector to trigger
    all_detectors.append([xbpm2, xbpm3, ring.current])  #add all the values to track  for analysis
    sd.baseline = []    #Initializatin of the baseline
    SMI.get_md()    #update metadata from the beamline

    #Update metadata for the detectors
    if 'pil300KW' in [det.name for det in dets]:
        all_detectors.append(WAXS) #Record the position of the WAXS arc and beamstop
        sd.baseline.append(smi_waxs_detector)   #Load metadata of WAXS detector in the baseline

    if 'pil1M' in [det.name for det in dets]:
        SMI_SAXS_Det()  #Update metadata from the beamline
        # Nothing added as detector so far since the saxs detector is not moved but anything could be implemented
        sd.baseline.append(smi_saxs_detector)   #Load metadata of SAXS detector in the baseline

    if 'rayonix' in [det.name for det in dets]:
        print('no metadata for the rayonix yet')


    #Update metadata for motors not used and add the motor as detector if so
    # ToDo: what other values do we need to track, lakeshore and ...
    if 'piezo' in [motor.name for motor in motors]: all_detectors.append(piezo)
    else: sd.baseline.append(piezo)

    if 'stage' in [motor.name for motor in motors]: all_detectors.append(stage)
    else: sd.baseline.append(stage)

    if 'prs' in [motor.name for motor in motors]: all_detectors.append(prs)
    else: sd.baseline.append(prs)
   
    if 'energy' in [motor.name for motor in motors]: all_detectors.append(energy)
    else: sd.baseline.append(energy)


    #Control if the input values are correct or if anything missing ...
    # ToDO: list the options of possible scans and figure out all the assumptions
    # ToDO: Can we write something general enough: or do we need

    assert(len(motors) == len(motor_range), f'Number of motor range ({len(motor_range)}) is different from number of motors ({len(motors)})')
    assert(len(sam_name) == len(motor_range), f'Number of sam_name ({len(sam_name)}) is different from number of motor range ({len(motor_range)})')   
    assert(scan_type in ['default_scan', 'list_scan', 'grid_scan', 'spiral_scan'], f'Scan ({scan_type}) not defined. Viable options: default_scan, list_scan, grid_scan, spiral_scan')

    if len(motors) != 1:
        #This need to be discussed
        raise Exception('Too many motors defined for GISAXS/GIWAXS')


    #Create signal for exposure_time, sample_name
    #Record motor position as detector if moved and as baseline if not


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
        

