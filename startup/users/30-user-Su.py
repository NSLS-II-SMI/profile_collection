def run_saxs_nexafs_greg(t=1):
    # yield from nexafs_prep_multisample_greg(t=0.5)
    # yield from bps.sleep(10)
    yield from saxs_prep_multisample(t=0.5)


def Su_nafion_nexafs_S_edge(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20, 40]
    energies = 7 + np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )

    yield from bps.mv(stage.y, 0)
    yield from bps.mv(stage.th, 0)

    names = ["NCo0", "NCo14", "NCo29", "NCo33", "DK_D139"]
    x = [43700, 21300, -1700, -24600, -55000]
    y = [-2400, -2400, -2000, -2000, -2400]
    z = [1186, 1186, 1186, 1186, 1186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)
            name_fmt = "nexafs_{sample}_{energy}eV_sdd3m_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)

    yield from bps.mv(stage.th, 5)
    yield from bps.mv(stage.y, -15)

    names = ["NCo70", "NCo114", "DK_N115", "DK_D114", "DK_D136"]
    x = [48300, 25800, 3300, -18800, -41800]
    y = [-9500, -9500, -9500, -9500, -9500]
    z = [14186, 14186, 14186, 14186, 14186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)
            name_fmt = "nexafs_{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)


def Su_nafion_swaxs_S_edge(t=1):
    dets = [pil900KW, pil300KW]

    waxs_arc = [0, 20]
    energies = 7 + np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    # energies = np.asarray(np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 1).tolist())

    names = ["AK_PFSA_HPA", "AK_PFSA_ref", "MP_5", "MP_6", "MP_7"]
    x = [43000, 20000, -2500, -25000, -56500]
    y = [1000, 1000, 2500, -1000, 2400]
    z = [1186, 1186, 1186, 1186, 1186]

    # names = ['MP_6', 'MP_7']
    # x =     [-25000, -56500]
    # y =     [  1000,   2400]
    # z =     [  1186,   1186]

    # for name, xs, ys, zs in zip(names, x, y, z):
    #     yield from bps.mv(piezo.x, xs)
    #     yield from bps.mv(piezo.y, ys)
    #     yield from bps.mv(piezo.z, zs)

    #     yss = np.linspace(ys, ys + 1000, 58)
    #     xss = np.linspace(xs, xs, 1)

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)

    #         if wa ==0:
    #             dets = [pil900KW]
    #         else:
    #             dets = [pil900KW, pil1M]

    #         det_exposure_time(t,t)
    #         name_fmt = '{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}'
    #         for e, xsss, ysss in zip(energies, xss, yss):
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(3)

    #             yield from bps.mv(piezo.y, ysss)
    #             yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
    #             sample_id(user_name='GF', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)

    #         yield from bps.mv(energy, 2470)
    #         yield from bps.sleep(3)
    #         yield from bps.mv(energy, 2450)
    #         yield from bps.sleep(3)

    waxs_arc = [0, 20]

    yield from bps.mv(stage.th, 0)
    yield from bps.mv(stage.y, -6)

    # names = ['MP_8', 'MP_1', 'MP_2', 'MP_3', 'MP_4']
    # x =     [ 46500,  21000,  -1500, -26500, -48000]
    # y =     [ -9500,  -9500,  -9500,  -9500,  -9500]
    # z =     [  1186,   1186,   1186,   1186,   1186]

    names = ["MP_4"]
    x = [-47000]
    y = [-8000]
    z = [1186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 67)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):

                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            # yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2830)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2810)
            # yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)


