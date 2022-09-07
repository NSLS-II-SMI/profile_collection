def giwaxs_S_edge_wenkai(t=1):
    dets = [pil300KW]

    names = ["A2", "A3", "A4", "A5", "A6"]
    x = [30000, 16000, 0, -15000, -36000]

    energies = (
        np.arange(2450, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = np.linspace(0, 26, 5)
    ai0 = 0

    for name, xs in zip(names, x):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.th, ai0)

        yield from bps.mv(GV7.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(GV7.open_cmd, 1)
        yield from bps.sleep(1)

        yield from alignement_gisaxs(angle=0.4)

        # yield from bps.mv(att2_9, 'Insert')
        yield from bps.mv(GV7.close_cmd, 1)
        yield from bps.sleep(1)
        # yield from bps.mv(att2_9, 'Insert')
        yield from bps.mv(GV7.close_cmd, 1)
        yield from bps.sleep(1)

        ai0 = piezo.th.position
        yield from bps.mv(piezo.th, ai0 + 0.7)

        xss = np.linspace(xs, xs - 8000, 57)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)
            name_fmt = "{sample}_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss in zip(energies, xss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

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


def nexafs_S_edge_wenkai(t=1):
    dets = [pil300KW]
    names = ["PFSA_LSC"]
    x = [41200]
    y = [-8000]
    z = [2700]

    energies = np.linspace(2450, 2500, 51)

    energies = (
        np.arange(2450, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    energies1 = 10 + np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )

    for name, xs in zip(names, x):

        det_exposure_time(t, t)
        name_fmt = "nexafs_{sample}_{energy}eV_wa52.00_bpm{xbpm}"
        for e in energies:
            yield from bps.mv(energy, e)
            yield from bps.sleep(1)

            bpm = xbpm2.sumX.value

            sample_name = name_fmt.format(
                sample=name, energy="%6.2f" % e, xbpm="%4.3f" % bpm
            )
            sample_id(user_name="GF", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2450)


def hardxray_wenkai2020_1(t=1):
    dets = [pil300KW, pil1M]

    names = [
        "PFSA_LSC",
        "PFSA_LSC",
        "N2200_vert",
        "N2200_hori",
        "A1",
        "A2",
        "B1",
        "B2",
        "C1",
        "C2",
        "D1",
        "D2",
        "A3",
        "B3",
        "C3",
        "D3",
    ]
    x = [
        41000,
        29000,
        -8000,
        -30000,
        43800,
        37500,
        32500,
        27500,
        22500,
        17100,
        12100,
        5900,
        -16900,
        -21900,
        -27300,
        -32500,
    ]
    y = [
        -8000,
        -8000,
        -8000,
        -8000,
        3800,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4200,
    ]
    z = [
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
        2700,
    ]

    waxs_arc = np.linspace(0, 39, 7)

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)

        for name, xs, ys, zs in zip(names, x, y, z):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            yield from bps.mv(piezo.z, zs)

            det_exposure_time(t, t)
            name_fmt = "{sample}_16.1keVeV_8.3m_wa{wax}"

            yield from bps.sleep(1)

            sample_name = name_fmt.format(sample=name, wax=wa)
            sample_id(user_name="WZ", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)


def waxs_S_edge_wenkai_2021_1(t=1):

    dets = [pil1M, pil300KW]

    # names = ['PFSA_LSC', 'PFSA_SSC', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'A3', 'B3', 'C3', 'D3']
    # x = [41000, 28000,  43300, 37600, 32700, 27500, 21700, 16600, 11300, 5900, -17600, -22600, -28100, -33100]
    # y = [-8500, -8500,   3800,  4000,  3900,  4200,  4100,  4100,  3800, 3900,   3900,   4100,   4100,   4200]
    # z = [ 2700,  2700,   2700,  2700,  2700,  2700,  2700,  2700,  2700, 2700,   2700,   2700,   2700,   2700]

    energies = (
        np.arange(2450, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    # energies1 = 10 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())
    # waxs_arc = np.linspace(13, 19.5, 2)

    # for k, wa in enumerate(waxs_arc):
    #     yield from bps.mv(waxs, wa)

    #     for name, xs, ys, zs in zip(names, x, y, z):
    #         yield from bps.mv(piezo.x, xs)
    #         yield from bps.mv(piezo.y, ys)
    #         yield from bps.mv(piezo.z, zs)

    #         yss = np.linspace(ys, ys + 700, 29)
    #         xss = np.array([xs, xs + 500])

    #         yss, xss = np.meshgrid(yss, xss)
    #         yss = yss.ravel()
    #         xss = xss.ravel()

    #         det_exposure_time(t,t)
    #         name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
    #         for e, xsss, ysss in zip(energies1, xss, yss):
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(1)

    #             yield from bps.mv(piezo.y, ysss)
    #             yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm2.sumX.value

    #             sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
    #             sample_id(user_name='WZ', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)

    #         yield from bps.mv(energy, 2470)
    #         yield from bps.mv(energy, 2450)

    names = ["N2200_vert", "N2200_hori"]
    x = [-8500, -30500]
    y = [-8500, -8000]
    z = [2700, 2700]

    waxs_arc = np.linspace(0, 19.5, 4)

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        for name, xs, ys, zs in zip(names, x, y, z):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            yield from bps.mv(piezo.z, zs)

            yss = np.linspace(ys, ys + 1000, 29)
            xss = np.array([xs, xs + 500])

            yss, xss = np.meshgrid(yss, xss)
            yss = yss.ravel()
            xss = xss.ravel()
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
                sample_id(user_name="WZ", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def wenkai_waxs_tensile_tender_2021_2(t=1):
    # 85s to do the loop
    dets = [pil300KW, pil1M]

    names = "SSC_loop4_waxs"
    t0 = time.time()
    # yield from bps.mvr(stage.y, -0.4)

    for i in range(60):
        det_exposure_time(t, t)
        yield from bps.mvr(stage.y, 0.03)

        if waxs.arc.position > 5:
            wa = [19.5, 13, 6.5, 0]
        else:
            wa = [0, 6.5, 13, 19.5]

        t1 = time.time()
        for wax in wa:
            name_fmt = "{sample}_2455.0eV_sdd3m_{time}s_{i}_wa{wa}"

            yield from bps.mv(waxs, wax)
            sample_name = name_fmt.format(
                sample=names, time="%1.1f" % (t1 - t0), i="%3.3d" % i, wa="%1.1f" % wax
            )
            sample_id(user_name="GF", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)

        yield from bps.sleep(5)

    t2 = time.time()
    print(t2 - t0)


def wenkai_waxsonly_tensile_tender_2021_2(t=1):
    # 85s to do the loop
    dets = [pil300KW]

    names = "LSC_loop5_waxs_kaclamp"
    t0 = time.time()
    # yield from bps.mvr(stage.y, -0.4)

    for i in range(1000):
        det_exposure_time(t, t)
        yield from bps.mvr(stage.y, 0.01)

        t1 = time.time()
        name_fmt = "{sample}_2484.25eV_sdd3m_{time}s_{i}_wa{wa}"

        sample_name = name_fmt.format(
            sample=names, time="%1.1f" % (t1 - t0), i="%3.3d" % i, wa="%1.1f" % 0
        )
        sample_id(user_name="GF", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=1)

    t2 = time.time()
    print(t2 - t0)


def wenkai_saxsonly_tensile_tender_2021_2(t=1):
    # 85s to do the loop
    dets = [pil300KW, pil1M]

    names = "SSC_loop3_saxs"
    t0 = time.time()
    # yield from bps.mvr(stage.y, -0.4)

    for i in range(1000):
        det_exposure_time(t, t)
        yield from bps.mvr(stage.y, 0.005)

        t1 = time.time()
        name_fmt = "{sample}_2484.24eV_sdd3m_{time}s_{i}_wa{wa}"

        sample_name = name_fmt.format(
            sample=names, time="%1.1f" % (t1 - t0), i="%3.3d" % i, wa="%1.1f" % 8
        )
        sample_id(user_name="GF", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=1)

        yield from bps.sleep(0.5)

    t2 = time.time()
    print(t2 - t0)


def wenkai_saxs_waxs_tensile_hard(t=1):
    dets = [pil300KW, pil1M]

    names = "PF-T2PO1_loop1"
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t, t)

        if waxs.arc.position > 5:
            wa = [13, 6.5, 0]
        else:
            wa = [0, 6.5, 13]

        name_fmt = "{sample}_14000eV_{time}s_{i}_wa{wa}"
        t1 = time.time()
        for wax in wa:
            yield from bps.mv(waxs, wax)
            sample_name = name_fmt.format(
                sample=names, time="%1.1f" % (t1 - t0), i="%3.3d" % i, wa="%1.1f" % wax
            )
            sample_id(user_name="GF", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)


def wenkai_waxs_tensile_2021_3(t=0.5):
    names = "LSC_RT_loop1"

    dets = [pil900KW, pil300KW]
    wa = [0]
    yield from bps.mv(stage.y, 0.1)
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t, t)

        name_fmt = "{sample}_14keV_{time}s_{i}_wa{wa}"
        t1 = time.time()
        for wax in wa:
            yield from bps.mv(waxs, wax)
            sample_name = name_fmt.format(
                sample=names, time="%1.1f" % (t1 - t0), i="%3.3d" % i, wa="%1.1f" % wax
            )
            sample_id(user_name="GF", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)
            yield from bps.mvr(stage.y, 0.01)
            # yield from bps.sleep(2)


def wenkai_saxs_tensile_2021_3(t=0.5):
    names = "LSC_RT_loop6_samesample"

    dets = [pil1M]
    wa = [20]
    yield from bps.mv(stage.y, -0.3)
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t, t)

        name_fmt = "{sample}_2484.24keV_{time}s_{i}_wa{wa}"
        t1 = time.time()
        for wax in wa:
            yield from bps.mv(waxs, wax)
            sample_name = name_fmt.format(
                sample=names, time="%1.1f" % (t1 - t0), i="%3.3d" % i, wa="%1.1f" % wax
            )
            sample_id(user_name="GF", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)
            yield from bps.mvr(stage.y, 0.01)
            # yield from bps.sleep(2)
