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


def run_mesh_fastUCI(t=1): 
    waxs_range = [0, 6.5, 13, 19.5, 26]
    name = 'TW'
    dets = [pil300KW]
    det_exposure_time(t,t)
    
    
    samples = ['tooth4_bot', 'tooth4_cen-tip', 'Mag-gypsum', 'Mag-cell', 'Mag-nocell', 'tooth0pm', 'tooth1pm', 'tooth2pm', 'tooth3pm', 'tooth4pm', 'tooth5pm']
    x_list = [    17045,          17190,           3220,       -12740,      -32520,      27950,     28550,       29000,     29450,       29850,      30250]
    y_list = [    -4110,          -4160,            670,        -1800,       -1160,      -1650,     -1500,       -1650,     -1750,      -1500,       -1000]
    x_range=[ [0, 125, 6],  [0, 400, 17],    [0, 200, 9],  [0, 200, 9], [0, 200, 9], [0, 250, 6], [0, 300, 7],[0, 300, 7], [0, 350, 8], [0, 400, 9], [0, 350, 8]]
    y_range=[[0, 200, 101],[0, 200, 101],  [0, 200, 101],[0, 200, 101],[0, 200, 101],[0, 350, 36],[0, 400, 41],[0, 400, 41],[0, 400, 41],[0, 450, 46],[0, 500, 51]]
    

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        for wa in waxs_range:
            yield from bps.mv(waxs, wa)
            name_fmt = '{sam}_wa{waxs}'
            sample_name = name_fmt.format(sam=sample, waxs='%2.1f'%wa)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r, 0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)
