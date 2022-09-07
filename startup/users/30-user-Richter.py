def P_edge_measurments(t=1):
    dets = [pil1M, pil300KW]
    det_exposure_time(t, t)

    names = [
        "s05_P3MEEMT_115C_KPF6",
        "s34_MM460_170_KPF6",
        "s30_MMM389_170_KPF6",
        "s38_MM461_170_KPF6",
        "s8_P3HT_ac_KPF6",
        "s42_MM389_170_KPF6",
        "s46_MM460_170_KPF6",
        "s50_MM461_170_KPF6",
    ]
    x_piezo = [42000, 31000, 19000, 6000, -6000, -16000, -33000, -44000]

    energies = [
        2140.0,
        2145.0,
        2150.0,
        2155.0,
        2157.0,
        2157.5,
        2158.0,
        2158.5,
        2159.0,
        2159.5,
        2160.0,
        2160.5,
        2161.0,
        2161.5,
        2162.0,
        2162.5,
        2163.0,
        2163.5,
        2164.0,
        2164.5,
        2165.0,
        2165.5,
        2166.0,
        2170.0,
        2175.0,
        2180.0,
        2185.0,
        2190.0,
        2195.0,
        2200.0,
    ]
    xbpm3_y = [
        1.416,
        1.414,
        1.412,
        1.41,
        1.4092,
        1.409,
        1.4088,
        1.4086,
        1.4084,
        1.4082,
        1.408,
        1.4078,
        1.4076,
        1.4074,
        1.4072,
        1.407,
        1.4068,
        1.4066,
        1.4064,
        1.4062,
        1.406,
        1.4058,
        1.4056,
        1.404,
        1.402,
        1.4,
        1.398,
        1.396,
        1.394,
        1.392,
    ]

    waxs_arc = [0, 17]
    ai0 = 0
    ai_list = [0.52, 0.80]

    offset = 0  # offset to not measure again teh same position as sulfur

    for name, xs in zip(names, x_piezo):
        yield from bps.mv(piezo.x, xs)

        yield from alignement_special(angle=0.75)

        ai0 = piezo.th.position
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)
                yield from bps.mv(piezo.x, xs + offset + k * 400)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"

                for e, xbpm3_ys in zip(energies, xbpm3_y):
                    yield from bps.mv(energy, e)
                    yield from bps.mv(xbpm3_pos.y, xbpm3_ys)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                yield from bps.mvr(piezo.x, 200)
                name_fmt = "{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}"
                for e, xbpm3_ys in zip(energies[::-1], xbpm3_y[::-1]):
                    yield from bps.mv(energy, e)
                    yield from bps.mv(xbpm3_pos.y, xbpm3_ys)
                    yield from bps.sleep(1)
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


def transition_Cl_S_edges():
    yield from bps.mv(energy, 2800)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2780)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2760)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2740)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2720)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2700)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2680)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2660)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2640)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2610)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2580)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2550)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2525)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2500)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2475)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2450)
    yield from bps.sleep(2)


def transition_S_Cl_edges():
    yield from bps.mv(energy, 2450)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2475)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2500)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2525)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2550)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2580)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2610)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2640)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2660)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2680)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2700)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2720)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2740)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2760)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2780)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2800)
    yield from bps.sleep(2)


def Cl_edge_vertical(t=1):
    dets = [pil300KW]
    det_exposure_time(t, t)

    # name = 's01_P3HT015_un', 's04_P3MEEMT_115_un', 's33_MM460_170_ClO4'
    name = "s33_MM460_170_ClO4"

    energies = [
        2820.0,
        2830.0,
        2832.0,
        2834.0,
        2834.5,
        2835.0,
        2835.5,
        2836.0,
        2836.5,
        2837.0,
        2837.5,
        2838.0,
        2838.5,
        2839.0,
        2839.5,
        2840.0,
        2840.5,
        2841.0,
        2841.5,
        2845.0,
        2850.0,
        2855.0,
        2860.0,
        2865.0,
        2870.0,
    ]

    waxs_arc = [4, 10.5, 17, 45]

    ai0 = piezo.th.position
    for i, wa in enumerate(waxs_arc):
        if i == 0:
            print("wa=4deg")
        else:
            yield from bps.mv(waxs, wa)

        name_fmt = "{sample}_vertical_{energy}eV_ai0.8deg_pos1_wa{wax}_bpm{xbpm}"
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)
            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(
                sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
            )
            sample_id(user_name="LR", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 2850)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2830)
        yield from bps.sleep(2)
        yield from bps.mv(energy, 2810)
        yield from bps.sleep(2)


def NEXAFS_P_edge(t=0.5):
    yield from bps.mv(waxs, 45)
    dets = [pil300KW]
    name = "NEXAFS_s3_test_Pedge_nspot1"

    energies = np.linspace(2130, 2180, 51)
    xbpm3_y = np.linspace(1.42, 1.40, 51)

    det_exposure_time(t, t)
    name_fmt = "{sample}_{energy}eV_xbpm{xbpm}"

    for e, xbpm3_ys in zip(energies, xbpm3_y):
        yield from bps.mv(energy, e)
        yield from bps.mv(xbpm3_pos.y, xbpm3_ys)

        yield from bps.sleep(1)

        sample_name = name_fmt.format(
            sample=name, energy=e, xbpm="%3.1f" % xbpm3.sumX.value
        )
        sample_id(user_name="LR", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=1)


