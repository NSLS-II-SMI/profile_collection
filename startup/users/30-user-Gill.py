
def gill_giwaxs(exp_time=0.5):
    dets = [pil300KW]
    name = 'Ni110_RT_afterramp'  
    #initial_angle_zero = -0.72
    inc_angle = [0.12, 0.22, 0.30, 0.4]
    phi = [5]
    waxs_arc = [6.5, 39, 6]
    #yield from bps.mv(stage.th, initial_angle_zero)
    x = [-4, -3, -2, -1, 0, 1]
    for i, xsss in enumerate(x):
        yield from bps.mv(stage.x, xsss)
        for ph in phi:
            # yield from bps.mv(prs, ph)
            yield from bps.mv(GV7.open_cmd, 1 )
            yield from bps.sleep(1)
            yield from bps.mv(GV7.open_cmd, 1 )

            yield from alignement_gisaxs_hex_short(angle = 0.08)
            
            yield from bps.mv(GV7.close_cmd, 1 )
            yield from bps.sleep(1)
            yield from bps.mv(GV7.close_cmd, 1 )

            ai_0 = stage.th.position

            for incident_angle in inc_angle:
                name_fmt = '{sample}_pos{pos}_phi{phiii}deg_{angle}deg'
                yield from bps.mv(stage.th, ai_0 + incident_angle)
                sample_name = name_fmt.format(sample=name, pos ='%2.2f'%i ,phiii=ph, angle=incident_angle)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                sample_id(user_name='SG', sample_name=sample_name)
                det_exposure_time(exp_time, exp_time)
                yield from bp.scan(dets, waxs, *waxs_arc)
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5, 0.5)
