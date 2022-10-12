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
    """
    macro_user_name = 'alice_grid_scans_2022_3'


    # Row A
    # names_A =   [ '6A1','6A4','6A7','6A10','6A13']
    # shear_A =   [10 for n in names_A]
    # draw_A  =   [1,1.3,1.6,2,2.3]
    # anneal_A =  [True for n in names_A]
    # piezo_x_A = [-42000,-23700,-5700,12400,30100]
    # piezo_y_A = [-8600,-8700,-8700,-8300,-8500]
    # hexa_y_A  = [ -7 for n in names_A ]

    # Row B
    names_B =   ['6B1','6B4','6B7','6B10','6B15']
    shear_B =   [100 for n in names_B]
    draw_B  =   [1,1.3,1.6,2,2.3]
    anneal_B =  [True for n in names_B]
    piezo_x_B = [-41900,-23800,-5700,12400,42400]
    piezo_y_B = [-3800,-3700,-3700,-3300,-3300]
    hexa_y_B  = [ -7 for n in names_B ] 

    # Row C
    names_C =   [ '6C1','6C4']
    shear_C =   [0.1,1]
    draw_C  =   [1,1]
    anneal_C =  [True for n in names_C]
    piezo_x_C = [-41900,-23900]
    piezo_y_C = [1300,1200]
    hexa_y_C  = [ -7 for n in names_C ] 

    # Row D
    names_D =   [ '6D1','6D4' ]
    shear_D =   [0.1,1]
    draw_D  =   [2,2]
    anneal_D =  [True for n in names_D]
    piezo_x_D = [-42200,-24100]
    piezo_y_D = [6300,6500]
    hexa_y_D  = [ -7 for n in names_D ] 

    # # Row E
    # names_E =   ['5E1','5E2','5E3','5E4','5E5','5E6','5E7','5E8','5E9','5E10','5E11','5E12','5E13','5E14','5E15']
    # shear_E =   [10 for n in names_E]
    # draw_E  =   [1,1,1,1.3,1.3,1.3,1.6,1.6,1.6,2,2,2,2.3,2.3,2.3]
    # anneal_E =  [True for n in names_E]
    # piezo_x_E = [-39300,-33300,-27300,-21300,-15300,-9300,-3300,2700,8700,14700,20700,26700,32700,38700,44700]
    # piezo_y_E = [-725,-325,-325,-425,-425,-525,-125,-425,-625,-1025,-425,-525,-225,-175,-475]
    # hexa_y_E  = [ 5 for n in names_E] 

    # # Row F
    # names_F =   ['5F1','5F2','5F3','5F4','5F5','5F6','5F7','5F8','5F9','5F10','5F11','5F12','5F13','5F14','5F15']
    # shear_F =   [30 for n in names_F]
    # draw_F  =   [1,1,1,1.3,1.3,1.3,1.6,1.6,1.6,2,2,2,2.3,2.3,2.3]
    # anneal_F =  [True for n in names_F]
    # piezo_x_F = [-39300,-33300,-27300,-21300,-15300,-9300,-3300,2700,8700,14700,20700,26700,32700,38700,44700]
    # piezo_y_F = [4275,4475,4875,4575,4775,4175,4475,4175,4575,4475,4275,4275,4075,4175,4175]
    # hexa_y_F  = [ 5 for n in names_F] 
    
    # # Row G
    # names_G =   [ f'5G{x + 1}' for x in range(15) ]
    # shear_G =   [100 for n in names_G]
    # draw_G  =   [1,1,1,1.3,1.3,1.3,1.6,1.6,1.6,2,2,2,2.3,2.3,2.3]
    # anneal_G =  [True for n in names_G]
    # piezo_x_G = [-39300,-33300,-27300,-21300,-15300,-9300,-3300,2700,8700,14700,20700,26700,32700,38700,44700]
    # piezo_y_G = [9375,9175,9275,9375,9375,9075,9375,9375,9275,9275,9575,9475,9475,9375,9175]
    # hexa_y_G  = [ 5 for n in names_G]



    # Combine lists
    # names = names_A + names_B + names_C + names_D #+ names_E + names_F + names_G
    # shear = shear_A + shear_B + shear_C + shear_D #+ shear_E + shear_F + shear_G
    # draw = draw_A + draw_B + draw_C + draw_D #+ draw_E + draw_F + draw_G
    # anneal = anneal_A + anneal_B + anneal_C + anneal_D #+ anneal_E + anneal_F + anneal_G
    # piezo_x = piezo_x_A + piezo_x_B + piezo_x_C + piezo_x_D #+ piezo_x_E + piezo_x_F + piezo_x_G
    # piezo_y = piezo_y_A + piezo_y_B + piezo_y_C + piezo_y_D #+ piezo_y_E + piezo_y_F + piezo_y_G
    # hexa_y = hexa_y_A + hexa_y_B + hexa_y_C + hexa_y_D #+ hexa_y_E + hexa_y_F + hexa_y_G

    names = names_B + names_C + names_D #+ names_E + names_F + names_G
    shear = shear_B + shear_C + shear_D #+ shear_E + shear_F + shear_G
    draw = draw_B + draw_C + draw_D #+ draw_E + draw_F + draw_G
    anneal = anneal_B + anneal_C + anneal_D #+ anneal_E + anneal_F + anneal_G
    piezo_x = piezo_x_B + piezo_x_C + piezo_x_D #+ piezo_x_E + piezo_x_F + piezo_x_G
    piezo_y = piezo_y_B + piezo_y_C + piezo_y_D #+ piezo_y_E + piezo_y_F + piezo_y_G
    hexa_y = hexa_y_B + hexa_y_C + hexa_y_D #+ hexa_y_E + hexa_y_F + hexa_y_G


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