

def xrr_spol_waxs(t=1):
    # names =  ['PS-20', 'PSS_20', 'Y6_ac-ref', 'homo_M', 'homo_T', 'homo_S' ]
    # x_piezo = [ 30000,    15800,         800,   -16200,   -35200,   -46200]
    # y_piezo = [  6570,     6570,        6570,     6570,     6570,     6570]
    # z_piezo = [  3000,     3000,        2000,     2000,     2000,     2000]
    # ener = [[2450, 2477]], [2450, 2483, 2484, 2484.5, 2485, 2485.5, 2490, 2500], [2450, 2475, 2476.5, 2477, 2477.5, 2478, 2483, 2500],
    # [2450, 2477]], [2450, 2475, 2476.0, 2476.5, 2477, 2477.5, 2483, 2500], [2450, 2482, 2483, 2483.5, 2484.0, 2484.5, 2490, 2500],]



    names =  ['PSS_20', 'Y6_ac-ref', 'homo_M', 'homo_T', 'homo_S' ]
    x_piezo = [  13800,       -3200,   -17500,   -36200,   -48200]
    y_piezo = [   6570,        6570,     6570,     6570,     6570]
    z_piezo = [   2000,        2000,     2000,     2000,     2000]
    ener = [[2450, 2483, 2484, 2484.5, 2485, 2485.5, 2490, 2500], [2450, 2475, 2476.5, 2477, 2477.5, 2478, 2483, 2500],
    [2450, 2477], [2450, 2475, 2476.0, 2476.5, 2477, 2477.5, 2483, 2500], [2450, 2482, 2483, 2483.5, 2484.0, 2484.5, 2490, 2500]]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(ener), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(ener)})'

    dets = [pil300KW]
    waxs_arc = [1]

    # #List of incident angles clustured in subsection for attenuators
    # ai_lists = [[np.linspace(0.03, 0.3, 10).tolist()] + [np.linspace(0.21, 0.51, 11).tolist()] + 
    # [np.linspace(0.42, 0.99, 20).tolist()] + [np.linspace(0.87,  1.5, 22).tolist() + [1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2.0, 2.05, 2.1]] + 
    # [np.linspace(1.8, 10, 165).tolist()]]
    # #[np.linspace(1.8, 4.2, 49).tolist()] + [np.linspace(4,  10, 121).tolist()]] 

    # ai_lists = [[np.linspace(0.03, 0.51, 17).tolist()] + [np.linspace(0.21, 0.99, 27).tolist()] + 
    # [np.linspace(0.42, 1.5, 37).tolist()] + [np.linspace(0.87,  1.5, 22).tolist() + np.linspace(1.55,  4, 50).tolist()]
    # + [np.linspace(1.8, 10, 165).tolist()]]

    ai_lists = [[np.linspace(0.03, 1.03, 51).tolist() + np.linspace(1.05,  2.01, 33).tolist()] + [np.linspace(0.87,  1.5, 22).tolist()] + [np.linspace(1.55, 4, 50).tolist()]
    + [np.linspace(4, 6, 41).tolist()] + [np.linspace(6, 8, 41).tolist()] + [np.linspace(8, 10, 41).tolist()]]

    for name, xs, zs, ys, eners in zip(names, x_piezo, z_piezo, y_piezo, ener):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from alignement_gisaxs(angle = 0.15)
        ai0 = piezo.th.position

        for wa in waxs_arc:
            yield from bps.mv(waxs.arc, wa)  

            for energ in eners:
                yield from bps.mv(energy, energ)  
                yield from bps.sleep(5)  
                yield from bps.mvr(piezo.x, 300)  


                #ai_list should be a list of list. No change of attenuation inside one list
                for k, ai_list in enumerate(ai_lists[0]):
                    ai_list = [round(1000 * x, 4) for x in ai_list]
                    ai_list = np.asarray(ai_list) / 1000
                    print(ai_list)

                    # yield from calc_absorbers(num=k)
                    absorbers, exp_time = yield from calc_absorbers_expt(num=k)

                    #iterate over the angle stored in one list
                    for l, ais in enumerate(ai_list):
                        yield from bps.mv(piezo.th, ai0 + ais)
                        yield from bps.sleep(0.5)

                        det_exposure_time(exp_time,exp_time)

                        bpm = xbpm3.sumX.value
                        name_fmt = '{sample}_aiscan_{energy}keV_ai{angle}deg_wa{waxs}_abs{absorber}_bpm{bpm}_time{time}'
                        sample_name = name_fmt.format(sample=name,
                                                        energy = '%4.2f'%energ,   
                                                        angle ='%4.3f'%ais,
                                                        waxs ='%2.1f'%wa,
                                                        absorber = absorbers,
                                                        bpm = '%2.3f'%bpm,
                                                        time = '%1.1f'%exp_time)

                        sample_id(user_name='TF', sample_name=sample_name)
                        print(f'\n\t=== Sample: {sample_name} ===\n')    #Duplicate the 
                        yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)  
        yield from bps.mv(piezo.th, ai0)



