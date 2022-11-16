from ophyd import Signal
import stat, os


# ToDo: Improve the way of reading motor name from a cycler
# ToDo: make sure that the ophyd signal can be give as an input to the cycler. If so, remove the 2 lines of definition of sample name later
# ToDo: make sure that the sample_name ophyd Signal is defined somewhere when loading the profile collection
def scan(
    dets=[pil300KW, pil1M],
    trajectory="None",
    measurement_time=1,
    number_images=1,
    user_name="GF",
    plan_name="gisaxs_scan",
    md=None,
):
    """
    Read a trajectory of motors and acquire data at the each position of the trajectory. Data will be save as a databroker document.
    :param dets: list of SMI detector which will acquire data: pil300KW, pil1M, rayonix
    :param trajectory: a cycle trjactory of motor and ophyd signal
    :param measurement_time: (integer) exposure time for 1 image
    :param number_images: (integer) number of images
    :param user_name: (string) user name
    :param plan_name: (string) plan name that will be used for the analysis
    :param md: extra metadata if needed
    """

    # Pull out the motor names from a cycler
    motor_names = []
    for trajs in trajectory:
        for traj in trajs.items():
            if traj[0].name not in motor_names:
                motor_names.append(traj[0].name)

    # Check if what is planned is doable
    try:
        motor_names
        [det for det in dets]
    except:
        raise Exception("Motors or detectors not known")

    # Fixed values. If this values change over a scan, possibility to transform in ophyd signal and record over a scan
    geometry = (
        "reflection"
        if "gisaxs" in plan_name or "giwaxs" in plan_name
        else "transmission"
    )
    base_md = {
        "plan_name": plan_name,
        "geometry": geometry,
        "detectors": [det.name for det in dets],
        "user_name": user_name,
        "motor_scanned": motor_names,
        "exposure_time": measurement_time,
        "number_image": number_images,
    }

    base_md.update(md or {})

    all_detectors = dets  # Start a list off all the detector to trigger
    all_detectors.append(xbpm2)  # add all the values to track  for analysis
    all_detectors.append(xbpm3)  # add all the values to track  for analysis
    all_detectors.append(ring.current)  # add all the values to track  for analysis

    sd.baseline = []  # Initializatin of the baseline
    SMI.update_md()  # update metadata from the beamline

    # Update metadata for the detectors
    if "pil300KW" in [det.name for det in dets]:
        all_detectors.append(waxs)  # Record the position of the WAXS arc and beamstop
        sd.baseline.append(
            smi_waxs_detector
        )  # Load metadata of WAXS detector in the baseline

    if "pil1M" in [det.name for det in dets]:
        SMI_SAXS_Det()  # Update metadata from the beamline
        sd.baseline.append(
            smi_saxs_detector
        )  # Load metadata of SAXS detector in the baseline

    if "rayonix" in [det.name for det in dets]:
        print("no metadata for the rayonix yet")

    # Update metadata for motors not used in baseline and add the motor as detector if so
    all_detectors.append(piezo) if "piezo" in motor_names else sd.baseline.append(piezo)
    all_detectors.append(stage) if "stage" in motor_names else sd.baseline.append(stage)
    all_detectors.append(prs) if "prs" in motor_names else sd.baseline.append(prs)
    all_detectors.append(energy) if "energy" in motor_names else sd.baseline.append(
        energy
    )
    all_detectors.append(waxs) if "waxs" in motor_names else sd.baseline.append(waxs)
    all_detectors.append(ls) if "ls" in motor_names else sd.baseline.append(ls)

    # That is not needed because sample name should be in the motor list
    sample_na = Signal(name="sample_name", value="test")
    all_detectors.append(sample_na)

    # Set exposure time
    det_exposure_time(measurement_time, number_images * measurement_time)

    bec.disable_plots()
    yield from bp.scan_nd(all_detectors, trajectory, md=base_md)
    bec.enable_plots()

    print("Scan with metadata done")


