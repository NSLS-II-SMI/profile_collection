# pil300KW for waxs, pil1M for saxs


def cd_saxs(th_ini, th_fin, th_st, exp_t=1):
    sample = ["cdsaxs_ech03_defectivity_pitch128","cdsaxs_ech03_defectivity_pitch127","cdsaxs_ech03_defectivity_pitch124",
              "cdsaxs_ech03_defectivity_pitch121","cdsaxs_ech03_defectivity_pitch118","cdsaxs_ech03_defectivity_pitch115",
              "cdsaxs_ech03_defectivity_pitch112","cdsaxs_ech04_defectivity_pitch128","cdsaxs_ech04_defectivity_pitch127",
              "cdsaxs_ech04_defectivity_pitch124","cdsaxs_ech04_defectivity_pitch121","cdsaxs_ech04_defectivity_pitch118",
              "cdsaxs_ech04_defectivity_pitch115","cdsaxs_ech04_defectivity_pitch112","cdsaxs_ech11b_defectivity_pitch128",
              "cdsaxs_ech11b_defectivity_pitch127","cdsaxs_ech11b_defectivity_pitch124","cdsaxs_ech11b_defectivity_pitch121",
              "cdsaxs_ech11b_defectivity_pitch118","cdsaxs_ech11b_defectivity_pitch115","cdsaxs_ech11b_defectivity_pitch112"]
    x = [-41100,-38550,-34050,-29550,-25050,-20550,-16050,-11150,-9650,-5150,-650,3850,8350,12850,17000,18500,23000,27500,32000,36500, 41000]
    y = [  2000,  2000,  2000,  2000,  2000,  2000,  2000,2000,2000,2000,2000,2000,2000,2000,3900,3900,3900,3900,3900,3900,3900,    ]    
    det = [pil1M]

    det_exposure_time(exp_t, exp_t)
    for xs, ys, sample in zip(x, y, sample):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        for theta in np.linspace(th_ini, th_fin, th_st):
            yield from bps.mv(prs, theta)
            name_fmt = "{sample}_{th}deg"

            sample_name = name_fmt.format(sample=sample, th="%2.2d" % theta)
            sample_id(user_name="PG", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count(det, num=10)


def cd_saxs_old(sample, x, y, num=1, exp_t=1, step=121):
    det = [pil1M]

    det_exposure_time(exp_t, exp_t)
    yield from bps.mv(piezo.x, x)
    yield from bps.mv(piezo.y, y)

    for i, theta in enumerate(np.linspace(-60, 60, step)):
        yield from bps.mv(prs, theta)
        name_fmt = "{sample}_{num}_{th}deg"

        sample_name = name_fmt.format(sample=sample, num="%2.2d"%i, th="%2.2d"%theta)
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from bp.count(det, num=num)
        yield from bps.sleep(1)


def cdsaxs_all_pitch(sample, x, y, num=1, exp_t=1, step=121):
    pitches = ["p112nm","p113nm","p114nm","p115nm","p116nm","p117nm","p118nm","p119nm","p120nm","p121nm","p122nm","p123nm","p124nm","p125nm",
               "p126nm","p127nm","p128nm"]
    x_off = [0,1500,3000,4500,6000,7500,9000,10500,12000,13500,15000,16500,18000,19500,21000,22500,24000]
    det_exposure_time(exp_t, exp_t)
    for x_of, pitch in zip(x_off, pitches):
        yield from bps.mv(piezo.x, x + x_of)

        name_fmt = "{sample}_{pit}"
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        yield from cd_saxs_new(sample_name, x + x_of, y, num=1, exp_t=exp_t, step=step)


def night_patrice(exp_t=1):
    numero = 6
    det = [pil1M]

    # names = ['champs00', 'bkg_champs00','champs05','bkg_champs05','champs0-4','bkg_champs0-4','champs0-3', 'bkg_champs0-3']
    # xs = [-41100, -41100, 14100, 14100, -36450, -36550, -10250, -10250]
    # ys = [-7500, -8500, -7000, -8000, 5450, 6450, 5500, 6400]
    names = ["champs0-3", "bkg_champs0-3"]

    xs = [2220, 2220]
    ys = [6470, 7470]

    for name, x, y in zip(names, xs, ys):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        numero += 1
        name_fmt = "{sample}_num{numb}"
        sample_name = name_fmt.format(sample=name, numb=numero)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from cdsaxs_important_pitch(sample_name, x, y, num=1)
        # numero+=1
        # yield from cdsaxs_important_pitch(sample_name, x, y, num=1)

    names = ["champs00"]
    xs = [-14380]
    ys = [-6200]

    numero += 1
    name_fmt = "{sample}_num{numb}"
    sample_name = name_fmt.format(sample=names[0], numb=numero)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    yield from cdsaxs_important_pitch(sample_name, xs[0], ys[0], num=1)

    numero += 1
    name_fmt = "{sample}_num{numb}"
    sample_name = name_fmt.format(sample=names[0], numb=numero)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    yield from cdsaxs_important_pitch(sample_name, xs[0], ys[0], num=1)

    names = ["champs00", "bkg_champs00"]
    xs = [-14380, -14380]
    ys = [-6200, -7200]

    for name, x, y in zip(names, xs, ys):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        numero += 1

        name_fmt = "{sample}_num{numb}"
        sample_name = name_fmt.format(sample=name, numb=numero)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from cdsaxs_all_pitch(sample_name, x, y, num=1, step=61)

    numero += 1
    name_fmt = "{sample}_offset300_num{numb}"
    sample_name = name_fmt.format(sample=name, numb=numero)
    yield from cd_saxs_new(sample_name, xs[0], ys[0] + 300, num=1, exp_t=exp_t)

    numero += 1
    name_fmt = "{sample}_offset-300_num{numb}"
    sample_name = name_fmt.format(sample=name, numb=numero)
    yield from cd_saxs_new(sample_name, xs[0], ys[0] - 300, num=1, exp_t=exp_t)

    numero += 1
    name_fmt = "{sample}_num{numb}"
    sample_name = name_fmt.format(sample=name, numb=numero)
    yield from mesure_rugo(sample_name, xs[0], ys[0], num=200, exp_t=exp_t)

    numero += 1
    name_fmt = "{sample}_num{numb}"
    sample_name = name_fmt.format(sample=name, numb=numero)
    yield from mesure_rugo(sample_name, xs[1], ys[1], num=200, exp_t=exp_t)


def scan_boite_pitch(exp_t=1):
    sample = ["Echantillon03_defectivity","Echantillon04_defectivity","Echantillon11b_defectivity"]
    x = [-40050, -11150, 17000]
    y = [2000, 2000, 3900]
    det = [pil1M]

    pitches = np.linspace(128, 112, 17)

    det_exposure_time(exp_t, exp_t)
    for xs, ys, sample in zip(x, y, sample):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yield from bps.mvr(piezo.x, -1500)
        for i, pitch in enumerate(pitches):
            yield from bps.mvr(piezo.x, 1500)
            name_fmt = "{sample}_{pit}nm"

            sample_name = name_fmt.format(sample=sample, pit="%3.3d" % pitch)
            sample_id(user_name="PG", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count(det, num=10)


def macro_dinner():
    yield from scan_boite_pitch(1)
    yield from cd_saxs(-60, 60, 121, 2)


def NEXAFS_Ti_edge(t=0.5):

    dets = [pil300KW]
    name = "NEXAFS_echantillon2_Tiedge_ai1p4"
    # x = [8800]

    energies = np.linspace(4950, 5050, 101)

    det_exposure_time(t, t)
    name_fmt = "{sample}_{energy}eV_xbpm{xbpm}"

    for e in energies:
        yield from bps.mv(energy, e)
        sample_name = name_fmt.format(
            sample=name, energy=e, xbpm="%3.1f" % xbpm3.sumY.value
        )
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=1)

    yield from bps.mv(energy, 5030)
    yield from bps.mv(energy, 5010)
    yield from bps.mv(energy, 4990)
    yield from bps.mv(energy, 4970)
    yield from bps.mv(energy, 4950)


def NEXAFS_SAXS_Ti_edge(t=0.5):

    dets = [pil300KW, pil1M]
    name = "NEXAFS_SAXS_echantillon13realign_ai1p75_Tiedge"
    # x = [8800]

    energies = np.linspace(4950, 5050, 101)

    det_exposure_time(t, t)
    name_fmt = "{sample}_{energy}eV_xbpm{xbpm}"

    for e in energies:
        yield from bps.mv(energy, e)
        sample_name = name_fmt.format(
            sample=name, energy=e, xbpm="%3.1f" % xbpm3.sumY.value
        )
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=1)

    yield from bps.mv(energy, 5030)
    yield from bps.mv(energy, 5010)
    yield from bps.mv(energy, 4990)
    yield from bps.mv(energy, 4970)
    yield from bps.mv(energy, 4950)


