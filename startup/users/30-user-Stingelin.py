
def Cl_edge_nexafs_2024_1_surfactant(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)

    # bottom left first
    names = ['nexafs_test']             
    x_piezo = [      13000]
    x_hexa = [           0]
    y_piezo = [       7000]
    z_piezo = [      -3000]
    
    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"



    energies = -10 + np.asarray([2810.0, 2820.0, 2828.0, 2829.0, 2830.0, 2831.0, 2832.0, 2833.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    # energies = np.linspace(2820, 2860, 41)

    waxs_arc = [0]
    ai0_all = 0
    ai_list = [1.6]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="NS", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


            yield from bps.mv(piezo.th, ai0)




def Cl_edge_measurments_2024_1_surfactant(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)

    # names = ['Cl_12_PS', 'Cl_14_PS', 'Cl_16_PS']             
    # x_piezo = [   13000,        570,      -7430]
    # x_hexa = [        0,          0,          0]
    # y_piezo = [    7000,       7000,       7000]
    # z_piezo = [   -3000,      -3000,      -3000]

    # names = [      'PS', 'FS1_PBTTT_C14', 'FS3_PBTTT_C16', 'FS52_PBTTTC14_C', 'FS11_Cl12_PS','FS12_Cl14_PS', 'FS13_Cl16_PS', 'FS61_PBTTTC14_Cl12','FS54_PBTTTC14_Cl14','FS62_PBTTTC14_Cl16','FS63_PBTTTC16_Cl14','FS64_PBTTTC16_Cl16']             
    # x_piezo = [   55000,           55000,             44000,           33000,          22000,         12500,            500,               -10500,              -22200,              -33200,              -45200,              -45000]
    # x_hexa = [       11,               0,                 0,               0,              0,             0,              0,                    0,                   0,                   0,                   0,                 -12]
    # y_piezo = [    7000,            7000,              7000,            7000,           7000,          7000,           7000,                 7000,                7000,                7000,                7000,                7000]
    # z_piezo = [   -3000,           -3000,             -3000,           -3000,          -3000,         -3000,          -3000,                -3000,               -3000,               -3000,               -3000,               -3000]
    
    names = [' P3HT1500',        'PVC1000',      'IL5_C12mimCl',  'IL7_PBTTTC14',      'IL8_PBTTTC16', 'IL21_PBTTTC14_C12mimCl_3_1']             
    x_piezo = [    55000,            54000,               43000,           33000,               18000,                       -49000]
    x_hexa = [        13,                0,                   0,               0,                   0,                           -1]
    y_piezo = [     6600,             6600,                6700,            6800,                6800,                         7500]
    z_piezo = [    -3000,            -3000,               -3000,           -3000,               -3000,                        -3000]
       

    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    energies = -10 + np.asarray([2810.0, 2820.0, 2828.0, 2829.0, 2830.0, 2831.0, 2832.0, 2833.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    waxs_arc = [0, 20]
    ai0_all = 0
    ai_list = [1.6]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, -2000+xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        # yield from bps.mv(att2_9.open_cmd, 1)
        # yield from bps.sleep(1)
        # yield from bps.mv(att2_9.open_cmd, 1)
        # yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="NS", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


            yield from bps.mv(piezo.th, ai0)




def S_edge_measurments_2024_1_surfactant(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)

    names = [      'PS', 'FS1_PBTTT_C14', 'FS3_PBTTT_C16', 'FS52_PBTTTC14_C',  'FS61_PBTTTC14_Cl12','FS54_PBTTTC14_Cl14','FS62_PBTTTC14_Cl16','FS63_PBTTTC16_Cl14','FS64_PBTTTC16_Cl16']             
    x_piezo = [   55000,           55000,             44000,           33000,                -10500,              -22200,              -33200,              -45200,              -45000]
    x_hexa = [       11,               0,                 0,               0,                     0,                   0,                   0,                   0,                 -12]
    y_piezo = [    7000,            7000,              7000,            7000,                  7000,                7000,                7000,                7000,                7000]
    z_piezo = [   -3000,           -3000,             -3000,           -3000,                 -3000,               -3000,               -3000,               -3000,               -3000]

    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    energies = [2450.0,2455.0,2460.0,2465.0,2470.0,2473.0,2475.0,2475.5,2476.0,2476.5,2477.0,2477.5,2478.0,2478.5,2479.0,2479.5,
    2480.0,2480.5,2481.0,2482.0,2483.0,2484.0,2485.0,2486.0, 2487.0,2488.0,2489.0,2490.0,2492.5,2495.0,2500.0,2510.0,2515.0]


    waxs_arc = [0, 20]
    ai0_all = 0
    ai_list = [1.6]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        # yield from bps.mv(att2_9.open_cmd, 1)
        # yield from bps.sleep(1)
        # yield from bps.mv(att2_9.open_cmd, 1)
        # yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
       
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="NS", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


            yield from bps.mv(piezo.th, ai0)


def S_edge_measurments_2024_1_ILs(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)

    # names = [' P3HT1500',        'PVC1000',      'IL5_C12mimCl',  'IL7_PBTTTC14',      'IL8_PBTTTC16', 'IL16_PBTTTC14_C14mim_1_1','IL17_PBTTTC14_C14mim_1_3','IL18_PBTTTC14_C16mim_3_1','IL19_PBTTTC14_C16mim_1_1', 'IL20_PBTTTC14_C16mim_1_3','IL21_PBTTTC14_C12mimCl_3_1', 'IL22_PBTTTC14_C12mimOTrf_1_1']             
    # x_piezo = [    55000,            54000,               43000,           33000,               18000,                       9000,                         0,                    -9000,                    -26000,                     -38000,                     -49000,                    -49000]
    # x_hexa = [        13,                0,                   0,               0,                   0,                          0,                         0,                        0,                         0,                          0,                         -1,                       -14]
    # y_piezo = [     6600,             6600,                6700,            6800,                6800,                       6900,                      6800,                     7000,                      7300,                       7300,                       7500,                      7700]
    # z_piezo = [    -3000,            -3000,               -3000,           -3000,               -3000,                      -3000,                     -3000,                    -3000,                     -3000,                      -3000,                      -3000,                     -3000]
       
    # names = ['IL1_C8mim_NEXAFS'] 
    # x_piezo = [    55000] 
    # x_hexa = [        12] 
    # y_piezo = [     6040] 
    # z_piezo = [    -3000]

    # names = [      'IL5_C12mimCl_rerun',  'IL17_PBTTTC14_C14mim_1_3_rerun']             
    # x_piezo = [                   41000,                             -1750]
    # x_hexa = [                        0,                                 0]
    # y_piezo = [                    6700,                              7100]
    # z_piezo = [                   -3000,                             -3000]
       
    names = ['IL24_PBTTTC16_C16mim_1_1', 'IL23_PBTTTC16_C12mim_1_1', 'FS64_PBTTTC16_Cl16']             
    x_piezo = [                   54000,                      41000,                29000]
    x_hexa = [                        0,                          0,                    0]
    y_piezo = [                    6600,                       6700,                 6700]
    z_piezo = [                   -3000,                      -3000,                -3000]

    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    energies = [2450.0,2455.0,2460.0,2465.0,2470.0,2473.0,2475.0,2475.5,2476.0,2476.5,2477.0,2477.5,2478.0,2478.5,2479.0,2479.5,
    2480.0,2480.5,2481.0,2481.5,2482.0,2482.5,2483.0,2483.5,2484.0,2484.5,2485.0,2485.5,2486.0,2487.0,2488.0,2489.0,2490.0,2491.0,2492.5,2495.0,2500.0,2510.0,2515.0]

    # energies = np.linspace(2470,2510,41)

    waxs_arc = [0, 20]
    ai0_all = 0
    ai_list = [1.6]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        # yield from bps.mv(att2_9.open_cmd, 1)
        # yield from bps.sleep(1)
        # yield from bps.mv(att2_9.open_cmd, 1)
        # yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="NS", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


            yield from bps.mv(piezo.th, ai0)            




def nexafs_S_edge_measurments_2024_1_ILs(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)

    names = ['nexafs_IL22_PBTTTC14_C12mimOTrf_1_1']             
    x_piezo = [       -49000]
    x_hexa = [            -14]
    y_piezo = [        7700]
    z_piezo = [       -3000]
       
    # names = ['IL1_C8mim_NEXAFS'] 
    # x_piezo = [    55000] 
    # x_hexa = [        12] 
    # y_piezo = [     6040] 
    # z_piezo = [    -3000]


    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    # energies = [2450.0,2455.0,2460.0,2465.0,2470.0,2473.0,2475.0,2475.5,2476.0,2476.5,2477.0,2477.5,2478.0,2478.5,2479.0,2479.5,
    # 2480.0,2480.5,2481.0,2481.5,2482.0,2482.5,2483.0,2483.5,2484.0,2484.5,2485.0,2485.5,2486.0,2487.0,2488.0,2489.0,2490.0,2491.0,2492.5,2495.0,2500.0,2510.0,2515.0]

    energies = np.linspace(2470,2510,41)

    waxs_arc = [0]
    ai0_all = 0
    ai_list = [1.6]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        # yield from bps.mv(att2_9.open_cmd, 1)
        # yield from bps.sleep(1)
        # yield from bps.mv(att2_9.open_cmd, 1)
        # yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="NS", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


            yield from bps.mv(piezo.th, ai0)            





def Cl_edge_measurments_2024_1_ILs(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)

    # names = [' P3HT1500',        'PVC1000',      'IL5_C12mimCl',  'IL7_PBTTTC14',      'IL8_PBTTTC16', 'IL21_PBTTTC14_C12mimCl_3_1']             
    # x_piezo = [    55000,            54000,               43000,           33000,               18000,                       -49000]
    # x_hexa = [        13,                0,                   0,               0,                   0,                           -1]
    # y_piezo = [     6600,             6600,                6700,            6800,                6800,                         7500]
    # z_piezo = [    -3000,            -3000,               -3000,           -3000,               -3000,                        -3000]

    names = [ 'FS64_PBTTTC16_Cl16']             
    x_piezo = [              29000]
    x_hexa = [                   0]
    y_piezo = [               6700]
    z_piezo = [              -3000]


    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    energies = -10 + np.asarray([2810.0, 2820.0, 2828.0, 2829.0, 2830.0, 2831.0, 2832.0, 2833.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    waxs_arc = [0, 20]
    ai0_all = 0
    ai_list = [1.6]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="NS", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="NS", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


            yield from bps.mv(piezo.th, ai0)




def Cl_edge_measurments_2024_1_Amalie(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)

    # bottom left first
    # names = [  'Co_25mmol_FeCl3', 'hT_25mmol_FeCl3', 'mT_25mmol_FeCl3', 'hTe_25mmol_FeCl3', 'mTe_25mmol_FeCl3', 'mB_25mmol_FeCl3', 'hB_25mmol_FeCl3']             
    # x_piezo = [            18000,              5000,             -9000,             -22000,             -34000,            -40000,            -45000]
    # x_hexa = [                 0,                 0,                 0,                  0,                  0,                -9,               -16]
    # y_piezo = [             7000,              7000,              7000,               7200,               7200,              7200,              7200]
    # z_piezo = [            -3000,             -3000,             -3000,              -3000,              -3000,             -3000,             -3000]
    
    names = [       'Co_dedoped', 'hT_400mmol_FeCl3', 'mT_400mmol_FeCl3', 'hTe_1.5mmol_FeCl3',  'mTe_6mmol_FeCl3']             
    x_piezo = [            49000,              35000,              20000,                6000,             -10000]
    x_hexa = [                 0,                  0,                  0,                   0,                  0]
    y_piezo = [            -2000,              -1900,              -1800,               -1800,              -1600]
    z_piezo = [            -3000,              -3000,              -3000,               -3000,              -3000]

    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    energies = -10 + np.asarray([2810.0, 2820.0, 2828.0, 2829.0, 2830.0, 2831.0, 2832.0, 2833.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    waxs_arc = [0, 20]
    ai0_all = 0
    ai_list = [1.6, 3.2]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="LR", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


            yield from bps.mv(piezo.th, ai0)




def stingelin_2024_11_day(t=1):
    yield from Cl_edge_measurments_2024_1_ILs(t=t)

    proposal_id("2024_1", "313968_Stingelin_06")
    yield from Cl_edge_measurments_2024_1_Amalie(t=t)



def Cl_edge_measurments_2024_1_Ginger1(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)

    # names = [  ' P3HT1500', 'PVC1000','Pg32T-TT_FeCl3_sa1','Pg32T-TT_FeCl3_sa2','Pg32T-TT_FeCl3_sa3','Pg32T-TT_FeCl3_sa4','Pg32T-TT_FeCl3_sa5','Pg32T-TT_FeCl3_sa6','Pg32T-TT_FeCl3_sa7']             
    # x_piezo = [      55000,     51000,               38000,               23000,                7000,              -10000,              -24000,              -41000,              -46000]
    # x_hexa = [          10,         0,                   0,                   0,                   0,                   0,                   0,                   0,                 -10]
    # y_piezo = [       6700,      6700,                6800,                6800,                6900,                6900,                7000,                7000,                7100] 
    # z_piezo = [      -3000,     -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000]
     

    names = [ ' P3MEEMT_FeCl3_sa12','P3MEEMT_FeCl3_sa13','P3MEEMT_FeCl3_sa14','P3MEEMT_FeCl3_sa15','Pg32T-TT_KCl04_sa1','Pg32T-TT_KCl04_sa2','Pg32T-TT_KCl04_sa3','Pg32T-TT_KCl04_sa4','Pg32T-TT_KCl04_sa5',
               'Pg32T-TT_FeCl3_sa8','Pg32T-TT_KCl04_sa6','Pg32T-TT_KCl04_sa7','Pg32T-TT_KCl04_sa8','Pg32T-TT_KCl04_sa9', 'P3MEEMT_FeCl3_sa9','P3MEEMT_FeCl3_sa10','P3MEEMT_FeCl3_sa11']             
    x_piezo = [               55000,               53000,               36000,               21000,                6000,               -9000,              -24000,              -41000,              -46000,
                              55000,               50000 ,              34000,               17000,                   0,              -24000,              -41000,              -46000]
    x_hexa = [                   11,                   0,                   0,                   0,                   0,                   0,                   0,                   0,                 -10,
                                 10,                   0,                   0,                   0,                   0,                   0,                   0,                 -10]
    y_piezo = [                6700,                6700,                6800,                6800,                6900,                6900,                7000,                7000,                7100,
                              -2100,               -2000,               -1900,               -1700,               -1700,               -1600,               -1400,               -1400] 
    z_piezo = [               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,
                              -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000]
     

    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    #FeCl3
    energies = -10 + np.asarray([2810.0, 2820.0, 2828.0, 2829.0, 2830.0, 2831.0, 2832.0, 2833.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    waxs_arc = [0, 20]
    ai0_all = 0
    ai_list = [1.6]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="LR", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


                name_fmt = "{sample}_pos3_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


                name_fmt = "{sample}_pos4_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

            yield from bps.mv(piezo.th, ai0)




def Cl_edge_measurments_2024_1_Ginger2(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)


    # names = [ ' P3MEEMT_FeCl3_sa12','P3MEEMT_FeCl3_sa13','P3MEEMT_FeCl3_sa14','P3MEEMT_FeCl3_sa15','Pg32T-TT_KCl04_sa1','Pg32T-TT_KCl04_sa2','Pg32T-TT_KCl04_sa3','Pg32T-TT_KCl04_sa4','Pg32T-TT_KCl04_sa5',
    #            'Pg32T-TT_FeCl3_sa8','Pg32T-TT_KCl04_sa6','Pg32T-TT_KCl04_sa7','Pg32T-TT_KCl04_sa8','Pg32T-TT_KCl04_sa9', 'P3MEEMT_FeCl3_sa9','P3MEEMT_FeCl3_sa10','P3MEEMT_FeCl3_sa11']             
    # x_piezo = [               55000,               53000,               36000,               21000,                6000,               -9000,              -24000,              -41000,              -46000,
    #                           55000,               50000 ,              34000,               17000,                   0,              -24000,              -41000,              -46000]
    # x_hexa = [                   11,                   0,                   0,                   0,                   0,                   0,                   0,                   0,                 -10,
    #                              10,                   0,                   0,                   0,                   0,                   0,                   0,                 -10]
    # y_piezo = [                6700,                6700,                6800,                6800,                6900,                6900,                7000,                7000,                7100,
    #                           -2100,               -2000,               -1900,               -1700,               -1700,               -1600,               -1400,               -1400] 
    # z_piezo = [               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,
    #                           -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000,               -3000]
     
    names = [  'P3MEEMT_FeCl3_sa16','P3MEEMT_FeCl3_sa13_redo']             
    x_piezo = [               46000,                    29000]
    x_hexa = [                    0,                        0]
    y_piezo = [                6700,                     6700] 
    z_piezo = [               -3000,                    -3000]
     

    names = [  'P3MEEMT_FeCl3_sa16_redo']             
    x_piezo = [               41800]
    x_hexa = [                    0]
    y_piezo = [                6700] 
    z_piezo = [               -3000]

    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(z_piezo), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(x_hexa), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    #FeCl3
    energies1 = -10 + np.asarray([2810.0, 2820.0, 2828.0, 2829.0, 2830.0, 2831.0, 2832.0, 2833.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    #KCLO4
    energies2 = np.asarray([2810.0, 2820.0, 2828.0, 2829.0, 2830.0, 2831.0, 2832.0, 2833.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    waxs_arc = [0, 20]
    ai0_all = 0
    ai_list = [1.6]

    for name, xs, ys, zs, xs_hexa in zip(names, x_piezo, y_piezo, z_piezo, x_hexa):
        if 'KCl04' in name:
            energies = energies2
        else:
            energies = energies1

        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from bps.mv(piezo.th, ai0_all)
        yield from alignement_gisaxs_doblestack(0.7)

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_pos1_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                dets = [pil900KW, amptek]
                det_exposure_time(3, 3)
                yield from bps.sleep(5)

                name_fmt = "{sample}_amptek_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="LR", sample_name=sample_name)

                yield from bp.count(dets, num=1)
                yield from bps.sleep(5)

                det_exposure_time(t, t)
                dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

                name_fmt = "{sample}_pos2_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


                name_fmt = "{sample}_pos3_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1
                    
                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


                name_fmt = "{sample}_pos4_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(sample=name,energy="%6.2f"%e, ai="%3.2f"%ais, wax=wa, xbpm="%4.3f"%bpm)
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

            yield from bps.mv(piezo.th, ai0)

def stingelin_2024_11_afternoon(t=1):
    proposal_id("2024_1", "313968_Stingelin_08")
    yield from Cl_edge_measurments_2024_1_Amalie(t=t)

    proposal_id("2024_1", "313968_Stingelin_09")
    yield from Cl_edge_measurments_2024_1_Ginger1(t=t)





def Cl_edge_transmission_measurments_2024_1_Amalie(t=1):
    dets = [pil900KW, pil1M]

    # Att2_9 for this serie of sample
    names = [  'Co_25mmol_FeCl3', 'hT_25mmol_FeCl3', 'mT_25mmol_FeCl3', 'hTe_25mmol_FeCl3', 'mTe_25mmol_FeCl3', 'mB_25mmol_FeCl3']             
    x_piezo = [            44000,             37800,             31500,              25600,              19800,             12700]
    y_piezo = [            -6900,             -6900,             -6900,              -6700,              -6400,             -6900]

    # Remove att2_9 for this serie of sample
    names = [  'hB_25mmol_FeCl3', 'Co_dedoped', 'hT_400mmol_FeCl3', 'mT_400mmol_FeCl3', 'hTe_1.5mmol_FeCl3',  'mTe_6mmol_FeCl3']             
    x_piezo = [             6500,         -100,              -6500,             -12600,              -19000,             -25300]
    y_piezo = [            -6400,        -6200,              -6500,              -6800,               -6400,              -6700]


    assert len(x_piezo) == len(y_piezo), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x_piezo) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = -10 + np.asarray([2810.0, 2820.0, 2828.0, 2829.0, 2830.0, 2831.0, 2832.0, 2833.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x_piezo, y_piezo):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys, ys + 500, 33)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        yss1 = np.linspace(ys, ys + 500, 33)
        xss1 = np.array([xs-400])

        yss1, xss1 = np.meshgrid(yss1, xss1)
        yss1 = yss1.ravel()
        xss1 = xss1.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()
                name_fmt = "{sample}_pos1_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            for e, xsss, ysss in zip(energies[::-1], xss1, yss1):
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 50:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)

                    yield from bps.mv(piezo.y, ysss)
                    yield from bps.mv(piezo.x, xsss)

                    bpm = xbpm3.sumX.get()

                    name_fmt = "{sample}_pos2_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
                    sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                    sample_id(user_name="CM", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")

                    yield from bp.count(dets, num=1)




def bpmvspindiode_Cledge_2024_1(t=1):
    dets = [pil1M]
    det_exposure_time(t, t)

    name = 'direct_beam_Cledge_no att'

    energies = -10 + np.asarray([2810.0, 2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0,
    2839.5, 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0])

    for e in energies:
        yield from bps.mv(energy, e)
        yield from bps.sleep(2)
        if xbpm2.sumX.get() < 50:
            yield from bps.sleep(2)
            yield from bps.mv(energy, e)
            yield from bps.sleep(2)

        fs.open()
        yield from bps.sleep(2)
        bpm2 = xbpm2.sumX.get()
        bpm3 = xbpm3.sumX.get()
        pdc = pdcurrent2.get()
        fs.close()

        name_fmt = "{sample}_pos1_{energy}eV_bpm2_{xbpm2}_bpm3_{xbpm3}_pd_{pd}"

        sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, xbpm2="%4.3f"%bpm2, xbpm3="%4.3f"%bpm3, pd="%4.3f"%pdc)
        sample_id(user_name="LR", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from bp.count([pil1M], num=1)


    for e in energies[::-1]:
        yield from bps.mv(energy, e)
        yield from bps.sleep(2)
        if xbpm2.sumX.get() < 50:
            yield from bps.sleep(2)
            yield from bps.mv(energy, e)
            yield from bps.sleep(2)

        fs.open()
        yield from bps.sleep(2)
        bpm2 = xbpm2.sumX.get()
        bpm3 = xbpm3.sumX.get()
        pdc = pdcurrent2.get()
        fs.close()

        name_fmt = "{sample}_pos2_{energy}eV_bpm2_{xbpm2}_bpm3_{xbpm3}_pd_{pd}"

        sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, xbpm2="%4.3f"%bpm2, xbpm3="%4.3f"%bpm3, pd="%4.3f"%pdc)
        sample_id(user_name="LR", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from bp.count([pil1M], num=1)