def xrr_ppol_waxs(t=1):
    names =  ['PSS_20']
    x_piezo = [  13800]
    y_piezo = [   6570]
    z_piezo = [   2000]
    ener = [[2450]]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(ener), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(ener)})'

    dets = [pil300KW]
    waxs_arc = [1]

    ai_lists = [[np.linspace(0.03, 1.03, 51).tolist() + np.linspace(1.05,  2.01, 33).tolist()] + [np.linspace(0.87,  1.5, 22).tolist()] + [np.linspace(1.55, 4, 50).tolist()]
    + [np.linspace(4, 6, 41).tolist()] + [np.linspace(6, 8, 41).tolist()] + [np.linspace(8, 10, 41).tolist()]]

    for name, xs, zs, ys, eners in zip(names, x_piezo, z_piezo, y_piezo, ener):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from alignement_xrr(angle = 0.15)
        ai0 = prs.position

        for wa in waxs_arc:
            yield from bps.mv(waxs.arc, wa)

            for energ in eners:
                yield from bps.mv(energy, energ)
                yield from bps.sleep(5)
                yield from bps.mvr(piezo.x, 300)

                #ai_list should be a list of list. No change of attenuation inside one list
                for k, ai_list in enumerate(ai_lists[0]):
                    ai_list = [round(1000 * x, 4) for x in ai_list]
                    ai_list = np.asarray(ai_list) / 1000
                    print(ai_list)

                    # yield from calc_absorbers(num=k)
                    absorbers, exp_time = yield from calc_absorbers_expt(num=k)

                    #iterate over the angle stored in one list
                    for l, ais in enumerate(ai_list):
                        #check if negative is the good direction
                        yield from bps.mv(piezo.th, prs - ais)
                        yield from bps.sleep(0.5)

                        #How to move waxs => reste / quotien of ais

                        det_exposure_time(exp_time,exp_time)

                        bpm = xbpm3.sumX.value
                        name_fmt = '{sample}_aiscan_{energy}keV_ai{angle}deg_wa{waxs}_abs{absorber}_bpm{bpm}_time{time}'
                        sample_name = name_fmt.format(sample=name,
                                                        energy = '%4.2f'%energ,
                                                        angle ='%4.3f'%ais,
                                                        waxs ='%2.1f'%wa,
                                                        absorber = absorbers,
                                                        bpm = '%2.3f'%bpm,
                                                        time = '%1.1f'%exp_time)

                        sample_id(user_name='TF', sample_name=sample_name)
                        print(f'\n\t=== Sample: {sample_name} ===\n')    #Duplicate the
                        yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)
        yield from bps.mv(piezo.th, ai0)



