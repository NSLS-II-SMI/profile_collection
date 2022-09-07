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
