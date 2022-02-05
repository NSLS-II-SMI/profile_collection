
def run_simple(exp=0.05, t=10):
    name = 'JW'
    sample = 'recheck_90c_0.1mms'
    pil1M.cam.file_path.put(f"/ramdisk/images/users/2019_3/304549_Headrick/1M/%s"%sample)
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/2019_3/304549_Headrick3/300KW/%s"%sample)
    name_fmt = '{samp}_{temperature}C'
    temp = ls.ch1_read.value
    det_exposure_time(exp, t)
    sample_name = name_fmt.format(samp = sample, temperature=temp)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name)
    yield from bps.mv(waxs, 12) 
    yield from bp.count([pil1M, pil300KW], num = 1)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def run_fullgiwaxs(t=0.5):
    name = 'JW'
    sample = 'recheck_90c_0.1mms'
    pil1M.cam.file_path.put(f"/ramdisk/images/users/2019_3/304549_Headrick/1M/%s"%sample)
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/2019_3/304549_Headrick3/300KW/%s"%sample)
    waxs_range = [0, 19.5, 4] #up to 3.2 A-1
    #waxs_range = [0, 13, 3] #up to 2.3 A-1
    name_fmt = '{samp}_{temperature}C'
    temp = ls.ch1_read.value
    det_exposure_time(t, t)
    sample_name = name_fmt.format(samp = sample, temperature=temp)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name) 
    yield from bp.scan([pil1M, pil300KW], waxs, *waxs_range)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def run_BD(t=0.2):
    num = 300
    name = 'JW'
    sample = '60c_0.2mms'
    pil1M.cam.file_path.put(f"/ramdisk/images/users/2019_3/304549_Headrick/1M/%s"%sample)
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/2019_3/304549_Headrick/300KW/%s"%sample)
    name_fmt = '{samp}_{temperature}C'
    temp = ls.ch1_read.value
    det_exposure_time(t, t)
    yield from bps.mv(waxs, 12) 
    sample_name = name_fmt.format(samp = sample, temperature=temp)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name) 
    yield from bp.count([pil300KW, pil300kwroi2, pil300kwroi3, pil300kwroi4], num=num)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)





def giwaxs_insitu_heating(tim=0.5): 
    # samples = ['PHBTBTC10_vapor_sam3_run2_cooldown_25C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_25C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_40C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_50C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_60C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_70C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_80C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_90C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_100C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_110C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_120C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_130C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_140C']
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_150C']

    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_140C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_130C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_120C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_110C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_100C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_90C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_80C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_70C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_60C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_50C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_40C']
    # samples = ['PHBTBTC10_slow_cool_sam3_cool_down_25C']

    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_25C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_40C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_50C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_60C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_70C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_80C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_90C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_100C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_110C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_120C_1min']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_120C_6min']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_120C_11min']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_120C_16min']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_120C_21min']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_120C_26min']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_120C_31min']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_120C_36min']
    
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_110C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_100C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_90C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_80C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_70C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_60C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_50C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_40C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_cool_down_25C']

    # samples = ['PHBTBTC10_quenched_sam1_heat_up_25C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_40C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_50C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_60C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_70C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_80C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_90C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_100C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_110C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_120C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_130C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_140C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_150C']

    # samples = ['PHBTBTC10_quenched_sam1_cool_down_140C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_130C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_120C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_110C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_100C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_90C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_80C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_70C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_60C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_50C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_40C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_25C']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_25C_check']
    # samples = ['PHBTBTC10_quenched_sam1_cool_down_25C_check_2']

    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_25C']
    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_40C']
    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_60C']
    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_80C']
    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_100C']
    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_120C_1min']
    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_120C_6min']
    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_120C_11min']
    # samples = ['PHBTBTC10_quenched_sam1_run2_heat_up_120C_16min']

    # samples = ['PHBTBTC10_quenched_sam1_run2_cool_down_100C']
    # samples = ['PHBTBTC10_quenched_sam1_run2_cool_down_80C']
    # samples = ['PHBTBTC10_quenched_sam1_run2_cool_down_60C']
    # samples = ['PHBTBTC10_quenched_sam1_run2_cool_down_40C']
    samples = ['PHBTBTC10_quenched_sam1_run2_cool_down_25C']
    
    
    x_list  = [0]
    incident_angle = 0.1

    name = 'RH'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    dets = [pil900KW]
    
    waxs_arc = [0, 20] 
    name_fmt = '{sample}_16.1keV_ai{ai}_wa{waxs}'

    det_exposure_time(tim, tim)

    for s in samples:
        # yield from bps.mvr(piezo.x, 60)
        
        yield from alignement_gisaxs(0.1)
        ai0 = piezo.th.position
        yield from bps.mv(piezo.th, ai0 + incident_angle)
        
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
        
            sample_name = name_fmt.format(sample=s, ai = '%1.1f'%incident_angle, waxs='%2.1f'%wa)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            sample_id(user_name=name, sample_name=sample_name) 
            yield from bp.count(dets, num=1)
    
        yield from bps.mv(piezo.th, ai0)

    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)



