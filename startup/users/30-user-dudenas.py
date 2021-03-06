def run_night_Pete(t=1):
    #yield from giwaxs_S_edge_Pete(t=t)
    #yield from giwaxs_ai_S_edge_Pete(t=t)
    yield from nexafs_S_edge_Pete(t=1)


def giwaxs_multiprsangles_2020_3(t=1):
    dets = [pil1M, pil300KW]

    names = ['DDP_50','DDP_25','DDP_10','DDP_100','SEBS']
    x = [ -45000, -25000, -3000, 17000, 43000]
    z = [ 4190,  1690, -2310, -3310, -3810]
    chi_piezo = [-0.284, -0.129, -0.341, -0.401, -0.435]
    chi_hexa = [-0.256, -0.361, -0.349, -0.289, -0.255]
    th_hexa = [0.287, 0.287, 0.287, 0.287, 0.287]
    th_piezo = [0.76, 0.76, 0.56, 0.5, 0.5]

    waxs_arc = [1, 7.5]
    
    ai0 = 0
    ai_list = np.arange(0.07, 0.15, 0.002).tolist() 
    ai_list = [round(1000*x, 4) for x in ai_list] 
    ai_list = np.asarray(ai_list)/1000

    dets = [pil1M, pil300KW]
    
    for name, xs, zs, chi_pi, chi_hexa, th_pi, th_hexa in zip(names, x, z, chi_piezo, chi_hexa, th_piezo, th_hexa):
        yield from bps.mv(prs, 0)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chi_pi)
        yield from bps.mv(stage.ch, chi_hexa)
        yield from bps.mv(piezo.th, th_pi)
        yield from bps.mv(stage.th, th_hexa)

        yield from alignement_gisaxs(angle = 0.14)
        yield from bps.mv(att1_9, 'Insert')
        yield from bps.sleep(1)
        yield from bps.mv(att1_9, 'Insert')
        
        yield from bps.mv(prs, 20)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)   
            dets = [pil1M, pil300KW]

            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, th_hexa + ais)

                x_list = [-700, -500, -300, -100, 100, 300, 500, 700]
                for pos, xss in enumerate(x_list):
                    yield from bps.mv(piezo.x, xs + xss)
                    det_exposure_time(t,t) 
                    name_fmt = '{sample}_aiscan_14keV_ai{ai}_pos{pos}_prs{prs}_wa{wax}'
                    sample_name = name_fmt.format(sample=name, ai ='%4.3f'%ais, pos ='%2.2d'%pos, prs='00', wax = wa)
                    sample_id(user_name='GF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)


        yield from bps.mv(prs, -70)
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)   
            dets = [pil1M, pil300KW]

            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, th_hexa + ais)
                yield from bps.mv(piezo.x, xs)
                det_exposure_time(t,t) 
                name_fmt = '{sample}_aiscan_14keV_ai{ai}_pos{pos}_prs{prs}_wa{wax}'
                sample_name = name_fmt.format(sample=name, ai ='%4.3f'%ais, pos ='00', prs='90', wax = wa)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

        
        yield from bps.mv(prs, -70)
        yield from bps.mv(stage.th, th_hexa + 0.15)
        prs_list = np.linspace(-70, 20, 46)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)   
            dets = [pil1M, pil300KW]

            for k, prss in enumerate(prs_list):
                yield from bps.mv(prs, prss)
                yield from bps.mv(piezo.x, xs)
                det_exposure_time(t,t) 
                name_fmt = '{sample}_prsscan_14keV_ai{ai}_pos{pos}_prs{prs}_wa{wax}'
                sample_name = name_fmt.format(sample=name, ai ='0.15', pos ='00', prs='%2.2d'%prss, wax = wa)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

        yield from bps.mv(prs, 20)
        yield from bps.mv(stage.th, th_hexa + 0.2)
        prs_list = np.linspace(20, -70, 46)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)   
            dets = [pil1M, pil300KW]

            for k, prss in enumerate(prs_list):
                yield from bps.mv(prs, prss)
                yield from bps.mv(piezo.x, xs)
                det_exposure_time(t,t) 
                name_fmt = '{sample}_prsscan_14keV_ai{ai}_pos{pos}_prs{prs}_wa{wax}'
                sample_name = name_fmt.format(sample=name, ai ='0.20', pos ='00', prs='%2.2d'%prss, wax = wa)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

        det_exposure_time(0.3,0.3) 
        sample_id(user_name='test', sample_name='test')




