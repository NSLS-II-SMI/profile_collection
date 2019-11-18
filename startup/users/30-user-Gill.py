
def gill_giwaxs(exp_time=0.3):
    dets = [pil300KW, pil1M]
    name = 'Salt_nickel_sapphire_cool_300-0.3s'  
    inc_angle = [0.12, 0.3, 0.4]
    waxs_arc = [0, 39, 7]
    #yield from alignement_gisaxs_hex(angle = 0.1)
    for incident_angle in inc_angle:
        name_fmt = '{sample}_{angle}deg'
        yield from bps.mvr(stage.th, incident_angle)
        sample_name = name_fmt.format(sample=name, angle=incident_angle)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        sample_id(user_name='SG', sample_name=sample_name)
        det_exposure_time(exp_time, exp_time)
        yield from bp.scan(dets, waxs, *waxs_arc)
        yield from bps.mvr(stage.th, -incident_angle)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)
