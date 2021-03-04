def NEXAFS_S_edge(t=0.5):
    yield from bps.mv(waxs, 52.5)
    dets = [pil300KW]
    name = 'su8_ne'

    energies = np.linspace(2430, 2520, 91)
    
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
    for e in energies:                              
        yield from bps.mv(energy, e)
        yield from bps.sleep(1)
        
        bpm = xbpm3.sumX.value

        sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.2f'%bpm)
        sample_id(user_name='SR', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)


def NEXAFS_S_edge_fine(t=0.5):
    yield from bps.mv(waxs, 65)
    dets = [pil300KW]
    name = 'su8_ne_2'

    energies = np.arange(2440, 2470, 5).tolist() + np.arange(2470, 2475, 1).tolist() + np.arange(2475, 2485, 0.5).tolist() + np.arange(2485, 2500, 1).tolist() + np.arange(2500, 2520, 5).tolist()
    
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
    for e in energies:                              
        yield from bps.mv(energy, e)
        yield from bps.sleep(1)
        
        bpm = xbpm3.sumX.value

        sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.2f'%bpm)
        sample_id(user_name='SR', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)
    
    yield from bps.mv(energy, 2500)
    yield from bps.mv(energy, 2470)
    yield from bps.mv(energy, 2450)




def alignement_Tiwale(t=1):
    global names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, xs_hexa

    names=  ['su8_ue', 'su8_exp', 'uv6_ue', 'uv6_exp', 'pag_0',  'pag_20',  'pag_40']
    x_piezo = [53500,  34900,    25500,      5500,  -15500,    -38500,    -47500]
    y_piezo = [6859.975,   6900,     6900,      6900,    6900,      6900,      6900]
    z_piezo = [      0,        0,         0,       0,         0,         0]
    x_hexa =  [     10,       10,        10,      10,        10,         0]
    incident_angles = []
    y_piezo_aligned = []


    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique='gisaxs')

    for name, xs_piezo, zs_piezo, ys_piezo, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)
        yield from bps.mv(piezo.z, zs_piezo)

        yield from bps.mv(piezo.th, 0)
        yield from alignement_gisaxs_multisample(angle = 0.25)


        incident_angles = incident_angles + [piezo.th.position]
        y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    yield from smi.modeMeasurement()

    print(incident_angles)
    print(y_piezo_aligned)



def NEXAFS_S_edge_fine_multisample(t=0.5):

    global names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, xs_hexa

    names=  ['su8_ue', 'su8_exp', 'uv6_ue', 'uv6_exp', 'pag_0',  'pag_20',  'pag_40']
    x_piezo = [53500,  37900,    25500,      8500,  -15500,    -38500,    -47500]
    y_piezo = [ 6900,   6900,     6900,      6900,    6900,      6900,      6900]
    z_piezo = [    0,      0,        0,         0,       0,         0,         0]
    x_hexa =  [   10,     10,       10,        10,      10,        10,         0]
    incident_angles = [  0.2122, 0.168532, -0.113152, -0.313694, 0.233214, 0.207891, 0.186071]
    y_piezo_aligned = [6859.975, 6915.767,  6901.334,  6922.385, 6992.986, 7033.101, 7140.869]



    energies = np.arange(2440, 2470, 5).tolist() + np.arange(2470, 2475, 1).tolist() + np.arange(2475, 2485, 0.5).tolist() + np.arange(2485, 2500, 1).tolist() + np.arange(2500, 2520, 5).tolist()

    yield from bps.mv(waxs, 65)
    dets = [pil300KW]
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'

    for name, xs_piezo, zs_piezo, ys_piezo, xs_hexa, ais in zip(names, x_piezo, z_piezo, y_piezo_aligned, x_hexa, incident_angles):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)
        yield from bps.mv(piezo.z, zs_piezo)
        yield from bps.mv(piezo.th, ais + 0.7)

        for e in energies:                              
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)
            
            bpm = xbpm3.sumX.value

            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.2f'%bpm)
            sample_id(user_name='SR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
        
        yield from bps.mv(energy, 2500)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2470)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2450)
        yield from bps.sleep(2)



   