def GISAXS_scan_boite(t=1):

    sample = "Echantillon13realign_gisaxs_scanpolyperiod_e4950eV_ai1p75"
    x = np.linspace(55900, 31900, 81)

    det = [pil1M]

    det_exposure_time(t, t)
    for k, xs in enumerate(x):
        yield from bps.mv(piezo.x, xs)

        name_fmt = "{sample}_pos{pos}"
        sample_name = name_fmt.format(sample=sample, pos="%2.2d" % k)
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from bp.count(det, num=1)


def fly_scan_ai(det, motor, cycle=1, cycle_t=10, phi=-0.6):
    start = phi - 30
    stop = phi + 30
    acq_time = cycle * cycle_t
    yield from bps.mv(motor, start)
    # yield from bps.mv(attn_shutter, 'Retract')
    det.stage()
    det.cam.acquire_time.put(acq_time)
    print(f"Acquire time before staging: {det.cam.acquire_time.get()}")
    st = det.trigger()
    for i in range(cycle):
        yield from list_scan([], motor, [start, stop])
    while not st.done:
        pass
    det.unstage()
    print(f"We are done after {acq_time}s of waiting")
    # yield from bps.mv(attn_shutter, 'Insert')


def sample_patrice_2020_3(exp_t=1):
    numero = 1
    det = [pil1M]
    # wafer = 'wafer16'
    # names = ['champs5', 'champs5_bkg', 'champs4', 'champs4_bkg', 'champs3', 'champs3_bkg']
    # names = ['champs-1', 'champs-1_bkg', 'champs-2', 'champs-2_bkg', 'champs-3', 'champs-3_bkg']

    wafer = "wafer25"
    # names = ['champs-1', 'champs-1_bkg', 'champs-2', 'champs-2_bkg', 'champs-3', 'champs-3_bkg']
    names = ["champs1", "champs1_bkg", "champs0", "champs0_bkg"]

    xs = [-3400, -3400, 22650, 22650]
    ys = [6360, 7300, 6410, 7300]
    zs = [1800, 1800, 1470, 1470]

    for name, x, y, z in zip(names, xs, ys, zs):
        yield from bps.mv(piezo.z, z)
        numero += 1
        name_fmt = "{sample}_num{numb}"
        sample_name = name_fmt.format(wafer=wafer, sample=name, numb=numero)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        if "bkg" in name:
            yield from cdsaxs_important_pitch(sample_name, x, y, num=1)
        else:
            yield from cdsaxs_important_pitch(sample_name, x, y, num=2)

    names = ["champs2","champs2_bkg","champs1","champs1_bkg","champs0","champs0_bkg"]

    xs = [-29420, -29420, -3400, -3400, 22650, 22650]
    ys = [6460, 7300, 6360, 7300, 6410, 7300]
    zs = [2130, 2130, 1800, 1800, 1470, 1470]

    for name, x, y, z in zip(names, xs, ys, zs):
        yield from bps.mv(piezo.z, z)
        numero += 1
        name_fmt = "{sample}_num{numb}"
        sample_name = name_fmt.format(sample=name, numb=numero)

        if "bkg" in name:
            yield from mesure_rugo(sample_name, x, y, num=10, exp_t=exp_t)
        else:
            yield from mesure_rugo(sample_name, x, y, num=100, exp_t=exp_t)

    yield from bps.mvr(pil1m_pos.x, -5)
    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique="gisaxs")

    for name, x, y, z in zip(names, xs, ys, zs):
        numero += 1
        name_fmt = "{sample}_num{numb}"
        sample_name = name_fmt.format(sample=name, numb=numero)
        yield from bps.mv(piezo.z, z)
        yield from mesure_db(sample_name, x, y, num=1, exp_t=1)

    yield from smi.modeMeasurement()
    yield from bps.mvr(pil1m_pos.x, 5)


