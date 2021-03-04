
def new_folder(cycle, group):
    proposal_id(cycle, group)


def song_waxs_S_edge_new(t=1):
    dets = [pil300KW]

    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1 )

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 13, 3)

    yield from bps.mv(stage.th, 1)
    yield from bps.mv(stage.y, -8)
    names = ['C2C8C10_2_0per_2','C2C8C10_20per_2','C2C8C10_40per_2']
    x = [-29200, -34900, -40500]
    y = [-8470, -8620, -9240]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 620, 15)
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


def song_saxs_tensile_hard(t=1):
    dets = [pil1M]

    names = 'P3BT_loop2'

    t0 = time.time()
    for i in range(2000):

        det_exposure_time(t,t) 
        name_fmt = '{sample}_10_18250eV_sdd1p6_{time}_{i}'
        t1 = time.time()
        sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), i = '%3.3d'%i)
        sample_id(user_name='GF', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)

        time.sleep(20)


def song_saxs_waxs_tensile_hard(t=1):
    dets = [pil300KW, pil1M]

    names = 'P3BT_loop2'
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t,t) 

        if waxs.arc.position > 5:
            wa = [14, 7.5, 1]
        else:
            wa = [1, 7.5, 14]
        
        name_fmt = '{sample}_18250eV_{time}s_{i}_wa{wa}'
        t1 = time.time()
        for wax in wa:
            yield from bps.mv(waxs, wax)
            sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), i = '%3.3d'%i, wa = '%1.1f'%wax)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)




def wenkai_waxs_tensile_tender(t=1):
    dets = [pil300KW]

    names = 'Rxbai-P_S_loop1'
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t,t) 

        if waxs.arc.position > 5:
            wa = [19.5, 13, 6.5, 0]
        else:
            wa = [0, 6.5, 13, 19.5]
        
        t1 = time.time()
        for wax in wa:
                name_fmt = '{sample}_2476.2eV_{time}s_{i}_wa{wa}'

                yield from bps.mv(waxs, wax)
                sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), i = '%3.3d'%i, wa = '%1.1f'%wax)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


def song_saxs_waxs_tensile_tender(t=1):
    dets = [pil300KW]

    names = 'P3HT_loop1_S'
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t,t) 

        if waxs.arc.position > 5:
            wa = [19.5, 13, 6.5, 0]
        else:
            wa = [0, 6.5, 13, 19.5]
        
        t1 = time.time()
        for wax in wa:
            if energy.energy.position > 2475:
                ener = [2478, 2470]
            else:
                ener = [2470, 2478]

            for ene in ener:
                name_fmt = '{sample}_{energy}eV_{time}s_{i}_wa{wa}'
                yield from bps.mv(energy, ene)

                yield from bps.mv(waxs, wax)
                sample_name = name_fmt.format(sample=names, energy='%6.2f'%ene , time = '%1.1f'%(t1-t0), i = '%3.3d'%i, wa = '%1.1f'%wax)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


def wenkai_saxs_waxs_tensile_hard(t=1):
    dets = [pil300KW, pil1M]

    names = 'PF-T2PO1_loop1'
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t,t) 

        if waxs.arc.position > 5:
            wa = [13, 6.5, 0]
        else:
            wa = [0, 6.5, 13]
        
        name_fmt = '{sample}_14000eV_{time}s_{i}_wa{wa}'
        t1 = time.time()
        for wax in wa:
            yield from bps.mv(waxs, wax)
            sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), i = '%3.3d'%i, wa = '%1.1f'%wax)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)


def wenkai_saxs_waxs_tensile_hard1(t=1):
    dets = [pil300KW, pil1M]

    names = 'Rxbai_P_loop3'
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t,t) 

        if i == 0:
            wa = [1, 7.5, 14]

            name_fmt = '{sample}_18250eV_{time}s_{i}_wa{wa}'
            t1 = time.time()
            for wax in wa:
                yield from bps.mv(waxs, wax)
                sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), i = '%3.3d'%i, wa = '%1.1f'%wax)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
        t1 = time.time()
        
        if t1-t0 > 750 and t1-t0 < 1050:
            if waxs.arc.position > 5:
                wa = [14, 7.5, 1]
            else:
                wa = [1, 7.5, 14]

            name_fmt = '{sample}_18250eV_{time}s_{i}_wa{wa}'
            t1 = time.time()
            for wax in wa:
                yield from bps.mv(waxs, wax)
                sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), i = '%3.3d'%i, wa = '%1.1f'%wax)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
        else:
            wa = [1]
            name_fmt = '{sample}_18250eV_{time}s_{i}_wa{wa}'
            t1 = time.time()
            for wax in wa:
                yield from bps.mv(waxs, wax)
                sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), i = '%3.3d'%i, wa = '%1.1f'%wax)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
            
            time.sleep(25)
            



