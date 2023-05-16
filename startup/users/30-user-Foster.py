def run_swaxs_Foster_2023_2(t=15):
    """
    Take WAXS and SAXS as linescans across capillaries
    Take transmission using attenuators

    """

    names =   [ 'Empty_cap_longer2', ]
    piezo_x = [  -19575, ]
    piezo_y = [   1350, ]
    hexa_y =  [       0, ]  #in mm
    points =  [       1, ]

    dy = 0
    waxs_arc = [20, 0]

    bs_pos_x = 1.35
    transmission_exposure = 1.0
    dx = 1500
    user = "MF"


    # Check if the length of xlocs, ylocs and names are the same
    msg = "Wrong number of coordinates, check names, piezos, and hexas"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_x) == len(hexa_y), msg

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]

        for name, x, y, hy, pts in zip(names, piezo_x, piezo_y, hexa_y, points):
            yield from bps.mv(piezo.y, y,
                              piezo.x, x,
                              stage.y, hy)
            
            # Take sample camera image
            if wa == waxs_arc[0]:
                sample_name = f'{name}{get_scan_md()}_loc0'
                yield from bp.count([OAV_writing])
            
            for i, pt in enumerate(range(pts)):

                yield from bps.mv(piezo.y, y + i * dy)

                if ( 19 < waxs.arc.position ) and ( waxs.arc.position < 21 ):

                    # Take transmission
                    det_exposure_time(transmission_exposure, transmission_exposure)
                    while att1_7.status.get() != 'Open':
                        yield from bps.mv(att1_7.open_cmd, 1)
                        yield from bps.sleep(1)

                    # Sample
                    yield from bps.mv(pil1m_bs_rod.x, bs_pos_x + 5)
                    sample_name = f'{name}-attn-sample'
                    sample_id(user_name='test', sample_name=sample_name)
                    yield from bp.count([pil1M])
                    stats1_sample = db[-1].table(stream_name='primary')['pil1M_stats1_total'].values[0]

                    # Direct beam
                    yield from bps.mv(piezo.x, x + dx)
                    sample_name = f'{name}-attn-direct'
                    sample_id(user_name='test', sample_name=sample_name)
                    yield from bp.count([pil1M])
                    stats1_direct = db[-1].table(stream_name='primary')['pil1M_stats1_total'].values[0]

                    # Transmission
                    trans = np.round( stats1_sample / stats1_direct, 5)

                    # Revert configuraton
                    det_exposure_time(t, t)
                    yield from bps.mv(pil1m_bs_rod.x, bs_pos_x)
                    while att1_7.status.get() != 'Not Open':
                        yield from bps.mv(att1_7.close_cmd, 1)
                        yield from bps.sleep(1)
                else:
                    trans = 0

                # Take normal scans
                yield from bps.mv(piezo.x, x)
                sample_name = f'{name}{get_scan_md()}_loc{pt}_trs{trans}'
                sample_id(user_name=user, sample_name=sample_name)
                print(f"\n\n\n\t=== Sample: {sample_name} ===")
                yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)