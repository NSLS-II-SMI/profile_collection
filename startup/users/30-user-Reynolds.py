def new_folder(cycle, group):
    proposal_id(cycle, group)


def phong_waxs_S_edge_new(t=1):
    dets = [pil300KW]

    yield from bps.mv(GV7.close_cmd, 1)
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1)

    energies = (
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = np.linspace(0, 13, 3)

    yield from bps.mv(stage.th, 1)
    yield from bps.mv(stage.y, -8)
    names = ["C2C8C10_2_0per_2", "C2C8C10_20per_2", "C2C8C10_40per_2"]
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


def phong_waxs_Sedge_multi_2022_1(t=3):
    dets = [pil1M, pil900KW]

    energies = (
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = [0, 20, 40, 60]

    # initial run with t = 0.5 s
    # names = ['BCFH1','ACFH1','BCEH1','ACEH1','AgBehWasher','BlankSiNx','AgBehSiNx','EPSED','EPSEN','EPLiTFSI','EPSEN','EPSED','AgBehSiNx2','ACEH1','BCEH1','ACFH1','BCFH1']
    # x =     [17000,  11500,   6100,   1000,      -9000,        -18200,    -23300,  -29700, -35200,  -44800,   -34800, -29800,    -23800,     100,    5100, 10500,   16900]
    # y =     [4700,    4400,   4600,    4700,      3900,        4300,       4500,    4250,    4350,   -8900,   -8400,   -8600,    -8500,    -8300,   -8300,  -8100, -8300]

    # run with t = 3 s
    # names = ['complex50', 'complex60', 'complex75', 'complex90', 'complex100']
    # x = [44100, 21800, -700, -22800, -44400]
    # y = [900, -1800, 600, -2600, 400]

    # run with all samples except ACEH1 rotated by 90deg, t = 0.5
    # names = ['BCFH1','ACFH1','BCEH1','ACEH1','ADEH1','BDEH1','ADFH1','BDFH1', 'AgBehSiNx2']
    # x =     [16900,  11800,   6600,   1300,    300,    5500,   10900, 15900, -24000]
    # y =     [4600,    4600,   4600,   4450,  -8500,   -8100,  -8100,  -8100, -8100]

    # run with ACEH1 rotated by 90deg, t = 0.5
    # names = ['ACEH1', 'AgBehSiNx2']
    # x =     [19800,        -23800]
    # y =     [4450,        -8100]

    # run with t = 3 s
    names = ["complex50-2", "complex60-2", "complex75-2", "complex90-2", "complex100-2"]
    x = [43700, 21600, -1000, -23100, -44700]
    y = [900, -1800, 700, -2700, 200]

    assert len(names) == len(
        x
    ), f"Number of X coordinates ({len(names)}) is different from number of samples ({len(x)})"
    assert len(y) == len(
        x
    ), f"Number of X coordinates ({len(y)}) is different from number of samples ({len(x)})"

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 58)
        xss = np.linspace(xs, xs, 1)

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

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.get()

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="PN", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def song_waxs_S_edge_2022_1(t=0.5):
    # single energy scan in tensile stage
    dets = [pil1M, pil900KW]

    energies = (
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = [0, 20]

    names = ["sample_18l"]
    x = [-0.3]
    y = [-0.06]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(stage.x, xs)
        yield from bps.mv(stage.y, ys)

        yss = np.linspace(ys, ys + 1, 58)
        xss = np.linspace(xs, xs, 1)

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

                yield from bps.mv(stage.y, ysss)
                yield from bps.mv(stage.x, xsss)

                bpm = xbpm2.sumX.get()

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="SZ", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def song_saxs_tensile_hard(t=1):
    dets = [pil1M]

    names = "P3BT_loop2"

    t0 = time.time()
    for i in range(2000):

        det_exposure_time(t, t)
        name_fmt = "{sample}_10_18250eV_sdd1p6_{time}_{i}"
        t1 = time.time()
        sample_name = name_fmt.format(
            sample=names, time="%1.1f" % (t1 - t0), i="%3.3d" % i
        )
        sample_id(user_name="GF", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=1)

        time.sleep(20)


def song_saxs_waxs_tensile_hard(t=1):
    dets = [pil300KW, pil1M]

    names = "P3BT_loop2"
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t, t)

        if waxs.arc.position > 5:
            wa = [14, 7.5, 1]
        else:
            wa = [1, 7.5, 14]

        name_fmt = "{sample}_18250eV_{time}s_{i}_wa{wa}"
        t1 = time.time()
        for wax in wa:
            yield from bps.mv(waxs, wax)
            sample_name = name_fmt.format(
                sample=names, time="%1.1f" % (t1 - t0), i="%3.3d" % i, wa="%1.1f" % wax
            )
            sample_id(user_name="GF", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)


def song_tensile_tender_loop(t=1):
    # infinite time loop for contonuous data taking
    dets = [pil1M, pil900KW]

    names = "P77_loop1"
    t0 = time.time()
    for i in range(2000):
        det_exposure_time(t, t)

        if waxs.arc.position > 10:
            wa = [20, 0]
        else:
            wa = [0, 20]

        t1 = time.time()
        for wax in wa:
            if energy.energy.position > 2475:
                ener = [2478, 2470]
            else:
                ener = [2470, 2478]

            for ene in ener:
                name_fmt = "{sample}_{energy}eV_{time}s_{i}_wa{wa}"
                yield from bps.mv(energy, ene)

                yield from bps.mv(waxs, wax)
                sample_name = name_fmt.format(
                    sample=names,
                    energy="%6.2f" % ene,
                    time="%1.1f" % (t1 - t0),
                    i="%3.3d" % i,
                    wa="%1.1f" % wax,
                )
                sample_id(user_name="SZ", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)


def song_tensile_tender(t=0.4):
    # infinite time loop for contonuous data taking
    # dets = [pil1M, pil900KW]

    names = "P75_7_3_thickSEBS_50strain_cycle100_2"
    det_exposure_time(t, t)
    energies = [2470, 2476, 2478]

    if waxs.arc.position > 10:
        wa = [20, 0]
    else:
        wa = [0, 20]

    for wax in wa:
        dets = [pil900KW] if wax < 10 else [pil1M, pil900KW]

        if energy.energy.position > 2475:
            ener = energies[::-1]
        else:
            ener = energies

        for ene in ener:
            name_fmt = "{sample}_{energy}eV_{sdd}m_wa{wa}"
            yield from bps.mv(energy, ene)

            yield from bps.mv(waxs, wax)
            sdd = pil1m_pos.z.position / 1000

            sample_name = name_fmt.format(
                sample=names, energy="%6.2f" % ene, sdd="%.1f" % sdd, wa="%1.1f" % wax
            )
            sample_id(user_name="SZ", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)


def song_nexafs_S_2021_2(t=1):
    dets = [pil300KW]

    energies = (
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )
    waxs_arc = np.linspace(52, 52, 1)

    # names = ['1A1', '1A2', '2E3', '1A4']
    # x = [42500, 36500, 30500, 25000]
    # y = [-4700, -4800, -5200, -5400]

    # names=['1A6','1A7','1A8', '1A9','1A10','1A11', '1A12',  '1B1',  '1B2',  '1B3',  '1B4',  '1B5',
    #      '1B6', '1B7', '1B8', '1B9','1B11','1B12',   'D1',   'D2',   'D3',   'D4',   'D5',   'D6',   'D7',   'D8',   'D9', 'D10']
    # x = [20100, 13200,  8900,  3100, -2900, -9200, -14700, -20700, -26700, -33700, -38700, -43000,
    #      45200, 39800, 33800, 28800, 22800, 17300, 10300,   4300,   -700,  -7500, -12500, -17700, -23700, -29400, -35300, -40800]
    # y = [-5000, -6100, -4700, -4700, -4700, -5100,  -4800,  -4800,  -4800,  -4800,  -4800,  -4500,
    #       7500,  7400,  7700,  7700,  7700,  8000,  7800,   7500,   7500,   7700,   7700,   7700,   7000,   7700,   7700,   7100]

    names = [
        "D11",
        "D12",
        "1E1",
        "1E2",
        "1E3",
        "1E4",
        "1E5",
        "1E6",
        "1E7",
        "1E8",
        "1E9",
        "1E10",
        "2E1",
        "2E2",
        "2E4",
        "2E6",
        "2F1",
        "2F2",
        "2F3",
    ]
    x = [
        44800,
        38800,
        33800,
        27800,
        22800,
        16800,
        11300,
        5500,
        0,
        -5300,
        -11000,
        -17000,
        -22000,
        -27200,
        -33700,
        -40500,
        43300,
        37300,
        31400,
    ]
    y = [
        -5700,
        -5700,
        -5700,
        -5500,
        -5500,
        -5600,
        -5600,
        -5600,
        -5600,
        -5600,
        -5600,
        -5600,
        -5600,
        -4500,
        -4700,
        -4400,
        6800,
        6800,
        6800,
    ]

    assert len(names) == len(
        x
    ), f"Number of X coordinates ({len(names)}) is different from number of samples ({len(x)})"
    assert len(y) == len(
        x
    ), f"Number of X coordinates ({len(y)}) is different from number of samples ({len(x)})"

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t, t)
            name_fmt = "{sample}_nexafs_{energy}eV_wa{wax}_bpm{xbpm}"
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
