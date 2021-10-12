def waxs_S_edge_guil(t=1):
    dets = [pil300KW]
    

    names = ['sample02', 'sample03', 'sample04', 'sample05', 'sample06', 'sample07', 'sample08', 'sample09', 'sample10', 'sample11', 'sample12']
    x = [26500, 21500, 16000, 10500, 5000, 0, -5500, -10500, 16000, -21000, -26500]#, -34000, -41000]
    y = [600, 600, 800, 700, 700, 600, 600, 600, 600, 900, 900]#, 700, 800]

    
    energies = np.linspace(2450, 2500, 26)
    waxs_arc = [0, 6.5, 13]
    
    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        
        yss = np.linspace(ys, ys + 1300, 26)
        
        if int(waxs.arc.position) == 0:
                waxs_arc = [0, 6.5, 13]
        elif int(waxs.arc.position) == 13:
                waxs_arc = [13, 6.5, 0]
        
        if name == 'sample02':
            waxs_arc = [6.5, 0]
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}'
            for e, ysss in zip(energies, yss): 
                yield from bps.sleep(1)
                yield from bps.mv(energy, e)
                yield from bps.mv(piezo.y, ysss)
                sample_name = name_fmt.format(sample=name, energy=e, wax = wa)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

       
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


    

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



def waxs_Se_edge_chris_2ndrun(t=1):
    
    det_exposure_time(t,t) 

    names = ['J2_01_01','J2_01_02','J2_01_03','J2_01_04','J2_02_01','J2_02_02','J2_02_03','J2_02_04','J2_03_01','J2_03_02','J2_03_03',
    'J2_03_04','J2_04_01','J2_04_02','J2_04_03','J2_04_04', 'vacuum']
    x = [      44300,   38400,   32800,  27400, 22500, 17200, 11600, 6300, 900, -4000, -8800, -14300, -19500, -24900, -30200, -35200, -56000]
    y = [        500,     700,     600,    600,   600,   600,   600,  900, 900,   900,   900,    900,    900,    900,    700,    900,    900]

    energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12716, 5).tolist()
    waxs_arc = np.linspace(0, 0, 1)

    dets = [pil300KW]

    yield from bps.mv(energy, 12620)
    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs + 200)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 64)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(0.5,0.5) 
            name_fmt = '{sample}_samespot_{energy}eV_wa{wax}_bpm{xbpm}'

            for e, xsss, ysss in zip(energies, xss, yss): 
                # yield from bps.mv(energy, e)
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


    dets = [pil300KW, pil1M]
    energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12716, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 64)
        xss = np.array([xs])

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



def giwaxs_S_edge_chris(t=1):
    dets = [pil300KW]
    
    names = ['F1_01', 'F1_02', 'F1_03', 'F1_04', 'G1_01', 'G1_02', 'G1_03']
    x = [51000, 36000, 21000, 5000, -11000, -26000, -41000]

    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)
    ai0 = 0

    for name, xs in zip(names, x):
        yield from bps.mv(piezo.x, xs)
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

        xss = np.linspace(xs, xs - 8000, 57)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                try: 
                    yield from bps.mv(energy, e)
                except:
                    print('energy failed to move, sleep for 30 s')
                    yield from bps.sleep(30)
                    print('Slept for 30 s, try move energy again')
                    yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

       
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def giwaxs_S_edge_chris_redo(t=1):
    dets = [pil300KW]
    

    names = ['a1_02_redo']#, 'sample03', 'sample04', 'sample05', 'sample06', 'sample07', 'sample08', 'sample09', 'sample10', 'sample11', 'sample12']
    x = [38000,-6000,-16000, -26000, -38000]#, 21500, 16000, 10500, 5000, 0, -5500, -10500, 16000, -21000, -26500]#, -34000, -41000]
    #y = [600]#, 600, 800, 700, 700, 600, 600, 600, 600, 900, 900]#, 700, 800]
    energiess = [[2495, 2500], [2495], [2455, 2470, 2495, 2500], [2488, 2490, 2495, 2500], [2495, 2500]]

    
    waxs_arc = np.linspace(0, 39, 7)
    ai0 = 0

    for name, xs, energies in zip(names, x, energiess):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.th, ai0)
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)        
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)

        yield from alignement_gisaxs(angle = 0.4)
        
        yield from bps.mv(att2_9, 'Insert')
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)
        yield from bps.mv(att2_9, 'Insert')
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        yield from bps.mv(piezo.th, ai0 + 0.7)
        
        '''
        if int(waxs.arc.position) == 0:
                waxs_arc = [0, 6.5, 13]
        elif int(waxs.arc.position) == 13:
                waxs_arc = [13, 6.5, 0]
        '''
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            yield from bps.mvr(piezo.x, -500)
    
            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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


    

