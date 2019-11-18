def NEXAFS_Fe_edge(t=0.5):
        dets = [pil300KW]
        name = 'PBS1_NEXAFS_sdd_8p3_ns5'
        #x = [8800]

        energies = np.linspace(7100, 7150, 51)

        #for name, x in zip(names, x):
        #bps.mv(piezo.x, x)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
            sample_id(user_name='SR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 7100)
        name_fmt = '{sample}_2430eV_postmeas'
        sample_name = name_fmt.format(sample=name)
        sample_id(user_name='GF', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)

def GISAXS_Ca_edge(t=0.5):
        dets = [pil300KW]
        names = ['O5_3_gisaxs','O5_4_gisaxs','O11_1_gisaxs','O11_2_gisaxs','O11_3_gisaxs']
        xs = [-6100, -15100, -25100, -35100, -47100]

        
        energies = [4030, 4050, 4055, 4075]
        det_exposure_time(t,t) 
       
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_ai{ai}_wa{wa}'
        angles = [0.38, 0.4]
        wax = [0, 6.5]
        
        for x, name in zip(xs, names):
                yield from bps.mv(piezo.x, x)
                yield from alignement_gisaxs(0.2)
                th_0 = piezo.th.position
                for wa in wax:
                    yield from bps.mv(waxs, wa)            
                    for k, e in enumerate(energies): 
                        yield from bps.mv(energy, e) 
                        for alpha_i in angles:
                            yield from bps.mv(piezo.th, th_0 + alpha_i)    
                            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, ai='%3.2f'%alpha_i, wa='%2.1f'%wa)
                            sample_id(user_name='JDM', sample_name=sample_name)
                            print(f'\n\t=== Sample: {sample_name} ===\n')
                            yield from bp.count(dets, num=1)                                
                    
                    yield from bps.mv(energy, 4050)
                    yield from bps.mv(energy, 4030)


