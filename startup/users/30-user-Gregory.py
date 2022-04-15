def waxs_S_edge_Gregory_2022_1(t=0.5):
    """
    Based on waxs_S_edge_gordon_2021_2 from 30-user-Gordon
    and modified for GU-309504 Gregory. SAXS ssd 1.6 m.
    """
    dets = [pil1M, pil900KW]

    # x and y are top left position on the sample
    names_a = ['1-P3RT_doped', '2-P3RTe_doped', '3-blend_doped', '4-copolymer_doped']
    x_a = [             34225,           28275,           21525,               15375]
    y_a = [              -250,            -175,            -175,                 -75]
    
    names_b = ['5-P3RT_undoped', '6-P3RTe_undoped', '7-blend_undoped', '8-copolymer_undoped', '9-control_empty']
    x_b = [                5625,              -425,             -6825,                -13345,            -21225]
    y_b = [                -100,              -125,              -275,                  -255,              -175]

    names = names_a + names_b
    x = x_a + x_b
    y = y_a + y_b

    # Move all x values by + xxx um to be at the centre in x
    x = (np.array(x) + 600).tolist()
    y = (np.array(y) - 50).tolist()

    # Energies for sulphur
    #energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    
    # Energies for chlorine
    energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 5).tolist() + np.arange(2850, 2910, 10).tolist()
    waxs_arc = np.linspace(0, 40, 3)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        # Cover a range of 1 mm in y to avoid damage
        yss = np.linspace(ys, ys + 1000, 62)
        # Stay at the same x position
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            # Do not read SAXS if WAXS is in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            det_exposure_time(t,t)

            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.get()

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='AA', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)

            # Go back gently with energy
            #yield from bps.mv(energy, 2470)
            #yield from bps.mv(energy, 2450)
            yield from bps.mv(energy, 2870)
            yield from bps.mv(energy, 2840)
