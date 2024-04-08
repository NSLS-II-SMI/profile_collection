def get_positions():
    """
    Create a string with scan metadata
    """
    
    # Metadata
    x = piezo.x.position
    y = piezo.y.position
    z = piezo.z.position
    th = piezo.th.position
    
    x = str(np.round(float(x), 0)).zfill(5)
    y = str(np.round(float(y), 0)).zfill(5)
    z = str(np.round(float(z), 0)).zfill(5)
    th = str(np.round(float(th), 4)).zfill(0)
   
    return f'x={x}_y={y}_z={z}_th={th}'


def name_sample(name, tstamp):
    """
    Create sample name with metadata

    Args:
        name (str): sample name
        tstamp (time): referenced start time created separately as
            tstamp = time.time()
    """

    eplased = time.time() - tstamp
    sample_name = f'{name}{get_scan_md()}_t{eplased:.1f}_{get_positions()}'
    sample_id(user_name='YCK', sample_name=sample_name)
    print(sample_name)

def take_data_manually(name, t=2):
    """
    """
    try:
        tstamp = RE.md['tstamp']
    except:
        tstamp = time.time()
        RE.md['tstamp'] = tstamp
    name_sample(name, tstamp)

    det_exposure_time(t, t)
    yield from bp.count([pil900KW])


def create_timestamp():
    """
    store in RE.md and print
    """
    RE.md['tstamp'] = time.time()
    print('\nTime stamp created in RE.md')
    tstamp = RE.md['tstamp']
    print(f'tstamp: {tstamp}')


def continous_run(sname='test', t=2, wait=8, frames=2160):
    """
    Take data continously
    
    Create timestamp in BlueSky before running this function as
    create_timestamp()

    Args:
        sname (str): basic sample name,
        t (float): camera exposure time is seconds,
        wait (float): delay between frames,
        frames(int): number of frames to take
    """
    try:
        tstamp = RE.md['tstamp']
    except:
        tstamp = time.time()
        RE.md['tstamp'] = tstamp
    
    det_exposure_time(t, t)

    for i in range(frames):

        print(f'Taking {i + 1} / {frames} frames')

        # update sample name
        name_sample(sname, tstamp)

        # take one fram
        yield from bp.count([pil900KW])

        # wait
        print(f'\nWaiting {wait} s')
        yield from bps.sleep(wait)

def manual_th_scan(name, t=2, angles=[0.05, 0.10, 0.15, 0.20, 0.25, 0.30], loc=None):
    """
    Take data manually over a few theta angles
    and come back to 0.1 deg incident angle
    
    """
    det_exposure_time(t, t)
    
    try:
        tstamp = RE.md['tstamp']
    except:
        tstamp = time.time()
        RE.md['tstamp'] = tstamp

    try:
        th0 = RE.md['th0']
    except:
        th0 = -1.30-0.1 # as measured
        RE.md['th0'] = th0

    for ai in angles:
        yield from bps.mv(piezo.th, th0 + ai)

        name_sample(name, tstamp)
        sname = RE.md['sample_name']
        RE.md['sample_name'] += f'ai={ai}'
        if loc is not None:
            RE.md['sample_name'] += f'_loc{loc}'
        yield from bp.count([pil900KW])
        RE.md['sample_name'] = sname

    yield from bps.mv(piezo.th, th0 + 0.1)


def run_x_th_scan(name, t):
    """
    """

    x = piezo.x.position

    x_table = [-100, -50, 0, 50, 100]

    for x_step in x_table:
        yield from bps.mv(piezo.x, x + x_step)

        yield from manual_th_scan(name, t)
    
    yield from bps.mv(piezo.x, x)