def SAXS_Ca_edge_hyd(t=0.5):
        dets = [pil1M]
        name = 'UntreatedC_Ca_edge_nspot4'


        energies = [4030, 4050, 4055, 4075]
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_sp{sp}'
        x_pos = piezo.x.position
        y_pos = piezo.y.position
        
        for k, e in enumerate(energies):                              
            yield from bps.mv(energy, e)
            yield from bps.mv(piezo.x, x_pos + k*500)
            
            for i in range(0, 10, 1):
                yield from bps.mv(piezo.y, y_pos + i*50)
   
                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, sp='%2.2d'%i)
                sample_id(user_name='JDM', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                
            yield from bps.mv(piezo.y, y_pos)
            
        yield from bps.mv(energy, 4050)
        yield from bps.mv(energy, 4030)



def SAXS_Ca_edge_dry1(t=1):
        dets = [pil300KW]
        name = '11_7_Ca2_edge_ns'

        energies = [4030, 4040, 4050, 4055, 4075]
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'
        wa = [0.0, 6.5]

        for wax in wa:
            yield from bps.mv(waxs, wax)
            for k, e in enumerate(energies):                              
                yield from bps.mv(energy, e)
                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wax)
                sample_id(user_name='SR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                          
            yield from bps.mv(energy, 4050)
            yield from bps.mv(energy, 4030)
        


def NEXAFS_Ca_edge(t=0.5):
        yield from bps.mv(waxs, 60)
        dets = [pil300KW]
        name = 'NEXAFS_CaTreatedA_full_Caedge'
        #x = [8800]

        energies = np.linspace(4030, 4150, 121)

        #for name, x in zip(names, x):
        #bps.mv(piezo.x, x)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
            sample_id(user_name='JDM', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 4125)
        yield from bps.mv(energy, 4100)        
        yield from bps.mv(energy, 4075)
        yield from bps.mv(energy, 4050)
        yield from bps.mv(energy, 4030)
        name_fmt = '{sample}_4030.0eV_postmeas'
        sample_name = name_fmt.format(sample=name)
        sample_id(user_name='SR', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)


def NEXAFS_P_edge(t=0.5):
        yield from bps.mv(waxs, 30)
        dets = [pil300KW]
        name = 'NEXAFS_PBS1_Pedge_nspot1'

        energies = np.linspace(2140, 2180, 41)
        energies_back = np.linspace(2180, 2140, 41)
        
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
            sample_id(user_name='SR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        
        for e in energies_back:                              
            yield from bps.mv(energy, e)
            time.sleep(2)


def NEXAFS_S_edge(t=0.5):
        yield from bps.mv(waxs, 30)
        dets = [pil300KW]
        name = 'NEXAFS_A12_Sedge'

        energies = np.linspace(2430, 2500, 71)
        energies_back = np.linspace(2500, 2430, 36)
        
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
            sample_id(user_name='SR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        
        for e in energies_back:                              
            yield from bps.mv(energy, e)
  
def waxs_S_edge(t=1):
    dets = [pil300KW]
    

    names = ['A41']
    x = [-28200]
    y = [1600]
    
    names1 = ['P3HT']
    x1 = [-38700]
    y1 = [900]
    
    energies = np.linspace(2456, 2500, 23)
    Ys = np.linspace(900, 2200, 23)
    waxs_arc = [0, 19.5, 4]
    
    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='SR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_arc)

        yield from bps.mv(energy, 2490)
        yield from bps.mv(energy, 2480)
        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2460)
        yield from bps.mv(energy, 2456)

        name_fmt = '{sample}_2456eV_postmeas'
        sample_name = name_fmt.format(sample=name)
        sample_id(user_name='SR', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.scan(dets, waxs, *waxs_arc)


def waxs_S_edge_Gui(t=1):
    dets = [pil300KW]
    
    names1 = ['P3HT']
    x1 = [-38700]
    y1 = [900]
    
    energies = [2460, 2465, 2470, 2474, 2475, 2476, 2478, 2480]
    Ys = np.linspace(900, 2200, 8)

    waxs_arc = [0, 39, 7]
    for name, xs, ys in zip(names1, x1, y1):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for e, ys in zip(energies, Ys):                              
            yield from bps.mv(energy, e)
            yield from bps.mv(piezo.y, ys)
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_arc)


        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2460)

        
        name_fmt = '{sample}_2460eV_postmeas'
        sample_name = name_fmt.format(sample=name)
        sample_id(user_name='SR', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.scan(dets, waxs, *waxs_arc)

    
def gratings_S_edge(t=1):
    dets = [pil300KW]
    
    names = ['1908_J3030_40p20cd']
    
    energies = [2400, 2432, 2433, 2434, 2435, 2436, 2437, 2438, 2439, 2440, 2441, 2442, 2443, 2444, 2445, 2446, 2447, 2448, 2449, 2450]
    
    for name in names:
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)


def gratings_Sn_edge(t=1):
    dets = [pil300KW]
    
    names = ['1908_YAHY_40p11cd']
    
    energies = [3900, 3920, 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3940]
    
    for name in names:
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_ai0.7deg'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)


def nikhil_Zn_edge(t=1):
    dets = [pil300KW, pil300kwroi2]
    
    names = ['Zn0_unexposed', 'Zn0_exposed']
    xs = [14000, -8000]
    
    energies = np.linspace(9620, 9700, 81)
    
    for x, name in zip(xs, names):
        bps.mv(piezo.x, x)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_ct{xbpm}_ai0.1deg'
        for e in energies:                              
            yield from bps.mv(energy, e)
            xbpm = xbpm3.sumX.value
            sample_name = name_fmt.format(sample=name, energy=e, xbpm ='%3.2f'%xbpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
        
        yield from bps.mv(energy, 9680)
        yield from bps.mv(energy, 9660)
        yield from bps.mv(energy, 9640)
        yield from bps.mv(energy, 9620)
        
def trans_sulf(en1, en2, step):
        eners = np.linspace(en1, en2, step)
        for e in eners:
                yield from bps.mv(energy, e)
                time.sleep(2)
                 