def song_saxs_waxs_tensile_hard1(t=1, names='test'):
    dets = [pil300KW, pil1M]

    det_exposure_time(t,t) 

    if waxs.arc.position > 5:
        wa = [14, 7.5, 1]
    else:
        wa = [1, 7.5, 14]
        
    name_fmt = '{sample}_18250eV_wa{wa}'
    for wax in wa:
        yield from bps.mv(waxs, wax)
        sample_name = name_fmt.format(sample=names, wa = '%2.1f'%wax)
        sample_id(user_name='GF', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)



def song_waxs_new(t=1):
    dets = [pil300KW, pil1M]

    # yield from bps.mv(GV7.close_cmd, 1 )
    # yield from bps.sleep(5)
    # yield from bps.mv(GV7.close_cmd, 1 )

    waxs_arc = np.linspace(0, 13, 3)
    del_y = [-100, 0, 100]

    # yield from bps.mv(stage.th, 1)
    # yield from bps.mv(stage.y, -8)
    names = ['C2C6C8_0per','C2C6C8_20per','C2C6C8_40per','C2C6C8_60per','C2C6C8_80per','C2C8C10_0per','C2C8C10_20per','C2C8C10_40per','C2C8C10_60per','C2C8C10_80per',
    'C2C8C10_100per','C2C10C12_0per','C2C10C12_20per','C2C10C12_40per','C2C10C12_60per','C2C10C12_80per','C2C10C12_100per']
    x = [43200, 38200, 33200, 27200, 21900, 16900, 11700, 6700, 1700, -3200, -9000,-14000,-19000,-24000,-29000,-34000,-40000]
    y = [-8500, -8500, -8500, -8500, -8300, -8500, -8500,-8500,-8700, -8300, -8800, -8500, -8500, -8500, -8500, -8700, -8800]

    names = ['bkg_vac']
    x = [-10500]
    y = [-3000]


    for wa, de_y in zip(waxs_arc, del_y):
        yield from bps.mv(waxs, wa)
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
           
            det_exposure_time(t,t) 
            name_fmt = '{sample}_10_16100eV_wa{wax}_bpm{xbpm}'

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%4.3f'%bpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    # yield from bps.mv(stage.y, 0)
    # yield from bps.mv(stage.th, 0)
    # names = ['C2C12C14_0per','C2C12C14_20per','C2C12C14_40per','C2C12C14_60per','C2C12C14_80per']
    # x = [44100, 4100, -100, -5100, -16100]
    # y = [-3000,-4000,-4000, -4000, -4000]

    # for wa, de_y in zip(waxs_arc, del_y):
    #     yield from bps.mv(waxs, wa)
    #     for name, xs, ys in zip(names, x, y):
    #         yield from bps.mv(piezo.x, xs)
    #         yield from bps.mv(piezo.y, ys+de_y)
          
    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_8_16100eV_wa{wax}_bpm{xbpm}'

    #         bpm = xbpm2.sumX.value

    #         sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%4.3f'%bpm)
    #         sample_id(user_name='GF', sample_name=sample_name)
    #         print(f'\n\t=== Sample: {sample_name} ===\n')
    #         yield from bp.count(dets, num=1)


