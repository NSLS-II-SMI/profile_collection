
def new_folder(cycle, group):
    proposal_id(cycle, group)


def song_waxs_S_edge_new(t=1):
    dets = [pil300KW]

    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1 )

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 13, 3)

    yield from bps.mv(stage.th, 1)
    yield from bps.mv(stage.y, -8)
    names = ['C2C8C10_2_0per_2','C2C8C10_20per_2','C2C8C10_40per_2']
    x = [-29200, -34900, -40500]
    y = [-8470, -8620, -9240]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 620, 15)
        xss = np.linspace(xs, xs + 1000, 4)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def song_waxs_new(t=1):
    dets = [pil300KW, pil1M]

    # yield from bps.mv(GV7.close_cmd, 1 )
    # yield from bps.sleep(5)
    # yield from bps.mv(GV7.close_cmd, 1 )

    waxs_arc = np.linspace(0, 13, 3)
    del_y = [-100, 0, 100]

    # yield from bps.mv(stage.th, 1)
    # yield from bps.mv(stage.y, -8)
    names = ['C2C6C8_0per','C2C6C8_20per','C2C6C8_40per','C2C6C8_60per','C2C6C8_80per','C2C8C10_0per','C2C8C10_20per','C2C8C10_40per','C2C8C10_60per','C2C8C10_80per',
    'C2C8C10_100per','C2C10C12_0per','C2C10C12_20per','C2C10C12_40per','C2C10C12_60per','C2C10C12_80per','C2C10C12_100per']
    x = [43200, 38200, 33200, 27200, 21900, 16900, 11700, 6700, 1700, -3200, -9000,-14000,-19000,-24000,-29000,-34000,-40000]
    y = [-8500, -8500, -8500, -8500, -8300, -8500, -8500,-8500,-8700, -8300, -8800, -8500, -8500, -8500, -8500, -8700, -8800]

    names = ['bkg_vac']
    x = [-10500]
    y = [-3000]


    for wa, de_y in zip(waxs_arc, del_y):
        yield from bps.mv(waxs, wa)
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
           
            det_exposure_time(t,t) 
            name_fmt = '{sample}_10_16100eV_wa{wax}_bpm{xbpm}'

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%4.3f'%bpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    # yield from bps.mv(stage.y, 0)
    # yield from bps.mv(stage.th, 0)
    # names = ['C2C12C14_0per','C2C12C14_20per','C2C12C14_40per','C2C12C14_60per','C2C12C14_80per']
    # x = [44100, 4100, -100, -5100, -16100]
    # y = [-3000,-4000,-4000, -4000, -4000]

    # for wa, de_y in zip(waxs_arc, del_y):
    #     yield from bps.mv(waxs, wa)
    #     for name, xs, ys in zip(names, x, y):
    #         yield from bps.mv(piezo.x, xs)
    #         yield from bps.mv(piezo.y, ys+de_y)
          
    #         det_exposure_time(t,t) 
    #         name_fmt = '{sample}_8_16100eV_wa{wax}_bpm{xbpm}'

    #         bpm = xbpm2.sumX.value

    #         sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%4.3f'%bpm)
    #         sample_id(user_name='GF', sample_name=sample_name)
    #         print(f'\n\t=== Sample: {sample_name} ===\n')
    #         yield from bp.count(dets, num=1)

def waxs_zhang(t=2):
    dets = [pil300KW]

    names = ['F1bd','C1bd']
    x = [-2000, -12000]
    y = [1500, 1500]

    
    #energies = np.linspace(2450, 2500, 26)
    waxs_arc = [0]
    
    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
                
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_16100.00eV_wa{wax}_bpm{xbpm}'

            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%4.3f'%bpm)
            sample_id(user_name='SZ', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            
            yield from bp.count(dets, num=50)


def mapping_S_edge_zhang(t=2):
    dets = [pil300KW, pil1M]
    
    names = ['F3map','C4map']
    xx = [19200, 8800]
    yy = [600, 600]
    

    for x, y, name in zip(xx, yy, names):

        ys = np.linspace(y, y + 1800, 37)
        xs = np.linspace(x, x - 3000, 16)
        
        #energies = [2450, 2474, 2478, 2500]
        waxs_arc = [0]
        
        yss, xss = np.meshgrid(ys, xs)
        yss = yss.ravel()
        xss = xss.ravel()

      #  for e in energies: 
      #      yield from bps.mv(energy, e)
      #      yield from bps.sleep(5)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            for pos, (xsss, ysss) in enumerate(zip(xss, yss)):
                yield from bps.mv(piezo.x, xsss)
                yield from bps.mv(piezo.y, ysss)

                det_exposure_time(t,t)
                name_fmt = '{sample}_16100eV_wa{wax}_bpm{xbpm}_pos{posi}'
                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, wax = wa, xbpm = '%4.3f'%bpm, posi = '%3.3d'%pos)
                sample_id(user_name='SZ', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

       # yield from bps.mv(energy, 2470)
       # yield from bps.mv(energy, 2450)



def nightplan_S_edge_zhang(t=2):
    #yield from waxs_S_edge_zhang(t=2)
    #yield from bps.sleep(10)
    yield from mapping_S_edge_zhang(t=2)