def waxs_S_edge_chris_n(t=1):
    
    dets = [pil300KW]
    

    names = ['F2_01', 'F2_02', 'F2_03', 'F2_04', 'G2_01', 'G2_02', 'G2_03']
    x = [42000, 35800, 29100, 23000, 17000, 10500, 3500]
    y = [-3000, -2800, -3000, -3100, -2500, -3000, -2800]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 29)
        xss = np.array([xs, xs + 500])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                try: 
                    yield from bps.mv(energy, e)
                except:
                    print('energy failed to move, sleep for 30 s')
                    yield from bps.sleep(30)
                    print('Slept for 30 s, try move energy again')
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

    

def giwaxs_S_edge_2021_1(t=1):
    #sample alignement
    global names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, xs_hexa
    names = ['M1_01', 'M1_02', 'M1_03', 'M1_04', 'M1_05', 'M1_06', 'T1_01', 'T1_02', 'T1_03', 'T1_04', 'T1_05']
    x_piezo = [59000, 48000, 28000, 12000, -4000, -22000, -40000, -48000, 59000, 44000, 24000]
    y_piezo = [-4100, -4100, -4100, -4100, -4100,  -4100,  -4100,  -4100,  4800,  4800, 4800]
    z_piezo = [ 2700,  3700,  3700,  3700,  3700,   3700,   4500,   3700,   100,   100,  100]
    x_hexa =  [    6,     0,     0,     0,     0,      0,      0,     -8,     2,     0,    0]

    incident_angles = [-0.391445, -0.421654,    -0.334, -0.294984,  -0.289,  -0.53524, -0.421115, -0.436745, 0.17461, 0.109098, 0.264193]
    y_piezo_aligned = [-3947.954, -3864.194, -3870.767, -3847.222, -3874.9, -3793.295, -3737.792, -3693.625, 4853.88, 4890.095, 4947.866]

    # smi = SMI_Beamline()
    # yield from smi.modeAlignment(technique='gisaxs')

    # for name, xs_piezo, zs_piezo, ys_piezo, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
    #     yield from bps.mv(stage.x, xs_hexa)
    #     yield from bps.mv(piezo.x, xs_piezo)
    #     yield from bps.mv(piezo.y, ys_piezo)
    #     yield from bps.mv(piezo.z, zs_piezo)

    #     yield from alignement_gisaxs_multisample(angle = 0.45)

    #     incident_angles = incident_angles + [piezo.th.position]
    #     y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    # yield from smi.modeMeasurement()

    # print(incident_angles)
    # print(y_piezo_aligned)

    # yield from bps.mv(GV7.close_cmd, 1 )
    # yield from bps.sleep(1)
    # yield from bps.mv(GV7.close_cmd, 1 )
    # yield from bps.sleep(1)
    

    dets = [pil300KW]
    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)
    ai_list = [0.7]

    for name, xs, zs, aiss, ys, xs_hexa in zip(names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, aiss + ai_list[0])

        xss = np.linspace(xs, xs - 8000, 57)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
       
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def giwaxs_S_edge_2020_3(t=1):
    dets = [pil300KW]
    
    names = ['L1_03_par', 'L1_03_per']
    x = [-41000, -23000]

    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)
    ai0 = 0

    for name, xs in zip(names, x):
        yield from bps.mv(piezo.x, xs)
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

        xss = np.linspace(xs, xs - 8000, 57)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
       
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def waxs_S_edge_chris_2020_3(t=1):
    dets = [pil300KW]

    # names = [e'L2_01_01per', 'L2_01_02-45dg', 'L2_01_03par', 'L2_01_04-45deg', 'R2_01_01', 'R2_01_02', 'R2_02_01', 'R2_02_02', 'R2_03_01', 'R2_03_02',]
    # x = [29800, 22800, 15400,  8800, -17200, -23400, -29300, -34700, -40200, 39200]
    # y = [-5660, -5460, -5600, -5600,  -5600,  -5300,  -5300,  -5600,  -5500,  7000]
    # names = ['X1_03_per']
    # x = [-1500]
    # y = [-116]
    names = ['X1_03_par_redo3_pos1']
    x = [1600]
    y = [1335]
    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 0, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 150, 15)
        xss = np.linspace(xs, xs + 200, 4)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_sdd260.6_{energy}eV_wa{wax}_bpm{xbpm}'
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



