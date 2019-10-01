#Align GiSAXS sample
import numpy as np


    
def run_mesh_fastUCR(t=0.5): 
    samples = ['stel_styl_m_s5_D2-cut5_']
    x_list = [-15740]
    y_list = [-5654]
        
    name = 'TW'
    
    x_range=[ [-280, 280, 17]]
    y_range=[ [-225, 225, 101]]
    
    
    # Detectors, motors:
    dets = [pil300KW]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    waxs_range = np.linspace(0, 26, 5)
    
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            name_fmt = '{sam}_wa{waxs}deg'
            sample_name = name_fmt.format(sam=sample, waxs='%2.1f'%wa)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
             
            yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r, 1) #1 = snake, 0 = not-snake
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


