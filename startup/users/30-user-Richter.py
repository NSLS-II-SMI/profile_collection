def giwaxs_S_edge_Lee(t=1):
    dets = [pil1M, pil300KW]
    
    # names = ['P3MMEMT_115C_1_', 'P3MMEMT_115C_Cl04', 'P3HT_F', 'P3MMEMT_175C_', 'P3MMEMT_175C_Cl04', 'P3HHT', 'P3HHT_ClO4']
    # x = [-49800, -40000, -24000, -8000, 3000, 22000, 43000]

    # energies = [2450.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    # 2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]


    # names = ['P3MMEMT_115C_Cl04_4', 'P3MMEMT_115C_4_']
    # x = [-36000, -47000]
    # names = ['P3MMEMT_115C_Cl04_4', 'P3MMEMT_115C_4_', 'P3MMEMT_175C_', 'P3MMEMT_175C_Cl04', 'P3HHT', 'P3HHT_ClO4']
    # x = [-36000, -47000, -5500, 5500, 25000, 46000]

    # # energies = [2810.0, 2820.0, 2823.0, 2825.0, 2825.5, 2826.0, 2826.5, 2827.0, 2827.5, 2828.0, 2828.5, 2829.0, 2829.5,
    # 2830.0, 2830.5, 2833.0, 2835.0, 2840.0, 2845.0, 2850.0]



    # energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5,
    # 2838.0, 2838.5, 2839.0, 2839.5, 2841.0, 2845.0, 2850.0, 2855.0]


    names = ['P3MMEMT_115C_4_']
    energies = [2450.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    
    waxs_arc = [10.5, 17]

    dets = [pil300KW]

    for name in names:
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)   

            name_fmt = '{sample}_{energy}eV_ai0.8_pos1_wa{wax}_bpm{xbpm}'
            for e in energies:
                yield from bps.mv(energy, e)
                yield from bps.sleep(0.5)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                # for e in energies[::-1]:
                #     yield from bps.mvr(piezo.x, 50)
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(0.5)
                #     bpm = xbpm2.sumX.value
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='GF', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)

                # yield from bps.mvr(piezo.x, 200)
                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos3_wa{wax}_bpm{xbpm}'
                # for e in energies: 
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(0.5)
                #     bpm = xbpm2.sumX.value
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='GF', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos4_wa{wax}_bpm{xbpm}'
                # for e in energies[::-1]: 
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(0.5)
                #     bpm = xbpm2.sumX.value
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='GF', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)


        # dets = [pil300KW]


        # yield from bps.mv(att2_9, 'Retract')
        # yield from bps.mv(att2_10, 'Retract')
        # yield from bps.mv(GV7.close_cmd, 1 )
        # yield from bps.sleep(1)
        # yield from bps.mv(att2_9, 'Retract')
        # yield from bps.mv(att2_10, 'Retract')
        # yield from bps.mv(GV7.close_cmd, 1 )
        # yield from bps.sleep(1)

        # yield from bps.mv(waxs, 52.5)    
        # for k, ais in enumerate(ai_list):
        #     yield from bps.mv(piezo.th, ai0 + ais)
        #     yield from bps.mv(piezo.x, xs + 2000 + k*200)

        #     det_exposure_time(t,t) 
        #     name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
        #     for e in energies: 
        #         yield from bps.mv(energy, e)
        #         yield from bps.sleep(0.5)

        #         bpm = xbpm2.sumX.value
        #         sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
        #         sample_id(user_name='GF', sample_name=sample_name)
        #         print(f'\n\t=== Sample: {sample_name} ===\n')
        #         yield from bp.count(dets, num=1)

        #     yield from bps.mv(energy, 2780)
        #     yield from bps.sleep(1)
        #     yield from bps.mv(energy, 2750)
        # yield from bps.mv(GV7.open_cmd, 1 )
        # yield from bps.sleep(1)
        # yield from bps.mv(GV7.open_cmd, 1 )
        # yield from bps.sleep(1)





