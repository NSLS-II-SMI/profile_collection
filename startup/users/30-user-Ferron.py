

def xrr_spol_waxs(t=1):
    # names =  ['PS-20', 'PSS_20', 'Y6_ac-ref', 'homo_M', 'homo_T', 'homo_S' ]
    # x_piezo = [ 30000,    15800,         800,   -16200,   -35200,   -46200]
    # y_piezo = [  6570,     6570,        6570,     6570,     6570,     6570]
    # z_piezo = [  3000,     3000,        2000,     2000,     2000,     2000]
    # ener = [[2450, 2477]], [2450, 2483, 2484, 2484.5, 2485, 2485.5, 2490, 2500], [2450, 2475, 2476.5, 2477, 2477.5, 2478, 2483, 2500],
    # [2450, 2477]], [2450, 2475, 2476.0, 2476.5, 2477, 2477.5, 2483, 2500], [2450, 2482, 2483, 2483.5, 2484.0, 2484.5, 2490, 2500],]


    # names =  ['PM6_ref_redo', 'PS_50',  'BCP_MT', 'BCP_TM', 'BCP_MS', 'BCP_SM', 'homo_T', 'homo_S', 'Y6_ref']
    # x_piezo = [   53000,   42000,     22500,     8500,    -5500,   -17500,   -29500,   -40500,   -48500]
    # y_piezo = [    6570,    6570,      6570,     6570,     6570,     6570,     6570,     6570,     6570]
    # z_piezo = [    2000,    2000,      2000,     2000,     2000,     2000,     2000,     2000,     2000]
    
    # ener = [[2450, 2475, 2477, 2483],
    # [2450, 2477],
    # [2450, 2475, 2476.0, 2476.5,   2477, 2477.5, 2483, 2500],
    # [2450, 2475, 2476.0, 2476.5,   2477, 2477.5, 2483, 2500],
    # [2450, 2482,   2483, 2483.5, 2484.0, 2484.5, 2490, 2500],
    # [2450, 2482,   2483, 2483.5, 2484.0, 2484.5, 2490, 2500],
    # [2450, 2475, 2476.0, 2476.5,   2477, 2477.5, 2483, 2500],
    # [2450, 2482,   2483, 2483.5, 2484.0, 2484.5, 2490, 2500],
    # [2450, 2475, 2476.5,   2477, 2477.5,   2478, 2483, 2500]]

    names =  [ 'BCP_SM', 'Y6_ref']
    x_piezo = [  -29600,   -45600]
    y_piezo = [    7200,     7200]
    z_piezo = [       0,        0]
    
    ener = [[2450, 2483, 2483.5, 2484.0, 2484.5, 2490], [2450, 2475, 2477, 2477.5,   2478, 2483]]


    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(ener), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(ener)})'

    dets = [pil300KW]
    waxs_arc = [1]

    # #List of incident angles clustured in subsection for attenuators
    # ai_lists = [[np.linspace(0.03, 1.03, 51).tolist() + np.linspace(1.05,  2.01, 33).tolist()] + [np.linspace(2.01,  2.51, 26).tolist()] + 
    # [np.linspace(0.51,  1.5, 34).tolist()] + [np.linspace(1.55, 4, 50).tolist()] + [np.linspace(4, 6, 41).tolist()] + [np.linspace(6, 8, 41).tolist()]]

    ai_lists = [[np.linspace(0.03, 1.03, 51).tolist() + np.linspace(1.05,  2.01, 33).tolist()] + [np.linspace(2.01,  2.51, 26).tolist()] + 
    [np.linspace(0.87,  1.17, 11).tolist()] + [np.linspace(1.2,  1.5, 11).tolist()] + [np.linspace(1.55, 2.7, 24).tolist()] + 
    [np.linspace(2.75, 4, 26).tolist()] + [np.linspace(4, 6, 41).tolist()] + [np.linspace(6, 8, 41).tolist()]]


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
                yield from bps.mvr(piezo.x, -200)  

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