def run_swaxs_KCW_2023_3(t=2):
    """
    Hard X-ray WAXS and SAXS
    """

    names =   [ 'calib-kapton', 'calib-celgart-rot0', 'calib-glass-fibre', 'calib-cu-foil', 'calib-celgard-rot90'] 
    piezo_x = [   -15000, -6700, 2300, 12300, 22300 ]   
    piezo_y = [    -4000, -4000, -4000, -4000, -5700 ]          
    piezo_z = [ 3000 for n in names ]
    hexa_x =  [ 0 for n in names]

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(piezo_z), msg
    assert len(piezo_x) == len(hexa_x), msg

    user_name = "KCW"
    waxs_arc = [0, 20]

    det_exposure_time(t, t)

    # Make sure cam server engages with the detector
    yield from engage_detectors()

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)

        dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]

        for name, x, y, z, hx in zip(names, piezo_x, piezo_y, piezo_z, hexa_x):
            yield from bps.mv(piezo.x, x,
                              piezo.y, y,
                              piezo.z, z,
                              stage.x, hx)

            # Take normal scans
            sample_name = f'{name}{get_scan_md()}'
            sample_id(user_name=user_name, sample_name=sample_name)
            print(f"\n\n\n\t=== Sample: {sample_name} ===")
            yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def loop_scans_across_y(sname=f'20231106_opexp_NaCu_a', t=2, wait=1, frames=1):
    """
    Sample alignment
    """

    piezo_x = np.round(piezo.x.position, 2)
    piezo_y = np.round(piezo.y.position, 2)

    x_off = [-100, 0, 100, 250]
    y_off = np.linspace(-20, 20, 41)

    for x in x_off:
        yield from bps.mv(piezo.x, piezo_x + x)

        for y in y_off:
            yield from bps.mv(piezo.y, piezo_y + y)

            yield from continous_run(sname=sname, t=t, wait=wait, frames=frames)

    yield from bps.mv(piezo.x, piezo_x,
                      piezo.y, piezo_y,)

def loop_overnight_scans_(sname=f'20231106_opexp_NaCu_a', t=2, wait=1, frames=1):
    """
    Overnight x vs y vs theta
    move to nominal pozition manually after the scan
    """

    piezo_x = [  12450,  12550,  12650, ]
    piezo_y = [ -1225, -1225, -1225, ]

    y_off = [-2, 0, 2]

    for frame in range(frames):
        print(f'Taking {frame + 1} / {frames} frames')

        for i, (x, y) in enumerate(zip(piezo_x, piezo_y)):
            yield from bps.mv(piezo.x, x,
                              piezo.y, y)

            for j, y_of in enumerate(y_off):
                yield from bps.mv(piezo.y, y + y_of)

                loc = f'{i}{j}'
                yield from manual_th_scan(sname, t=2, angles=[0.05, 0.10, 0.15], loc=loc)