def song_waxs_2020_3(t=1):
    dets = [pil300KW, pil1M]

    waxs_arc = np.linspace(19.5, 19.5, 1)
    del_y = [-500, 500, 3]

    yield from bps.mv(stage.th, 0)
    yield from bps.mv(stage.y, 0)
    names = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2',
    'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2', 'G3']
    x = [43200, 37500, 32400, 27000, 21700, 16700, 11700,  6700,  1700, -3300, -8300, -13300, -18400, -23300, -28500, -34500, -40700, 
    44000, 39000, 34000, 28200, 22700, 17000, 11000, 5300, -500, -6400, -12100, -17900, -23300, -29000, -35200, -41200]
    y = [-7800, -7800, -7800, -7800, -7800, -7800, -7800, -7800, -7800, -7800, -7800, -7800,  -7800,  -7800,  -7800,  -7800,  -7800,
    4500,  4500,  4300,  4500,  4500,  4500,  4500,  4500, 5400,  4500,  4500,   5100,   4500,   4700,   4700,  4700]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
           
            det_exposure_time(t,t) 
            name_fmt = '{sample}_10_16100eV_wa{wax}_bpm{xbpm}'

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(sample=name, wax = '%2.1f'%wa, xbpm = '%4.3f'%bpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.rel_scan(dets, piezo.x, *del_y)


    # yield from bps.mv(stage.th, 1)
    # yield from bps.mv(stage.y, -7)
    # names = ['G4', 'H1', 'H2', 'H3', 'H4', 'H5']
    # x = [43200, 36800, 30000, 24200, 17500, 10600]
    # y = [-9000, -9000, -9000, -8900, -8900, -8500]

    # for wa in waxs_arc:
    #     yield from bps.mv(waxs, wa)
    #     for name, xs, ys in zip(names, x, y):
    #         yield from bps.mv(piezo.x, xs)
    #         yield from bps.mv(piezo.y, ys)
          
    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_16100eV_wa{wax}_bpm{xbpm}'

    #         bpm = xbpm2.sumX.value

    #         sample_name = name_fmt.format(sample=name, wax = '%2.1f'%wa, xbpm = '%4.3f'%bpm)
    #         sample_id(user_name='GF', sample_name=sample_name)
    #         print(f'\n\t=== Sample: {sample_name} ===\n')
    #         yield from bp.rel_scan(dets, piezo.x, *del_y)



def song_waxs_Sedge_2020_3(t=1):
    
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1 )

    dets = [pil300KW]
    waxs_arc = np.linspace(0, 19.5, 4)
    energies = np.linspace(2460, 2490, 16)

    yield from bps.mv(stage.th, 0)
    yield from bps.mv(stage.y, 0)

    names = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2',
    'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2', 'G3']
    x = [43300, 37500, 32150, 26600, 21600, 16600, 11600,  6500,  1500, -3500, -8300, -13300, -18650, -23800, -29000, -34500, -40950, 
    44000, 38750, 33750, 28450, 22700, 16500, 11000, 5050, -250, -6400, -12100, -17900, -23300, -29000, -35450, -41200]
    y = [-7300, -7300, -6800, -6800, -6800, -7000, -7000, -6500, -6500, -6700, -6700, -6700,  -6700,  -6500,  -7000,  -7000,  -7000,
    5500,  5500,  5500,  5500,  5700,  5900,  5900,  5900, 6600,  6100,  5600,   6400,   5900,   5900,   6400,  6400]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 500, 8)
        xss = np.linspace(xs, xs + 250, 2)

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

            yield from bps.mv(energy, 2475)
            yield from bps.mv(energy, 2460)


