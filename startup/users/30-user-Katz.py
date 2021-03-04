def alignement_katz_2021_1():
    global names, x_piezo, y_piezo, z_piezo, incident_angles, y_piezo_aligned
    
    names =   ['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6', 'sample7']
    x_piezo = [   55000,     42000,     19000,      2000,    -16000,    -31000,    -49000]
    y_piezo = [    4800,      2900,      2900,      2900,      2900,      2900,      3300]
    x_hexa =  [       7,         0,         0,         0,         0,         0,         0]

    incident_angles = [       0,      0,        0,        0,        0,        0,       0]
    y_piezo_aligned = [4757.703, 3054.9, 3133.065, 3031.989, 3414.158, 3546.666, 3715.74]

    #sample2: y = 5332.784, th = 0.973826
    #sample 4:: th [2, 0.9738, 2, 0.97, 0.582, 0.297, 0.0655], y: [7100, 5332.784, 5142.4, 4975.875, 5447.996, 5487.398, 5792.193]

    # incident_angles = [2, 0.9738, 2, 0.97, 0.582, 0.297, 0.0655]
    # y_piezo_aligned = [7100, 5332.784, 5142.4, 4975.875, 5447.996, 5487.398, 5792.193]

    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique='gisaxs')


    for name, xs_piezo, ys_piezo, xs_hexa in zip(names, x_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)

        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)
        # yield from alignement_gisaxs(0.3)

        yield from alignement_gisaxs_multisample_special(angle = 0.25)

        y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    yield from smi.modeMeasurement()

    print(incident_angles)



def nexafs_Sedge_Katz(t=1):
    dets = [pil300KW]


    names =   ['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6', 'sample7']
    x_piezo = [   55000,     42000,     19000,      2000,    -16000,    -31000,    -49000]
    y_piezo = [    4800,      2900,      2900,      2900,      2900,      2900,      3300]
    x_hexa =  [       7,         0,         0,         0,         0,         0,         0]

    incident_angles = [       0,      0,        0,        0,        0,        0,       0]
    y_piezo_aligned = [4757.703, 3054.9, 3133.065, 3031.989, 3414.158, 3546.666, 3715.74]


    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())
    waxs_arc = [52.5]

    for name, xs, ys, zs, aiss, ys in zip(names, x_piezo, y_piezo, z_piezo, incident_angles, y_piezo_aligned):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, aiss + 0.7)

        ai0 = piezo.th.position

        yield from bps.mv(waxs, waxs_arc[0])    
        det_exposure_time(t,t) 
        name_fmt = 'nexafs_{sample}_{energy}eV_wa52.5_bpm{xbpm}'
        for e in energies: 
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, xbpm = '%4.3f'%bpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 2490)
        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2450)




def nexafs_Caedge_Katz(t=1):
    dets = [pil300KW]

    names =   ['sample7_1']

    energies = np.linspace(4030, 4110, 81)
    waxs_arc = [52.5]

    for name in names:

        ai0 = piezo.th.position

        yield from bps.mv(waxs, waxs_arc[0])    
        det_exposure_time(t,t) 
        name_fmt = 'nexafs_{sample}_{energy}eV_wa52.5_ai0.7deg_bpm{xbpm}'
        for e in energies: 
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, xbpm = '%4.3f'%bpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 4100)
        yield from bps.mv(energy, 4080)
        yield from bps.mv(energy, 4050)