def scan_gi_1motor_waxsscan(
    dets=[pil300KW, pil1M],
    sam_name=["test"],
    motor="energy",
    motor_range=[16000, 16100, 16200],
    waxs_arc=[0, 13, 3],
    t=1,
    user_name="IC",
    reali=False,
    alphai=0.15,
):
    det_exposure_time(t, t)

    if motor is "energy":
        name_fmt = "{sample}_ai{ai}deg_{motor}eV"
        mot_name = energy
    elif motor is "x":
        name_fmt = "{sample}_ai{ai}deg_x{motor}"
        mot_name = piezo.x
    elif motor is "y":
        name_fmt = "{sample}_ai{ai}deg_y{motor}"
        mot_name = piezo.y
    elif motor is "th":
        name_fmt = "{sample}_ai{motor}deg"
        mot_name = piezo.th
    else:
        raise Exception("unknown motor")

    if len(sam_name) == 1:
        sam_name = sam_name * len(motor_range)
    elif len(sam_name) != len(motor_range):
        raise Exception(
            "Sample name length different from the number of motor positions"
        )

    for i, (mot_pos, sam_nam) in enumerate(zip(motor_range, sam_name)):
        yield from bps.mv(mot_name, mot_pos)

        if i == 0 or reali:
            alignement_gisaxs(angle=alphai)
            if motor is "th":
                yield from bps.mvr(piezo.th, mot_pos)
                sample_name = name_fmt.format(sample=sam_nam, motor=mot_pos)
            else:
                yield from bps.mvr(piezo.th, alphai)
                sample_name = name_fmt.format(sample=sam_nam, ai=alphai, motor=mot_pos)

        sample_id(user_name=user_name, sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.scan(dets, waxs, *waxs_arc)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def scan_trans_1motor_waxsscan(
    dets=[pil300KW, pil1M],
    sam_name=["test"],
    motor="energy",
    motor_range=[16000, 16100, 16200],
    waxs_arc=[0, 13, 3],
    t=1,
    user_name="IC",
):
    det_exposure_time(t, t)

    if motor is "energy":
        name_fmt = "{sample}_{motor}eV"
        mot_name = energy
    elif motor is "x":
        name_fmt = "{sample}_x{motor}"
        mot_name = piezo.x
    elif motor is "y":
        name_fmt = "{sample}_y{motor}"
        mot_name = piezo.y
    else:
        raise Exception("unknown motor")

    if len(sam_name) == 1:
        sam_name = sam_name * len(motor_range)
    elif len(sam_name) != len(motor_range):
        raise Exception(
            "Sample name length different from the number of motor positions"
        )

    for mot_pos, sam_nam in zip(motor_range, sam_name):
        yield from bps.mv(mot_name, mot_pos)
        sample_name = name_fmt.format(sample=sam_nam, motor=mot_pos)
        sample_id(user_name=user_name, sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.scan(dets, waxs, *waxs_arc)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def scan_trans_1motor(
    dets=[pil300KW, pil1M],
    sam_name="test",
    motor="energy",
    motor_range=[16000, 16100, 16200],
    t=1,
    user_name="IC",
    num=1,
):
    det_exposure_time(t, t)

    if motor is "energy":
        name_fmt = "{sample}_{motor}eV"
        mot_name = energy
    elif motor is "x":
        name_fmt = "{sample}_x{motor}"
        mot_name = piezo.x
    elif motor is "y":
        name_fmt = "{sample}_y{motor}"
        mot_name = piezo.y
    else:
        raise Exception("unknown motor")

    if len(sam_name) == 1:
        sam_name = sam_name * len(motor_range)
    elif len(sam_name) != len(motor_range):
        raise Exception(
            "Sample name length different from the number of motor positions"
        )

    for mot_pos, sam_nam in zip(motor_range, sam_name):
        yield from bps.mv(mot_name, mot_pos)
        sample_name = name_fmt.format(sample=sam_nam, motor=mot_pos)
        sample_id(user_name=user_name, sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        yield from bp.count(dets, num=num)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


from bluesky.utils import short_uid
import bluesky.plan_stubs as bps
import bluesky.preprocessors as bpp

def rocking_scan(det, motor, cycle=1, cycle_t=10, phi=-0.6, half_delta=30, md=None):
    md = dict(md) if md is not None else {}
    md.update({'cycles': cycle, 'cycle_t': cycle_t, 'phi': phi, 'half_delta': half_delta})

    start = phi - half_delta
    stop = phi + half_delta

    @bpp.stage_decorator([det])
    @bpp.run_decorator(md=md)
    def inner():
        # name of the group we should wait for
        group=short_uid('reading')
        # trigger the detector
        st = yield from bps.trigger(det, group=group)
        # move the motor back and forth, cycle in the original was back and forth
        # except for the last one, this does N-1 cycles
        for i in range(cycle-1):
            yield from bps.mv(motor, stop)
            yield from bps.mv(motor, start)
        # and the last pass forward
        yield from bps.mv(motor, stop)

        # wait for the detector to really finish
        yield from bps.wait(group=group)
        # put the detector reading in the primary stream
        yield from bps.create(name='primary')
        yield from bps.read(det)
        yield from bps.save()

    yield from bps.mv(motor, start)
    return (yield from inner())