####line scan


def run_harv_temp(tim=0.5):
    # Slowest cycle:
    temperatures = [25]
    name = "ML"
    x_list = [-7000, 6000]
    y_list = [4900, 5100]
    samples = ["set7_sample1_3rdcycle", "set7_sample2_3rdcycle"]
    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil300KW]  # ALL detectors
    # dets = [pil300KW,ls.ch1_read, xbpm3.sumY] # WAXS detector ALONE

    x_offset = [0, 0, 400, 400]
    y_offset = [0, 50, 0, 50]
    zoff = -9000
    waxs_arc = np.linspace(0, 32.5, 6)
    name_fmt = "{sample}_pos{offset}_{temperature}C_wa{waxs}"
    yield from bps.mv(piezo.z, zoff)

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        if i_t != 0:
            yield from bps.sleep(600)
        temp = ls.ch1_read.value
        for j, wa in enumerate(waxs_arc):  #
            yield from bps.mv(waxs, wa)
            for x, y, s in zip(x_list, y_list, samples):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)
                for i_0, (x_0, y_0) in enumerate(zip(x_offset, y_offset)):
                    sample_name = name_fmt.format(
                        sample=s,
                        offset=i_0 + 1,
                        temperature="%3.1f" % temp,
                        waxs="%2.1f" % wa,
                    )
                    yield from bps.mv(piezo.x, x + x_0)
                    yield from bps.mv(piezo.y, y + y_0)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    sample_id(user_name=name, sample_name=sample_name)
                    yield from bp.count(dets, num=1)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)
    yield from bps.mv(ls.ch1_sp, 28)


def run_harv_temp_all_2022_1(tim=0.5):
    # Slowest cycle:
    temperatures = [30, 100, 180]
    # temperatures = [30, 100, 150]

    name = "ML"

    # x_list  = [-45880, -38480, -29480, -23480, -16700, -4700, 3300, 10300, 18300, 26300, 32700, 37600, 45800]
    # y_list =  [  6700,   6700,   6700,   6520,   6480,  6440, 6400,  6340,  6340,  6220,  6180,  6180,  6380]
    # samples = ['set1_MML_071', 'set1_MML_076', 'set1_MML_077', 'set1_MML_081', 'set1_MML_082-1', 'set1_MML_082-2', 'set1_MML_083-1',
    # 'set1_MML_083-2', 'set2_ST03457', 'set2_ST03866', 'set2_ST05874', 'set2_ST02670', 'set2_ST04180']

    # x_list  = [-42000, -34500, -27000, -21000, -14000, -8300, -2300, 5300, 13000, 19500, 26500, 32500, 40500, 49500]
    # y_list =  [  6630,   6630,   6530,   6330,   6530,  6330,  6130, 6230,  6330,  6030,  6130,  6130,  6330,  6230]
    # samples = ['set3_RM257_2.5', 'set3_RM257_5.0', 'set3_RM257_10.0', 'set3_RM257_15.0', 'set4_RM82_2.5', 'set4_RM82_5.0', 'set4_RM82_10.0',
    # 'set5_sample1', 'set7_700G', 'set7_790G', 'set7_600G', 'set7_250G', 'set10_sample1', 'set10_sample2d']

    # x_list  = [-48000, -40000, -32000, -25000, -20500, -16500, -11700, -6700, 3300, 15300, 26200, 32800, 41900, 49500]
    # y_list =  [  6580,   6580,   6880,   6730,   6830,   6830,   6330,  6430, 5030,  5030,  6730,  6670,  6630,  6690]
    # samples = ['set4_RM82_2.5-2', 'set4_RM82_15.0', 'set8_azo_2.5', 'set8_azo_5.0', 'set8_azo_5.0-2', 'set8_azo_10.0', 'set8_azo_15.0',
    # 'stex_MML-076', 'set11_symx_1', 'set11_symz_2', 'set6_SP1', 'set6_SP2', 'set6_SP3', 'set6_SP4']

    x_list = [-41000, -30500, -22500, -14000, -3000]
    y_list = [6620, 6500, 6580, 6400, 6220]
    samples = [
        "set9_ST04180",
        "set9_ST03866",
        "set9_ST03866_2",
        "set9_ST02670",
        "set9_ST05874",
    ]

    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil300KW]  # ALL detectors
    # dets = [pil300KW,ls.ch1_read, xbpm3.sumY] # WAXS detector ALONE

    x_offset = [0, 0, 400, 400]
    y_offset = [0, 50, 0, 50]
    zoff = -10000
    waxs_arc = np.linspace(0, 32.5, 6)
    name_fmt = "{sample}_2_pos{offset}_{temperature}C_wa{waxs}"
    yield from bps.mv(piezo.z, zoff)

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        if i_t != 0:
            yield from bps.sleep(600)

        temp = ls.ch1_read.value
        for j, wa in enumerate(waxs_arc):  #
            yield from bps.mv(waxs, wa)
            for x, y, s in zip(x_list, y_list, samples):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)
                if s == "set11_symx_1" or s == "set11_symz_2":
                    sample_name = name_fmt.format(
                        sample=s,
                        offset=0,
                        temperature="%3.1f" % temp,
                        waxs="%2.1f" % wa,
                    )
                    yield from bps.mv(piezo.x, x)
                    yield from bps.mv(piezo.y, y)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    sample_id(user_name=name, sample_name=sample_name)
                    yield from bp.scan(dets, piezo.y, y, y + 1110, 38)

                else:
                    for i_0, (x_0, y_0) in enumerate(zip(x_offset, y_offset)):
                        sample_name = name_fmt.format(
                            sample=s,
                            offset=i_0 + 1,
                            temperature="%3.1f" % temp,
                            waxs="%2.1f" % wa,
                        )
                        yield from bps.mv(piezo.x, x + x_0)
                        yield from bps.mv(piezo.y, y + y_0)
                        print(f"\n\t=== Sample: {sample_name} ===\n")
                        sample_id(user_name=name, sample_name=sample_name)
                        yield from bp.count(dets, num=1)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)
    yield from bps.mv(ls.ch1_sp, 28)


