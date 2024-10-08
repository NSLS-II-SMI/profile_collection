def measure(det=[pil1M], sample='test',  t=1):
    det_exposure_time(t, t)
    sample_name = "{sample}".format(sample=sample)
    sample_id(user_name="JK", sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    yield from bp.count(det, num=1)


def cd_saxs(th_ini, th_fin, th_st, exp_t=1, sample='test', nume=1, det=[pil1M]):
    det_exposure_time(exp_t, exp_t)

    for num, theta in enumerate(np.linspace(th_ini, th_fin, th_st)):
        yield from bps.mv(prs, theta)
        name_fmt = "{sample}_5.2m_16.1keV_num{num}_{th}deg_bpm{bpm}"
        sample_name = name_fmt.format(sample=sample, num="%2.2d"%num, th="%2.2d"%theta, bpm="%1.3f"%xbpm3.sumX.get())
        sample_id(user_name="JK", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(det, num=nume)



def cdsaxs_2024_1(t=1):
    det = [pil1M]
    det_exposure_time(t, t)

    phi_offest = -2


    # names = [ 'C5b-L60p120']
    # x =     [   20800]
    # x_hexa =[     0.3]
    # y=      [    -3400]
    # z=      [    -1200]
    # chi=    [    0.6]
    # th =    [  5.75]

    # names = [ 'H5b-L52p104', 'E4b-L52p104', 'C5-L50p100', 'C5-L52p104', 'C5-L55p110', 'C5-L60p120']
    # x =     [   8550, -24350,       24400, 23500, 22600, 21700]
    # x_hexa =[     0.3, 0.3,         0.3, 0.3, 0.3, 0.3]
    # y=      [    -3250, -4100,      -3400, -3400, -3400, -3400]
    # z=      [    -550, 550,         -1200, -1200, -1200, -1200]
    # chi=    [    -0.5, 0.1,         0.6, 0.6, 0.6, 0.6]
    # th =    [  5.35, 5.85,          5.75, 5.75, 5.75, 5.75]

    names = [ 'B305-L50p100', 'B305-L52p104', 'B305-L55p110', 'B305-L57p115', 'B305-L60p120']
    x =     [   -350, 550, 1450, 2350, 3250]
    x_hexa =[     0.3,  0.3,    0.3, 0.3,  0.3]
    y=      [    3450, 3450, 3450, 3450, 3450]
    z=      [    -4600, -4600, -4600, -4600, -4600]
    chi=    [    -1.6, -1.6, -1.6, -1.6, -1.6]
    th =    [  3.5, 3.5, 3.5, 3.5, 3.5]

    # names = [ 'F11-L60P120V', 'F11-L80P160V']
    # x =     [   15200, 16100]
    # x_hexa =[     0.3 , 0.3]
    # y=      [    650, 650]
    # z=      [    -4800, -4800]
    # chi=    [    -0.1, -0.1]
    # th =    [  5.5, 5.5]




    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"

    for i in range(1):
        for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
            yield from bps.mv(stage.x, xs_hexa)
            # yield from bps.mv(stage.y, ys_hexa)

            yield from bps.mv(piezo.z, zs)
            yield from bps.mv(piezo.ch, chis)
            yield from bps.mv(piezo.th, ths)
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            # yield from bp
            yield from cd_saxs(phi_offest, phi_offest, 1, exp_t=t, sample=name+'measure_ref-A%s'%(i+1), nume=1)
            yield from cd_saxs(-60+phi_offest, 60+phi_offest, 121, exp_t=t, sample=name+'measure%s'%(i+1), nume=1)
            yield from cd_saxs(phi_offest, phi_offest, 1, exp_t=t, sample=name+'measure_ref-B%s'%(i+1), nume=1)








def cd_gisaxs(t=1):
    prs_offset = -1.854

    det = [pil1M]
    det_exposure_time(t, t)

    names = ['sam2_g1',  'sam2_g2',  'sam2_g3',  'sam2_g4', 'sam2_g5', 'sam2_g6']
    x =     [   -29300,     -35300,     -21300,     -17300,     -13300,    -9300]
    x_hexa =[     0.20,       0.20,       0.20,       0.20,       0.20,     0.20]
    y=      [     6900,       6900,       6900,       6900,       6900,     6900]
    y_hexa =[      0.0,        0.0,        0.0,        0.0,        0.0,      0.0]
    z=      [      200,        200,        200,        200,        200,      200]
    chi=    [   -1.055,     -1.055,     -1.055,     -1.055,     -1.055,   -1.055]
    th =    [  -0.7229,    -0.7229,    -0.7229,    -0.7229,    -0.7229,  -0.7229]

    names = ['sam2_g2',  'sam2_g3',  'sam2_g4', 'sam2_g5', 'sam2_g6']
    x =     [   -25300,     -21300,     -17300,     -13300,    -9300]
    x_hexa =[     0.20,       0.20,       0.20,       0.20,     0.20]
    y=      [     6900,       6900,       6900,       6900,     6900]
    y_hexa =[      0.0,        0.0,        0.0,        0.0,      0.0]
    z=      [      200,        200,        200,        200,      200]
    chi=    [   -1.055,     -1.055,     -1.055,     -1.055,   -1.055]
    th =    [  -0.7229,    -0.7229,    -0.7229,    -0.7229,  -0.7229]

    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"

    for name, xs, xs_hexa, ys, ys_hexa, zs, chis, ths in zip(names, x, x_hexa, y, y_hexa, z, chi, th):
        yield from bps.mv(prs, prs_offset)
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(stage.y, ys_hexa)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)
        yield from bps.mv(piezo.th, ths)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yield from alignement_gisaxs_hex(0.1)
        
        ai0=stage.th.position

        for num, ai in enumerate([0.15, 0.20, 0.30, 0.50]):
            if ai == 0.15:
                    yield from bps.mv(att1_5.open_cmd, 1)
                    yield from bps.mv(att1_6.open_cmd, 1)
                    yield from bps.sleep(2)
                    yield from bps.mv(att1_5.open_cmd, 1)
                    yield from bps.mv(att1_6.open_cmd, 1)
            else:
                    yield from bps.mv(att1_5.close_cmd, 1)
                    yield from bps.mv(att1_6.open_cmd, 1)
                    yield from bps.sleep(2)
                    yield from bps.mv(att1_5.close_cmd, 1)
                    yield from bps.mv(att1_6.open_cmd, 1)       

            yield from bps.mv(stage.th, ai0+ai)
            
            for num1, phi in enumerate(np.concatenate([np.linspace(-5, -1.02, 200), np.linspace(-1, 1, 401), np.linspace(1.02, 5, 200)])):
                yield from bps.mv(prs, prs_offset+phi)

                name_fmt = "{sample}_9.2m_16.1keV_phi{phii}deg_ai{aii}deg"
                sample_name = name_fmt.format(sample=name, num="%2.2d"%num1, phii="%1.3f"%phi, aii="%1.2f"%ai)
                sample_id(user_name="KY_GI", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(det, num=1)



    prs_offset = -3.337
    names = ['sam1_g1',  'sam1_g2',  'sam1_g3',  'sam1_g4', 'sam1_g5', 'sam1_g6']
    x =     [    42700,      38700,      34700,      30700,      26700,    22700]
    x_hexa =[     0.20,       0.20,       0.20,       0.20,       0.20,     0.20]
    y=      [     6900,       6900,       6900,       6900,       6900,     6900]
    y_hexa =[      0.0,        0.0,        0.0,        0.0,        0.0,      0.0]
    z=      [      200,        200,        200,        200,        200,      200]
    chi=    [   -1.055,     -1.055,     -1.055,     -1.055,     -1.055,   -1.055]
    th =    [  -0.7229,    -0.7229,    -0.7229,    -0.7229,    -0.7229,  -0.7229]

    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"

    for name, xs, xs_hexa, ys, ys_hexa, zs, chis, ths in zip(names, x, x_hexa, y, y_hexa, z, chi, th):
        yield from bps.mv(prs, prs_offset)

        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(stage.y, ys_hexa)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)
        yield from bps.mv(piezo.th, ths)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yield from alignement_gisaxs_hex(0.1)
        ai0=stage.th.position

        for num, ai in enumerate([0.15, 0.20, 0.30, 0.50]):
            if ai == 0.15:
                    yield from bps.mv(att1_5.open_cmd, 1)
                    yield from bps.mv(att1_6.open_cmd, 1)
                    yield from bps.sleep(2)
                    yield from bps.mv(att1_5.open_cmd, 1)
                    yield from bps.mv(att1_6.open_cmd, 1)
            else:
                    yield from bps.mv(att1_5.close_cmd, 1)
                    yield from bps.mv(att1_6.open_cmd, 1)
                    yield from bps.sleep(2)
                    yield from bps.mv(att1_5.close_cmd, 1)
                    yield from bps.mv(att1_6.open_cmd, 1)       

            yield from bps.mv(stage.th, ai0+ai)
            
            for num1, phi in enumerate(np.concatenate([np.linspace(-5, -1.02, 200), np.linspace(-1, 1, 401), np.linspace(1.02, 5, 200)])):
                yield from bps.mv(prs, prs_offset+phi)

                name_fmt = "{sample}_9.2m_16.1keV_phi{phii}deg_ai{aii}deg"
                sample_name = name_fmt.format(sample=name, num="%2.2d"%num1, phii="%1.3f"%phi, aii="%1.2f"%ai)
                sample_id(user_name="KY_GI", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(det, num=1)