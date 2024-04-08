def run_giwaxs_Fak(t=1):
    dets = [pil300KW, pil1M]
    xlocs1 = [-22000, 3000, 21500]
    names1 = ["TPD_52nm", "TPD_42nm", "TPD_32nm"]

    # what we run now
    curr_tray = xlocs1
    curr_names = names1
    assert len(curr_tray) == len(
        curr_names
    ), f"Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})"
    waxs_range = [0, 13, 3]
    for x, name in zip(curr_tray, curr_names):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.th, 0.1)
        yield from alignement_gisaxs(0.1)
        plt.close("all")
        angle_offset = [0.1]
        a_off = piezo.th.position
        det_exposure_time(t, t)
        name_fmt = "{sample}_{angle}deg"
        for j, ang in enumerate(a_off + np.array(angle_offset)):
            yield from bps.mv(piezo.x, (x + j * 500))
            real_ang = angle_offset[j]
            yield from bps.mv(piezo.th, ang)
            sample_name = name_fmt.format(sample=name, angle=float("%.3f" % real_ang))
            sample_id(user_name="YJ", sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.scan(dets, waxs, *waxs_range)

        sample_id(user_name="test", sample_name="test")
        det_exposure_time(0.5, 0.5)


def gFak1(meas_t=1):
    username = "AZ"
    names1 = "aaA_20190926_OG_hot"

    dets = [pil1M, pil300KW, rayonix]
    angle_offset = [0.1]
    length = 17000
    x_edge = 31000  # make sure to define the edge as a top border of the sample on the camera using SmarAct X
    x_step = 4000
    nb_pt = (length - 500) // x_step
    xlocs1 = []
    for step in range(0, nb_pt + 1, 1):
        xlocs1 += [np.round(x_edge - step * x_step)]

    # what we run now
    curr_tray = xlocs1
    waxs_range = [0, 13, 3]

    yield from bps.mv(piezo.x, x_edge)
    yield from bps.mv(piezo.th, 0.1)
    yield from alignement_gisaxs(0.1)
    a_off = piezo.th.position
    plt.close("all")
    for i, x in enumerate(curr_tray):
        yield from bps.mv(piezo.x, x)
        if i != 0:
            yield from bps.mv(piezo.th, a_off + angle_offset[0])
            yield from quickalign_gisaxs(0.1)
            plt.close("all")
            a_off = piezo.th.position
        for ii, an in enumerate(angle_offset):
            yield from bps.mv(piezo.th, a_off + an)
            det_exposure_time(meas_t, meas_t)
            # temper = ls.ch1_read.value
            name_fmt = "{sample}_x{xlocation}_{angl}deg"
            sample_name = name_fmt.format(sample=names1, xlocation=x, angl=an)
            sample_id(user_name=username, sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.scan(dets, waxs, *waxs_range)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)


def gFak2(meas_t=1):
    username = "YJ"
    names1 = "aaA_20190926_OG_middle"

    dets = [pil1M, pil300KW, rayonix]
    angle_offset = [0.1]
    length = 21000
    x_edge = 11000  # make sure to define the edge as a top border of the sample on the camera using SmarAct X
    x_step = 4000
    nb_pt = (length - 500) // x_step
    xlocs1 = []
    for step in range(0, nb_pt + 1, 1):
        xlocs1 += [np.round(x_edge - step * x_step)]

    # what we run now
    curr_tray = xlocs1
    waxs_range = [0, 13, 3]

    yield from bps.mv(piezo.x, x_edge)
    yield from bps.mv(piezo.th, 0.1)
    yield from alignement_gisaxs(0.1)
    a_off = piezo.th.position
    plt.close("all")
    for i, x in enumerate(curr_tray):
        yield from bps.mv(piezo.x, x)
        if i != 0:
            yield from bps.mv(piezo.th, a_off + angle_offset[0])
            yield from quickalign_gisaxs(0.1)
            plt.close("all")
            a_off = piezo.th.position
        for ii, an in enumerate(angle_offset):
            yield from bps.mv(piezo.th, a_off + an)
            det_exposure_time(meas_t, meas_t)
            # temper = ls.ch1_read.value
            name_fmt = "{sample}_x{xlocation}_{angl}deg"
            sample_name = name_fmt.format(sample=names1, xlocation=x, angl=an)
            sample_id(user_name=username, sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.scan(dets, waxs, *waxs_range)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)


def gFak3(meas_t=1):
    username = "AZ"
    names1 = "aaA_20190926_OG_cold"

    dets = [pil1M, pil300KW, rayonix]
    angle_offset = [0.1]
    length = 17000
    x_edge = (
        -14000
    )  # make sure to define the edge as a top border of the sample on the camera using SmarAct X
    x_step = 4000
    nb_pt = (length - 500) // x_step
    xlocs1 = []
    for step in range(0, nb_pt + 1, 1):
        xlocs1 += [np.round(x_edge - step * x_step)]

    # what we run now
    curr_tray = xlocs1
    waxs_range = [0, 13, 3]

    yield from bps.mv(piezo.x, x_edge)
    yield from bps.mv(piezo.th, 0.1)
    yield from alignement_gisaxs(0.1)
    a_off = piezo.th.position
    plt.close("all")
    for i, x in enumerate(curr_tray):
        yield from bps.mv(piezo.x, x)
        if i != 0:
            yield from bps.mv(piezo.th, a_off + angle_offset[0])
            yield from quickalign_gisaxs(0.1)
            plt.close("all")
            a_off = piezo.th.position
        for ii, an in enumerate(angle_offset):
            yield from bps.mv(piezo.th, a_off + an)
            det_exposure_time(meas_t, meas_t)
            # temper = ls.ch1_read.value
            name_fmt = "{sample}_x{xlocation}_{angl}deg"
            sample_name = name_fmt.format(sample=names1, xlocation=x, angl=an)
            sample_id(user_name=username, sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            yield from bp.scan(dets, waxs, *waxs_range)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)


def run_all_gFak():
    yield from gFak1()
    yield from gFak2()
    yield from gFak3()


###################
### 2022_02 Luo ###
###################


def grazing_Luo_2022_2(t=0.5, incident_angle=0.1):
    """
    Scan substrates on the bar

    309557 Luo
    Overlaping essential to cover the detector gaps

    SmarAct nanopositioner units: micrometers
    Hexapod stage units: milimeters
    Incident angle (piezo.th): degrees

    Params:
        t (float): exposure time,
        incident_angle (float): self explained
    """
    user_name = "PL"

    # Samples

    skip = 0

    names = ["81nm_aaA27C_0p2As_2022-05-17"]
    piezo_xs = [50600]
    hexa_xs = [0]
    angles = [0, 2, 18, 20]  # degrees
    step_across_sample = 200  # microns

    assert len(names) == len(
        piezo_xs
    ), f"Number of X coordinates ({len(piezo_xs)}) is different from number of samples ({len(names)})"
    assert len(hexa_xs) == len(
        names
    ), f"Number of X hexapod coordinates ({len(hexa_xs)}) is different from number of samples ({len(names)})"

    for name, piezo_x, hexa_x in zip(names[skip:], piezo_xs[skip:], hexa_xs[skip:]):

        # Move motors to locate the sample
        yield from bps.mv(piezo.x, piezo_x, stage.x, hexa_x)
        # Align the sample
        try:
            yield from alignement_gisaxs()
        except:
            yield from alignement_gisaxs(0.4)

        # Go to incident
        yield from bps.mvr(piezo.th, incident_angle)

        det_exposure_time(t, t)

        # Scan sample across angles
        for i, wa in enumerate(angles):
            yield from bps.mv(waxs, wa)
            dets = [pil900KW] if wa < 15 else [pil900KW, pil1M]
            yield from bps.mvr(piezo.x, (i + 1) * step_across_sample)

            # Metadata
            name_fmt = "{sample}_{energy}keV_{sdd}m_wa{wax}_ai{ai}_bpm{xbpm}"
            bpm = xbpm2.sumX.get()
            e = energy.energy.position / 1000
            sdd = pil1m_pos.z.position / 1000

            sample_name = name_fmt.format(
                sample=name,
                energy="%.1f" % e,
                sdd="%.0f" % sdd,
                wax=wa,
                ai="%.1f" % incident_angle,
                xbpm="%4.3f" % bpm,
            )
            sample_id(user_name=user_name, sample_name=sample_name)
            print(f"\n\t=== Sample: {sample_name} ===\n")
            # Take data
            yield from bp.count(dets, num=1)

            sample_id(user_name="test", sample_name="test")


def grazing_gradient_Luo_2022_2(t=0.5, incident_angle=0.1):
    """
    Scan gradient sample

    309557 Luo
    Overlaping WAXS essential to cover the detector gaps, no offset in x.

    SmarAct nanopositioner units: micrometers
    Hexapod stage units: milimeters
    Incident angle (piezo.th): degrees

    Params:
        t (float): exposure time,
        incident_angle (float): self explained
    """
    user_name = "PL"
    angles = [0, 2, 18, 20]  # degrees
    step_across_gradient = 2  # mm

    # Sample parameters
    names = ["60nm_TPD_0p2As_-63Cto67C_2022-05-05"]
    sample_edges = [[34700, -32200]]
    sample_margins = [[0, 0]]

    assert len(names) == len(
        sample_edges
    ), f"Number of samples ({len(names)}) is different from number of edges ({len(sample_edges)})"
    assert len(names) == len(
        sample_margins
    ), f"Number of samples ({len(names)}) is different from number of margins ({len(sample_margins)})"

    # Make sure beam is on
    # yield from bps.mv(GV7.open_cmd, 1)
    yield from shopen()
    yield from bps.sleep(3)

    yield from bps.mv(piezo.z, 300)

    for name, edges, margins in zip(names, sample_edges, sample_margins):

        # Check sample name just in case
        name = name.translate({ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+"})

        start_piezo_x = edges[0] - margins[0]
        end_piezo_x = edges[1] + margins[1]
        length = start_piezo_x - end_piezo_x

        positions = [
            1 + i * step_across_gradient for i in range(100) if i * 2 < length / 1000
        ]

        for i, position in enumerate(positions):
            # print('Position {} / {}'.format(i + 1), len(positions))

            new_piezo_x = start_piezo_x - 1000 * position
            yield from bps.mv(piezo.x, new_piezo_x + 200)

            # Full alignment / quick wasn't working well
            try:
                yield from alignement_gisaxs()
            except:
                yield from alignement_gisaxs(0.4)
            yield from bps.mvr(piezo.th, incident_angle)

            yield from bps.mv(piezo.x, new_piezo_x)

            for wa in angles:
                yield from bps.mv(waxs, wa)
                dets = [pil900KW] if wa < 15 else [pil900KW, pil1M]

                # Metadata
                name_fmt = (
                    "{sample}_{energy}keV_{sdd}m_wa{wax}_ai{ai}_pos_{pos}mm_bpm{xbpm}"
                )
                bpm = xbpm2.sumX.get()
                e = energy.energy.position / 1000
                sdd = pil1m_pos.z.position / 1000

                sample_name = name_fmt.format(
                    sample=name,
                    energy="%.1f" % e,
                    sdd="%.0f" % sdd,
                    wax=wa,
                    ai="%.1f" % incident_angle,
                    pos="%.1f" % position,
                    xbpm="%4.3f" % bpm,
                )
                sample_id(user_name=user_name, sample_name=sample_name)

                # Take data
                yield from bp.count(dets, num=1)
                sample_id(user_name="test", sample_name="test")

def atten_move_in(x4=True, x2=True):
    """
    Move 4x + 2x Sn 60 um attenuators in
    """
    print('Moving attenuators in')

    if x4:
        while att1_7.status.get() != 'Open':
            yield from bps.mv(att1_7.open_cmd, 1)
            yield from bps.sleep(1)
    if x2:
        while att1_6.status.get() != 'Open':
            yield from bps.mv(att1_6.open_cmd, 1)
            yield from bps.sleep(1)

def atten_move_out():
    """
    Move 4x + 2x Sn 60 um attenuators out
    """
    print('Moving attenuators out')
    while att1_7.status.get() != 'Not Open':
        yield from bps.mv(att1_7.close_cmd, 1)
        yield from bps.sleep(1)
    while att1_6.status.get() != 'Not Open':
        yield from bps.mv(att1_6.close_cmd, 1)
        yield from bps.sleep(1)

def engage_detectors():
    """
    Making sure camserver responds and data is taken
    """

    yield from atten_move_in()
    sample_id(user_name='test', sample_name='test')
    print(f"\n\n\n\t=== Making sure detectores are engaged and ready ===")
    yield from bp.count([pil900KW, pil1M])
    yield from atten_move_out()


def grazing_Kritika_2023_3(t=0.5):
    """
    standard GI-S/WAXS
    """
    #names   = [   's01',  's02',  's03',  's04',  's05',  's06',  's07',  's08',  's09',  's10',  's11',  's12',  's13',  's14',  's15', ]
    #piezo_x = [ -56000,  -46500, -39000, -40500, -30000, -19500,  -9500,  -1000,  14000,  22000,  32000,  42000,  51500,  51000,  55500, ]
    #piezo_y = [   4800,    4800,   4800,   4600,   4500,   4500,   4300,   4300,   4200,   4200,   4200,   4100,   3900,   3800,   3800  ]          
    #piezo_z = [   5000,    5000,   5000,   5000,   5000,   5000,   4000,   4000,   4000,   4000,   4000,   3500,   3500,   3500,   3500, ]
    #hexa_x =  [    -14,     -14,    -14,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,   10,       13, ]

    names   = [   's03',  's04',  's09',  's10', ]
    piezo_x = [ -33000,  -23000,  39000,  51000, ]
    piezo_y = [   4600,    4400,   4000,   4000, ]          
    piezo_z = [   5000,    5000,   3500,   3500, ]
    hexa_x =  [      0,       0,      0,      0, ]
    
    
    names = [ n + '-rot90'+ '-inair' + '-2023Oct30' for n in names ]
    #piezo_x = np.asarray(piezo_x) + 1000


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

    waxs_arc = [ 0, 2, 20, 22 ]  # degrees
    x_off = [-500, 0, 500 ]
    incident_angles = [ 0.1 ]
    user_name = 'KJ'

    det_exposure_time(t, t)

    # Make sure cam server engages with the detector
    #yield from engage_detectors()
 
    for name, x, y, z, hx in zip(names, piezo_x, piezo_y, piezo_z, hexa_x):

        yield from bps.mv(piezo.x, x,
                          piezo.y, y,
                          piezo.z, z,
                          stage.x, hx)

        # Align the sample
        try:
            yield from alignement_gisaxs(0.1) #0.1 to 0.15
        except:
            yield from alignement_gisaxs(0.01)

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

                    sample_name = f'{name}{get_scan_md()}_loc{xx}_ai{ai}'

                    sample_id(user_name=user_name, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

        yield from bps.mv(piezo.th, ai0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)


def grazing_Kritika_2024_1(t=0.5):
    """
    standard GI-S/WAXS
    """
    
    names   = [   's03a', 's03b', 's05a', 's05b',  's10a',  's10b',  's14a',   's14b', ]
    piezo_x = [  -27000,  -26000, -14000, -13000,   -1000,       0,   14000,    15000, ]
    piezo_y = [    2100,    2100,   2200,   2250,    2400,    2400,    2400,     2400, ]          
    piezo_z = [    4000,    4000,   4000,   4000,    4600,    4600,    4600,     4600, ]
    hexa_x =  [ 0 for n in names ]
    
    
    names = [ n + '-rot90alonglonger' for n in names]
    #piezo_x = np.asarray(piezo_x) + 1000


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

    waxs_arc = [ 0, 2, 20, 22 ]  # degrees
    x_off = [0]
    incident_angles = [ 0.1 ]
    user_name = 'KJ'

    det_exposure_time(t, t)

    # Make sure cam server engages with the detector
    #yield from engage_detectors()
 
    for name, x, y, z, hx in zip(names, piezo_x, piezo_y, piezo_z, hexa_x):

        yield from bps.mv(piezo.x, x,
                          piezo.y, y,
                          piezo.z, z,
                          stage.x, hx)

        # Align the sample
        try:
            yield from alignement_gisaxs(0.1) #0.1 to 0.15
        except:
            yield from alignement_gisaxs(0.01)

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

                    sample_name = f'{name}{get_scan_md()}_loc{xx}_ai{ai}'

                    sample_id(user_name=user_name, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)

        yield from bps.mv(piezo.th, ai0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)