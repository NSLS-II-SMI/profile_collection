
def gill_giwaxs(exp_time=0.5):
    dets = [pil300KW]
    name = 'Ni_111_Salt-RTcoolx2_0.5s'  
    #initial_angle_zero = -0.72
    inc_angle = [0.12, 0.22, 0.3]
    phi = [0]
    waxs_arc = [0, 39, 7]
    #yield from bps.mv(stage.th, initial_angle_zero)
    for ph in phi:
        yield from bps.mv(prs, ph)
        yield from alignement_gisaxs_hex_short(angle = 0.08)
        for incident_angle in inc_angle:
            name_fmt = '{sample}_phi{phiii}deg_{angle}deg'
            yield from bps.mvr(stage.th, incident_angle)
            sample_name = name_fmt.format(sample=name, phiii=ph, angle=incident_angle)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            sample_id(user_name='SG', sample_name=sample_name)
            det_exposure_time(exp_time, exp_time)
            yield from bp.scan(dets, waxs, *waxs_arc)
            yield from bps.mvr(stage.th, -incident_angle)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)