def S_edge_vertical(t=1):
    dets = [pil300KW]
    det_exposure_time(t, t)

    # name = 's01_P3HT015_un', 's04_P3MEEMT_115_un', 's33_MM460_170_ClO4'
    name = "MM460_170"

    energies = [
        2450.0,
        2455.0,
        2460.0,
        2465.0,
        2470.0,
        2473.0,
        2475.0,
        2475.5,
        2476.0,
        2476.5,
        2477.0,
        2477.5,
        2478.0,
        2478.5,
        2479.0,
        2479.5,
        2480.0,
        2480.5,
        2483.0,
        2485.0,
        2487.5,
        2490.0,
        2492.5,
        2495.0,
        2500.0,
        2510.0,
        2515.0,
    ]

    # waxs_arc = [4, 10.5, 17]
    waxs_arc = [10.5, 17]

    ai0 = piezo.th.position
    for i, wa in enumerate(waxs_arc):
        if wa == 4:
            print("wa=4deg")
        else:
            yield from bps.mv(waxs, wa)

        name_fmt = "{sample}_vertical_{energy}eV_ai7.7deg_pos1_wa{wax}_bpm{xbpm}"
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)
            bpm = xbpm2.sumX.value
            sample_name = name_fmt.format(
                sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
            )
            sample_id(user_name="LR", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 2490)
        yield from bps.sleep(1)
        yield from bps.mv(energy, 2470)
        yield from bps.sleep(1)
        yield from bps.mv(energy, 2450)
        yield from bps.sleep(1)


def giwaxs_Cl_edge_Lee_aois_2121_1(t=1):
    dets = [pil1M, pil300KW]

    # names =   ['P3HT_600_KCl04_par', 'P3HT_500_KCl04', 'P3HT_neat', 'P3HT_600_KCl']
    # x_piezo = [              -31000,           -41000,      -53000,         -56000]
    # x_hexa =  [                   0,                0,           0,             -8]
    # z_piezo = [                   0,                0,           0,              0]

    names = ["P3HT_KCl04_bilayer"]
    x_piezo = [50000]
    x_hexa = [0]
    z_piezo = [0]

    dets = [pil1M, pil300KW]
    waxs_arc = [0, 15]

    for numero, (name, xs_piezo, xs_hexa, zs_piezo) in enumerate(
        zip(names, x_piezo, x_hexa, z_piezo)
    ):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.z, zs_piezo)

        ai0 = 0
        yield from bps.mv(piezo.th, ai0)
        yield from alignement_gisaxs(angle=0.4)
        ai0 = piezo.th.position

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)

        ai_list = np.arange(0.3, 0.8, 0.01).tolist()
        ai_list = [round(1000 * x, 4) for x in ai_list]
        ai_list = np.asarray(ai_list) / 1000
        energies = [2820.0, 2838.5, 2870.0]

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            for k, e in enumerate(energies):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xs_piezo + k * 600 + i * 200)

                for l, ais in enumerate(ai_list):
                    yield from bps.mv(piezo.th, ai0 + ais)

                    det_exposure_time(t, t)
                    name_fmt = (
                        "{sample}_pos1_aiscan_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                    )

                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%1.4f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="GF", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

            for k, e in enumerate(energies[::-1]):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.x, xs_piezo + 1000 + k * 600 + i * 200)

                for l, ais in enumerate(ai_list):
                    yield from bps.mv(piezo.th, ai0 + ais)

                    det_exposure_time(t, t)
                    name_fmt = (
                        "{sample}_pos2_aiscan_{energy}eV_ai{ai}_wa{wax}_bpm{xbpm}"
                    )

                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="GF", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


