def run_saxs_nexafs_greg(t=1):
    # yield from nexafs_prep_multisample_greg(t=0.5)
    # yield from bps.sleep(10)
    yield from saxs_prep_multisample(t=0.5)


def Su_nafion_nexafs_S_edge(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20, 40]
    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())

    yield from bps.mv(stage.y, 0)
    yield from bps.mv(stage.th, 0)

    names = ['NCo0','NCo14','NCo29','NCo33', 'DK_D139']
    x =     [ 43700,  21300,  -1700, -24600,    -55000]
    y =     [ -2400,  -2400,  -2000,  -2000,     -2400]
    z =     [  1186,   1186,   1186,   1186,      1186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_{sample}_{energy}eV_sdd3m_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


    yield from bps.mv(stage.th, 5)
    yield from bps.mv(stage.y, -15)

    names = ['NCo70', 'NCo114', 'DK_N115', 'DK_D114', 'DK_D136']
    x =     [  48300,    25800,      3300,    -18800,    -41800]
    y =     [  -9500,    -9500,     -9500,     -9500,     -9500]
    z =     [  14186,    14186,     14186,     14186,     14186]


    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)




def Su_nafion_swaxs_S_edge(t=1):
    dets = [pil900KW, pil300KW]

    waxs_arc = [0, 20]
    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())
    # energies = np.asarray(np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist())

    names = ['AK_PFSA_HPA','AK_PFSA_ref','MP_5', 'MP_6', 'MP_7']
    x =     [        43000,        20000, -2500, -25000, -56500]
    y =     [         1000,         1000,  2500,  -1000,   2400]
    z =     [         1186,         1186,  1186,   1186,   1186]

    # names = ['MP_6', 'MP_7']
    # x =     [-25000, -56500]
    # y =     [  1000,   2400]
    # z =     [  1186,   1186]


    # for name, xs, ys, zs in zip(names, x, y, z):
    #     yield from bps.mv(piezo.x, xs)
    #     yield from bps.mv(piezo.y, ys)
    #     yield from bps.mv(piezo.z, zs)

    #     yss = np.linspace(ys, ys + 1000, 58)
    #     xss = np.linspace(xs, xs, 1)

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)    

    #         if wa ==0:
    #             dets = [pil900KW]
    #         else:
    #             dets = [pil900KW, pil1M]

    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}'
    #         for e, xsss, ysss in zip(energies, xss, yss): 
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(3)

    #             yield from bps.mv(piezo.y, ysss)
    #             yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
    #             sample_id(user_name='GF', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)

    #         yield from bps.mv(energy, 2470)
    #         yield from bps.sleep(3)
    #         yield from bps.mv(energy, 2450)
    #         yield from bps.sleep(3)


    waxs_arc = [0, 20]

    yield from bps.mv(stage.th, 0)
    yield from bps.mv(stage.y, -6)

    # names = ['MP_8', 'MP_1', 'MP_2', 'MP_3', 'MP_4']
    # x =     [ 46500,  21000,  -1500, -26500, -48000]
    # y =     [ -9500,  -9500,  -9500,  -9500,  -9500]
    # z =     [  1186,   1186,   1186,   1186,   1186]

    names = [   'MP_4']
    x =     [  -47000]
    y =     [    -8000]
    z =     [     1186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 67)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    
            
            if wa ==0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 

                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            # yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2830)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2810)           
            # yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)



def Su_nafion_waxs_S_edge(t=1):
    dets = [pil300KW, pil1M]

    yield from bps.mv(GV7.open_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.open_cmd, 1 )

    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())
    waxs_arc = np.linspace(0, 26, 5)

    yield from bps.mv(stage.y, 0)
    yield from bps.mv(stage.th, 0)

    names = ['SPES20','SPES40','SPES60','70nPA']
    x = [41500, 18500, -4500, -26500]
    y = [1500,  1000,   500,  -500]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 15)
        xss = np.linspace(xs, xs + 1000, 4)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)

    yield from bps.mv(stage.th, 1)
    yield from bps.mv(stage.y, -8)
    
    names = ['50nPA', '30nPA', '10nPA']
    x = [30500, 7500, -14200]
    y = [-9600, -9600, -9700]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 15)
        xss = np.linspace(xs, xs + 1000, 4)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)




