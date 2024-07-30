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

'''
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
        # construct the det list here
        # add run decorator and stage decorators here ()
        def inner():
            for wa in waxs_arc:
                yield from bps.mv(waxs, wa)
                dets = [pil900KW] if waxs.arc.position < 15 else [pil900KW, pil1M] # making one run this will not be possible
                # potentially we don't link those useless files
                # or make the detecor know when it's useless and produce none and have tiled assume nans
                # or have different trigger and reads e.g.(name="saxs") (different streams) for each detector
                yield from bps.declare_stream(...)
                for ai in incident_angles:

                    yield from bps.mv(piezo.th, ai0 + ai)
                    for e in energies:
                        
                        yield from bps.mv(energy, e)# ADD SETTLE TIME TO ENERGY?
                        yield from bps.sleep(2)

                        sample_name = f'{name}{get_scan_md_tender()}_ai{ai}'
                        sample_id(user_name=user_name, sample_name=sample_name)
                        print(f"\n\n\n\t=== Sample: {sample_name} ===")
                        yield from bp.count(dets) # potentially add all motors to  and motor indexes(soft signals to match up saxs and nosaxs streams) 
                        
                        def inner_copunt(...):
                        #Toms replacement for bp.count
                        yield from bps.checkpoint()
                        yield from bps.trigger(pil900KW, group='dets')
                        arc = yield from  bps.rd(waxs.arc)
                        if arc is not None and arc > 15:
                            yield from bps.trigger(pil1M, group='dets')
                        yield from bps.wait(group='dets')
                        yield from bps.create(name='SAXS')
                        yield from bps.read(...)
                        yield from bps.save()
                        if COND:
                            yield from bps.create(name='WAXS')

                            yield from bps.read(pil1M)
                            for m in motors:
                                yield from bps.read(m)
                            yield from bps.save()
                        # (do hinting to adjust what adds to the livetable etc)
                        # change count to trigger_and_read(), add around the outer for loop stage list of detector, run decorator 
                        # add all motors we care about in the dets scan_nd([dets])
                        # add signal for index position in scan -  motor positions
                        # to trigger once..
                    yield from bps.mv(energy, energies[int(len(energies) / 2)])
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, energies[0])
                
                yield from bps.mv(piezo.th, ai0)
            waxs_arc = waxs_arc[::-1]
        yield from inner()
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)
'''
'''
Sample    piezo_x: min     max    cen   piezo_y    piezo_z   th_0    stage_x
-----------------------------------------------------------------------
Fl screen       -51000                   6000
6.0             -46000  -38000 -42000    6646.7       800      2.920      o
5.0             -34000  -26000 -30000    6616.7       800      2.927      0
4.0             -22000  -16000 -19000    6628.1       800      2.930      0
0                -9000   -1000  -5000    6544.6       800      2.943      0
0                 3000   13000   8000    6574.1       800      2.930      0
3.0              18000   25000  21500    6571.1       800      2.930      0
2.5              29000   37000  33000    6536.7       800      2.452      0
2.25             42000   50000  45000    6554.9       800      2.939      0
Si               53000   57000  54000    6713.0       200      2.943      0

Si
----------
angle   roi_min_Y      attenuators
0           1253         att2_6, att2_5 
0.1         1247
0.2         1241
0.3         1236
0.4         1230
0.5         1225
0.75        1211         att2_6, att2_12
1           1197            
1.25                 att2_6
1.5         1167         att2_5, att2_12
1.75                
2           1139         att2_5
2.25                 att2_12
2.5         1112         att2_12
3           1082         att2_12
3.5         1053         att2_12
4           1026         att2_12

'''

def att6(angle):
    if angle < 1.3:
        return 1
    else:
        return 0
def att5(angle):
    if angle < 0.5:
        return 1
    elif angle < 1.3:
        return 0
    elif angle <2.2:
        return 1
    else:
        return 0
    
def att12(angle):
    if angle < 0.5:
        return 0
    elif angle < 0.9 :
        return 1
    elif angle < 1.3:
        return 0
    elif angle < 1.9:
        return 1
    elif angle < 2.2:
        return 0
    else:
        return 1


def roiy(angle):
    return int(1252.855 -1620.548*np.tan(np.deg2rad(angle)*2)) 

def goto_angle(angle,th0_si):
    yield from bps.mv(
        att2_6.open_cmd, att6(angle),
        att2_6.close_cmd, 1-att6(angle),
        att2_5.open_cmd, att5(angle),
        att2_5.close_cmd, 1-att5(angle),
        att2_12.open_cmd, att12(angle),
        att2_12.close_cmd, 1-att12(angle),
        pil900KW.roi4.min_xyz.min_y,roiy(angle),
        piezo.th,th0_si+angle
    )