def giwaxs_insitu_heating_norealignement(tim=0.5): 
    # samples = ['PHBTBTC10_slow_cool_sam3_heat_up_25C']
    # samples = ['PHBTBTC10_slow_cool_sam3_run2_heat_up_25C']
    # samples = ['PHBTBTC10_quenched_sam1_heat_up_25C']
    samples = ['Chad_sample']


    x_list  = [0]
    incident_angle = 0.1
    # incident_angle = 0.2

    name = 'RH'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    dets = [pil900KW]
    
    waxs_arc = [0, 20] 
    name_fmt = '{sample}_16.1keV_ai{ai}_wa{waxs}'

    det_exposure_time(tim, tim)

    for x, s in zip(x_list, samples):
        # yield from bps.mv(piezo.x, 60)
        
        ai0 = piezo.th.position
        yield from bps.mv(piezo.th, ai0 + incident_angle)
        
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
        
            sample_name = name_fmt.format(sample=s, ai = '%1.1f'%incident_angle, waxs='%2.1f'%wa)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            sample_id(user_name=name, sample_name=sample_name) 
            yield from bp.count(dets, num=1)
    
        yield from bps.mv(piezo.th, ai0)

    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)


def alignement_h(): 
    yield from alignement_gisaxs_hex(0.1)
    yield from bps.mv(waxs, 10)
    yield from bps.mvr(stage.th, 0.1)



def giwaxs_insitu_roll(t=0.1, tim=180):
    #pil900KW.unstage()
    samples = 'PHBTBTC10_solution_sam3'

    name = 'RH'
    dets = [pil900KW]
    name_fmt = '{sample}_16.1keV_ai{ai}_wa{waxs}'

    det_exposure_time(t, tim)

   # for s in samples:
    #    yield from bps.mvr(piezo.x, 60)

    sample_name = name_fmt.format(sample=samples, ai = '%1.1f'%0.1, waxs='%2.1f'%10.0)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name) 
    yield from bp.count(dets)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)


def giwaxs_insitu_single(t=0.5, tim=0.5):
    #pil900KW.unstage()
    samples = 'PHBTBTC10_solution_cooldown_25C_sam3'

    name = 'RH'
    dets = [pil900KW]
    name_fmt = '{sample}_16.1keV_ai{ai}_wa{waxs}'

    det_exposure_time(t, tim)

    for s in samples:
       yield from bps.mvr(piezo.x, -60)

    sample_name = name_fmt.format(sample=samples, ai = '%1.1f'%0.1, waxs='%2.1f'%10.0)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name) 
    yield from bp.count(dets)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)


def giwaxs_headrick_2022_1(t=0.5): 
    
    

    names = [   'Chad_S1_1', 'Chad_S1_2', 'Chad_S2_1', 'Chad_S2_2', 'Chad_S3_1', 'Chad_S3_2',]
    x_piezo = [    57000,  45000, 10000, -4000, -39000, -51000]
    y_piezo = [     5500,   5500, 5500, 5500, 5500, 5500]
    z_piezo = [     1100,   1100, 1100, 1100, 1100, 1100]
    x_hexa =  [      0,    0, 0, 0, 0, 0]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(x_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})'

    waxs_arc = [0, 20]
    angle = [0.1]
    # angle = [5]

    dets = [pil900KW, pil1M]
    det_exposure_time(t,t)

    for name, xs, zs, ys, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, 0.6)
        
        yield from alignement_gisaxs(angle = 0.1)

        ai0 = piezo.th.position
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)  

            for i, an in enumerate(angle):
                yield from bps.mv(piezo.x, xs)
                yield from bps.mv(piezo.th, ai0 + an)                
                name_fmt = '{sample}_16.1keV_ai{angl}deg_wa{waxs}_5m'
                sample_name = name_fmt.format(sample=name, angl='%3.2f'%an, waxs='%2.1f'%wa)
                sample_id(user_name='RH', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)
            
            yield from bps.mv(piezo.th, ai0)