def cdsaxs_important_pitch(sample, x, y, num=1, exp_t=1):
    pitches = ["p113nm", "p100nm"]

    if "bkg" in sample:
        x_off = [0, 0]
        y_off = [0, -13300]
    else:
        x_off = [0, 0]
        y_off = [0, -10500]

    det_exposure_time(exp_t, exp_t)
    for x_of, y_of, pitch in zip(x_off, y_off, pitches):
        yield from bps.mv(piezo.x, x + x_of)
        yield from bps.mv(piezo.y, y + y_of)

        name_fmt = "{sample}_{pit}"
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        yield from cd_saxs_new(sample_name, x + x_of, y + y_of, num=num, exp_t=exp_t)


def mesure_rugo(sample, x, y, num=200, exp_t=1):
    print(sample)
    pitches = ["p100nm"]

    if "bkg" in sample:
        x_off = [0]
        y_off = [-13300]
    else:
        x_off = [0]
        y_off = [-10500]

    yield from bps.mv(prs, -1)

    det_exposure_time(exp_t, exp_t)
    for x_of, y_of, pitch in zip(x_off, y_off, pitches):
        yield from bps.mv(piezo.x, x + x_of)
        yield from bps.mv(piezo.y, y + y_of)

        name_fmt = "{sample}_rugo_{pit}_up"
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        print(sample_name)
        sample_id(user_name="PG", sample_name=sample_name)

        yield from bp.count([pil1M], num=num)

    yield from bps.mvr(pil1m_pos.y, 4.3)
    for x_of, y_of, pitch in zip(x_off, y_off, pitches):
        yield from bps.mv(piezo.x, x + x_of)
        yield from bps.mv(piezo.y, y + y_of)
        name_fmt = "{sample}_rugo_{pit}_down"
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        sample_id(user_name="PG", sample_name=sample_name)
        yield from bp.count([pil1M], num=num)

    yield from bps.mvr(pil1m_pos.y, -4.3)


def mesure_db(sample, x, y, num=1, exp_t=1):
    pitches = ["p100nm"]
    if "bkg" in sample:
        x_off = [0]
        y_off = [-13300]
    else:
        x_off = [0]
        y_off = [-10500]
    yield from bps.mv(prs, -1)

    det_exposure_time(exp_t, exp_t)
    for x_of, y_of, pitch in zip(x_off, y_off, pitches):
        yield from bps.mv(piezo.x, x + x_of)
        yield from bps.mv(piezo.y, y + y_of)

        name_fmt = "{sample}_db_{pit}_att9x60umSn"
        sample_name = name_fmt.format(sample=sample, pit=pitch)
        sample_id(user_name="PG", sample_name=sample_name)

        yield from bp.count([pil1M], num=1)


def NEXAFS_P_edge(t=0.5):
    yield from bps.mv(waxs, 0)
    dets = [pil300KW]
    name = "nexafs_s4_wa0_0.5deg"

    energies = np.linspace(2140, 2200, 61)

    det_exposure_time(t, t)
    name_fmt = "{sample}_{energy}eV_xbpm{xbpm}"
    for e in energies:
        yield from bps.mv(energy, e)
        yield from bps.sleep(2)

        sample_name = name_fmt.format(
            sample=name, energy=e, xbpm="%3.2f" % xbpm3.sumY.value
        )
        sample_id(user_name="SR", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=1)

    yield from bps.mv(energy, 2190)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2180)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2170)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2160)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2150)
    yield from bps.sleep(2)
    yield from bps.mv(energy, 2140)
    yield from bps.sleep(2)


def cd_saxs_new2(th_ini, th_fin, th_st, exp_t=1):
    sample = "sample-33"
    det = [pil1M]
    yield from bps.mv(piezo.y, 1000)

    det_exposure_time(exp_t, exp_t)

    theta_zer=-4

    for num, theta in enumerate(np.linspace(th_ini, th_fin, th_st)):
        yield from bps.mv(prs, theta+theta_zer)
        name_fmt = "{sample}_8.3m_16.1keV_num{num}_{th}deg"

        sample_name = name_fmt.format(
            sample=sample, num="%2.2d" % num, th="%2.2d" % theta
        )
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")

        yield from bp.count(det, num=1)

    sample = "sample-33_bkg"
    yield from bps.mv(piezo.y, -3600)

    theta_zer=-4

    for num, theta in enumerate(np.linspace(th_ini, th_fin, th_st)):
        yield from bps.mv(prs, theta+theta_zer)
        name_fmt = "{sample}_8.3m_16.1keV_num{num}_{th}deg"

        sample_name = name_fmt.format(
            sample=sample, num="%2.2d" % num, th="%2.2d" % theta
        )
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        
        yield from bps.sleep(2)
        yield from bp.count(det, num=1)


def rugo_contact(exp_t=1):
    sample = "sample-10_rugo_8.3m_16.1keV_5s"
    det = [pil1M]

    det_exposure_time(exp_t, exp_t)
    sample_id(user_name="PG", sample_name=sample)

    yield from bp.count(det, num=50)


def cd_saxs_new(th_ini, th_fin, th_st, exp_t=1, sample='test', nume=1, det=[pil1M]):

    det_exposure_time(exp_t, exp_t)

    for num, theta in enumerate(np.linspace(th_ini, th_fin, th_st)):
        yield from bps.mv(prs, theta)
        name_fmt = "{sample}_9.2m_16.1keV_num{num}_{th}deg_bpm{bpm}"
        sample_name = name_fmt.format(sample=sample, num="%2.2d"%num, th="%2.2d"%theta, bpm="%1.3f"%xbpm3.sumX.get())
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(det, num=nume)


def night_1_cdsaxs(t=1):
    det = [pil1M]
    det_exposure_time(t, t)

    names = ['w08_-3-1', 'w08_-3-1_bkg', 'w08_1-1', 'w08_1-1_bkg', 'w08_2-1', 'w08_2-1_bkg', 
             'w08_-1-1', 'w08_-1-1_bkg', 'w08_0-1', 'w08_0-1_bkg', 'w08_3-1', 'w08_3-1_bkg', 'ech_tim_ref', 'ech_tim_ref_bkg']
    x =     [    -32000,         -32000,     -1400,         -1400,     21400,         21400, 
                 -32900,         -32900,     -9800,         -9800,     20700,         20700,         40000,             40000]
    x_hexa =[       0.1,            0.1,       0.3,           0.3,       0.5,           0.5, 
                    0.5,            0.5,       0.5,           0.5,       0.5,           0.5,           0.5,               0.5]
    y=      [      8900,           6500,      8900,          6000,      8000,          5900, 
                  -7000,          -9700,     -7000,         -9700,     -7000,        -10500,         -8000,            -10000]
    z=      [     10800,          10800,      9600,          9600,      8900,          8900, 
                  11000,          11000,      9700,          9700,      8900,          8900,          7900,              7900]
    chi=[           0.3,            0.3,      -0.2,          -0.2,      -0.2,          -0.2, 
                  -0.05,          -0.05,     -0.05,         -0.05,      -0.2,          -0.2,          -0.5,               0.5]
    th =[          -0.4,           -0.4,      -0.4,          -0.4,      -0.4,          -0.4,
                 -0.633,         -0.633,     -0.43,         -0.43,       0.3,           0.3,          -2.7,              -2.7]

    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"


    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)
        yield from bps.mv(piezo.th, ths)

        if 'bkg' in name:
            num=1
        else:
            num=2

        yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name, nume=num)