def xrr_spol_waxs_smallstep(t=1):

    names =  ['Bilayer_ref']
    x_piezo = [30500]
    y_piezo = [6570]
    z_piezo = [2000]
    
    ener = [[2450, 2475, 2477, 2479, 2483]]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(ener), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(ener)})'

    dets = [pil300KW]
    waxs_arc = [1]

    # #List of incident angles clustured in subsection for attenuators
    ai_lists = [[np.linspace(0.03, 1.03, 101).tolist() + np.linspace(1.05,  2.01, 65).tolist()] + [np.linspace(2.01,  2.51, 51).tolist()] + 
    [np.linspace(0.87,  1.5, 43).tolist()] + [np.linspace(1.55, 4, 99).tolist()] + [np.linspace(4, 6, 81).tolist()] + [np.linspace(6, 8, 81).tolist()]]


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
                yield from bps.mvr(piezo.x, -200)  

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
    # names =  ['PSS70_ver', 'Y6_ver']
    # x_piezo = [      -900,     -900]
    # y_piezo = [     -2000,    -7000]
    # y_hexa =  [         0,       -8]
    # z_piezo = [      2000,     2000]
    # ener =    [[2450, 2485], [2450, 2475, 2476.5, 2477, 2477.5, 2478, 2483, 2500]]

    names =  [ 'PM6_ver', 'bilayer_ref']
    x_piezo = [     -900,          -900]
    y_piezo = [     4000,         -7000]
    y_hexa =  [        0,            -7]
    z_piezo = [     2000,          2000]
    ener =    [[2450, 2475, 2477, 2483], [2450, 2475, 2477, 2479, 2483]]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(y_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_hexa)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(ener), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(ener)})'

    dets = [pil300KW]
    waxs_arc = [1]

    ai_lists = [[np.linspace(0.03, 1.03, 51).tolist() + np.linspace(1.05,  2.01, 33).tolist()] + [np.linspace(2.01,  2.51, 26).tolist()] + 
    [np.linspace(0.87,  1.17, 11).tolist()] + [np.linspace(1.2,  1.5, 11).tolist()] + [np.linspace(1.55, 2.7, 24).tolist()] + 
    [np.linspace(2.75, 4, 26).tolist()] + [np.linspace(4, 6, 41).tolist()] + [np.linspace(6, 8, 41).tolist()]]

    for name, xs, zs, ys, ys_hexa, eners in zip(names, x_piezo, z_piezo, y_piezo, y_hexa, ener):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.y, ys_hexa)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(GV7.open_cmd, 1)
        yield from bps.sleep(2)
        yield from bps.mv(GV7.open_cmd, 1)
        yield from bps.sleep(2)

        yield from alignement_xrr(angle = 0.15)
        ai0 = prs.position

        yield from bps.mv(GV7.close_cmd, 1)
        yield from bps.sleep(2)
        yield from bps.mv(GV7.close_cmd, 1)
        yield from bps.sleep(2)

        for energ in eners:
            yield from bps.mv(energy, energ)
            yield from bps.sleep(5)
            yield from bps.mvr(piezo.y, -30)

            #ai_list should be a list of list. No change of attenuation inside one list
            for k, ai_list in enumerate(ai_lists[0]):
                ai_list = [round(1000 * x, 4) for x in ai_list]
                ai_list = np.asarray(ai_list) / 1000
                print(ai_list)

                absorbers, exp_time = yield from calc_absorbers_expt(num=k)

                #iterate over the angle stored in one list
                for l, ais in enumerate(ai_list):
                    #check if negative is the good direction
                    yield from bps.mv(prs, ai0 - ais)

                    #How to move waxs => reste / quotien of ais
                    yield from bps.mv(waxs.arc, waxs_arc[0] + 2*ais)
                    det_exposure_time(exp_time,exp_time)

                    bpm = xbpm3.sumX.value
                    name_fmt = '{sample}_aiscan_{energy}keV_ai{angle}deg_wa{waxs}_abs{absorber}_bpm{bpm}_time{time}'
                    sample_name = name_fmt.format(sample=name,
                                                    energy = '%4.2f'%energ,
                                                    angle ='%4.3f'%ais,
                                                    waxs ='%2.1f'%(waxs_arc[0] + 2*ais),
                                                    absorber = absorbers,
                                                    bpm = '%2.3f'%bpm,
                                                    time = '%1.1f'%exp_time)

                    sample_id(user_name='TF', sample_name=sample_name)
                    yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 2470)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2450)
        yield from bps.mv(prs, ai0)





