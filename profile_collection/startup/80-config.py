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


def proposal_id(proposal_id):
    RE.md['proposal_id'] = proposal_id
    
    pil1M.cam.file_path.put(f"/GPFS/xf12id1/data/1M/images/users/{proposal_id}/")
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/300KW/images/users/{proposal_id}/")


def beamline_mode(mode=None):
    allowed_modes = ['tender', 'hard']
    assert mode in allowed_modes, f'Wrong mode: {mode}, must choose: {" or ".join(allowed_modes)}'
    if mode == 'hard':
        hfm.y.move(11.6)
        hfm.x.move(0)
        hfm.th.move(-0.1722)
        vfm.x.move(12.3)
        vfm.y.move(-2.5)
        vfm.th.move(-0.18)
        vdm.x.move(12.3)
        vdm.th.move(-0.1801)
        vdm.y.move(-2.5)
    elif mode == 'tender':
        hfm.y.move(-12.4)
        hfm.x.move(-0.01)
        hfm.th.move(-0.17165)
        vfm.x.move(-11.7)
        vfm.y.move(-4.85)
        vfm.th.move(-0.35)
        vdm.x.move(-11.7)
        vdm.th.move(-0.3583)
        vdm.y.move(-2.2)