def cdsaxs_echolivier(t=1):
    det = [pil1M]
    det_exposure_time(t, t)

    # names = ['w03_c0_p113', 'w03_c0_p113_bkg', 'w03_c0_p118', 'w03_c0_p118_bkg', 'w03_c0_p100', 'w03_c0_p100_bkg',
    #          'w03_c1_p113', 'w03_c1_p113_bkg', 'w03_c1_p118', 'w03_c1_p118_bkg', 'w03_c1_p100', 'w03_c1_p100_bkg',
    #          'w03_c2_p113', 'w03_c2_p113_bkg', 'w03_c2_p118', 'w03_c2_p118_bkg', 'w03_c2_p100', 'w03_c2_p100_bkg']

    # x =     [       -34900,            -34900,        -10800,            -10800,        -32900,            -32900, 
    #                  -8900,             -8900,         15200,             15200,         -6900,             -6900, 
    #                  17100,             17100,         41150,             41150,         19100,             19100]
    # x_hexa =[          0.5,               0.5,           0.5,               0.5,           0.5,               0.5, 
    #                    0.5,               0.5,           0.5,               0.5,           0.5,               0.5,
    #                    0.5,               0.5,           0.5,               0.5,           0.5,               0.5]
    # y=      [        -4700,             -5400,         -4700,             -5400,          5300,              7600, 
    #                  -4700,             -5400,         -4800,             -5500,          5300,              7600,
    #                  -4800,             -5500,         -4900,             -5600,          5300,              7600,]
    # z=      [        11000,             11000,         10050,             10050,         11000,             11000, 
    #                  10050,             10050,          9100,              9100,         10050,             10050,
    #                   9100,              9100,          8080,              8080,          9100,              9100,]
    # chi=[                0,                 0,             0,                 0,             0,                 0, 
    #                      0,                 0,             0,                 0,             0,                 0,
    #                      0,                 0,             0,                 0,             0,                 0]
    # th =[                0,                 0,             0,                 0,             0,                 0,
    #                      0,                 0,             0,                 0,             0,                 0,
    #                      0,                 0,             0,                 0,             0,                 0]

    # names = ['w03_c3_p113', 'w03_c3_p113_bkg', 'w03_c3_p128', 'w03_c3_p128_bkg', 'w03_c3_p100', 'w03_c3_p100_bkg',
    #          'w03_c4_p113', 'w03_c4_p113_bkg', 'w03_c4_p128', 'w03_c4_p128_bkg', 'w03_c4_p100', 'w03_c4_p100_bkg',
    #          'w03_c5_p113', 'w03_c5_p113_bkg', 'w03_c5_p128', 'w03_c5_p128_bkg', 'w03_c5_p100', 'w03_c5_p100_bkg']

    # x =     [       -35150,            -35150,        -12500,            -12500,        -34150,            -34150, 
    #                  -9100,             -9100,         13500,             13500,         -8600,             -8600, 
    #                  16950,             16950,         39100,             39100,         19100,             19100]
    # x_hexa =[          0.5,               0.5,           0.5,               0.5,           0.5,               0.5, 
    #                    0.5,               0.5,           0.5,               0.5,           0.5,               0.5,
    #                    0.5,               0.5,           0.5,               0.5,           0.5,               0.5]
    # y=      [        -4300,             -5100,         -4400,             -5100,          7000,              8100, 
    #                  -4300,             -5100,         -4400,             -5200,          7000,              8100,
    #                  -4400,             -5200,         -4500,             -5200,          7000,              8100]
    # z=      [        10900,             10900,         10050,             10050,         10900,             10900, 
    #                  10050,             10050,          9150,              9150,         10050,             10050,
    #                   9150,              9150,          8080,              8080,          9150,              9150]
    # chi=[                0,                 0,             0,                 0,             0,                 0, 
    #                      0,                 0,             0,                 0,             0,                 0,
    #                      0,                 0,             0,                 0,             0,                 0]
    # th =[                0,                 0,             0,                 0,             0,                 0,
    #                      0,                 0,             0,                 0,             0,                 0,
    #                      0,                 0,             0,                 0,             0,                 0]

    # names = ['w03_c-3_p113', 'w03_c-3_p113_bkg', 'w03_c-3_p128', 'w03_c-3_p128_bkg', 'w03_c-3_p100', 'w03_c-3_p100_bkg',
    #          'w03_c-2_p113', 'w03_c-2_p113_bkg', 'w03_c-2_p128', 'w03_c-2_p128_bkg', 'w03_c-2_p100', 'w03_c-2_p100_bkg',
    #          'w03_c-1_p113', 'w03_c-1_p113_bkg', 'w03_c-1_p128', 'w03_c-1_p128_bkg', 'w03_c-1_p100', 'w03_c-1_p100_bkg']

    # x =     [       -35250,            -35250,        -12750,            -12750,        -33750,            -33750, 
    #                  -9300,             -9300,         13500,             13500,         -7800,             -7800, 
    #                  16700,             16700,         39100,             39100,         18200,             18200]
    # x_hexa =[          0.5,               0.5,           0.5,               0.5,           0.5,               0.5, 
    #                    0.5,               0.5,           0.5,               0.5,           0.5,               0.5,
    #                    0.5,               0.5,           0.5,               0.5,           0.5,               0.5]
    # y=      [        -4400,             -5300,         -4500,             -5400,          6200,              7800, 
    #                  -4600,             -5400,         -4700,             -5500,          6200,              7800,
    #                  -4700,             -5500,         -4700,             -5700,          6200,              7800]
    # z=      [        10900,             10900,         10000,             10000,         10900,             10900, 
    #                  10000,             10000,          9100,              9100,         10050,             10050,
    #                   9100,              9100,          8100,              8100,          9100,              9100]
    # chi=[              0.1,               0.1,           0.1,               0.1,           0.1,               0.1, 
    #                    0.1,               0.1,           0.1,               0.1,           0.1,               0.1,
    #                    0.1,               0.1,           0.1,               0.1,           0.1,               0.1]
    # th =[             -0.3,              -0.3,          -0.3,              -0.3,          -0.3,              -0.3,
    #                   -0.3,              -0.3,          -0.3,              -0.3,          -0.3,              -0.3,
    #                   -0.3,              -0.3,          -0.3,              -0.3,          -0.3,              -0.3]

    names = ['w03_c0_p113', 'w03_c0_p113_bkg', 'w03_c1_p113', 'w03_c1_p113_bkg', 'w03_c2_p113', 'w03_c2_p113_bkg']
    x =     [       -35050,            -35050,         -9150,             -9150,         16950,             16950]
    x_hexa =[          0.5,               0.5,           0.5,               0.5,           0.5,               0.5]
    y=      [        -4400,             -5300,         -4400,             -5400,         -4500,             -5400]
    z=      [        10900,             10900,         10000,             10000,          9100,              9100]
    chi=[            -0.05,             -0.05,         -0.05,             -0.05,         -0.05,             -0.05]
    th =[              0.3,               0.3,           0.3,               0.3,           0.3,               0.3]


    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"


    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)
        yield from bps.mv(piezo.th, ths)

        if 'w03_c-3_p113' in name or 'w03_c-1_p113' in name:
            num=10
        else:
            num=2

        yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name, nume=num)



