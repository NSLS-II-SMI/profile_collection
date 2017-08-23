# things to read at begining and end of every scan
sd.baseline = [energy, sample, stage]

# this is the defalt list for %wa
BlueskyMagics.positioners = ([getattr(stage, m) for m in stage.signal_names] +
                             [getattr(sample, m) for m in sample.signal_names] +
                             [energy.bragg, energy.energy, energy.ivugap])

# this is the default list for %ct
BlueskyMagics.detectors = [FS]
