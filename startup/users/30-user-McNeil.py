  
def waxs_Se_edge_chris_n(t=1):
    
    dets = [pil300KW]
    

    names = ['J1_01', 'J1_02', 'J1_03', 'J1_04']
    x = [18200, 12400,  6400,   400]
    y = [-7300, -7400, -7500, -7500]

    energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12701, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 31)
        xss = np.array([xs, xs + 500])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%7.2f'%e, wax = wa, xbpm = '%1.3f'%bpm)
                sample_id(user_name='CM', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)



            yield from bps.mv(energy, 12670)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12640)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12620)
            yield from bps.sleep(2)




def NEXAFS_Br_edge(t=0.5, name='sample1'):
        dets = [pil300KW]
        #name = 'Kapton_NEXAFS_1_gvopen_wa70_'
        #x = [8800]

        energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12716, 5).tolist()
        energies = 815 + np.asarray(energies)

        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy='%7.2f'%e, xbpm = '%3.1f'%xbpm3.sumY.value)
            sample_id(user_name='CM', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 13500)



def waxs_Br_edge_chris(t=1):
    
    det_exposure_time(t,t) 

    names = ['Br_01_02', 'Br_01_03']
    x = [       46300,  41200]
    y = [       -9200,  -9200]

    dets = [pil300KW, pil1M]
    energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12716, 5).tolist()
    energies = 815 + np.asarray(energies)

    waxs_arc = np.linspace(0, 26, 5)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 500, 32)
        xss = np.array([xs, xs - 500])

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

            yield from bps.mv(energy, 13495)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 13460)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 13435)
            yield from bps.sleep(2)



def giwaxs_Se_edge_chris(t=1):
    dets = [pil300KW]
    
    names = ['J2_01', 'J2_02', 'J2_03', 'J2_04']
    x = [      46000,   28000,   10000,  -11000]

    energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12701, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)
    ai0 = 0

    for name, xs in zip(names, x):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.th, ai0)

        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)        
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)

        yield from alignement_gisaxs(angle = 0.2)
        
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        yield from bps.mv(piezo.th, ai0 + 0.13)

        xss = np.linspace(xs, xs - 8000, 71)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_ai0.13_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%7.2f'%e, wax = wa, xbpm = '%1.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

       
            yield from bps.mv(energy, 12670)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12640)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12620)
            yield from bps.sleep(2)




def nexafs_90deg_McNeil(t=1):
    dets = [pil300KW]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = [52.5]

    ai = [0.7, 20, 55]

    names = ['D1_06']

    for name in names:
        det_exposure_time(t,t) 
        name_fmt = 'nexafs_vert_{sample}_{energy}eV_angle{ai}_bpm{xbpm}'
        
        ai0 = prs.position


        for ais in ai:
            yield from bps.mv(prs, ai0-ais)
            yield from bps.mvr(piezo.y, 100)


            for e in energies: 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%2.2d'%ais, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2450)


def giwaxs_vert_S_edge_McNeil(t=1):
    dets = [pil300KW]

    names = ['3-2_ver_per_redo']
    x = [-1333.6]
    ys = [-5000]
    # names = ['3-1_ver_par', '3-2_ver_per', '4-1_ver']

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()

    waxs_arc = [4, 10.5, 17]
    dets = [pil300KW]

    for name, y in zip(names, ys):
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(piezo.y, y)

            if i==0:
                print('wa=4deg')
            else:
                yield from bps.mv(waxs, wa)   

            name_fmt = 'GIWAXS_90deg_{sample}_{energy}eV_pos{pos}_ai1.5_wa{wax}_bpm{xbpm}'
            for k, e in enumerate(energies):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mvr(piezo.y, 3)

                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, pos = '%2.2d'%k, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


    for name, y in zip(names, ys):
        yield from bps.mv(piezo.y, y)

        name_fmt = 'GIWAXS_90deg_{sample}_{energy}eV__pos{pos}_ai1.5_wa{wax}_bpm{xbpm}'
        for k, e in enumerate(energies):
            yield from bps.mvr(piezo.y, 3)

            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, energy=2450, pos = '%2.2d'%k, wax = 17, xbpm = '%4.3f'%bpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)



