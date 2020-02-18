def waxs_S_edge_zhang(t=2):
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