def saxs_prep_multisample(t=1):
    dets = [pil300KW]

    energies = [2450, 2475, 2476, 2477, 2478, 2479, 2480, 2481, 2482, 2483, 2484, 2490, 2500]
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_pos{posi}_wa{wa}_xbpm{xbpm}'
    
    waxs_range = np.linspace(0, 39, 7)

    # names=  [  'pag_0',  'pag_20',  'pag_40']
    # x_piezo = [ -15500,    -38500,    -47500]
    # y_piezo = [   6900,      6900,      6900]
    # z_piezo = [      0,         0,         0]
    # x_hexa =  [      7,         7,         0]
    # incident_angles = [ 0.233214, 0.207891, 0.186071]
    # y_piezo_aligned = [ 6992.986, 7033.101, 7140.869]


    names=  [ 'pag_40']
    x_piezo = [ -47500]
    y_piezo = [   6900]
    z_piezo = [      0]
    x_hexa =  [     -4]
    incident_angles = [ 0.186071]
    y_piezo_aligned = [ 7140.869]

    det_exposure_time(t,t)

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)

        for name, xs_piezo, zs_piezo, ys_piezo, xs_hexa, ais in zip(names, x_piezo, z_piezo, y_piezo_aligned, x_hexa, incident_angles):
            yield from bps.mv(stage.x, xs_hexa)
            yield from bps.mv(piezo.x, xs_piezo)
            yield from bps.mv(piezo.y, ys_piezo)
            yield from bps.mv(piezo.z, zs_piezo)
            yield from bps.mv(piezo.th, ais)

            for k, e in enumerate(energies):  
                yield from bps.mv(piezo.x, xs_piezo - k * 300)
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                name_fmt = '{sample}_saxs_ai{ai}_{energy}eV_xbpm{xbpm}_wa{wa}'

                for j, aiss in enumerate([0.3, 0.5, 0.7, 1.0, 1.5]):
                    yield from bps.mv(piezo.th, ais + aiss)

                    sample_name = name_fmt.format(sample=name, ai = '%1.2f'%aiss, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                    sample_id(user_name='OS', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)
                                    

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)


def SAXS_S_edge_fine(t=1):
    dets = [pil1M]
    name = 's3_ai0.9deg_sdd2.5m'
    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2475, 1).tolist() + np.arange(2475, 2485, 0.5).tolist() + np.arange(2485, 2500, 1).tolist() + np.arange(2500, 2520, 5).tolist()
    
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
    for e in energies:                              
        yield from bps.mv(energy, e)
        yield from bps.sleep(1)
        
        bpm = xbpm3.sumX.value

        sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.2f'%bpm)
        sample_id(user_name='SR', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)
    
    yield from bps.mv(energy, 2500)
    yield from bps.mv(energy, 2470)
    yield from bps.mv(energy, 2450)



def fly_scan_ai_nikhil(det, motor, cycle=1, cycle_t=10, phi = -0.6):
    start = phi - 35
    stop = phi + 35

    acq_time = cycle * cycle_t

    yield from bps.mv(motor, start)
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


def SAXS_S_edge_allprs(t=1):
    dets = [pil1M]
    name = 's2_ai0.9deg'
    
    prs0 = 1.275
    det_exposure_time(t,t) 
    name_fmt = '{sample}_2450eV_sdd2.5m_prs{prs}_xbpm{xbpm}'

    for prs_pos in np.linspace(-25, 25, 1001):                              
        yield from bps.mv(prs, prs0 + prs_pos)
        yield from bps.sleep(1)
        
        bpm = xbpm3.sumX.value

        sample_name = name_fmt.format(sample=name, prs='%3.2f'%prs_pos, xbpm = '%3.2f'%bpm)
        sample_id(user_name='SR', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)
    