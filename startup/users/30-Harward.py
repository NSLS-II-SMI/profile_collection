####line scan

    
    
def waxs_zher(t=1): 
    x_list  = [-42000, -20400, 200, 20400, 44300]#
    y_list =  [  5600,   5800, 5920, 5822,  5972]
    # Detectors, motors:
    dets = [pil1M]
    y_range = [0, 200, 11]
    samples = [ 'S1_30C', 'S2_30C','S3_30C','S4_30C','S5_30C']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, y, sample in zip(x_list,y_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name='BM', sample_name=sample) 
        #yield from bp.scan(dets, piezo.y, *y_range)
        yield from bp.count(dets, num=1)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(1)

def run_harv_temp(tim=1,name = 'HarvTemp'): 
    # Slowest cycle:
    temperatures = [150]
    #x_list  = [-42000, -20400, 200, 20400, 44300]
    x_list  = [-10200, 9500, 25800]
    #y_list =  [  5600,   5800, 5920, 5822,  5972]
    y_list =  [-9060, -8920, -8900]
    #samples = [ 'S1', 'S2','S3','S4','S5']
    samples = ['S2', 'S3', 'S5_90deg']
    # Detectors, motors:
    dets = [pil1M, rayonix, pil300KW,ls.ch1_read, xbpm3.sumY]
    y_offset = np.arange(0, 201, 20)
    waxs_arc = [2.8, 20.8, 4]
    name_fmt = '{sample}_{offset}um_{temperature}C'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(tim)
    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        if i_t > 0:
            yield from bps.sleep(600)
        for x,y, s in zip(x_list, y_list, samples):
            temp = ls.ch1_read.value
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            for i_o, o in enumerate(y_offset):
                sample_name = name_fmt.format(sample=s, offset = o, temperature=temp)
                yield from bps.mv(piezo.y, y+y_offset[i_o])
                print(f'\n\t=== Sample: {sample_name} ===\n')
                sample_id(user_name=name, sample_name=sample_name) 
                yield from bp.scan(dets, waxs.arc, *waxs_arc)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
    yield from bps.mv(ls.ch1_sp, 28)    