def nexafs_Su(t=1):
    dets = [pil300KW]

    energies = np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())
    # energies = np.linspace(2450, 2500, 51)
    waxs_arc = [52.5]

    names = ['sampleA_redo', 'sampleB', 'sampleC', 'sampleD']
    x = [-22200, -33200, -38700, -29600]
    y = [ -5250,  -5250,  -5450,   7600]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    
            det_exposure_time(t,t) 
            name_fmt = 'nexafs_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e in energies: 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def waxs_S_edge_greg_2021_2(t=1):
    dets = [pil300KW, pil1M]
    yield from bps.mv(prs, 1)

    names = ['sampleA', 'sampleB', 'sampleC', 'sampleD']
    x = [-22200, -33200, -39200, -29600]
    y = [ -5250,  -5250,  -5450,   7600]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 2).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(13, 13, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 200, 33)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t)

            name_fmt = '{sample}_1.6m_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def humidity_experiment(t=1):
    dets = [pil300KW, pil1M]

    # ai_aligned = [1.931, 1.788, 1.666, 1.817]
    # ys_aligned = [3.2, 3.189, 3.122, 3.053]
    # names = ['A30_T0', 'A50_T0', 'A70_T0', 'A90_T0']
    # x_hexa = [     23,        8,       -6,      -18]
    # y_hexa = [    3.2,      3.2,      3.2,      3.2]

    ai_aligned = [1.1248, 0.985, 0.995, 0.916] 
    ys_aligned = [3.293, 3.247, 3.19, 3.123]
                                                                                                                                           
    # names = ['A30_T7', 'A50_T7', 'A70_T7', 'A90_T7']
    # x_hexa = [     22,       9,       -7,      -16.5]
    # y_hexa = [    3.2,      3.2,      3.2,      3.2]

    names = ['bkg']
    x_hexa = [23.6]
    y_hexa = [    0]

    setDryFlow(5)
    setWetFlow(0)

    humidity = '%3.2f'%readHumidity(verbosity=0)

    waxs_arc = np.linspace(0, 13, 3)

    ai_list = [0.10]

    for num, (name, xs_hexa, ys_hexa) in enumerate(zip(names, x_hexa, y_hexa)):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(stage.y, ys_hexa)

        # yield from alignement_special_hex(angle = 0.15)

        # ai_aligned = ai_aligned + [ai0]
        # ys_aligned = ys_aligned + [stage.y.position]
        
        # yield from bps.mv(stage.y, ys_aligned[num])
        # yield from bps.mv(stage.th, ai_aligned[num])

        ai0 = stage.th.position

        # print(ai_aligned)
        # print(ys_aligned)

        det_exposure_time(t,t)                                                                                                                                                                     

        for i, wa in enumerate(waxs_arc[::-1]):
            yield from bps.mv(waxs, wa)
            
            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + k*0.2)
 
                name_fmt = '{sample}_posthumi_16.1keV_3m_hum{hum}_wa{wax}'
                sample_name = name_fmt.format(sample=name, hum = humidity, wax = wa)
                sample_id(user_name='AB', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
        yield from bps.mv(stage.th, ai0)

    print(ai_aligned)
    print(ys_aligned)



def waxs_Se_edge_greg(t=1):
    
    det_exposure_time(t,t) 

    names = ['PBTTTSe_neat', 'P3RSe_dopped', 'PBTTTS_dopped', 'PBTTTSe_dopped']
    x = [      23700,  17600, 11300,  5400]
    y = [      -8300,  -8400, -8200, -8600]

    dets = [pil300KW, pil1M]
    energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12716, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 400, 32)
        xss = np.array([xs, xs - 400])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%7.2f'%e, wax = wa, xbpm = '%1.3f'%bpm)
                sample_id(user_name='CM', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 12680)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12645)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12620)
            yield from bps.sleep(2)


    
def Su_nafion_swaxs_K_edge(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20, 40]
    energies = np.asarray(np.arange(3570, 3600, 5).tolist() + np.arange(3600, 3608, 2).tolist() + np.arange(3608, 3640, 1).tolist()+ np.arange(3640, 3690, 5).tolist())

    yield from bps.mv(stage.y, 5)
    yield from bps.mv(stage.th, 0)

    names = ['MP_1', 'MP_3']
    x =     [ -1000, -23000]
    y =     [  3000,   2000]
    z =     [  1186,   1186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 52)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc[::-1]:
            yield from bps.mv(waxs, wa)    

            if wa ==0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_sdd3m_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 3650)
            yield from bps.mv(energy, 3610)

        
def Su_nafion_nexafs_K_edge(t=1):
    dets = [pil900KW]

    waxs_arc = [40]
    energies = np.asarray(np.arange(3570, 3600, 5).tolist() + np.arange(3600, 3608, 2).tolist() + np.arange(3608, 3640, 1).tolist()+ np.arange(3640, 3690, 5).tolist())

    yield from bps.mv(stage.y, 5)
    yield from bps.mv(stage.th, 0)

    names = ['MP_1']
    x =     [ -1000]
    y =     [  3000]
    z =     [  1186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 52)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_{sample}_{energy}eV_sdd3m_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 3650)
            yield from bps.mv(energy, 3610)




