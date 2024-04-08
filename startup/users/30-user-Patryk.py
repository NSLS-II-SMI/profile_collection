def patryk_saxs_overnight(t=1):
    """
    SAXS mapping
    """

    names =     ['ORF7A-C-60um', 'ORF7A-C-60um-bkg', 'ORF7A-D-50um-wet', 'ORF7A-D-50um-wet-bkg', 
             'ORF7A-D-50um-dry', 'ORF7A-D-50um-dry-bkg', ]

    piezo_x =   [         14000,              19000,             -11000,               -8000, 
                         -18700,                 -16100, ]
    
    piezo_y =   [             0,                  0,               2200,                2200, 
                          -2100,                  -3100, ]
    
    piezo_z =   [          7700,               7700,               7900,                7900, 
                           7900,                   7900, ]

    names = [n + '-grid01' for n in names]

    assert len(names)   == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x) == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_z), f"Wrong list lenghts"

    # Move WAXS out of the way
    if waxs.arc.position < 19.5:
        yield from bps.mv(waxs, 20)
    dets = [pil1M]
    det_exposure_time(t, t)

    for name, x, y, z, in zip(names, piezo_x, piezo_y, piezo_z):
        yield from bps.mv(piezo.x, x,
                          piezo.y, y,
                          piezo.z, z)

        sample_name = f'{name}{get_scan_md()}'
        sample_id(user_name='PW', sample_name=sample_name)
        print(f"\n\n\n\t=== Sample: {sample_name} ===")

        # Take on axis camera
        yield from bp.count([OAV_writing])

        scan_id = db[-1].start['scan_id'] + 1
        msg = f'sample: {sample_name}\nscan_id: {scan_id}'
        olog(msg, logbooks='Experiments')

        y_range = [-3000, 3000, 31] if 'ORF7A-D-50um' not in name else [-2000, 2000, 81]
        x_range = [-3000, 3000, 31] if 'ORF7A-D-50um' not in name else [-2000, 2000, 21]

        if 'bkg' not in name:
            yield from rel_grid_scan([pil1M], piezo.y, *y_range, piezo.x, *x_range)

        else:
            yield from rel_grid_scan([pil1M], piezo.y, -500, 500, 5, piezo.x, -500, 500, 5)


def run_swaxs_Dominik_2023_1(t=0.1):
    """
    Take WAXS and SAXS at a few sample positions for averaging

    Specify central positions on the samples with xlocs and ylocs,
    then offsets from central positions with x_off and y_off. Run
    WAXS arc as the slowest motor.
    """

    names_1   = [   'D123', 'FeEDTA', 'Ni5Z30', '10RhZ23', 'D133', '1.0Pdfresh',   '1.0Pdcalc',]
    piezo_x_1 = [  -28600,    -20600,   -14000,     -2600,  13400,        27000,         39000,]
    piezo_y_1 = [   -2000,     -1500,    -1500,     -2000,  -2000,        -2000,         -2000,]
    stage_y_1 = [ 0 for n in names_1 ]

    names_2   = [ ] 
    piezo_x_2 = [ ]
    piezo_y_2 = [ ]
    stage_y_2 = [ ]

    # Combine rows
    names   = names_1   + names_2
    piezo_x = piezo_x_1 + piezo_x_2
    piezo_y = piezo_y_1 + piezo_y_2
    stage_y  = stage_y_1  + stage_y_2

    # Offsets for taking a few points per sample
    x_off = [0, 500]
    y_off = [0, 200]

    waxs_arc = [20, 0]
    user_name = "DW"

    assert len(names)    == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x)  == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_y)  == len(stage_y), f"Wrong list lenghts"

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        
        dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        det_exposure_time(t, t)

        for name, x, y, hex_y in zip(names, piezo_x, piezo_y, stage_y):

            yield from bps.mv(piezo.x, x,
                              piezo.y, y,
                              stage.y, hex_y)

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)

                    loc = f'{yy}{xx}'
                    sample_name = f'{name}{get_scan_md()}_loc{loc}'
                    sample_id(user_name=user_name, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")

                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.1, 0.1)


