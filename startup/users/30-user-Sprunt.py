   
def waxs_S_edge_cherun(t=1):
    
    dets = [pil300KW, pil1M]
    
    # yield from bps.mv(stage.th, 0)
    # yield from bps.mv(stage.y, 6)
    # names = ['bar1_sa01_2','bar1_sa02_2','bar1_sa03_2','bar1_sa04_2','bar1_sa05_2','bar1_sa06_2','bar1_sa07_2','bar1_sa08_2'
    # ,'bar1_sa09_2','bar1_sa10_2','bar1_sa11_2','bar1_sa12_2','bar1_sa13_2','bar1_sa14_2']
    
    # x = [51700,43700,35700,27700,19600,11700,4700,-4200,-12200,-20200,-28200,-36200,-44200,-52200] 
    # y = [7600, 7600, 7900, 7900, 7900, 8200, 8771, 8900, 8300, 8700,  8800,  9100,  9300,  9400]
    


    # energies = np.arange(2450, 2476, 5).tolist() + np.arange(2476, 2486, 0.5).tolist() + np.arange(2486, 2496, 2).tolist()+ np.arange(2496, 2511, 5).tolist()
    # waxs_arc = np.linspace(6.5, 13, 2)

    # for wa in waxs_arc:
    #     yield from bps.mv(waxs, wa)    
    #     for name, xs, ys in zip(names, x, y):
    #         yield from bps.mv(piezo.x, xs)
    #         yield from bps.mv(piezo.y, ys)

    #         # yss = np.linspace(ys, ys + 380, 20)
    #         # xss = np.array([xs, xs + 250, xs + 500])

    #         # yss, xss = np.meshgrid(yss, xss)
    #         # yss = yss.ravel()
    #         # xss = xss.ravel()

    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
    #         for e in energies: 
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(1)

    #             # yield from bps.mv(piezo.y, ysss)
    #             # yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
    #             sample_id(user_name='GF', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)
           
    #         yield from bps.mv(energy, 2490)
    #         yield from bps.mv(energy, 2470)
    #         yield from bps.mv(energy, 2450)

    # yield from bps.mv(stage.th, 0)
    # yield from bps.mv(stage.y, 0)

    # names = ['bar2_sa01','bar2_sa02','bar2_sa03','bar2_sa04','bar2_sa05','bar2_sa06','bar2_sa07','bar2_sa08','bar2_sa09'
    # ,'bar2_sa10','bar2_sa11','bar2_sa12','bar2_sa13','bar2_sa14']
    # x = [51800,43300,35200,27300,19200,11800,3300,-4600,-12600,-20600, -28600, -36600, -44600, -52600] 
    # y = [3500, 3600, 3700, 3800, 4100, 4800, 4400, 4800, 4900,  5000,   5100,   5500,   5500,  5500]


    # energies = np.arange(2450, 2476, 5).tolist() + np.arange(2476, 2486, 1).tolist() + np.arange(2486, 2496, 3).tolist()+ np.arange(2496, 2511, 5).tolist()
    # waxs_arc = np.linspace(0, 13, 3)

    # for wa in waxs_arc:
    #     yield from bps.mv(waxs, wa)    
    #     for name, xs, ys in zip(names, x, y):
    #         yield from bps.mv(piezo.x, xs)
    #         yield from bps.mv(piezo.y, ys)

    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
    #         for e in energies: 
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(1)

    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
    #             sample_id(user_name='GF', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)
           
    #         yield from bps.mv(energy, 2490)
    #         yield from bps.mv(energy, 2470)
    #         yield from bps.mv(energy, 2450)

    # yield from bps.mv(stage.th, 0)
    # yield from bps.mv(stage.y, 0)
    # names = ['bar3_sa01','bar3_sa02','bar3_sa03','bar3_sa04','bar3_sa05','bar3_sa06','bar3_sa07','bar3_sa08','bar3_sa09'
    # ,'bar3_sa10','bar3_sa11','bar3_sa12','bar3_sa13','bar3_sa14']
    # x = [51800,43600,35900,27900,19600,11800,4000, -4100, -12100, -20100,-28100,-36400,-44100,-52100] 
    # y = [-7300,-7100,-7100,-6900,-6700,-6500,-6000,-6200, -6000,  -5800, -5600, -5300, -5200, -4900]

    names = ['bar3_sa07_2']
    x = [4000] 
    y = [-5000]

    energies = np.arange(2450, 2476, 5).tolist() + np.arange(2476, 2486, 1).tolist() + np.arange(2486, 2496, 3).tolist()+ np.arange(2496, 2511, 5).tolist()
    waxs_arc = np.linspace(0, 32.5, 6)


    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)

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
           
            yield from bps.mv(energy, 2490)
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)
    



def nexafs_S_edge_cherun(t=1):

    yield from bps.mv(waxs, 52.5)   
    dets = [pil300KW]
    
    names = ['bar1_sa03.5deg']

    energies = np.arange(2460, 2521, 1).tolist()
    energies = np.arange(2450, 2476, 5).tolist() + np.arange(2476, 2486, 0.25).tolist() + np.arange(2486, 2496, 1).tolist()+ np.arange(2496, 2511, 5).tolist()

    
    for name in (names):

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