def refl_ener_scan_spol_waxs(t=1):
    names =  ['PS-20', 'PSS_20', 'Y6_ac-ref', 'homo_M', 'homo_T', 'homo_S' ]
    x_piezo = [ 30000,    13800,       -3200,   -17500,   -36200,    -48200]
    y_piezo = [  6570,     6570,        6570,     6570,     6570,      6570]
    z_piezo = [  2000,     2000,        2000,     2000,     2000,      2000]

    ener =  [np.arange(2445, 2480, 10).tolist() + np.arange(2483, 2487, 0.5).tolist() + np.arange(2487, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2480, 10).tolist() + np.arange(2483, 2487, 0.5).tolist() + np.arange(2487, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(), 
    np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2470, 10).tolist() + np.arange(2472, 2482, 0.5).tolist() + np.arange(2482, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2480, 10).tolist() + np.arange(2483, 2487, 0.5).tolist() + np.arange(2487, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(ener), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(ener)})'

    dets = [pil300KW]
    waxs_arc = [1]


    ai_list = [0.4, 1]

    for name, xs, zs, ys, eners in zip(names, x_piezo, z_piezo, y_piezo, ener):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from alignement_gisaxs(angle = 0.15)
        ai0 = piezo.th.position

        for wa in waxs_arc:
            yield from bps.mv(waxs.arc, wa)  

            for k, ai in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.sleep(0.5)

                yield from bps.mv(att2_11.open_cmd, 1)
                yield from bps.sleep(1)
                yield from bps.mv(att2_11.open_cmd, 1)
                yield from bps.sleep(1)

                

                det_exposure_time(1, 1)

                for energ in eners:
                    yield from bps.mv(energy, energ)  
                    yield from bps.sleep(1)  

                    bpm = xbpm3.sumX.value
                    name_fmt = '{sample}_energyscan_{energy}keV_ai{angle}deg_wa{waxs}_abs{absorber}_bpm{bpm}_time{time}'
                    sample_name = name_fmt.format(sample=name,
                                                    energy = '%4.2f'%energ,   
                                                    angle ='%4.3f'%ais,
                                                    waxs ='%2.1f'%wa,
                                                    absorber = absorbers,
                                                    bpm = '%2.3f'%bpm,
                                                    time = '%1.1f'%exp_time)

                    sample_id(user_name='TF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')    #Duplicate the 
                    yield from bp.count(dets, num=1)

                yield from bps.mv(energy, 2470)
                yield from bps.sleep(2)
                yield from bps.mv(energy, 2450)                
                yield from bps.sleep(2)
        yield from bps.mv(piezo.th, ai0)



def night_xrr(t=1):
    yield from xrr_spol_waxs(t=1)
    yield from bps.sleep(5)

    yield from refl_ener_scan_spol_waxs(t=1)
    yield from bps.sleep(5)



def calc_absorbers_expt(num):
    print('num', num)
    if num==0:
        yield from bps.mv(att2_10.close_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_11.open_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_10.close_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_11.open_cmd, 1)        
        yield from bps.sleep(1)

        det_exposure_time(0.5, 0.5)
        
        return '1', 0.5

    if num == 1:
        yield from bps.mv(att2_10.open_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_11.close_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_10.open_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_11.close_cmd, 1)        
        yield from bps.sleep(1)
        det_exposure_time(0.5, 0.5)
        return '2', 0.5

    if num == 2:
        det_exposure_time(0.5, 0.5)
        return '2', 0.5

    if num == 3:
        det_exposure_time(1, 1)
        return '2', 1

    if num == 4:
        det_exposure_time(2, 2)
        return '2', 2

    if num == 5:
        det_exposure_time(5, 5)
        return '2', 5