def giwaxs_S_edge_Lee_2020_3(t=1):
    dets = [pil1M, pil300KW]
    

    # names = ['s01_P3HT015_un', 's04_P3MEEMT_115_un', 's33_MM460_170_ClO4', 's09_Pg2t-tt_woac_un', 's10_Pg2t-tt_woac_ClO4']
    # x = [40000, 25000, 16000, 5000, -4000]

    names = ['s11_Pg2t-tt_wac_un', 's12_Pg2t-tt_wac_ClO4', 's39_MM389_170_un', 's29_MM389_170_ClO4']
    x = [-15000, -27000, -37000, -50000]

    energies = [2450.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    
    waxs_arc = [2, 8.5, 15]

    dets = [pil1M, pil300KW]
    det_exposure_time(t,t) 

    ai0 = 0
    ai_list = [0.52, 0.80]

    for name, xs in zip(names, x):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.th, ai0)

        yield from alignement_special(angle = 0.45)
        
        yield from bps.mv(att2_9, 'Insert')
        yield from bps.sleep(1)
        yield from bps.mv(att2_9, 'Insert')
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*400)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 200)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                # yield from bps.mvr(piezo.x, 200)
                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos3_wa{wax}_bpm{xbpm}'
                # for e in energies: 
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(1)
                #     bpm = xbpm2.sumX.value
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='LR', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)

                # yield from bps.mvr(piezo.x, 200)
                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos4_wa{wax}_bpm{xbpm}'
                # for e in energies[::-1]: 
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(1)
                #     bpm = xbpm2.sumX.value
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='LR', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)

            

        yield from bps.mv(waxs, 45)

        yield from bps.mv(piezo.th, ai0 + 0.8)
        yield from bps.mv(piezo.x, xs + 1000)
 
        name_fmt = '{sample}_{energy}eV_ai0.8_pos5_wa{wax}_bpm{xbpm}'
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)
            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
            sample_id(user_name='LR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)



def night_12_02(t=1):
    # yield from transition_S_Cl_edges()

    proposal_id('2020_3', '307296_Richter1')
    yield from Cl_edge_measurments_night_12_02(t=t)

    yield from transition_Cl_S_edges()

    proposal_id('2020_3', '307296_Richter')
    yield from S_edge_measurments_night_12_02(t=t)



def S_edge_measurments_night_12_02(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    # names = ['s13_P3HT_ac_un', 's14_P3HT_ac_ClO4', 's15_P3HHT_ac_un', 's16_P3HHT_ac_ClO4', 's17_P3MEEMT_ac_un', 's18_P3MEEMT_ac_ClO4', 's19_P3APPT_ac_un',
    # 's20_P3APPT_ac_ClO4','s21_P3PAAT_ac_un', 's22_P3PAAT_ac_ClO4', 's11_Pg2t-tt_wac_un', 's12_Pg2t-tt_wac_ClO4', 's39_MM389_170_un']
    # x_piezo = [57500, 46500, 36500, 25500, 30500, 20500, 11500, 1500, -9500, -20500, -39500, -49500, -57500]
    # z_piezo = [  500,   500,   500,   500,   500,   500,   500,  500,  -300,   -300,  -1500,  -2000 , -1100]
    # x_hexap = [   17,    17,    17,    17,     0,     0,     0,    0,     0,      0,    -13,    -13,   -13]

    names = ['s39_MM389_170_Cl']
    x_piezo = [-5000]
    z_piezo = [-1100]
    x_hexap = [    0]
    energies = [2450.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    
    waxs_arc = [2, 8.5, 15]
    ai0 = 0
    ai_list = [0.52, 0.80]

    yield from bps.mv(piezo.x, -2200)

    for name, xs, zs, xs_hexap in zip(names, x_piezo, z_piezo, x_hexap):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(stage.x, xs_hexap)

        yield from bps.mv(piezo.th, 0.3877)

        # yield from bps.mv(piezo.th, ai0)

        # yield from alignement_special(angle = 0.45)
        
        # yield from bps.mv(att2_9, 'Insert')
        # yield from bps.sleep(1)
        # yield from bps.mv(att2_9, 'Insert')
        # yield from bps.sleep(1)

        ai0 = piezo.th.position
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*400)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 200)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

        yield from bps.mv(waxs, 45)

        yield from bps.mv(piezo.th, ai0 + 0.8)
        yield from bps.mv(piezo.x, xs + 1000)
 
        name_fmt = '{sample}_{energy}eV_ai0.8_pos5_wa{wax}_bpm{xbpm}'
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)
            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = 45, xbpm = '%4.3f'%bpm)
            sample_id(user_name='LR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        
        yield from bps.mv(energy, 2490)
        yield from bps.sleep(1)
        yield from bps.mv(energy, 2470)
        yield from bps.sleep(1)
        yield from bps.mv(energy, 2450)
        yield from bps.sleep(1)



def Cl_edge_measurments_night_12_02(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    # names = ['s13_P3HT_ac_un', 's14_P3HT_ac_ClO4', 's15_P3HHT_ac_un', 's16_P3HHT_ac_ClO4', 's17_P3MEEMT_ac_un', 's18_P3MEEMT_ac_ClO4', 's19_P3APPT_ac_un',
    # 's20_P3APPT_ac_ClO4','s21_P3PAAT_ac_un', 's22_P3PAAT_ac_ClO4', 's09_Pg2t-tt_woac_un', 's10_Pg2t-tt_woac_ClO4', 's11_Pg2t-tt_wac_un', 's12_Pg2t-tt_wac_ClO4',
    # 's39_MM389_170_un']
    # x_piezo = [57500, 46500, 36500, 25500, 30500, 20500, 11500, 1500, -9500, -20500, -31500, -41500, -39500, -49500, -57500]
    # z_piezo = [  500,   500,   500,   500,   500,   500,   500,  500,  -300,   -500,   -700,   -700, -1500,  -2000 , -1100]
    # x_hexap = [   17,    17,    17,    17,     0,     0,     0,    0,     0,      0,      0,      0,   -13,    -13,    -13]

    # energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    # 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0]


    # names = ['s01_P3HT015_un', 's04_P3MEEMT_115_un', 's33_MM460_170_ClO4', 's39_MM389_170_Cl']
    # x_piezo = [ 34000, 22000, 10000, -5000]
    # z_piezo = [ -1000,   -1000,   0, -1100]
    # x_hexap = [      0,    0,     0,     0]

    names = ['s39_MM389_170_Cl']
    x_piezo = [ -5000]
    z_piezo = [ -1100]
    x_hexap = [     0]

    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0]
    
    waxs_arc = [2, 8.5, 15]
    ai0 = 0
    ai_list = [0.52, 0.80]

    offset = 1000 # offset to not measure again teh same position as sulfur

    for name, xs, zs, xs_hexap in zip(names, x_piezo, z_piezo, x_hexap):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(stage.x, xs_hexap)

        yield from bps.mv(piezo.th, 0.3877)

        # yield from alignement_special(angle = 0.45)
        
        # yield from bps.mv(att2_9, 'Insert')
        # yield from bps.sleep(1)
        # yield from bps.mv(att2_9, 'Insert')
        # yield from bps.sleep(1)

        ai0 = piezo.th.position
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + offset + k*400)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 200)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

        yield from bps.mv(waxs, 45)

        yield from bps.mv(piezo.th, ai0 + 0.8)
        yield from bps.mv(piezo.x, xs + offset + 1000)
 
        name_fmt = '{sample}_{energy}eV_ai0.8_pos5_wa{wax}_bpm{xbpm}'
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)
            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = 45, xbpm = '%4.3f'%bpm)
            sample_id(user_name='LR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
        
        yield from bps.mv(energy, 2850)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2830)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2810)
        yield from bps.sleep(2)




