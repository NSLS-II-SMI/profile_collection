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
    names_A =   ['5A1', '5A2', '5A3', '5A10', '5A11', '5A12']
    shear_A =   [0.1 for n in names_A]
    draw_A  =   [1,1,1,2,2,2]
    anneal_A =  [True for n in names_A]
    piezo_x_A = []
    piezo_y_A = []
    hexa_y_A  = [ -7 for n in names_A ]

    # Row B
    names_B =   ['5B1','5B2','5B3','5B10','5B11','5B12']
    shear_B =   [0.3 for n in names_B]
    draw_B  =   [1,1,1,2,2,2]
    anneal_B =  [True for n in names_B]
    piezo_x_B = []
    piezo_y_B = []
    hexa_y_B  = [ -7 for n in names_B ] 

    # Row C
    names_C =   ['5C1','5C2','5C3','5C10','5C11','5C12']
    shear_C =   [1 for n in names_C]
    draw_C  =   [1,1,1,2,2,2]
    anneal_C =  [True for n in names_C]
    piezo_x_C = []
    piezo_y_C = []
    hexa_y_C  = [ -7 for n in names_C ] 

    # Row D
    names_D =   ['5D1','5D2','5D3','5D4','5D5','5D6','5D7','5D8','5D9','5D10','5D11','5D12','5D13','5D14','5D15']
    shear_D =   [3 for n in names_D]
    draw_D  =   [1,1,1,1.3,1.3,1.3,1.6,1.6,1.6,2,2,2,2.3,2.3,2.3]
    anneal_D =  [True for n in names_D]
    piezo_x_D = []
    piezo_y_D = []
    hexa_y_D  = [ -7 for n in names_D ] 

    # Row E
    names_E =   ['5E1','5E2','5E3','5E4','5E5','5E6','5E7','5E8','5E9','5E10','5E11','5E12','5E13','5E14','5E15']
    shear_E =   [10 for n in names_E]
    draw_E  =   [1,1,1,1.3,1.3,1.3,1.6,1.6,1.6,2,2,2,2.3,2.3,2.3]
    anneal_E =  [True for n in names_E]
    piezo_x_E = []
    piezo_y_E = []
    hexa_y_E  = [ 5 for n in names_E] 

    # Row F
    names_F =   ['5F1','5F2','5F3','5F4','5F5','5F6','5F7','5F8','5F9','5F10','5F11','5F12','5F13','5F14','5F15']
    shear_F =   [30 for n in names_F]
    draw_F  =   [1,1,1,1.3,1.3,1.3,1.6,1.6,1.6,2,2,2,2.3,2.3,2.3]
    anneal_F =  [True for n in names_F]
    piezo_x_F = []
    piezo_y_F = []
    hexa_y_F  = [ 5 for n in names_F] 
    
    # Row G
    names_G =   ['5G1','5G2','5G3','5G4','5G5','5G6','5G7','5G8','5G9','5G10','5G11','5G12','5G13','5G14','5G15']
    shear_G =   [100 for n in names_G]
    draw_G  =   [1,1,1,1.3,1.3,1.3,1.6,1.6,1.6,2,2,2,2.3,2.3,2.3]
    anneal_G =  [True for n in names_G]
    piezo_x_G = []
    piezo_y_G = []
    hexa_y_G  = [ 5 for n in names_G]

    # Combine lists
    names = names_A + names_B + names_C + names_D + names_E + names_F + names_G
    shear = shear_A + shear_B + shear_C + shear_D + shear_E + shear_F + shear_G
    draw = draw_A + draw_B + draw_C + draw_D + draw_E + draw_F + draw_G
    anneal = anneal_A + anneal_B + anneal_C + anneal_D + anneal_E + anneal_F + anneal_G
    piezo_x = piezo_x_A + piezo_x_B + piezo_x_C + piezo_x_D + piezo_x_E + piezo_x_F + piezo_x_G
    piezo_y = piezo_y_A + piezo_y_B + piezo_y_C + piezo_y_D + piezo_y_E + piezo_y_F + piezo_y_G
    hexa_y = hexa_y_A + hexa_y_B + hexa_y_C + hexa_y_D + hexa_y_E + hexa_y_F + hexa_y_G


    # Ranges the same for all samples
    # For line scan, make x_range last value = 1, i.e. x_range = [0, 100, 1]
    # For sample specific range one could use
    # if name == 'sample-for-which-to-change] x_range = [0, 150, 16] else [0, 1250, 51]

    y_range = [0, 1000, 201]
    x_range = [0, 1, 1]

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