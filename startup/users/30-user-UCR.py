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





def mesh_UCI_2020_3(t=1): 
    waxs_range = [0, 6.5, 13, 19.5, 26]
    name = 'TW'
    dets = [pil300KW]
    det_exposure_time(t,t)
    
    
    samples = [    'T1',           'T2',           'T3']
    x_list = [    10270,           2715,          -3465]
    y_list = [    -1440,          -1860,          -1800]
    x_range=[ [0, 450, 19],  [0, 375, 17],  [0, 375, 16]]
    y_range=[[0, 400, 201], [0, 400, 201], [0, 500, 251]]
    

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





def mesh_UCI_2021_2(t=1): 
    waxs_range = np.linspace(0, 26, 5)
    
    name = 'TW'
    dets = [pil300KW, pil1M]
    det_exposure_time(t,t)
    

    #Finished at -17300 in X

    # samples = [    'S1_map1', 'S1_map2', 'S2_map1', 'S2_map2', 'S5', 'S7','chiton_art_frontal','chiton_art_lateral',
    # 'chi_ima13-22_t13','chi_ima13-22_t14','chi_ima13-22_t15','chi_ima13-22_t16','chi_ima13-22_t17','chi_ima13-22_t18','chi_ima13-22_t19','chi_ima13-22_t20-22',
    # 'chi_ima0-12_map1','chi_ima0-12_map2','chi_ima0-12_map3','chi_ima0-12_map4', 'wood', 'chitin_edgeon', 'chitin_large']
    # x_list = [     41600,        42800,      29200,     29950,     20900,     12900,      2200,      1250,     -8970,      -9020,     -8970,     -9070,     -9120,     -9470,     -9670,
    #     -9920,    -17520,       -17300,     -17200,    -17250,    -24150,    -33250,    -40250]
    # y_list = [       800,          600,        500,       350,       550,       500,      1150,       950,       100,        350,       900,      1250,      1500,      1750,      1950,
    #      2150,       100,          300,        600,      1500,      1500,      1500,      1500]
    # x_range=[[0, 1200,31], [0,350, 11], [0,700,21],[0,350,11],[0,300,11],[0,700,21],[0,390,14],[0,300,11], [0,200,5], [0,250,6], [0,250,6], [0,200,5], [0,200,5], [0,200,5], [0,200,5],
    # [0,250,11],[0,300,11],   [0,200,9],  [0,200,9],[0,300,11], [0,200,6],   [0,0,1],   [0,0,1]]
    # y_range=[ [0,550,111], [0,300, 61], [0,400,81],[0,250,51],[0,200,21],[0,250,26],[0,250,51],[0,300,61],[0,200,11],[0,200,11],[0,200,11],[0,200,11],[0,200,11],[0,200,11],[0,200,11],
    # [0,300,31],[0,200,21],  [0,300,31], [0,700,71],[0,600,61],[0,200,41],[0,100,10],[0,100,10]]
    

    samples = ['chi_ima0-12_map2','chi_ima0-12_map3','chi_ima0-12_map4', 'wood', 'chitin_edgeon', 'chitin_large']
    x_list = [       -17300,     -17200,    -17250,    -23850,    -33050,    -40250]
    y_list = [          300,        600,      1500,      1400,      1500,      1500]
    x_range=[     [0,200,9],  [0,200,9],[0,300,11], [0,200,6],   [0,0,1],   [0,0,1]]
    y_range=[    [0,300,31], [0,700,71],[0,600,61],[0,200,41],[0,100,10],[0,100,10]]


    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_list)})'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(x_range), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(x_range)})'
    assert len(x_list) == len(y_range), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_range)})'

    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        for wa in waxs_range:
            yield from bps.mv(waxs, wa)
            name_fmt = '{sam}_wa{waxs}_16.1keV_1.6m'
            sample_name = name_fmt.format(sam=sample, waxs='%2.1f'%wa)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r, 0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)