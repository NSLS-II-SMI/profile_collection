print(f"Loading {__file__}")

from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt

# things to read at begining and end of every scan
sd.baseline = [energy, stage, prs, piezo]

# this is the default list for %ct
# BlueskyMagics.detectors = [FS]


def sample_id(*, user_name, sample_name, tray_number=None):
    RE.md["user_name"] = user_name
    RE.md["sample_name"] = sample_name
    if tray_number is None:
        RE.md.pop("tray_number", None)
    else:
        RE.md["tray_number"] = tray_number
    if tray_number is None:
        fname = f"{user_name}_{sample_name}"
    else:
        fname = f"{user_name}_{sample_name}_{tray_number}"
    # DIRTY HACK, do not copy
    pil1M.cam.file_name.put(fname)
    pil1M.cam.file_number.put(1)
    pil300KW.cam.file_name.put(fname)
    pil300KW.cam.file_number.put(1)
    rayonix.cam.file_name.put(fname)
    rayonix.cam.file_number.put(1)


def proposal_id(proposal_id):
    RE.md["proposal_id"] = proposal_id
    pil1M.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/{proposal_id}/1M")
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/{proposal_id}/300KW")
    rayonix.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/{proposal_id}/MAXS")
    # 2018-04-10: Maksim asked Tom about why this 'put' does not create the folder,
    # Tom suggested to ask PoC to update AD installation.
    import stat

    newDir = "/GPFS/xf12id1/data/MAXS/images/users/" + str(proposal_id) + "/"
    # newDir = "/GPFS/xf12id1/data/images/users/{proposal_id}/MAXS"
    try:
        os.stat(newDir)
    except FileNotFoundError:
        os.makedirs(newDir)
        os.chmod(newDir, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)


def beamline_mode(mode=None):
    allowed_modes = ["sulfur", "hard"]
    assert (
        mode in allowed_modes
    ), f'Wrong mode: {mode}, must choose: {" or ".join(allowed_modes)}'
    if mode == "hard":
        hfm.y.move(11.6)  # 3.6 for Rh stripe
        hfm.x.move(-0.055)
        hfm.th.move(-0.1756)  # -0.1754 for Rh stripe
        vfm.x.move(12.3)
        vfm.y.move(-2.5)
        vfm.th.move(-0.18)
        vdm.x.move(12.3)
        vdm.th.move(-0.18)
        vdm.y.move(-2.59)
    elif mode == "sulfur":
        hfm.y.move(-12.4)
        hfm.x.move(-0.055)
        hfm.th.move(-0.1751)
        vfm.x.move(-11.7)
        vfm.y.move(-4.7)
        vfm.th.move(-0.35)
        vdm.x.move(-11.7)
        vdm.th.move(-0.36)
        vdm.y.move(-2.014)


def fly_scan(det, motor, cycle=1, cycle_t=10, phi=-0.6):
    start = phi + 10
    stop = phi - 10
    acq_time = cycle * cycle_t
    yield from bps.mv(motor, start)
    # yield from bps.mv(attn_shutter, 'Retract')
    det.stage()
    det.cam.acquire_time.put(acq_time)
    print(f"Acquire time before staging: {det.cam.acquire_time.get()}")
    st = det.trigger()
    for i in range(cycle):
        yield from list_scan([], motor, [start, stop, start])
    while not st.done:
        pass
    det.unstage()
    print(f"We are done after {acq_time}s of waiting")
    # yield from bps.mv(attn_shutter, 'Insert')


manual_PID_disable_pitch = EpicsSignal(
    "XF:12IDB-BI:2{EM:BPM3}fast_pidY_incalc.CLCN", name="manual_PID_disable_pitch"
)
manual_PID_disable_roll = EpicsSignal(
    "XF:12IDB-BI:2{EM:BPM3}fast_pidX_incalc.CLCN", name="manual_PID_disable_roll"
)


def feedback(action=None):
    allowed_actions = ["on", "off"]
    assert (
        action in allowed_actions
    ), f'Wrong action: {mode}, must choose: {" or ".join(allowed_actions)}'
    if action == "off":
        manual_PID_disable_pitch.set("1")
        manual_PID_disable_roll.set("1")
    elif action == "on":
        manual_PID_disable_pitch.set("0")
        manual_PID_disable_roll.set("0")