def P_edge_measurments(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    names = ['s05_P3MEEMT_115C_KPF6', 's34_MM460_170_KPF6', 's30_MMM389_170_KPF6', 's38_MM461_170_KPF6', 's8_P3HT_ac_KPF6',
    's42_MM389_170_KPF6', 's46_MM460_170_KPF6', 's50_MM461_170_KPF6']
    x_piezo = [42000, 31000, 19000, 6000, -6000, -16000, -33000, -44000]

    energies = [2140.0, 2145.0, 2150.0, 2155.0, 2157.0, 2157.5, 2158.0, 2158.5, 2159.0, 2159.5, 2160.0, 2160.5, 2161.0, 2161.5, 2162.0, 2162.5,
    2163.0, 2163.5, 2164.0, 2164.5, 2165.0, 2165.5, 2166.0, 2170.0, 2175.0, 2180.0, 2185.0, 2190.0, 2195.0, 2200.0]
    xbpm3_y = [1.416,   1.414,   1.412,  1.41,  1.4092, 1.409, 1.4088, 1.4086, 1.4084, 1.4082,  1.408, 1.4078, 1.4076, 1.4074, 1.4072,  1.407, 
    1.4068, 1.4066, 1.4064, 1.4062, 1.406,  1.4058, 1.4056,  1.404,  1.402,    1.4,  1.398,  1.396,  1.394,  1.392]

    waxs_arc = [0, 17]
    ai0 = 0
    ai_list = [0.52, 0.80]

    offset = 0 # offset to not measure again teh same position as sulfur

    for name, xs in zip(names, x_piezo):
        yield from bps.mv(piezo.x, xs)

        yield from alignement_special(angle = 0.75)

        ai0 = piezo.th.position
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + offset + k*400)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'

                for e, xbpm3_ys in zip(energies, xbpm3_y):                              
                    yield from bps.mv(energy, e)
                    yield from bps.mv(xbpm3_pos.y, xbpm3_ys)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 200)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e, xbpm3_ys in zip(energies[::-1], xbpm3_y[::-1]):                              
                    yield from bps.mv(energy, e)
                    yield from bps.mv(xbpm3_pos.y, xbpm3_ys)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)



def transition_Cl_S_edges():
    yield from bps.mv(energy, 2800)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2780)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2760)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2740)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2720)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2700)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2680)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2660)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2640)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2610)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2580)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2550)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2525)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2500)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2475)
    yield from bps.sleep(5)
    yield from bps.mv(energy, 2450)
    yield from bps.sleep(5)

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





def SVA_night_12_02(t=1):

    global names, x_hexa, y_hexa, incident_angles, y_hexa_aligned
    # names = ['s27_MM389_170_un_2nd', 's28_MM389_170_Cl', 's29_MM389_170_ClO4', 's37_MM461_170_ClO4', 's31_MM460_170_Un', 's35_MM461_170_Un', 's36_MM461_170_Cl',
    # 's32_MM460_170_Cl']
    # x_hexa = [ -15, -15, -7 ,   -5,    7,   7,  13, 14.5]
    # y_hexa = [-3.2, 3.2, 3.2, -3.2, -3.2, 3.2, 3.2, -3.2]

    names = ['MM389_ac_un', 'MM389_ac_Cl', 'MM460_ac_un', 'MM460_ac_Cl', 'ps_peo_11', 'ps_peo_7525']
    x_hexa = [ -15, -7.0,  5.0, 17.0,  -8,   8]
    y_hexa = [-3.2, -3.2, -3.2, -3.2, 3.2, 3.2]

    incident_angles = []
    y_hexa_aligned = []

    # ai01 = 3.1
    # ai02 = 3.1


    setDryFlow(5)
    setWetFlow(0)

    # for name, xs_hexa, ys_hexa in zip(names, x_hexa, y_hexa):
    #     yield from bps.mv(stage.x, xs_hexa)
    #     yield from bps.mv(stage.y, ys_hexa)
    #     if ys_hexa == -3.2:
    #         yield from bps.mv(stage.th, ai01)
        
    #     else:
    #         yield from bps.mv(stage.th, ai02)

    #     yield from alignement_special_hex(angle = 0.45)

    #     incident_angles = incident_angles + [stage.th.position]
    #     y_hexa_aligned = y_hexa_aligned + [stage.y.position]




    incident_angles = [ 2.935,  3.074,  2.729,  2.785, 3.188, 3.076]                                                                                                                                                                                               
    y_hexa_aligned =  [-3.251, -3.303, -3.281, -3.318, 3.259, 3.193]

    print(incident_angles)
    print(y_hexa_aligned)

    # humidity = '%3.2f'%readHumidity(verbosity=0)
    # # Measure the samples with N2 flow
    # offset = 0
    # yield from S_edge_SVA_measurments1(t=t, offset = offset, humidity = humidity)

    # yield from transition_S_Cl_edges()
    # offset = 0.8
    # yield from Cl_edge_SVA_measurments(t=t, offset = offset, humidity = humidity)
    # yield from transition_Cl_S_edges()

    # Measure at flow 80 percent
    # setDryFlow(2.)
    # setWetFlow(4.35)

    # yield from bps.sleep(40 * 60)
    # humidity = '%3.2f'%readHumidity(verbosity=0)

    # offset = 1.6
    # yield from S_edge_SVA_measurments(t=t, offset = offset, humidity = humidity)
    # yield from transition_S_Cl_edges()
    # offset = 2.4
    # yield from Cl_edge_SVA_measurments(t=t, offset = offset, humidity = humidity)
    # yield from transition_Cl_S_edges()

    # # Measure at flow 100 percent
    # setDryFlow(0)
    # setWetFlow(5)

    # yield from bps.sleep(90 * 60)
    # humidity = '%3.2f'%readHumidity(verbosity=0)
    # offset = 3.2
    # yield from S_edge_SVA_measurments(t=t, offset = offset, humidity = humidity)
    # yield from transition_S_Cl_edges()
    # offset = 4.0
    # yield from Cl_edge_SVA_measurments(t=t, offset = offset, humidity = humidity)         
    # yield from bps.sleep(60*60)
    

    # # Back at flow 0 percent
    # setDryFlow(0)
    # setWetFlow(0)

    yield from bps.sleep(90 * 60)

    humidity = '%3.2f_post'%readHumidity(verbosity=0)

    offset = 4.8
    yield from S_edge_SVA_measurments(t=t, offset = offset, humidity = humidity)
    yield from transition_S_Cl_edges()
    offset = 5.6
    yield from Cl_edge_SVA_measurments(t=t, offset = offset, humidity = humidity)
    yield from transition_Cl_S_edges()




def S_edge_SVA_measurments1(t=1, offset = 0, humidity = 'test'):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    energies = [2450.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    
    waxs_arc = [0, 15]
    ai0 = 0
    ai_list = [0.52, 0.80]

    for name, xs_hexa, incident_ang, ys_hexap in zip(names[2:-2], x_hexa[2:-2], incident_angles[2:-2], y_hexa_aligned[2:-2]):
        yield from bps.mv(stage.x, xs_hexa + offset)
        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            
            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + offset + k*0.4)
 
                name_fmt = '{sample}_hum{hum}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, hum = humidity, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(stage.x, 0.2)
                name_fmt = '{sample}_hum{hum}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'

                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, hum = humidity, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)


    
    for name, xs_hexa, incident_ang, ys_hexap in zip(names[-2:], x_hexa[-2:], incident_angles[-2:], y_hexa_aligned[-2:]):
        yield from bps.mv(stage.x, xs_hexa + offset)
        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            
            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + offset + k*0.4)
 
                name_fmt = '{sample}_hum{hum}_2450.00eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, hum = humidity, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