#sdd=   [8.3, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.6]
#bs_pos=[1.7, 1.7, 1.5, 1.5, 1.9, 2.1, 2.1, 2.1, 2.1]

def rugo(t=1, sdd='8.30', num=10, name='test', ys=[0, 0], th=0):
    det = [pil1M]
    det_exposure_time(t, t)

    yield from bps.mv(piezo.y, ys[0])
    name_fmt = "{name}_rugo_{sdd}m_16.1keV_th{th}deg_dn"
    sample_name = name_fmt.format(name=name, sdd=sdd, th="%1.1f"%th)
    sample_id(user_name="PG", sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    yield from bps.mv(pil1m_pos.y, -3.7)
    yield from bp.count(det, num=num)


    name_fmt = "{name}_rugo_{sdd}m_16.1keV_th{th}deg_up"
    sample_name = name_fmt.format(name=name, sdd=sdd, th="%1.1f"%th)
    sample_id(user_name="PG", sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    yield from bps.mv(pil1m_pos.y, -8.0)
    yield from bp.count(det, num=num)


    yield from bps.mv(piezo.y, ys[1])

    name_fmt = "{name}_bkg_rugo_{sdd}m_16.1keV_th{th}deg_up"
    sample_name = name_fmt.format(name=name, sdd=sdd, th="%1.1f"%th)
    sample_id(user_name="PG", sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    yield from bps.mv(pil1m_pos.y, -8.0)
    yield from bp.count(det, num=num)
    

    name_fmt = "{name}_bkg_rugo_{sdd}m_16.1keV_th{th}deg_dn"
    sample_name = name_fmt.format(name=name, sdd=sdd, th="%1.1f"%th)
    sample_id(user_name="PG", sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    yield from bps.mv(pil1m_pos.y, -3.7)
    yield from bp.count(det, num=num)



def measure_pitch(t=1):
    name_fmt = "w03_c-2_p{pitch}_8.3m_16.1keV_0deg"
    pitches = np.linspace(112, 128, 17)
    xs = -10750+1500*np.linspace(0, 16, 17)

    yield from bps.mv(prs, -5.25)
    yield from bps.mv(piezo.y, -4500)

    for pitch, x in zip(pitches, xs):
        yield from bps.mv(piezo.x, x)
        yield from bps.sleep(2)

        sample_name = name_fmt.format(pitch="%3.3d"%pitch)
        print(sample_name)
        sample_id(user_name="PG", sample_name=sample_name)
        
        yield from bp.count(det, num=1)


# def run_night2(t=1):
#     # yield from cdsaxs_echolivier(1)
    
#     # proposal_id("2022_3", "311003_Reche1")
#     # yield from bps.mv(prs, -5.25)
#     # yield from bps.mv(piezo.x, -35250)
#     # yield from bps.mv(piezo.z, 10900)

#     # yield from rugo(t=1, sdd='8.30', num=100, name='w03_c-3_p113', ys=[-4400, -5300])
    
#     # yield from bps.mv(piezo.x, 16700)
#     # yield from bps.mv(piezo.z, 9100)
#     # yield from rugo(t=1, sdd='8.30', num=100, name='w03_c-1_p113', ys=[-4700, -5500])

#     # proposal_id("2022_3", "311003_Dubreuil1")
#     # yield from measure_pitch(1)



def run_day2(t=1):

    proposal_id("2022_3", "311003_Reche1")

    yield from bps.mv(prs, -5.25)
    yield from bps.mv(piezo.x, -35250)
    yield from bps.mv(piezo.z, 10900)
    yield from rugo(t=1, sdd='8.30', num=100, name='w03_c-3_p113', ys=[-4400, -5300], th=0)

    yield from bps.mv(prs, -17.25)
    yield from bps.mv(piezo.x, -35250)
    yield from bps.mv(piezo.z, 10900)
    yield from rugo(t=1, sdd='8.30', num=100, name='w03_c-3_p113', ys=[-4400, -5300], th=-12)


    sdds=   [8.3, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.6]
    bs_pos=[1.7, 1.7, 1.5, 1.5, 1.9, 2.1, 2.1, 2.1, 2.1]
    for sdd, bs in zip(sdds, bs_pos):
        yield from bps.mv(pil1m_pos.z, 1000*sdd)
        yield from bps.mv(pil1m_bs_rod.x, bs)


        yield from bps.mv(prs, -5.25)
        yield from bps.mv(piezo.x, -35250)
        yield from bps.mv(piezo.z, 10900)
        yield from rugo(t=1, sdd='%1.2f'%sdd, num=10, name='w03_c-3_p113', ys=[-4400, -5300], th=0)

        yield from bps.mv(prs, -17.25)
        yield from bps.mv(piezo.x, -35250)
        yield from bps.mv(piezo.z, 10900)
        yield from rugo(t=1, sdd='%1.2f'%sdd, num=10, name='w03_c-3_p113', ys=[-4400, -5300], th=-12)




def measure_nicolas2(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)
    
    # name_fmt = "ech1_14.5keV_ai_7.0deg_l{ligne}_c{colone}_wa{wax}deg"
    # xs = 22925+ 200 * np.linspace(0, 39, 40)
    # ys1 = 4460.5-24.3*np.linspace(0, 39, 40)
    # ys2 = 4424.5-24.3*np.linspace(0, 39, 40)

    name_fmt = "ech2_14.5keV_ai_7.0deg_l{ligne}_c{colone}_wa{wax}deg"
    # xs = -6680+ 200 * np.linspace(0, 39, 40)
    # ys1 = 4654.5-24.3*np.linspace(0, 39, 40)
    # ys2 = 4619.5-24.3*np.linspace(0, 39, 40)
    
    xs = -6680+ 200 * np.linspace(20, 39, 20)
    ys1 = 4654.5-24.3*np.linspace(20, 39, 20)
    ys2 = 4619.5-24.3*np.linspace(20, 39, 20)


    # yield from bps.mv(prs, -5.5)
    # yield from bps.mv(piezo.th, 7.243685)
    # yield from bps.mv(piezo.ch, 0.1)
    yield from bps.mv(piezo.z, 9300)
    waxs_arc = [0, 20]

    for i, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

        for yy, (y1, y2) in enumerate(zip(ys1, ys2)):
            # y1, y2 = ys1[::-1][xx], ys2[::-1][xx]
            ys = np.linspace(y1, y2, 40)[::-1]

            for xx, x in enumerate(xs[::-1]):
                y=ys[xx]
                yield from bps.mv(piezo.y, y)      
                yield from bps.mv(piezo.x, x)

                sample_name = name_fmt.format(ligne='%2.2d'%xx, colone='%2.2d'%yy, wax='%2.2d'%wa)
                print(sample_name)
                sample_id(user_name="NV", sample_name=sample_name)

                yield from bp.count(dets, num=1)




def measure_nicolas_bkg(t=1):
    dets = [pil1M, pil900KW]
    det_exposure_time(t, t)
    
    name_fmt = "ech1_14.5keV_ai_7.0deg_bkg_wa{wax}deg"
    waxs_arc = [0, 20]

    for i, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if wa < 10 else [pil1M, pil900KW]

        sample_name = name_fmt.format(wax='%2.2d'%wa)
        print(sample_name)
        sample_id(user_name="NV", sample_name=sample_name)

        yield from bp.count(dets, num=1)



# 22950 3512.924     4959.92
# 23145 3512.06      4459.06
# 30760 3477.79      4425.076

#ai 0.27715
#phi -3.24



def cd_gisaxs_phi(phi0, phi_ini, phi_fin, phi_st, ai0, ai, exp_t=1, sample='test', nume=1):
    sample = sample+'phiscan'
    det = [pil1M]
    det_exposure_time(exp_t, exp_t)

    yield from bps.mv(stage.th, ai0+ai)

    for num, phi in enumerate(np.linspace(phi_ini, phi_fin, phi_st)):        
        yield from bps.mv(prs, phi0+phi)
        
        name_fmt = "{sample}_5m_16.1keV_num{num}_phi{phii}deg_ai{aii}deg"
        sample_name = name_fmt.format(sample=sample, num="%2.2d"%num, phii="%1.3f"%phi, aii="%1.2f"%ai)
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(det, num=nume)

def cd_gisaxs_alphai(ai0, ai_ini, ai_fin, ai_st, phi0, phi, exp_t=1, sample='test', nume=1):
    sample = sample+'aiscan'
    det = [pil1M]
    det_exposure_time(exp_t, exp_t)

    yield from bps.mv(prs, phi0+phi)

    for num, ai in enumerate(np.linspace(ai_ini, ai_fin, ai_st)):        
        yield from bps.mv(stage.th, ai0+ai)
        
        name_fmt = "{sample}_5m_16.1keV_num{num}_phi{phii}deg_ai{aii}deg"
        sample_name = name_fmt.format(sample=sample, num="%2.2d"%num, phii="%1.2f"%phi, aii="%1.3f"%ai)
        sample_id(user_name="PG", sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(det, num=nume)


def nigh_cdgisaxs(t=0.5):
    #ech c-3 prs -3.33, th -0.504, chi 0.0765, hexa_th 0.29925 stage_y 0.032
    yield from bps.mv(stage.y, -0.022)
    yield from bps.mv(piezo.x, 23000)
    yield from bps.mv(piezo.z, 6300)

    yield from bps.mv(piezo.ch, 0.0765)
    yield from bps.mv(piezo.th, -0.504)

    phi0, ai0 = -3.33, 0.29614
    phi_ini, phi_fin, phi_st = -5, 5, 2001
    sample = 'w03_c-3_p100nm'

    # for ai in [0.35, 0.45]:
    #     yield from cd_gisaxs_phi(phi0, phi_ini, phi_fin, phi_st, ai0, ai, exp_t=t, sample=sample, nume=1)


    ai_ini, ai_fin, ai_st = 0.3, 1, 701

    for phi in [0, -0.5]:
        yield from cd_gisaxs_alphai(ai0, ai_ini, ai_fin, ai_st, phi0, phi, exp_t=t, sample=sample, nume=1)


    #ech c-3 prs -3.342, th -0.504, chi 0.098, hexa_th 0.28768 stage_y 0.032
    
    # yield from bps.mv(stage.y, -0.0157)
    # yield from bps.mv(piezo.x, -30000)
    # yield from bps.mv(piezo.z, 8300)

    # yield from bps.mv(piezo.ch, 0.0985)
    # yield from bps.mv(piezo.th, -0.504)

    # phi0, ai0 = -3.342, 0.28768 
    # phi_ini, phi_fin, phi_st = -5, 5, 2001
    # sample = 'w03_c-1_p100nm'

    # for ai in [0.35, 0.45]:
    #     yield from cd_gisaxs_phi(phi0, phi_ini, phi_fin, phi_st, ai0, ai, exp_t=t, sample=sample, nume=1)


    # ai_ini, ai_fin, ai_st = 0.3, 1, 701

    # for phi in [0, -0.5]:
    #     yield from cd_gisaxs_alphai(ai0, ai_ini, ai_fin, ai_st, phi0, phi, exp_t=t, sample=sample, nume=1)

#0.28507 prs -3.129




def cdsaxs_echPaul_2023_2(t=1):
    det = [pil1M]
    det_exposure_time(t, t)

    names = ['E1_001', 'E1_001_bkg', 'E1_010', 'E1_010-bkg','E1_100', 'E1_100_bkg', 'E2_001', 'E2_001_bkg', 'E2_010', 'E2_010_bkg', 'E2_100', 'E2_100_bkg']
    x =     [  -21300,       -23000,    -8400,        -9950,     700,         -900,    11600,        10100,    23300,        21800,    34700,        33100]
    x_hexa =[    0.15,         0.15,     0.15,         0.15,    0.15,         0.15,     0.15,         0.15,     0.15,         0.15,     0.15,         0.15]
    y=      [   -5200,        -5200,    -5700,        -5700,   -6200,        -6200,    -6400,        -6400,    -6200,        -6200,    -6200,        -6200]
    z=      [    8800,         8800,     8800,         8800,    8800,         8800,     8800,         8800,     8800,         8800,     8800,         8800]
    chi=    [       0,            0,        0,            0,       0,            0,     -1.5,         -1.5,     -1.8,         -1.8,     -1.6,         -1.6]
    th =    [       0,            0,        0,            0,       0,            0,        0,            0,        0,            0,        0,            0]


    names = [ 'bkg']
    x =     [-17500]
    x_hexa =[  0.15]
    y=      [ -9200]
    z=      [  8800]
    chi=    [     0]
    th =    [     0]

    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"


    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)
        yield from bps.mv(piezo.th, ths)

        num=2

        yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name, nume=num)




def cdsaxs_ocd_2023_2(t=1):
    det = [pil1M]
    det_exposure_time(t, t)

    # names = ['w25_cm4', 'w25_cm4_bkg', 'w25_cm3', 'w25_cm3_bkg', 'w25_cm2', 'w25_cm2_bkg', 'w25_cm1', 'w25_cm1_bkg']
    # x =     [  -27600,         -27600,    -12000,        -12000,     18700,        18700,     38500,         38500]
    # x_hexa =[    0.15,           0.15,      0.15,          0.15,      0.15,          0.15,      0.15,          0.15]
    # y=      [   -7100,          -4800,     -7100,         -4800,     -7100,         -4800,     -7100,         -4800]
    # z=      [    4800,           4800,      4800,          4800,      4800,          4800,      4800,          4800]
    # chi=    [     -0.7,          -0.7,      -0.7,          -0.7,      -0.7,          -0.7,      -0.7,          -0.7]
    # th =    [       0,              0,         0,             0,         0,             0,         0,             0]


    # names = ['w25_c0', 'w25_c0_bkg', 'w25_c1', 'w25_c1_bkg', 'w25_c2', 'w25_c2_bkg']
    # x =     [   -9000,        -9000,    17000,        17000,    36500,        36500]
    # x_hexa =[    0.15,         0.15,     0.15,         0.15,     0.15,         0.15]
    # y=      [   -7100,        -4800,    -7100,        -4800,    -7100,        -4800]
    # z=      [    4800,         4800,     4800,         4800,     4800,         4800]
    # chi=    [     -0.7,        -0.7,     -0.7,         -0.7,     -0.7,         -0.7]
    # th =    [       0,            0,        0,            0,        0,            0]

    names = ['w25_c3', 'w25_c3_bkg', 'w25_c4', 'w25_c4_bkg', 'w25_c5', 'w25_c5_bkg']
    x =     [   -8000,        -8000,    18000,        17000,    37000,        37000]
    x_hexa =[    0.15,         0.15,     0.15,         0.15,     0.15,         0.15]
    y=      [   -7100,        -4500,    -7100,        -4500,    -7100,        -4500]
    z=      [    4800,         4800,     4800,         4800,     4800,         4800]
    chi=    [     -0.4,        -0.4,     -0.4,         -0.4,     -0.4,         -0.4]
    th =    [       0,            0,        0,            0,        0,            0]

    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"


    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)
        yield from bps.mv(piezo.th, ths)

        if 'bkg' not in name:
            for xx in [-4000, 0, 4000]:
                for yy in [-1000, 0, 1000]:
                    yield from bps.mv(piezo.x, xs + xx)
                    yield from bps.mv(piezo.y, ys + yy)
                    num=1
                    yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'xx%.1d_yy%.1d'%(0.001*xx, 0.001*yy), nume=num)

        else:                    
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            num=2
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name, nume=num)

    