# RE.md['SAF_number'] = 311069

def run_swaxs_fibres_2023_1(t=1):
    """
    Take WAXS and SAXS at a few sample positions for averaging

    Specify central positions on the samples with xlocs and ylocs,
    then offsets from central positions with x_off and y_off. Run
    WAXS arc as the slowest motor.
    """

    names_1   = [ '4-pgsk-fib-1', '4-pgsk-fib-2', '4-pgsk-fib-3', '3-sk-fib-1', '3-sk-fib-2', '3-sk-fib-3', 'bkg_vcm', ]
    piezo_x_1 = [            700,           1850,           4010,        15810,        17310,        19500,     20500, ]
    piezo_y_1 = [          -1850,          -1850,          -2400,        -2400,        -2400,        -1000,     -1000, ]
    stage_y_1 = [ 0 for n in names_1 ]

    names_2   = [ '2-pgsk-flm-1', '2-pgsk-flm-2', '2-pgsk-flm-3', '1-sk-flm-1', '1-sk-flm-2', '1-sk-flm-3', ] 
    piezo_x_2 = [          29500,          30000,          28500,        43500,        44000,        45000, ]
    piezo_y_2 = [          -1000,          -2000,            500,        -2000,            0,         1000, ]
    stage_y_2 = [ 0 for n in names_2 ]

    # Combine rows
    names   = names_1   + names_2
    piezo_x = piezo_x_1 + piezo_x_2
    piezo_y = piezo_y_1 + piezo_y_2
    stage_y  = stage_y_1  + stage_y_2

    # offsets inside the main loop

    waxs_arc = [20]
    user_name = "PW"

    assert len(names)    == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x)  == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_y)  == len(stage_y), f"Wrong list lenghts"

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        
        #dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        dets = [pil1M]
        det_exposure_time(t, t)

        for name, x, y, hex_y in zip(names, piezo_x, piezo_y, stage_y):

            yield from bps.mv(piezo.x, x,
                              piezo.y, y,
                              stage.y, hex_y)
            
            if 'fib' in name:
                x_off = [0, ]
                y_off = [0, 30, 60, 90, 120]
            else:
                x_off = [0, 250, 500, 750, ]
                y_off = [0, 250, 500, 750, ]

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)

                    loc = f'{yy}{xx}'
                    sample_name = f'{name}{get_scan_md()}_loc{loc}'
                    sample_id(user_name=user_name, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")

                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def run_swaxs_textile_2023_2(t=0.5):
    """
    Take WAXS and SAXS at a few sample positions for averaging
    """

    names   = [  's01']#, 's02', 's03', 's04', 's05',  'bkg', ]
    piezo_x = [  -37900]#, 33000, 18000,  4500, -8000, -18000, ]
    piezo_y = [  3200 for n in names ]
    stage_y = [ 0 for n in names ]
    names = [ n + '-try4' for n in names]

    # offsets inside the main loop

    waxs_arc = [ 20 ]
    x_off = [ 500, 0, 500 ]
    y_off = [ 0, ]
    user_name = "PW"

    assert len(names)    == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x)  == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_y)  == len(stage_y), f"Wrong list lenghts"


    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)

        #dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        dets = [pil1M]
        det_exposure_time(t, t)

        for name, x, y, hex_y in zip(names, piezo_x, piezo_y, stage_y):

            yield from bps.mv(piezo.x, x,
                              piezo.y, y,
                              stage.y, hex_y)

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)

                    #if (
                    #     #(name == names[0])
                    #     (wa == waxs_arc[0])
                    #     and (yy == 0)
                    #     and (xx == 0)
                    #    ):
                    #
                    #    sample_id(user_name="test", sample_name="test")
                    #    yield from bp.count(dets)

                    loc = f'{yy}{xx}'
                    sample_name = f'{name}{get_scan_md()}_loc{loc}'
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    sample_id(user_name=user_name, sample_name=sample_name)
                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def run_swaxs_workaround_2023_2(t=0.5):
    """
    Take WAXS and SAXS at a few sample positions for averaging
    """

    names   = [  's01', 's02', 's03', 's04', 's05',  'bkg', ]
    piezo_x = [  44000, 33000, 18000,  4500, -8000, -18000, ]
    piezo_y = [  2000 for n in names ]
    stage_y = [ 0 for n in names ]
    names = [ n + '-attn-nobs' for n in names]

    # offsets inside the main loop

    waxs_arc = [ 20 ]
    x_off = [ -500, 0, 500 ]
    y_off = [ 0, ]
    user_name = "PW"

    assert len(names)    == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x)  == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_y)  == len(stage_y), f"Wrong list lenghts"


    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)

        #dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        dets = [pil1M]
        det_exposure_time(t, t)

        for name, x, y, hex_y in zip(names, piezo_x, piezo_y, stage_y):

            yield from bps.mv(piezo.x, x,
                              piezo.y, y,
                              stage.y, hex_y)

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)

                    loc = f'{yy}{xx}'

                    if loc != '01':
                        sample_name = 'test'
                        sample_id(user_name="test", sample_name=sample_name)

                    else:
                        sample_name = f'{name}{get_scan_md()}_loc{loc}'
                        sample_id(user_name=user_name, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

def move_energy_slowly(target_e, e_step=100):
    """
    Move energy gently using feedback
    """

    current_e = energy.position.energy
    

    if (current_e > 10000) and (target_e > 10000):

        energies = np.arange(current_e, target_e + 1, e_step)

        for e in energies:

            feedback('off')
            yield from bps.mv(energy, e)
            yield from bps.sleep(2)
            feedback('on')
            yield from bps.sleep(5)
    else:
        print('Energy change not allowed, do proper alignment')



def test_DI(t=1):
    """
    Test duplicated images
    """

    user_name = "test"

    names = ["test2", "test3"]

    det_exposure_time(t, t)

    # Energies for calcium K edge, coarse resolution
    energies_coarse = np.concatenate(
        (
            np.linspace(4030, 4045, 3),
        )
    )

    # Do not read SAXS if WAXS is in the way
    wa = waxs.arc.position
    dets = [pil900KW]

    # Change energies
    energies = energies_coarse

    # Go over samples

    for name in names:

        # Scan over energies
        for e in energies:
            yield from bps.sleep(2)

            # Metadata
            bpm = xbpm3.sumX.get()
            sdd = pil1m_pos.z.position / 1000
            wa = str(np.round(float(wa), 1)).zfill(4)

            # Detector file name
            name_fmt = "{sample}_{energy}eV_wa{wax}_sdd{sdd}m_bpm{xbpm}"
            sample_name = name_fmt.format(
                sample=name,
                energy="%6.2f" % e,
                wax=wa,
                sdd="%.1f" % sdd,
                xbpm="%4.3f" % bpm,
            )
            sample_id(user_name=user_name, sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")

            yield from bp.count(dets, num=1)

def test_example_SWAXS_2023_3(t=0.5):
    """
    Standard SWAXS scan
    """
    
    names =   [ 'AgBH-1', 'AgBH-2', 'empty', ]
    piezo_x = [   -45400,   -44400,  -19000, ] 
    piezo_y = [     3800,     4200,    4200, ]
    piezo_z = [ 14400 for n in names ]

    assert len(names)   == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x) == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_x) == len(piezo_z), f"Wrong list lenghts"

    user = 'test'
    waxs_arc = [40, 20, 0]
    det_exposure_time(t, t)

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
            
        for name, x, y, z in zip(names, piezo_x, piezo_y, piezo_z):
            yield from bps.mv(piezo.x, x,
                              piezo.y, y,
                              piezo.z, z,
            )
        
            sample_name = f'{name}{get_scan_md()}'
            sample_id(user_name=user, sample_name=sample_name)
            print(f"\n\n\n\t=== Sample: {sample_name} ===")
            yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