def nexafs_Ferron(t=1):
    dets = [pil300KW]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = [52.5]
    ai = [1.5]

    # names =  [  'PS', 'PSS0', 'Y6', 'homo_M', 'homo_T', 'homo_S']
    # x_piezo = [34600,  15800,  800,   -16200,   -35200,   -46200]
    # y_piezo = [ 6570,   6570, 6570,     6570,     6570,     6570]
    # z_piezo = [ 3000,   2000, 3000,     3000,     3000,     3000]

    names =  [ 'PSS0', 'Y6', 'homo_M', 'homo_T', 'homo_S']
    x_piezo = [15800,  800,   -16200,   -35200,   -46200]
    y_piezo = [ 6570, 6570,     6570,     6570,     6570]
    z_piezo = [ 2000, 3000,     3000,     3000,     3000]


    for name, x, y in zip(names, x_piezo, y_piezo):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)

        det_exposure_time(t,t) 
        name_fmt = 'nexafs_{sample}_{energy}eV_angle{ai}_bpm{xbpm}'
        
        yield from bps.mv(GV7.open_cmd, 1)
        yield from bps.sleep(2)
        yield from bps.mv(GV7.open_cmd, 1)

        yield from alignement_gisaxs(angle = 0.5)
    
        yield from bps.mv(GV7.close_cmd, 1)
        yield from bps.sleep(2)
        yield from bps.mv(GV7.close_cmd, 1)


        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)

        ai0 = piezo.th.position

        for ais in ai:
            yield from bps.mv(piezo.th, ai0 + ais)

            for e in energies: 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                bpm = xbpm3.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%2.2d'%ais, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

        yield from bps.mv(piezo.th, ai0)

        yield from bps.mv(energy, 2470)
        yield from bps.sleep(1)
        yield from bps.mv(energy, 2450)
        yield from bps.sleep(1)







def xrr_spol_saxs(t=1):
    names =  ['PS_test9_saxs']
    x_piezo = [34800]
    y_piezo = [ 6570]
    z_piezo = [ 3000]
    ener = 2450.0

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'

    dets = [pil1M]
    waxs_arc = [13]

    # #List of incident angles clustured in subsection for attenuators
    # ai_lists = [[np.linspace(0.03, 0.3, 10).tolist()] + [np.linspace(0.21, 0.51, 11).tolist()] + 
    # [np.linspace(0.42, 0.99, 20).tolist()] + [np.linspace(0.87,  1.5, 22).tolist() + [1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2.0, 2.05, 2.1]] + 
    # [np.linspace(1.8, 10, 165).tolist()]]
    # #[np.linspace(1.8, 4.2, 49).tolist()] + [np.linspace(4,  10, 121).tolist()]] 

    # ai_lists = [[np.linspace(0.03, 0.51, 17).tolist()] + [np.linspace(0.21, 0.99, 27).tolist()] + 
    # [np.linspace(0.42, 1.5, 37).tolist()] + [np.linspace(0.87,  1.5, 22).tolist() + np.linspace(1.55,  4, 50).tolist()]
    # + [np.linspace(1.8, 10, 165).tolist()]]


    ai_lists = [[np.linspace(0.03, 0.99, 65).tolist()]]

    for name, xs, zs, ys in zip(names, x_piezo, z_piezo, y_piezo):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, -2.085)
        # yield from alignement_gisaxs(angle = 0.5)
        ai0 = piezo.th.position

        for wa in waxs_arc:
            yield from bps.mv(waxs.arc, wa)  

            #ai_list should be a list of list. No change of attenuation inside one list
            for k, ai_list in enumerate(ai_lists[0]):
                ai_list = [round(1000 * x, 4) for x in ai_list]
                ai_list = np.asarray(ai_list) / 1000
                print(ai_list)

                # yield from calc_absorbers(num=k)
                absorbers, exp_time = yield from calc_absorbers_expt(num=k)

                #iterate over the angle stored in one list
                for l, ais in enumerate(ai_list):
                    yield from bps.mv(piezo.th, ai0 + ais)
                    yield from bps.sleep(0.5)

                    det_exposure_time(exp_time,exp_time)

                    bpm = xbpm3.sumX.value
                    name_fmt = '{sample}_aiscan_{energy}keV_ai{angle}deg_wa{waxs}_abs{absorber}_bpm{bpm}_time{time}'
                    sample_name = name_fmt.format(sample=name,
                                                  energy = '%4.2f'%ener,   
                                                  angle ='%4.3f'%ais,
                                                  waxs ='%2.1f'%wa,
                                                  absorber = absorbers,
                                                  bpm = '%2.3f'%bpm,
                                                  time = '%1.1f'%exp_time)

                    sample_id(user_name='TF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')    #Duplicate the 

                    yield from bp.count(dets, num=1)