def waxs_zhang(t=2):
    dets = [pil300KW]

    names = ['F1bd','C1bd']
    x = [-2000, -12000]
    y = [1500, 1500]

    
    #energies = np.linspace(2450, 2500, 26)
    waxs_arc = [0]
    
    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
                
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_16100.00eV_wa{wax}_bpm{xbpm}'

            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%4.3f'%bpm)
            sample_id(user_name='SZ', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            
            yield from bp.count(dets, num=50)


def mapping_S_edge_zhang(t=2):
    dets = [pil300KW, pil1M]
    
    names = ['F3map','C4map']
    xx = [19200, 8800]
    yy = [600, 600]
    

    for x, y, name in zip(xx, yy, names):

        ys = np.linspace(y, y + 1800, 37)
        xs = np.linspace(x, x - 3000, 16)
        
        #energies = [2450, 2474, 2478, 2500]
        waxs_arc = [0]
        
        yss, xss = np.meshgrid(ys, xs)
        yss = yss.ravel()
        xss = xss.ravel()

      #  for e in energies: 
      #      yield from bps.mv(energy, e)
      #      yield from bps.sleep(5)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            for pos, (xsss, ysss) in enumerate(zip(xss, yss)):
                yield from bps.mv(piezo.x, xsss)
                yield from bps.mv(piezo.y, ysss)

                det_exposure_time(t,t)
                name_fmt = '{sample}_16100eV_wa{wax}_bpm{xbpm}_pos{posi}'
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%4.3f'%bpm, posi = '%3.3d'%pos)
                sample_id(user_name='SZ', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

       # yield from bps.mv(energy, 2470)
       # yield from bps.mv(energy, 2450)



def nightplan_S_edge_zhang(t=2):
    #yield from waxs_S_edge_zhang(t=2)
    #yield from bps.sleep(10)
    yield from mapping_S_edge_zhang(t=2)




def song_nexafs_S_2021_1(t=1):
    dets = [pil300KW]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(52, 52, 1)

    names = ['A2_2_nexafs', 'B1_2_nexafs', 'C1_2_nexafs']
    # x = [-10600, 22000]
    # y = [ -4400, -5000]

    x = [15500, 9500, 1800]
    y = [-4000, -4400, -4400]

    # names = ['C2_2_nexafs']
    # x = [-5400]
    # y = [-5200]
    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

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



def song_waxs_2021_1(t=1):
    dets = [pil300KW, pil1M]

    waxs_arc = np.linspace(0, 19.5, 4)

    # names = ['A1',  'A3',  'A5',  'A8',  'A9', 'A11',  'B1',  'B3',   'B5',   'B8',  'B10',  'B11',   'C1',   'C2']
    # x =    [37200, 31900, 25400, 18400, 11400,  5400,  -600, -7900, -14200, -19900, -25900, -31900, -37900, -43500]
    # y =    [-5480, -4700, -4800, -4800, -4800, -4600, -4100, -5100,  -4700,  -4100,  -4500,  -4100,  -4500,  -4100]


    names = ['B10']
    x =    [-25900]
    y =    [-4500]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        for name, xs, ys in zip(names, x, y):

            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
           
            for pos, i in enumerate([-250, 0, 250]):
                yield from bps.mv(piezo.x, xs + i)

                det_exposure_time(t,t) 
                name_fmt = '{sample}_2_16100eV_sdd5m_wa{wax}_bpm{xbpm}_pos{pos}'

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, wax = '%2.1f'%wa, xbpm = '%4.3f'%bpm, pos = '%2.2d'%pos)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)




def song_waxs_Sedge_2021_1(t=1):
    dets = [pil300KW, pil1M]
    waxs_arc = np.linspace(0, 39, 7)
    energies = [2450, 2474, 2476, 2478]

    # names = ['A1',  'A3',  'A5',  'A8',  'A9', 'A11',  'B1',  'B3',   'B5',   'B8',  'B10',  'B11',   'C1',   'C2',  'A2',  'A4', 'A10', 'A12',  'B2', 'B4', 'B6', 'xxx']
    # x =    [36800, 31500, 24400, 18100, 10600,  4700,  -800, -8400, -14600, -19900, -25900, -31700, -37900, -43700, 41500, 35500, 28500, 21000, 14000, 8150,  650, -5400]
    # y =    [-5500, -4800, -5400, -5200, -5100, -5100, -4400, -5100,  -5100,  -4700,  -4700,  -4600,  -4900,  -4500,  8000,  7000,  7500,  7500,  8200, 8300, 8100,  8300]


    names = ['A3_2',  'A9_2', 'A11_2',  'B1_2',  'B10_2',  'B11_2',   'C2_2',  'A2_2',  'A12_2',  'B2_2']
    x =    [30800, 11200,  4700, -1100, -26500, -32300, -44000, 41300,  21000, 13500]
    y =    [-4500, -4800, -5100, -5560,  -4700,  -4460,  -4360,  8040,   8120,  7260]

    for wa in waxs_arc[::-1]:
        yield from bps.mv(waxs, wa)    
        
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            yss = np.linspace(ys, ys + 120, 4)

            det_exposure_time(t,t) 
            name_fmt = '{sample}_sdd1.6m_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, ysss in zip(energies, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2460)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(2)
