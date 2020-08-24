####line scan



def run_gi_sweden_GISAXS(tim=0.5, sample='Test', ti_sl = 197): 
    # Slowest cycle:
    name = 'TP'
    num = 30
    x_interface  = [piezo.x.position]
    
    x_surface = x_interface[0]-2000

    piezo_y_range = [-20, 20, 41]
    samples = [sample  +  '_interface']
    
    surface_sample = sample  + '_surface'
    angle = 0.08
    
    #Detectors, motors:
    dets = [pil1M, pil1mroi2] # WAXS detector ALONE
    x_offset = 10
    t0=time.time()
    
    yield from bps.mv(piezo.x, x_surface)
    #yield from alignement_gisaxs(angle)
    yield from bps.mvr(piezo.th, angle)
    
    det_exposure_time(tim, tim)
    sample_id(user_name=name, sample_name=surface_sample)
    yield from bp.rel_scan(dets, piezo.y, *piezo_y_range) 
    
    
    
    #yield from bps.mv(piezo.x, xinterface)
    
    name_fmt = '{sample}_{angle}deg_{ti}sec'
    #    param   = '16.1keV'
    assert len(x_interface) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, s in zip(x_interface, samples):
        yield from bps.mv(piezo.x, x)
        #yield from alignement_gisaxs_shorter(angle)
        #yield from bps.mvr(piezo.th, angle) 
        for i in range (num):
            #x_pos = [piezo.x.position]
            #yield from bps.mv(piezo.x, x_pos+x_offset)
            yield from bps.mv(piezo.x, x+x_offset*i)
            t1=time.time()
            t_min = np.round((t1-t0))
            sample_name = name_fmt.format(sample=s, angle=angle, ti = '%5.5d'%t_min)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.rel_scan(dets, piezo.y, *piezo_y_range)
            
            
            
            yield from bps.sleep(ti_sl)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(1,1)

    

    