# DT-313930

def get_more_md(temp=25, tender=True, bpm=True):
    """
    Add temperature and XBPM3 readings into the scan metadata
    """

    more_md = f'{get_scan_md(tender=tender)}'

    if temp:
        temp = str(np.round(float(temp), 1)).zfill(5)
        more_md = f'_{temp}degC{more_md}'
    if bpm:
        xbpm = xbpm3.sumX.get()
        xbpm = str(np.round(float(xbpm), 3)).zfill(5)
        more_md = f'{more_md}_xbpm{xbpm}'

    return more_md


def take_single_temp_frame(name='test', temp=25):
    """
    After reaching T, take data
    """

    dets = [pil900KW]


    sample_name = f'{name}{get_more_md(temp)}'
    sample_id(user_name='PW', sample_name=sample_name)
    print(f"\n\n\n\t=== Sample: {sample_name} ===")
    yield from bp.count(dets)

def take_energy_temp_scan(name='test', temp=25):
    """
    After reaching T, take data
    """

    e = np.around(energy.position.energy)
    energies = np.concatenate((
        np.arange(e - 5, e - 2, 1),
        np.arange(e - 2, e + 2 + 0.5, 0.5),
        np.arange(e + 2 + 1 , e + 2 + 2 + 1, 1),
    ))

    dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]

    for nrg in energies:
        yield from bps.mv(energy, nrg)
        yield from bps.sleep(2)
        if xbpm2.sumX.get() < 50:
            yield from bps.sleep(2)
            yield from bps.mv(energy, nrg)
            yield from bps.sleep(2)

        sample_name = f'{name}-escan{get_more_md(temp=temp)}'
        sample_id(user_name='PW', sample_name=sample_name)
        print(f"\n\n\n\t=== Sample: {sample_name} ===")
        yield from bp.count(dets)

    yield from bps.mv(energy, e)
    sample_id(user_name='test', sample_name=f'test_{get_more_md()}')