def SVA_night_12_02(t=1):
    global names, x_hexa, y_hexa, incident_angles, y_hexa_aligned

    names = [
        "MM460_170C_ClO4",
        "MM389_as_un",
        "MM389_as_ClO4",
        "MM389_170C_un",
        "MM389_170C_ClO4",
    ]
    x_hexa = [-17, 18, 9, -6, -15]
    # y_hexa = [-3.2, -3.2, -3.2, -3.2,  3,  3,  3,   3]
    # incident_angl = [ 2.8,  2.5,  2.2,  2.2, 2.2, 2.2, 2.2, 2.2]

    # assert len(x_hexa) == len(names), f'Number of X coordinates ({len(x_hexa)}) is different from number of samples ({len(names)})'
    # assert len(x_hexa) == len(y_hexa), f'Number of X coordinates ({len(x_hexa)}) is different from number of samples ({len(y_hexa)})'
    # assert len(x_hexa) == len(incident_angl), f'Number of X coordinates ({len(x_hexa)}) is different from number of samples ({len(incident_angles)})'

    setDryFlow(5)
    setWetFlow(0)

    y_hexa_aligned = [-3.013, 3.311, 3.32, 3.356, 3.322]
    incident_angles = [1.581, 1.199, 1.849, 1.367, 1.825]
    # for name, xs_hexa, ys_hexa, ais in zip(names[4:], x_hexa[4:], y_hexa[4:], incident_angl[4:]):
    #     yield from bps.mv(stage.x, xs_hexa)
    #     yield from bps.mv(stage.y, ys_hexa)
    #     yield from bps.mv(stage.th, ais)

    #     yield from alignement_gisaxs_hex(angle = 0.45)

    #     incident_angles = incident_angles + [stage.th.position]
    #     y_hexa_aligned = y_hexa_aligned + [stage.y.position]

    print(incident_angles)
    print(y_hexa_aligned)

    assert len(x_hexa) == len(
        names
    ), f"Number of X coordinates ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(x_hexa) == len(
        y_hexa_aligned
    ), f"Number of X coordinates ({len(x_hexa)}) is different from number of samples ({len(y_hexa_aligned)})"
    assert len(x_hexa) == len(
        incident_angles
    ), f"Number of X coordinates ({len(x_hexa)}) is different from number of samples ({len(incident_angles)})"

    humidity = "%3.2f" % readHumidity(verbosity=0)
    # Measure the samples with N2 flow
    offset = 0
    yield from Cl_edge_SVA_measurments_2021_2(t=t, offset=offset, humidity=humidity)

    # # Measure at flow 80 percent
    # setDryFlow(2.)
    # setWetFlow(4.35)

    # yield from bps.sleep(40 * 60)
    # humidity = '%3.2f'%readHumidity(verbosity=0)

    # offset = 0.9
    # yield from Cl_edge_SVA_measurments(t=t, offset = offset, humidity = humidity)

    # # Measure at flow 100 percent

    names = [
        "MM460_as_un",
        "MM460_as_ClO4",
        "MM460_170C_un",
        "MM460_170C_ClO4",
        "MM389_as_un",
        "MM389_as_ClO4",
        "MM389_170C_un",
        "MM389_170C_ClO4",
    ]
    x_hexa = [17, 6, -8.0, -17, 18, 9, -6, -15]
    y_hexa_aligned = [-3.052, -3.06, -2.998, -3.013, 3.311, 3.32, 3.356, 3.322]
    incident_angles = [1.94502, 1.77, 1.747, 1.581, 1.199, 1.849, 1.367, 1.825]

    setDryFlow(0)
    setWetFlow(5)

    yield from bps.sleep(40 * 60)
    humidity = "%3.2f" % readHumidity(verbosity=0)
    offset = 1.5
    yield from Cl_edge_SVA_measurments_2021_2(t=t, offset=offset, humidity=humidity)

    # # Back at flow 0 percent
    setDryFlow(5)
    setWetFlow(0)

    yield from bps.sleep(40 * 60)
    humidity = "%3.2f_post" % readHumidity(verbosity=0)

    offset = 3.0
    yield from Cl_edge_SVA_measurments_2021_2(t=t, offset=offset, humidity=humidity)