def S_edge_SVA_measurments(t=1, offset = 0, humidity = 'test'):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    energies = [2450.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    
    waxs_arc = [0, 15]
    ai0 = 0
    ai_list = [0.52, 0.80]

    for name, xs_hexa, incident_ang, ys_hexap in zip(names[:-2], x_hexa[:-2], incident_angles[:-2], y_hexa_aligned[:-2]):
        yield from bps.mv(stage.x, xs_hexa + offset)
        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            
            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + offset + k*0.4)
 
                name_fmt = '{sample}_hum{hum}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, hum = humidity, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(stage.x, 0.2)
                name_fmt = '{sample}_hum{hum}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'

                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, hum = humidity, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)


    
    for name, xs_hexa, incident_ang, ys_hexap in zip(names[-2:], x_hexa[-2:], incident_angles[-2:], y_hexa_aligned[-2:]):
        yield from bps.mv(stage.x, xs_hexa + offset)
        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            
            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + offset + k*0.4)
 
                name_fmt = '{sample}_hum{hum}_2450.00eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, hum = humidity, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)



def Cl_edge_SVA_measurments(t=1, offset = 1, humidity = 'test'):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0]
    
    waxs_arc = [0, 15]
    ai_list = [0.52, 0.80]

    for name, xs_hexa, incident_ang, ys_hexap in zip(names[:-2], x_hexa[:-2], incident_angles[:-2], y_hexa_aligned[:-2]):
        yield from bps.mv(stage.x, xs_hexa + offset)
        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + offset + k*0.4)
 
                name_fmt = '{sample}_hum{hum}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, hum = humidity, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(stage.x, 0.2)
                name_fmt = '{sample}_hum{hum}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, hum = humidity, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)


    for name, xs_hexa, incident_ang, ys_hexap in zip(names[-2:], x_hexa[-2:], incident_angles[-2:], y_hexa_aligned[-2:]):
        yield from bps.mv(stage.x, xs_hexa + offset)
        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            
            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + offset + k*0.4)
 
                name_fmt = '{sample}_hum{hum}_2820.00eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, hum = humidity, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)



def SVA_Si(t=1):

    global names, x_hexa, y_hexa, incident_angles, y_hexa_aligned
    names = ['Si_top', 'Si_bottom']
    x_hexa = [-7 ,   -7]
    y_hexa = [-3.2, 3.2]
    incident_angles = [1.942, 2.1248]
    y_hexa_aligned = [ -3.30, 3.126]

    # yield from bps.sleep(40 * 60)
    humidity = '%3.2f'%readHumidity(verbosity=0)

    offset = 0
    yield from S_edge_SVA_measurments_Si(t=t, offset = offset, humidity = humidity)
    yield from transition_S_Cl_edges()
    offset = 0
    yield from Cl_edge_SVA_measurments_Si(t=t, offset = offset, humidity = humidity)
    yield from transition_Cl_S_edges()

    setDryFlow(0)
    setWetFlow(0)


def S_edge_SVA_measurments_Si(t=1, offset = 0, humidity = 'test'):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    energies = [2450.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    
    waxs_arc = [0, 15]
    ai_list = [0.52, 0.80]

    for name, xs_hexa, incident_ang, ys_hexap in zip(names, x_hexa, incident_angles, y_hexa_aligned):
        yield from bps.mv(stage.x, xs_hexa + offset)
        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            
            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + offset + k*0.4)
 
                name_fmt = '{sample}_hum{hum}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, hum = humidity, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)



def Cl_edge_SVA_measurments_Si(t=1, offset = 1, humidity = 'test'):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0]
    
    waxs_arc = [0, 15]
    ai_list = [0.52, 0.80]

    for name, xs_hexa, incident_ang, ys_hexap in zip(names, x_hexa, incident_angles, y_hexa_aligned):
        yield from bps.mv(stage.x, xs_hexa + offset)
        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + offset + k*0.4)
 
                name_fmt = '{sample}_hum{hum}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, hum = humidity, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)



