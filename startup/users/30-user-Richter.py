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