def S_edge_measurments_transmission(t=1):
    dets = [pil1M, pil900KW, pil300KW]

    # names = ['P3MEEMT_13k_115C', 'P3MEEMT_23k_115C', 'MM460_170C', 'PB2T_TEG_undoped', 'PB2T_TEG_partialCV', 'PB2T_TEG_partial_dedope',
    # 'PB2T_TEG_doped400mV', 'KClO4_neat']
    # x_piezo = [28100, 20500, 12500, 4700, -800, -6800, -12000, -19000]
    # y_piezo = [  400,   400,   400,  500,  400,   200,    300,    300]

    names = ["P3MEEMT_13k_115C", "P3MEEMT_23k_115C", "MM460_170C"]
    x_piezo = [27400, 19700, 11800]
    y_piezo = [0, -100, -100]

    assert len(x_piezo) == len(
        names
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"

    energies = [
        2450.0,
        2455.0,
        2460.0,
        2465.0,
        2470.0,
        2473.0,
        2475.0,
        2475.5,
        2476.0,
        2476.5,
        2477.0,
        2477.5,
        2478.0,
        2478.5,
        2479.0,
        2479.5,
        2480.0,
        2480.5,
        2483.0,
        2485.0,
        2487.5,
        2490.0,
        2492.5,
        2495.0,
        2500.0,
        2510.0,
        2515.0,
    ]

    waxs_arc = [23]
    det_exposure_time(t, t)

    for numb, (name, xs, ys) in enumerate(zip(names, x_piezo, y_piezo)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 27)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(waxs, wa)

            name_fmt = "{sample}_saxsredo_{energy}eV_pos1_wa{wax}_bpm{xbpm}"
            for e, ysss in zip(energies, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="LR", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mvr(piezo.x, 400)
            name_fmt = "{sample}_{energy}eV_pos2_wa{wax}_bpm{xbpm}"
            for e, ysss in zip(energies[::-1], yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="LR", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)


def Cl_edge_measurments_transmission(t=1):
    dets = [pil1M, pil900KW, pil300KW]

    # names = ['PB2T_TEG_undoped', 'PB2T_TEG_partialCV', 'PB2T_TEG_partial_dedope', 'PB2T_TEG_doped400mV', 'KClO4_neat']
    # x_piezo = [3800, -1800, -7800, -13300, -20000]
    # y_piezo = [ 400,   200,     0,    300,    300]

    names = ["PB2T_TEG_doped400mV", "KClO4_neat"]
    x_piezo = [-12500, -20000]
    y_piezo = [300, 300]

    assert len(x_piezo) == len(
        names
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"

    energies = [
        2810.0,
        2820.0,
        2830.0,
        2832.0,
        2834.0,
        2834.5,
        2835.0,
        2835.5,
        2836.0,
        2836.5,
        2837.0,
        2837.5,
        2838.0,
        2838.5,
        2839.0,
        2839.5,
        2840.0,
        2840.5,
        2841.0,
        2841.5,
        2845.0,
        2850.0,
        2855.0,
        2860.0,
        2865.0,
        2870.0,
        2875.0,
        2880.0,
        2890.0,
    ]

    waxs_arc = [2, 23]
    det_exposure_time(t, t)

    for numb, (name, xs, ys) in enumerate(zip(names, x_piezo, y_piezo)):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 27)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(waxs, wa)

            name_fmt = "{sample}_saxs_{energy}eV_pos1_wa{wax}_bpm{xbpm}"
            for e, ysss in zip(energies, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="LR", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mvr(piezo.x, 300)
            name_fmt = "{sample}_{energy}eV_pos2_wa{wax}_bpm{xbpm}"
            for e, ysss in zip(energies[::-1], yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, ysss)
                bpm = xbpm2.sumX.value
                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="LR", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)


def S_edge_SVA_measurments_2021_3(t=1, offset=1, humidity="test"):

    names = ["PB2T_TEG_doped400mV"]
    x_hexa = [-12500]
    y_hexa = [300]

    dets = [pil1M, pil300KW, pil900KW]
    det_exposure_time(t, t)

    energies = [
        2450.0,
        2455.0,
        2460.0,
        2465.0,
        2470.0,
        2473.0,
        2475.0,
        2475.5,
        2476.0,
        2476.5,
        2477.0,
        2477.5,
        2478.0,
        2478.5,
        2479.0,
        2479.5,
        2480.0,
        2480.5,
        2483.0,
        2485.0,
        2487.5,
        2490.0,
        2492.5,
        2495.0,
        2500.0,
        2510.0,
        2515.0,
    ]

    waxs_arc = [2, 23]
    ai_list = [0.80]

    for name, xs_hexa, incident_ang, ys_hexap in zip(
        names, x_hexa, incident_angles, y_hexa
    ):

        yield from bps.mv(stage.x, xs_hexa + offset)
        xs = xs_hexa + offset

        yield from alignement_gisaxs_hex(angle=0.45)

        yield from bps.mv(stage.y, ys_hexap)
        yield from bps.mv(stage.th, incident_ang)

        ai0 = incident_ang
        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)

                name_fmt = "{sample}_hum{hum}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    yield from bps.mv(stage.x, xs + counter * 0.025)
                    counter += 1
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(
                        sample=name,
                        hum=humidity,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                name_fmt = "{sample}_hum{hum}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(1)
                    yield from bps.mv(stage.x, xs + counter * 0.025)
                    counter += 1
                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(
                        sample=name,
                        hum=humidity,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)


def Cl_edge_measurments_2022_1(t=1):
    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t, t)

    # names = ['MM389_submerged', 'MM389_n500mV', 'MM389_n400mV', 'MM389_n300mV', 'MM389_p400mV', 'MM389_n200mV', 'MM389_n100mV', 'MM389_n000mV', 'MM389_p100mV', 'MM389_p200mV',
    # 'MM460_submerged', 'MM460_n500', 'MM460_n400', 'MM460_n300', 'MM460_p400', 'MM460_n200', 'MM460_n100', 'MM460_n000', 'MM460_p100', 'MM460_p200',
    # 'P3PAAT_un_1', 'P3PAAT_do_1','P3PAAT_un_2','P3PAAT_do_2','Polystyrene', 'PVC']
    # x_piezo = [ -50700,-51200,-44600,-33900,-23300,-12600,-1700, 9300, 19600, 30700, 41300, 48600, 48600,
    # -48500,-48700,-41800,-31700,-21300,-10700, -200,10200, 21700, 32800, 42300, 47500, 46900]
    # x_hexap = [    -15,  -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 15,
    # -15, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 15 ]
    # y_piezo = [  -2900, -2850, -2800, -2750, -2700, -2650, -2600, -2550, -2500, -2450, -2400, -2350, -2300,
    # 5800,  5850,  5900,  5950,  6000,  6050,  6100,  6150,  6200,  6250,  6300,  6350,  6400]
    # to finish up last 8 samples at Cl edge:
    names = [
        "MM460_p200",
        "P3PAAT_un_1",
        "P3PAAT_do_1",
        "P3PAAT_un_2",
        "P3PAAT_do_2",
        "Polystyrene",
        "PVC",
    ]
    x_piezo = [-200, 10200, 21700, 32800, 42300, 47500, 46900]
    x_hexap = [0, 0, 0, 0, 0, 4, 15]
    y_piezo = [6100, 6150, 6200, 6250, 6300, 6350, 6400]

    assert len(x_piezo) == len(
        names
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(
        x_hexap
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})"

    energies = [
        2810.0,
        2820.0,
        2830.0,
        2832.0,
        2834.0,
        2834.5,
        2835.0,
        2835.5,
        2836.0,
        2836.5,
        2837.0,
        2837.5,
        2838.0,
        2838.5,
        2839.0,
        2839.5,
        2840.0,
        2840.5,
        2841.0,
        2841.5,
        2845.0,
        2850.0,
        2855.0,
        2860.0,
        2865.0,
        2870.0,
        2875.0,
        2880.0,
        2890.0,
    ]

    waxs_arc = [0, 20]
    ai0 = 0
    ai_list = [0.80]

    for name, xs, ys, xs_hexap in zip(names, x_piezo, y_piezo, x_hexap):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.x, xs_hexap)

        yield from bps.mv(piezo.th, ai0)
        yield from alignement_gisaxs_doblestack(0.2)

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):

            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW, pil300KW] if wa < 10 else [pil1M, pil900KW, pil300KW]

            yield from bps.mv(waxs, wa)
            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs + counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs + counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos3_wa{wax}_bpm{xbpm}'
                # for e in energies:
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(2)
                #     if xbpm2.sumX.get() < 120:
                #         yield from bps.sleep(2)
                #         yield from bps.mv(energy, e)
                #         yield from bps.sleep(2)
                #     yield from bps.mv(piezo.x, xs + counter * 30)
                #     counter += 1

                #     bpm = xbpm2.sumX.get()
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='LR', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos4_wa{wax}_bpm{xbpm}'
                # for e in energies[::-1]:
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(2)
                #     if xbpm2.sumX.get() < 120:
                #         yield from bps.sleep(2)
                #         yield from bps.mv(energy, e)
                #         yield from bps.sleep(2)
                #     yield from bps.mv(piezo.x, xs + counter * 30)
                #     counter += 1

                #     bpm = xbpm2.sumX.get()
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='LR', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)


