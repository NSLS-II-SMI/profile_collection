# things to read at begining and end of every scan
sd.baseline = [energy, sample, stage]

# this is the defalt list for %wa
BlueskyMagics.positioners = ([getattr(stage, m) for m in stage.component_names] +
                             [getattr(sample, m) for m in sample.component_names] +
                             [energy.bragg, energy.energy, energy.ivugap])

# this is the default list for %ct
BlueskyMagics.detectors = [FS]

def sample_id(*, user_name, sample_name, tray_number=None):
    RE.md['user_name'] = user_name
    RE.md['sample_name'] = sample_name
    if tray_number is None:
        RE.md.pop('tray_number', None)
    else:
        RE.md['tray_number'] = tray_number
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
    RE.md['proposal_id'] = proposal_id
    pil1M.cam.file_path.put(f"/GPFS/xf12id1/data/1M/images/users/{proposal_id}/")
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/300KW/images/users/{proposal_id}/")
    # 2018-04-10: Maksim asked Tom about why this 'put' does not create the folder,
    # Tom suggested to ask PoC to update AD installation.
    import stat
    newDir = "/GPFS/xf12id1/data/MAXS/images/users/" + str(proposal_id) + "/"
    try:
        os.stat(newDir)
    except FileNotFoundError:
        os.makedirs(newDir)
        os.chmod(newDir, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)
    rayonix.cam.file_path.put(f"/GPFS/xf12id1/data/MAXS/images/users/{proposal_id}/")

def beamline_mode(mode=None):
    allowed_modes = ['sulfur', 'hard']
    assert mode in allowed_modes, f'Wrong mode: {mode}, must choose: {" or ".join(allowed_modes)}'
    if mode == 'hard':
        hfm.y.move(11.6)
        hfm.x.move(0.0)
        hfm.th.move(-0.1748)
        vfm.x.move(12.3)
        vfm.y.move(-2.5)
        vfm.th.move(-0.18)
        vdm.x.move(12.3)
        vdm.th.move(-0.1798)
        vdm.y.move(-2.59)
    elif mode == 'sulfur':
        hfm.y.move(-12.4)
        hfm.x.move(0.0)
        hfm.th.move(-0.1742)
        vfm.x.move(-11.7)
        vfm.y.move(-4.7)
        vfm.th.move(-0.35)
        vdm.x.move(-11.7)
        vdm.th.move(-0.3576)
        vdm.y.move(-2.2)


def fly_scan(det, motor, cycle=1, cycle_t=10, phi = -0.6):
    start = phi +10
    stop = phi-10
    acq_time = cycle * cycle_t
    yield from bps.mv(motor, start)
    #yield from bps.mv(attn_shutter, 'Retract')
    det.stage()
    det.cam.acquire_time.put(acq_time)
    print(f'Acquire time before staging: {det.cam.acquire_time.get()}')
    st = det.trigger()
    for i in range(cycle):
        yield from list_scan([], motor, [start, stop, start])
    while not st.done:
        pass
    det.unstage()
    print(f'We are done after {acq_time}s of waiting')
    #yield from bps.mv(attn_shutter, 'Insert')
    