def waxs_S_edge_chris_2021_1(t=1):
    dets = [pil300KW]

    names = ['M2_01', 'M2_02', 'M2_03', 'M2_04', 'M2_05', 'M2_06']
    x =     [  22500,   17000,   11200,     200,   -5100,  -10700]
    y =     [   7000,    7200,    7100,    6800,    6800,    6800]
    
    names = ['M2_06']
    x =     [-10700]
    y =     [ 6800]

    # waxs_arc = np.linspace(0, 0, 1)
    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()

    # for name, xs, ys in zip(names, x, y):
    #     yield from bps.mv(piezo.x, xs)
    #     yield from bps.mv(piezo.y, ys)

    #     yss = np.linspace(ys, ys + 1000, 31)
    #     xss = np.array([xs, xs + 500])

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)    

    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_thvar_2445.00eV_wa{wax}_bpm{xbpm}'
    #         for e, xsss, ysss in zip(energies, xss, yss): 
    #             yield from bps.sleep(1)

    #             yield from bps.mv(piezo.y, ysss)
    #             yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%1.3f'%bpm)
    #             sample_id(user_name='CM', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)


    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)
    # waxs_arc = np.linspace(39, 39, 1)

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



from epics import caput



def nexafs_oriented_S_edge(t=1):
    
    dets = [pil300KW]
        
    #prs 0 deg
    # names = ['1-1_par_prs0deg', '1-2_per_prs0deg', '1-3_45de_prs0deg', '2-2_prs0deg', '5-1_par_prs0deg', '5-2_per_prs0deg', '5-3_45de_prs0deg',
    # '6-1_prs0deg']
    # x = [                13300,              4600,              -6600,        -15000,              9000,               700,              -7300,
    #        -15500]
    # y = [                -6000,             -5800,              -6200,         -5500,              7000,              6700,              6700,
    #          7500]

    #prs 30 deg
    # names = ['1-1_par_prs30deg', '1-2_per_prs30deg', '1-3_45de_prs30deg', '2-2_prs30deg', '5-1_par_prs30deg', '5-2_per_prs30deg', '5-3_45de_prs30deg',
    # '6-1_prs30deg']
    # x = [                 14000,               4900,               -6000,         -14200,               9700,               1000,               -6000,
    #         -14400]
    # y = [                 -6000,              -6000,               -6200,          -5500,               7000,               7000,                7000,
    #           7500]

    #prs 60 deg
    names = ['1-1_par_prs60deg', '1-2_per_prs60deg', '1-3_45de_prs60deg', '2-2_prs60deg', '5-1_par_prs60deg', '5-2_per_prs60deg', '5-3_45de_prs60deg',
    '6-1_prs60deg']
    x = [                 15200,               6400,               -3600,         -11900,              11200,               3200,               -3800,
            -12400]
    y = [                 -6000,              -6000,               -6200,          -5500,               7000,               7000,                7000,
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

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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


    
def waxs_S_edge_chris_night(t=1):
    dets = [pil300KW]
    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)

    yield from bps.mv(stage.th, 0)
    yield from bps.mv(stage.y, 0)

    names = ['e2_01', 'e2_02', 'e2_03', 'e2_04', 'b2_04', 'b2_08', 'd2_01', 'd2_02', 'd2_03', 
    'd2_04', 'd2_05', 'd2_06', 'd2_07', 'd2_08']
    x = [41600, 35800, 29400, 23500, 6500, 1200, -4500, -9800,-15200,-21000,-26700,-32000,-37200,-42800,]
    y = [-4300, -4300, -4100, -4000, -4200,-4200, -4300, -4200, -4200, -4300, -4300, -4200, -4100, -4300, ]
    

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 29)
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
    names = ['d2_10', 'd2_11']
    x = [-15700, -10200]
    y = [-8800, -8800]


    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 29)
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


    yield from bps.mv(energy, 2450)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2500)
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
    


    dets = [pil300KW]

    yield from bps.mv(stage.th, 0)
    yield from bps.mv(stage.y, 0)
    names = ['b2_01', 'b2_02', 'b2_04', 'b2_08']
    x = [17800, 12200, 6750, 1450]
    y = [-4100, -4200,-4200,-4200]

    
    energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist()
    waxs_arc = np.linspace(0, 39, 7)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 29)
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
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2830)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2810)
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



