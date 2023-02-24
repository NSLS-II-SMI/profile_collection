def alice_grid_scans_2022_3(t=0.5):
    """
    Run sample grid scans

    From 30-user-Telles.py
    
    Note:
        names: sample names
        piezo_x: position of piezo x in um for the vertical line scan,
        piezo_y: starting position (top of the sample) for the vertical line scan in um,
        hexa_y: positon of the hexapod in mm,
        y_range: [0 as you start from the piezo_y, then relative distance in um to the end of the smple, number
                  of points to get 10 um step + 1,]
        x_range: [0 as you start from the piezo_x, then relative distance in um to the end of the smple, number
                  of points to get 10 um step + 1,]

        To load in interactive namespace in BlueSky
        %run -i startup/users/30-user-Fergerson.py

        proposal_id("2023_1", "311050_Fergerson2)
    """
    macro_user_name = 'alice_grid_scans_2022_3'


    # # Row A
    # names_A =   [ '7A1','7A2','7A3','7A4','7A5','7A6','7A7','7A8','7A9','7A10','7A11','7A12','7A13','7A14','7A15']
    # shear_A =   [100 for n in names_A]
    # draw_A  =   [1,1,1, 1.3,1.3,1.3, 1.6,1.6,1.6, 2,2,2, 2.3,2.3,2.3]
    # anneal_A =  [False for n in names_A]
    # piezo_x_A = [-38600,-32600, -26600,-20600, -14600, -8600, -2600, 3400,  9400, 15400, 21400, 27400, 33400, 39400, 45400]
    # piezo_y_A = [-9000, -9000,  -9000, -9000,  -9000, -9200, -9250, -9500, -9400, -9300, -9600, -9500, -9800, -9800, 9850] 
    # hexa_y_A  = [ -6 for n in names_A ]

    # # Row B
    # names_B =   [ '7B1','7B2','7B3','7B4','7B5','7B6','7B7','7B8','7B9','7B10','7B11','7B12','7B13','7B14','7B15']
    # shear_B =   [300 for n in names_B]
    # draw_B  =   [1,1,1, 1.3,1.3,1.3, 1.6,1.6,1.6, 2,2,2, 2.3,2.3,2.3]
    # anneal_B =  [False for n in names_B]
    # piezo_x_B = [-38600,-32600, -26600,-20600, -14600, -8600, -2600, 3400,  9400, 15400, 21400, 27400, 33400, 39400, 45400]
    # piezo_y_B = [-4000, -4200,   -4200, -3900, -4000,  -4000, -4300, -4400, -4500, -4400, -4500, -4700, -4800, -5100, -4900]
    # hexa_y_B  = [ -6 for n in names_B ] 

    # # Row C
    # names_C =   [ '7C1','7C2','7C3','7C4','7C5','7C6','7C7','7C8','7C9']
    # shear_C =   [1000 for n in names_C]
    # draw_C  =   [1,1,1, 1.3,1.3,1.3, 1.6,1.6,1.6]
    # anneal_C =  [False for n in names_C]
    # piezo_x_C = [-38600,-32600, -26600,-20600, -14600, -8600, -2600, 3400,  9400]
    # piezo_y_C = [1350, 1100,    800,   800,     900,   900,   700,   450, 350,    ]
    # hexa_y_C  = [ -6 for n in names_C ] 

    # # Row D
    # names_D =   [ '7D1','7D2','7D3','7D4','7D5','7D6','7D7','7D8','7D9','7D10','7D11','7D12','7D13','7D14','7D15']
    # shear_D =   [100 for n in names_A]
    # draw_D  =   [1,1,1, 1.3,1.3,1.3, 1.6,1.6,1.6, 2,2,2, 2.3,2.3,2.3]
    # anneal_D =  [True for n in names_D]
    # piezo_x_D = [-38600,-32600, -26600,-20600, -14600, -8600, -2600, 3400,  9400, 15400, 21400, 27400, 33400, 39400, 45400]
    # piezo_y_D = [-8100,  -8100, -8100, -8000,  -8100,  -8000,  -8300, -8300,-8600,-8500, -8700, -8600, -8800, -9000, -8800]
    # hexa_y_D  = [ 8 for n in names_D ] 

    # # Row E
    # names_E =   ['7E1','7E2','7E3','7E4','7E5','7E6','7E7','7E8','7E9','7E10','7E11','7E12','7E13','7E14','7E15']
    # shear_E =   [300 for n in names_E]
    # draw_E  =   [1,1,1, 1.3,1.3,1.3, 1.6,1.6,1.6, 2,2,2, 2.3,2.3,2.3]
    # anneal_E =  [True for n in names_E]
    # piezo_x_E = [-38600,-32600, -26600,-20600, -14600, -8600, -2600, 3400,  9400, 15400, 21400, 27400, 33400, 39400, 45400]
    # piezo_y_E = [-3200, -3300, -3400,  -3300, -3600, -3300,   -3600, -3500, -3400, -3400, -3600,-3750, -3750, -4100, -3900]
    # hexa_y_E  = [ 8 for n in names_E] 

    # # Row F
    # names_F =   ['5F1','5F2','5F3','5F4','5F5','5F6','5F7','5F8','5F9']
    # shear_F =   [1000 for n in names_F]
    # draw_F  =   [1,1,1, 1.3,1.3,1.3, 1.6,1.6,1.6]
    # anneal_F =  [True for n in names_F]
    # piezo_x_F = [-38600,-32600, -26600,-20600, -14600, -8600, -2600, 3400,  9400]
    # piezo_y_F = [1600,  1650,    1650, 1650,     1500,  1450,  1450, 1550, 1450]
    # hexa_y_F  = [ 8 for n in names_F] 
    
    # # Row G
    # names_G =   [ f'5G{x + 1}' for x in range(15) ]
    # shear_G =   [100 for n in names_G]
    # draw_G  =   [1,1,1,1.3,1.3,1.3,1.6,1.6,1.6,2,2,2,2.3,2.3,2.3]
    # anneal_G =  [True for n in names_G]
    # piezo_x_G = [-39300,-33300,-27300,-21300,-15300,-9300,-3300,2700,8700,14700,20700,26700,32700,38700,44700]
    # piezo_y_G = [9375,9175,9275,9375,9375,9075,9375,9375,9275,9275,9575,9475,9475,9375,9175]
    # hexa_y_G  = [ 5 for n in names_G]



    # Combine lists
 
    # names = names_A + names_B + names_C + names_D + names_E + names_F #+ names_G
    # shear = shear_A + shear_B + shear_C + shear_D + shear_E + shear_F #+ shear_G
    # draw = draw_A + draw_B + draw_C + draw_D + draw_E + draw_F #+ draw_G
    # anneal = anneal_A + anneal_B + anneal_C + anneal_D + anneal_E + anneal_F #+ anneal_G
    # piezo_x = piezo_x_A + piezo_x_B + piezo_x_C + piezo_x_D + piezo_x_E + piezo_x_F #+ piezo_x_G
    # piezo_y = piezo_y_A +  piezo_y_B + piezo_y_C + piezo_y_D + piezo_y_E + piezo_y_F #+ piezo_y_G
    # hexa_y = hexa_y_A +  hexa_y_B + hexa_y_C + hexa_y_D + hexa_y_E + hexa_y_F #+ hexa_y_G

    # 
    names =     ['6C1', '6C4',  '6C7',  '6C8',  '6D1',  '6D4',  '6D7',  '6D8',  '6B1',  '6B10', '6B4',  '6B7',  '6B13']
    shear =      [0.1,   1,      1000,   1000,   0.1,    1,      1000,   1000,   100,    100,    100,    100,    100]
    draw =       [   1,  1,      1,      1,      2,      2,      2,      2,     1,       1.3,    1.6,    2,      2.3]
    anneal =    [True,  True,   False, True,   True,   True,    False,  True,   True,   True,   True,   True,   True]
    piezo_x =   [-39700,-21750, -3600,  2100, -33600,   -21700, -3400,  2250, -39200,   14400,  -21600, -3700,  32500]
    piezo_y =   [-1625, -2025,  -2025,  -1925,  3175,   3175,   2875,   3000,   -6700,  -7200,  -6900,  -7250,  -7650]
    hexa_y =    [-3 for n in names]



    # Ranges the same for all samples
    # For line scan, make x_range last value = 1, i.e. x_range = [0, 100, 1]
    # For sample specific range one could use
    # if name == 'sample-for-which-to-change] x_range = [0, 150, 16] else [0, 1250, 51]

    y_range = [0, 1000, 41]
    x_range = [0, 1000, 41]


    assert len(piezo_x) == len(names), f"Number of X coordinates ({len(piezo_x)}) is different from number of samples ({len(names)})"
    assert len(shear) == len(names), f"Number of shear entries ({len(shear)}) is different from number of samples ({len(names)})"
    assert len(draw) == len(names), f"Number of draw entries ({len(draw)}) is different from number of samples ({len(names)})"
    assert len(anneal) == len(names), f"Number of anneal entries ({len(anneal)}) is different from number of samples ({len(names)})"
    assert len(hexa_y) == len(names), f"Number of hexapod Y position entries ({len(hexa_y)}) is different from number of samples ({len(names)})"
    assert len(piezo_x) == len(piezo_y ), f"Number of X coordinates ({len(piezo_x)}) is different from number of Y coordinates ({len(piezo_y)})"

    # Move WAXS out of the way
    if waxs.arc.position < 19.5:
        yield from bps.mv(waxs, 20)
    dets = [pil1M]
    det_exposure_time(t, t)

    for name, x, y, h_y, sh, dr, ann in zip(names, piezo_x, piezo_y, hexa_y, shear, draw, anneal):

        user_dict={
            'sample name':name, 'shear':sh, 'draw':dr, 'annealed':ann, 'user_macro':macro_user_name,
            'x_range':x_range,'y_range':y_range
        }

        yield from bps.mv(piezo.x, x,
                          piezo.y, y,
                          stage.y, h_y)
    
        # Metadata
        e = energy.position.energy / 1000  # energy keV
        sdd = pil1m_pos.z.position / 1000  # SAXS detector distance

        dy = int((y_range[1] - y_range[0]) / (y_range[2] - 1 ))
        if x_range[2] > 2:
            dx = int((x_range[1] - x_range[0]) / (x_range[2] - 1 ))
        else:
            dx = 0


        name_fmt = "{sample}_{energy}keV_sdd{sdd}m_dy{dy}um_dx{dx}um"
        sample_name = name_fmt.format(
            sample=name, energy="%.1f" % e, sdd="%.2f" % sdd, dy=dy, dx=dx)
        sample_id(user_name="AF", sample_name=sample_name)
        print(f"\n\n\n\t=== Sample: {sample_name} ===")

        yield from bp.rel_grid_scan(dets, piezo.y, *y_range, piezo.x, *x_range, 0,
                                    md=user_dict)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)