def cdsaxs_ovl_2023_2(t=1):
    det = [pil1M]
    det_exposure_time(t, t)


    names = ['w09ovl_c00-p112', 'w09ovl_c00_bkg-p112', 'w09ovl_c00-p128', 'w09ovl_c00_bkg-p128', 'w09ovl_-10-p112', 'w09ovl_c-10_bkg-p112', 'w09ovl_-10-p112', 'w09ovl_c-10_bkg-p112']
    x =     [           -21100,                -20400,              2900,                  2100,              4900,                   5900,             28900,                  27900]
    x_hexa =[             0.15,                  0.15,              0.15,                  0.15,              0.15,                   0.15,              0.15,                   0.15]
    y=      [             -900,                  -100,             -1000,                  -200,             -1000,                   -200,             -1200,                   -400]
    z=      [             4800,                  4800,              4800,                  4800,              4800,                   4800,              4800,                   4800]
    chi=    [             -0.6,                  -0.6,              -0.6,                  -0.6,              -0.6,                   -0.6,              -0.6,                   -0.6]
    th =    [                0,                     0,                0,                      0,                 0,                      0,                 0,                      0]

    names = [ 'w09ovl_-10-p118', 'w09ovl_c-10_bkg-p118']
    x =     [             28900,                  27900]
    x_hexa =[              0.15,                   0.15]
    y=      [             -1200,                   -400]
    z=      [              4800,                   4800]
    chi=    [              -0.6,                   -0.6]
    th =    [                 0,                      0]



    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"


    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)
        yield from bps.mv(piezo.th, ths)
                  
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        num=2
        if 'bkg' not in name:
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet1', nume=num)
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet2', nume=num)
        else:
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name, nume=1)



    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
        if 'bkg' not in name:
            yield from bps.mv(stage.x, xs_hexa)
            yield from bps.mv(piezo.z, zs)
            yield from bps.mv(piezo.ch, chis)
            yield from bps.mv(piezo.th, ths)
                    
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            num=2
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet3', nume=num)





