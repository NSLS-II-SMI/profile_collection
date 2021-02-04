def alignement_katz_2021_1():
    global names, x_piezo, y_piezo, z_piezo, incident_angles, y_piezo_aligned
    
    # names =   ['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6', 'sample7']
    # x_piezo = [  -48000,     -35000,    -21000,     10000,     24000,     37000,     50000]
    # y_piezo = [    6900,       5300,      5300,      5300,      5300,      5300,      5300]
    # z_piezo = [    2700,       1200,     -1200,     -1200,     -1200,      -700,     -1200]

    names =   ['sample3redo']
    x_piezo = [   -20500]
    y_piezo = [     5312]
    z_piezo = [     1200]

    # incident_angles = []
    # y_piezo_aligned = []

    # yield from smi.modeAlignment(technique='gisaxs')
    #sample2: y = 5332.784, th = 0.973826
    #sample 4:: th [2, 0.9738, 2, 0.97, 0.582, 0.297, 0.0655], y: [7100, 5332.784, 5142.4, 4975.875, 5447.996, 5487.398, 5792.193]

    # incident_angles = [2, 0.9738, 2, 0.97, 0.582, 0.297, 0.0655]
    # y_piezo_aligned = [7100, 5332.784, 5142.4, 4975.875, 5447.996, 5487.398, 5792.193]

    incident_angles = [0.8738]
    y_piezo_aligned = [5312.784]
    # for name, xs_piezo, ys_piezo, zs_piezo in zip(names[3:], x_piezo[3:], y_piezo[3:], z_piezo[3:]):
    #     yield from bps.mv(piezo.x, xs_piezo)
    #     yield from bps.mv(piezo.y, ys_piezo)
    #     yield from bps.mv(piezo.z, zs_piezo)

    #     yield from alignement_gisaxs_multisample_special(angle = 0.3)

    #     incident_angles = incident_angles + [piezo.th.position]
    #     y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    # yield from smi.modeMeasurement()

    print(incident_angles)


def nexafs_Sedge_Katz(t=1):
    dets = [pil300KW]

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