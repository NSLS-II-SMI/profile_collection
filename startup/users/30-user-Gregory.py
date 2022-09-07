def waxs_S_edge_Gregory_2022_2(t=0.5):
    """
    Based on waxs_S_edge_gordon_2021_2 from 30-user-Gordon
    and modified for GU-309504 Gregory. SAXS ssd 1.6 m.
    """
    # detectors will be defined later in the macro -> inside the waxc_arc cycle!
    # dets = [pil1M, pil900KW]

    # x and y are top center position on the sample
    names_a = [
        "0_pristine",
        "1_hT",
        "2_hT-6",
        "3_hT-25",
        "4_hT-400",
        "5_hTe",
        "6_hPTe-1pt5",
        "7_hTe-3",
        "8_hTe_400",
        "9_sintu30_reverse",
        "10_sintu50_reverse",
    ]
    x_a = [41000, 35400, 29400, 24100, 17800, 11900, 6600, 1200, -5000, -17600, -26100]
    y_a = [-7500, -7525, -7595, -7595, -7440, -7495, -7440, -7590, -7470, -6670, -6670]

    names_b = [
        "11_hB",
        "12_hB-1pt5",
        "13_hB-3",
        "14_hB-400",
        "15_copoly",
        "16_copoly-1pt5",
        "17_copoly-3",
        "18_copoly-400",
        "19_sintu70_reverse",
        "20_sintu90_reverse",
    ]
    x_b = [35300, 29800, 23800, 17600, 11600, 5600, 100, -5900, -17400, -31400]
    y_b = [5180, 5156, 5556, 5156, 5106, 5056, 5106, 5006, 6006, 6006]

    # names = names_a + names_b
    # x = x_a + x_b
    # y = y_a + y_b

    # Rerunning some samples
    names = names_a[-2:] + names_b[-2:]
    x = x_a[-2:] + x_b[-2:]
    y = y_a[-2:] + y_b[-2:]

    # Move all x values by + xxx um to be at the centre in x
    x = (np.array(x) + 0).tolist()
    y = (np.array(y) + 0).tolist()

    # Energies for sulphur
    energies = (
        np.arange(2448, 2478, 5).tolist()
        + np.arange(2478, 2488, 0.25).tolist()
        + np.arange(2488, 2498, 1).tolist()
        + np.arange(2498, 2503, 5).tolist()
    )

    # Energies for chlorine
    # energies = np.arange(2810, 2820, 5).tolist() + np.arange(2820, 2825, 1).tolist() + np.arange(2825, 2835, 0.25).tolist() + np.arange(2835, 2840, 0.5).tolist() + np.arange(2840, 2850, 5).tolist() + np.arange(2850, 2910, 10).tolist()
    # waxs_arc = np.linspace(7, 67, 4)
    # may26: mrl ran "reverse" arc angles to test beam damage
    waxs_arc = np.linspace(67, 7, 4)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs, piezo.y, ys)

        # Cover a range of 1 mm in y to avoid damage
        yss = np.linspace(ys, ys + 900, len(energies))
        # Stay at the same x position
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            # Do not read SAXS if WAXS is in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            det_exposure_time(t, t)

            name_fmt = "{sample}_{energy}eV_wa{wax}_sdd{sdd}m_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()
                sdd = pil1m_pos.z.position / 1000

                sample_name = name_fmt.format(
                    sample=name,
                    energy="%6.2f" % e,
                    wax=str(wa).zfill(4),
                    sdd="%.1f" % sdd,
                    xbpm="%4.3f" % bpm,
                )
                sample_id(user_name="AA", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            # Go back gently with energy
            yield from bps.mv(energy, 2480)
            yield from bps.mv(energy, 2450)
            # yield from bps.mv(energy, 2870)
            # yield from bps.mv(energy, 2840)


def spectroscopy_scan(t=0.3):
    """
    Quick energy scan to see where the edge (Pt M3) in on the sample
    """
    user_name = "test"
    sample_name = "test"

    sample_id(user_name=user_name, sample_name=sample_name)
    det_exposure_time(t, t)
    yield from bps.mv(waxs, 40)
    yield from bp.scan([pil900KW], energy, 2620, 2660, 21)
    yield from bps.mv(energy, 2640)
    yield from bps.mv(energy, 2620)
    yield from bps.mv(energy, 2600)


def waxs_Pt_L_edge_Gregory_2022_2(t=0.3):
    """
    Scan samples across Pt L edge
    """

    # detectors will be defined later in the macro -> inside the waxc_arc cycle!
    # dets = [pil1M, pil900KW]

    # x and y are top left position on the sample
    names = ["Pt-1", "Pt-2", "Pt-3"]
    x = [41235, 33235, 26235]
    y = [1000, 1000, 1000]

    # Energies for platinum L edge
    energies = np.concatenate(
        (
            np.arange(11530, 11550, 2),
            np.arange(11550, 11580, 1),
            np.arange(11580, 11620, 2),
        )
    )
    # energies = [12000]
    waxs_arc = np.linspace(7, 47, 3)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs, piezo.y, ys)

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            # Do not read SAXS if WAXS is in the way
            dets = [pil900KW] if wa < 15 else [pil1M, pil900KW]
            det_exposure_time(t, t)

            # Stay at the same x and y positions
            yss = np.array([ys])
            xss = np.array([xs])

            yss, xss = np.meshgrid(yss, xss)
            yss = yss.ravel()
            xss = xss.ravel()

            name_fmt = "{sample}_{energy}eV_wa{wax}_sdd{sdd}m_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()
                sdd = pil1m_pos.z.position / 1000

                sample_name = name_fmt.format(
                    sample=name,
                    energy="%6.2f" % e,
                    wax=str(wa).zfill(4),
                    sdd="%.1f" % sdd,
                    xbpm="%4.3f" % bpm,
                )
                sample_id(user_name="SG", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            # Go back gently with energy
            yield from bps.mv(energy, 11600)
            yield from bps.mv(energy, 11570)
            yield from bps.mv(energy, 11555)
            yield from bps.mv(energy, 11530)


def waxs_Te_edge_Gregory_2022_2(t=0.35):
    """
    Tellurium L edge TReXS, based on waxs_S_edge_2022_2 above. SAXS ssd 1.6 m.
    """
    # detectors will be defined later in the macro -> inside the waxc_arc cycle!
    # dets = [pil1M, pil900KW]

    # x and y are top center position on the sample
    # names_a = ['0_pristine', '1_hT', '2_hT-6', '3_hT-25', '4_hT-400', '5_hTe', '6_hPTe-1pt5', '7_hTe-3', '8_hTe_400']
    # x_a = [40500, 34800, 28800, 23500, 17200, 11350, 6000, 300, -5500]
    # y_a = [-7800, -7800, -7900, -7900, -7750, -7750, -7750, -7800, -7700]
    names_a = ["00_pristine_0pt35s", "6_hPTe-1pt5", "7_hTe-3", "8_hTe_400"]
    x_a = [40100, 5760, 300, -5800]
    y_a = [-7650, -7680, -7750, -7680]

    # names_b = ['11_hB', '12_hB-1pt5', '13_hB-3', '14_hB-400', '15_copoly', '16_copoly-1pt5']
    # x_b = [34380, 29000, 23000, 16800, 10820, 4820]
    # y_b = [5000, 5000, 4470, 4900, 4900, 4850]

    names = ["16_copoly-1pt5"]
    x = [4820]
    y = [4850]

    # names = names_a + names_b
    # x = x_a + x_b
    # y = y_a + y_b

    # Move all x values by + xxx um to be at the centre in x
    x = (np.array(x) - 60).tolist()
    y = (np.array(y) + 0).tolist()

    # Energies for Tellurium
    energies = (
        np.arange(4320, 4345, 5).tolist()
        + np.arange(4345, 4350, 2.5).tolist()
        + np.arange(4350, 4360, 0.4).tolist()
        + np.arange(4360, 4380, 2).tolist()
        + np.arange(4380, 4400, 5).tolist()
    )

    waxs_arc = np.linspace(7, 67, 4)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs, piezo.y, ys)

        # Cover a range of 0.9 mm in y and 0.24 mm in x to avoid damage
        yss = np.linspace(ys, ys + 900, len(energies))
        # xss = np.linspace(xs, xs + 240, len(waxs_arc))

        # Stay at the same x position
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            yield from bps.mvr(piezo.x, 60)

            # Do not read SAXS if WAXS is in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            det_exposure_time(t, t)

            name_fmt = "{sample}_{energy}eV_wa{wax}_sdd{sdd}m_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                # yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()
                sdd = pil1m_pos.z.position / 1000

                sample_name = name_fmt.format(
                    sample=name,
                    energy="%6.2f" % e,
                    wax=str(wa).zfill(4),
                    sdd="%.1f" % sdd,
                    xbpm="%4.3f" % bpm,
                )
                sample_id(user_name="AA", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            # Go back gently with energy
            yield from bps.mv(energy, 4375)
            yield from bps.mv(energy, 4350)
            yield from bps.mv(energy, 4320)


def waxs_Ca_edge_Gregory_2022_2(t=0.5):
    """
    Calcium K edge TReXS, based on waxs_S_edge_2022_2 above ad revised for Ca edge. SAXS ssd 1.6 m.
    """
    # detectors will be defined later in the macro -> inside the waxc_arc cycle!
    # dets = [pil1M, pil900KW]

    # x and y are top left position on the sample
    # two bars for these samples since washers are massive
    names = []
    x = []
    y = []

    # names = [            ]
    #    x = [            ]
    #    y = [            ]

    # Energies for Calcium K edge
    energies = (
        np.arange(4030, 4040, 5).tolist()
        + np.arange(4040, 4050, 0.25).tolist()
        + np.arange(4050, 4060, 1).tolist()
        + np.arange(4060, 4070, 2.5).tolist()
        + np.arange(4070, 4080, 5).tolist()
    )

    waxs_arc = np.linspace(7, 67, 4)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs, piezo.y, ys)

        # Cover a range of 1 mm in y to avoid damage
        yss = np.linspace(ys, ys + 900, len(energies))

        # Stay at the same x position
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            # Do not read SAXS if WAXS is in the way
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

            det_exposure_time(t, t)

            name_fmt = "{sample}_{energy}eV_wa{wax}_sdd{sdd}m_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()
                sdd = pil1m_pos.z.position / 1000

                sample_name = name_fmt.format(
                    sample=name,
                    energy="%6.2f" % e,
                    wax=str(wa).zfill(4),
                    sdd="%.1f" % sdd,
                    xbpm="%4.3f" % bpm,
                )
                sample_id(user_name="AA", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            # Go back gently with energy
            yield from bps.mv(energy, 4060)
            yield from bps.mv(energy, 4045)
            yield from bps.mv(energy, 4030)


def waxs_S_edge_Gregory_2022_1(t=0.5):
    """
    Based on waxs_S_edge_gordon_2021_2 from 30-user-Gordon
    and modified for GU-309504 Gregory. SAXS ssd 1.6 m.
    """
    dets = [pil1M, pil900KW]

    # x and y are top left position on the sample
    names_a = ["1-P3RT_doped", "2-P3RTe_doped", "3-blend_doped", "4-copolymer_doped"]
    x_a = [34225, 28275, 21525, 15375]
    y_a = [-250, -175, -175, -75]

    names_b = [
        "5-P3RT_undoped",
        "6-P3RTe_undoped",
        "7-blend_undoped",
        "8-copolymer_undoped",
        "9-control_empty",
    ]
    x_b = [5625, -425, -6825, -13345, -21225]
    y_b = [-100, -125, -275, -255, -175]

    names = names_a + names_b
    x = x_a + x_b
    y = y_a + y_b

    # Move all x values by + xxx um to be at the centre in x
    x = (np.array(x) + 600).tolist()
    y = (np.array(y) - 50).tolist()

    # Energies for sulphur
    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()

    # Energies for chlorine
    energies = (
        np.arange(2810, 2820, 5).tolist()
        + np.arange(2820, 2825, 1).tolist()
        + np.arange(2825, 2835, 0.25).tolist()
        + np.arange(2835, 2840, 0.5).tolist()
        + np.arange(2840, 2850, 5).tolist()
        + np.arange(2850, 2910, 10).tolist()
    )
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
                sample_id(user_name="AA", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            # Go back gently with energy
            # yield from bps.mv(energy, 2470)
            # yield from bps.mv(energy, 2450)
            yield from bps.mv(energy, 2870)
            yield from bps.mv(energy, 2840)


def giwaxs_shawn_2022_2(t=0.5):
    """
    GIWAXS macro for 309504 Gregory
    """
    user_name = "SG"

    # Samples and coordinates
    # first bar: Georgia Tech GIWAXS, PEDOT and DPP samples
    # names = ['1_p20','2_p40','3_p60','4_p80','5_p100','6_p150','7_DPP_S3_pristine','8_DPP_S3_8','9_DPP_S3_1','10_DPP_S3_0pt25','11_DPP_Se3_pristine','12_DPP_Se3_8','13_DPP_Se3_1','14_DPP_Se3_0pt25', '15_DPP_O3_pristine','16_DPP_O3_8','17_DPP_O3_1','18_DPP_O3_0pt25']
    # x_piezo = [-58500, -50525, -50525, -46525, -40525, -34525, -28525, -20525, -11525, -4525, 475, 7475, 13475, 19475, 27475, 37475, 44475, 52475]
    # y_piezo = [ 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]
    # z_piezo = [ 1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1500]
    # x_hexa =  [  -10, -10, -2.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # second bar: Georgia Tech GIWAXS, ALD samples
    # names = ['19_w1','20_w2','21_w3','22_w4','23_w5','24_w6','25_w7','26_w8','27_w9','28_w10','29_w11','30_w12']
    # x_piezo = [47980, 47980, 47980, 47980, 44485, 35485, 30985, 24985, 17485, 8985, 2985, -6015]
    # y_piezo = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]
    # z_piezo = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
    # x_hexa =  [19, 13.5, 7.5, 2, 0, 0, 0, 0, 0, 0, 0, 0]

    # redo a few in second bar
    names = ["25redo_w7"]
    x_piezo = [29985]
    y_piezo = [4600]
    z_piezo = [1500]
    x_hexa = [0]

    # Checks
    assert len(x_piezo) == len(
        names
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(
        z_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(
        x_hexa
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    # Geometry conditions
    waxs_angles = [0, 20]
    inc_angles = [0.1, 0.25]
    det_exposure_time(t, t)

    # Go over samples and thier positions
    for name, xs, zs, ys, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, 0.5)

        # Align sample
        yield from alignement_gisaxs(angle=0.1)

        ai0 = piezo.th.position

        # Go over WAXS detector angles
        for wa in waxs_angles:
            yield from bps.mv(waxs, wa)
            dets = [pil900KW] if wa < 15 else [pil900KW, pil1M]

            # Go over different incident angles
            for ai in inc_angles:
                yield from bps.mv(piezo.th, ai0 + ai)

                # Metadata
                name_fmt = "{sample}_{energy}eV_wa{wax}_sdd{sdd}m_bpm{xbpm}_ai{ai}"
                bpm = xbpm3.sumX.get()
                e = energy.energy.position / 1000
                sdd = pil1m_pos.z.position / 1000

                sample_name = name_fmt.format(
                    sample=name,
                    energy="%.1f" % e,
                    sdd="%.1f" % sdd,
                    wax=str(wa).zfill(4),
                    xbpm="%4.3f" % bpm,
                    ai="%.1f" % ai,
                )
                sample_id(user_name=user_name, sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                # Take data
                yield from bp.count(dets, num=1)
            yield from bps.mv(piezo.th, ai0)


def run_waxs_simple_2022_2(t=1):

    # sintu's transmission WAXS samples (from UCB)
    samples = [
        "0_blank",
        "1_Au1",
        "2_Au3thin",
        "4_alkyl",
        "5_Bquick",
        "6_DEG",
        "7_Au3thick",
        "8_F1thick",
        "9_Bslow",
    ]
    xlocs = [19485, 13485, 7735, 1985, -4765, -10965, -17765, -23965, -29465]
    ylocs = [2250, 2250, 2000, 2250, 2250, 2000, 2000, 2000, 2250]

    user = "SG"

    # Check if the length of xlocs, ylocs and names are the same
    assert len(xlocs) == len(
        samples
    ), f"Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil900KW]
    waxs_range = np.linspace(0, 40, 3)

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if wa < 15 else [pil900KW, pil1M]

        for sam, x, y in zip(samples, xlocs, ylocs):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            name_fmt = "{sam}_wa{waxs}_12keV_2m"
            sample_name = name_fmt.format(sam=sam, waxs="%2.1f" % wa)
            sample_id(user_name=user, sample_name=sample_name)

            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=1)


def waxs_Te_edge_Gregory_2022_2_mrl_june(t=0.35):
    """
    Tellurium L edge TReXS, based on waxs_S_edge_2022_2 above. SAXS ssd 8.3 m.
    """
    # detectors will be defined later in the macro -> inside the waxc_arc cycle!
    # dets = [pil1M, pil900KW]

    names = ["mrl_copoly_med", "mrl_copoly_high", "mrl_copoly_pristine"]
    x = [-18700, -24500, -12400]
    y = [-8800, -9000, -8800]

    # Move all x values by + xxx um to be at the centre in x
    x = (np.array(x) - 0).tolist()
    y = (np.array(y) + 0).tolist()

    # Energies for Tellurium
    energies = (
        np.arange(4320, 4345, 5).tolist()
        + np.arange(4345, 4350, 2.5).tolist()
        + np.arange(4350, 4360, 0.4).tolist()
        + np.arange(4360, 4380, 2).tolist()
        + np.arange(4380, 4400, 5).tolist()
    )

    waxs_arc = (27, 47, 67)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs, piezo.y, ys)

        # Cover a range of 0.9 mm in y and 0.24 mm in x to avoid damage
        yss = np.linspace(ys, ys + 900, len(energies))
        # xss = np.linspace(xs, xs + 240, len(waxs_arc))

        # Stay at the same x position
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            yield from bps.mvr(piezo.x, 60)

            # Do not read SAXS if WAXS is in the way
            dets = [pil900KW] if wa < 10 else [pil900KW]

            det_exposure_time(t, t)

            name_fmt = "{sample}_{energy}eV_wa{wax}_sdd{sdd}m_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                # yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()
                sdd = pil1m_pos.z.position / 1000

                sample_name = name_fmt.format(
                    sample=name,
                    energy="%6.2f" % e,
                    wax=str(wa).zfill(4),
                    sdd="%.1f" % sdd,
                    xbpm="%4.3f" % bpm,
                )
                sample_id(user_name="ML", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            # Go back gently with energy
            yield from bps.mv(energy, 4375)
            yield from bps.mv(energy, 4350)
            yield from bps.mv(energy, 4320)
