#pil300KW for waxs, pil1M for saxs


def cd_saxs(th_ini, th_fin, th_st, exp_t=1):
    sample = ['cdsaxs_ech03_defectivity_pitch128', 'cdsaxs_ech03_defectivity_pitch127', 'cdsaxs_ech03_defectivity_pitch124', 'cdsaxs_ech03_defectivity_pitch121', 'cdsaxs_ech03_defectivity_pitch118', 'cdsaxs_ech03_defectivity_pitch115', 'cdsaxs_ech03_defectivity_pitch112', 'cdsaxs_ech04_defectivity_pitch128', 'cdsaxs_ech04_defectivity_pitch127', 'cdsaxs_ech04_defectivity_pitch124', 'cdsaxs_ech04_defectivity_pitch121', 'cdsaxs_ech04_defectivity_pitch118', 'cdsaxs_ech04_defectivity_pitch115', 'cdsaxs_ech04_defectivity_pitch112', 'cdsaxs_ech11b_defectivity_pitch128', 'cdsaxs_ech11b_defectivity_pitch127', 'cdsaxs_ech11b_defectivity_pitch124', 'cdsaxs_ech11b_defectivity_pitch121', 'cdsaxs_ech11b_defectivity_pitch118', 'cdsaxs_ech11b_defectivity_pitch115', 'cdsaxs_ech11b_defectivity_pitch112']
    x = [-40050, -38550 ,-34050 ,-29550 ,-25050 ,-20550 ,-16050 ,-11150 ,-9650 ,-5150 ,-650 ,3850 ,8350, 12850, 17000, 18500, 23000, 27500, 32000, 36500, 41000]
    y = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 3900, 3900, 3900, 3900, 3900, 3900, 3900]
    det = [pil1M]
    
    det_exposure_time(exp_t, exp_t)
    for xs, ys, sample in zip(x, y, sample):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for theta in np.linspace(th_ini, th_fin, th_st):
            yield from bps.mv(prs, theta + 1.6 )
            name_fmt = '{sample}_{th}deg'

            sample_name = name_fmt.format(sample=sample, th='%2.2d'%theta)
            sample_id(user_name='PG', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            
            yield from bp.count(det, num=1)
            
            
def scan_boite_pitch(exp_t=1):
    sample = ['Echantillon03_defectivity', 'Echantillon04_defectivity', 'Echantillon11b_defectivity']
    x = [-40050, -11150, 17000]
    y = [2000, 2000, 3900]
    det = [pil1M]
    
    pitches = np.linspace(128, 112, 17)
    
    det_exposure_time(exp_t, exp_t)
    for xs, ys, sample in zip(x, y, sample):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yield from bps.mvr(piezo.x, -1500)
        for i, pitch in enumerate(pitches):
            yield from bps.mvr(piezo.x, 1500)
            name_fmt = '{sample}_{pit}nm'

            sample_name = name_fmt.format(sample=sample, pit='%3.3d'%pitch)
            sample_id(user_name='PG', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
       
            yield from bp.count(det, num=10)
            
            
def macro_dinner():
    yield from scan_boite_pitch(1)
    yield from cd_saxs(-60, 60, 121, 2)
    
    

def NEXAFS_Ti_edge(t=0.5):
        
        dets = [pil300KW]
        name = 'NEXAFS_echantillon2_Tiedge_ai1p4'
        #x = [8800]

        energies = np.linspace(4950, 5050, 101)

        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
            sample_id(user_name='PG', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 5030)
        yield from bps.mv(energy, 5010)        
        yield from bps.mv(energy, 4990)
        yield from bps.mv(energy, 4970)
        yield from bps.mv(energy, 4950)


def NEXAFS_SAXS_Ti_edge(t=0.5):
        
        dets = [pil300KW, pil1M]
        name = 'NEXAFS_SAXS_echantillon13realign_ai1p75_Tiedge'
        #x = [8800]

        energies = np.linspace(4950, 5050, 101)

        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
            sample_id(user_name='PG', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 5030)
        yield from bps.mv(energy, 5010)        
        yield from bps.mv(energy, 4990)
        yield from bps.mv(energy, 4970)
        yield from bps.mv(energy, 4950)


def GISAXS_scan_boite(t=1):
    
    sample = 'Echantillon13realign_gisaxs_scanpolyperiod_e4950eV_ai1p75'
    x = np.linspace(55900, 31900, 81) 

    det = [pil1M]    
    
    det_exposure_time(t, t)
    for k, xs in enumerate(x):
        yield from bps.mv(piezo.x, xs)

        name_fmt = '{sample}_pos{pos}'
        sample_name = name_fmt.format(sample=sample, pos='%2.2d'%k)
        sample_id(user_name='PG', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
       
        yield from bp.count(det, num=1)


def fly_scan_ai(det, motor, cycle=1, cycle_t=10, phi = -0.6):
    start = phi - 30
    stop = phi + 30
    acq_time = cycle * cycle_t
    yield from bps.mv(motor, start)
    #yield from bps.mv(attn_shutter, 'Retract')
    det.stage()
    det.cam.acquire_time.put(acq_time)
    print(f'Acquire time before staging: {det.cam.acquire_time.get()}')
    st = det.trigger()
    for i in range(cycle):
        yield from list_scan([], motor, [start, stop])
    while not st.done:
        pass
    det.unstage()
    print(f'We are done after {acq_time}s of waiting')
    #yield from bps.mv(attn_shutter, 'Insert')
    