def temp_2021_3(tim=0.5):
    # Slowest cycle:
    # temperatures = [27, 45, 70, 100, 120, 150, 170, 30]
    temperatures = [30]

    name = "MW"

    # samples = ['set1_sam1', 'set1_sam2', 'set1_sam3', 'set1_sam4', 'set1_sam5', 'set1_sam6', 'set1_sam7', 'set1_sam8', 'set1_sam9', 'set1_sam10',
    #  'set1_sam11', 'set1_sam12','set1_sam13', 'set1_sam14', 'set1_sam15', 'set1_sam16']
    # x_list  = [49600, 45600, 41000, 35800, 29000, 23800, 17800, 7600,  800, -5000, -12500, -18900, -24500, -31300,-37900, -44300]
    # y_list =  [-8700, -8700, -9000, -8700,-8700, -8700, -8700, -8700, -8600, -8500, -8700, -8700,  -8600, -8700, -8450, -8450]

    samples = [
        "Sideon_7.5HDDA_zalignedrod",
        "Endon_2.5HDDA_zalignedrod_thick",
        "Endon_2.5HDDA_zalignedrod_thin_5CBswollen",
        "Endon_2.5HDDA_splayalignedrod_5CBswollen",
    ]
    x_list = [-40400, -35200, -26000, -18600, -11200, -3800, 2800]
    y_list = [400, 475, 450, 400, 250, 100, 225]

    # -24000 -50000
    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil900KW]  # ALL detectors

    x_offset = [0, 0, 400, 400, 800, 800, 1200, 1200]
    y_offset = [0, 50, 0, 50, 0, 50, 0, 50]
    waxs_arc = [0, 20]
    name_fmt = "{sample}_afterheating_18.25keV_1.6m_pos{offset}_{temperature}C_wa{waxs}"

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        t_kelvin = t + 273.15
        yield from ls.output1.mv_temp(t_kelvin)
        temp = ls.input_A.get()

        while abs(temp - t_kelvin) > 2:
            print(abs(temp - t_kelvin))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

        if i_t != 0:
            yield from bps.sleep(450)

        # temp = ls.input_A.get()
        t_celsius = temp - 273.15

        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            for x, y, s in zip(x_list, y_list, samples):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)

                # if s != 'set3_sam1':
                #     x_offset = [0, 0, 400, 400]
                #     y_offset = [0, 50, 0, 50]

                # else:
                #     x_offset = np.linspace(0, -26000, 27)
                #     y_offset = np.linspace(0, 0, 27)

                for i_0, (x_0, y_0) in enumerate(zip(x_offset, y_offset)):
                    sample_name = name_fmt.format(
                        sample=s,
                        offset=i_0 + 1,
                        temperature="%3.1f" % t_celsius,
                        waxs="%2.1f" % wa,
                    )
                    yield from bps.mv(piezo.x, x + x_0)
                    yield from bps.mv(piezo.y, y + y_0)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    sample_id(user_name=name, sample_name=sample_name)
                    yield from bp.count(dets, num=1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    t_kelvin = 25 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)


def temp_xscan_2022_1(tim=0.5):
    # Slowest cycle:
    # temperatures = [27, 45, 70, 100, 120, 150, 170, 30]
    temperatures = [30, 100, 180]

    name = "PQ"

    # samples = ['set1_sam1', 'set1_sam2', 'set1_sam3', 'set1_sam4', 'set1_sam5', 'set1_sam6', 'set1_sam7', 'set1_sam8', 'set1_sam9', 'set1_sam10',
    #  'set1_sam11', 'set1_sam12','set1_sam13', 'set1_sam14', 'set1_sam15', 'set1_sam16']
    # x_list  = [49600, 45600, 41000, 35800, 29000, 23800, 17800, 7600,  800, -5000, -12500, -18900, -24500, -31300,-37900, -44300]
    # y_list =  [-8700, -8700, -9000, -8700,-8700, -8700, -8700, -8700, -8600, -8500, -8700, -8700,  -8600, -8700, -8450, -8450]

    samples = ["A-0", "A-4", "A-5", "A-6", "A-7", "A-8"]
    x_list = [-15800, -34000, -19000, -8000, 6000, 19000]
    y_list = [-2200, 3630, 3540, 3510, 3900, 3870]
    y_range = [
        [0, 6000, 61],
        [0, 8000, 81],
        [0, 7000, 71],
        [0, 8000, 81],
        [0, 7500, 76],
        [0, 3500, 36],
    ]

    # -24000 -50000
    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil900KW]  # ALL detectors
    det_exposure_time(tim, tim)
    waxs_arc = [0, 20]
    name_fmt = "{sample}_16.1keV_1.6m_pos{offset}_{temperature}C_wa{waxs}"

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        t_kelvin = t + 273.15
        yield from ls.output1.mv_temp(t_kelvin)
        temp = ls.input_A.get()

        while abs(temp - t_kelvin) > 2:
            print(abs(temp - t_kelvin))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

        if i_t != 0:
            yield from bps.sleep(450)

        # temp = ls.input_A.get()
        t_celsius = temp - 273.15

        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            for x, y, s, x_r in zip(x_list, y_list, samples, x_range):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)

                for i_0, xrs in enumerate(np.linspace(x_r[0], x_r[1], x_r[2])):
                    sample_name = name_fmt.format(
                        sample=s,
                        offset=i_0 + 1,
                        temperature="%3.1f" % t_celsius,
                        waxs="%2.1f" % wa,
                    )
                    yield from bps.mv(piezo.x, x + xrs)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    sample_id(user_name=name, sample_name=sample_name)
                    yield from bp.count(dets, num=1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    t_kelvin = 25 + 273.15
    yield from ls.output1.mv_temp(t_kelvi % rn)


def temp_yscan_2022_1(tim=1):
    # Slowest cycle:
    # temperatures = [27, 45, 70, 100, 120, 150, 170, 30]
    temperatures = [30, 100, 180]

    name = "PQ"

    # samples = ['set1_sam1', 'set1_sam2', 'set1_sam3', 'set1_sam4', 'set1_sam5', 'set1_sam6', 'set1_sam7', 'set1_sam8', 'set1_sam9', 'set1_sam10',
    #  'set1_sam11', 'set1_sam12','set1_sam13', 'set1_sam14', 'set1_sam15', 'set1_sam16']
    # x_list  = [49600, 45600, 41000, 35800, 29000, 23800, 17800, 7600,  800, -5000, -12500, -18900, -24500, -31300,-37900, -44300]
    # y_list =  [-8700, -8700, -9000, -8700,-8700, -8700, -8700, -8700, -8600, -8500, -8700, -8700,  -8600, -8700, -8450, -8450]

    samples = ["A-0", "A-1", "A-2", "C-1-1", "C-1-2"]
    x_list = [-15800, -4800, 10200, 26030, 36190]
    y_list = [-2200, -2200, -2200, -400, 700]
    chi_list = [0, 0, 0, 4, 4.2]
    y_range = [
        [0, 2000, 11],
        [0, 2000, 11],
        [0, 2000, 11],
        [0, 1800, 91],
        [0, 1800, 91],
    ]

    # -24000 -50000
    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil900KW]  # ALL detectors

    waxs_arc = [0, 20]
    name_fmt = "{sample}_16.1keV_1.6m_pos{offset}_{temperature}C_wa{waxs}"

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        t_kelvin = t + 273.15
        yield from ls.output1.mv_temp(t_kelvin)
        temp = ls.input_A.get()

        while abs(temp - t_kelvin) > 2:
            print(abs(temp - t_kelvin))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

        if i_t != 0:
            yield from bps.sleep(450)

        # temp = ls.input_A.get()
        t_celsius = temp - 273.15

        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            for x, y, chi, s, y_r in zip(x_list, y_list, chi_list, samples, y_range):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)
                yield from bps.mv(piezo.ch, chi)

                for i_0, yrs in enumerate(np.linspace(y_r[0], y_r[1], y_r[2])):
                    sample_name = name_fmt.format(
                        sample=s,
                        offset=i_0 + 1,
                        temperature="%3.1f" % t_celsius,
                        waxs="%2.1f" % wa,
                    )
                    yield from bps.mv(piezo.y, y + yrs)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    sample_id(user_name=name, sample_name=sample_name)
                    yield from bp.count(dets, num=1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    t_kelvin = 25 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)