def giwaxs_S_edge_2021_2(t=1):
    dets = [pil300KW]
    
    names = ['3-1_hor_par', '3-2_hor_per', '4-1_hor']
    x = [35000, 16000, -11000]

    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)
    ai0 = 0

    for name, xs in zip(names, x):
        yield from bps.mv(piezo.x, xs)
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
        yield from bps.mv(piezo.th, ai0 + 1.5)

        xss = np.linspace(xs, xs - 8000, 57)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_pos{pos}_ai1.5_wa{wax}_bpm{xbpm}'
            for k, (e, xsss) in enumerate(zip(energies, xss)): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, pos = '%2.2d'%k, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
       
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)

        
        yield from bps.mv(piezo.x, xs)
        name_fmt = '{sample}_{energy}eV_pos{pos}_ai1.5_wa{wax}_bpm{xbpm}'
        for k, (e, xsss) in enumerate(zip(energies, xss)): 
                # yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy=2450, pos = '%2.2d'%k, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


def waxs_S_edge_chris_night_2021_1(t=1):
    # proposal_id('2021_1', '307822_McNeil6')

    # dets = [pil300KW]
    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    # waxs_arc = np.linspace(0, 39, 7)

    # names = ['CL2_01_01', 'CL2_01_02', 'CL2_02_01', 'CL2_02_02', 'CL2_03_01', 'CL2_03_02', 'CL2_04_01', 'CL2_04_02']
    # x = [          42100,       36900,       31800,       26500,       10200,        4600,      -12300,      -17800]
    # y = [            700,         900,         700,         900,         700,         600,         400,         700]
    
    # for name, xs, ys in zip(names, x, y):
    #     yield from bps.mv(piezo.x, xs)
    #     yield from bps.mv(piezo.y, ys)

    #     yss = np.linspace(ys, ys + 1000, 29)
    #     xss = np.array([xs, xs + 500])

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)    

    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
    #         for e, xsss, ysss in zip(energies, xss, yss): 
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(1)

    #             yield from bps.mv(piezo.y, ysss)
    #             yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
    #             sample_id(user_name='GF', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)

    #         yield from bps.mv(energy, 2470)
    #         yield from bps.mv(energy, 2450)

    # yield from transition_S_Cl_edges()
    
    proposal_id('2021_1', '307822_McNeil7')

    dets = [pil300KW]

    # names = ['CL2_01_01', 'CL2_01_02', 'CL2_02_03', 'CL2_02_04', 'CL2_03_03', 'CL2_03_04', 'CL2_04_03', 'CL2_04_04']
    # x = [          42900,       37700,       21300,       15500,        -900,       -6700,      -23600,      -29100]
    # y = [            700,         900,         700,         700,         500,         300,         900,         800]

    names = [ 'CL2_03_03', 'CL2_03_04', 'CL2_04_03', 'CL2_04_04']
    x = [            -900,       -6700,      -23600,      -29100]
    y = [             500,         300,         900,         800]

    energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist()
    waxs_arc = np.linspace(0, 39, 7)

    for i, (name, xs, ys) in enumerate(zip(names, x, y)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 29)
        xss = np.array([xs, xs + 500])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        if i ==0:
            waxs_arc = np.linspace(19.5, 39, 4)
        else:
            waxs_arc = np.linspace(0, 39, 7)

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

            yield from bps.mv(energy, 2830)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2810)
            yield from bps.sleep(2)



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