def transition_S_Cl_edges():
    yield from bps.mv(energy, 2450)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2475)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2500)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2525)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2550)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2580)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2610)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2640)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2660)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2680)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2700)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2720)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2740)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2760)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2780)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2800)
    yield from bps.sleep(5)





def nexafs_oriented_S_edge_corr_only_allprs(t=1):
    dets = [pil300KW]
        
    #prs 0 deg
    yield from bps.mv(prs, 1)
    names = ['1-1_par_prs0deg', '1-2_per_prs0deg', '1-3_45de_prs0deg', '2-2_prs0deg', '5-1_par_prs0deg', '5-2_per_prs0deg', '5-3_45de_prs0deg',
    '6-1_prs0deg']
    x = [                13300,              4600,              -6600,        -15000,              9000,               700,              -7300,
           -15500]
    y = [                -6000,             -5800,              -6200,         -5500,              7000,              6700,              6700,
             7500]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(52, 52, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 250, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            yield from bps.mv(energy, 2500)
            name_fmt = 'nexafs_intcor_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.sleep(0.5)
                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

    
    #prs 30 deg
    yield from bps.mv(prs, -29)
    names = ['1-1_par_prs30deg', '1-2_per_prs30deg', '1-3_45de_prs30deg', '2-2_prs30deg', '5-1_par_prs30deg', '5-2_per_prs30deg', '5-3_45de_prs30deg',
    '6-1_prs30deg']
    x = [                 14000,               4900,               -6000,         -14200,               9700,               1000,               -6000,
            -14400]
    y = [                 -6000,              -6000,               -6200,          -5500,               7000,               7000,                7000,
              7500]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(52, 52, 1)

    for name, xs, ys in zip(names, x, y):
        xss = np.linspace(xs-200, xs-200, 1)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 250, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            yield from bps.mv(energy, 2500)
            name_fmt = 'nexafs_intcor_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.sleep(0.5)
                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


    #prs 60 deg
    yield from bps.mv(prs, -59)
    names = ['1-1_par_prs60deg', '1-2_per_prs60deg', '1-3_45de_prs60deg', '2-2_prs60deg', '5-1_par_prs60deg', '5-2_per_prs60deg', '5-3_45de_prs60deg',
    '6-1_prs60deg']
    x = [                 15200,               6400,               -3600,         -11900,              11200,               3200,               -3800,
            -12400]
    y = [                 -6000,              -6000,               -6200,          -5500,               7000,               7000,                7000,
              7500]

    
    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(52, 52, 1)

    for name, xs, ys in zip(names, x, y):
        xss = np.linspace(xs-200, xs-200, 1)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 250, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            yield from bps.mv(energy, 2500)
            name_fmt = 'nexafs_intcor_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.sleep(0.5)
                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)

    yield from bps.mv(prs, 1)


