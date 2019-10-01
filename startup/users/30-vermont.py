

def run_simple(exp=0.05, t=10):
    name = 'jw'
    sample = 'sam18_room_temp'
    
    name_fmt = '{samp}_{temperature}C'
    temp = ls.ch1_read.value
    det_exposure_time(exp, t)
    sample_name = name_fmt.format(samp = sample, temperature=temp)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name) 
    yield from bp.count([pil1M, pil300KW], num = 1)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)















def run_harv_poly(tim=1,name = 'HarvPoly'): 
    # Slowest cycle:
    temperatures = [85]
    x_list  = [-1000 ]
    y_list =  [-4740]
    samples = ['S29']
    # Detectors, motors:
    dets = [pil300KW,ls.ch1_read, xbpm3.sumY]
    name_fmt = '{sample}_{temperature}C'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        #time.sleep(30)
        yield from bps.mv(ls.ch1_sp, 28)
        for x,y, s in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, 200)
            for i in range(600):
                temp = ls.ch1_read.value
                sample_name = name_fmt.format(sample=s, temperature=temp)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                sample_id(user_name=name, sample_name=sample_name) 
                yield from bp.count(dets, num=1)
                time.sleep(30)                
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)
    yield from bps.mv(ls.ch1_sp, 28)   
    

