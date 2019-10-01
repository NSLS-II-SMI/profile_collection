def run_waxs_IC(t=1): 
    dets = [pil300KW, pil1M]
    
    
    names = ['2um_725_7m', '2um_725_45d_7m', '5um_825_7m','5um_825_45d_7m', '10um_825_7m', '10um_825_45d_7m', 'AgBh']
    x = [34000, 36000 ,19500 ,13500 , 4500 ,-3000 ,-25000 ]

    energies = [2405, 2465, 2471, 2473, 2475, 2477, 2479, 2481]
    
    waxs_arc = [0, 19.5, 4]
    
    for xs, name in zip(x, names):
        yield from bps.mv(piezo.x , xs)
        
        if name == '2um_725_45d_7m' or name == '5um_825_45d_7m' or name == '10um_825_45d_7m':
            yield from bps.mv(prs , 45)
        else:
            yield from bps.mv(prs , 0)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for i, e in enumerate(energies):
                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='IC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_arc)
            if e == 2405:
                yield from bps.mv(energy, 2430)
            elif e == 2481:
                yield from bps.mv(energy, 2460)
                yield from bps.mv(energy, 2430)
                yield from bps.mv(energy, 2405)
                name_fmt = '{sample}_2405eV_postedge'
                sample_name = name_fmt.format(sample=name)
                sample_id(user_name='IC', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.scan(dets, waxs, *waxs_arc)

    names = ['10um_825_45d_7m_nexafs_w20']
    x = [-5000]
    dets = [pil300KW]  
    yield from bps.mv(waxs, 20)
    yield from bps.mv(energy, 2420)
    yield from bps.mv(energy, 2440)
    yield from bps.mv(energy, 2450)
    energies = np.linspace(2450, 2531, 163)
    for xs, name in zip(x, names):
        yield from bps.mv(piezo.x , xs)
        yield from bps.mv(prs , 0)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for i, e in enumerate(energies):                  
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='IC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num = 1)
            if e == 2405:
                yield from bps.mv(energy, 2430)
            elif e > 2530.6:
                yield from bps.mv(energy, 2500)
                yield from bps.mv(energy, 2470)
                yield from bps.mv(energy, 2430)
                yield from bps.mv(energy, 2405)
                name_fmt = '{sample}_2405eV_postedge'
                sample_name = name_fmt.format(sample=name)
                sample_id(user_name='IC', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num = 1)
        
        
def film_Sn_edge2(t=0.5):
    dets = [pil300KW]
    
    names = ['1909_utbVE_40p11cd_ai1p1_2bragg_w3p7', '1909_utbVE_40p11cd_ai1p1_2bragg_bkg_w3p7']
    x = [6700, -5000]

    
    energies = np.concatenate([np.asarray([3850, 3900, 3920, 3925]), np.arange(3930, 3941, 1)])
    for xs, name in zip(x, names):
        yield from bps.mv(piezo.x , xs)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for e in energies:                              
            yield from bps.mv(energy, e)

            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='IC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
            
            if e == 3850:
                yield from bps.mv(energy, 3875)
                
            elif e > 3939.5:
                yield from bps.mv(energy, 3920)
                yield from bps.mv(energy, 3890)
                yield from bps.mv(energy, 3850)
                name_fmt = '{sample}_3850eV_postedge'
                sample_name = name_fmt.format(sample=name)
                sample_id(user_name='IC', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)



def film_Sn_edge1(t=0.5):
    dets = [pil300KW]
    
    names = ['1909_bbVE_40p11cd_ai1p1_2bragg_w3p7', '1909_bbVE_40p11cd_ai1p1_2bragg_bkg_w3p7']
    x = [-23000, -17000]

    
    energies = np.concatenate([np.asarray([3850, 3900, 3920]), np.arange(3925, 3935, 0.5),  np.arange(3935, 3946, 1)])
    for xs, name in zip(x, names):
        yield from bps.mv(piezo.x , xs)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for e in energies:                              
            yield from bps.mv(energy, e)

            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='IC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
            
            if e == 3850:
                yield from bps.mv(energy, 3875)
                
            elif e > 3944.5:
                yield from bps.mv(energy, 3920)
                yield from bps.mv(energy, 3890)
                yield from bps.mv(energy, 3850)
                name_fmt = '{sample}_3850eV_postedge'
                sample_name = name_fmt.format(sample=name)
                sample_id(user_name='IC', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


def film_Sn_edge(t=0.5):
    dets = [pil300KW]
    
    names = ['1909_utbVE_40p11CD_ai0p5deg']
    
    energies = [3850, 3900, 3920, 3925, 3930, 3935, 3945, 3850]
    waxs_arc = [3, 16, 3]
    i = 0
    for name in names:
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for e in energies:                              
            yield from bps.mv(energy, e)
            if i == 1:
                name_fmt = '{sample}_{energy}eV_postedge'
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='IC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_arc)
            
            if e == 3850:
                yield from bps.mv(energy, 3875)
                
            elif e == 3945:
                yield from bps.mv(energy, 3920)
                yield from bps.mv(energy, 3890)
                yield from bps.mv(energy, 3850)
                i = 1
  
                
def fly_scan_ai(det, motor, cycle=1, cycle_t=10, phi = -0.6):
    start = phi + 0
    stop = phi + 4.5
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