def Cl_edge_vertical(t=1):
    dets = [pil300KW]
    det_exposure_time(t,t)     

    #name = 's01_P3HT015_un', 's04_P3MEEMT_115_un', 's33_MM460_170_ClO4'
    name = 's33_MM460_170_ClO4'

    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0]
    
    waxs_arc = [4, 10.5, 17, 45]

    ai0 = piezo.th.position
    for i, wa in enumerate(waxs_arc):
        if i==0:
            print('wa=4deg')
        else:
            yield from bps.mv(waxs, wa)  

        name_fmt = '{sample}_vertical_{energy}eV_ai0.8deg_pos1_wa{wax}_bpm{xbpm}'
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)
            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
            sample_id(user_name='LR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 2850)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2830)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2810)
        yield from bps.sleep(2)







def NEXAFS_P_edge(t=0.5):
        yield from bps.mv(waxs, 45)
        dets = [pil300KW]
        name = 'NEXAFS_s3_test_Pedge_nspot1'

        energies = np.linspace(2130, 2180, 51)
        xbpm3_y = np.linspace(1.42, 1.40, 51)
        
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
        
        for e, xbpm3_ys in zip(energies, xbpm3_y):                              
            yield from bps.mv(energy, e)
            yield from bps.mv(xbpm3_pos.y, xbpm3_ys)

            yield from bps.sleep(1)

            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumX.value)
            sample_id(user_name='LR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        



def SCledges_night_12_04(t=0.5):

    global names, x_piezo, z_piezo, x_hexa, incident_angles, y_piezo_aligned, offset
    names = ['s05_P3MEEMT_115C_KPF6', 's34_MM460_170_KPF6', 's30_MMM389_170_KPF6', 's38_MM461_170_KPF6', 's8_P3HT_ac_KPF6', 
    's27_MM389_170_un_2nd', 's28_MM389_170_Cl', 's29_MM389_170_ClO4', 's31_MM460_170_Un','s32_MM460_170_Cl',
    's35_MM461_170_Un', 's36_MM461_170_Cl', 's37_MM461_170_ClO4']
    
    x_piezo = [57000, 46000, 33000, 22000, 23500, 7500,  -500, -16000, -28000, -40000, -49000, -48000, -59800]
    z_piezo = [  900,   900,   900,   900,  -100, -100, -1100,  -1100,  -1100,   -100,  -1100,  -2100,  -2100]
    x_hexa = [    13,    13,    13,    13,     0,    0,     0,     0,       0,      0,      0,    -16,    -16]
    incident_angles = [1.054,         1.504,     0.703,     0.735,     0.738,     0.882,     1.050,     0.671,     0.843,     0.862,     0.941,    0.8726,   0.8755] 
    y_piezo_aligned = [-1092.163, -1392.168, -1599.025, -1771.178, -1861.675, -2123.148, -2241.939, -2504.472, -2684.332, -2757.973, -2990.557, -3099.528, -3258.484]

    # for name, xs_piezo, zs_piezo, xs_hexa in zip(names, x_piezo, z_piezo, x_hexa):
    #     yield from bps.mv(stage.x, xs_hexa)
    #     yield from bps.mv(piezo.x, xs_piezo)
    #     yield from bps.mv(piezo.z, zs_piezo)

    #     yield from alignement_special(angle = 0.45)
        

    #     incident_angles = incident_angles + [piezo.th.position]
    #     y_piezo_aligned = y_piezo_aligned + [piezo.y.position]


    yield from bps.mv(att2_9, 'Insert')
    yield from bps.sleep(1)
    yield from bps.mv(att2_9, 'Insert')
    yield from bps.sleep(1)

    print(incident_angles)
    print(y_piezo_aligned)


    offset = 0
    yield from S_edge_measurments_night_12_04(t=t)
    yield from transition_S_Cl_edges()
    
    offset = 1000
    yield from Cl_edge_measurments_night_12_04(t=t)
    yield from transition_Cl_S_edges()





def S_edge_measurments_night_12_04(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    energies = [2450.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    
    waxs_arc = [0, 15]
    ai_list = [0.52, 0.80]

    for name, xs, zs, xs_hexap, aiss, ys in zip(names[1:], x_piezo[1:], z_piezo[1:], x_hexa[1:], incident_angles[1:], y_piezo_aligned[1:]):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, aiss)
        yield from bps.mv(stage.x, xs_hexap)

        ai0 = piezo.th.position
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, offset + xs + k*400)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 200)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)


def Cl_edge_measurments_night_12_04(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0]
    
    waxs_arc = [0, 15]
    ai_list = [0.52, 0.80]

    for name, xs, zs, xs_hexap, aiss, ys in zip(names[5:], x_piezo[5:], z_piezo[5:], x_hexa[5:], incident_angles[5:], y_piezo_aligned[5:]):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, aiss)
        yield from bps.mv(stage.x, xs_hexap)

        ai0 = piezo.th.position
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, offset + xs + k*400)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 200)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)    









def S_edge_measurments_night_03_03(t=1):
    dets = [pil1M, pil300KW]

    # names = ['P3MEEMT_13_075_000', 'P3MEEMT_13_075_275', 'P3MEEMT_13_075_300', 'P3MEEMT_13_075_350', 'P3MEEMT_13_075_400', 'P3MEEMT_13_075_600',
    # 'P3MEEMT_13_115_000', 'P3MEEMT_13_115_275', 'P3MEEMT_13_115_300', 'P3MEEMT_13_115_350', 'P3MEEMT_13_115_400', 'P3MEEMT_13_115_600',
    # 'P3MEEMT_13_175_000', 'P3MEEMT_13_175_300', 'P3MEEMT_13_175_275', 'P3MEEMT_13_175_350', 'P3MEEMT_13_175_400', 'P3MEEMT_13_175_600',
    # 'P3MEEMT_40_115_000', 'P3MEEMT_40_115_275', 'P3MEEMT_40_115_300', 'P3MEEMT_40_115_350', 'P3MEEMT_40_115_400', 'P3MEEMT_40_115_600',
    # 'P3MEEMT_40_175_000', 'P3MEEMT_40_175_275', 'P3MEEMT_40_175_300', 'P3MEEMT_40_175_350', 'P3MEEMT_40_175_400', 
    # #'P3MEEMT_40_175_600',
    # ]
   
    # x_piezo = [52000, 50000, 40000, 30000, 20000, 10000,    0, -10000, -19000, -27000, -37000, -46000, -56000, -57000,
    # 52000, 52000, 45000, 35500, 26000, 17000, 8000, -2500, -13000, -24000, -33000, -43000, -52000, -57000, -58000]
    # x_hexap = [   11,     0,     0,     0,     0,     0,    0,      0,     0,       0,      0,      0,      0,     -9,
    #    13,     2,     0,     0,     0,     0,    0,     0,      0,      0,      0,      0,      0,     -5,    -12]
    # y_piezo = [ 4800,  4800,  4800,  4800,  4800,  4800, 4800,   4800,   4800,   4800,   4800,   4800,   4800,   4800,
    # -4400, -4400, -4400, -4400, -4400, -4400,-4400, -4400,  -4400,  -4400,  -4400,  -4400,  -4400,  -4400,  -4400]


    names = ['P3MEEMT_13_075_400', 'P3MEEMT_13_075_600',
    'P3MEEMT_13_115_000', 'P3MEEMT_13_115_275', 'P3MEEMT_13_115_300', 'P3MEEMT_13_115_350', 'P3MEEMT_13_115_400', 'P3MEEMT_13_115_600',
    'P3MEEMT_13_175_000', 'P3MEEMT_13_175_300', 'P3MEEMT_13_175_275', 'P3MEEMT_13_175_350', 'P3MEEMT_13_175_400', 'P3MEEMT_13_175_600',
    'P3MEEMT_40_115_000', 'P3MEEMT_40_115_275', 'P3MEEMT_40_115_300', 'P3MEEMT_40_115_350', 'P3MEEMT_40_115_400', 'P3MEEMT_40_115_600',
    'P3MEEMT_40_175_000', 'P3MEEMT_40_175_275', 'P3MEEMT_40_175_300', 'P3MEEMT_40_175_350', 'P3MEEMT_40_175_400', 
    ]
   
    x_piezo = [20000, 10000,    0, -10000, -19000, -27000, -37000, -46000, -56000, -57000,
    52000, 52000, 45000, 35500, 26000, 17000, 8000, -2500, -13000, -24000, -33000, -43000, -52000, -57000, -58000]
    x_hexap = [    0,     0,    0,      0,     0,       0,      0,      0,      0,     -9,
       13,     2,     0,     0,     0,     0,    0,     0,      0,      0,      0,      0,      0,     -5,    -12]
    y_piezo = [ 4800,  4800, 4800,   4800,   4800,   4800,   4800,   4800,   4800,   4800,
    -3800, -3800, -3800, -3800, -3800, -3800,-3800, -3800,  -3800,  -3800,  -3800,  -3800,  -3800,  -3800,  -3800]


    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(x_hexap), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})'
    energies = [2450.0, 2455.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2487.5, 2490.0, 2492.5, 2495.0, 2500.0, 2510.0, 2515.0]
    
    waxs_arc = [0, 15]
    ai0 = 0
    ai_list = [0.80, 7.70]

    for numb, (name, xs, ys, xs_hexap) in enumerate(zip(names, x_piezo, y_piezo, x_hexap)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yield from bps.mv(stage.x, xs_hexap)


        yield from bps.mv(piezo.th, 0)

        # yield from alignement_special(angle = 0.45)
        yield from alignement_gisaxs(0.45)   

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
                    

        ai0 = piezo.th.position
        det_exposure_time(t,t)     

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*600)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 300)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)
        