def grazing_Chen_Wiegart_2023_3(t=0.5):
    """
    standard GI-S/WAXS
    """
    #[ 'G1-01-x2.083']
    #[ -52417 ] 
    #[   6775 ]  
    #[   9800 ] 
    #[    -13 ] 
    # names   =  [  'G1-01-x7.083',  'G1-01-x8.750',  'G1-01-x9.167', 'G1-01-x10.000', 'G1-01-x25.000', 'G3-01-x25.000', 'G3-01-x10.000', 'G3-01-x7.083', 'G3-01-x2.083', 'G4-01-x2.083', 'G4-01-x7.083', 'G4-01-x25.000']
    # piezo_x =  [    -47417,          -45750,          -45333,         -44500,          -29500,          7300,             22292,          25211,          30215,           17985,          22989,          40900]
    # piezo_y =  [    6775,              6775,           6775,           6775,           6775,            6775,             5815,           5815,           5815,            5615,           5615,           5415]          
    # piezo_z =  [    9800,              9800,           9800,           9800,           9200,            6600,             5600,           5600,           5600,            5400,           5400,           4200]
    # hexa_x =   [     -13,               -13,            -13,            -13,            -13,            -13,              -13,            -13,            -13,             12,             12,             12]
    # names   =  [  'b44-01_VTiCu_Pristine',  'b44-02_VTiCu_750C30M',  'b45-01_NbAlCu_Pristine', 'b45-02_NbAlCu_500C30M', 'b46-01_MoTiCu_Pristine', 'b46-02_MoTiCu_750C30M', 'b47-01_NbAlSc_Pristine', 'b47-02_NbAlSc_900C30M']
    # piezo_x =  [  -53100,                   -41100,                  -29100,                   -17100,                  -3100,                    8900,                    20900,                    34900                  ]
    # piezo_y =  [    6984,                     6984,                    6784,                     6684,                   6584,                    6484,                     6484,                    6284                   ]          
    # piezo_z =  [    8800,                     7800,                    7300,                     6800,                   6800,                    6300,                     6300,                    4800                   ]
    # hexa_x =   [     -13,                      -13,                     -13,                      -13,                    -13,                     -13,                      -13,                    -13                    ]
    names   =  [  'Cufoil_reflection']
    piezo_x =  [  1900]
    piezo_y =  [  7856]          
    piezo_z =  [  6800]
    hexa_x =   [   -13]


    i = 0
    names   = names[i:]
    piezo_x = piezo_x[i:]
    piezo_y = piezo_y[i:]
    piezo_z = piezo_z[i:]
    hexa_x =  hexa_x[i:]

    msg = "Wrong number of coordinates"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(piezo_z), msg
    assert len(piezo_x) == len(hexa_x), msg

    waxs_arc = [ 0, 20, ]  # degrees
    x_off = [ 0 ]
    incident_angles = [ 0.10, 0.15, 0.20, 0.25, 0.30, 0.50]
    user_name = 'YCW'

    det_exposure_time(t, t)

    # Make sure cam server engages with the detector
    #yield from engage_detectors()
 
    for name, x, y, z, hx in zip(names, piezo_x, piezo_y, piezo_z, hexa_x):

        #yield from bps.mv(piezo.x, x,
        #                  piezo.y, y,
        #                  piezo.z, z,
        #                  stage.x, hx)

        # Align the sample
        #yield from alignement_gisaxs(0.1) #0.1 to 0.15


        # Sample flat at ai0
        ai0 = piezo.th.position

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]

            # problems with the beamstop
            yield from bps.mv(waxs.bs_y, -3)

            for xx, x_of in enumerate(x_off):
                yield from bps.mv(piezo.x, x + x_of)
            
                for ai in incident_angles:
                    yield from bps.mv(piezo.th, ai0 + ai)

                    sample_name = f'{name}{get_scan_md()}_ai{ai}'

                    sample_id(user_name=user_name, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

        yield from bps.mv(piezo.th, ai0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)

def alignment_on():
    """
    Alignment mode on
    """
    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique="gisaxs")
    yield from smi.setDirectBeamROI(size=[48, 20])
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)
    print('\t\tALIGNMENT MODE ON')

def alignment_off():
    """
    Alignment mode off
    """
    print('\t\tALIGNMENT MODE OFF and WAXS arc to 0 deg')
    smi = SMI_Beamline()
    yield from smi.modeMeasurement()
    yield from bps.mv(waxs, 0)

def continous_run_change_xpos(sname='test', t=2, wait=8, frames=5000, x_off=[-50, 0, 50]):
    """
    Take data continously
    
    Create timestamp in BlueSky before running this function as
    create_timestamp()

    Args:
        sname (str): basic sample name,
        t (float): camera exposure time is seconds,
        wait (float): delay between frames,
        frames(int): number of frames to take,
        x_off (list of floats): relative x positions to take data at.
    """
    try:
        tstamp = RE.md['tstamp']
    except:
        tstamp = time.time()
        RE.md['tstamp'] = tstamp
    
    det_exposure_time(t, t)

    for i in range(frames):

        print(f'Taking {i + 1} / {frames} frames for {len(x_off)} x positions')

        x_0 = piezo.x.position

        for x_step in x_off:
            yield from bps.mv(piezo.x, x_0 + x_step)
            # update sample name
            name_sample(sname, tstamp)

            # take one frame
            yield from bp.count([pil900KW])
        
        yield from bps.mv(piezo.x, x_0)

        # don't wait
        #print(f'\nWaiting {wait} s')
        #yield from bps.sleep(wait)

def take_data_across_x(sname='20240326_op_Na_Cu_bar_a', t=2, x_off=[-300, -200, 100, 0, 100, 200, 300]):

    try:
        tstamp = RE.md['tstamp']
    except:
        tstamp = time.time()
        RE.md['tstamp'] = tstamp

    x_0 = piezo.x.position

    for x_step in x_off:
        yield from bps.mv(piezo.x, x_0 + x_step)
        # update sample name
        name_sample(sname, tstamp)

        # take one frame
        yield from bp.count([pil900KW])
    
    yield from bps.mv(piezo.x, x_0)