def K_edge_measurments_2022_1(t=0.5):
    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t, t)

    # exploratory K L-edge at 2022-1:
    names = [
        "Acid_PEDOT_n600mV",
        "Acid_PEDOT_p600mV",
        "Acid_PEDOT_exposed",
        "Acid_PEDOT_n300mV",
        "Acid_PEDOT_p300mV",
        "EG_PEDOT_neat",
        "   EG_PEDOT_n600mV",
        "EG_PEDOT_p600mV",
        "EG_PEDOT_exposed",
        "EG_PEDOT_n300mV",
        "Eg_PEDOT_p300mV",
    ]
    x_piezo = [
        -56402,
        -42402,
        -30402,
        -18402,
        -5402,
        7597,
        21597,
        34597,
        43594,
        55597,
        50597,
    ]
    x_hexap = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15]
    y_piezo = [6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100]

    assert len(x_piezo) == len(
        names
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(
        x_hexap
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})"

    energies = np.asarray(
        np.arange(3590, 3611, 5).tolist()
        + np.arange(3612, 3629, 0.4).tolist()
        + np.arange(3630, 3721, 5).tolist()
    )

    waxs_arc = [0, 20]
    ai0 = 0
    ai_list = [0.60]

    for name, xs, ys, xs_hexap in zip(names, x_piezo, y_piezo, x_hexap):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.x, xs_hexap)

        yield from bps.mv(piezo.th, ai0)
        yield from alignement_gisaxs(0.4)

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):

            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW, pil300KW] if wa < 10 else [pil1M, pil900KW, pil300KW]

            yield from bps.mv(waxs, wa)
            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)
                yield from bps.mv(energy, 3680)
                yield from bps.sleep(2)
                yield from bps.mv(energy, 3640)
                yield from bps.sleep(2)
                yield from bps.mv(energy, 3590)
                yield from bps.sleep(2)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                # for e in energies[::-1]:
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(2)
                #     if xbpm2.sumX.get() < 120:
                #         yield from bps.sleep(2)
                #         yield from bps.mv(energy, e)
                #         yield from bps.sleep(2)
                #     yield from bps.mv(piezo.x, xs - counter * 30)
                #     counter += 1

                #     bpm = xbpm2.sumX.get()
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='LR', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def S_edge_measurments_2022_1(t=1):
    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t, t)

    names = ["P3HT_TCB1to20_paral_phi8deg"]
    x_piezo = np.asarray([19900])
    x_hexap = [0]
    y_piezo = [5475]

    # names = ['MM389_submerged', 'MM389_n500mV', 'MM389_n400mV', 'MM389_n300mV', 'MM389_p400mV', 'MM389_n200mV', 'MM389_n100mV', 'MM389_n000mV', 'MM389_p100mV', 'MM389_p200mV',
    # 'MM460_submerged', 'MM460_n500', 'MM460_n400', 'MM460_n300', 'MM460_p400', 'MM460_n200', 'MM460_n100', 'MM460_n000', 'MM460_p100', 'MM460_p200',
    # 'P3PAAT_un_1', 'P3PAAT_do_1','P3PAAT_un_2','P3PAAT_do_2','Polystyrene', 'PVC']
    # x_piezo = -200 + np.asarray([ -50700,-51200,-44600,-33900,-23300,-12600,-1700, 9300, 19600, 30700, 41300, 48600, 48600,
    # -48500,-48700,-41800,-31700,-21300,-10700, -200,10200, 21700, 32800, 42300, 47500, 46900])
    # x_hexap = [    -15,  -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 15,
    # -15, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 15 ]
    # y_piezo = [  -2900, -2850, -2800, -2750, -2700, -2650, -2600, -2550, -2500, -2450, -2400, -2350, -2300,
    # 5800,  5850,  5900,  5950,  6000,  6050,  6100,  6150,  6200,  6250,  6300,  6350,  6400]

    # names = ['P3MEEMT_23KDa_115C_600mV', 'P3MEEMT_13KDa_115C_600mV', 'P3MEEMT_13KDa_115C_450mV', 'P3MEEMT_13KDa_115C_400mV', 'P3MEEMT_13KDa_115C_350mV',
    #'P3MEEMT_13KDa_115C_325mV', 'P3MEEMT_13KDa_115C_300mV', 'P3MEEMT_13KDa_115C_275mV', 'P3MEEMT_13KDa_115C_0mV']
    # x_piezo = -5000 + np.asarray([ 37000,  21000, 8000, -6000, -19000, -32000, -43000, -50000, -50000])
    # x_hexap = [     0,      0,    0,     0,      0,      0,      0,     -4,    -16]
    # y_piezo = [  6000,   6000, 6000,  6000,   6000,   6000,   6000,   6000,   6000]

    assert len(x_piezo) == len(
        names
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(
        x_hexap
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})"

    energies = [
        2450.0,
        2455.0,
        2460.0,
        2465.0,
        2470.0,
        2473.0,
        2475.0,
        2475.5,
        2476.0,
        2476.5,
        2477.0,
        2477.5,
        2478.0,
        2478.5,
        2479.0,
        2479.5,
        2480.0,
        2480.5,
        2483.0,
        2485.0,
        2487.5,
        2490.0,
        2492.5,
        2495.0,
        2500.0,
        2510.0,
        2515.0,
    ]

    waxs_arc = [0, 20]  # new cords 1 degree overlap
    ai0 = 0.0397
    ai_list = [0.80]

    for name, xs, ys, xs_hexap in zip(names, x_piezo, y_piezo, x_hexap):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.x, xs_hexap)

        yield from bps.mv(piezo.th, ai0)
        # yield from alignement_gisaxs(0.20)

        # insert attenuator, factor 10
        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(
            att2_9.open_cmd, 1
        )  # sometimes doesn't work, belt and suspenders always two twice

        # ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            yield from bps.mv(piezo.x, xs)
            counter = 0
            dets = [pil900KW, pil300KW] if wa < 10 else [pil1M, pil900KW, pil300KW]
            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(
                            2
                        )  # used to be 5 when fighting RF noise, can be sped up to
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs - counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos3_wa{wax}_bpm{xbpm}'
                # for e in energies:
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(2)
                #     if xbpm2.sumX.get() < 120:
                #         yield from bps.sleep(2)
                #         yield from bps.mv(energy, e)
                #         yield from bps.sleep(2)
                #     yield from bps.mv(piezo.x, xs - counter * 30)
                #     counter += 1

                #     bpm = xbpm2.sumX.get()
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='LR', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                # #     yield from bp.count(dets, num=1)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos4_wa{wax}_bpm{xbpm}'
                # for e in energies[::-1]:
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(2)
                #     if xbpm2.sumX.get() < 120:
                #         yield from bps.sleep(2)
                #         yield from bps.mv(energy, e)
                #         yield from bps.sleep(2)
                #     yield from bps.mv(piezo.x, xs - counter * 30)
                #     counter += 1

                #     bpm = xbpm2.sumX.get()
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='LR', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def night_2021_12_15(t=1):
    proposal_id("2021_3", "307296_Richter4")
    yield from S_edge_measurments_2021_3(t=t)

    proposal_id("2021_3", "308274_Ferron5")
    yield from xrr_spol_waxs()