def Su_nafion_waxs_S_edge(t=1):
    dets = [pil300KW, pil1M]

    yield from bps.mv(GV7.open_cmd, 1)
    yield from bps.sleep(5)
    yield from bps.mv(GV7.open_cmd, 1)

    energies = 7 + np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = np.linspace(0, 26, 5)

    yield from bps.mv(stage.y, 0)
    yield from bps.mv(stage.th, 0)

    names = ["SPES20", "SPES40", "SPES60", "70nPA"]
    x = [41500, 18500, -4500, -26500]
    y = [1500, 1000, 500, -500]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 15)
        xss = np.linspace(xs, xs + 1000, 4)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)

    yield from bps.mv(stage.th, 1)
    yield from bps.mv(stage.y, -8)

    names = ["50nPA", "30nPA", "10nPA"]
    x = [30500, 7500, -14200]
    y = [-9600, -9600, -9700]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 15)
        xss = np.linspace(xs, xs + 1000, 4)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def nexafs_Su(t=1):
    dets = [pil300KW]

    energies = np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    # energies = np.linspace(2450, 2500, 51)
    waxs_arc = [52.5]

    names = ["sampleA_redo", "sampleB", "sampleC", "sampleD"]
    x = [-22200, -33200, -38700, -29600]
    y = [-5250, -5250, -5450, 7600]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            det_exposure_time(t, t)
            name_fmt = "nexafs_{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
            for e in energies:
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def waxs_S_edge_greg_2021_2(t=1):
    dets = [pil300KW, pil1M]
    yield from bps.mv(prs, 1)

    names = ["sampleA", "sampleB", "sampleC", "sampleD"]
    x = [-22200, -33200, -39200, -29600]
    y = [-5250, -5250, -5450, 7600]

    energies = (
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.5).tolist()
        + np.arange(2480, 2490, 2).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = np.linspace(13, 13, 1)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 200, 33)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_1.6m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def humidity_experiment(t=1):
    dets = [pil300KW, pil1M]

    # ai_aligned = [1.931, 1.788, 1.666, 1.817]
    # ys_aligned = [3.2, 3.189, 3.122, 3.053]
    # names = ['A30_T0', 'A50_T0', 'A70_T0', 'A90_T0']
    # x_hexa = [     23,        8,       -6,      -18]
    # y_hexa = [    3.2,      3.2,      3.2,      3.2]

    ai_aligned = [1.1248, 0.985, 0.995, 0.916]
    ys_aligned = [3.293, 3.247, 3.19, 3.123]

    # names = ['A30_T7', 'A50_T7', 'A70_T7', 'A90_T7']
    # x_hexa = [     22,       9,       -7,      -16.5]
    # y_hexa = [    3.2,      3.2,      3.2,      3.2]

    names = ["bkg"]
    x_hexa = [23.6]
    y_hexa = [0]

    setDryFlow(5)
    setWetFlow(0)

    humidity = "%3.2f" % readHumidity(verbosity=0)

    waxs_arc = np.linspace(0, 13, 3)

    ai_list = [0.10]

    for num, (name, xs_hexa, ys_hexa) in enumerate(zip(names, x_hexa, y_hexa)):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(stage.y, ys_hexa)

        # yield from alignement_special_hex(angle = 0.15)

        # ai_aligned = ai_aligned + [ai0]
        # ys_aligned = ys_aligned + [stage.y.position]

        # yield from bps.mv(stage.y, ys_aligned[num])
        # yield from bps.mv(stage.th, ai_aligned[num])

        ai0 = stage.th.position

        # print(ai_aligned)
        # print(ys_aligned)

        det_exposure_time(t, t)

        for i, wa in enumerate(waxs_arc[::-1]):
            yield from bps.mv(waxs, wa)

            for k, ais in enumerate(ai_list):
                yield from bps.mv(stage.th, ai0 + ais)
                yield from bps.mv(stage.x, xs_hexa + k * 0.2)

                name_fmt = "{sample}_posthumi_16.1keV_3m_hum{hum}_wa{wax}"
                sample_name = name_fmt.format(sample=name, hum=humidity, wax=wa)
                sample_id(user_name="AB", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

        yield from bps.mv(stage.th, ai0)

    print(ai_aligned)
    print(ys_aligned)


def waxs_Se_edge_greg(t=1):

    det_exposure_time(t, t)

    names = ["PBTTTSe_neat", "P3RSe_dopped", "PBTTTS_dopped", "PBTTTSe_dopped"]
    x = [23700, 17600, 11300, 5400]
    y = [-8300, -8400, -8200, -8600]

    dets = [pil300KW, pil1M]
    energies = (
        np.arange(12620, 12640, 5).tolist()
        + np.arange(12640, 12660, 0.5).tolist()
        + np.arange(12660, 12670, 1).tolist()
        + np.arange(12670, 12716, 5).tolist()
    )
    waxs_arc = np.linspace(0, 26, 5)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 400, 32)
        xss = np.array([xs, xs - 400])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%7.2f" % e, wax=wa, xbpm="%1.3f" % bpm
                )
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 12680)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12645)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 12620)
            yield from bps.sleep(2)


def Su_nafion_swaxs_K_edge(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20, 40]
    energies = np.asarray(
        np.arange(3570, 3600, 5).tolist()
        + np.arange(3600, 3608, 2).tolist()
        + np.arange(3608, 3640, 1).tolist()
        + np.arange(3640, 3690, 5).tolist()
    )

    yield from bps.mv(stage.y, 5)
    yield from bps.mv(stage.th, 0)

    names = ["MP_1", "MP_3"]
    x = [-1000, -23000]
    y = [3000, 2000]
    z = [1186, 1186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 52)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc[::-1]:
            yield from bps.mv(waxs, wa)

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_sdd3m_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 3650)
            yield from bps.mv(energy, 3610)


def Su_nafion_nexafs_K_edge(t=1):
    dets = [pil900KW]

    waxs_arc = [40]
    energies = np.asarray(
        np.arange(3570, 3600, 5).tolist()
        + np.arange(3600, 3608, 2).tolist()
        + np.arange(3608, 3640, 1).tolist()
        + np.arange(3640, 3690, 5).tolist()
    )

    yield from bps.mv(stage.y, 5)
    yield from bps.mv(stage.th, 0)

    names = ["MP_1"]
    x = [-1000]
    y = [3000]
    z = [1186]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1000, 52)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)
            name_fmt = "nexafs_{sample}_{energy}eV_sdd3m_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 3650)
            yield from bps.mv(energy, 3610)


def Su_nafion_swaxs_Co_edge(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20, 40]
    energies = np.asarray(
        np.arange(7650, 7700, 5).tolist()
        + np.arange(7700, 7750, 1).tolist()
        + np.arange(7750, 8405, 5).tolist()
    )
    yield from bps.mv(stage.th, 0)

    names = ["NCo0", "NCo14", "NCo29", "NCo033", "NCo70", "NCo114"]
    x = [-56000, 46000, 22000, 0, -23000, -46000]
    y = [1000, -9500, -9500, -9500, -9500, -9500]
    z = [1186, 1186, 1186, 1186, 1186, 1186]
    y_hexa = [5, -6, -6, -6, -6, -6]

    for name, xs, ys, ys_hexa, zs in zip(names, x, y, y_hexa, z):
        if name == "NCo0":
            waxs_arc = [0, 20]
        else:
            waxs_arc = [0, 20, 40]

        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.y, ys_hexa)

        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 1700, 170)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc[::-1]:
            yield from bps.mv(waxs, wa)

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_sdd3m_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            for ene in np.linspace(8400, 7660, 38):
                yield from bps.mv(energy, ene)
                yield from bps.sleep(2)