def hydrogel_2021_1(tim=0.5):

    x_list = [43900, 35000, 23500, 13500, 6000, -10700, -18500, -32400, -33800, -36400]
    y_list = [8700, -5300, -5300, -5300, 8700, 8700, -5300, 8700, 8700, 8700]
    samples = [
        "hyd_gel_Spindmso",
        "hyd_gel_sample2",
        "hyd_gel_sample3",
        "hyd_gel_sample9",
        "hyd_gel_sample10",
        "hyd_gel_sample5",
        "hyd_gel_sample11",
        "hyd_gel_sample6",
        "hyd_gel_sample7",
        "hyd_gel_sample8",
    ]

    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil300KW]  # ALL detectors

    x_offset = [0, 0, 0]
    y_offset = [-200, 0, 200]
    waxs_arc = np.linspace(0, 32.5, 6)
    name_fmt = "{sample}_18.25keV_1.6m_pos{offset}_wa{waxs}"

    det_exposure_time(tim, tim)

    for j, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
        for x, y, s in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for i_0, (x_0, y_0) in enumerate(zip(x_offset, y_offset)):
                sample_name = name_fmt.format(
                    sample=s, offset=i_0 + 1, waxs="%2.1f" % wa
                )
                yield from bps.mv(piezo.x, x + x_0)
                yield from bps.mv(piezo.y, y + y_0)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                sample_id(user_name="ML", sample_name=sample_name)
                yield from bp.count(dets, num=1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    t_kelvin = 25 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)


def run_harv_temp_all(tim=0.5):
    # Slowest cycle:
    temperatures = [100, 150]
    name = "ML"
    # x_list  = [-46300, -37300, -29800, -20300, -13800, -6200, 1300, 9000, 16700, 26300, 33300, 39300, 46300, 53000]
    # y_list =  [-8800, -8800, -8800, -8750, -8750, -8750, -9200, -9200, -9300, -9100, -9200, -9300, -8970, -9000]
    # samples = [ 'set1_sample1', 'set1_sample2','set1_sample3','set1_sample4','set1_sample5', 'set1_sample6', 'set3_sample1', 'set3_sample2','set3_sample3','set3_sample4','set3_sample5', 'set3_sample6','set2_sample3', 'set2_sample4']

    x_list = [42000, 28000, 13300, -7700, -14100]
    y_list = [-6800, -7800, -8800, -8800, -7800]
    samples = [
        "set6_headon_sample1",
        "set6_headon_sample2",
        "set6_headon_sample3",
        "set6_headon_sample4",
        "set6_headon_sample5",
    ]

    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil300KW]  # ALL detectors
    # dets = [pil300KW,ls.ch1_read, xbpm3.sumY] # WAXS detector ALONE

    x_offset = [0, 0, 400, 400]
    y_offset = [0, 50, 0, 50]
    zoff = -2000
    waxs_arc = np.linspace(0, 32.5, 6)
    name_fmt = "{sample}_pos{offset}_{temperature}C_wa{waxs}"
    yield from bps.mv(piezo.z, zoff)

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        if i_t != 0:
            yield from bps.sleep(600)
        temp = ls.ch1_read.value
        for j, wa in enumerate(waxs_arc):  #
            yield from bps.mv(waxs, wa)
            for x, y, s in zip(x_list, y_list, samples):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)
                for i_0, (x_0, y_0) in enumerate(zip(x_offset, y_offset)):
                    sample_name = name_fmt.format(
                        sample=s,
                        offset=i_0 + 1,
                        temperature="%3.1f" % temp,
                        waxs="%2.1f" % wa,
                    )
                    yield from bps.mv(piezo.x, x + x_0)
                    yield from bps.mv(piezo.y, y + y_0)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    sample_id(user_name=name, sample_name=sample_name)
                    yield from bp.count(dets, num=1)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)
    yield from bps.mv(ls.ch1_sp, 28)