def Cl_edge_measurments_night_03_03(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    # names = ['P3MEEMT_13_075_000', 'P3MEEMT_13_075_275', 'P3MEEMT_13_075_300', 'P3MEEMT_13_075_350', 'P3MEEMT_13_075_400', 'P3MEEMT_13_075_600',
    # 'P3MEEMT_13_115_000', 'P3MEEMT_13_115_275', 'P3MEEMT_13_115_300', 'P3MEEMT_13_115_350', 'P3MEEMT_13_115_400', 'P3MEEMT_13_115_600',
    # 'P3MEEMT_13_175_000', 'P3MEEMT_13_175_300', 'P3MEEMT_13_175_275', 'P3MEEMT_13_175_350', 'P3MEEMT_13_175_400', 'P3MEEMT_13_175_600',
    # 'P3MEEMT_40_115_000', 'P3MEEMT_40_115_275', 'P3MEEMT_40_115_300', 'P3MEEMT_40_115_350', 'P3MEEMT_40_115_400', 'P3MEEMT_40_115_600',
    # 'P3MEEMT_40_175_000', 'P3MEEMT_40_175_275', 'P3MEEMT_40_175_300', 'P3MEEMT_40_175_350', 'P3MEEMT_40_175_400', 
    # #'P3MEEMT_40_175_600',
    # ]
   
    # x_piezo = [54000, 52000, 42000, 32000, 22000, 12000, 2000,  -8000, -17000, -25000, -35000, -44000, -54000, -55000,
    # 54000, 54000, 47000, 37500, 28000, 19000,10000,  -500, -11000, -22000, -31000, -41000, -50000, -55000, -56000]
    # x_hexap = [   11,     0,     0,     0,     0,     0,    0,      0,     0,       0,      0,      0,      0,     -9,
    #    13,     2,     0,     0,     0,     0,    0,     0,      0,      0,      0,      0,      0,     -5,    -12]
    # y_piezo = [ 4800,  4800, 4800,   4800,  4800,  4800,  4800,   4800,  4800,   4800,   4800,   4800,   4800,   4800,
    # -4400, -4400, -4400, -4400, -4400, -4400,-4400, -4400,  -4400,  -4400,  -4400,  -4400,  -4400,  -4400,  -4400]


    names = [
    'P3MEEMT_13_175_350', 'P3MEEMT_13_175_400', 'P3MEEMT_13_175_600',
    'P3MEEMT_40_115_000', 'P3MEEMT_40_115_275', 'P3MEEMT_40_115_300', 'P3MEEMT_40_115_350', 'P3MEEMT_40_115_400', 'P3MEEMT_40_115_600',
    'P3MEEMT_40_175_000', 'P3MEEMT_40_175_275', 'P3MEEMT_40_175_300', 'P3MEEMT_40_175_350', 'P3MEEMT_40_175_400', 
    #'P3MEEMT_40_175_600',
    ]
   
    x_piezo = [
    54000, 47000, 37500, 28000, 19000,10000,  -500, -11000, -22000, -31000, -41000, -50000, -55000, -56000]
    x_hexap = [
        2,     0,     0,     0,     0,    0,     0,      0,      0,      0,      0,      0,     -5,    -12]
    y_piezo = [
     -3800, -3800, -3800, -3800, -3800,-3800, -3800,  -3800,  -3800,  -3800,  -3800,  -3800,  -3800,  -3800]

    global y_piezo_aligned, ai_aligned

    y_piezo_aligned = []
    ai_aligned = []

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(x_hexap), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})'


    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0]
    
    waxs_arc = [0, 15]
    ai0 = 0
    ai_list = [0.80, 6.7]

    for name, xs, ys, xs_hexap in zip(names, x_piezo, y_piezo, x_hexap):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.x, xs_hexap)

        yield from bps.mv(piezo.th, 0)

        # yield from alignement_special(angle = 0.45)
        yield from alignement_gisaxs_quickLee(0.40)   

        y_piezo_aligned = y_piezo_aligned + [piezo.y.position]
        ai_aligned = ai_aligned + [piezo.th.position]

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)

        ai0 = piezo.th.position
        det_exposure_time(t,t)     

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*600)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 300)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)


def S_edge_measurments_night_03_04(t=1):
    dets = [pil1M, pil300KW]

    names = ['P3MEEMT_40_175_600']
   
    x_piezo = [ 54000]
    x_hexap = [    14]
    y_piezo = [  6900]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(x_hexap), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})'
    
    energies = [2450.0, 2455.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2487.5, 2490.0, 2492.5, 2495.0, 2500.0, 2510.0, 2515.0]
    
    waxs_arc = [0, 15]
    ai0 = 0
    ai_list = [0.80, 7.70]

    for numb, (name, xs, ys, xs_hexap) in enumerate(zip(names, x_piezo, y_piezo, x_hexap)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.x, xs_hexap)
        yield from bps.mv(piezo.th, 0)

        yield from alignement_gisaxs_quickLee(0.40)   

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
                    
        ai0 = piezo.th.position
        det_exposure_time(t,t)     

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*600)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 300)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)