def Su_nafion_swaxs_hard(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20, 40]
    yield from bps.mv(stage.th, 0)

    # names = ['AK_PFSA_HPA','AK_PFSA_ref']
    # x =     [        43000,        20000]
    # y =     [         2000,         1500]
    # z =     [         1186,         1186]
    # y_hexa = [           5,            5]

    names = [
        "DK_N115",
        "DK_D114",
        "DK_D136",
        "DK_D139",
        "DK_D165",
        "MP_5",
        "MP_6",
        "MP_7",
        "MP_8",
    ]
    x = [42000, 17000, -5000, -30000, -56000, 45000, 5000, -18000, -41000]
    y = [3500, 3500, 3500, 3500, 2500, -8500, -8500, -8200, -8200]
    z = [1186, 1186, 1186, 1186, 1186, 1186, 1186, 1186, 1186]
    y_hexa = [5, 5, 5, 5, 5, -6, -6, -6, -6]

    x = [-41000]
    y = [-8200]
    z = [1186]
    y_hexa = [-6]

    for name, xs, ys, ys_hexa, zs in zip(names, x, y, y_hexa, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(stage.y, ys_hexa)
        yield from bps.mv(piezo.z, zs)

        for wa in waxs_arc[::-1]:
            yield from bps.mv(waxs, wa)

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)
            name_fmt = "{sample}_16.1keV_sdd5m_wa{wax}"

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(sample=name, wax=wa)
            sample_id(user_name="GF", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)


