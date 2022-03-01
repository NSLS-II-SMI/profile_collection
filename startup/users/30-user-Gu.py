def saxs_gu_2022_1(t=1): 
 
    xlocs = [ 33000,    24000,   15000,    6000,    -3000,   -12000,  -21000,  -30000,
              33000,    24000,   15000,    6000,    -3000,   -12000,  -21000,  -30000,]
    ylocs = [  5200,     6000,    5500,    6100,     5600,     5600,    5600,    4700,
                300,      300,     600,     300,      100,      100,    -200,    -500,]
    zlocs = [  2700,     2700,    2700,    2700,     2700,     2700,    2700,    2700,
               2700,     2700,    2700,    2700,     2700,     2700,    2700,    2700,]
    ystage =   [ 1.0,     1.0,     1.0,     1.0,      1.0,      1.0,     1.0,     1.0,
                 1.0,     1.0,     1.0,     1.0,      1.0,      1.0,     1.0,     1.0]
    names = ['samA1', 'samA2', 'samA3', 'samA4',  'samA5',  'samA6', 'samA7', 'samA8',
             'samB1', 'samB2', 'samB3', 'samB4',  'samB5',  'samB6', 'samB7', 'samB8',]
  
    user = 'YW'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})'
    assert len(xlocs) == len(ylocs), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(ylocs)})'
    assert len(xlocs) == len(zlocs), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(zlocs)})'
    assert len(xlocs) == len(ystage), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(ystage)})'
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})'

    # Detectors, motors:
    dets = [pil1M]
    waxs_range = [20]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z, y_sta in zip(names, xlocs, ylocs, zlocs, ystage):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)
            yield from bps.mv(stage.y, y_sta)

            name_fmt = '{sam}_16.1keV_sdd7.0m_wa{waxs}'
            sample_name = name_fmt.format(sam=sam,  waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=10)
            yield from bps.sleep(2)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 






def temp_2021_3(tim=0.5): 
    # Slowest cycle:
    temperatures = [115]

    name = 'YW'

    samples = ['Trimethyl_benzene', 'Pff4TBT', 'Toluene',  'PS', 'P3DT']
    x_list  = [              32200,     22500,     13200,  4200,  -9800]
    y_list =  [              -2900,     -3700,     -3500, -3700,  -3700]

    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    #Detectors, motors:
    dets = [pil1M] #ALL detectors
    
    waxs_arc = [20] 
    name_fmt = '{sample}_16.1keV_4.0m_{temperature}C_wa{waxs}'

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        t_kelvin = t + 273.15
        yield from ls.output1.mv_temp(t_kelvin)
        temp = ls.input_A.get()

        while abs(temp - t_kelvin) > 2.5:
            print(abs(temp - t_kelvin))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

        if i_t !=0:
            yield from bps.sleep(300)

        # temp = ls.input_A.get()
        t_celsius = temp - 273.15

        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            for x, y, s in zip(x_list, y_list, samples):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)
                
                sample_name = name_fmt.format(sample=s, temperature='%3.1f'%t_celsius, waxs='%2.1f'%wa)
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                sample_id(user_name=name, sample_name=sample_name) 
                yield from bp.count(dets, num=1)

    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)
    
    t_kelvin = 25 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)





def gu_nexafs_S_2021_3(t=1):
    dets = [pil900KW]

    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    energies = 2+np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())

    waxs_arc = np.linspace(40, 40, 1)


    # names=['Trimethyl_benzene_redo', 'Pff4TBT_redo_180C']
    # x = [31600, 4400]
    # y = [-3600, -4300]

    # names=['PTB7', 'PCE10', 'Pff4TBT_2ndrun', 'P3DT']
    # x = [ 13600, 19200, 4400, -27000]
    # y = [-4200, -4200, -4700, -4800]

    names=['Trimethyl_benzene_2ndrun']
    x = [ 31600]
    y = [-3400]

    assert len(names) == len(x), f'Number of X coordinates ({len(names)}) is different from number of samples ({len(x)})'
    assert len(y) == len(x), f'Number of X coordinates ({len(y)}) is different from number of samples ({len(x)})'


    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_nexafs_{energy}eV_wa{wax}_bpm{xbpm}'
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






def gu_saxs_S_2022_1(t=1):
    dets = [pil1M]

    energies = [2450, 2460, 2470, 2475, 2476, 2477, 2478, 2480, 2500]
    waxs_arc = [20]


    names=['Trimethyl_benzene_2ndrun']
    x = [ 31600]
    y = [-3300]
    # names=['PTB7', 'PCE10', 'Pff4TBT_2ndrun', 'P3DT']
    # x = [ 13600, 19200, 4400, -27000]
    # y = [-4200, -4200, -4700, -4800]
    # names=['Trimethyl_benzene', 'Pff4TBT']
    # x = [31600, 4600]
    # y = [-3600, -4300]

    assert len(names) == len(x), f'Number of X coordinates ({len(names)}) is different from number of samples ({len(x)})'
    assert len(y) == len(x), f'Number of X coordinates ({len(y)}) is different from number of samples ({len(x)})'


    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_1.6m_{energy}eV_wa{wax}_bpm{xbpm}'
            for i, e in enumerate(energies): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(5)
                # yield from bps.mv(piezo.y, ys + i * 50)


                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)




def gu_saxs_hardxray_2022_1(t=1):
    dets = [pil1M]

    energies = [16100]
    waxs_arc = [20]


    names=['Trimethyl_benzene', 'PCE10', 'PTB7', 'Pff4TBT', 'P3DT']
    x = [                31800,   19200,  14100,      5100, -27000]
    y = [                -3300,   -3800,  -3900,     -4000,  -4200]


    assert len(names) == len(x), f'Number of X coordinates ({len(names)}) is different from number of samples ({len(x)})'
    assert len(y) == len(x), f'Number of X coordinates ({len(y)}) is different from number of samples ({len(x)})'


    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_4.0m_{energy}eV_wa{wax}_exp5s'
            for i, e in enumerate(energies): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(5)
                # yield from bps.mv(piezo.y, ys + i * 50)

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)