def Su_nafion_swaxs_Co_edge(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20, 40]
    energies = np.asarray(np.arange(7650, 7700, 5).tolist() + np.arange(7700, 7750, 1).tolist() + np.arange(7750, 8405, 5).tolist())
    yield from bps.mv(stage.th, 0)

    names = [ 'NCo0', 'NCo14', 'NCo29', 'NCo033', 'NCo70', 'NCo114']
    x =     [ -56000,   46000,   22000,        0,  -23000,   -46000]
    y =     [   1000,   -9500,   -9500,    -9500,   -9500,    -9500]
    z =     [   1186,    1186,    1186,     1186,    1186,     1186]
    y_hexa = [     5,      -6,      -6,       -6,      -6,       -6]
    
    for name, xs, ys, ys_hexa, zs in zip(names, x, y, y_hexa, z):
        if name == 'NCo0':
            waxs_arc = [0, 20]
        else:
            waxs_arc = [0, 20, 40]

        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.y, ys_hexa)

        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1700, 170)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc[::-1]:
            yield from bps.mv(waxs, wa)    

            if wa ==0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_sdd3m_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            
            for ene in np.linspace(8400, 7660, 38):
                yield from bps.mv(energy, ene)
                yield from bps.sleep(2)





def Su_nafion_swaxs_hard(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20, 40]
    yield from bps.mv(stage.th, 0)

    # names = ['AK_PFSA_HPA','AK_PFSA_ref']
    # x =     [        43000,        20000]
    # y =     [         2000,         1500]
    # z =     [         1186,         1186]
    # y_hexa = [           5,            5]
    
    names = ['DK_N115', 'DK_D114', 'DK_D136', 'DK_D139', 'DK_D165', 'MP_5', 'MP_6', 'MP_7', 'MP_8']
    x =     [    42000,     17000,      -5000,   -30000,    -56000,  45000,   5000, -18000,  -41000]
    y =     [     3500,      3500,       3500,     3500,      2500,  -8500,  -8500,  -8200,  -8200]
    z =     [     1186,      1186,       1186,     1186,      1186,   1186,   1186,   1186,   1186]
    y_hexa = [       5,         5,          5,        5,         5,    -6,      -6,     -6,     -6]

    x =     [  -41000]
    y =     [    -8200]
    z =     [   1186]
    y_hexa = [       -6]

    for name, xs, ys, ys_hexa, zs in zip(names, x, y, y_hexa, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.y, ys_hexa)
        yield from bps.mv(piezo.z, zs)


        for wa in waxs_arc[::-1]:
            yield from bps.mv(waxs, wa)    

            if wa ==0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t) 
            name_fmt = '{sample}_16.1keV_sdd5m_wa{wax}'

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(sample=name, wax = wa)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)









def Su_nafion_swaxs_S_edge_SVA_2021_3(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20]
    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())

    names = ['bkg','NCo0','NCo14','NCo33','NCo70','NCo114','MP_5', 'MP_6', 'MP_7', 'MP_7']
    x =     [ 30.5,  24.0,   18.0,   11.5,    5.0,    -1.2,  -7.6,  -14.0,  -20.2,  -26.5]
    y =     [ -1.5,  -1.5,   -1.7,   -1.7,   -1.7,    -1.7,  -1.7,   -1.7,   -1.7,   -1.7]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(stage.x, xs)
        yield from bps.mv(stage.y, ys)

        yss = np.linspace(ys, ys + 0.4 , 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            if wa ==0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}_hum0per'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(stage.y, ysss)
                yield from bps.mv(stage.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)


    # # Measure at flow 100 percent
    setDryFlow(0)
    setWetFlow(5)
    yield from bps.sleep(600)

   names = ['bkg','NCo0','NCo14','NCo33','NCo70','NCo114','MP_5', 'MP_6', 'MP_7', 'MP_7']
    x =     [ 30.5,  24.0,   17.5,   11.5,    5.0,    -1.5,  -8.0,  -14.0,  -20.5,  -26.5]
    y =     [ -1.5,  -1.5,   -1.5,   -1.5,   -1.5,    -1.5,  -1.5,   -1.5,   -1.5,   -1.5]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(stage.x, xs)
        yield from bps.mv(stage.y, ys)

        yss = np.linspace(ys+0.4, ys + 0.8 , 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            if wa ==0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}_hum100per'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(stage.y, ysss)
                yield from bps.mv(stage.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)


    # # Measure at flow 100 percent
    setDryFlow(5)
    setWetFlow(0)
    yield from bps.sleep(600)

    names = ['bkg','NCo0','NCo14','NCo33','NCo70','NCo114','MP_5', 'MP_6', 'MP_7', 'MP_7']
    x =     [ 30.5,  24.0,   17.5,   11.5,    5.0,    -1.5,  -8.0,  -14.0,  -20.5,  -26.5]
    y =     [ -1.5,  -1.5,   -1.5,   -1.5,   -1.5,    -1.5,  -1.5,   -1.5,   -1.5,   -1.5]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(stage.x, xs)
        yield from bps.mv(stage.y, ys)

        yss = np.linspace(ys+0.8, ys + 1.2 , 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            if wa ==0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}_hum0per_aftercycle'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(stage.y, ysss)
                yield from bps.mv(stage.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)


    setDryFlow(0)
    setWetFlow(0)