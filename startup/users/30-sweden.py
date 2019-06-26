####line scan



def run_gi_sweden(tim=1): 
    # Slowest cycle:
    name = 'TP'
    num = 18
    x_interface  = [730]
    
    x_surface = x_interface[0]-1500
    piezo_y_range = [-20, 20, 41]
    #y_list =  [  5600,   5800, 5920, 5822,  5972]
    samples = [ '1p5wt_cylinder_CNF_drying_interface']
    
    surface_sample = '1p5wt_cylinder_CNF_drying_surface'
    angle = 0.1
    #Detectors, motors:
    #dets = [pil1M, rayonix, pil300KW,ls.ch1_read, xbpm3.sumY] #ALL detectors
    dets = [pil1M, pil1mroi2] # WAXS detector ALONE
    x_offset = 10
    t0=time.time()
    yield from bps.mv(piezo.x, x_surface)
    yield from alignement_gisaxs_shorter(angle)
    yield from bps.mvr(piezo.th, angle)
    det_exposure_time(tim, tim)
    sample_id(user_name=name, sample_name=surface_sample)
    yield from bp.rel_scan(dets, piezo.y, *piezo_y_range) 
    
    name_fmt = '{sample}_{angle}deg_{ti}min'
    #    param   = '16.1keV'
    assert len(x_interface) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(tim, tim)
    for x, s in zip(x_interface, samples):
        yield from bps.mv(piezo.x, x)
        #yield from alignement_gisaxs_shorter(angle)
        #yield from bps.mvr(piezo.th, angle)
        det_exposure_time(tim, tim)      
        for i in range (num):
            yield from bps.mv(piezo.x, x+x_offset*i)
            t1=time.time()
            t_min = np.round((t1-t0)/60)
            sample_name = name_fmt.format(sample=s, angle=angle, ti = t_min)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.rel_scan(dets, piezo.y, *piezo_y_range)
            time.sleep(530)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(1,1)

    

    