def waxs_S_edge_chris_2021_3(t=1):
    dets = [pil900KW, pil1M]

    # names = ['A2_01', 'A2_02', 'A2_03', 'A2_04', 'A2_05', 'A2_06', 'A2_07', 'A2_08', 'A2_09', 'A2_10', 'A2_11', 'A2_12', 'A2_13', 'A2_14', 
    # 'A2_15', 'B2_01', 'B2_02', 'B2_03', 'B2_04', 'B2_05', 'B2_06', 'B2_07', 'B2_08', 'B2_09', 'B2_10', 'B2_11', 'B2_12', 'C2_01', 'C2_02',
    # 'C2_03', 'C2_04', 'C2_05', 'C2_06', 'C2_07']
    # x = [      44000,   38500,   33000,   27500,   21500,   16200,   10700,    5000,    -500,   -6000,  -11500,  -16500,  -21700,  -27000, 
    #  -32500,  -37500,  -43000,   45000,   39800,   34200,   29200,   24000,   18800,   13600,    8300,    2800,   -2400,   -7800,  -12900, 
    #  -18000,  -23600,  -28600,  -33700,  -38800]
    # y = [      -7800,   -7700,   -7650,   -7700,   -7700,   -7700,   -7500,   -7200,   -7200,   -7200,   -7200,   -7400,   -7500,   -7300,
    #   -7200,   -7250,   -6900,    5400,    5400,    5500,    5400,    5300,    5300,    5200,    5350,    5500,    5500,    5600,    5700,
    #    5800,    5550,    5700,    5300,    5500]

    # names = ['C2_08', 'C2_09', 'C2_10', 'C2_11', 'D2_01', 'D2_02', 'D2_03', 'D2_04', 'D2_05', 'D2_06', 'D2_07', 'D2_08', 'D2_09']
    # x = [      35000,   29000,   24000,   18300,   13000,    7500,    2000,  -10500,  -15800,  -21800,  -27500,  -32700,  -38700]
    # y = [      -8200,   -8200,   -8200,   -8300,   -8200,   -8550,   -8500,   -8300,   -8300,   -8250,   -8000,   -7850,   -7700]

    names = ['D2_03', 'D2_04', 'D2_05', 'D2_06', 'D2_07', 'D2_08', 'D2_09']
    x = [       2000,  -10500,  -15800,  -21800,  -27500,  -32700,  -38700]
    y = [      -8500,   -8300,   -8300,   -8250,   -8000,   -7850,   -7700]


    assert len(x) == len(y), f'Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})'
    assert len(x) == len(names), f'Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})'

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist() + np.arange(2490, 2500, 5).tolist() + np.arange(2500, 2560, 10).tolist()
    waxs_arc = [0, 20, 40]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1400, 63)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t)

            name_fmt = '{sample}_sdd7.0m_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                if energy.energy.position - e > 5:
                    yield from bps.mv(energy, e-5)
                    yield from bps.sleep(2) 
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2) 
                elif energy.energy.position - e > 2:
                    yield from bps.sleep(5)
                else:
                    yield from bps.sleep(2) 


                if xbpm2.sumX.get() < 120:
                    yield from bps.sleep(5)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(3)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)       
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)



def waxs_Cl_edge_chris_2021_3(t=1):
    dets = [pil900KW, pil1M]

    names = ['B2_01', 'B2_02', 'B2_03', 'B2_04', 'B2_05', 'B2_06', 'B2_07', 'B2_08', 'B2_09', 'B2_10', 'B2_11', 'B2_12']
    x = [     -37000,  -42500,   45600,   40400,   34900,   29800,   24600,   19600,   14200,    8900,    3400,   -1800]
    y = [      -7250,   -6900,    5400,    5400,    5500,    5400,    5300,    5250,    5200,    5300,    5400,    5500]

    assert len(x) == len(y), f'Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})'
    assert len(x) == len(names), f'Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})'

    energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 5).tolist() + np.arange(2850, 2910, 10).tolist()

    waxs_arc = [0, 20, 40]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1500, 65)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t,t)

            name_fmt = '{sample}_sdd7.0m_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                if xbpm2.sumX.get() < 120:
                    yield from bps.sleep(5)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2880)
            yield from bps.sleep(3)       
            yield from bps.mv(energy, 2850)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2810)
            yield from bps.sleep(3)