def night_xrr(t=1):
    yield from xrr_spol_waxs(t=1)
    yield from bps.sleep(5)

    yield from xrr_spol_waxs_smallstep(t=1)
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
        det_exposure_time(2, 2)
        return '1', 2

    if num == 2:
        yield from bps.mv(att2_10.open_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_11.close_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_10.open_cmd, 1)        
        yield from bps.sleep(1)
        yield from bps.mv(att2_11.close_cmd, 1)        
        yield from bps.sleep(1)
        det_exposure_time(0.1, 0.1)
        return '2', 0.1

    if num == 3:
        det_exposure_time(0.2, 0.2)
        return '2', 0.2

    if num == 4:
        det_exposure_time(0.5, 0.5)
        return '2', 0.5

    if num == 5:
        det_exposure_time(1, 1)
        return '2', 1

    if num == 6:
        det_exposure_time(2, 2)
        return '2', 2

    if num == 7:
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

    # names =  [ 'PSS0', 'Y6', 'homo_M', 'homo_T', 'homo_S']
    # x_piezo = [15800,  800,   -16200,   -35200,   -46200]
    # y_piezo = [ 6570, 6570,     6570,     6570,     6570]
    # z_piezo = [ 2000, 3000,     3000,     3000,     3000]


    names =  [ 'PM6_hor']
    x_piezo = [-33000]


    for name, x in zip(names, x_piezo):
        yield from bps.mv(piezo.x, x)

        det_exposure_time(t,t) 
        name_fmt = 'nexafs_{sample}_{energy}eV_angle{ai}_bpm{xbpm}'
        
        yield from bps.mv(GV7.open_cmd, 1)
        yield from bps.sleep(2)
        yield from bps.mv(GV7.open_cmd, 1)

        yield from alignement_gisaxs(angle = 0.4)
    
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