def Cl_edge_measurments_night_03_04(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    names = ['P3MEEMT_40_175_600']
    x_piezo = [56000]
    x_hexap = [14]
    y_piezo = [6900]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(x_hexap), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})'


    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0]
    
    waxs_arc = [0, 15]
    ai0 = 0
    ai_list = [0.80, 6.7]

    for name, xs, ys, xs_hexap in zip(names, x_piezo, y_piezo, x_hexap):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.x, xs_hexap)

        yield from bps.mv(piezo.th, 0)
        yield from alignement_gisaxs_quickLee(0.40)   

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)

        ai0 = piezo.th.position
        det_exposure_time(t,t)     

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*600)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 300)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)



def SCledges_night_04_04(t=0.5):
    # proposal_id('2021_1', '307296_Richter3')
    # yield from S_edge_measurments_night_03_04(t=1)

    # yield from bps.sleep(5)
    # yield from transition_S_Cl_edges()
    # yield from bps.sleep(5)

    # proposal_id('2021_1', '307296_Richter2')
    # yield from Cl_edge_measurments_night_03_04(t=0.5)

    # yield from bps.sleep(5)
    # yield from transition_Cl_S_edges()
    # yield from bps.sleep(5)

    proposal_id('2021_1', '307822_McNeil10')
    yield from giwaxs_S_edge_2021_1_night2(t=1)




def S_edge_vertical(t=1):
    dets = [ pil300KW]
    det_exposure_time(t,t)     

    #name = 's01_P3HT015_un', 's04_P3MEEMT_115_un', 's33_MM460_170_ClO4'
    name = 'MM460_170'

    energies = [2450.0, 2455.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2487.5, 2490.0, 2492.5, 2495.0, 2500.0, 2510.0, 2515.0]
    
    
    # waxs_arc = [4, 10.5, 17]
    waxs_arc = [10.5, 17]

    ai0 = piezo.th.position
    for i, wa in enumerate(waxs_arc):
        if wa == 4:
            print('wa=4deg')
        else:
            yield from bps.mv(waxs, wa)

        name_fmt = '{sample}_vertical_{energy}eV_ai7.7deg_pos1_wa{wax}_bpm{xbpm}'
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)
            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
            sample_id(user_name='LR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 2490)
        yield from bps.sleep(1)
        yield from bps.mv(energy, 2470)
        yield from bps.sleep(1)
        yield from bps.mv(energy, 2450)
        yield from bps.sleep(1)





def S_edge_measurments_day_03_08(t=1):
    dets = [pil1M, pil300KW]

    names = ['P3HT_CB', 'P3MEEMT_40_115_000', 'P3MEEMT_13_115_000', 'PS', 'PVC', 'P3HT015', 'P3MEEMT_40_175_000', 'MM460_170']
   
    x_piezo = [ 56000, 56000, 51000, 38000, 24000,  12000, 3000, -6000]
    x_hexap = [    14,     5,     0,     0,     0,      0,    0,     0]
    y_piezo = [  6900,  6900,  6900,  6900,  6900,   6900, 6900,  6900]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(x_hexap), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})'
    
    # energies = [2450.0, 2455.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    # 2480.0, 2480.5, 2483.0, 2485.0, 2487.5, 2490.0, 2492.5, 2495.0, 2500.0, 2510.0, 2515.0]
    
    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0]

    waxs_arc = [0, 15]
    ai0 = 0
    # ai_list = [0.80, 7.70]
    ai_list = [0.80, 6.7]


    for numb, (name, xs, ys, xs_hexap) in enumerate(zip(names, x_piezo, y_piezo, x_hexap)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.x, xs_hexap)
        yield from bps.mv(piezo.th, 0)

        yield from alignement_gisaxs_quickLee(0.40)   

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
                    
        ai0 = piezo.th.position
        det_exposure_time(t,t)     

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*600)
 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 300)
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='LR', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)






def giwaxs_Cl_edge_Lee_aois_2121_1(t=1):
    dets = [pil1M, pil300KW]
    
    # names =   ['P3HT_600_KCl04_par', 'P3HT_500_KCl04', 'P3HT_neat', 'P3HT_600_KCl']
    # x_piezo = [              -31000,           -41000,      -53000,         -56000]   
    # x_hexa =  [                   0,                0,           0,             -8]
    # z_piezo = [                   0,                0,           0,              0]

    names =   ['P3HT_KCl04_bilayer']
    x_piezo = [               50000]   
    x_hexa =  [                   0]
    z_piezo = [                   0]

    dets = [pil1M, pil300KW]
    waxs_arc = [0, 15]

    for numero, (name, xs_piezo, xs_hexa, zs_piezo) in enumerate(zip(names, x_piezo, x_hexa, z_piezo)):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.z, zs_piezo)

        ai0 = 0
        yield from bps.mv(piezo.th, ai0)
        yield from alignement_gisaxs(angle = 0.4)
        ai0 = piezo.th.position

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
        

        ai_list = np.arange(0.3, 0.8, 0.01).tolist()
        ai_list = [round(1000*x, 4) for x in ai_list] 
        ai_list = np.asarray(ai_list)/1000
        energies = [2820.0, 2838.5, 2870.0]

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)   

            for k, e in enumerate(energies):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                
                yield from bps.mv(piezo.x, xs_piezo + k*600 + i*200)

                for l, ais in enumerate(ai_list):
                    yield from bps.mv(piezo.th, ai0 + ais)

                    det_exposure_time(t,t) 
                    name_fmt = '{sample}_pos1_aiscan_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}'

                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%1.4f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='GF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)
            
            for k, e in enumerate(energies[::-1]):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                
                yield from bps.mv(piezo.x, xs_piezo + 1000 + k*600 + i*200)

                for l, ais in enumerate(ai_list):
                    yield from bps.mv(piezo.th, ai0 + ais)

                    det_exposure_time(t,t) 
                    name_fmt = '{sample}_pos2_aiscan_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}'

                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='GF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)











