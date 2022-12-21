def saxs_gu_2022_1(t=1):

    xlocs = [
        33000,
        24000,
        15000,
        6000,
        -3000,
        -12000,
        -21000,
        -30000,
        33000,
        24000,
        15000,
        6000,
        -3000,
        -12000,
        -21000,
        -30000,
    ]
    ylocs = [
        5200,
        6000,
        5500,
        6100,
        5600,
        5600,
        5600,
        4700,
        300,
        300,
        600,
        300,
        100,
        100,
        -200,
        -500,
    ]
    zlocs = [
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
    ystage = [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
    ]
    names = [
        "samA1",
        "samA2",
        "samA3",
        "samA4",
        "samA5",
        "samA6",
        "samA7",
        "samA8",
        "samB1",
        "samB2",
        "samB3",
        "samB4",
        "samB5",
        "samB6",
        "samB7",
        "samB8",
    ]

    user = "YW"
    det_exposure_time(t, t)

    assert len(xlocs) == len(
        names
    ), f"Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})"
    assert len(xlocs) == len(
        ylocs
    ), f"Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(ylocs)})"
    assert len(xlocs) == len(
        zlocs
    ), f"Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(zlocs)})"
    assert len(xlocs) == len(
        ystage
    ), f"Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(ystage)})"
    assert len(xlocs) == len(
        names
    ), f"Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})"

    # Detectors, motors:
    dets = [pil1M]
    waxs_range = [20]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z, y_sta in zip(names, xlocs, ylocs, zlocs, ystage):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)
            yield from bps.mv(stage.y, y_sta)

            name_fmt = "{sam}_16.1keV_sdd7.0m_wa{waxs}"
            sample_name = name_fmt.format(sam=sam, waxs="%2.1f" % wa)
            sample_id(user_name=user, sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.count(dets, num=10)
            yield from bps.sleep(2)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)


def temp_2021_3(tim=0.5):
    # Slowest cycle:
    temperatures = [115]

    name = "YW"

    samples = ["Trimethyl_benzene", "Pff4TBT", "Toluene", "PS", "P3DT"]
    x_list = [32200, 22500, 13200, 4200, -9800]
    y_list = [-2900, -3700, -3500, -3700, -3700]

    assert len(x_list) == len(
        y_list
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_list) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    # Detectors, motors:
    dets = [pil1M]  # ALL detectors

    waxs_arc = [20]
    name_fmt = "{sample}_16.1keV_4.0m_{temperature}C_wa{waxs}"

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        t_kelvin = t + 273.15
        yield from ls.output1.mv_temp(t_kelvin)
        temp = ls.input_A.get()

        while abs(temp - t_kelvin) > 2.5:
            print(abs(temp - t_kelvin))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

        if i_t != 0:
            yield from bps.sleep(300)

        # temp = ls.input_A.get()
        t_celsius = temp - 273.15

        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            for x, y, s in zip(x_list, y_list, samples):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)

                sample_name = name_fmt.format(
                    sample=s, temperature="%3.1f" % t_celsius, waxs="%2.1f" % wa
                )
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                sample_id(user_name=name, sample_name=sample_name)
                yield from bp.count(dets, num=1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    t_kelvin = 25 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)


def gu_nexafs_S_2021_3(t=1):
    dets = [pil900KW]

    # energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    energies = 2 + np.asarray(
        np.arange(2445, 2470, 5).tolist()
        + np.arange(2470, 2480, 0.25).tolist()
        + np.arange(2480, 2490, 1).tolist()
        + np.arange(2490, 2501, 5).tolist()
    )

    waxs_arc = np.linspace(40, 40, 1)

    # names=['Trimethyl_benzene_redo', 'Pff4TBT_redo_180C']
    # x = [31600, 4400]
    # y = [-3600, -4300]

    # names=['PTB7', 'PCE10', 'Pff4TBT_2ndrun', 'P3DT']
    # x = [ 13600, 19200, 4400, -27000]
    # y = [-4200, -4200, -4700, -4800]

    names = ["Trimethyl_benzene_2ndrun"]
    x = [31600]
    y = [-3400]

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


