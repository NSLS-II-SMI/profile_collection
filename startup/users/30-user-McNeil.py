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




def waxs_Se_edge_chris_2ndrun(t=1):
    
    dets = [pil300KW]
    det_exposure_time(t,t) 


    names = ['J1_01', 'J1_02', 'J1_03', 'J1_04', 'vacuum']
    x = [      36200,   30300,   24800,  18800, 14900]
    y = [       6000,    6000,    6300,   6000, 6000]

    energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12701, 5).tolist()
    waxs_arc = np.linspace(0, 0, 1)

    yield from bps.mv(energy, 12620)


    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 31)
        xss = np.array([xs, xs + 1300])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_thvar_12620.00eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                # yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%1.3f'%bpm)
                sample_id(user_name='CM', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


    names = ['J1_01', 'J1_02', 'J1_03', 'J1_04', 'vacuum']
    x = [      36200,   30300,   24800,  18800, 14900]
    y = [       6000,    6000,    6300,   6000, 6000]

    # names = ['vacuum']
    # x = [-1000]
    # y = [-1600]

    energies = np.arange(12620, 12640, 5).tolist() + np.arange(12640, 12660, 0.5).tolist() + np.arange(12660, 12670, 1).tolist() + np.arange(12670, 12701, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 31)
        xss = np.array([xs, xs + 1300])

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

            yield from bps.mv(energy, 12670)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12640)
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
    
    # #prs 0 deg
    # names = ['L2_01_01per', 'L2_01_02per', 'L2_01_03par', 'L2_01_04par', 'L2_02_01per', 'L2_02_02par', 'L2_02_03par']
    # x = [29800, 21800, 15400,  9600,  2100, -3900, -10600 ]
    # y = [-5660, -5600, -5600, -5860, -5560, -5360,  -5460]
    
    # #prs 30 deg
    # names = ['L2_01_01per', 'L2_01_02per', 'L2_01_03par', 'L2_01_04par', 'L2_02_01per', 'L2_02_02par', 'L2_02_03par']
    # x = [29500, 21300, 14900,  9200,  1500, -4500, -11400 ]
    # y = [-5660, -5600, -5600, -5860, -5560, -5360,  -5460]

    #prs 60 deg
    #Here there is a mistake. I skipped the samples L2_01_per and tehrefore all the samples names are shiffted
    # names = ['L2_01_02per', 'L2_01_03par', 'L2_01_04par', 'L2_02_01per', 'L2_02_02par', 'L2_02_03par']
    # x = [17100, 11300,  3700,  -2000, -8500, -15000 ]
    # y = [-5760, -5860, -5960, -5560, -5460,  -5560]

    # names = ['L2_01_02per_real','L2_02_01per_real']
    # x = [23100, 3700]
    # y = [-5660, -5660]

    # names = ['X1_03_par_30deg']
    # x = [31300]
    # y = [320] 
    names = ['X1_03_45deg_60deg']
    x = [6500]
    y = [-9150]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(52, 52, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        # yss = np.linspace(ys, ys + 200, 12)
        # xss = np.linspace(xs, xs + 1000, 5)

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

    names = ['L1_03_per']
    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()

    
    waxs_arc = [4, 10.5, 17]

    dets = [pil300KW]

    for name in names:
        for i, wa in enumerate(waxs_arc):
            if i==0:
                print('wa=4deg')
            else:
                yield from bps.mv(waxs, wa)   

            name_fmt = 'GIWAXS_90deg_{sample}_{energy}eV_ai0.7_wa{wax}_bpm{xbpm}'
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
    # proposal_id('2021_1', '307822_McNeil8')

    # names = ['CL1_01_01', 'CL1_02_01', 'CL1_03_01', 'CL1_04_01']
    # x_piezo = [    59000,       57000,       40500,       23500]
    # x_hexa = [        12,           0,           0,           0]
    # y_piezo = [     6900,        6900,        6900,        6900]

    # dets = [pil300KW]
    # energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    # waxs_arc = np.linspace(0, 39, 7)
    # ai0 = 0

    # for name, xs_piezo, xs_hexa, ys_piezo  in zip(names, x_piezo, x_hexa, y_piezo):
    #     yield from bps.mv(stage.x, xs_hexa)
    #     yield from bps.mv(piezo.x, xs_piezo)
    #     yield from bps.mv(piezo.y, ys_piezo)
    #     yield from bps.mv(piezo.th, ai0)


    #     yield from bps.mv(GV7.open_cmd, 1 )
    #     yield from bps.sleep(1)        
    #     yield from bps.mv(GV7.open_cmd, 1 )
    #     yield from bps.sleep(1)

    #     yield from alignement_gisaxs(angle = 0.4)
        
    #     yield from bps.mv(GV7.close_cmd, 1 )
    #     yield from bps.sleep(1)
    #     yield from bps.mv(GV7.close_cmd, 1 )
    #     yield from bps.sleep(1)

    #     ai0 = piezo.th.position
    #     yield from bps.mv(piezo.th, ai0 + 0.7)


    #     xss = np.linspace(xs_piezo, xs_piezo - 5500, 57)
    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)    

    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
    #         for e, xsss in zip(energies, xss): 
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(2)

    #             yield from bps.mv(piezo.x, xsss)
    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
    #             sample_id(user_name='GF', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)
       
    #         yield from bps.mv(energy, 2470)
    #         yield from bps.sleep(2)
    #         yield from bps.mv(energy, 2450)
    #         yield from bps.sleep(2)


    # yield from transition_S_Cl_edges()
    # proposal_id('2021_1', '307822_McNeil9')

    # names = ['CL1_02_02', 'CL1_03_02', 'CL1_04_02']
    # x_piezo = [    52000,       35000,       18000]
    # x_hexa = [         0,           0,           0]
    # y_piezo = [     6900,        6900,        6900]


    # dets = [pil300KW]
    # energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist()
    # waxs_arc = np.linspace(0, 39, 7)
    # ai0 = 0

    # for name, xs_piezo, xs_hexa, ys_piezo  in zip(names, x_piezo, x_hexa, y_piezo):
    #     yield from bps.mv(stage.x, xs_hexa)
    #     yield from bps.mv(piezo.x, xs_piezo)
    #     yield from bps.mv(piezo.y, ys_piezo)
    #     yield from bps.mv(piezo.th, ai0)


    #     yield from bps.mv(GV7.open_cmd, 1 )
    #     yield from bps.sleep(1)        
    #     yield from bps.mv(GV7.open_cmd, 1 )
    #     yield from bps.sleep(1)

    #     yield from alignement_gisaxs(angle = 0.4)
        
    #     yield from bps.mv(GV7.close_cmd, 1 )
    #     yield from bps.sleep(1)
    #     yield from bps.mv(GV7.close_cmd, 1 )
    #     yield from bps.sleep(1)

    #     ai0 = piezo.th.position
    #     yield from bps.mv(piezo.th, ai0 + 0.7)


    #     xss = np.linspace(xs_piezo, xs_piezo - 5500, 57)
    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)    

    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
    #         for e, xsss in zip(energies, xss): 
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(2)

    #             yield from bps.mv(piezo.x, xsss)
    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
    #             sample_id(user_name='GF', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)
       
    #         yield from bps.mv(energy, 2830)
    #         yield from bps.sleep(2)
    #         yield from bps.mv(energy, 2810)
    #         yield from bps.sleep(2)

    # yield from transition_Cl_S_edges()
    proposal_id('2021_1', '307822_McNeil10')


    names = ['GG1_01_01', 'GG1_01_02', 'GG1_01_03', 'GG1_02_01', 'GG1_02_02']
    x_piezo = [     7500,       -8000,      -23000,      -38000,      -45000]
    x_hexa = [         0,           0,           0,           0,          -8]
    y_piezo = [     6900,        6900,        6900,        6900,        6900]

    dets = [pil300KW]
    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)
    ai0 = 0

    aiss = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2.0, 3.0, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] 

    i = 0

    for i, (name, xs_piezo, xs_hexa, ys_piezo)  in enumerate(zip(names, x_piezo, x_hexa, y_piezo)):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)
        yield from bps.mv(piezo.th, ai0)

        if i!=0:
            yield from bps.mv(GV7.open_cmd, 1 )
            yield from bps.sleep(1)        
            yield from bps.mv(GV7.open_cmd, 1 )
            yield from bps.sleep(1)

            yield from alignement_gisaxs(angle = 0.4)
            
            yield from bps.mv(GV7.close_cmd, 1 )
            yield from bps.sleep(1)
            yield from bps.mv(GV7.close_cmd, 1 )
            yield from bps.sleep(1)


        else:
            waxs_arc = np.linspace(6.5, 26, 4)
            yield from bps.mv(piezo.th, 0.61229)


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

                sample_name = name_fmt.format(sample=name, ai='%1.1f'%aiss[i], energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
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

                sample_name = name_fmt.format(sample=name, ai='%1.1f'%aiss[i], energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
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

                sample_name = name_fmt.format(sample=name, ai='%1.1f'%aiss[i], energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)
            i = i +1
