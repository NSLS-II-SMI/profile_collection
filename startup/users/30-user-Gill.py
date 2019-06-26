
def gill_giwaxs(exp_time):
    dets = [pil300KW, pil1M]
    name = 'sapphire_salt_1strun_600C'
        
    inc_angle = [0.12, 0.2, 0.30]
    waxs_arc = [0, 39, 7]
    yield from alignement_gisaxs_hex(angle = 0.1)
    for incident_angle in inc_angle:
        name_fmt = '{sample}_{angle}deg'
        yield from bps.mvr(stage.th, incident_angle)
        sample_name = name_fmt.format(sample=name, angle=incident_angle)
        sample_id(user_name='SG', sample_name=sample_name)
        det_exposure_time(exp_time, exp_time)
        yield from bp.scan(dets, waxs, *waxs_arc)
        yield from bps.mvr(stage.th, -incident_angle)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)
