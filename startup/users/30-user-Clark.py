def run_waxs_UCol(t=1):
    xlocs = [5500]
    names = ['salmonDNA2_air']
    user = 'GS'    
    det_exposure_time(t,t)    
    y0 = -1350
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    y_range = np.linspace(-40, 200, 49) #if you start from the bottom, reverse signs: 40, -200, 49
    # Detectors, motors:
    dets = [pil300KW]
    waxs_range = [0, 13, 3]
    for sam,x in zip(names, xlocs):
        yield from bps.mv(piezo.x, x)
        for y in y_range:
            yield from bps.mv(piezo.y, y0+y)
            name_fmt = '{sam}_y{y_pos}um'
            sample_name = name_fmt.format(sam=sam, y_pos='%2.1f'%y)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_range)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 

def run_waxs_emptyUCol(t=1):
    xlocs = [-34500,-25000,-17050,-3825,3750,14050]
    ylocs = [0,0,0,0,0,0]
    names = ['sDDnem_vac1_bkg','sDDcol_vac_bkg','DDshort_vac1_bkg','DDlong_vac_bkg','GTACshort_vac_bkg','GTAClong_vac_bkg']
    user = 'GS'    
    det_exposure_time(t,t)    
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil300KW]
    waxs_range = [0, 13, 3]
    for sam,x in zip(names, xlocs):
        yield from bps.mv(piezo.x, x)
        name_fmt = '{sam}'
        sample_name = name_fmt.format(sam=sam)
        sample_id(user_name=user, sample_name=sample_name) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.scan(dets, waxs, *waxs_range)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 


def saxs_waxs_temps_Ucol( t = 0.5): 
    # Slowest cycle:
    name = 'VM'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW, rayonix, ls.ch1_read]
    y_range = [5.6, 5.6, 1]
    sample = 'W1013ITO'
    waxs_range = [0, 13, 3]
        
    name_fmt = '{sam}_{temperature}C_{tim}s'
    
    det_exposure_time(t,t)
    temp = ls.ch1_read.value
    t1=time.time()
    time_elapsed = int(t1-t0)
    sample_name = name_fmt.format(temperature=temp, sam = sample, tim = time_elapsed)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=sample, sample_name=sample_name) 
    #yield from bp.count(dets)
    yield from bp.scan(dets, waxs, *waxs_range)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3)



def run_contRPI(t=1, numb = 100, sleep = 5):
    det_exposure_time(t,t)
    dets = [pil1M,pil300KW]
    #dets = [pil300Kw]
    for i in range(numb):
        yield from bp.count(dets, num=1)
        time.sleep(sleep)