def create_timestamp():
    """
    store in RE.md and print
    """
    RE.md['tstamp'] = time.time()
    print('\nTime stamp created in RE.md')
    tstamp = RE.md['tstamp']
    print(f'tstamp: {tstamp}')



def run_Linkam_temp_run(name, t=0.5, td= 4 * 60, frames=600):
    """
    Set temperature ramp in Linkam, create timestamp,
    run continous measurement, explore WAXS and SAXS

    Args:
        name (str): sample name,
        t (float): exposure time for one frame in s,
        td (float): time difference between point measurements,
        frames (int): number of franes.
    """

    try:
        tstamp = RE.md['tstamp']
    except:
        tstamp = time.time()
        RE.md['tstamp'] = tstamp
        print(f'\nTime stamp created in RE.md: {tstamp}')

    waxs_arc = [0, 20]
    det_exposure_time(t, t)
    user = 'PW'

    for spoint in range(frames):
        print(f'Frame {spoint + 1} / {frames}')
        t_frame = time.time()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            dets = [pil900KW] if waxs.arc.position < 14.9 else [pil1M, pil900KW]

            t_measurement = time.time()
            time_sname = str(np.round(t_measurement - tstamp, 0)).zfill(7)
            md = f'{get_more_md(temp=False)}'

            sample_name = f'{name}-tscan_time{time_sname}s{md}'
            sample_id(user_name=user, sample_name=sample_name)
            print(f"\n\n\n\t=== Sample: {sample_name} ===")
            yield from bp.count(dets)

        yield from bps.mv(waxs, waxs_arc[0])
        print(f'Waiting for {td}s to pass between frames')
        while (time.time() - t_frame) < td:
            yield from bps.sleep(1)

    sample_id(user_name='test', sample_name=f'test')