def Su_nafion_swaxs_S_edge_SVA_2021_3(t=1):
    dets = [pil900KW, pil1M]

    waxs_arc = [0, 20]
    energies = 7 + np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )

    names = [
        "bkg",
        "NCo0",
        "NCo14",
        "NCo33",
        "NCo70",
        "NCo114",
        "MP_5",
        "MP_6",
        "MP_7",
        "MP_7",
    ]
    x = [30.5, 24.0, 18.0, 11.5, 5.0, -1.2, -7.6, -14.0, -20.2, -26.5]
    y = [-1.5, -1.5, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(stage.x, xs)
        yield from bps.mv(stage.y, ys)

        yss = np.linspace(ys, ys + 0.4, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}_hum0per"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(stage.y, ysss)
                yield from bps.mv(stage.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)

    # # Measure at flow 100 percent
    setDryFlow(0)
    setWetFlow(5)
    yield from bps.sleep(600)

    names = [
        "bkg",
        "NCo0",
        "NCo14",
        "NCo33",
        "NCo70",
        "NCo114",
        "MP_5",
        "MP_6",
        "MP_7",
        "MP_7",
    ]
    x = [30.5, 24.0, 17.5, 11.5, 5.0, -1.5, -8.0, -14.0, -20.5, -26.5]
    y = [-1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(stage.x, xs)
        yield from bps.mv(stage.y, ys)

        yss = np.linspace(ys + 0.4, ys + 0.8, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}_hum100per"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(stage.y, ysss)
                yield from bps.mv(stage.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)

    # # Measure at flow 100 percent
    setDryFlow(5)
    setWetFlow(0)
    yield from bps.sleep(600)

    names = [
        "bkg",
        "NCo0",
        "NCo14",
        "NCo33",
        "NCo70",
        "NCo114",
        "MP_5",
        "MP_6",
        "MP_7",
        "MP_7",
    ]
    x = [30.5, 24.0, 17.5, 11.5, 5.0, -1.5, -8.0, -14.0, -20.5, -26.5]
    y = [-1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(stage.x, xs)
        yield from bps.mv(stage.y, ys)

        yss = np.linspace(ys + 0.8, ys + 1.2, 58)
        xss = np.linspace(xs, xs, 1)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)
            name_fmt = (
                "{sample}_{energy}eV_sdd1.7m_wa{wax}_bpm{xbpm}_hum0per_aftercycle"
            )
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(3)

                yield from bps.mv(stage.y, ysss)
                yield from bps.mv(stage.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.sleep(3)
            yield from bps.mv(energy, 2450)
            yield from bps.sleep(3)

    setDryFlow(0)
    setWetFlow(0)


def waxs_S_edge_greg_2022_1(t=1):
    """
    307830_Su Feb 2, 2022
    """

    dets = [pil900KW, pil1M]

    # names = ['M725', 'M825', 'M1000', 'TF725T', 'TF825T', 'TF1000T', 'TF30T', 'TF50T', 'TF70T', 'TF90T', 'TF725', 'TF825', 'TF1000',
    #          'TF30', 'TF50',  'TF70',   'TF90',   'DT20',    'DT35',  'DT50', 'BLANK',   'M30',   'M50',   'M70',   'M90']

    # x =     [ 43000,  37000,   31000,    24500,    18500,     13000,    7500,    2000,   -3000,   -8500,  -14500,  -19500,  -25000,
    #           42000,  36500,   31000,    26000,    20500,     15000,    9500,    4200,   -3800,  -10000,  -18000,  -26000]

    # y =     [ -8500,  -8500,   -8500,    -8500,    -8700,     -8700,   -8700,   -8500,   -8500,   -8500,   -8500,   -8500,   -8500,
    #            4000,   4000,    4000,     4000,     4000,      4000,    4000,    4200,    4200,    4200,    4200,    4200]

    names = [
        "M725",
        "M825",
        "M1000",
        "TF50T",
        "TF70T",
        "TF90T",
        "TF725",
        "TF825",
        "TF1000",
        "TF30",
        "TF50",
        "TF70",
        "TF90",
        "DT20",
        "DT35",
        "DT50",
        "BLANK",
        "M30",
        "M50",
        "M70",
        "M90",
    ]

    x = [
        43000,
        37700,
        30000,
        2000,
        -3000,
        -8500,
        -14500,
        -19500,
        -25000,
        42000,
        36500,
        31000,
        26000,
        20500,
        15000,
        9500,
        4200,
        -3800,
        -10000,
        -18000,
        -26000,
    ]

    y = [
        -8500,
        -8700,
        -8700,
        -8500,
        -8500,
        -8500,
        -8500,
        -8500,
        -8500,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4200,
        4200,
        4200,
        4200,
        4200,
    ]

    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 2).tolist()+ np.arange(2490, 2501, 5).tolist()
    energies = 7 + np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = [0, 20, 40, 60]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        ys = ys - 200
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 500, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_1.6m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="AB", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def saxs_S_edge_greg_2022_1(t=1):
    """
    307830_Su Feb 2, 2022
    """
    proposal_id("2022_1", "307830_Su2")

    dets = [pil1M]

    # names = ['M725', 'M825', 'M1000', 'TF725T', 'TF825T', 'TF1000T', 'TF30T', 'TF50T', 'TF70T', 'TF90T', 'TF725', 'TF825', 'TF1000',
    #          'TF30', 'TF50',  'TF70',   'TF90',   'DT20',    'DT35',  'DT50', 'BLANK',   'M30',   'M50',   'M70',   'M90']

    # x =     [ 43000,  37000,   31000,    24500,    18500,     13000,    7500,    2000,   -3000,   -8500,  -14500,  -19500,  -25000,
    #           42000,  36500,   31000,    26000,    20500,     15000,    9500,    4200,   -3800,  -10000,  -18000,  -26000]

    # y =     [ -8500,  -8500,   -8500,    -8500,    -8700,     -8700,   -8700,   -8500,   -8500,   -8500,   -8500,   -8500,   -8500,
    #            4000,   4000,    4000,     4000,     4000,      4000,    4000,    4200,    4200,    4200,    4200,    4200]

    names = [
        "M725",
        "M825",
        "M1000",
        "TF50T",
        "TF70T",
        "TF90T",
        "TF725",
        "TF825",
        "TF1000",
        "TF30",
        "TF50",
        "TF70",
        "TF90",
        "DT20",
        "DT35",
        "DT50",
        "BLANK",
        "M30",
        "M50",
        "M70",
        "M90",
    ]

    x = [
        43000,
        37700,
        30000,
        2000,
        -3000,
        -8500,
        -14500,
        -19500,
        -25000,
        42000,
        36500,
        31000,
        26000,
        20500,
        15000,
        9500,
        4200,
        -3800,
        -10000,
        -18000,
        -26000,
    ]

    y = [
        -8500,
        -8700,
        -8700,
        -8500,
        -8500,
        -8500,
        -8500,
        -8500,
        -8500,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4200,
        4200,
        4200,
        4200,
        4200,
    ]

    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 2).tolist()+ np.arange(2490, 2501, 5).tolist()
    energies = 7 + np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = [60]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        ys = ys - 200
        xs = xs - 400

        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 500, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_3.2m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="AB", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def waxs_hard_Xray_Su3_2022_1(t=1):
    """
    307830_Su3 Feb 16, 2022
    """

    dets = [pil900KW, pil1M]

    # Included all the samples mounted on the sample bar
    names = [
        "M725",
        "M825",
        "M1000",
        "TF725T",
        "TF825T",
        "TF1000T",
        "TF30T",
        "TF50T",
        "TF70T",
        "TF90T",
        "TF725",
        "TF825",
        "TF1000",
        "TF30",
        "TF50",
        "TF70",
        "TF90",
        "DT20",
        "DT35",
        "DT50",
        "BLANK",
        "M30",
        "M50",
        "M70",
        "M90",
    ]

    x = [
        43500,
        37800,
        29000,
        24500,
        18500,
        13000,
        7700,
        2200,
        -2800,
        -8300,
        -14200,
        -19600,
        -24800,
        42000,
        36800,
        31500,
        26000,
        20500,
        15000,
        9700,
        4200,
        -3800,
        -10000,
        -18000,
        -26000,
    ]

    y = [
        -8500,
        -8500,
        -8500,
        -8500,
        -8500,
        -8500,
        -8500,
        -8300,
        -8500,
        -8500,
        -8300,
        -8300,
        -8500,
        4200,
        4200,
        4200,
        4200,
        4200,
        4200,
        4200,
        4000,
        4000,
        4000,
        4000,
        4000,
    ]

    waxs_arc = [0, 20, 40]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        det_exposure_time(t, t)

        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            while abs(piezo.y.position - ys) > 100:
                yield from bps.mv(piezo.y, ys)
                yield from bps.sleep(10)

            name_fmt = "{sample}_{sdd}m_{energy}eV_wa{wax}_bpm{xbpm}"
            bpm = xbpm2.sumX.get()
            e = energy.energy.position
            sdd = pil1m_pos.z.position / 1000

            sample_name = name_fmt.format(
                sample=name,
                sdd="%.1f" % sdd,
                energy="%.0f" % e,
                wax=wa,
                xbpm="%4.3f" % bpm,
            )
            sample_id(user_name="AB", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count(dets, num=1)



def waxs_S_edge_greg_2024_1(t=1):
    """
    307830_Su Feb 2, 2024
    """

    dets = [pil900KW, pil1M]

    names = ['N211_AR', 'NC700_AR', 'NC700_H', 'Pemion', 'Pemion_X1']
    x =     [    17500,       8500,      1500,    -6500,      -14500]
    y =     [    -7500,      -7500,     -7400,    -7400,       -7400]


    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 2).tolist()+ np.arange(2490, 2501, 5).tolist()
    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()
                              + np.arange(2490, 2501, 5).tolist())
    
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1500, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
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

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="GS", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)




def swaxs_S_edge_greg_2024_2(t=1):
    """
    307830_Su Feb 2, 2024
    """

    dets = [pil900KW, pil1M]

    names = ['SO3_particle_1', 'SO3_particle_2', 'SO3_particle_3', 'SO3_particle_4']
    x =     [          -19200,           -25100,           -30500,           -36100]
    y =     [            6000,             6500,             6000,             6000]


    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 2).tolist()+ np.arange(2490, 2501, 5).tolist()
    energies = 7+np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()
                              + np.arange(2490, 2501, 5).tolist())
    
    waxs_arc = [20]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 0, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_3.0m_{energy}eV_wa{wax}_bpm{xbpm}"
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

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="GS", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def nexafs_Ce_edge_greg_2024_1(t=1):
    """
    307830_Su Feb 2, 2024
    """

    dets = [pil900KW, pil1M]

    names = ['test_nexafs']
    x =     [         8500]
    y =     [        -7500]

    dets = [pil900KW]
    det_exposure_time(t, t)

    energies = np.linspace(5710, 5760, 51)

    energies = np.asarray(np.arange(5700, 5720, 5).tolist() + np.arange(5720, 5727, 1).tolist() + np.arange(5727, 5737, 0.5).tolist() + np.arange(5737, 5747, 2).tolist()
                            + np.arange(5747, 5780, 5).tolist())
    
    waxs_arc = [40]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 0, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
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

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="GS", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 5740)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 5710)
            yield from bps.sleep(2)