def run_linkam_cooling(t=0.15, tim=0.15):
    name = "PQ"
    sample = "insitu_b-7"
    offset = 300  # microns
    # Detectors, motors:
    # dets = [pil900KW, pil1M]
    waxs_arc = [0, 20]
    name_fmt = "{sample}_wa{waxs}_time{ctime}s"
    now = time.time()
    det_exposure_time(t, tim)
    for i in range(100):
        yield from bps.mvr(piezo.x, offset)
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]
            ctime = time.time() - now
            sample_name = name_fmt.format(
                sample=sample, waxs="%2.1f" % wa, ctime="%.0f" % ctime
            )
            print(f"\n\t=== Sample: {sample_name} ===\n")
            sample_id(user_name=name, sample_name=sample_name)
            yield from bp.count(dets, num=1)
            yield from bps.sleep(120)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def run_harv_linkam_waxs(t=0.2, tim=20):
    name = "MW"
    sample = "InSitu_AzoSideon_spot2"
    offset = 600  # microns
    # Detectors, motors:
    dets = [pil900KW]
    waxs_arc = [7]
    name_fmt = "{sample}_{temperature}C_wa{waxs}"

    det_exposure_time(t, tim)

    temp = ls.input_A_celsius.get()
    yield from bps.mvr(piezo.x, offset)
    for j, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
        sample_name = name_fmt.format(
            sample=sample, temperature="%2.2f" % temp, waxs="%2.1f" % wa
        )
        print(f"\n\t=== Sample: {sample_name} ===\n")
        sample_id(user_name=name, sample_name=sample_name)
        # yield from bp.count(dets, num=1)
        pil900KW.cam.acquire.put(1)
        yield from bps.sleep(tim + 1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def run_harv_linkam_saxs(t=0.2, tim=20):
    name = "MW"
    sample = "InSitu_AzoSideonspot2"

    # Detectors, motors:
    dets = [pil1M]
    wa = 20
    name_fmt = "{sample}_{temperature}C"

    det_exposure_time(t, tim)

    temp = ls.input_A_celsius.get()
    yield from bps.mv(waxs, wa)
    sample_name = name_fmt.format(sample=sample, temperature="%2.2f" % temp)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    sample_id(user_name=name, sample_name=sample_name)
    # yield from bp.count(dets, num=1)
    pil1M.cam.acquire.put(1)
    yield from bps.sleep(tim + 1)


def run_harv_linkam(t=0.2, tim=20):
    yield from run_harv_linkam_saxs(t=t, tim=tim)
    yield from run_harv_linkam_waxs(t=t, tim=tim)


def run_harv_linkam_both(t=0.3, tim=0.3):
    name = "MW"
    names = [
        "endon_2.5HDDA_zalignedrod_pos1_lower",
        "endon_2.5HDDA_zalignedrod_pos2_lower",
        "endon_2.5HDDA_zalignedrod_pos3_lower",
        "endon_2.5HDDA_zalignedrod_pos4_lower",
        "endon_2.5HDDA_zalignedrod_pos5_lower",
        "endon_2.5HDDA_zalignedrod_pos6_lower",
        "endon_2.5HDDA_zalignedrod_pos7_lower",
    ]
    piezo_x = [-1651, -451, 749, 1949, 3149, 4349, 5549]
    piezo_y = [-3349, -3349, -3349, -3349, -3349, -3349, -3349]
    # sample = 'InSitu_AzoSideon_spot2'
    # Detectors, motors:
    dets = [pil1M]
    wa = 20
    name_fmt = "{sample}_{temperature}C"

    det_exposure_time(t, tim)

    temp = ls.input_A_celsius.get()
    yield from bps.mv(waxs, wa)

    for sample, x, y in zip(names, piezo_x, piezo_y):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_name = name_fmt.format(sample=sample, temperature="%2.2f" % temp)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        sample_id(user_name=name, sample_name=sample_name)
        yield from bp.count(dets, num=1)  # for singleshot
        # pil1M.cam.acquire.put(1) #next 2 lines for burst shots
        # yield from bps.sleep(tim+1)

    offset = 600  # microns
    # Detectors, motors:
    dets = [pil900KW]
    waxs_arc = [7]
    name_fmt = "{sample}_{temperature}C_wa{waxs}"

    yield from bps.mvr(piezo.x, offset)
    for j, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
        for sample, x in zip(names, piezo_x):
            yield from bps.mv(piezo.x, x + offset)
            sample_name = name_fmt.format(
                sample=sample, temperature="%2.2f" % temp, waxs="%2.1f" % wa
            )
            print(f"\n\t=== Sample: {sample_name} ===\n")
            sample_id(user_name=name, sample_name=sample_name)
            yield from bp.count(dets, num=1)  # for single shot
            # pil900KW.cam.acquire.put(1) #next 2 lines for burst shots
            # yield from bps.sleep(tim+1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def run_harv_temp_time(tim=0.2):
    name = "SL"
    sample = "InSitu_EndOn_NoCross_PhaseDia_40C_v3_UVlvl_0.5V"
    timegaps = [10] * 4 + [30] * 2 + [60] * 3
    # Detectors, motors:
    dets = [pil1M]
    waxs_arc = [19.5]
    name_fmt = "{sample}_{temperature}C_wa{waxs}"

    # Openinig the gate valve
    yield from bps.mv(GV7.open_cmd, 1)
    yield from bps.sleep(5)
    yield from bps.mv(GV7.open_cmd, 1)
    yield from bps.sleep(5)

    det_exposure_time(tim, tim)

    temp = ls.ch1_read.value
    for i, gap in enumerate(timegaps):
        sample = sample + "_timestep" + str(i)
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            sample_name = name_fmt.format(
                sample=sample, temperature="%2.2f" % temp, waxs="%2.1f" % wa
            )
            print(f"\n\t=== Sample: {sample_name} ===\n")
            sample_id(user_name=name, sample_name=sample_name)
            yield from bp.count(dets, num=1)
        yield from bps.sleep(gap)
    for j, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
        sample_name = name_fmt.format(
            sample=sample, temperature="%2.2f" % temp, waxs="%2.1f" % wa
        )
        print(f"\n\t=== Sample: {sample_name} ===\n")
        sample_id(user_name=name, sample_name=sample_name)
        yield from bp.count(dets, num=1)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    # Closing the gate valve
    yield from bps.mv(GV7.close_cmd, 1)
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1)
    yield from bps.sleep(5)