def run_swaxs_2024_1_slk(t=1):
    """
    Take WAXS and SAXS at several sample positions

    Specify central positions on the samples with xlocs and ylocs,
    then offsets from central positions with x_off and y_off.
    """

    names_1 = ['flm-100-0-MeOH', 'flm-90-10-MeOH', 'flm-80-20-MeOH', 'flm-70-30-MeOH', 'flm-50-50-MeOH',]           
    piezo_x_1 = [        -43200,           -37000,           -32000,           -24500,           -17500,]         
    piezo_y_1 = [          1000,              600,             1000,             1200,             1200,]

    names_2 = ['flm-30-70-MeOH', 'fbr-30-70-untr-1draw', 'fbr-30-70-untr-2draw', 'fbr-30-70-MeOH-2draw',]
    piezo_x_2 = [        -10000,                  -2860,                   2290,                   6790,] 
    piezo_y_2 = [          1200,                    600,                   1700,                   1200,]

    names   = names_1   + names_2
    piezo_x = piezo_x_1 + piezo_x_2
    piezo_y = piezo_y_1 + piezo_y_2      

    #x_off = [ 0 ]
    #y_off = [ 0 ]    
    waxs_arc = [0, 20]

    user = "PW"
    det_exposure_time(t, t)

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        dets.append(OAV_writing)

        for name, x, y in zip(names, piezo_x, piezo_y):
            yield from bps.mv(piezo.y, y,
                              piezo.x, x,
                              )
            
            if 'fbr' in name:
                x_off = [ 0 ]
                y_off = [ -200, -150, -100, -50, 0, 50, 100, 150, 200 ]
            else:
                x_off = [ -300, 0, 300 ]
                y_off = [ -300, 0, 300 ] 

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)
                    
                    loc = f'{yy}{xx}'
                    sample_name = f'{name}{get_scan_md()}_loc{loc}'
                    sample_id(user_name=user, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)

def run_swaxs_2024_1_par(t=1):
    """
    Take WAXS and SAXS at several sample positions

    Specify central positions on the samples with xlocs and ylocs,
    then offsets from central positions with x_off and y_off.
    """

    names =   [  'AgBH', 'PSTFSI-Li-10to1',]           
    piezo_x = [  -44000,            -11200, ]         
    piezo_y = [   -4000,              6400, ]
    piezo_z = [    8200,             12600, ]
    # hexa(x, y, z) =  (0, 7, 4)

    x_off = [ -600, -300, 0, 300, 600 ]
    y_off = [ -150,       0,      150 ]
    waxs_arc = [0, 20]

    user = "PW"
    det_exposure_time(t, t)

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(piezo_z), msg

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        dets.append(OAV_writing)

        for name, x, y, z in zip(names, piezo_x, piezo_y, piezo_z):
            yield from bps.mv(piezo.y, y,
                              piezo.x, x,
                              piezo.z, z,
                              )

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)
                    
                    loc = f'{xx}{yy}'
                    sample_name = f'{name}{get_scan_md()}_loc{loc}'
                    sample_id(user_name=user, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)



def get_more_md(tender=True, bpm=True):
    """
    Add temperature and XBPM2 readings into the scan metadata
    """

    more_md = f'{get_scan_md(tender=tender)}'

    if bpm:
        xbpm = xbpm2.sumX.get()
        xbpm = str(np.round(float(xbpm), 3)).zfill(5)
        more_md = f'{more_md}_xbpm{xbpm}'

    return more_md

