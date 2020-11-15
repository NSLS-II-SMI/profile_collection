def saxs_waxs_yuchung(t=1):
    dets = [pil300KW, pil1M]

    # waxs_arc = np.linspace(13, 26, 3)

    # yield from bps.mv(stage.y, 0)
    # yield from bps.mv(stage.th, 0)

    # names = ['20H-5', '12H-5', '8H-5', '9010_F1200', '9010_F7200',]
    # x = [-39000, -12500, -2500, 23500, 41500]
    # y = [ 1200,    1200,  1200,  1100,  1300]
    # z = [  1000,   1000,  1000,  1000,  1000]
    # det_exposure_time(t,t) 

    # for wa in waxs_arc:
    #     yield from bps.mv(waxs, wa)    
        
    #     for name, xs, ys, zs in zip(names, x, y, z):
    #         yield from bps.mv(piezo.x, xs)
    #         yield from bps.mv(piezo.y, ys)
    #         yield from bps.mv(piezo.z, zs)

    #         xss = np.linspace(xs - 500, xs + 500, 3)
    #         yss = np.linspace(ys - 500, ys + 500, 51)
    #         yss, xss = np.meshgrid(yss, xss)
    #         yss = yss.ravel()
    #         xss = xss.ravel()

    #         name_fmt = '{sample}_16100eV_sdd8.3_wa{wax}'
    #         sample_name = name_fmt.format(sample=name, wax = wa)
    #         sample_id(user_name='GF', sample_name=sample_name)
    #         print(f'\n\t=== Sample: {sample_name} ===\n')
    #         yield from bp.list_scan(dets, piezo.x, xss.tolist() , piezo.y, yss.tolist())


    waxs_arc = np.linspace(0, 26, 5)

    yield from bps.mv(stage.th, 1.5)
    yield from bps.mv(stage.y, -8)
    names = ['99PL_1PP', '99.75_PLA0.25PP', '75PP25PS']
    x = [-20000, 4000, 21000]
    y = [ -8900,-8900, -9380]
    z = [  3000, 3000,  3000]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        
        for name, xs, ys, zs in zip(names, x, y, z):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            yield from bps.mv(piezo.z, zs)

            xss = np.linspace(xs - 500, xs + 500, 3)
            yss = np.linspace(ys - 500, ys + 500, 51)
            yss, xss = np.meshgrid(yss, xss)
            yss = yss.ravel()
            xss = xss.ravel()

            name_fmt = '{sample}_16100eV_sdd8.3_wa{wax}'
            sample_name = name_fmt.format(sample=name, wax = wa)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.list_scan(dets, piezo.x, xss.tolist() , piezo.y, yss.tolist())