def harvphi(meas_t=0.5):
    waxs_arc = np.linspace(0, 32.5, 6)  # (2th_min 2th_max steps)
    dets = [pil300KW, pil1M]
    names = ["DDDA5_vert_100C"]
    # phis = np.linspace(-90, 90, 13)
    phis = np.linspace(-75, 75, 11)

    for name in names:
        det_exposure_time(meas_t, meas_t)

        name_fmt = "{sample}_phi{phi}deg_wa{waxs}"
        # waxs is the slowest cycle:
        for j, wa in enumerate(waxs_arc):  #
            yield from bps.mv(waxs, wa)
            # phi is scanned for a single waxs
            for i, phi in enumerate(phis):
                yield from bps.mv(prs, phi)
                sample_name = name_fmt.format(
                    sample=name, phi="%2.1f" % phi, waxs="%2.1f" % wa
                )
                sample_id(user_name="SL", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

        yield from bps.mv(prs, 0)
    sample_id(user_name="test", sample_name="test")


def run_harv_poly(tim=1, name="HarvPoly"):
    # Slowest cycle:
    temperatures = [85]
    x_list = [-1000]
    y_list = [-4740]
    samples = ["S29"]
    # Detectors, motors:
    dets = [pil300KW, ls.ch1_read, xbpm3.sumY]
    name_fmt = "{sample}_{temperature}C"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        # yield from bps.sleep(def run_harv_pos_scan(tim=3,name = 'Harv_SideOn_2.5_PA'):
    # x_list  = [-42000, -20400, 200, 20400, 44300]
    x_list = np.linspace(-5800, -13800, 17)
    # y_list =  [  5600,   5800, 5920, 5822,  5972]
    y_list = [-4400]

    # Detectors, motors:
    # dets = [pil1M, rayonix, pil300KW,ls.ch1_read, xbpm3.sumY] #ALL detectors
    dets = [pil300KW, ls.ch1_read, xbpm3.sumY]  # WAXS detector ALONE
    waxs_arc = [0, 30, 6]
    name_fmt = "{sample}_{xoffset}um_{temperature}C"
    #    param   = '16.1keV'
    det_exposure_time(tim, tim)
    yield from bps.mv(ls.ch1_sp, t)
    if i_t > 0:
        yield from bps.sleep(600)
    for x, y, s in zip(x_list, y_list, samples):
        temp = ls.ch1_read.value
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, 2800)
        for i_x, xo in enumerate(x_offset):
            sample_name = name_fmt.format(sample=s, xoffset=xo, temperature=temp)
            yield from bps.mv(piezo.x, x + x_offset[i_x])
            print(f"\n\t=== Sample: {sample_name} ===\n")
            sample_id(user_name=name, sample_name=sample_name)
            yield from bp.rel_scan(dets, piezo.y, *y_range)
    sample_id(user_name="test", sample_name="test")


def run_harv_micro(tim=3, name="HarvMicro_2_25C"):
    # Slowest cycle:
    temperatures = [150]
    # x_list  = [-42000, -20400, 200, 20400, 44300]
    x_list = [
        40016,
    ]
    # y_list =  [  5600,   5800, 5920, 5822,  5972]
    y_list = [
        -3880,
    ]
    samples = ["SC10", "SC11", "SC12", "SC13", "SC14", "SC15", "SC16", "SC17"]
    # samples = ['S29']
    # Detectors, motors:
    # dets = [pil1M, rayonix, pil300KW,ls.ch1_read, xbpm3.sumY] #ALL detectors
    dets = [pil300KW, ls.ch1_read, xbpm3.sumY]  # WAXS detector ALONE
    x_offset = [-704, -352, 0, 352, 704]
    y_range = [20, -20, 3]
    waxs_arc = [0, 30, 6]
    name_fmt = "{sample}_{xoffset}um_{temperature}C"
    #    param   = '16.1keV'
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        if i_t > 0:
            yield from bps.sleep(600)
        for x, y, s in zip(x_list, y_list, samples):
            temp = ls.ch1_read.value
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, 2800)
            for i_x, xo in enumerate(x_offset):
                sample_name = name_fmt.format(sample=s, xoffset=xo, temperature=temp)
                yield from bps.mv(piezo.x, x + x_offset[i_x])
                print(f"\n\t=== Sample: {sample_name} ===\n")
                sample_id(user_name=name, sample_name=sample_name)
                yield from bp.rel_scan(dets, piezo.y, *y_range)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)
    yield from bps.mv(ls.ch1_sp, 28)


def run_harv_pos(tim=5):
    # Slowest cycle:
    name = "SL"
    x_list = [np.linspace(27700, 28200, 26)]
    y_list = [-4400]
    samples = ["EndOn_1.5_HDDA_MicroStruct_Cap_Step20um_Area2"]

    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M, pil300KW]  # ALL detectors

    waxs_arc = [13]
    name_fmt = "{sample}_pos{offset}_wa{waxs}"

    det_exposure_time(tim, tim)
    for j, wa in enumerate(waxs_arc):  #
        yield from bps.mv(waxs, wa)

        for x, y, s in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.y, y)

            for i_0, x_0 in enumerate(x):
                yield from bps.mv(piezo.x, x_0)
                sample_name = name_fmt.format(
                    sample=s, offset=i_0 + 1, waxs="%2.1f" % wa
                )
                print(f"\n\t=== Sample: {sample_name} ===\n")
                sample_id(user_name=name, sample_name=sample_name)
                yield from bp.count(dets, num=1)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)
    yield from bps.mv(ls.ch1_sp, 28)


def mesh_milan_2022_2(t=0.5):
    waxs_range = [0, 20]

    dets = [pil900KW, pil1M]
    det_exposure_time(t, t)

    # these samples are very large areas and 3rd priority (lowest) except for the 1st teeth12.
    samples = [
        "20220801MW_C_1",
        "20220801MW_C_2",
        "20220801MW_C_3",
        "20220801MW_C_4",
        "20220801MW_C_5",
        "20220801MW_C_6",
        "20220801MW_C_7",
    ]
    x_list = [46200, 34900, 18050, 5950, -24710, -45660, -58760]
    y_list = [2940, 3310, 3840, 3980, 4170, 4320, 4370]
    z_list = [-2600, -2600, -2600, -2800, -2600, -2400, -2400]
    hexa_x = [16, 0, 0, 0, 0, 0, 0]
    th_list = [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
    x_range = [
        [0, 12000, 241],
        [0, 18000, 361],
        [0, 9000, 181],
        [0, 4000, 81],
        [0, 10000, 201],
        [0, 10000, 201],
        [0, 9000, 181],
    ]
    y_range = [
        [0, 700, 3],
        [0, 700, 3],
        [0, 100, 3],
        [0, 150, 3],
        [0, 200, 3],
        [0, 200, 3],
        [0, 200, 3],
    ]

    # first load room T
    # samples = ['20220801MW_C_1', '20220801MW_C_2','20220801MW_C_3', '20220801MW_C_4', '20220801MW_C_5', '20220801MW_C_6', '20220801MW_C_7']
    # x_list = [ 46100,              34800,                18050,            5950,            -24710,              -45660,            -58760]
    # y_list = [ 2940,               3310,                 3840,              3980,             4170,                4320 ,              4370]
    # z_list = [  -2600,           -2600,                 -2600,            -2800,             -2600,              -2400,              -2400]
    # hexa_x = [   16,               0,                   0,                 0,               0,                   0 ,                 0]
    # th_list = [0.7,               0.7,                 0.7,               0.7,              0.7,                 0.7,                0.7]
    # x_range=[ [0,12000,241],   [0,18000,361],       [0,9000,181],       [0,4000,81],     [0,10000,201],    [0,10000,201],      [0,9000,181]]
    # y_range=[ [0,700,3],        [0,700,3],          [0,100,3],          [0,150,3],       [0,200,3],         [0,200,3],           [0,200,3]]

    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    assert len(x_list) == len(
        x_range
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(x_range)})"
    assert len(x_list) == len(
        y_range
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_range)})"

    for x, y, z, th, hx, name, x_r, y_r in zip(
        x_list, y_list, z_list, th_list, hexa_x, samples, x_range, y_range
    ):
        # proposal_id('2021_3', 'Wang%s'%num)
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)
        yield from bps.mv(piezo.th, th)
        yield from bps.mv(stage.x, hx)

        for wa in waxs_range:
            yield from bps.mv(waxs, wa)
            dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]

            e = energy.position.energy / 1000  # energy keV
            sdd = pil1m_pos.z.position / 1000  # SAXS detector distance
            scan_id = db[-1].start["scan_id"] + 1  # transient scan ID
            proposal_id("2022_2", "310149_Wilborn/%s" % name)

            name_fmt = "{sample}_{energy}keV_sdd{sdd}m_wa{wax}_id{scan_id}_dx50um"
            sample_name = name_fmt.format(
                sample=name,
                energy="%.1f" % e,
                sdd="%.1f" % sdd,
                wax="%2.1f" % wa,
                scan_id=scan_id,
            )
            sample_name = sample_name.translate(
                {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =,"}
            )
            sample_id(user_name="MW", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r, 0)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)