def giwaxs_S_edge_2021_1_night(t=1):
    proposal_id('2021_1', '307822_McNeil8')

    names = ['CL1_01_01', 'CL1_02_01', 'CL1_03_01', 'CL1_04_01']
    x_piezo = [    59000,       57000,       40500,       23500]
    x_hexa = [        12,           0,           0,           0]
    y_piezo = [     6900,        6900,        6900,        6900]

    dets = [pil300KW]
    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)
    ai0 = 0

    for name, xs_piezo, xs_hexa, ys_piezo  in zip(names, x_piezo, x_hexa, y_piezo):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
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


        xss = np.linspace(xs_piezo, xs_piezo - 5500, 57)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
       
            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)


    yield from transition_S_Cl_edges()
    proposal_id('2021_1', '307822_McNeil9')

    names = ['CL1_02_02', 'CL1_03_02', 'CL1_04_02']
    x_piezo = [    52000,       35000,       18000]
    x_hexa = [         0,           0,           0]
    y_piezo = [     6900,        6900,        6900]


    dets = [pil300KW]
    energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist()
    waxs_arc = np.linspace(0, 39, 7)
    ai0 = 0

    for name, xs_piezo, xs_hexa, ys_piezo  in zip(names, x_piezo, x_hexa, y_piezo):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
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


        xss = np.linspace(xs_piezo, xs_piezo - 5500, 57)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
       
            yield from bps.mv(energy, 2830)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2810)
            yield from bps.sleep(2)

    yield from transition_Cl_S_edges()