'''    
def fly_scan_gisaxs(det, motor, name='SNS', cycle=1, cycle_t=10, n_cycles=3):
    x1 = -11.55
    y1 = 1.65
    start_angle1 = -0.416
    phi1 = -0.641
    x2 = 17
    y2 = 1.605
    start_angle2 = -0.356
    phi2 = -0.603    
    #the loop for 302 K   
    #sample 1
    stage.th.move(start_angle1)
    prs.move(phi1)
    sample_id(user_name=name, sample_name='C72_poly-b_302K_0.35deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    RE(bps.mv(attn_shutter, 'Retract'))
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_302K_0.35deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    bp.time.sleep(1)
    prs.move(phi1)
    stage.x.move(x1+0.2)
    sample_id(user_name=name, sample_name='C72_poly-b_302K_0.25deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle1+0.1)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_302K_0.25deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    bp.time.sleep(1)
    prs.move(phi1)
    stage.x.move(x1+0.4)
    sample_id(user_name=name, sample_name='C72_poly-b_302K_0.2deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle1+0.15)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_302K_0.2deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    RE(bps.mv(attn_shutter, 'Insert'))   
    #sample 2
    stage.th.move(start_angle2)
    prs.move(phi2)
    sample_id(user_name=name, sample_name='C36_poly_302K_0.35deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    RE(bps.mv(attn_shutter, 'Retract'))
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_302K_0.35deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    bp.time.sleep(1)
    prs.move(phi2)
    stage.x.move(x2+0.2)
    sample_id(user_name=name, sample_name='C36_poly_302K_0.25deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle2+0.1)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_302K_0.25deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    bp.time.sleep(1)
    prs.move(phi2)
    stage.x.move(x2+0.4)
    sample_id(user_name=name, sample_name='C36_poly_302K_0.2deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle2+0.15)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_302K_0.2deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    RE(bps.mv(attn_shutter, 'Insert'))

    #loop for 305K
    #sample 1
    x1 = x1+0.6
    stage.x.move(x1)
    stage.th.move(start_angle1)
    prs.move(phi1)
    sample_id(user_name=name, sample_name='C72_poly-b_305K_0.35deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    RE(bps.mv(attn_shutter, 'Retract'))
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_305K_0.35deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    bp.time.sleep(1)
    prs.move(phi1)
    stage.x.move(x1+0.2)
    sample_id(user_name=name, sample_name='C72_poly-b_305K_0.25deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle1+0.1)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_305K_0.25deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    bp.time.sleep(1)
    prs.move(phi1)
    stage.x.move(x1+0.4)
    sample_id(user_name=name, sample_name='C72_poly-b_305K_0.2deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle1+0.15)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_305K_0.2deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    RE(bps.mv(attn_shutter, 'Insert'))   
    #sample 2
    x2 = x2+0.6
    stage.x.move(x2)
    stage.th.move(start_angle2)
    prs.move(phi2)
    sample_id(user_name=name, sample_name='C36_poly_305K_0.35deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    RE(bps.mv(attn_shutter, 'Retract'))
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_305K_0.35deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    bp.time.sleep(1)
    prs.move(phi2)
    stage.x.move(x2+0.2)
    sample_id(user_name=name, sample_name='C36_poly_305K_0.25deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle2+0.1)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_305K_0.25deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    bp.time.sleep(1)
    prs.move(phi2)
    stage.x.move(x2+0.4)
    sample_id(user_name=name, sample_name='C36_poly_305K_0.2deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle2+0.15)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_305K_0.2deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    RE(bps.mv(attn_shutter, 'Insert'))

    #loop for 310K
    #sample 1
    x1 = x1+1.2
    stage.x.move(x1)
    stage.th.move(start_angle1)
    prs.move(phi1)
    sample_id(user_name=name, sample_name='C72_poly-b_310K_0.35deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    RE(bps.mv(attn_shutter, 'Retract'))
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_310K_0.35deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    bp.time.sleep(1)
    prs.move(phi1)
    stage.x.move(x1+0.2)
    sample_id(user_name=name, sample_name='C72_poly-b_310K_0.25deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle1+0.1)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_310K_0.25deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    bp.time.sleep(1)
    prs.move(phi1)
    stage.x.move(x1+0.4)
    sample_id(user_name=name, sample_name='C72_poly-b_310K_0.2deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle1+0.15)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C72_poly-b_310K_0.2deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi1))
    RE(bps.mv(attn_shutter, 'Insert'))   
    #sample 2
    x2 = x2+1.2
    stage.x.move(x2)
    stage.th.move(start_angle2)
    prs.move(phi2)
    sample_id(user_name=name, sample_name='C36_poly_310K_0.35deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    RE(bps.mv(attn_shutter, 'Retract'))
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_310K_0.35deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    bp.time.sleep(1)
    prs.move(phi2)
    stage.x.move(x2+0.2)
    sample_id(user_name=name, sample_name='C36_poly_310K_0.25deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle2+0.1)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_310K_0.25deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    bp.time.sleep(1)
    prs.move(phi2)
    stage.x.move(x2+0.4)
    sample_id(user_name=name, sample_name='C36_poly_310K_0.2deg')
    det.cam.acquire_time.put(cycle*cycle_t)
    stage.th.move(start_angle2+0.15)
    RE(count([pil1M], num=1))
    sample_id(user_name=name, sample_name='C36_poly_310K_0.2deg_sweep20')
    for i in range(n_cycles):    
        RE(fly_scan(det, motor, cycle, cycle_t, phi2))
    RE(bps.mv(attn_shutter, 'Insert'))




'''
