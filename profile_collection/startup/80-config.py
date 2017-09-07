# things to read at begining and end of every scan
sd.baseline = [energy, sample, stage]

# this is the defalt list for %wa
BlueskyMagics.positioners = ([getattr(stage, m) for m in stage.signal_names] +
                             [getattr(sample, m) for m in sample.signal_names] +
                             [energy.bragg, energy.energy, energy.ivugap])

# this is the default list for %ct
BlueskyMagics.detectors = [FS]

def change_sample(*, user_name, sample_name, tray_number=None):
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
    pil1M.cam.file_number.put(0)
    pil300KW.cam.file_name.put(fname)
    pil300KW.cam.file_number.put(0)    


def proposal_id(proposal_id):
    RE.md['proposal_id'] = proposal_id
    
    pil1M.cam.file_path.put(f"/data/1M/images/users/{proposal_id}/")
    pil300KW.cam.file_path.put(f"/data/300KW/images/users/{proposal_id}/")