def giwaxs_S_edge_2021_1_night2(t=1):
    proposal_id('2021_1', '307822_McNeil11')

    names = ['GG1_03_01', 'GG1_03_02', 'GG1_03_03', 'GG1_04_01', 'GG1_04_02', 'GG1_04_03']
    x_piezo = [    58000,       52500,       35000,       17000,           0,      -15000]
    x_hexa = [        11,           0,           0,           0,           0,           0]
    y_piezo = [     6900,        6900,        6900,        6900,        6900,        6900]


    dets = [pil300KW]
    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)
    ai0 = 0

    aiss = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0,
            0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0] 


    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(x_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})'
    assert len(x_piezo) == int(len(aiss)/3), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(aiss)})'


    for i, (name, xs_piezo, xs_hexa, ys_piezo)  in enumerate(zip(names, x_piezo, x_hexa, y_piezo)):
        if 'GG1_04' in name:
            waxs_arc = np.linspace(0, 32.5, 6)
        else:
            waxs_arc = np.linspace(0, 26, 5)

        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
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

        for wa in waxs_arc:
            num = i * 3

            yield from bps.mv(waxs, wa)    

            yield from bps.mv(piezo.th, ai0 + aiss[num])
            xss = np.linspace(xs_piezo, xs_piezo - 3500, 57)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{ai}deg_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, ai='%1.1f'%aiss[num], energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)


            yield from bps.mv(piezo.th, ai0 + aiss[num+1])
            xss = np.linspace(xs_piezo- 3600, xs_piezo - 7100, 57)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{ai}deg_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, ai='%1.1f'%aiss[num+1], energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)

            yield from bps.mv(piezo.th, ai0 + aiss[num+2])
            xss = np.linspace(xs_piezo - 7200, xs_piezo - 11000, 57)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{ai}deg_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, ai='%1.1f'%aiss[num+2], energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)


    names = ['GG1_03_01', 'GG1_04_01', 'GG1_01_01', 'GG1_02_01']
    x_piezo = [    58000,       17000,      -30500,      -47000]
    x_hexa = [        11,           0,           0,         -13]
    y_piezo = [     6900,        6900,        6900,        6900]


    dets = [pil300KW]
    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)
    ai0 = 0

    aiss = [6.0, 6.0, 6.0, 6.0] 
    num=0
    for i, (name, xs_piezo, xs_hexa, ys_piezo)  in enumerate(zip(names, x_piezo, x_hexa, y_piezo)):
        if 'GG1_04' in name:
            waxs_arc = np.linspace(0, 32.5, 6)
        else:
            waxs_arc = np.linspace(0, 26, 5)

        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
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

        for wa in waxs_arc:
            num = i

            yield from bps.mv(waxs, wa)    

            yield from bps.mv(piezo.th, ai0 + aiss[num])
            xss = np.linspace(xs_piezo, xs_piezo - 3500, 57)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{ai}deg_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss in zip(energies, xss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.x, xsss)
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, ai='%1.1f'%aiss[num], energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)





def nexafs_oriented_S_edge_allprs(t=1):
    dets = [pil300KW]    
    #prs 0 deg
    yield from bps.mv(prs, 1)
    # names = ['1-1_par_prs0deg', '1-2_per_prs0deg', '1-3_45de_prs0deg', '2-2_prs0deg', '5-1_par_prs0deg', '5-2_per_prs0deg', '5-3_45de_prs0deg',
    # '6-1_prs0deg']
    # x = [                13300,              4600,              -6600,        -15000,              9000,               700,              -7300,
    #        -15500]
    # y = [                -6000,             -5800,              -6200,         -5500,              7000,              6700,              6700,
    #          7500]

    names = ['1-1_par_prs0deg', '1-2_per_prs0deg', '1-3_45de_prs0deg', '5-1_par_prs0deg', '5-2_per_prs0deg', '5-3_45de_prs0deg']
    x = [                13600,              4900,              -6300,              9300,              1300,              -6400]
    y = [                -5900,             -5900,              -6600,              6800,              6700,               7000]

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

        x_loc = [-300, -300, 0, 0, 300, 300]
        y_loc = [0, 500, 0, 500, 0, 500]

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_pos1_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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
                yield from bp.rel_list_scan(dets, piezo.x, x_loc, piezo.y, y_loc)

            
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)





