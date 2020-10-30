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

    names = ['D1_06']
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