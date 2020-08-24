####line scan



def run_gi_sweden_GISAXS_pulling(tim=0.5, sample='Test', ti_sl =4): 
    # Slowest cycle:
    name = 'PULLING'
    num = 30
    n=1
    x_interface  = [piezo.x.position]
    


    #piezo_y_range = [0, 0, 1]
    samples = [sample]

    
    #Detectors, motors:
    dets = [pil1M, pil1mroi2] # WAXS detector ALONE
    t0=time.time()
        
    det_exposure_time(tim, tim)

    
    
    
    
    name_fmt = '{sample}_{ti}sec'
    
    #    param   = '16.1keV'
    assert len(x_interface) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, s in zip(x_interface, samples):
        for i in range (num):
            t1=time.time()
            t_min = np.round((t1-t0))
            sample_name = name_fmt.format(sample=s, angle=angle, ti = '%3.3d'%t_min)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, n) 
            
            
            
            yield from bps.sleep(ti_sl)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(1,1)

    

    