def mesh_milan_temp_2022_2(t=0.5):
    waxs_range = [0, 20]
    temperatures = [100, 150]
    dets = [pil900KW, pil1M]
    det_exposure_time(t, t)

    # second load, heated stage
    samples = [
        "20220801MW_C_8",
        "20220801MW_C_10",
        "20220801MW_C_11",
        "20220801MW_C_12",
        "20220801MW_C_13",
        "20220801MW_C_14",
        "20220801MW_C_15",
    ]
    x_list = [37128, 27598, 9798, -8602, -23352, -28352, -49752]
    y_list = [3369, 3329, 3469, 3509, 3729, 4129, 3939]
    z_list = [-11300, -11300, -11300, -11300, -11300, -11300, -7300]
    hexa_x = [0, 0, 0, 0, 0, 0, 0]
    th_list = [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
    x_range = [
        [0, 18000, 361],
        [0, 5000, 101],
        [0, 8000, 161],
        [0, 9000, 181],
        [0, 8500, 171],
        [0, 7500, 151],
        [0, 8000, 161],
    ]
    y_range = [
        [0, 200, 3],
        [0, 100, 3],
        [0, 200, 3],
        [0, 200, 3],
        [0, 250, 3],
        [0, 150, 3],
        [0, 300, 3],
    ]

    # first load, heated stage
    # samples = ['20220801MW_C_1', '20220801MW_C_3', '20220801MW_C_4', '20220801MW_C_5', '20220801MW_C_6', '20220801MW_C_7']
    # x_list = [ 39500,                -1000,            -13500,          -27400,           -40800,            -52400]
    # y_list = [ 2970,                  3690,              3780,            3960,             4110 ,              4070]
    # z_list = [ -12100,               -12100,            -12100,          -12100,           -11300,              -11300]
    # hexa_x = [   0,                   0,                 0,                0,                0 ,                 0]
    # th_list = [0.7,                  0.7,               0.7,              0.7,              0.7,                0.7]
    # x_range=[ [0,12000,241],       [0,9000,181],       [0,8000,81],     [0,9000,181],    [0,10000,201],      [0,8000,11]]
    # y_range=[ [0,500,3],           [0,100,3],          [0,100,3],       [0,100,3],         [0,100,3],           [0,200,3]]

    # first load room T
    # samples = ['20220801MW_C_1', '20220801MW_C_2','20220801MW_C_3', '20220801MW_C_4', '20220801MW_C_5', '20220801MW_C_6', '20220801MW_C_7']
    # x_list = [ 46100,              34800,                18050,            5950,            -24710,              -45660,            -58760]
    # y_list = [ 2940,               3310,                 3840,              3980,             4170,                4320 ,              4370]
    # z_list = [  -2600,           -2600,                 -2600,            -2800,             -2600,              -2400,              -2400]
    # hexa_x = [   16,               0,                   0,                 0,               0,                   0 ,                 0]
    # th_list = [0.7,               0.7,                 0.7,               0.7,              0.7,                 0.7,                0.7]
    # x_range=[ [0,12000,241],   [0,18000,361],       [0,9000,181],       [0,4000,81],     [0,10000,201],    [0,10000,201],      [0,9000,181]]
    # y_range=[ [0,700,3],        [0,700,3],          [0,100,3],          [0,150,3],       [0,200,3],         [0,200,3],           [0,200,3]]

    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    assert len(x_list) == len(
        x_range
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(x_range)})"
    assert len(x_list) == len(
        y_range
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_range)})"

    for temperature in temperatures:
        t_kelvin = temperature + 273.15
        yield from ls.output1.mv_temp(t_kelvin)

        # Activate heating range in Lakeshore
        # if temperature < 80:
        #    yield from bps.mv(ls.output1.status, 1)
        # else:
        yield from bps.mv(ls.output1.status, 3)

        # Equalise temperature
        print(f"Equalising temperature to {temperature} deg C")
        start = time.time()
        temp = ls.input_A.get()
        while abs(temp - t_kelvin) > 1:
            print("Difference: {:.1f} K".format(abs(temp - t_kelvin)))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

            # Escape the loop if too much time passes
            if time.time() - start > 1800:
                temp = t_kelvin
        print(
            "Time needed to equilibrate: {:.1f} min".format((time.time() - start) / 60)
        )
        # Wait extra time depending on temperature
        if (35 < temperature) and (temperature < 181):
            yield from bps.sleep(300)

        # Read T and convert to deg C
        temp_degC = ls.input_A.get() - 273.15

        for x, y, z, th, hx, name, x_r, y_r in zip(
            x_list, y_list, z_list, th_list, hexa_x, samples, x_range, y_range
        ):
            # proposal_id('2021_3', 'Wang%s'%num)
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)
            yield from bps.mv(piezo.th, th)
            yield from bps.mv(stage.x, hx)

            for wa in waxs_range:
                yield from bps.mv(waxs, wa)
                dets = [pil900KW] if wa < 15 else [pil900KW, pil1M]

                e = energy.position.energy / 1000  # energy keV
                sdd = pil1m_pos.z.position / 1000  # SAXS detector distance
                scan_id = db[-1].start["scan_id"] + 1  # transient scan ID
                temp = str(np.round(float(temp_degC), 1)).zfill(5)
                proposal_id("2022_2", "310149_Wilborn1/%s" % name)

                name_fmt = "{sample}_{temp}degC_{energy}keV_sdd{sdd}m_wa{wax}_id{scan_id}_dx50um"
                sample_name = name_fmt.format(
                    sample=name,
                    temp=temp,
                    energy="%.1f" % e,
                    sdd="%.1f" % sdd,
                    wax="%2.1f" % wa,
                    scan_id=scan_id,
                )
                sample_name = sample_name.translate(
                    {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =,"}
                )
                sample_id(user_name="MW", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r, 0)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)
    # Turn off the heating and set temperature to 23 deg C
    t_kelvin = 23 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)
    yield from ls.output1.turn_off()


