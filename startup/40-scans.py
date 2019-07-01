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
        

