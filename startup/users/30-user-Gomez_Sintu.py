def run_saxs_nexafs_sintu(t=1):
    # yield from nexafs_prep_multisample_sintu(t=0.5)
    # yield from bps.sleep(10)
    yield from saxs_prep_multisample_sintu(t=0.5)


def nexafs_prep_multisample_sintu(t=1):

    yield from bps.mv(stage.th, 2.5)
    yield from bps.mv(stage.y, -5)

    samples = ['L1_J', 'L5_K', 'L7_L', 'L11_M', 'L15_N', 'L19_0']
    x_list  = [42500,  22400,  10200,  -7400,   -21150,  -33700]
    y_list =  [3900,  3900,  3900,  3900, 3900, 3900]

    for x, y, name in zip(x_list, y_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)

        yield from NEXAFS_Ca_edge_multi_sintu(t=t, name=name)
    

    # yield from bps.mv(stage.y, -5.5)
    # yield from bps.mv(stage.th, 1.5)

    # samples = ['O5L_1','O5CaL_1', 'DB_only']
    # x_list  = [39500, 30500, 35500]
    # y_list =  [3900, 3900, 3900]


    # for x, y, name in zip(x_list, y_list, samples):
    #     yield from bps.mv(piezo.x, x)
    #     yield from bps.mv(piezo.y, y)
    #     yield from NEXAFS_Ca_edge_multi_sintu(t=t, name=name)

    sample_id(user_name='test', sample_name='test')



def saxs_prep_multisample_sintu(t=1):
    dets = [pil300KW, pil1M]

    energies = [4030, 4040, 4050, 4055, 4075]
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_pos{posi}_wa{wa}_xbpm{xbpm}'
    waxs_range = [0, 6.5, 13.0, 19.5]


    det_exposure_time(t,t)

    ypos = [0, 400, 3]    
    for wa in waxs_range[::-1]:
        yield from bps.mv(waxs, wa)
    #     yield from bps.mv(stage.th, 2.5)
    #     yield from bps.mv(stage.y, -5)

    #     samples = ['L1_J', 'L2_J', 'L3_J', 'L4_J', 'L5_K', 'L6_K', 'L7_L', 'L8_L', 'L9_L', 'L10_L', 'L11_M', 'L12_M', 'L13_M', 
    #     'L14_M', 'L15_N', 'L16_N', 'L17_N', 'L18_N', 'L19_0', 'L20_0', 'L21_0', 'L22_0']
    #     x_list  = [42500, 38100, 34000, 30200, 22400, 17400, 10200, 5200, 600, -3500, -7400, -9950, -13800, 
    #     -17650, -21150, -24400, -27400, -30100, -33700, -36100, -38500, -41100]
    #     y_list =  [3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900, 3900,
    #     3900, 3900, 3900]


    #     for name, x, y in zip(samples, x_list, y_list):
    #         yield from bps.mv(piezo.x, x)
    #         yield from bps.mv(piezo.y, y)

    #         for k, e in enumerate(energies):                              
    #             yield from bps.mv(energy, e)
    #             name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

    #             sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
    #             sample_id(user_name='OS', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.rel_scan(dets, piezo.y, *ypos)
                            

    #         yield from bps.mv(energy, 4050)
    #         yield from bps.mv(energy, 4030)

        yield from bps.mv(stage.th, 2.5)
        yield from bps.mv(stage.y, -12)

        samples = ['PG2b', 'PG3b']
        x_list  = [-23000, -27900]
        y_list =  [-9800, -9700]


        ypos1 = [0, 600, 4]    
        xpos1 = [0, 600, 5]    
        for name, x, y in zip(samples, x_list, y_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for k, e in enumerate([4030, 4055]):                              
                yield from bps.mv(energy, e)
                name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.rel_grid_scan(dets, piezo.y, *ypos1, piezo.x, *xpos1, 0)

                            
            yield from bps.mv(energy, 4050)
            yield from bps.mv(energy, 4030)
            

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)




def NEXAFS_Ca_edge_multi_sintu(t=0.5, name='test'):
    yield from bps.mv(att2_11, 'Retract')
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(1)
    yield from bps.mv(att2_11, 'Retract')
    yield from bps.mv(GV7.close_cmd, 1 )

    yield from bps.mv(waxs, 52)
    dets = [pil300KW, amptek]
    
    dets = [pil300KW]

    energies = np.linspace(4030, 4150, 121)

    det_exposure_time(t,t) 
    name_fmt = 'nexafs_{sample}_{energy}eV_xbpm{xbpm}'
    for e in energies:                              
        yield from bps.mv(energy, e)
        sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
        RE.md['filename'] = sample_name
        sample_id(user_name='OS', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)

    yield from bps.mv(energy, 4125)
    yield from bps.mv(energy, 4100)        
    yield from bps.mv(energy, 4075)
    yield from bps.mv(energy, 4050)
    yield from bps.mv(energy, 4030)

    sample_id(user_name='test', sample_name='test')

    yield from bps.mv(att2_11, 'Insert')
    yield from bps.mv(GV7.open_cmd, 1 )
    yield from bps.sleep(1)
    yield from bps.mv(att2_11, 'Insert')
    yield from bps.mv(GV7.open_cmd, 1 )




# def NEXAFS_db_Ca_edge_multi_sintu(t=0.5, name='test'):

#     yield from bps.mv(waxs, 52)
    
#     dets = [pil1M]

#     energies = np.linspace(4030, 4150, 121)

#     det_exposure_time(t,t) 
#     name_fmt = 'transmission_nexafs_{sample}_{energy}eV_xbpm{xbpm}'
#     for e in energies:                              
#         yield from bps.mv(energy, e)
#         sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
#         sample_id(user_name='OS', sample_name=sample_name)
#         print(f'\n\t=== Sample: {sample_name} ===\n')
#         yield from bp.count(dets, num=1)


#     sample_id(user_name='test', sample_name='test')