def linescan_milan_temp_2022_3(t=0.5):
    """
    Fine line scan on Linkam GI thermal stage
    """

    names =   ['MWA01','MWA02', 'MWA03','MWB01','MWB02','MWB03','MWB04','MWD01','FSB21','FSB23']

    piezo_x = [ 61200,  50700,     45850,  42750,   31000,  19300,       7650,      -4450, -32950, -42750]
    piezo_y = [  170,    380,     400,      610,   870,   1090,        1240,    1670,      2110,    2110]
    piezo_z = [   -3270,  -3270,    -3270,        -3270, -3270,    -3270,    -3270,    -3270, -3270, -3270]
    #piezo_z = [8400 for n in names]
    y_range = [[0, -9500, 96],[0,-4200,43], [0,-2100,22], [0, -10500, 106],[0, -10800, 109], [0,-11000,111], [0, -8800, 89], [0, -14500, 146], [0, -4000, 41], [0, -800, 9]]

    assert len(names) == len(piezo_x),  f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_x),  f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_z), f"Wrong list lenghts"
    assert len(piezo_z) == len(y_range), f"Wrong list lenghts"

    waxs_arc = [0, 20]
    temperatures = [38, 95, 150]


    for temperature in temperatures:
        t_kelvin = temperature + 273.15
        yield from ls.output1.mv_temp(t_kelvin)
        yield from bps.mv(ls.output1.status, 3)

        # Equalise temperature
        print(f"Equalising temperature to {temperature} deg C")
        start = time.time()
        temp = ls.input_A.get()
        while abs(temp - t_kelvin) > 3:
            print("Difference: {:.1f} K".format(abs(temp - t_kelvin)))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

            # Escape the loop if too much time passes
            if time.time() - start > 1800:
                temp = t_kelvin
        print(
            "Time needed to equilibrate: {:.1f} min".format((time.time() - start) / 60)
        )
        # Wait extra time depending on temperature
        if (35 < temperature) and (temperature < 181):
            yield from bps.sleep(300)

        # Read T and convert to deg C
        temp_degC = ls.input_A.get() - 273.15

        for name, x, y, z, scan_pts in zip(names, piezo_x, piezo_y, piezo_z, y_range):
            yield from bps.mv(piezo.x, x,
                              piezo.y, y,
                              piezo.z, z)

            for wa in waxs_arc:
                yield from bps.mv(waxs, wa)
                dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
                det_exposure_time(t, t)

                e = energy.position.energy / 1000  # energy keV
                sdd = pil1m_pos.z.position / 1000  # SAXS detector distance
                temp = str(np.round(float(temp_degC), 1)).zfill(5)
                wa = waxs.arc.position + 0.001
                wa = str(np.round(float(wa), 1)).zfill(4)
                #proposal_id("2022_2", "310149_Wilborn1/%s" % name)
                name_fmt = "{sample}_{temp}degC_{energy}keV_wa{wax}_sdd{sdd}m"
                sample_name = name_fmt.format(
                    sample=name,
                    temp=temp,
                    energy="%.2f" % e,
                    wax=wa,
                    sdd="%.1f" % sdd,   
                )
                sample_name = sample_name.translate(
                    {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =,"}
                )
                sample_id(user_name="MW", sample_name=sample_name)
                print(f"\n\n\n\t=== Sample: {sample_name} ===")

                yield from bp.rel_scan(dets, piezo.x, *scan_pts)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)
    # Turn off the heating and set temperature to 23 deg C
    t_kelvin = 23 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)
    yield from ls.output1.turn_off()