def take_energy_scan_2024_1(t=1):
    """
    Energy scan
    """
    names =   [ 'SLi10-nexafs-3', ]           
    piezo_x = [           -31650, ]         
    piezo_y = [            -7800, ]
    piezo_z = [             7000, ]

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(piezo_z), msg

    waxs_arc = [ 60 ]

    user = "PW"
    det_exposure_time(t, t)

    energies = np.concatenate((
        np.arange(2445, 2470, 5),
        np.arange(2470, 2480, 0.5),
        np.arange(2480, 2490, 0.5),
        np.arange(2490, 2501, 5),
    ))
    
    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] # if waxs.arc.position < 15 else [pil900KW, pil1M]

        for name, x, y, z in zip(names, piezo_x, piezo_y, piezo_z):
            yield from bps.mv(piezo.y, y,
                              piezo.x, x,
                              piezo.z, z,
                              )

            for nrg in energies:
                yield from bps.mv(energy, nrg)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, nrg)
                    yield from bps.sleep(2)

                sample_name = f'{name}-escan{get_more_md()}_loc00'
                sample_id(user_name='PW', sample_name=sample_name)
                print(f"\n\n\n\t=== Sample: {sample_name} ===")
                yield from bp.count(dets)

    sample_id(user_name='test', sample_name=f'test_{get_more_md()}')


def run_swaxs_2024_1_par2(t=2):
    """
    Take WAXS and SAXS at several sample positions

    Specify central positions on the samples with xlocs and ylocs,
    then offsets from central positions with x_off and y_off.
    """

    names =   [  'mpt1.5', 'mpt1.0',  'SLi10',  'SNa10',  'MLi10',  'MNa10', 'SNa0', 'SLi0', 'MLi0',  'MNa0', 'SLi5', 'MNa5', 'SNa5', ]           
    piezo_x = [   -44100,    -37500,   -31650,   -24600,   -18000,   -12600,  -5250,    600,   6900,   13500,  20200,  25400,  32100, ]         
    piezo_y = [     6000,      6000,    -7800,    -8600,    -8400,    -8600,  -7400,   1750,  -6500,   -8900,  -7200,  -8500,   1550, ]
    piezo_z = [     9400,      6600,     7000,     5200,     5200,     5200,   5200,   7000,   5600,    5600,   5600,   5600,   5600, ]


    x_off = [ 0 ]
    y_off = [ -100, -50, 0, 50, 100, 150, 200, 250, 300]
    waxs_arc = [0, 20]

    user = "BP"
    det_exposure_time(t, t)

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(piezo_z), msg

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        #dets.append(OAV_writing)

        for name, x, y, z, in zip(names, piezo_x, piezo_y, piezo_z):
            yield from bps.mv(piezo.y, y,
                              piezo.x, x,
                              piezo.z, z,
                              )

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)
                    
                    loc = f'{xx}{yy}'
                    sample_name = f'{name}{get_scan_md()}_loc{loc}'
                    sample_id(user_name=user, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)

def run_swaxs_2024_1_par2tender(t=5):
    """
    Take WAXS and SAXS at several sample positions

    Specify central positions on the samples with xlocs and ylocs,
    then offsets from central positions with x_off and y_off.
    """

    names =   [  'mpt1.5', 'mpt1.0',  'SLi10',  'SNa10',  'MLi10',  'MNa10', 'SNa0', 'SLi0', 'MLi0',  'MNa0', 'SLi5', 'MNa5', 'SNa5', ]           
    piezo_x = [   -44200,    -37600,   -31650,   -24600,   -18000,   -12600,  -5250,    750,   7000,   13500,  20200,  25700,  32100, ]         
    piezo_y = [     6000,      6000,    -6000,    -8100,    -8300,    -8300,  -7300,   1550,  -6500,   -8900,  -7400,  -8500,   1350, ]
    piezo_z = [     9400,      6600,     7000,     5800,     5400,     5400,   5200,   5400,   5600,    5600,   5600,   5600,   5600, ]


    x_off = [ 0 ]
    y_off = [ -100, -50, 0, 50, 100, 150, 200, 250, 300]
    waxs_arc = [0, 20]

    user = "BP"
    det_exposure_time(t, t)

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(piezo_z), msg

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        #dets.append(OAV_writing)

        for name, x, y, z, in zip(names, piezo_x, piezo_y, piezo_z):
            yield from bps.mv(piezo.y, y,
                              piezo.x, x,
                              piezo.z, z,
                              )

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)
                    
                    loc = f'{xx}{yy}'
                    sample_name = f'{name}{get_more_md()}_loc{loc}'
                    sample_id(user_name=user, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)