def night_2022_1(t=1):
    #   removed for night 2, kept bps.mv
    #   proposal_id('2022_1', '309251_Richter_Clnight')
    #   yield from Cl_edge_measurments_2022_1(t=t)
    yield from transition_Cl_S_edges()
    yield from bps.mv(xbpm3_pos.y, 1.376)
    proposal_id("2022_1", "309251_Richter_Snight")
    yield from S_edge_measurments_2022_1(t=t)
    #   yield from transition_S_Cl_edges()
    #   yield from bps.mv(xbpm3_pos.y, 1.43)
    #


def Cl_edge_measurments_2021_3_hex(t=1):
    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t, t)

    names = ["20um_blank"]
    x_hexap = [18]

    assert len(x_hexap) == len(
        names
    ), f"Number of X coordinates ({len(x_hexap)}) is different from number of samples ({len(names)})"

    energies = [
        2810.0
    ]  # , 2820.0, 2830.0, 2832.0, 2834.0, 2834.5, 2835.0, 2835.5, 2836.0, 2836.5, 2837.0, 2837.5, 2838.0, 2838.5, 2839.0, 2839.5,
    # 2840.0, 2840.5, 2841.0, 2841.5, 2845.0, 2850.0, 2855.0, 2860.0, 2865.0, 2870.0, 2875.0, 2880.0, 2890.0]

    waxs_arc = [0, 20]  # changed 2022_1 for prpoer waxs center
    ai0 = 0
    ai_list = [0.80]

    for name, xs_hexap in zip(names, x_hexap):
        yield from bps.mv(stage.x, xs_hexap)

        yield from alignement_gisaxs_hex_roughsample(angle=0.45)

        ai0 = stage.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(5)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(stage.x, xs_hexap + counter * 0.02)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}"
                for e in energies[::-1]:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(5)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(stage.x, xs_hexap + counter * 0.02)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

            yield from bps.mv(stage.th, ai0)


