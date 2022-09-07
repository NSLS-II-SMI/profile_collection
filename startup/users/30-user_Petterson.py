####line scab


def run_gi_sweden_SAXS(tim=0.5, sample="Test", ti_sl=60):
    # Slowest cycle:
    name = "TP"
    num = 2
    x_interface = [piezo.x.position]

    x_surface = x_interface[0] - 1500
    piezo_y_range = [-20, 20, 41]
    samples = [sample + "_interface"]

    surface_sample = sample + "_surface"
    angle = 0.1

    # Detectors, motors:
    dets = [pil1M, pil1mroi2]  # WAXS detector ALONE
    x_offset = 10
    t0 = time.time()

    yield from bps.mv(piezo.x, x_surface)
    yield from alignement_gisaxs(angle)
    yield from bps.mvr(piezo.th, angle)

    det_exposure_time(tim, tim)
    sample_id(user_name=name, sample_name=surface_sample)
    yield from bp.rel_scan(dets, piezo.y, *piezo_y_range)

    name_fmt = "{sample}_{angle}deg_{ti}sec"
    #    param   = '16.1keV'
    assert len(x_interface) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    for x, s in zip(x_interface, samples):
        yield from bps.mv(piezo.x, x)
        # yield from alignement_gisaxs_shorter(angle)
        # yield from bps.mvr(piezo.th, angle)
        for i in range(num):
            yield from bps.mv(piezo.x, x + x_offset * i)
            t1 = time.time()
            t_min = np.round((t1 - t0))
            sample_name = name_fmt.format(sample=s, angle=angle, ti="%5.5d" % t_min)
            sample_id(user_name=name, sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.rel_scan(dets, piezo.y, *piezo_y_range)

            yield from bps.sleep(ti_sl)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(1, 1)


def gisaxs_KTH_2021_1(t=1):

    global names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, xs_hexa

    # names = ['1BL_DI', '3BL_DI', '5BL_DI', '1BL_NaCl', '3BL_NaCl', '5BL_NaCl', 'Si_wafer', 'PVAm', 'PVAm_CNF', 'PVAm_CNF_PAH', 'PEI']

    # x_piezo = [59000, 55000, 43000, 30000, 17000, 4000, -9000, -22000, -33000, -45000, -50000]
    # y_piezo = [ 7400,  7400,  7400,  7400,  7400, 7400,  7400,   7400,   7400,   7400,   7400]
    # z_piezo = [    0,     0,     0,     0,     0,    0,     0,      0,      0,      0,      0]
    # x_hexa =  [    8,     0,     0,     0,     0,    0,     0,      0,      0,      0,     -6]
    # incident_angles = [0.079829, 0.113749, 0.022469, 0.002876, 0.156458, 0.017894, 0.472448, -0.001836, 0.03759, -0.062716, 0.033808]
    # y_piezo_aligned = [7598.066, 7613.373, 7603.519, 7569.923, 7566.072, 7542.689, 7521.385, 7491.759, 7484.312, 7445.632, 7480.081]

    names = ["PEI_CNF", "PEI_CNF_PAH"]

    x_piezo = [18000, 1000]
    y_piezo = [7400, 7400]
    z_piezo = [0, 0]
    x_hexa = [0, 0]
    incident_angles = []
    y_piezo_aligned = []

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

    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique="gisaxs")

    for name, xs_piezo, zs_piezo, ys_piezo, xs_hexa in zip(
        names, x_piezo, z_piezo, y_piezo, x_hexa
    ):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)
        yield from bps.mv(piezo.z, zs_piezo)
        yield from bps.mv(piezo.th, 0)

        # if ys_piezo>0:
        yield from alignement_gisaxs_multisample(angle=0.08)
        # else:
        #     yield from bps.mv(piezo.th, -1)
        #     yield from alignement_gisaxs_multisample_special(angle = 0.08)

        incident_angles = incident_angles + [piezo.th.position]
        y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    yield from smi.modeMeasurement()
    print(incident_angles)
    print(y_piezo_aligned)

    angle = [0.1]
    dets = [pil1M]
    det_exposure_time(t, t)

    for name, xs, zs, aiss, ys, xs_hexa in zip(
        names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, x_hexa
    ):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, aiss)

        for an in angle:
            for i in range(1, 11, 1):
                yield from bps.mv(piezo.x, xs - i * 200)
                yield from bps.mv(piezo.th, aiss + an)
                name_fmt = "{sample}_sdd6.2m_16.1keV_ai{angl}deg_pos{pos}"
                sample_name = name_fmt.format(
                    sample=name, angl="%3.2f" % an, pos="%2.2d" % i
                )
                sample_id(user_name="PT", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

    angle = np.linspace(0.08, 0.4, 17)
    dets = [pil1M]
    det_exposure_time(t, t)

    for name, xs, zs, aiss, ys, xs_hexa in zip(
        names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, x_hexa
    ):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, aiss)

        for j, an in enumerate(angle):
            yield from bps.mv(piezo.x, xs - 2500 - j * 50)
            yield from bps.mv(piezo.th, aiss + an)
            name_fmt = "{sample}_sdd6.2m_16.1keV_ai{angl}deg"
            sample_name = name_fmt.format(sample=name, angl="%3.2f" % an)
            sample_id(user_name="PT", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count(dets, num=1)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.1, 0.1)


def run_gi_sweden_GISAXS(tim=0.5, sample="Test", ti_sl=77):
    # Slowest cycle:
    name = "TP"
    num = 1
    x_interface = [piezo.x.position]

    x_surface = x_interface[0] - 500

    piezo_y_range = [-20, 20, 41]
    samples = [sample + "_interface"]

    surface_sample = sample + "_surface"
    angle = 0.1

    # Detectors, motors:
    dets = [pil1M, pil1mroi2]  # WAXS detector ALONE
    x_offset = 10
    t0 = time.time()

    # yield from bps.mv(piezo.x, x_surface)
    # yield from alignement_gisaxs(angle)
    # yield from bps.mvr(piezo.th, angle)

    det_exposure_time(tim, tim)
    sample_id(user_name=name, sample_name=surface_sample)
    # yield from bp.rel_scan(dets, piezo.y, *piezo_y_range)

    # yield from bps.mv(piezo.x, x_interface)

    name_fmt = "{sample}_{angle}deg_{ti}sec"
    #    param   = '16.1keV'
    assert len(x_interface) == len(
        samples
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    for x, s in zip(x_interface, samples):
        yield from bps.mv(piezo.x, x)
        # yield from alignement_gisaxs_shorter(angle)
        # yield from bps.mvr(piezo.th, angle)
        for i in range(num):
            # x_pos = [piezo.x.position]
            # yield from bps.mv(piezo.x, x_pos+x_offset)
            yield from bps.mv(piezo.x, x + x_offset * i)
            t1 = time.time()
            t_min = np.round((t1 - t0))
            sample_name = name_fmt.format(sample=s, angle=angle, ti="%5.5d" % t_min)
            sample_id(user_name=name, sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.rel_scan(dets, piezo.y, *piezo_y_range)

            yield from bps.sleep(ti_sl)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(1, 1)