def swaxs_Ce_edge_greg_2024_1(t=1):
    """
    307830_Su Feb 2, 2024
    """

    dets = [pil900KW, pil1M]

    names = ['NC700_AR', 'NC700_H']
    x =     [      7500,       500]
    y =     [     -7500,     -7500]

    det_exposure_time(t, t)

    energies = np.asarray(np.arange(5700, 5720, 5).tolist() + np.arange(5720, 5727, 1).tolist() + np.arange(5727, 5737, 0.5).tolist() + np.arange(5737, 5747, 2).tolist()
                            + np.arange(5747, 5790, 5).tolist())
    
    waxs_arc = [40, 20, 0]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_sdd5100_{energy}eV_wa{wax}_bpm{xbpm}"
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

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="GS", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 5750)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 5700)
            yield from bps.sleep(2)



def swaxs_S_edge_nafion_2024_2(t=1):
    """
    307830_Su June 23, 2024
    """

    dets = [pil900KW, pil1M]

    names = [ 'kapton', 'ppion_zrox01', 'ppion_zrox02', 'nafion212', 'P25-0p25',  'P25-0p5',    'P25-1',      'P25-2', 
              'P25-4',    'AHPP25-0p5',  'AHPP25-0p25',  'AHPP25-1', 'AHPP25-2', 'AHPP25-4',    'P5A-4',
               'P5A-2',        'P5A-1',      'P5A-0p5',  'P5A-0p25', 'AHPP5A-4',  'AHPP5-2', 'AHPP5A-1', 'AHPP5A-0p5', 
         'AHPP5A-0p25',        'LK-01',        'LK-02',     'LK-03',    'LK-04',    'LK-05']
    x =     [    42000,          33000,          26000,       18000,      12000,       5000,          0,        -5000,
                -10000,         -15000,         -19000,      -24000,     -29000,     -33000,     -38000,
                 45000,          40000,          35000,       30000,      26000,      21500,      16000,        11000,
                  6000,              0,          -5000,      -10000,     -18000,     -25000]
    y =     [    -8000,          -8000,          -8000,       -8000,      -8000,      -8000,      -8000,        -8000,
                 -8000,          -8000,          -8000,       -8000,      -8000,      -8000,      -8000,
                  4500,           4500,           4500,        4500,       4500,       4500,       4500,         4500,
                  4500,           4900,           4900,        4900,       4900,       4900]
    z =     [     2000,           2000,           2000,        1500,       1500,       1000,       1000,         1000,
                   500,            500,            500,           0,          0,          0,          0,
                  2000,           2000,           2000,        2000,       1500,       1500,       1000,         1000,
                  1000,            500,            500,           0,          0,          0]


    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.5).tolist() + np.arange(2480, 2490, 2).tolist()+ np.arange(2490, 2501, 5).tolist()
    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()
                              + np.arange(2490, 2501, 5).tolist())
    
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1500, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
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

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="GS", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def bpmvspindiode_Sedge_2024_2(t=1):
    dets = [pil1M]
    det_exposure_time(t, t)

    name = 'Greg_Su_direct_beam_Sedge_scannormal'


    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()
                              + np.arange(2490, 2501, 5).tolist())
    
    # yield from bp.list_scan([energy, xbpm2, xbpm3, pdcurrent2], energy, list_ener)

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

        name_fmt = "{sample}_{energy}eV_bpm2_{xbpm2}_bpm3_{xbpm3}_pd_{pd}"

        sample_name = name_fmt.format(sample=name, energy="%6.2f"%e, xbpm2="%4.3f"%bpm2, xbpm3="%4.3f"%bpm3, pd="%4.3f"%pdc)
        sample_id(user_name="LR", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from bp.count([pil1M], num=1)

        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2450)