def nexafs_Ferron_vertical(t=1):
    dets = [pil300KW]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = [52.5]
    ai = [1.5]

    # names =  ['Y6']
    # x_piezo = [ -900]
    # y_piezo = [-7000]
    # y_hexa = [    -8]
    # z_piezo = [    0]

    names =  [ 'PM6_real_ver']
    x_piezo = [     -900]
    y_piezo = [     4000]
    y_hexa =  [        0]
    z_piezo = [     2000]


    for name, x, y, ys_hexa in zip(names, x_piezo, y_piezo, y_hexa):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(stage.y, ys_hexa)

        det_exposure_time(t,t) 
        name_fmt = 'nexafs_{sample}_{energy}eV_angle{ai}_bpm{xbpm}'
        
        yield from bps.mv(GV7.open_cmd, 1)
        yield from bps.sleep(2)
        yield from bps.mv(GV7.open_cmd, 1)

        yield from alignement_xrr(angle = 0.15)
    
        yield from bps.mv(GV7.close_cmd, 1)
        yield from bps.sleep(2)
        yield from bps.mv(GV7.close_cmd, 1)


        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)

        ai0 = prs.position

        for ais in ai:
            yield from bps.mv(prs, ai0 - ais)

            for e in energies: 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                bpm = xbpm3.sumX.value

                sample_name = name_fmt.format(sample=name+'vert', energy='%6.2f'%e, ai ='%2.2d'%ais, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

        yield from bps.mv(prs, ai0)

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




def refl_ener_scan_spol_waxs(t=1):
    names =  ['PM6_ref', 'PS_50', 'Bilayer_ref', 'BCP_MT', 'BCP_TM', 'BCP_MS', 'BCP_SM', 'homo_T', 'homo_S', 'Y6_ref']
    x_piezo = [   54000,   42000,         30500,    22500,     8500,    -5500,   -17500,   -29500,   -40500,   -48500]
    y_piezo = [    6570,    6570,          6570,     6570,     6570,     6570,     6570,     6570,     6570,     6570]
    z_piezo = [    2000,    2000,          2000,     2000,     2000,     2000,     2000,     2000,     2000,     2000]
    

    ener =  [np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2480, 10).tolist() + np.arange(2483, 2487, 0.5).tolist() + np.arange(2487, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2480, 10).tolist() + np.arange(2483, 2487, 0.5).tolist() + np.arange(2487, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(), 
    np.arange(2445, 2480, 10).tolist() + np.arange(2483, 2487, 0.5).tolist() + np.arange(2487, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist(),
    np.arange(2445, 2470, 10).tolist() + np.arange(2472, 2482, 0.5).tolist() + np.arange(2482, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()]

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




def refl_ener_scan_ppol_waxs(t=1):
    names =  [ 'PM6_ver']
    x_piezo = [     -900]
    y_piezo = [     4000]
    y_hexa =  [        0]
    z_piezo = [     2000]
    ener =  [np.arange(2445, 2470, 10).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(ener), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(ener)})'

    dets = [pil300KW]
    waxs_arc = [1]

    ai_list = [0.4, 1]


    for name, xs, zs, ys, ys_hexa, eners in zip(names, x_piezo, z_piezo, y_piezo, y_hexa, ener):
        # yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.y, ys_hexa)
        yield from bps.mv(piezo.z, zs)

        # yield from alignement_gisaxs(angle = 0.15)
        ai0 = prs.position

        for k, ais in enumerate(ai_list):
            #check if negative is the good direction
            yield from bps.mv(prs, ai0 - ais)

            #How to move waxs => reste / quotien of ais
            yield from bps.mv(waxs.arc, waxs_arc[0] + 2*ais)
        
            yield from bps.mv(att2_11.open_cmd, 1)
            yield from bps.sleep(1)
            yield from bps.mv(att2_11.open_cmd, 1)
            yield from bps.sleep(1)
            yield from bps.mv(att2_10.close_cmd, 1)
            yield from bps.sleep(1)
            yield from bps.mv(att2_10.close_cmd, 1)
            yield from bps.sleep(1)

            det_exposure_time(t, t)

            for energ in eners:
                yield from bps.mv(energy, energ)  
                yield from bps.sleep(1)  

                bpm = xbpm3.sumX.value
                name_fmt = '{sample}_energyscan_{energy}keV_ai{angle}deg_wa{waxs}_abs{absorber}_bpm{bpm}_time{time}'
                sample_name = name_fmt.format(sample=name,
                                                energy = '%4.2f'%energ,   
                                                angle ='%4.3f'%ais,
                                                waxs ='%2.1f'%(waxs_arc[0] + 2*ais),
                                                absorber = '2',
                                                bpm = '%2.3f'%bpm,
                                                time = '%1.1f'%t)

                sample_id(user_name='TF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2450)                
            yield from bps.sleep(2)
        yield from bps.mv(prs, ai0)




def xrr_spol_waxs_smallstep_pedge(t=1):

    names =  ['homo_P', 'BCP_M9', 'BCP_PM1', 'homo_M']
    x_piezo = [-10000, -23000, -38000, -52000]
    y_piezo = [6570,6570, 6570, 6570]
    z_piezo = [2000, 2000, 2000, 2000]
    
    ener = [[2140, 2152, 2155, 2156, 2190], [2140, 2152, 2155, 2156, 2190], [2140, 2152, 2155, 2156, 2190], [2140, 2152, 2155, 2156, 2190]]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(ener), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(ener)})'

    dets = [pil300KW]
    waxs_arc = [1]

    # #List of incident angles clustured in subsection for attenuators
    ai_lists = [[np.linspace(0.03, 1.03, 101).tolist() + np.linspace(1.05,  2.01, 65).tolist()] + [np.linspace(2.01,  2.51, 51).tolist()] + 
    [np.linspace(0.87,  1.5, 43).tolist()] + [np.linspace(1.55, 4, 99).tolist()] + [np.linspace(4, 6, 81).tolist()] + [np.linspace(6, 7, 41).tolist()]]


    for name, xs, zs, ys, eners in zip(names, x_piezo, z_piezo, y_piezo, ener):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from alignement_gisaxs(angle = 0.15)
        ai0 = piezo.th.position

        for wa in waxs_arc:
            yield from bps.mv(waxs.arc, wa)  

            for energ in eners:
                while abs(energy.energy.position - energ) > 10:
                    if energ > energy.energy.position:
                        yield from bps.mv(energy, energy.energy.position+10)
                    else:
                        yield from bps.mv(energy, energy.energy.position-10)
                    yield from bps.sleep(5)  

                    
                yield from bps.mv(energy, energ)  
                yield from bps.sleep(5)  
                yield from bps.mvr(piezo.x, -200)  

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

 
        yield from bps.mv(piezo.th, ai0)