def gu_saxs_S_2022_1(t=1):
    dets = [pil1M]

    energies = [2450, 2460, 2470, 2475, 2476, 2477, 2478, 2480, 2500]
    waxs_arc = [20]

    names = ["Trimethyl_benzene_2ndrun"]
    x = [31600]
    y = [-3300]
    # names=['PTB7', 'PCE10', 'Pff4TBT_2ndrun', 'P3DT']
    # x = [ 13600, 19200, 4400, -27000]
    # y = [-4200, -4200, -4700, -4800]
    # names=['Trimethyl_benzene', 'Pff4TBT']
    # x = [31600, 4600]
    # y = [-3600, -4300]

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
            name_fmt = "{sample}_1.6m_{energy}eV_wa{wax}_bpm{xbpm}"
            for i, e in enumerate(energies):
                yield from bps.mv(energy, e)
                yield from bps.sleep(5)
                # yield from bps.mv(piezo.y, ys + i * 50)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(
                    sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm
                )
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def gu_saxs_hardxray_2022_1(t=1):
    dets = [pil1M]

    energies = [16100]
    waxs_arc = [20]

    names = ["Trimethyl_benzene", "PCE10", "PTB7", "Pff4TBT", "P3DT"]
    x = [31800, 19200, 14100, 5100, -27000]
    y = [-3300, -3800, -3900, -4000, -4200]

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
            name_fmt = "{sample}_4.0m_{energy}eV_wa{wax}_exp5s"
            for i, e in enumerate(energies):
                yield from bps.mv(energy, e)
                yield from bps.sleep(5)
                # yield from bps.mv(piezo.y, ys + i * 50)

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa)
                sample_id(user_name="GF", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")
                yield from bp.count(dets, num=1)


def wang_temperature_hard_2022_2(t=1):
    """
    WAXS and SAXS using heating stage controlled by Lakeshore

    For reference: 16.1 keV, low divergence, in vacuum, SAXS sdd 8.3 m
    """

    # solid sample position
    samples = [
        "PffBT4T_1",
        "PffBT4T_2",
        "P3OT_1",
        "P3OT_2",
        "P3DT_1",
        "P3DT_2",
        "P3DDT_1",
        "P3DDT_2",
        "PIB_A_DPP_A",
        "PIB_Br_DPP_A",
        "PIB_A_DPP_Br",
        "PIB_Br_DPP_Br",
        "5%P3HT",
        "5%DPP",
    ]
    x_piezo = [
        41600,
        42200,
        34200,
        35400,
        27600,
        27600,
        20800,
        22000,
        12600,
        2600,
        -6400,
        -16400,
        -25500,
        -36500,
    ]
    y_piezo = [
        -3200,
        -3700,
        -4300,
        -4300,
        -4100,
        -3200,
        -3300,
        -3300,
        -3300,
        -4300,
        -4300,
        -4000,
        -3700,
        -4100,
    ]

    # Move all samples
    y_piezo = np.asarray(y_piezo) - 50

    # solution sample position
    # samples = ['blank_SiNx', 'TMB1_1', 'TMB1_2', 'TMB2_1', 'TMB2_2', 'PS_TMB_1', 'PS_TMB_2', 'PffBT4T1_TMB_1', 'PffBT4T1_TMB_2', 'PffBT4T2_TMB_1', 'PffBT4T2_TMB_2', 'P3OT1_TMB_1', 'P3OT1_TMB_2', 'P3DT_TMB_1', 'P3DT_TMB_2', 'P3DDT_TMB_1', 'P3DDT_TMB_2']
    # x_piezo = [       45000,    38900,    37700,    31700,    31700,     25300,      26100,             20600,            21200,            14300,            15100,          8500,          8400,       -1800,         -3100,         -7300,         -8500]
    # y_piezo = [       -3200,    -3000,    -3000,    -3000,    -3500,     -3900,      -2500,             -3700,            -3700,            -3500,            -2700,         -2500,         -3900,       -4100,         -4100,         -4300,         -3050]

    # Correct sample names just in case
    samples = [
        s.translate({ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =,"}) for s in samples
    ]
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})"
    assert len(x_piezo) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"

    user_name = "YW"
    temperatures = [30]
    waxs_arc = [0, 20]
    name_fmt = "{sample}_{energy}keV_temp{temp}degC_wa{wax}_sdd{sdd}m_id{scan_id}"

    for temperature in temperatures:
        t_kelvin = temperature + 273.15
        yield from ls.output1.mv_temp(t_kelvin)

        # Activate heating range in Lakeshore
        if temperature < 50:
            yield from bps.mv(ls.output1.status, 1)
        else:
            yield from bps.mv(ls.output1.status, 3)

        # Equalise temperature
        print("Equalising temperature")
        start = time.time()
        temp = ls.input_A.get()
        while abs(temp - t_kelvin) > 5:
            print("Difference: {:.1f} K".format(abs(temp - t_kelvin)))
            yield from bps.sleep(10)
            temp = ls.input_A.get()
            # Escape the loop if too much time passes
            if time.time() - start > 3600:
                temp = t_kelvin
        print(
            "Time needed to equilibrate: {:.1f} min".format((time.time() - start) / 60)
        )

        # Wait extra time depending on temperature
        if (56 < temperature) and (temperature < 160):
            yield from bps.sleep(300)
        elif 160 <= temperature:
            yield from bps.sleep(600)

        # Read T and convert to deg C
        temp_degC = ls.input_A.get() - 273.15

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
            det_exposure_time(t, t)

            for x, y, name in zip(x_piezo, y_piezo, samples):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y + i * 50)

                # Metadata
                e = energy.position.energy / 1000
                temp = str(np.round(float(temp_degC), 1)).zfill(5)
                wa = str(np.round(float(wa), 1)).zfill(4)
                sdd = pil1m_pos.z.position / 1000
                scan_id = db[-1].start["scan_id"] + 1

                sample_name = name_fmt.format(
                    sample=name,
                    energy="%.1f" % e,
                    temp=temp,
                    wax=wa,
                    sdd="%.1f" % sdd,
                    scan_id=scan_id,
                )

                print(f"\n\t=== Sample: {sample_name} ===\n")
                sample_id(user_name=user_name, sample_name=sample_name)
                yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    # Turn off the heating and set temperature to 23 deg C
    t_kelvin = 23 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)
    yield from ls.output1.turn_off()