def S_edge_measurments_trans_night_03_08(t=1):
    dets = [pil1M, pil300KW]

    # names = ['Standford_B8', 'Standford_B9', 'P3HT_CB', 'P3MEEMT_40_AS_trans', 'P3MEEMT_40_115_trans', 'P3MEEMT_40_175_trans', 'P3MEEMT_13_AS_trans', 'P3MEEMT_13_75_trans',
    # 'P3MEEMT_13_173_trans', 'P3MEEMT_13_175_300_trans', 'P3MEEMT_13_175_350_trans', 'P3MEEMT_13_175_400_trans', 'P3MEEMT_13_175_600_trans', 'P3MEEMT_13_115_trans','MM460_170_trans', 'Standford_B3', 'Standford_B4', 'Standford_B5', 'Standford_B6', 'Standford_B7', ]
   
    # x_piezo = [ 32200, 27100,  9100,  2500, -4600, -18600, -29800, -35800,
    # 40000, 34400, 28400, 22600, 16900, 11000,  200,  -13300, -18800, -25200, -29800, -36400]
    # y_piezo = [ -5400, -5400, -5800, -5800, -5800,  -5600,  -5600,  -5600,
    #  6700,  6700,  7000, 6700,   7000,  6600, 6700,    6800,   6800,   7300,   7000,   7000]

    names = ['Standford_B9', 'P3HT_CB', 'P3MEEMT_40_AS_trans', 'P3MEEMT_40_115_trans', 'P3MEEMT_40_175_trans', 'P3MEEMT_13_AS_trans', 'P3MEEMT_13_75_trans',
    'P3MEEMT_13_173_trans', 'P3MEEMT_13_175_300_trans', 'P3MEEMT_13_175_350_trans', 'P3MEEMT_13_175_400_trans', 'P3MEEMT_13_175_600_trans', 'P3MEEMT_13_115_trans','MM460_170_trans', 'Standford_B3', 'Standford_B4', 'Standford_B5', 'Standford_B6', 'Standford_B7', ]
   
    x_piezo = [27100,  9100,  2500, -4600, -18600, -29800, -35800,
    40000, 34400, 28400, 22600, 16900, 11000,  200,  -13300, -18800, -25200, -29800, -36400]
    y_piezo = [-5400, -5800, -5800, -5800,  -5600,  -5600,  -5600,
     6700,  6700,  7000, 6700,   7000,  6600, 6700,    6800,   6800,   7300,   7000,   7000]
    

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    
    energies = [2450.0, 2455.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2487.5, 2490.0, 2492.5, 2495.0, 2500.0, 2510.0, 2515.0]
    
    waxs_arc = [2, 8.5, 15]
    det_exposure_time(t,t)     

    for numb, (name, xs, ys) in enumerate(zip(names, x_piezo, y_piezo)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
                    
        yss = np.linspace(ys, ys + 1000, 27)
        
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            yield from bps.mv(piezo.x, xs)

            name_fmt = '{sample}_{energy}eV_pos1_wa{wax}_bpm{xbpm}'
            for e, ysss in zip(energies, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


            yield from bps.mvr(piezo.x, 300)
            name_fmt = '{sample}_{energy}eV_pos2_wa{wax}_bpm{xbpm}'
            for e, ysss in zip(energies[::-1], yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)



def S_edge_measurments_transprs54_night_03_08(t=1):
    yield from bps.mv(prs, -54.7356)
    dets = [pil1M, pil300KW]

    names = ['P3HT_CB', 'P3MEEMT_40_115_trans', 'P3MEEMT_40_175_trans', 'P3MEEMT_13_115_trans','MM460_170_trans']
   
    x_piezo = [  9900, -11600, -22800, 6900, -4500]
    y_piezo = [ -6000,  -5700,  -5800, 6800,  6800]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    
    energies = [2450.0, 2455.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2487.5, 2490.0, 2492.5, 2495.0, 2500.0, 2510.0, 2515.0]
    
    waxs_arc = [2, 8.5, 15]
    det_exposure_time(t,t)     

    for numb, (name, xs, ys) in enumerate(zip(names, x_piezo, y_piezo)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
                    
        yss = np.linspace(ys, ys + 1000, 27)
        
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(waxs, wa)

            name_fmt = '{sample}_prs-54.73deg_{energy}eV_pos1_wa{wax}_bpm{xbpm}'
            for e, ysss in zip(energies, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


            yield from bps.mvr(piezo.x, 100)
            name_fmt = '{sample}_{energy}eV_pos2_wa{wax}_bpm{xbpm}'
            for e, ysss in zip(energies[::-1], yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

    yield from bps.mv(prs, 0)




def Cl_edge_measurments_trans_night_03_08(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)     

    names = ['P3MEEMT_13_173_trans', 'P3MEEMT_13_175_300_trans', 'P3MEEMT_13_175_350_trans', 'P3MEEMT_13_175_400_trans', 'P3MEEMT_13_175_600_trans']
    x_piezo = [ 40500, 34500, 28900, 22900, 17000]
    y_piezo = [  4500,  4500,  4900,  4700,  5000]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'


    energies = [2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5, 
    2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0]
    
    waxs_arc = [2, 8.5, 15]
    for numb, (name, xs, ys) in enumerate(zip(names, x_piezo, y_piezo)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
                    
        yss = np.linspace(ys, ys + 1000, 27)
        
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            yield from bps.mv(piezo.x, xs)

            name_fmt = '{sample}_{energy}eV_pos1_wa{wax}_bpm{xbpm}'
            for e, ysss in zip(energies, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)


            yield from bps.mvr(piezo.x, 200)
            name_fmt = '{sample}_{energy}eV_pos2_wa{wax}_bpm{xbpm}'
            for e, ysss in zip(energies[::-1], yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='LR', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)



def SCledges_night_03_08(t=0.5):
    proposal_id('2021_1', '307296_Richter7')
    yield from S_edge_measurments_trans_night_03_08(t=0.5)
    yield from S_edge_measurments_transprs54_night_03_08(t=0.5)

    yield from bps.sleep(5)
    yield from transition_S_Cl_edges()
    yield from bps.sleep(5)

    proposal_id('2021_1', '307296_Richter8')
    yield from Cl_edge_measurments_trans_night_03_08(t=0.5)