def reflectivity_multisample():
    sample_names = ['IBMSi1',    'IBM6p0',  'IBM5p0',  'IBM4p0',  'IBM0p01',    'IBM0p02', 'IBM3p0',  'IBM2p5',     'IBM2p25', 'IBMSi2']
    x_piezos =     [55000,      -43000,    -31000,     -20000,     -6000,      -9000,      22000,      33000,      47000,     55000]
    y_piezos =     [6713.0,     6646.7,    6616.7,     6628.1,     6544.6,     6574.1,     6571.1,     6536.7,     6554.9,    6713.0]
    th0s     =     [2.943,      2.920,     2.927,      2.930,      2.943,      2.930,      2.930,      2.452 ,     2.939,     2.943]



    angles = np.linspace(0,4,800)
    
    attenuator6o = [att6(angle) for angle in angles]
    attenuator6c = [1-att6(angle)for angle in angles]
    attenuator5o = [att5(angle) for angle in angles]
    attenuator5c = [1-att5(angle) for angle in angles]
    attenuator12o = [att12(angle) for angle in angles]
    attenuator12c = [1-att12(angle) for angle in angles]

    roi_centers = [roiy(angle) for angle in angles]


    pil900KW.stats4.centroid.x.kind = 'hinted'
    pil900KW.stats4.centroid.y.kind = 'hinted'
    pil900KW.stats4.centroid_total.kind = 'hinted'
    pil900KW.stats4.total.kind = 'hinted'
    pil900KW.stats4.kind = 'hinted'
    
    for sample, xp, yp, th0 in zip(sample_names, x_piezos, y_piezos, th0s):
        angles0 = [th0 + angle for angle in angles]


        yield from bps.mv(  piezo.x, xp,
                            piezo.y, yp)
        sample_id(user_name="Eliot", sample_name=sample)

        yield from bp.list_scan([pil900KW,pil900KW.stats4.centroid_total,pil900KW.stats4.total],
                                piezo.th,angles0,
                                pil900KW.roi4.min_xyz.min_y,roi_centers,
                                att2_6,attenuator6o,
                                att2_5,attenuator5o,
                                att2_12,attenuator12o,
                                )





### In case useful ###

def atten_move_in():
    """
    Move 4x + 2x Sn 60 um attenuators in
    """
    print('Moving attenuators in')

    while att1_7.status.get() != 'Open':
        yield from bps.mv(att1_7.open_cmd, 1)
        yield from bps.sleep(1)
    while att1_6.status.get() != 'Open':
        yield from bps.mv(att1_6.open_cmd, 1)
        yield from bps.sleep(1)

def atten_move_out():
    """
    Move 4x + 2x Sn 60 um attenuators out
    """
    print('Moving attenuators out')
    while att1_7.status.get() != 'Not Open':
        yield from bps.mv(att1_7.close_cmd, 1)
        yield from bps.sleep(1)
    while att1_6.status.get() != 'Not Open':
        yield from bps.mv(att1_6.close_cmd, 1)
        yield from bps.sleep(1)

### In case useful ###
def reflectivity_multisample_segment():
    sample_names = ['IBMSi']#,    'IBM6p0',  'IBM5p0',  'IBM4p0',  'IBM0p01',    'IBM0p02', 'IBM3p0',  'IBM2p5',     'IBM2p25', 'IBMSi']
    x_piezos =     [55000]#,      -43000,    -31000,     -20000,     -6000,      -9000,      22000,      33000,      47000,     55000]
    y_piezos =     [6713.0]#,     6646.7,    6616.7,     6628.1,     6544.6,     6574.1,     6571.1,     6536.7,     6554.9,    6713.0]
    th0s     =     [2.943]#,      2.920,     2.927,      2.930,      2.943,      2.930,      2.930,      2.452 ,     2.939,     2.943]

    angles_1 = np.linspace(0.0,  0.7,  71)[:-1]
    angles_2 = np.linspace(0.7,  0.9,  21)[:-1]
    angles_3 = np.linspace(0.9,  1.3,  41)[:-1]
    angles_4 = np.linspace(1.3,  1.9,  61)[:-1]
    angles_5 = np.linspace(1.9,  2.2,  31)[:-1]
    angles_6 = np.linspace(2.2,  4.0,  181)[:-1]

    angles = np.linspace(0,4,20)
    
    attenuator6o = [att6(angle) for angle in angles]
    attenuator6c = [1-att6(angle)for angle in angles]
    attenuator5o = [att5(angle) for angle in angles]
    attenuator5c = [1-att5(angle) for angle in angles]
    attenuator12o = [att12(angle) for angle in angles]
    attenuator12c = [1-att12(angle) for angle in angles]

    roi_centers = [roiy(angle) for angle in angles]


    pil900KW.stats4.centroid.x.kind = 'hinted'
    pil900KW.stats4.centroid.y.kind = 'hinted'
    pil900KW.stats4.centroid_total.kind = 'hinted'
    pil900KW.stats4.total.kind = 'hinted'
    
    for sample, xp, yp, th0 in zip(sample_names, x_piezos, y_piezos, th0s):
        angles0 = [th0 + angle for angle in angles]


        yield from bps.mv(  piezo.x, xp,
                            piezo.y, yp)
        sample_id(user_name="Eliot", sample_name=sample)

        yield from bp.list_scan([pil900KW,pil900KW.stats4.centroid_total,pil900KW.stats4.total],
                                piezo.th,angles0,
                                pil900KW.roi4.min_xyz.min_y,roi_centers,
                                att2_6.open_cmd,attenuator6o,
                                att2_6.close_cmd,attenuator6c,
                                att2_5.open_cmd,attenuator5o,
                                att2_5.close_cmd,attenuator5c,
                                att2_12.open_cmd,attenuator12o,
                                att2_12.close_cmd,attenuator12c,
                                )