def wang_temperature_tender_2022_2(t=1):
    """
    REMEMBER TO TURN ON HEATING FOR LIQUID RUN

    WAXS and SAXS using heating stage controlled by Lakeshore

    For reference: 2.470 keV, low divergence, in vacuum, SAXS sdd 8.3 m
    for fun

    YWang: I restart it 1:15am 07/21/22. Changed code to skip NEXAFS and 25C. Details can be found in following comments.
    """
    print("REMEMBER TO TURN ON HEATING FOR LIQUID RUN")

    # solution sample position
    samples = [
        "blank_SiNx",
        "TMB1_1",
        "TMB1_2",
        "TMB2_1",
        "TMB2_2",
        "PS_TMB_1",
        "PS_TMB_2",
        "PffBT4T1_TMB_1",
        "PffBT4T1_TMB_2",
        "PffBT4T2_TMB_1",
        "PffBT4T2_TMB_2",
        "P3OT1_TMB_1",
        "P3OT1_TMB_2",
        "P3DT_TMB_1",
        "P3DT_TMB_2",
        "P3DDT_TMB_1",
        "P3DDT_TMB_2",
    ]
    x_piezo = [
        45000,
        39100,
        38200,
        32000,
        32900,
        26800,
        25900,
        20800,
        21400,
        15400,
        14800,
        9000,
        9900,
        -2750,
        -1300,
        -7700,
        -6900,
    ]
    y_piezo = [
        -2500,
        -1900,
        -2000,
        -2000,
        -1700,
        -1700,
        -1700,
        -1700,
        -1800,
        -1800,
        -1800,
        -1300,
        -1200,
        -1200,
        -1200,
        -1400,
        -1400,
    ]

    # Correct sample names just in case
    samples = [
        s.translate({ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =,"}) for s in samples
    ]
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of Y coordinates ({len(y_piezo)})"
    assert len(x_piezo) == len(
        samples
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(samples)})"

    energies_coarse = [2460, 2470, 2472, 2474, 2475, 2476, 2477, 2478, 2480]

    energies_nexafs = np.concatenate(
        (
            np.arange(2445, 2470, 5),
            np.arange(2470, 2480, 0.25),
            np.arange(2480, 2490, 1),
            np.arange(2490, 2501, 5),
        )
    )

    user_name = "YW"
    temperatures = [
        50,
        100,
        150,
        170,
        180,
        190,
        200,
        210,
        220,
        230,
        240,
        250,
    ]  # YWang: I delete 25 here to skip 25C because I have had the SAXS data and most WAXS DATA  1:16 am 07/21/22
    waxs_arc = [0, 20, 40]
    name_fmt = "{sample}_{energy}eV_temp{temp}degC_wa{wax}_sdd{sdd}m_id{scan_id}"

    for temperature in temperatures:
        t_kelvin = temperature + 273.15
        yield from ls.output1.mv_temp(t_kelvin)

        # Activate heating range in Lakeshore
        if temperature < 50:
            yield from bps.mv(ls.output1.status, 1)
        else:
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
        if (35 < temperature) and (temperature < 160):
            yield from bps.sleep(300)
        elif 160 <= temperature:
            yield from bps.sleep(600)

        # Read T and convert to deg C
        temp_degC = ls.input_A.get() - 273.15

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            # YWang: I changed < 25 to <45 to skip NEXAFS  1:16 am 07/21/22
            energies = energies_coarse if waxs.arc.position < 45 else energies_nexafs
            dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
            det_exposure_time(t, t)

            for j, (x, y, name) in enumerate(zip(x_piezo, y_piezo, samples)):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)

                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                    # Metadata
                    # e = energy.position.energy / 1000
                    temp = str(np.round(float(temp_degC), 1)).zfill(5)
                    wa = str(np.round(float(wa), 1)).zfill(4)
                    sdd = pil1m_pos.z.position / 1000
                    scan_id = db[-1].start["scan_id"] + 1

                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%.2f" % e,
                        temp=temp,
                        wax=wa,
                        sdd="%.1f" % sdd,
                        scan_id=scan_id,
                    )

                    print(f"\n\t=== Sample {j + 1}/{len(samples)}: {sample_name} ===\n")
                    sample_id(user_name=user_name, sample_name=sample_name)
                    yield from bp.count(dets)

                yield from bps.mv(energy, 2475)
                yield from bps.mv(energy, 2460)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    # Turn off the heating and set temperature to 23 deg C
    t_kelvin = 23 + 273.15
    yield from ls.output1.mv_temp(t_kelvin)
    yield from ls.output1.turn_off()