def run_waxs_waitwater_2022_1(t=1):
    names = ["KClO4_flow_on_AuNps_2450eV"]
    user = "LR"
    det_exposure_time(t, t)
    waxs_arc = [0]
    # Detectors, motors:
    dets = [pil900KW]

    t0 = time.time()
    yield from bps.mv(waxs, waxs_arc)

    for t in np.linspace(0, 299, 300):

        name_fmt = "{sample}_{time}s"
        sample_name = name_fmt.format(sample=names[0], time="%.1f" % (time.time() - t0))
        sample_id(user_name=user, sample_name=sample_name)

        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=1)
        yield from bps.sleep(50)

    sample_id(user_name=user, sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")

    det_exposure_time(0.3, 0.3)


def Cl_edge_measurments_liquid_cell(t=1):
    dets = [pil900KW]
    det_exposure_time(t, t)

    name = "KClO4_2ndload_flowing_300ssleep"

    energies = [
        2800.0,
        2810.0,
        2820.0,
        2825.0,
        2830.0,
        2832.0,
        2834.0,
        2834.5,
        2835.0,
        2835.5,
        2836.0,
        2836.5,
        2837.0,
        2837.5,
        2838.0,
        2838.5,
        2839.0,
        2839.5,
        2840.0,
        2840.5,
        2841.0,
        2841.5,
        2845.0,
        2850.0,
        2855.0,
        2860.0,
        2865.0,
        2870.0,
        2875.0,
        2880.0,
        2890.0,
    ]

    waxs_arc = [23]

    for i, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
        counter = 0

        name_fmt = "{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(300)
            # yield from bps.mvr(stage.y, -0.02)
            # if xbpm2.sumX.get() < 120:
            #     yield from bps.sleep(5)
            #     yield from bps.mv(energy, e)
            #     yield from bps.sleep(2)

            bpm = xbpm3.sumX.get()
            sample_name = name_fmt.format(
                sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
            )
            sample_id(user_name="LR", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)

    yield from bps.mv(energy, 2860)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2830)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2810)
    yield from bps.sleep(2)

    yield from bps.sleep(300)

    dets = [pil900KW]
    det_exposure_time(t, t)

    # names = ['KClO4']
    # name = 'KClO4_2ndload_flowing_300ssleep'

    energies = 0.25 + np.asarray(
        [
            2800.0,
            2810.0,
            2820.0,
            2825.0,
            2830.0,
            2832.0,
            2834.0,
            2834.5,
            2835.0,
            2835.5,
            2836.0,
            2836.5,
            2837.0,
            2837.5,
            2838.0,
            2838.5,
            2839.0,
            2839.5,
            2840.0,
            2840.5,
            2841.0,
            2841.5,
            2845.0,
            2850.0,
            2855.0,
            2860.0,
            2865.0,
            2870.0,
            2875.0,
            2880.0,
            2890.0,
        ]
    )

    waxs_arc = [23]

    for i, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
        counter = 0

        name_fmt = "{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(300)
            # yield from bps.mvr(stage.y, -0.02)
            # if xbpm2.sumX.get() < 120:
            #     yield from bps.sleep(5)
            #     yield from bps.mv(energy, e)
            #     yield from bps.sleep(2)

            bpm = xbpm3.sumX.get()
            sample_name = name_fmt.format(
                sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
            )
            sample_id(user_name="LR", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)

    yield from bps.mv(energy, 2860)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2830)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2810)
    yield from bps.sleep(2)


def PEDOT_Cl_edge_measurments_2022_1(t=1):
    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t, t)
    #
    # Doped PEDOT PSS Films (run on K) at Cl
    #
    names = [
        "Acid_PEDOT_neat",
        "Acid_PEDOT_n600mV",
        "Acid_PEDOT_p600mV",
        "Acid_PEDOT_exposed",
        "Acid_PEDOT_n300mV",
        "Acid_PEDOT_p300mV",
        "EG_PEDOT_neat",
        "   EG_PEDOT_n600mV",
        "EG_PEDOT_p600mV",
        "EG_PEDOT_exposed",
        "EG_PEDOT_n300mV",
        "Eg_PEDOT_p300mV",
    ]
    x_piezo = [
        -54000,
        -56402,
        -42402,
        -30402,
        -18402,
        -5402,
        7597,
        21597,
        34597,
        43594,
        55597,
        50597,
    ]
    x_hexap = [-15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15]
    y_piezo = [6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100, 6100]

    assert len(x_piezo) == len(
        names
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(
        x_hexap
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexap)})"

    energies = [
        2810.0,
        2820.0,
        2830.0,
        2832.0,
        2834.0,
        2834.5,
        2835.0,
        2835.5,
        2836.0,
        2836.5,
        2837.0,
        2837.5,
        2838.0,
        2838.5,
        2839.0,
        2839.5,
        2840.0,
        2840.5,
        2841.0,
        2841.5,
        2845.0,
        2850.0,
        2855.0,
        2860.0,
        2865.0,
        2870.0,
        2875.0,
        2880.0,
        2890.0,
    ]

    waxs_arc = [0, 20]
    ai0 = 0
    ai_list = [0.80]

    for name, xs, ys, xs_hexap in zip(names, x_piezo, y_piezo, x_hexap):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.x, xs_hexap)

        yield from bps.mv(piezo.th, ai0)
        yield from alignement_gisaxs(0.4)

        yield from bps.mv(att2_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_9.open_cmd, 1)

        ai0 = piezo.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):

            # Do not take SAXS when WAXS detector in the way
            dets = [pil900KW, pil300KW] if wa < 10 else [pil1M, pil900KW, pil300KW]

            yield from bps.mv(waxs, wa)
            yield from bps.mv(piezo.x, xs)
            counter = 0

            for k, ais in enumerate(ai_list):
                yield from bps.mv(piezo.th, ai0 + ais)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(2)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(piezo.x, xs + counter * 30)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)
                yield from bps.mv(energy, 2860)  # step back gracefully
                yield from bps.sleep(2)
                yield from bps.mv(energy, 2830)
                yield from bps.sleep(2)
                yield from bps.mv(energy, 2810)
                yield from bps.sleep(2)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                # for e in energies[::-1]:
                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(2)
                #     if xbpm2.sumX.get() < 120:
                #         yield from bps.sleep(2)
                #         yield from bps.mv(energy, e)
                #         yield from bps.sleep(2)
                #     yield from bps.mv(piezo.x, xs + counter * 30)
                #     counter += 1


