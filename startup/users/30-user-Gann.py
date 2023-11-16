def get_scan_md_tender():
    """
    Create a string with scan metadata
    """
    # Metadata
    e = energy.position.energy / 1000
    #temp = str(np.round(float(temp_degC), 1)).zfill(5)
    wa = waxs.arc.position + 0.001
    wa = str(np.round(float(wa), 1)).zfill(4)
    sdd = pil1m_pos.z.position / 1000

    md_fmt = ("_{energy}keV_wa{wa}_sdd{sdd}m")

    scan_md = md_fmt.format(
        energy = "%.5f" % e ,
        wa = wa,
        sdd = "%.1f" % sdd,
    )
    return scan_md


def test_gi_tender(t=0.5):
    """
    Grazing incidence tender
    """

    proposal_id('2023_2', '000001_Gann', analysis=True)

    names   = ['subhSK1','subhSK2','subhSK3','subhSK4','subhSK6','subhSK7','subhSK8', ]
    piezo_x = [  -55000 , -45000  , -31000  , -15000  , 18000   , 35000   , 47000, ]
    piezo_y = [ 6648 for n in names ]
    piezo_z = [ 6600 for n in names ]

    energies = np.concatenate((np.arange(2445, 2470, 5),
                               np.arange(2470, 2480, 0.25),
                               np.arange(2480, 2490, 1),
                               np.arange(2490, 2501, 5),
                               ))

    incident_angles = [0.1, 0.2, 0.3, 0.4]
    waxs_arc = [0, 20, 40, 60]

    user_name = "EG"
    det_exposure_time(t, t)

    msg = "Wrong number of coordinates, check names, piezos, and hexas"
    assert len(piezo_x) == len(names), msg
    assert len(piezo_x) == len(piezo_y), msg
    assert len(piezo_y) == len(piezo_z), msg
    yield from bps.mv(waxs, waxs_arc[0])

    for name, x, y, z in zip(names, piezo_x, piezo_y, piezo_z):

        yield from bps.mv(piezo.x, x,
                          piezo.y, y,
                          piezo.z, z,)

        # Align the sample
        try:
            yield from alignement_gisaxs()
        except:
            yield from alignement_gisaxs(0.01)

        # Sample flat at ai0
        ai0 = piezo.th.position
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M]
        
            for ai in incident_angles:

                yield from bps.mv(piezo.th, ai0 + ai)
                for e in energies:
                    
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                    sample_name = f'{name}{get_scan_md_tender()}_ai{ai}'
                    sample_id(user_name=user_name, sample_name=sample_name)
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    yield from bp.count(dets)
                
                yield from bps.mv(energy, energies[int(len(energies) / 2)])
                yield from bps.sleep(2)
                yield from bps.mv(energy, energies[0])
            
            yield from bps.mv(piezo.th, ai0)
        waxs_arc = waxs_arc[::-1]
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)