def swaxs_hardxray_nafion_2024_2(t=1):
    """
    307830_Su June 23, 2024
    """

    dets = [pil900KW, pil1M]

    names = [ 'kapton', 'ppion_zrox01', 'ppion_zrox02', 'nafion212', 'P25-0p25',  'P25-0p5',    'P25-1',      'P25-2', 
              'P25-4',    'AHPP25-0p5',  'AHPP25-0p25',  'AHPP25-1', 'AHPP25-2', 'AHPP25-4',    'P5A-4',
               'P5A-2',        'P5A-1',      'P5A-0p5',  'P5A-0p25', 'AHPP5A-4',  'AHPP5-2', 'AHPP5A-1', 'AHPP5A-0p5', 
         'AHPP5A-0p25',        'LK-01',        'LK-02',     'LK-03',    'LK-04',    'LK-05']
    x =     [    42000,          33000,          26000,       18000,      12000,       5000,          0,        -5000,
                -10000,         -15000,         -19000,      -24000,     -29000,     -33000,     -38000,
                 45000,          40000,          35000,       30000,      26000,      21500,      16000,        11000,
                  6000,              0,          -5000,      -10000,     -18000,     -25000]
    y =     [    -8000,          -8000,          -8000,       -8000,      -8000,      -8000,      -8000,        -8000,
                 -8000,          -8000,          -8000,       -8000,      -8000,      -8000,      -8000,
                  4500,           4500,           4500,        4500,       4500,       4500,       4500,         4500,
                  4500,           4900,           4900,        4900,       4900,       4900]
    z =     [     2000,           2000,           2000,        1500,       1500,       1000,       1000,         1000,
                   500,            500,            500,           0,          0,          0,          0,
                  2000,           2000,           2000,        2000,       1500,       1500,       1000,         1000,
                  1000,            500,            500,           0,          0,          0]


    waxs_arc = [0, 20, 40]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_1.8m_16100.0eV_wa{wax}"

            sample_name = name_fmt.format(sample=name, wax=wa)
            sample_id(user_name="GS", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count(dets, num=1)







# 3 pm on Monday 24 June
# matt's bar w/ 9 samples for hard x-ray saxs/waxs (10 measurements since one sample has two positions)

def swaxs_hardxray_mrl_2024_2(t=1):
    """
    307830_Su June 23, 2024
    """

    dets = [pil900KW, pil1M]

    names = [             'xle-ctrl',               'xle-01',       'xle-02',           'xle-03',    'xle-04',    'xle-05',
              'alaska-filter1a-pos1', 'alaska-filter1a-pos2',  'kapton-ctrl',  'kapton-filter1b']
        
    x =     [                  43000,                  34000,          27000,              19000,       13000,      5000, 
                              -14300,                 -17300,         -26300,             -36300]
    y =     [                  -8500,                  -8500,          -8500,              -8500,       -8500,     -8500, 
                               -7900,                  -7900,          -7600,              -7600]
    z =     [                   2000,                   2000,           2000,               2000,        2000,      2000, 
                                2000,                   2000,           2000,               2000]


    waxs_arc = [0, 20, 40]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_1.8m_16100.0eV_wa{wax}"

            sample_name = name_fmt.format(sample=name, wax=wa)
            sample_id(user_name="GS", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count(dets, num=1)





def saxs_hardxray_capillaries_2024_2(t=0.1):
    """
    307830_Su June 24, 2024
    """

    dets = [pil1M]

    #names = [  'capillary-AgB', '144D7-20CuAc', '144D6-20CuAc', '144D5-20CuAc', '144Z-20CuAc', '144A-20CuAc',
     #          '93N-24', '109I-12CuAc', '109I-12CuAc-cloudy', '124Z6-20', '105D6-20CuAc', '105D5-20CuAc',
      #         '105Z-20CuAc', '107-Adam-SV', 'Adam-SAN15']
        
    #x =     [ -42000, -35500,  -29000, -22700, -16400, -10000, -3800, 2800, 9100, 15600 , 21700 , 28500, 34500 ,41100, 47600   ]
    #y =     [ -2500, -2500, -2500, -2500, -2500, -2500, -2500 , -2500 , -2500,  -2500 , -2500, -2500,  -2500 ,-2500 ,      -2500   ]
    #z =     [ 2000, 2000, 2000, 2000, 2000, 2000, 2000 , 2000, 2000,  2000 , 2000, 2000,  2000 ,2000,  2000 ]


    names = [  'capillary-AgB']
    
    x =     [ -42000  ]
    y =     [ -2500   ]
    z =     [ 2000    ]



    waxs_arc = [40]

    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)

            name_fmt = "{sample}_1.8m_16100.0eV_wa{wax}"

            sample_name = name_fmt.format(sample=name, wax=wa)
            sample_id(user_name="GS", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count(dets, num=1)




















def saxs_hardxray_mrl_capillaries_2024_2(t=1):
    """
    307830_Su June 24, 2024
    """

    dets = [pil1M]
    #names = [  'capillary-AgB']
    
   # x =     [ -42000  ]
    #y =     [ -8200   ]
    #z =     [ 2000    ]
    #sample names for bar 1, measured under vacuum, may have popped, may need to redo 
    names = [  '144D7-20CuAc', '144D6-20CuAc', '144D5-20CuAc', '144Z-20CuAc', '144A-20CuAc',
               '93N-24', '109I-12CuAc', '109I-12CuAc-cloudy', '124Z6-20', '105D6-20CuAc', '105D5-20CuAc',
               '105Z-20CuAc', '107-Adam-SV', 'Adam-SAN15']
        
    x =     [ -35500,  -29000, -22700, -16400, -10000, -3800, 2800, 9100, 15600 , 21700 , 28500, 34500 ,41100, 47600   ]
    y =     [ -2500, -2500, -2500, -2500, -2500, -2500 , -2500 , -2500,  -2500 , -2500, -2500,  -2500 ,-2500 ,      -2500   ]
    z =     [  2000, 2000, 2000, 2000, 2000, 2000 , 2000, 2000,  2000 , 2000, 2000,  2000 ,2000,  2000 ]




    #Sample names for bar 2
    names = ['Adam-SAN25', 'N-blend', '91N1', '91N1-MgAc02', '91N1-MgAc04',
            '91N1-MgAc1', '91N1-MgAc17','91N1-MgAc2', '91N1-CuAc03','91N1-CuAc05',
            '91N1-CuAc08', '91N1-CuAc11', '91N1-CuAc18']
    
    #positions
    x =     [ -42000, -35500, -29400, -22800, -16300,    -10000, -3500, 2600, 8900, 15400, 21900,  28200, 34400  ]
    y =     [ -2500, -2500, -2500, -2500, -2500, -2500 , -2500 , -2500,  -2500 , -2500, -2500,  -2500 ,-2500  ]
    z =     [  2000, 2000, 2000, 2000, 2000, 2000 , 2000, 2000,  2000 , 2000, 2000,  2000 ,2000 ]

   
    # sample names for bar 3
    names = ['tulasi-water', 'tulasi-01a', 'tulasi-01b', 'tulasi-02a', 'tulasi-02b', 'tulasi-03a', 'tulasi-03b']
    x = [             21200,        15800,         7800,         1300,        -6300,        -9900,      -17900 ]
    y = [             -1000,         -500,        -1000,        -1000,        -1000,        -1000,       -1000 ]
    z = [              2000,         2000,         2000,         2000,         2000,         2000,        2000 ]



    for name, xs, ys in zip(names, x, y):
        # changing ys to allow for more room during dense energy scan
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        det_exposure_time(t, t)

        name_fmt = "{sample}_1.8m_16100.0eV"

        sample_name = name_fmt.format(sample=name)
        sample_id(user_name="ML", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from bp.count([pil1M], num=1)



'''  notes from eliot for 2024-2 blade coating
thorlabs_su is the thorlabs motor, it's a normal motor record, so you can set .velocity

syringe_pu is the syringe pump, but I would suggest changing the component names to volume, rate and run rather than x1, x2, x3


matt notes:
- "value" parameters dont seem to work on syringe pump, but the start/stop commands do, so we'll use time and the syringe diameter (defined manually on the syringe pump) to control our rate and volume dispensing
- files are not saved properly, we'll deal with that later

'''



def alignment_blade_coating_2024_2(coating_start_pos, measurement_pos,th):

    yield from bps.mv(thorlabs_su, measurement_pos)
    yield from alignement_gisaxs_hex(angle=th)

    yield from bps.mvr(stage.th, th)
    yield from bps.mvr(stage.y, 0.05)

    yield from bps.mv(thorlabs_su, coating_start_pos)







def blade_coating_2024_2(sample_name='bladecoating', coating_start_pos=10, measurement_pos=87, th=0.16, dets = [pil1M, pil900KW]):
    # dets = ['pil900KW','pil1M']

    yield from shopen()
    yield from bps.sleep(1)
    yield from shopen()
    yield from bps.sleep(1)
    yield from shopen()
    yield from bps.sleep(2)
    
    yield from bps.mv(thorlabs_su, thorlabs_su.position)
    yield from alignment_blade_coating_2024_2(coating_start_pos, measurement_pos,th)

    #det_exposure_time(0.5,300)
    det_exposure_time(2, 600)
    sample_id(user_name='ML', sample_name=sample_name)
    yield from bps.mv(syringe_pu.x3, 1) 
    yield from bps.sleep(2.5)
    yield from bps.mv(syringe_pu.x4, 1)
    
    yield from bps.mv(thorlabs_su, measurement_pos)
    
    
    yield from bp.count(dets)

    yield from shclose()
    yield from bps.sleep(1)
    yield from shclose()
    yield from bps.sleep(1)
    yield from shclose()



def take_data():
    
    det_exposure_time(0.5,10)
    yield from bp.count([pil1M])



    
def syringe_pump_testing():
    yield from bps.mv(syringe_pu.x3, 1) 
    yield from bps.sleep(2.5)
    yield from bps.mv(syringe_pu.x4, 1)


def thorlabs_testing():
    yield from bps.mv(thorlabs_su, thorlabs_su.position)
    yield from bps.mv(thorlabs_su, 87)
    yield from bps.mv(thorlabs_su, 10)


def saxs_hardxray_inair_capillaries_2024_2(t=0.5):
    """
    307830_Su June 25, 2024
    MRL, in-air environemtn (same AgB as blade coating stage)
    moving the hexapod stage instead of SmarAct

    more capillaries and thin films on the morning (2am) of june 27, MRL
    """

    dets = [pil1M]

 
    # sample names
    names = ['tulasi03a-pos1', 'tulasi03a-pos2',  'tulasi02b-pos1', 'tulasi02b-pos2', 'tulasi02a-pos1', 'tulasi02a-pos2']
    x_hexa = [            1.0,              1.2,               7.5,              7.5,             13.7,             13.7]
    y_hexa = [            0.2,              1.5,                 0,              1.5,                0,              2.2]
    z_hexa = [            0.1,                0,                 0,                0,                0,                0]

    names = ['tulasi01b-pos1', 'tulasi01b-pos2',  'tulasi01a-pos1', 'tulasi01a-pos2', 'tulasi01a-pos3']
    x_hexa = [            1.2,              1.2,               7.0,              7.4,              7.7]
    y_hexa = [            0.2,              2.0,               1.4,             -7.5,             -8.8]
    z_hexa = [            0.1,                0,                 0,                0,                0]

    names     = [         'mostafa00',       'mostafa01', 'mostafa02', 'mostafa03', 'mostafa04', 'mostafa05', 'mostafa06', 'mostafa07', 
                 'tulasi-kapton-ctrl', 'tulasi-kapton-01a', 'tulasi-kapton-01b', 'tulasi-kapton-02a' ]
    x_smaract = [               19000,              8000,        1000,       -7000,      -14000,      -22000,      -27000,      -33000,
                               -37000,              -40000,              -46500,              -54500 ]
    y_smaract = [               -7000,             -7000,       -7000,       -7000,       -7000,       -7000,       -7000,       -7000,
                                -7000,               -7000,               -6500,               -5500 ]
   

    for name, xs_smaract, ys_smaract in zip(names, x_smaract, y_smaract):
        #yield from bps.mv(stage.x, xs_hexa)
        #yield from bps.mv(stage.y, ys_hexa)

        yield from bps.mv(piezo.x, xs_smaract)
        yield from bps.mv(piezo.y, ys_smaract)

        det_exposure_time(t, t)

        name_fmt = "{sample}_8.3m_16100.0eV"

        sample_name = name_fmt.format(sample=name)
        sample_id(user_name="ML", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from bp.count([pil1M], num=1)










def alignment_static_swaxs_2024_2(th=0.16):

    yield from bps.mv(thorlabs_su, thorlabs_su.position)
    yield from alignement_gisaxs_hex(angle=th)

    yield from bps.mvr(stage.th, th)
    yield from bps.mvr(stage.y, 0.05)















def waxs_hardxray_inair_2024_2(t=1):


    dets = [pil900KW]

 
    # sample names
    names     = ['tulasi-kapton-ctrl', 'tulasi-kapton-01a', 'tulasi-kapton-01b', 'tulasi-kapton-02a' ]
    x_smaract = [              -37000,              -40000,              -46500,              -54500 ]
    y_smaract = [               -7000,               -7000,               -6500,               -5500 ]
    
    
    names =     ['alaska-filter1a', 'alaska-filter1a-acid', 'alaska-filter1b', 'alaska-filter3a-pristine',       
                 'alaska-filter3b-fouled', 'alaska-filter3b-acid' ]
    x_smaract = [            17000,                    3000,             -5000,                     -18500,
                                   -27000,                 -33500 ]
    y_smaract = [            -1000,                   -1000,             -1000,                      -1000,
                                    -1000,                  -1000 ]


    names = ['AgB-thinfilm']
    x_smaract = [-40000]
    y_smaract = [-500]



    waxs_arc = [0, 20, 40]
    
    
    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)

        for name, xs_smaract, ys_smaract in zip(names, x_smaract, y_smaract):
            #yield from bps.mv(stage.x, xs_hexa)
            #yield from bps.mv(stage.y, ys_hexa)

            yield from bps.mv(piezo.x, xs_smaract)
            yield from bps.mv(piezo.y, ys_smaract)

            det_exposure_time(t, t)

            name_fmt = "{sample}_8.3m_16100.0eV_wa{wax}"

            sample_name = name_fmt.format(sample=name, wax=wa)
            sample_id(user_name="ML", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count([pil900KW], num=1)



def saxs_hardxray_inair_june27_2024_2(t=1):


    dets = [pil1M]

 
    # sample names
    names =     ['kapton-psp4vp-ctrl', 'kapton-psp4vp-20wt', 'kapton-ctrl']
    x_smaract = [              -35000,                -5000,         20000]
    y_smaract = [               -1500,                -1500,         -1500]



    names     = ['105D6-20CuAc',  '105D5-20CuAc',      '105Z-20CuAc']
    x_smaract = [-46000, -22000, 7000 ]
    y_smaract = [-6500, -7500, -7000 ]


    waxs_arc = [40]
    
    
    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)

        for name, xs_smaract, ys_smaract in zip(names, x_smaract, y_smaract):
            #yield from bps.mv(stage.x, xs_hexa)
            #yield from bps.mv(stage.y, ys_hexa)

            yield from bps.mv(piezo.x, xs_smaract)
            yield from bps.mv(piezo.y, ys_smaract)

            det_exposure_time(t, t)

            name_fmt = "{sample}_8.3m_16100.0eV_wa{wax}"

            sample_name = name_fmt.format(sample=name, wax=wa)
            sample_id(user_name="ML", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count([pil1M], num=1)





def acq_delay(dets,exp_time,delay,num):
    det_exposure_time(exp_time,exp_time)
    yield from bp.count(dets,num,delay)


def blade_coating_acqdelay_2024_2(sample_name='bladecoating', coating_start_pos=10, measurement_pos=87, th=0.16, dets = [pil1M, pil900KW]):
    # dets = ['pil900KW','pil1M']

    yield from shopen()
    yield from bps.sleep(1)
    yield from shopen()
    yield from bps.sleep(1)
    yield from shopen()
    yield from bps.sleep(2)
    
    yield from bps.mv(thorlabs_su, thorlabs_su.position)
    yield from alignment_blade_coating_2024_2(coating_start_pos, measurement_pos,th)

    #det_exposure_time(0.5,300)
    
    sample_id(user_name='ML', sample_name=sample_name)
    yield from bps.mv(syringe_pu.x3, 1) # start pump
    yield from bps.sleep(2.5)
    yield from bps.mv(syringe_pu.x4, 1) # stop pump
    
    yield from bps.mv(thorlabs_su, measurement_pos)
    
    yield from acq_delay(dets=dets, exp_time=1, delay=4, num= 120)

    yield from shclose()
    yield from bps.sleep(1)
    yield from shclose()
    yield from bps.sleep(1)
    yield from shclose()











def swaxs_Br_edge_capillaries_2024_2(t=1):
    """
    315602 June 28, 2024
    MRL
    """

    dets = [pil900KW]

    names = [ 'carly01', 'carly02', 'carly03', 'carly04', 'carly05', 'carly06', 'carly07', 'carly08', 'carly09']
    x =     [    -43700,    -37400,    -31100,    -24800,    -18500,    -12000,     -5700,       700,     7050 ]
    y =     [     -6000,     -4620,     -4620,     -4620,     -4620,     -4620,     -4620,     -4620,    -4620 ]
    z =     [      2000,      2000,      2000,      2000,      2000,      2000,      2000,      2000,     2000 ]
 
    energies_swaxs = np.asarray(np.arange(13440, 13460, 5).tolist() +
                          np.arange(13460, 13480, 2).tolist() +
                          np.arange(13490, 13520, 10).tolist() )
    
    energies_swaxs_add = np.asarray([13420, 13480, 13485 ])
    
    energies_nexafs = np.asarray(np.arange(13440, 13520, 2))



    waxs_arc_swaxs = [0, 20, 40]
    waxs_arc_nexafs = [40]

    waxs_arc = waxs_arc_swaxs
    energies = energies_swaxs_add


    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)

        for name, xs, ys in zip(names, x, y):
            # changing ys to allow for more room during dense energy scan
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)

            yss = np.linspace(ys, ys + 1500, len(energies))
            xss = np.array([xs])

            yss, xss = np.meshgrid(yss, xss)
            yss = yss.ravel()
            xss = xss.ravel()



            det_exposure_time(t, t)

            name_fmt = "{sample}_4.0m_{energy}eV_wa{wax}_bpm{xbpm}"
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

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f"%bpm)
                sample_id(user_name="ML", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 13480)
            yield from bps.mv(energy, 13440)














