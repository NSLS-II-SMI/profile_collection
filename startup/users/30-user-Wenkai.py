def giwaxs_S_edge_wenkai(t=1):
    dets = [pil300KW]
    


    
    names = [ 'A2', 'A3', 'A4', 'A5', 'A6']
    x = [30000, 16000, 0, -15000, -36000]

    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 26, 5)
    ai0 = 0

    for name, xs in zip(names, x):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.th, ai0)

        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)        
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.sleep(1)

        yield from alignement_gisaxs(angle = 0.4)
        
        # yield from bps.mv(att2_9, 'Insert')
        yield from bps.mv(GV7.close_cmd, 1 )
        yield from bps.sleep(1)
        # yield from bps.mv(att2_9, 'Insert')
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


def nexafs_S_edge_wenkai(t=1):
    dets = [pil300KW]
    names = ['A1_1']
    x = [48000]

    #energies = np.linspace(2450, 2500, 51)

    energies = np.arange(2450, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()

    for name, xs in zip(names, x):

        det_exposure_time(t,t) 
        name_fmt = 'nexafs_{sample}_{energy}eV_wa39.00_bpm{xbpm}'
        for e in energies: 
            yield from bps.mv(energy, e)
            yield from bps.sleep(2)

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, xbpm = '%4.3f'%bpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    
        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2450)