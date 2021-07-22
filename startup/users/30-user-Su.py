def run_saxs_nexafs_greg(t=1):
    # yield from nexafs_prep_multisample_greg(t=0.5)
    # yield from bps.sleep(10)
    yield from saxs_prep_multisample(t=0.5)




def nexafs_prep_multisample_greg(t=1):

    yield from bps.mv(stage.y, -5.5)
    yield from bps.mv(stage.th, 1.5)


    # samples = ['sample02', 'sample03', 'sample04', 'sample05', 'sample06', 'sample07', 'sample08', 'sample01']
    # x_list  = [32500, 19500, 8500, -3500, -15500, -27500, -39500, 44500]
    # y_list =  [3900,  3900,  3900,  3900, 3900,  3900,   3900,   3900]

    samples = ['sample02a_', 'sample03a']
    x_list  = [32500, 19500]
    y_list =  [3900,  3900]

    for x, y, name in zip(x_list, y_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)

        yield from NEXAFS_Ca_edge_multi_greg(t=t, name=name)
    

    # yield from bps.mv(stage.y, -6.5)
    # yield from bps.mv(stage.th, 1.5)

    # samples = ['sample09', 'sample10', 'sample11']
    # x_list  = [41000, 24000, 9000]
    # y_list =  [-9500, -9500, -9500]

    # for x, y, name in zip(x_list, y_list, samples):
    #     yield from bps.mv(piezo.x, x)
    #     yield from bps.mv(piezo.y, y)

    #     yield from NEXAFS_Ca_edge_multi_greg(t=t, name=name)


    sample_id(user_name='test', sample_name='test')



def saxs_prep_multisample(t=1):
    dets = [pil300KW, pil1M]

    energies = [4030, 4040, 4050, 4055, 4075]
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_pos{posi}_wa{wa}_xbpm{xbpm}'
    waxs_range = np.linspace(0, 39, 7)

    det_exposure_time(t,t)

    for wa in waxs_range[::-1]:
        yield from bps.mv(waxs, wa)

        samples = ['mwet_01', 'mwet_02', 'mwet_03', 'mwet_04', 'mwet_05', 'mwet_06', 'mwet_07', 'mwet_08', 'mwet_09', 'mwet_10', 'mwet_11', 'mwet_12', 'mwet_13', 'mwet_14']
        x_list  = [    43000,     33000,     23000,     12000,      1000,    -11000,    -22500,    -33000,     41500,     30500,     19500,      8500,     -3000,    -14000]
        y_list =  [    -8000,     -8000,     -8000,     -8000,     -8000,     -8000,     -8000,     -8000,      5000,      5000,      5000,      5000,      5000,      5000]
        

        for name, x, y in zip(samples, x_list, y_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for k, e in enumerate(energies):                              
                yield from bps.mv(energy, e)
                yield from bps.mv(piezo.y, y + k * 30)

                name_fmt = '{sample}_pos{pos}_{energy}eV_xbpm{xbpm}_wa{wa}'

                for i in [0, 1, 3]:
                    yield from bps.mv(piezo.x, x + i * 500)

                    sample_name = name_fmt.format(sample=name, pos = '%1.1d'%i, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                    sample_id(user_name='OS', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)
                            
            yield from bps.mv(energy, 4050)
            yield from bps.mv(energy, 4030)


def NEXAFS_Ca_edge_multi_greg(t=0.5, name='test'):
    yield from bps.mv(waxs, 52.5)
    dets = [pil300KW]

    energies = np.linspace(4030, 4150, 121)


    samples = ['mwet_01', 'mwet_02', 'mwet_03', 'mwet_04', 'mwet_05', 'mwet_06', 'mwet_07', 'mwet_08', 'mwet_09', 'mwet_10', 'mwet_11', 'mwet_12', 'mwet_13', 'mwet_14']
    x_list  = [    43000,     33000,     23000,     12000,      1000,    -11000,    -22500,    -33000,     41500,     30500,     19500,      8500,     -3000,    -14000]
    y_list =  [    -8000,     -8000,     -8000,     -8000,     -8000,     -8000,     -8000,     -8000,      5000,      5000,      5000,      5000,      5000,      5000]
    

    for name, x, y in zip(samples, x_list, y_list):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y + 500)

        det_exposure_time(t,t) 
        name_fmt = 'nexafs_{sample}_{energy}eV_xbpm{xbpm}'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.2f'%xbpm3.sumY.value)
            RE.md['filename_amptek'] = sample_name
            sample_id(user_name='GS', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 4125)
        yield from bps.mv(energy, 4100)        
        yield from bps.mv(energy, 4075)
        yield from bps.mv(energy, 4050)
        yield from bps.mv(energy, 4030)

        sample_id(user_name='test', sample_name='test')



def run_day():
    yield from NEXAFS_Ca_edge_multi_greg(t=0.5)
    yield from saxs_prep_multisample(t=0.5)


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