def Cl_edge_measurments_2022_1_hex(t=5, sample="test"):
    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t, t)

    names = [sample]
    x_hexap = [-27.6]

    assert len(x_hexap) == len(
        names
    ), f"Number of X coordinates ({len(x_hexap)}) is different from number of samples ({len(names)})"

    energies = [
        2810.0,
        2820.0,
        2830.0,
        2832.0,
        2834.0,
        2834.5,
        2835.0,
        2835.5,
        2836.0,
        2836.5,
        2837.0,
        2837.5,
        2838.0,
        2838.5,
        2839.0,
        2839.5,
        2840.0,
        2840.5,
        2841.0,
        2841.5,
        2845.0,
        2850.0,
        2855.0,
        2860.0,
        2865.0,
        2870.0,
        2875.0,
        2880.0,
        2890.0,
    ]

    waxs_arc = [0, 20]  # changed 2022_1 for propoer waxs center
    #   ai0 = 0
    ai_list = [1.00]  # aligned and set ai before

    for name, xs_hexap in zip(names, x_hexap):
        yield from bps.mv(stage.x, xs_hexap)

        #       yield from alignement_gisaxs_hex_roughsample(angle = 0.45) is already aligned

        ai0 = stage.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            counter = 0

            for k, ais in enumerate(ai_list):
                #               yield from bps.mv(stage.th, ai0 + ais)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(5)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(stage.x, xs_hexap - counter * 0.00)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

                # yield from bps.mv(stage.x, xs_hexap - counter * 0.10)

                # name_fmt = '{sample}_{energy}eV_ai{ai}_pos2_wa{wax}_bpm{xbpm}'
                # for e in energies[::-1]:

                #     yield from bps.mv(energy, e)
                #     yield from bps.sleep(2)
                #     if xbpm2.sumX.get() < 120:
                #         yield from bps.sleep(2)
                #         yield from bps.mv(energy, e)
                #         yield from bps.sleep(2)
                #     yield from bps.mv(piezo.x, xs_hexap - counter * 00)
                #     counter += 1

                #     bpm = xbpm2.sumX.get()
                #     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
                #     sample_id(user_name='LR', sample_name=sample_name)
                #     print(f'\n\t=== Sample: {sample_name} ===\n')
                #     yield from bp.count(dets, num=1)


#          yield from bps.mv(stage.th, ai0) #


# name_fmt = '{sample}_{energy}eV_ai{ai}_pos3_wa{wax}_bpm{xbpm}'
# for e in energies:
#     yield from bps.mv(energy, e)
#     yield from bps.sleep(2)
#     if xbpm2.sumX.get() < 120:
#         yield from bps.sleep(2)
#         yield from bps.mv(energy, e)
#         yield from bps.sleep(2)
#     yield from bps.mv(piezo.x, xs - counter * 30)
#     counter += 1

#     bpm = xbpm2.sumX.get()
#     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
#     sample_id(user_name='LR', sample_name=sample_name)
#     print(f'\n\t=== Sample: {sample_name} ===\n')
#     yield from bp.count(dets, num=1)

# name_fmt = '{sample}_{energy}eV_ai{ai}_pos4_wa{wax}_bpm{xbpm}'
# for e in energies[::-1]:
#     yield from bps.mv(energy, e)
#     yield from bps.sleep(2)
#     if xbpm2.sumX.get() < 120:
#         yield from bps.sleep(2)
#         yield from bps.mv(energy, e)
#         yield from bps.sleep(2)
#     yield from bps.mv(piezo.x, xs + counter * 30)
#     counter += 1

#     bpm = xbpm2.sumX.get()
#     sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, ai ='%3.2f'%ais, wax = wa, xbpm = '%4.3f'%bpm)
#     sample_id(user_name='LR', sample_name=sample_name)
#     print(f'\n\t=== Sample: {sample_name} ===\n')
#     yield from bp.count(dets, num=1)


def Cl_edge_measurments_2022_1_hex_slide_only(t=5, sample="test"):
    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t, t)

    names = [sample]
    x_hexap = [-3.46]

    assert len(x_hexap) == len(
        names
    ), f"Number of X coordinates ({len(x_hexap)}) is different from number of samples ({len(names)})"

    energies = [
        2810.0,
        2820.0,
        2830.0,
        2832.0,
        2834.0,
        2834.5,
        2835.0,
        2835.5,
        2836.0,
        2836.5,
        2837.0,
        2837.5,
        2838.0,
        2838.5,
        2839.0,
        2839.5,
        2840.0,
        2840.5,
        2841.0,
        2841.5,
        2845.0,
        2850.0,
        2855.0,
        2860.0,
        2865.0,
        2870.0,
        2875.0,
        2880.0,
        2890.0,
    ]

    energies = [2810 for x in energies]

    waxs_arc = [0]  # changed 2022_1 for propoer waxs center
    #   ai0 = 0
    ai_list = [1.00]  # aligned and set ai before

    for name, xs_hexap in zip(names, x_hexap):
        yield from bps.mv(stage.x, xs_hexap)

        #       yield from alignement_gisaxs_hex_roughsample(angle = 0.45) is already aligned

        ai0 = stage.th.position
        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            counter = 0

            for k, ais in enumerate(ai_list):
                #               yield from bps.mv(stage.th, ai0 + ais)

                name_fmt = "{sample}_{energy}eV_ai{ai}_pos1_wa{wax}_bpm{xbpm}"
                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                    if xbpm2.sumX.get() < 120:
                        yield from bps.sleep(5)
                        yield from bps.mv(energy, e)
                        yield from bps.sleep(2)
                    yield from bps.mv(stage.x, xs_hexap - counter * 0.02)
                    counter += 1

                    bpm = xbpm2.sumX.get()
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%6.2f" % e,
                        ai="%3.2f" % ais,
                        wax=wa,
                        xbpm="%4.3f" % bpm,
                    )
                    sample_id(user_name="LR", sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    yield from bp.count(dets, num=1)

    yield from bps.mv(energy, 2860)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2830)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2810)
    yield from bps.sleep(2)