def milan_temp_2023_1(tim=1):
    """
    Temperature scan using Linkam thermal GI stage for transmission with the hexa tilt.
    RT, 100C, 150C, 4 points per sample. For hockey pucks.

    REMEMBER: add temperature to file name or retrive later with databroker...
    """

    names =   ['JMA08', 'JMB08','JMA02','JMA04','JMA06','JMA07','JMA09','JMB04','JMB06','JMA05','JMA03','JMA10','FTB64','FTA64','FTB53','FTA67','FTD54','FTA54','FTB54', 'FTB75']
    piezo_x = [  57900,    53100,  47300, 42500,     37500,   30500,     23500,     18300,    12900,   8100,      2900,     -2100,    -6900,   -11300,   -17300,   -22900,   -28100,   -34300,   -41500,   -47900]
    piezo_y = [    300,      300,    550,   600,        750,     750,      1000,     1000,     1000,     1350,        1350,      1350,     1850,   1950, 2150, 2400, 2400, 2250, 2800,2449]
    piezo_z = [       -3370,         -3370,        -3370,      -3370,            -3370,        -3370,         -3370,      -3370,     -3370,     -3370,        -3370,       -3370,      -3370,    -1470, -2470, -1220, -2270, -2970, -1870, -4620]
    #piezo_z = [8400 for n in names]


    assert len(names) == len(
        piezo_x), f"Number of X coordinates ({len(names)}) is different from number of samples ({len(piezo_x)})"
    assert len(piezo_y) == len(
        piezo_x), f"Number of Y coordinates ({len(piezo_y)}) is different from number of samples ({len(piezo_x)})"


    temperatures = [28, 55, 70, 100, 140]
    user_name = 'MW'

    x_offset = [0,  0, 200, 200,]
    y_offset = [0, 50,   0,  50,]
    waxs_arc = [0, 20]

    for i_t, t in enumerate(temperatures):
        print(f'Going to {t:.0f} deg C')
        t_kelvin = t + 273.15
        yield from ls.output1.mv_temp(t_kelvin)
        yield from bps.mv(ls.output1.status, 3)
        temp = ls.input_A.get()

        while abs(temp - t_kelvin) > 3:
            print(f'Current temp: {temp - 273.15:.1f} degC,\t difference: {(temp - t_kelvin):.1f} deg C')
            yield from bps.sleep(10)
            temp = ls.input_A.get()

        if i_t != 0:
            yield from bps.sleep(450)

        temp = ls.input_A.get()
        t_celsius = temp - 273.15

        for wa in waxs_arc:

            yield from bps.mv(waxs, wa)
            
            dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
            det_exposure_time(tim, tim)

            for name, x, y, z in zip(names, piezo_x, piezo_y, piezo_z):
                yield from bps.mv(piezo.x, x,
                                  piezo.y, y,
                                  piezo.z, z)

                for i, (x_off, y_off) in enumerate(zip(x_offset, y_offset)):
                    
                    yield from bps.mv(piezo.x, x + x_off,
                                      piezo.y, y + y_off)

                    # Metadata
                    e = energy.position.energy / 1000
                    wa = waxs.arc.position + 0.001
                    wa = str(np.round(float(wa), 1)).zfill(4)
                    sdd = pil1m_pos.z.position / 1000
                    t_celsius = str(np.round(float(t_celsius), 1)).zfill(5)


                    # Sample name
                    name_fmt = '{sample}_{t_c}degC_{energy}keV_wa{wax}_sdd{sdd}m_pos{pos}'
                    sample_name = name_fmt.format(
                        sample=name,
                        t_c = t_celsius,
                        energy="%.2f" % e,
                        wax=wa,
                        sdd="%.1f" % sdd,
                        pos=i,
                    )
                    
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    sample_id(user_name=user_name, sample_name=sample_name)
                    yield from bp.count(dets)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.2, 0.2)

    t_kelvin = 25 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)
    yield from ls.output1.turn_off()


def grid_milan_temp_2023_1(t=1):
    """
    Fine grid scan on Linkam GI thermal stage
    """
    names =   [ 'JMB9','JMC8','JMD8','FTB47','FTB49','FTD67','FTA75','FTA70','FTA68', 'FT',  'KLA12',      'KLA11',        'KLA10',      'KLA09',        'KLA08',   'KLA07',      'KLA06',     'KLA05',    'KLA04',    'KLA03',    'KLA02',    'KLA01']

    piezo_x = [-46900, -39300, -35200, -23800, -13600, -9200, -1600, 2000, 6000, 12800, 20600, 24600, 28600,30600,35100, 36600,40600,43600, 44600, 46600,50600, 56600]
    piezo_y = [ 3000, 3149, 2949, 2099, 2049, 1899, 1749, 1749, 1649, 1449, 1250, 1150,  1050,1050,950, 950,550, 950,450,450,650, 650]
    piezo_z = [-1570, 180, 180, 630, -2020, -1970,-1970,-1970,-1970,-1970, -3670,-3670,-3670,-3670,-3670,-3670,-3670,-3670,-3670,-3670,-3670, -3670]
    #piezo_z = [8400 for n in names]
    y_range = [[0, 100, 2],[0, 100, 2],[0, 100, 2],[0, 100, 2],[0, 100, 2],[0, 100, 2],[0, 100, 2],[0, 100, 2],[0, 100, 2],[0, 100, 2],[0, 100, 11],[0, 100, 11],[0, 100, 11],[0, 100, 11],[0, 100, 11],[0, 100, 11],[0, 200, 21],[0, 200, 21],[0, 400, 41],[0, 200, 21],[0, 200, 21],[0, 200, 21]]
    x_range = [[0, 300, 2], [0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2],[0, 300, 2]]


    assert len(names) == len(piezo_x),   f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_z), f"Wrong list lenghts"
    assert len(piezo_z) == len(y_range), f"Wrong list lenghts"
    assert len(y_range) == len(x_range), f"Wrong list lenghts"

    waxs_arc = [0, 20]
    temperatures = [28] 

    for temperature in temperatures:
        t_kelvin = temperature + 273.15
        yield from ls.output1.mv_temp(t_kelvin)
        yield from bps.mv(ls.output1.status, 3)

        # Equalise temperature
        print(f"Equalising temperature to {temperature} deg C")
        start = time.time()
        temp = ls.input_A.get()
        while abs(temp - t_kelvin) > 5:
            print("Difference: {:.1f} K".format(abs(temp - t_kelvin)))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

            # Escape the loop if too much time passes
            if time.time() - start > 1800:
                temp = t_kelvin
        print(
            "Time needed to equilibrate: {:.1f} min".format((time.time() - start) / 60)
        )
        # Wait extra time depending on temperature
        if (40 < temperature) and (temperature < 181):
            yield from bps.sleep(300)

        # Read T and convert to deg C
        temp_degC = ls.input_A.get() - 273.15

        for name, x, y, z, scan_pts_y, scan_pts_x in zip(names, piezo_x, piezo_y, piezo_z, y_range, x_range):
            yield from bps.mv(piezo.x, x,
                              piezo.y, y,
                              piezo.z, z)

            for wa in waxs_arc:
                yield from bps.mv(waxs, wa)
                dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
                det_exposure_time(t, t)

                e = energy.position.energy / 1000
                sdd = pil1m_pos.z.position / 1000
                temp = str(np.round(float(temp_degC), 1)).zfill(5)
                wa = waxs.arc.position + 0.001
                wa = str(np.round(float(wa), 1)).zfill(4)
                #proposal_id("2022_2", "310149_Wilborn1/%s" % name)
                name_fmt = "{sample}_{temp}degC_{energy}keV_wa{wax}_sdd{sdd}m"
                sample_name = name_fmt.format(
                    sample=name,
                    temp=temp,
                    energy="%.2f" % e,
                    wax=wa,
                    sdd="%.1f" % sdd,   
                )
                sample_name = sample_name.translate(
                    {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =,"}
                )
                sample_id(user_name="MW", sample_name=sample_name)
                print(f"\n\n\n\t=== Sample: {sample_name} ===")

                yield from bp.rel_grid_scan(dets, piezo.x, *scan_pts_x, piezo.y, *scan_pts_y)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)
    # Turn off the heating and set temperature to 23 deg C
    t_kelvin = 23 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)
    yield from ls.output1.turn_off()