def run_swaxs_2024_1_par2tender_energy(t=2):
    """
    Take WAXS and SAXS at several sample positions

    Specify central positions on the samples with xlocs and ylocs,
    then offsets from central positions with x_off and y_off.
    """

    names =   [  'mpt1.5', 'mpt1.0',  'SLi10',  'SNa10',  'MLi10',  'MNa10', 'SNa0', 'SLi0', 'MLi0',  'MNa0', 'SLi5', 'MNa5', 'SNa5', ]           
    piezo_x = [   -44200,    -37600,   -31650,   -24600,   -18000,   -12600,  -5250,    750,   7000,   13500,  20200,  25700,  32100, ]         
    piezo_y = [     6000,      6000,    -6000,    -8100,    -8300,    -8300,  -7300,   1550,  -6500,   -8900,  -7400,  -8500,   1350, ]
    piezo_z = [     9400,      6600,     7000,     5800,     5400,     5400,   5200,   5400,   5600,    5600,   5600,   5600,   5600, ]


    waxs_arc = [0, 20]

    energies = np.concatenate((
        np.arange(2445, 2470, 5),
        np.arange(2470, 2480, 0.25),
        np.arange(2480, 2490, 1),
        np.arange(2490, 2501, 5),
    ))

    user = "BP"
    det_exposure_time(t, t)

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(piezo_z), msg

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        #dets.append(OAV_writing)

        for name, x, y, z, in zip(names, piezo_x, piezo_y, piezo_z):
            yield from bps.mv(piezo.y, y,
                              piezo.x, x,
                              piezo.z, z,
                              )

            for nrg in energies:
                yield from bps.mv(energy, nrg)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, nrg)
                    yield from bps.sleep(2)

                loc = '00'
                sample_name = f'{name}-escan{get_more_md()}_loc{loc}'
                sample_id(user_name='PW', sample_name=sample_name)
                print(f"\n\n\n\t=== Sample: {sample_name} ===")
                yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)


def run_swaxs_2024_1_par3(t=2):
    """
    Take WAXS and SAXS at several sample positions

    Specify central positions on the samples with xlocs and ylocs,
    then offsets from central positions with x_off and y_off.
    """

    names =   [  'mpt1.5', 'mpt1.0',  'SLi10',  'SNa10',  'MLi10',  'MNa10', 'SNa0', 'SLi0', 'MLi0',  'MNa0', 'SLi5', 'MNa5', 'SNa5', ]           
    piezo_x = [   -44100,    -37500,   -31650,   -24600,   -18100,   -12700,  -5650,    600,   6900,   13300,  20200,  25800,  32900, ]         
    piezo_y = [     6000,      6000,    -8100,    -8900,    -8400,    -8800,  -7400,   1650,   7700,    3500,  -7200,  -7200,   1350, ]
    piezo_z = [     6600,      6600,     7000,     6000,     6000,     6000,   6200,   7000,   5600,    5600,   5600,   5600,   5600, ]


    x_off = [ 0 ]
    y_off = [ -100, 0, 100, 200, ]
    waxs_arc = [ 20, 0 ]

    user = "BP"
    det_exposure_time(t, t)

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(piezo_z), msg

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        #dets.append(OAV_writing)

        for name, x, y, z, in zip(names, piezo_x, piezo_y, piezo_z):
            yield from bps.mv(piezo.y, y,
                              piezo.x, x,
                              piezo.z, z,
                              )

            for yy, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x + x_of)
                    
                    loc = f'{xx}{yy}'
                    sample_name = f'{name}{get_scan_md()}_loc{loc}'
                    sample_id(user_name=user, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)