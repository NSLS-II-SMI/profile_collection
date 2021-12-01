

def nexafs_S_edge(t=1):
    dets = [pil900KW]    
    #prs 0 deg
    names = ['BPI_20nm_LCE', 'cholesteric_film_20nm']
    x = [-6000, -17000]
    y = [-4100, -4900]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = [40]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = 'nexafs_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e in energies:

                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def S_edge_SAXSWAXS_2021_3(t=1):
    dets = [pil900KW, pil1M]

    names = ['cholesteric_film_20nm']#'BPI_20nm_LCE']#
    x = [-15900]#, -5900]
    y = [-5000]#, -5600]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 200, 20)
        xss = np.array([xs, xs+200, xs+400])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t)

            name_fmt = '{sample}_sdd5m_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)
