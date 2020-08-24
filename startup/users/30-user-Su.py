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
    waxs_range = [0, 6.5, 13.0, 19.5, 26, 32.5, 39.0]
    #waxs_range = [0, 6.5, 13.0, 19.5]


    det_exposure_time(t,t)

    for wa in waxs_range[::-1]:
        yield from bps.mv(waxs, wa)
        yield from bps.mv(stage.y, -5.5)
        yield from bps.mv(stage.th, 1.5)

        samples = ['sample02', 'sample03', 'sample04', 'sample05', 'sample06', 'sample07', 'sample08', 'sample01']
        x_list  = [32500, 19500, 8500, -3500, -15500, -27500, -39500, 44500]
        y_list =  [3900,  3900,  3900,  3900, 3900,  3900,   3900,   3900]
        
        for name, x, y in zip(samples, x_list, y_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for k, e in enumerate(energies):                              
                yield from bps.mv(energy, e)
                name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                            

            yield from bps.mv(energy, 4050)
            yield from bps.mv(energy, 4030)
        

        yield from bps.mv(stage.y, -6.5)
        yield from bps.mv(stage.th, 1.5)

        samples = ['sample09', 'sample10', 'sample11']
        x_list  = [41000, 24000, 9000]
        y_list =  [-9500, -9500, -9500]

        for name, x, y in zip(samples, x_list, y_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for k, e in enumerate(energies):                              
                yield from bps.mv(energy, e)
                name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                            

            yield from bps.mv(energy, 4050)
            yield from bps.mv(energy, 4030)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)



def NEXAFS_Ca_edge_multi_greg(t=0.5, name='test'):
    yield from bps.mv(waxs, 52)
    dets = [pil300KW, amptek]
    
    #dets = [pil300KW]

    energies = np.linspace(4030, 4150, 121)

    det_exposure_time(t,t) 
    name_fmt = 'nexafs_{sample}_{energy}eV_xbpm{xbpm}'
    for e in energies:                              
        yield from bps.mv(energy, e)
        sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
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

    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())
    # energies = np.linspace(2450, 2500, 26)
    waxs_arc = [52.5]

    names = ['SPES20_2']
    x = [42000]
    y = [ 2000]

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