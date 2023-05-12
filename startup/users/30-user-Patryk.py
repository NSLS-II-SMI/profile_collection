def get_scan_md():
    """
    Create a string with scan metadata
    """
    # Metadata
    e = energy.position.energy / 1000
    #temp = str(np.round(float(temp_degC), 1)).zfill(5)
    wa = waxs.arc.position + 0.001
    wa = str(np.round(float(wa), 1)).zfill(4)
    sdd = pil1m_pos.z.position / 1000

    md_fmt = ("_{energy}keV_wa{wa}_sdd{sdd}m")
    
    scan_md = md_fmt.format(
        energy = "%.2f" % e ,
        wa = wa,
        sdd = "%.1f" % sdd,
    )
    return scan_md


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