def cdwaxs_echPaulSophie_2023_2(t=1):
    det = [pil900KW]
    waxs_arc =[0, 20]
    det_exposure_time(t, t)

    yield from bps.mv(stage.y, -9)

    names = ['echsoph_E','echpaul_01','echpaul_02','echpaul_04','echpaul_05','echpaul_06', 'echsoph_F']
    x =     [      41000,       32000,       23000,        3000,       -8000,      -18000,      -33000]
    x_hexa =[       0.15,        0.15,        0.15,        0.15,        0.15,        0.15,        0.15]
    y=      [      -9000,       -9000,       -9000,       -9000,       -9000,       -9000,       -9000]
    z=      [       4550,        4550,        4550,        4550,        4550,        4550,        4550]
    chi=    [       -0.5,        -0.5,        -0.5,        -0.5,        -0.5,        -0.5,        -0.5]

    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"


    for name, xs, xs_hexa, ys, zs, chis in zip(names, x, x_hexa, y, z, chi):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)

        num=1

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            name = name+'_wa%sdeg'%wa

            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name, nume=num, det=det)
    
    
    
    yield from bps.mv(stage.y, 0)

    names = ['E1_01_A4','E1_01_C3','E1_01_D3','E1_10_A4','E1_10_C3','E1_10_D3','E1_100_A4','E1_100_C3','E1_100_D3',
             'E2_01_A4','E2_01_C3','E2_01_D3','E2_10_A4','E2_10_C3','E2_10_D3','E2_100_A4','E2_100_C3','E2_100_D3']
    x =     [     35400,     39300,     41300,     22900,     24900,     26900,       9700,      13700,      15500, 
                   -600,      3300,      5300,    -11700,     -7800,     -5700,     -22100,     -18300,     -16300]
    x_hexa =[      0.15,      0.15,      0.15,      0.15,      0.15,      0.15,       0.15,       0.15,       0.15,
                   0.15,      0.15,      0.15,      0.15,      0.15,      0.15,       0.15,       0.15,       0.15]
    y=      [      5800,      7900,      7900,      5700,      7800,      7900,       9700,       8000,       8000, 
                   5900,      7800,      7800,      6000,      8100,      8100,       5300,       7600,       7500]
    z=      [      4550,      4550,      4550,      4550,      4550,      4550,       4550,       4550,       4550,
                   4550,      4550,      4550,      4550,      4550,      4550,       4550,       4550,       4550]
    chi=    [      -0.5,      -0.5,      -0.5,      -0.5,      -0.5,      -0.5,       -0.5,       -0.5,       -0.5,
                   -0.5,      -0.5,      -0.5,      -0.5,      -0.5,      -0.5,       -0.5,       -0.5,       -0.5]

    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"


    for name, xs, xs_hexa, ys, zs, chis in zip(names, x, x_hexa, y, z, chi):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)

        num=1

        for i, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            name = name+'_wa%sdeg'%wa

            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name, nume=num, det=det)