def nexafs_oriented_S_edge_allprs_2021_3(t=1):
    dets = [pil900KW]    
    # yield from bps.mv(prs, 0)

    # names = ['Cl2_02_prs0deg', 'Cl2_03_prs0deg']
    # x = [                13700,              5100]
    # y = [                -5500,             -5500]

    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    # waxs_arc = np.linspace(50, 50, 1)

    # for name, xs, ys in zip(names, x, y):
    #     yield from bps.mv(piezo.x, xs)
    #     yield from bps.mv(piezo.y, ys)

    #     yss = np.linspace(ys, ys + 800, 58)
    #     xss = np.linspace(xs, xs, 1)

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)    

    #         det_exposure_time(t,t) 
    #         name_fmt = 'nexafs_pos1_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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
    #         yield from bps.mv(energy, 2450)

    yield from bps.mv(prs, -30)

    # names = ['Cl2_02_prs30deg', 'Cl2_03_prs30deg']
    # x = [                15300,              6400]
    # y = [                -5500,             -5500]

    names = [ 'Cl2_03_prs30deg']
    x = [               5000]
    y = [              -5500]
    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(52, 52, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 800, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_pos1_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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
            yield from bps.mv(energy, 2450)

    # yield from bps.mv(prs, -60)

    # names = ['Cl2_02_prs60deg', 'Cl2_03_prs60deg']
    # x = [                16200,              6200]
    # y = [                -5500,             -5500]


    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    # waxs_arc = np.linspace(52, 52, 1)

    # for name, xs, ys in zip(names, x, y):
    #     yield from bps.mv(piezo.x, xs)
    #     yield from bps.mv(piezo.y, ys)

    #     yss = np.linspace(ys, ys + 800, 58)
    #     xss = np.linspace(xs, xs, 1)

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)    

    #         det_exposure_time(t,t) 
    #         name_fmt = 'nexafs_pos1_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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
    #         yield from bps.mv(energy, 2450)
    




def nexafs_oriented_Cl_edge_allprs_2021_3(t=1):
    dets = [pil900KW]    
    yield from bps.mv(prs, 0)

    names = [ 'Cl2_03_prs0deg']
    x = [                 5100]
    y = [              -5500]

    energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist()
    waxs_arc = np.linspace(50, 50, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 800, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_pos1_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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
            
            yield from bps.mv(energy, 2830)
            yield from bps.mv(energy, 2800)

    yield from bps.mv(prs, -30)

    names = ['Cl2_02_prs30deg', 'Cl2_03_prs30deg']
    x = [                15300,              5000]
    y = [                -5500,             -5500]

    energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist()
    waxs_arc = np.linspace(52, 52, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 800, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_pos1_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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
            
            yield from bps.mv(energy, 2830)
            yield from bps.mv(energy, 2800)

    yield from bps.mv(prs, -60)

    names = ['Cl2_02_prs60deg', 'Cl2_03_prs60deg']
    x = [                16200,              6200]
    y = [                -5500,             -5500]


    energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist()
    waxs_arc = np.linspace(52, 52, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 800, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_pos1_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
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
            
            yield from bps.mv(energy, 2830)
            yield from bps.mv(energy, 2800)
    



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



def waxs_S_edge_chris_test_2021_2(t=1):
    dets = [pil1M]
    yield from bps.mv(prs, 1)

    yield from bps.mv(att2_9.close_cmd, 1)        
    yield from bps.sleep(1)        
    yield from bps.mv(att2_9.close_cmd, 1)        
    yield from bps.sleep(1)


    # names = ['1-1_par', '1-2_per', '1-3_45de',  '2-2', '5-1_par', '5-2_per', '5-3_45de']
    # x = [        13000,      4400,      -7000, -15500,      8500,       400,      -7500]
    # y = [        -4400,     -5800,      -6400,  -5700,      6400,      6500,       6900]
    # chi = [          3,   -0.23,      -0.23,  -0.23,     -0.23,      -0.23,       -0.23]

    # names = ['1-1_par_redo', '1-2_per', '1-3_45de',  '5-1_par', '5-2_per', '5-3_45de']
    # x = [        14500,      4600,      -6800,      10200,       850,      -7200]
    # y = [        -4400,     -5245,      -6000,       6500,      6680,       7280]
    # y_range = [    300,       300,        300,        300,       300,        300]
    # chi = [          3,         0,          0,          0,         0,          0]

    names = ['2-2_redo']
    x = [   -14900]
    y = [     -5700]
    y_range = [300]
    chi = [      0]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(13, 13, 1)

    for name, xs, ys, chis, y_ranges in zip(names, x, y, chi, y_range):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.ch, chis)

        yss = np.linspace(ys, ys + y_ranges, 62)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        # if 'per' in name:
        #     waxs_ar = [19.5, 13.0, 6.5, 0]
        # elif '5-3_45de' in name:
        #     waxs_ar = [10, 0, 6.5, 13, 19.5]
        # elif '1-3_45de' in name:
        #     waxs_ar = [13, 0, 6.5, 19.5]
        # else:
        #     waxs_ar = [0, 6.5, 13.0, 19.5]

        for l, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t)

            # if l==0:
            #     yield from bps.mv(energy, 2450)
            #     name_fmt = 'int_cor_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            #     for e, xsss, ysss in zip(energies, xss, yss): 
            #         yield from bps.sleep(0.5)

            #         yield from bps.mv(piezo.y, ysss)
            #         yield from bps.mv(piezo.x, xsss)

            #         bpm = xbpm2.sumX.value
            #         sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
            #         sample_id(user_name='GF', sample_name=sample_name)
            #         print(f'\n\t=== Sample: {sample_name} ===\n')

            #         yield from bp.count(dets, num=1)


            name_fmt = '{sample}_sdd1.6m_{energy}eV_wa{wax}_bpm{xbpm}'
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




def waxs_S_edge_chris_2021_2(t=1):
    dets = [pil300KW, pil1M]
    yield from bps.mv(prs, 1)

    yield from bps.mv(att2_9.close_cmd, 1)        
    yield from bps.sleep(1)        
    yield from bps.mv(att2_9.close_cmd, 1)        
    yield from bps.sleep(1)


    names = ['E2_01', 'E2_02', 'E2_03', 'E2_04',  'Cl2_01']
    x = [      41700,   36500,   30800,   24800,     19600]
    y = [      -6000,   -5700,   -5700,   -5700,     -5500]


    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 700, 31)
        xss = np.array([xs, xs + 500])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t)

            name_fmt = '{sample}_sdd4m_{energy}eV_wa{wax}_bpm{xbpm}'
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