def wang_temperature_hard_2022_3(t=1):
    """
    WAXS and SAXS using heating stage controlled by Lakeshore

    For reference: 16.1 keV, low divergence, in vacuum, SAXS sdd 8.3 m
    """

    ######### Yunfei solid sample position
    names =   ['SiNx-a', 'SiNx-b', 'SiNx-c', 'Pff1', 'Pff2', 'P3OT1-1', 'P3OT1-2', 'P3DT1-1', 'P3DT1-2', 'TMB4-1', 'TMB4-2',  'SiNx2-1', 'Pff3-1', 'Pff3-2', 'Pff5-1', 'Pff5-2', 'Pff5-3', 'empty-space']
    piezo_x = [   43000,    43600,    43600,  26100,  19500,     14300,     13250,      7200,      6000,   -20000,      -18800,       -25400,   -31400,   -31100,   -38500,   -38100,   -38000,     -41450]   
    piezo_y = [   -5000,    -5000,    -4400,  -4400,  -3800,     -3750,     -5000,     -3650,     -3650,    -2850,      -2900,         -2900,   -2900,     -2900,    -2900,    -2650,    -3450 ,     -3500]
    piezo_z = [4200 for n in names]
    # piezo_z = [4200, 4100, ]

    ######### Guorong solid sample position
    #names =   ['TAMU1', 'TAMU2', 'TAMU3', 'TAMU4', 'TAMU5', 'TAMU6', 'TAMU7', 'TAMU8','TAMU9', 'GM19', 'GER1', 'GER2', 'empty-space']
    #piezo_x = [   47000,  40700,   34300,   27700,   21300,   15200,    9000,    2500,  -3900, -10400, -16600, -23000,   -29300   ]   
    #piezo_y = [  -5250,   -5250,   -5250,   -5250,   -5250,   -5250,   -5250,   -4850,  -4850,  -4850,  -4850,  -4850,     -4850     ]
    #piezo_z = [4200 for n in names]
    # piezo_z = [4200, 4100, ]


    assert len(names) == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_x), f"Wrong list lenghts"

    user_name = "YW"
    temperatures = [180] #[25, 180]
    waxs_arc = [0, 20]

    for temperature in temperatures:
        t_kelvin = temperature + 273.15
        yield from ls.output1.mv_temp(t_kelvin)

        # Activate heating range in Lakeshore
        if temperature < 50:
            yield from bps.mv(ls.output1.status, 1)
        else:
            yield from bps.mv(ls.output1.status, 3)

        # Equalise temperature
        print(f"Equalising temperature to {temperature:.0f} deg C")
        start = time.time()
        temp = ls.input_A.get()
        while abs(temp - t_kelvin) > 5:
            print("Difference: {:.1f} K".format(abs(temp - t_kelvin)))
            yield from bps.sleep(10)
            temp = ls.input_A.get()
            
            # Escape the loop if too much time passes
            if time.time() - start > 15 * 60:
                temp = t_kelvin
        print(
            "Time needed to equilibrate: {:.1f} min".format((time.time() - start) / 60)
        )

        # Wait extra time depending on temperature
        ######## Yunfei changed both to 1 second. Previous is 300 , 600
        if (56 < temperature) and (temperature < 160):
            yield from bps.sleep(1)
        elif 160 <= temperature:
            yield from bps.sleep(1)

        # Read T and convert to deg C
        temp_degC = ls.input_A.get() - 273.15

        rod_pos = pil1m_bs_rod.x.position

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
            
            if not ((0 < rod_pos) and (rod_pos < 3)):
                dets.append(pdcurrent)
                dets.append(pdcurrent1)
                dets.append(pdcurrent2)

            det_exposure_time(t, t)

            for name, x, y in zip(names, piezo_x, piezo_y):
                yield from bps.mv(piezo.x, x,
                                  piezo.y, y + i * 0)

                # Metadata
                e = energy.position.energy / 1000
                temp = str(np.round(float(temp_degC), 1)).zfill(5)
                wa = waxs.arc.position + 0.001
                wa = str(np.round(float(wa), 1)).zfill(4)
                sdd = pil1m_pos.z.position / 1000

                if not ((0 < rod_pos) and (rod_pos < 3)):
                    if waxs.arc.position > 15:
                        fs.open()
                        yield from bps.sleep(0.3)
                        curr = pdcurrent2.get()
                        fs.close()
                    else:
                        curr = 0
                    curr = str(np.round(float(curr), 0))
                else:
                    curr = '_rod_'

                
                
                name_fmt = "{sample}_{temp}degC_{energy}keV_wa{wax}_sdd{sdd}m_pd{curr}"
                sample_name = name_fmt.format(
                    sample=name,
                    energy="%.2f" % e,
                    temp=temp,
                    wax=wa,
                    sdd="%.1f" % sdd,
                    #curr='%.0f' % curr,
                    curr = curr,
                )
                sample_name = sample_name.translate(
                    {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =, "}
                )
                print(f"\n\n\n\t=== Sample: {sample_name} ===")
                sample_id(user_name=user_name, sample_name=sample_name)
                yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    # Turn off the heating and set temperature to 23 deg C
    #t_kelvin = 23 + 273.15
    #yield from ls.output1.mv_temp(t_kelvin)
    #yield from ls.output1.turn_off()


def read_pd_current():
    """
    Read pin diode current with attenuated beam
    """
    #yield from bps.mv(att1_6.open_cmd, 1)
    #yield from bps.mv(att1_7.open_cmd, 1)
    #yield from bps.sleep(2)

    fs.open()
    yield from bps.sleep(0.3)
    pd_curr = pdcurrent2.get()
    fs.close()

    #yield from bps.mv(att1_6.close_cmd, 1)
    #yield from bps.mv(att1_7.close_cmd, 1)

    #yield from bps.sleep(2)

    return(pd_curr)

def turn_off_heating(temp=23):
    """
    Turn off the heating and set temperature to 23 deg C for Lakeshore
    """
    print(f'Setting temp to {temp} deg C and turning off the heater')
    t_kelvin = temp + 273.15
    yield from ls.output1.mv_temp(t_kelvin)
    yield from ls.output1.turn_off()


def wang_temperature_tender_2022_3(t=2.5):
    """
    Tender X-ray WAXS and SAXS Lakeshore heating stage, coarse energies

    For reference: 2470 eV, low divergence, in vacuum, SAXS sdd 1.6 m
    """

    names =   ['SiNx-a', 'SiNx-b',  'P3OT1-1', 'P3OT1-2', 'P3DT1-1', 'P3DT1-2', 'TMB4-1',          'TMB4-2',  'SiNx2-1',  'Pff5-1', 'Pff5-2', 'Pff5-3', 'empty-space']
    piezo_x = [   43500,    44000,      14700,     13650,      7600,      6400,   -19650,      -18450,       -25400,     -37900,   -37900,   -37700,     -34300]   
    piezo_y = [   -5000,    -5000,      -3800,     -5150,     -5200,     -3800,    -3050,      -3100,         -3100,       -2900,    -3300,    -3500 ,     -3500]
    piezo_z = [5600 for n in names]
    # piezo_z = [4200, 4100, ]

    assert len(names)   == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x) == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_z), f"Wrong list lenghts"

    user_name = "YW"
    temperatures = [25, 200] #[25, 180]
    waxs_arc = [0, 20]
    energies = [2460, 2470, 2472, 2474, 2475, 2476, 2477, 2478, 2480]
    rod_pos = pil1m_bs_rod.x.position

    pin_diode_in_rod_out = not ((0 < rod_pos) and (rod_pos < 3))

    # Add beamstop to sample name
    if pin_diode_in_rod_out:
        names = [n + '-pd' for n in names]
    else:
        names = [n + '-rod' for n in names]

    for temperature in temperatures:
        t_kelvin = temperature + 273.15
        yield from ls.output1.mv_temp(t_kelvin)

        # Activate heating range in Lakeshore
        if temperature < 50:
            yield from bps.mv(ls.output1.status, 1)
        else:
            yield from bps.mv(ls.output1.status, 3)

        # Equalise temperature
        print(f"Equalising temperature to {temperature:.0f} deg C")
        start = time.time()
        temp = ls.input_A.get()
        while abs(temp - t_kelvin) > 5:
            print("Difference: {:.1f} K".format(abs(temp - t_kelvin)))
            yield from bps.sleep(10)
            temp = ls.input_A.get()
            
            # Escape the loop if too much time passes
            if time.time() - start > 15 * 60:
                temp = t_kelvin
        print(
            "Time needed to equilibrate: {:.1f} min".format((time.time() - start) / 60)
        )

        # Wait extra time depending on temperature
        if (56 < temperature) and (temperature < 160):
            yield from bps.sleep(300)
        elif 160 <= temperature:
            yield from bps.sleep(600)

        # Read T and convert to deg C
        temp_degC = ls.input_A.get() - 273.15

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)

            dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
            det_exposure_time(t, t)

            if pin_diode_in_rod_out:
                dets.append(pdcurrent)
                dets.append(pdcurrent1)
                dets.append(pdcurrent2)

            for name, x, y in zip(names, piezo_x, piezo_y):
                yield from bps.mv(piezo.x, x,
                                  piezo.y, y + i * 0)

                for e in energies:
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)
                
                
                    # Metadata
                    #e = energy.position.energy / 1000
                    temp = str(np.round(float(temp_degC), 1)).zfill(5)
                    wa = waxs.arc.position + 0.001
                    wa = str(np.round(float(wa), 1)).zfill(4)
                    sdd = pil1m_pos.z.position / 1000

                    if pin_diode_in_rod_out:
                        if waxs.arc.position > 15:
                            fs.open()
                            yield from bps.sleep(0.3)
                            curr = pdcurrent2.get()
                            fs.close()
                        else:
                            curr = 0
                        curr = str(np.round(float(curr), 0))
                    else:
                        curr = '_rod_'

                    name_fmt = "{sample}_{temp}degC_{energy}eV_wa{wax}_sdd{sdd}m_pd{curr}"
                    sample_name = name_fmt.format(
                        sample=name,
                        energy="%.2f" % e,
                        temp=temp,
                        wax=wa,
                        sdd="%.1f" % sdd,
                        #curr='%.0f' % curr,
                        curr = curr,
                    )
                    sample_name = sample_name.translate(
                        {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =, "}
                    )
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    sample_id(user_name=user_name, sample_name=sample_name)
                    
                    yield from bp.count(dets)
                yield from bps.mv(energy, 2475)
                yield from bps.mv(energy, 2460)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    # Turn off the heating and set temperature to 23 deg C
    yield from turn_off_heating()