def cdsaxs_ovl_2023_3(t=1):
    det = [pil1M]
    det_exposure_time(t, t)

    names = ['ech1_p128', 'ech1_bkg_p128', 'ech2_p128', 'ech2_bkg_p128', 'ech3_p128', 'ech3_bkg_p128', 'ech4_p128', 'ech4_bkg_p128', 'ech5_p128','ech5_bkg_p128']
    x =     [     -44200,          -46100,      -25500,          -26500,       -1300,            1700,       16400,           15400,       36700,          35600]
    x_hexa =[      0.365,           0.365,       0.265,           0.265,       0.265,           0.265,       0.265,           0.265,       0.065,          0.065]
    y=      [      -6300,           -8500,       -7500,           -9600,       -7500,           -9600,       -7500,           -9600,       -8000,         -10000]
    z=      [      13310,           13310,       13410,           13410,       13310,           13310,       13110,           13110,       13210,          13210]
    chi=    [     -1.367,          -1.367,      -0.067,          -0.067,      -0.367,          -0.367,       0.433,           0.433,      -0.167,         -0.167]
    th =    [      -0.15,           -0.15,       -0.15,           -0.15,       -0.15,           -0.15,       -0.15,           -0.15,       -0.15,          -0.15]

    assert len(names) == len(x), f"len of x ({len(x)}) is different from number of samples ({len(names)})"
    assert len(names) == len(y), f"len of y ({len(y)}) is different from number of samples ({len(names)})"
    assert len(names) == len(x_hexa), f"len of x_hexa ({len(x_hexa)}) is different from number of samples ({len(names)})"
    assert len(names) == len(z), f"len of z ({len(z)}) is different from number of samples ({len(names)})"
    assert len(names) == len(chi), f"len of y ({len(chi)}) is different from number of samples ({len(names)})"
    assert len(names) == len(th), f"len of z ({len(th)}) is different from number of samples ({len(names)})"


    proposal_id("2023_3", "311000_Freychet_04")
    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.ch, chis)
        yield from bps.mv(piezo.th, ths)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        num=5
        if 'bkg' not in name:
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet1', nume=num)
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet2', nume=num)
        else:
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name, nume=1)

    proposal_id("2023_3", "311000_Freychet_05")
    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names[:1], x[:1], x_hexa[:1], y[:1], z[:1], chi[:1], th[:1]):
        if 'bkg' not in name:
            yield from bps.mv(stage.x, xs_hexa)
            yield from bps.mv(piezo.z, zs)
            yield from bps.mv(piezo.ch, chis)
            yield from bps.mv(piezo.th, ths)
                    
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            
            det_exposure_time(0.1, 0.1)
            num=20
            yield from cd_saxs_new(-60, 60, 241, exp_t=t, sample=name+'testfinestep', nume=num)
            det_exposure_time(t, t)


    proposal_id("2023_3", "311000_Freychet_06")

    for name, xs, xs_hexa, ys, zs, chis, ths in zip(names, x, x_hexa, y, z, chi, th):
        if 'bkg' not in name:
            yield from bps.mv(stage.x, xs_hexa)
            yield from bps.mv(piezo.z, zs)
            yield from bps.mv(piezo.ch, chis)
            yield from bps.mv(piezo.th, ths)
                    
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            num=5
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet3', nume=num)
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet4', nume=num)
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet5', nume=num)
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet6', nume=num)
            yield from cd_saxs_new(-60, 60, 121, exp_t=t, sample=name+'repet7', nume=num)