def giwaxs_S_edge_2021_3(t=1):
    dets = [pil900KW]
    
    # names = ['A1_01', 'A1_02', 'A1_03', 'A1_04', 'A1_05', 'A1_06', 'A1_07', 'A1_08', 'A1_09']
    # x_piezo = [59000,   57000,   40000,   24000,    7000,  -10000,  -27000,  -44000,  -48000]
    # x_hexa = [    15,       0,       0,       0,       0,       0,       0,       0,     -13]
    # y_piezo = [ 5900,    5900,    5900,    5900,    5900,    5900,    5900,    5900,    5900]

    names = ['A1_10', 'A1_11', 'A1_12', 'A1_13', 'A1_14', 'A1_15']
    x_piezo = [59000,   57000,   42000,   25000,    8000,  -10000]
    x_hexa = [    16,       0,       0,       0,       0,       0]
    y_piezo = [ 5900,    5900,    5900,    5900,    5900,    5900]



    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist() + np.arange(2490, 2500, 5).tolist() + np.arange(2500, 2560, 10).tolist()
    waxs_arc = [0, 20, 40]
    ai0 = 0

    assert len(x_piezo) == len(x_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})'
    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'

    for name, xs_piezo, xs_hexa, ys_piezo in zip(names, x_piezo, x_hexa, y_piezo):
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.y, ys_piezo)

        yield from bps.mv(piezo.th, ai0)

        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)        
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)

        yield from alignement_gisaxs(angle = 0.4)
        
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        yield from bps.mv(piezo.th, ai0 + 0.7)
        xss = np.linspace(xs_piezo, xs_piezo - 8000, 63)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_ai0.7_wa{wax}_bpm{xbpm}'
            for k, (e, xsss) in enumerate(zip(energies, xss)): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 120:
                    yield from bps.sleep(5)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.get()

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2510)
            yield from bps.sleep(2)       
            yield from bps.mv(energy, 2490)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)


def giwaxs_S_edge_2021_3_doblestack(t=1):
    dets = [pil900KW]
    
    # names = ['A1_01', 'A1_02', 'A1_03', 'A1_04', 'A1_05', 'A1_06', 'A1_07', 'A1_08', 'A1_09']
    # x_piezo = [59000,   57000,   40000,   24000,    7000,  -10000,  -27000,  -44000,  -48000]
    # x_hexa = [    15,       0,       0,       0,       0,       0,       0,       0,     -13]
    # y_piezo = [ 5900,    5900,    5900,    5900,    5900,    5900,    5900,    5900,    5900]

    names = ['B1_11', 'B1_12', 'C1_01', 'C1_02', 'C1_03', 'C1_04', 'C1_05', 'C1_06', 'C1_07', 'C1_08', 'C1_09', 'C1_10', 'C1_11', 'D1_01', 
    'D1_02', 'D1_03', 'D1_04', 'D1_05']
    x_piezo = [59000,   54000,   38000,   20000,    6000,   -8000,  -24000,  -40000,  -46000,   59000,   54000,   38000,   22000,    6000,
      -8000,  -25000,  -41000,  -46000]
    x_hexa = [     9,       0,       0,       0,       0,       0,       0,       0,       0,      11,       0,       0,       0,       0,
          0,       0,       0,     -11]
    y_piezo = [ 5900,    5900,    5900,    5900,    5900,    5900,    5900,    5900,    5900,   -2700,   -2700,   -2700,   -2700,   -2700,
      -2700,   -2700,   -2700,   -2700]
    z_piezo = [-2500,   -2500,   -2500,   -2500,   -2500,   -2500,   -2500,   -2500,   -2500,    5000,    5000,    5000,    5000,    5000,
       5000,    5000,    5000,    5000]


    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist() + np.arange(2490, 2500, 5).tolist() + np.arange(2500, 2560, 10).tolist()
    waxs_arc = [0, 20]
    ai0 = 0

    assert len(x_piezo) == len(x_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})'
    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'

    for name, xs_piezo, xs_hexa, ys_piezo, zs_piezo in zip(names, x_piezo, x_hexa, y_piezo, z_piezo):
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.y, ys_piezo)
        yield from bps.mv(piezo.z, zs_piezo)

        yield from bps.mv(piezo.th, ai0)

        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)        
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)

        yield from alignement_gisaxs_test(angle = 0.7)
        
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        yield from bps.mv(piezo.th, ai0 + 0.7)
        xss = np.linspace(xs_piezo, xs_piezo - 8000, 63)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_ai0.7_wa{wax}_bpm{xbpm}'
            for k, (e, xsss) in enumerate(zip(energies, xss)): 
                if energy.energy.position - e > 5:
                    yield from bps.mv(energy, e-5)
                    yield from bps.sleep(2) 
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2) 
                else:
                    yield from bps.sleep(2)

                if xbpm2.sumX.get() < 120:
                    yield from bps.sleep(5)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)


                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.get()

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2510)
            yield from bps.sleep(2)       
            yield from bps.mv(energy, 2490)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)