def waxs_S_edge_chris_2021_2_lowrange(t=1):
    dets = [pil300KW]

    names = ['6-1']
    x = [   -15600]
    y = [     7500]
    
    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 0, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 400, 31)
        xss = np.array([xs, xs + 400])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t,t)

            if wa == 0:
                yield from bps.mv(energy, 2450)
                name_fmt = 'int_cor_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
                for e, xsss, ysss in zip(energies, xss, yss): 
                    yield from bps.sleep(0.5)

                    yield from bps.mv(piezo.y, ysss)
                    yield from bps.mv(piezo.x, xsss)

                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='GF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')

                    yield from bp.count(dets, num=1)


            # name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            # for e, xsss, ysss in zip(energies, xss, yss): 
            #     yield from bps.mv(energy, e)
            #     yield from bps.sleep(2)

            #     yield from bps.mv(piezo.y, ysss)
            #     yield from bps.mv(piezo.x, xsss)

            #     bpm = xbpm2.sumX.value

            #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
            #     sample_id(user_name='GF', sample_name=sample_name)
            #     print(f'\n\t=== Sample: {sample_name} ===\n')

            #     yield from bp.count(dets, num=1)

            # yield from bps.mv(energy, 2470)
            # yield from bps.mv(energy, 2450)


def night_maccro(t=0.5):
    proposal_id('2021_2', '307822_McNeil6')
    yield from waxs_S_edge_chris_test_2021_2(t=0.3)
    yield from bps.sleep(5)

    yield from waxs_S_edge_chris_2021_2(t = 0.5)
    yield from bps.sleep(5)

    proposal_id('2021_2', '307830_Su1')
    yield from waxs_S_edge_greg_2021_2(t=1)
    yield from bps.sleep(5)