def giwaxs_S_edge_Pete(t=1):
    dets = [pil1M, pil300KW]
    
    # names = ['100_DDP_0deg','100_DDP_90deg','75_DDP_0deg''75_DDP_90deg','50_DDP_0deg','50_DDP_90deg','25_DDP_0deg','25_DDP_90deg']
    # x = [-48098, -29098, -21098, -2098, 9901, 52901, 28901, 39900 ]
    # z = [5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000]

    names = ['50_DDP_0deg','50_DDP_90deg','25_DDP_0deg','25_DDP_90deg']
    x = [3902, 16902, 34902,  45902]
    z = [5000, -5000, 5000, -5000]

    energies = [2450.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    waxs_arc = [15, 0]
    
    ai0 = 0
    ai_list = [0.3, 0.5, 0.8]

    for name, xs, zs in zip(names, x, z):
        print(zs)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, ai0)

        yield from alignement_special(angle = 0.15)
        
        ai0 = piezo.th.position

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)   

            if i == 0:
                dets = [pil1M, pil300KW]
                yield from bps.mv(att2_9, 'Insert')
                yield from bps.sleep(1)
                yield from bps.mv(att2_9, 'Insert')
            
            else:
                dets = [pil300KW]
                yield from bps.mv(att2_9, 'Insert')
                yield from bps.sleep(1)
                yield from bps.mv(att2_9, 'Insert')


            for k, ais in enumerate(ai_list):

                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*400)

                det_exposure_time(t,t) 
                name_fmt = '{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='GF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mv(energy, 2490)
                yield from bps.mv(energy, 2470)
                yield from bps.mv(energy, 2450)



def giwaxs_ai_S_edge_Pete(t=1):
    dets = [pil1M, pil300KW]
    
    names = ['75_DDP_0deg','75_DDP_90deg','50_DDP_0deg','50_DDP_90deg','25_DDP_0deg','25_DDP_90deg']
    x = [ -22098, -8098, 4902, 17902, 35902,  46902]
    z = [ 5000, -5000, 5000, -5000, 5000, -5000]

    energies = [2450.0, 2477.0, 2510.0]
    waxs_arc = [15, 0]
    
    ai0 = 0
    ai_list = np.arange(0.3, 0.44, 0.05).tolist() + np.arange(0.45, 0.6, 0.01).tolist() + np.arange(0.6, 1, 0.025).tolist() 
    ai_list = [round(1000*x, 4) for x in ai_list] 
    ai_list = np.asarray(ai_list)/1000

    dets = [pil1M, pil300KW]
    
    for name, xs, zs in zip(names, x, z):
        print(zs)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, ai0)

        yield from alignement_special(angle = 0.15)
        
        ai0 = piezo.th.position

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)   

            if i == 0:
                dets = [pil1M, pil300KW]
                yield from bps.mv(att2_9, 'Insert')
                yield from bps.sleep(1)
                yield from bps.mv(att2_9, 'Insert')
            
            else:
                dets = [pil300KW]
                yield from bps.mv(att2_9, 'Insert')
                yield from bps.sleep(1)
                yield from bps.mv(att2_9, 'Insert')


            for k, ais in enumerate(ai_list):

                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + k*200)

                det_exposure_time(t,t) 
                name_fmt = '{sample}_aiscan_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}'
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(0.5)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='GF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mv(energy, 2490)
                yield from bps.mv(energy, 2470)
                yield from bps.mv(energy, 2450)


def nexafs_S_edge_Pete(t=1):

    yield from bps.mv(waxs, 52.5)   
    dets = [pil300KW]
    
    names = ['100_DDP_0deg_vertically_ai0.5deg']
    x = [-52000]
    z = [-5000]

    energies = [2450.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5,
    2480.0, 2480.5, 2483.0, 2485.0, 2490.0, 2495.0, 2500.0, 2510.0]
    
    for name, xs in zip(names, x):
        #yield from bps.mv(piezo.x, xs)

        yield from bps.mv(att2_9, 'Retract')
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)
        yield from bps.mv(att2_9, 'Retract')
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)

        # yield from bps.mv(piezo.th, 1.5)

        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_wa52.5_bpm{xbpm}'
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(0.5)
            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, xbpm = '%4.3f'%bpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)


        yield from bps.mv(energy, 2490)
        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2450)
