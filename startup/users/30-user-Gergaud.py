#pil300KW for waxs, pil1M for saxs


def cd_saxs(th_ini, th_fin, th_st, exp_t=1):
    sample = ['cdsaxs_ech03_defectivity_pitch128', 'cdsaxs_ech03_defectivity_pitch127', 'cdsaxs_ech03_defectivity_pitch124', 'cdsaxs_ech03_defectivity_pitch121', 'cdsaxs_ech03_defectivity_pitch118', 'cdsaxs_ech03_defectivity_pitch115', 'cdsaxs_ech03_defectivity_pitch112', 'cdsaxs_ech04_defectivity_pitch128', 'cdsaxs_ech04_defectivity_pitch127', 'cdsaxs_ech04_defectivity_pitch124', 'cdsaxs_ech04_defectivity_pitch121', 'cdsaxs_ech04_defectivity_pitch118', 'cdsaxs_ech04_defectivity_pitch115', 'cdsaxs_ech04_defectivity_pitch112', 'cdsaxs_ech11b_defectivity_pitch128', 'cdsaxs_ech11b_defectivity_pitch127', 'cdsaxs_ech11b_defectivity_pitch124', 'cdsaxs_ech11b_defectivity_pitch121', 'cdsaxs_ech11b_defectivity_pitch118', 'cdsaxs_ech11b_defectivity_pitch115', 'cdsaxs_ech11b_defectivity_pitch112']
    x = [-41100, -38550 ,-34050 ,-29550 ,-25050 ,-20550 ,-16050 ,-11150 ,-9650 ,-5150 ,-650 ,3850 ,8350, 12850, 17000, 18500, 23000, 27500, 32000, 36500, 41000]
    y = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 3900, 3900, 3900, 3900, 3900, 3900, 3900]
    det = [pil1M]
    
    det_exposure_time(exp_t, exp_t)
    for xs, ys, sample in zip(x, y, sample):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for theta in np.linspace(th_ini, th_fin, th_st):
            yield from bps.mv(prs, theta)
            name_fmt = '{sample}_{th}deg'

            sample_name = name_fmt.format(sample=sample, th='%2.2d'%theta)
            sample_id(user_name='PG', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            
            yield from bp.count(det, num=10)



def cd_saxs_new(sample, x, y, num=1, exp_t=1, step = 121):
    det = [pil1M]
    
    det_exposure_time(exp_t, exp_t)
    yield from bps.mv(piezo.x, x)
    yield from bps.mv(piezo.y, y)

    for i, theta in enumerate(np.linspace(-60, 60, step)):
        yield from bps.mv(prs, theta-1)
        name_fmt = '{sample}_{num}_{th}deg'

        sample_name = name_fmt.format(sample=sample, num = '%2.2d'%i, th='%2.2d'%theta)
        sample_id(user_name='PG', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        
        yield from bp.count(det, num=num)


def cdsaxs_all_pitch(sample, x, y, num=1, exp_t=1, step=121):
    pitches = ['p112nm', 'p113nm', 'p114nm', 'p115nm', 'p116nm', 'p117nm', 'p118nm', 'p119nm', 'p120nm','p121nm','p122nm',
    'p123nm', 'p124nm', 'p125nm', 'p126nm', 'p127nm', 'p128nm']
 
    x_off = [0, 1500, 3000, 4500, 6000, 7500, 9000, 10500, 12000, 13500, 15000, 16500, 18000, 19500, 21000, 22500, 24000]
    det_exposure_time(exp_t, exp_t)
    for x_of, pitch in zip(x_off, pitches):
        yield from bps.mv(piezo.x, x+x_of)

        name_fmt = '{sample}_{pit}'
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        yield from cd_saxs_new(sample_name, x+x_of, y, num=1, exp_t=exp_t, step=step)  


def night_patrice(exp_t=1):
    numero = 6
    det = [pil1M]
    
    #names = ['champs00', 'bkg_champs00','champs05','bkg_champs05','champs0-4','bkg_champs0-4','champs0-3', 'bkg_champs0-3']
    #xs = [-41100, -41100, 14100, 14100, -36450, -36550, -10250, -10250]
    #ys = [-7500, -8500, -7000, -8000, 5450, 6450, 5500, 6400]
    names = ['champs0-3', 'bkg_champs0-3']

    xs = [ 2220, 2220]
    ys = [ 6470, 7470]

    for name, x, y in zip(names, xs, ys):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        numero+=1
        name_fmt = '{sample}_num{numb}'
        sample_name = name_fmt.format(sample=name, numb=numero)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        
        yield from cdsaxs_important_pitch(sample_name, x, y, num=1)
        #numero+=1
        #yield from cdsaxs_important_pitch(sample_name, x, y, num=1)


    names = ['champs00']
    xs = [-14380]
    ys = [-6200]

    numero+=1
    name_fmt = '{sample}_num{numb}'
    sample_name = name_fmt.format(sample=names[0], numb=numero)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    yield from cdsaxs_important_pitch(sample_name, xs[0], ys[0], num=1)

    numero+=1
    name_fmt = '{sample}_num{numb}'
    sample_name = name_fmt.format(sample=names[0], numb=numero)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    yield from cdsaxs_important_pitch(sample_name, xs[0], ys[0], num=1)


    names = ['champs00', 'bkg_champs00']
    xs = [-14380, -14380]
    ys = [-6200, -7200]

    for name, x, y in zip(names, xs, ys):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        numero+=1

        name_fmt = '{sample}_num{numb}'
        sample_name = name_fmt.format(sample=name, numb=numero)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        
        yield from cdsaxs_all_pitch(sample_name, x, y, num=1, step=61)
    

    numero+=1
    name_fmt = '{sample}_offset300_num{numb}'
    sample_name = name_fmt.format(sample=name, numb=numero)
    yield from cd_saxs_new(sample_name, xs[0], ys[0]+300, num=1, exp_t=exp_t)
    
    numero+=1
    name_fmt = '{sample}_offset-300_num{numb}'
    sample_name = name_fmt.format(sample=name, numb=numero)
    yield from cd_saxs_new(sample_name, xs[0], ys[0]-300, num=1, exp_t=exp_t)

    
    numero+=1
    name_fmt = '{sample}_num{numb}'
    sample_name = name_fmt.format(sample=name, numb=numero)
    yield from mesure_rugo(sample_name, xs[0], ys[0], num=200, exp_t=exp_t)
    
    numero+=1
    name_fmt = '{sample}_num{numb}'
    sample_name = name_fmt.format(sample=name, numb=numero)
    yield from mesure_rugo(sample_name, xs[1], ys[1], num=200, exp_t=exp_t)

            
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
    





def sample_patrice_2020_3(exp_t=1):
    numero = 1
    det = [pil1M]
    # wafer = 'wafer16'
    # names = ['champs5', 'champs5_bkg', 'champs4', 'champs4_bkg', 'champs3', 'champs3_bkg']
    # names = ['champs-1', 'champs-1_bkg', 'champs-2', 'champs-2_bkg', 'champs-3', 'champs-3_bkg']

    wafer = 'wafer25'
    # names = ['champs-1', 'champs-1_bkg', 'champs-2', 'champs-2_bkg', 'champs-3', 'champs-3_bkg']
    names = ['champs1', 'champs1_bkg', 'champs0', 'champs0_bkg']

    xs = [-3400, -3400, 22650, 22650]
    ys = [ 6360,  7300,  6410,  7300]
    zs = [ 1800,  1800,  1470,  1470]


    for name, x, y, z in zip(names, xs, ys, zs):
        yield from bps.mv(piezo.z, z)
        numero+=1
        name_fmt = '{sample}_num{numb}'
        sample_name = name_fmt.format(wafer = wafer, sample=name, numb=numero)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        
        if 'bkg' in name:
            yield from cdsaxs_important_pitch(sample_name, x, y, num=1)
        else:
            yield from cdsaxs_important_pitch(sample_name, x, y, num=2)



    names = ['champs2', 'champs2_bkg', 'champs1', 'champs1_bkg', 'champs0', 'champs0_bkg']

    xs = [ -29420, -29420, -3400, -3400, 22650, 22650]
    ys = [   6460,   7300,  6360,  7300,  6410,  7300]
    zs = [   2130,   2130,  1800,  1800,  1470,  1470]

    for name, x, y, z in zip(names, xs, ys, zs):
        yield from bps.mv(piezo.z, z)
        numero+=1
        name_fmt = '{sample}_num{numb}'
        sample_name = name_fmt.format(sample=name, numb=numero)

        if 'bkg' in name:
            yield from mesure_rugo(sample_name, x, y, num=10, exp_t=exp_t)
        else:
            yield from mesure_rugo(sample_name, x, y, num=100, exp_t=exp_t)


    yield from bps.mvr(pil1m_pos.x,-5)
    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique='gisaxs')

    for name, x, y, z in zip(names, xs, ys, zs):
        numero+=1
        name_fmt = '{sample}_num{numb}'
        sample_name = name_fmt.format(sample=name, numb=numero)
        yield from bps.mv(piezo.z, z)
        yield from mesure_db(sample_name, x, y, num=1, exp_t=1)
    
    yield from smi.modeMeasurement()
    yield from bps.mvr(pil1m_pos.x, 5)



def cdsaxs_important_pitch(sample, x, y, num=1, exp_t=1):
    pitches = ['p113nm', 'p100nm']


    if 'bkg' in sample:
        x_off = [0, 0]
        y_off = [0, -13300]
    else:
        x_off = [0, 0]
        y_off = [0, -10500]


    det_exposure_time(exp_t, exp_t)
    for x_of, y_of, pitch in zip(x_off, y_off, pitches):
        yield from bps.mv(piezo.x, x+x_of)
        yield from bps.mv(piezo.y, y+y_of)

        name_fmt = '{sample}_{pit}'
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        yield from cd_saxs_new(sample_name, x+x_of, y+y_of, num=num, exp_t=exp_t)            


def mesure_rugo(sample, x, y, num=200, exp_t=1):
    print(sample)
    pitches = ['p100nm']
    
    if 'bkg' in sample:
        x_off = [0]
        y_off = [-13300]
    else:
        x_off = [0]
        y_off = [-10500]


    yield from bps.mv(prs, -1)

    det_exposure_time(exp_t, exp_t)
    for x_of, y_of, pitch in zip(x_off, y_off, pitches):
        yield from bps.mv(piezo.x, x+x_of)
        yield from bps.mv(piezo.y, y+y_of)

        name_fmt = '{sample}_rugo_{pit}_up'
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        print(sample_name)
        sample_id(user_name='PG', sample_name=sample_name)

        yield from bp.count([pil1M], num=num)            


    yield from bps.mvr(pil1m_pos.y, 4.3)
    for x_of, y_of, pitch in zip(x_off, y_off, pitches):
        yield from bps.mv(piezo.x, x+x_of)
        yield from bps.mv(piezo.y, y+y_of)
        name_fmt = '{sample}_rugo_{pit}_down'
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        sample_id(user_name='PG', sample_name=sample_name)
        yield from bp.count([pil1M], num=num)            
   
    yield from bps.mvr(pil1m_pos.y, -4.3)


def mesure_db(sample, x, y, num=1, exp_t=1):
    pitches = ['p100nm']
    if 'bkg' in sample:
        x_off = [0]
        y_off = [-13300]
    else:
        x_off = [0]
        y_off = [-10500]
    yield from bps.mv(prs, -1)

    det_exposure_time(exp_t, exp_t)
    for x_of, y_of, pitch in zip(x_off, y_off, pitches):
        yield from bps.mv(piezo.x, x+x_of)
        yield from bps.mv(piezo.y, y+y_of)

        name_fmt = '{sample}_db_{pit}_att9x60umSn'
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        sample_id(user_name='PG', sample_name=sample_name)

        yield from bp.count([pil1M], num=1)            



def NEXAFS_P_edge(t=0.5):
        yield from bps.mv(waxs, 30)
        dets = [pil300KW]
        name = 'NEXAFS_S4_Pedge_wa30.0deg_ai0.6deg'

        energies = np.linspace(2140, 2180, 41)
        
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        for e in energies:                              
            yield from bps.mv(energy, e)
            yield from bps.sleep(2)

            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.2f'%xbpm3.sumY.value)
            sample_id(user_name='SR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)


