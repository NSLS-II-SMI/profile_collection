def giwaxs_chaney_2021_3(t=1):

    # names = ['sam01', 'sam02', 'sam03', 'sam04', 'sam05', 'sam06', 'sam07', 'sam08', 'sam09', 'sam10', 'sam11', 'sam12', 'sam13',
    #          'sam14', 'sam15', 'sam17', 'sam18', 'sam19', 'sam20', 'sam21', 'sam22', 'sam23', 'sam24', 'sam25', 'sam26', 'sam27']
    # names = ['sam28', 'sam29', 'sam30', 'sam31', 'sam33', 'sam34', 'sam35', 'sam36', 'sam37', 'sam38', 'sam39', 'sam40', 'sam41',
    #          'sam42', 'sam43', 'sam44', 'sam45', 'sam46', 'sam47', 'sam50', 'sam51', 'sam52', 'sam53', 'sam54', 'sam55', 'sam56']
    # names = ['sam57', 'sam58', 'sam59', 'sam60', 'sam61', 'sam62', 'sam63', 'sam64', 'sam65', 'sam66', 'sam67', 'sam68', 'sam69',
    #          'sam70', 'sam73', 'sam74', 'sam77', 'sam78',    'S1',    'S2',   'S3',    'S4',   'S5']
    # names = [  'S6',    'S7',    'S8',    'S9',    'S10',   'S11',   'S12',   'S13',  'S14',  'S15' ]
    # names = [ 'JH-CGE',  'TT1',  'TT3',  'SC1',   'SC2',   'MO3',   'MO4',   'ZZ1']
    # names = [ '1MEO',   '1FS',  'N2200', '10MEO', '10FS',   '5FS',   '20MEO',  '20FS', '5MEO']

    names = ["T1", "T2", "O", "C2", "C1", "Wenhan1", "Wenhan2"]
    x_piezo = [51000, 48000, 38000, 26000, 14000, -6000, -17000]
    y_piezo = [7000, 7000, 7000, 7000, 7000, 7300, 7300]
    z_piezo = [2300, 2300, 2300, 2300, 2300, 2300, 2300]
    x_hexa = [9, 0, 0, 0, 0, 0, 0]

    assert len(x_piezo) == len(
        names
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})"
    assert len(x_piezo) == len(
        y_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})"
    assert len(x_piezo) == len(
        z_piezo
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})"
    assert len(x_piezo) == len(
        x_hexa
    ), f"Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})"

    waxs_arc = [10.6]
    angle = [0.11, 0.14]

    dets = [pil900KW, pil300KW]
    det_exposure_time(t, t)

    for name, xs, zs, ys, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, 0)

        yield from alignement_gisaxs(angle=0.11)

        ai0 = piezo.th.position
        det_exposure_time(t, t)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            for i, an in enumerate(angle):
                yield from bps.mv(piezo.x, xs + 200)
                yield from bps.mv(piezo.th, ai0 + an)
                name_fmt = "{sample}_14keV_ai{angl}deg_wa{waxs}"
                sample_name = name_fmt.format(
                    sample=name, angl="%3.2f" % an, waxs="%2.1f" % wa
                )
                sample_id(user_name="PT", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(piezo.th, ai0)






def swaxs_S_edge_2024_1(t=1):
    dets = [pil900KW, pil1M]

    names = [ "Si3N4_membrane",  "To",    "CB", "PM7_10mg_To"]
    x = [                38900, 21600,    -400,        -19400]
    y = [                -8150, -8030,   -7450,         -7100] 

    names = [ "CB", "PM7_10mg_To"]
    x = [     -400,        -19400]
    y = [    -7450,         -7100] 


    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist()+[2530, 2500, 2470, 2445])
    
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys-200, ys + 200, 67)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            # yield from bps.mv(energy, 2500)
            # yield from bps.sleep(2)
            # yield from bps.mv(energy, 2480)
            # yield from bps.sleep(2)
            # yield from bps.mv(energy, 2445)
                

    names = [ "Updownsweep_PM7_10mg_To"]
    x = [       -19400]
    y = [         -7100] 

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
    + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    
    waxs_arc = [0]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys-300, ys + 300, 67)
        xss = np.array([xs + 200])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()


        yss1 = np.linspace(ys-300, ys + 300, 67)
        xss1 = np.array([xs - 200])

        yss1, xss1 = np.meshgrid(yss1, xss1)
        yss1 = yss1.ravel()
        xss1 = xss1.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)


            for e, xsss, ysss in zip(energies[::-1], xss1, yss1):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            # yield from bps.mv(energy, 2500)
            # yield from bps.sleep(2)
            # yield from bps.mv(energy, 2480)
            # yield from bps.sleep(2)
            # yield from bps.mv(energy, 2445)
                






def swaxs_S_edge_2024_liquidcell_1(t=1):
    dets = [pil900KW, pil1M]

    names = [ "PM7_1mg_CB_1", "PM7_10mg_CB_3", "PM6_10mg_CB_2", "PM7_1mg_CB_1"]
    x = [               36450,           17300,          -3830,         -35000]
    y = [               -7821,           -7700,          -7400,          -6750] 

    names = ["Y6_CB_1", "Y6BO_CB_1"]
    x = [        38000,       20300]
    y = [        -4140,       -4000]

    names = ["Si3N4_membrane"]
    x = [        4900]
    y = [        -3232]


    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist()+[2530, 2500, 2470, 2445])
    
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys-0, ys + 0, 67)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)

    
    names = ["Y6_CB_1", "Y6BO_CB_1"]
    x = [        38000,       20300]
    y = [        -4140,       -4000] 

    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = [2445.0, 2460.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5, 2485.0, 2550.0]
    
    det_exposure_time(10, 10)

    
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys-0, ys + 0, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            name_fmt = "{sample}_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)




def waxs_S_edge_chris_2024_1(t=1):
    dets = [pil900KW, pil1M]

    names = ["A1_08", "W2_04"]
    x = [      38500,   32800]
    y = [      -8000,   -7800] 


    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    waxs_arc = [0, 20, 40]
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys, ys + 1500, 63)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)



def waxs_S_edge_chaney_2024_1(t=2):
    dets = [pil900KW, pil1M]

    names = ["Trmsn_14", "Trmsn_17", "Trmsn_18", "Trmsn_21", "Trmsn_22", "Trmsn_23", "Trmsn_26",  "Trmsn_29",  "Trmsn_30", "Trmsn_33", "Trmsn_34", "Trmsn_35","Trmsn_01", "Trmsn_03"]
    x = [         43300,      37000,      31400,      25400,      19500,      13900,       7300,        1000,       -5000,     -11000,     -17300,     -23300,    -29500,     -35800]
    y = [          4500,       4600,       4700,       4800,       4700,       4900,       5000,        5100,        5200,       5100,       5000,       5100,      5200,       5300] 


    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    waxs_arc = [0, 20, 40]
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys, ys + 1200, 63)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="TC", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)



def run_2024_11_13_night(t=1):
    # proposal_id("2024_1", "000000_McNeil_02")
    # yield from waxs_S_edge_chris_2024_1(t=t)

    proposal_id("2024_1", "314903_Chaney_02")
    yield from waxs_S_edge_chaney_2024_1(t=t)








def swaxs_S_edge_2024_liquidcell_chris(t=1):
    dets = [pil900KW, pil1M]

    names = ["L1_01", "L1_02", "L1_03"]
    x = [      35370,   16450,   -3250]
    y = [      -6000,   -6450,   -5950] 

    #reduced energy range
    names = ["L1_02a"]
    x = [      16300]
    y = [      -6450] 

    #reduced energy range
    names = ["L1_02b"]
    x = [      16600]
    y = [      -6450] 

    # names = ["L1_01", "L1_02"]
    # x = [      38150,   20050]
    # y = [      -3830,   -3490] 

    #reduced energy range
    names = ["L1_03a"]
    x = [       19800]
    y = [       -3490] 
    
    #Long energy range
    names = ["L1_03b"]
    x = [       20150]
    y = [       -3490]

    #Long energy range
    names = ["L1_03d"]
    x = [       20150]
    y = [       -3490] 

    #Long energy range
    names = ["L1_01e"]
    x = [       38200]
    y = [       -3530]

    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    

    # energies = [2450.0, 2455.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0,
    #             2479.5, 2480.0, 2480.5, 2483.0, 2485.0, 2487.5, 2490.0, 2492.5, 2495.0, 2500.0, 2510.0, 2520.0, 2530.0, 2540.0, 2550.0]
    

    energies = [2445.0, 2460.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0, 2479.5, 2485.0, 2550.0]
    

    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)
        

        yss = np.linspace(ys-0, ys + 0, len(energies))
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M, pdcurrent2]

            det_exposure_time(t, t)

            name_fmt = "{sample}_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)





def swaxs_S_edge_2024_liquidcell1ener_chris(t=1):
    dets = [pil900KW, pil1M]

    #Long energy range
    names = ["L1_01d"]
    x = [       38400]
    y = [       -3830] 

    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energie = 2550
    
    # energies = [2450.0, 2455.0, 2460.0, 2465.0, 2470.0, 2473.0, 2475.0, 2475.5, 2476.0, 2476.5, 2477.0, 2477.5, 2478.0, 2478.5, 2479.0,
    #             2479.5, 2480.0, 2480.5, 2483.0, 2485.0, 2487.5, 2490.0, 2492.5, 2495.0, 2500.0, 2510.0, 2520.0, 2530.0, 2540.0, 2550.0]
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)
        

        yss = np.linspace(ys-300, ys + 300, 30)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M, pdcurrent2]

            det_exposure_time(t, t)
            
            yield from bps.mv(energy, energie)

            name_fmt = "{sample}_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for xsss, ysss in zip(xss, yss):

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % energie, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="CM", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)



def waxs_S_edge_chaney_variousprs_2024_1(t=1):
    dets = [pil900KW, pil1M]

    prs0 = -1
    # yield from bps.mv(prs, prs0)


    # names = ["Trmsn_14", "Trmsn_17", "Trmsn_01", "Trmsn_03",
    #          "Trmsn_18", "Trmsn_21", "Trmsn_22", "Trmsn_23", "Trmsn_26",  "Trmsn_29",  "Trmsn_30", "Trmsn_33", "Trmsn_34", "Trmsn_35"]
    # x = [         12300,       5900,      -9600,     -16200,     
    #               31400,      25400,      19500,      13900,       7300,        1000,       -5000,     -11000,     -17300,     -23300]
    # y = [         -7400,      -7600,      -7300,      -7400,      
    #                5000,       5100,       5000,       5100,       5300,        5300,        5400,       5200,       5200,       5200] 

    # assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    # assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    # energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
    #             + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    # waxs_arc = [0, 20, 40]
    # waxs_arc = [0, 20]

    # for name, xs, ys in zip(names, x, y):
    #     yield from bps.mv(piezo.x, xs,
    #                       piezo.y, ys)

    #     yss = np.linspace(ys, ys + 1200, 63)
    #     xss = np.array([xs])

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)
    #         if wa == 0:
    #             dets = [pil900KW]
    #         else:
    #             dets = [pil900KW, pil1M]

    #         det_exposure_time(t, t)

    #         name_fmt = "{sample}_prs0deg_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
    #         for e, xsss, ysss in zip(energies, xss, yss):
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(2)
    #             if xbpm2.sumX.get() < 50:
    #                 yield from bps.sleep(2)
    #                 yield from bps.mv(energy, e)
    #                 yield from bps.sleep(2)

    #             yield from bps.mv(piezo.y, ysss)
    #             yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm3.sumX.get()

    #             sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
    #             sample_id(user_name="TC", sample_name=sample_name)
    #             print(f"\n\t=== Sample: {sample_name} ===\n")

    #             yield from bp.count(dets, num=1)

    #         yield from bps.mv(energy, 2500)
    #         yield from bps.sleep(2)
    #         yield from bps.mv(energy, 2480)
    #         yield from bps.sleep(2)
    #         yield from bps.mv(energy, 2445)


    # yield from bps.mv(prs, prs0+35)

    # names = ["Trmsn_14", "Trmsn_17", "Trmsn_01", "Trmsn_03",
    #          "Trmsn_18", "Trmsn_21", "Trmsn_22", "Trmsn_23", "Trmsn_26",  "Trmsn_29",  "Trmsn_30", "Trmsn_33", "Trmsn_34", "Trmsn_35"]
    # x = [         14300,       7900,      -7800,     -14400,     
    #               33400,      27400,      21500,      15900,       9300,        3000,       -3100,      -9100,     -15500,     -21700]
    # y = [         -7400,      -7600,      -7300,      -7400,      
    #                5000,       5100,       5000,       5100,       5300,        5300,        5400,       5200,       5200,       5200] 

    # assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    # assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    # energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
    #             + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    # waxs_arc = [0, 20, 40]
    # waxs_arc = [0, 20]

    # for name, xs, ys in zip(names, x, y):
    #     yield from bps.mv(piezo.x, xs,
    #                       piezo.y, ys)

    #     yss = np.linspace(ys, ys + 1200, 63)
    #     xss = np.array([xs])

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)
    #         if wa == 0:
    #             dets = [pil900KW]
    #         else:
    #             dets = [pil900KW, pil1M]

    #         det_exposure_time(t, t)

    #         name_fmt = "{sample}_prs35deg_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
    #         for e, xsss, ysss in zip(energies, xss, yss):
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(2)
    #             if xbpm2.sumX.get() < 50:
    #                 yield from bps.sleep(2)
    #                 yield from bps.mv(energy, e)
    #                 yield from bps.sleep(2)

    #             yield from bps.mv(piezo.y, ysss)
    #             yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm3.sumX.get()

    #             sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
    #             sample_id(user_name="TC", sample_name=sample_name)
    #             print(f"\n\t=== Sample: {sample_name} ===\n")

    #             yield from bp.count(dets, num=1)

    #         yield from bps.mv(energy, 2500)
    #         yield from bps.sleep(2)
    #         yield from bps.mv(energy, 2480)
    #         yield from bps.sleep(2)
    #         yield from bps.mv(energy, 2445)



    # yield from bps.mv(prs, prs0+55)

    # names = ["Trmsn_14", "Trmsn_17", "Trmsn_01", "Trmsn_03",
    #          "Trmsn_18", "Trmsn_21", "Trmsn_22", "Trmsn_23", "Trmsn_26",  "Trmsn_29",  "Trmsn_30", "Trmsn_33", "Trmsn_34", "Trmsn_35"]
    # x = [         16600,      10200,      -5700,     -12400,     
    #               36100,      29900,      23900,      18000,      11600,        5000,       -1100,      -7000,     -13600,     -19900]
    # y = [         -7400,      -7600,      -7300,      -7400,      
    #                5000,       5100,       5000,       5100,       5300,        5300,        5400,       5200,       5200,       5200] 

    # assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    # assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    # energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
    #             + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    # waxs_arc = [0, 20, 40]
    # waxs_arc = [0, 20]

    # for name, xs, ys in zip(names, x, y):
    #     yield from bps.mv(piezo.x, xs,
    #                       piezo.y, ys)

    #     yss = np.linspace(ys, ys + 1200, 63)
    #     xss = np.array([xs])

    #     yss, xss = np.meshgrid(yss, xss)
    #     yss = yss.ravel()
    #     xss = xss.ravel()

    #     for wa in waxs_arc:
    #         yield from bps.mv(waxs, wa)
    #         if wa == 0:
    #             dets = [pil900KW]
    #         else:
    #             dets = [pil900KW, pil1M]

    #         det_exposure_time(t, t)

    #         name_fmt = "{sample}_prs55deg_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
    #         for e, xsss, ysss in zip(energies, xss, yss):
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(2)
    #             if xbpm2.sumX.get() < 50:
    #                 yield from bps.sleep(2)
    #                 yield from bps.mv(energy, e)
    #                 yield from bps.sleep(2)

    #             yield from bps.mv(piezo.y, ysss)
    #             yield from bps.mv(piezo.x, xsss)

    #             bpm = xbpm3.sumX.get()

    #             sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
    #             sample_id(user_name="TC", sample_name=sample_name)
    #             print(f"\n\t=== Sample: {sample_name} ===\n")

    #             yield from bp.count(dets, num=1)

    #         yield from bps.mv(energy, 2500)
    #         yield from bps.sleep(2)
    #         yield from bps.mv(energy, 2480)
    #         yield from bps.sleep(2)
    #         yield from bps.mv(energy, 2445)



    # names = ["Trmsn_14", "Trmsn_17", "Trmsn_01", "Trmsn_03",
    #          "Trmsn_18", "Trmsn_21", "Trmsn_22", "Trmsn_23", "Trmsn_26",  "Trmsn_29",  "Trmsn_30", "Trmsn_33", "Trmsn_34", "Trmsn_35"]
    # x = [         14300,       7900,      -7800,     -14400,     
    #               33400,      27400,      21500,      15900,       9300,        3000,       -3100,      -9100,     -15500,     -21700]
    # y = [         -7400,      -7600,      -7300,      -7400,      
    #                5000,       5100,       5000,       5100,       5300,        5300,        5400,       5200,       5200,       5200] 



    yield from bps.mv(prs, prs0+35)

    names = ["Trmsn_14",
             "Trmsn_22", "Trmsn_23", "Trmsn_26", "Trmsn_34", "Trmsn_35"]
    x = [         14300,     
                  21500,      15900,      9300,     -15500,     -21700]
    y = [         -7400,      
                   5000,       5100,       5300,       5200,       5200] 

    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    waxs_arc = [0, 20, 40]
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys, ys + 1200, 63)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_prs35deg_damagetest_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="TC", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)

def waxs_S_edge_chaney_variousprs_2024_1_march(t=2):
    dets = [pil900KW, pil1M]

    prs0 = -1
    yield from bps.mv(prs, prs0)


    names = ["SiN-0", "SiN-1", "SiN-2", "SiN-3", "SiN-4", "SiN-7",  "SiN-8",  "SiN-9", "SiN-10", "SiN-11"]
    x =     [  35044,   29044,   23544,   17544,   11044,    5044,    -1255,    -7255,   -13455,   -18956]
    y =     [  -3648,   -3648,   -3648,   -3848,   -4048,   -3848,    -3848,    -3848,    -3848,    -3848] 

    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    waxs_arc = [0, 20, 40]
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys, ys + 1200, 63)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_prs0deg_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="TC", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)


    yield from bps.mv(prs, prs0+35)

    names = ["SiN-0", "SiN-1", "SiN-2", "SiN-3", "SiN-4", "SiN-7",  "SiN-8",  "SiN-9", "SiN-10", "SiN-11"]
    x =     [  34544,   28544,   22644,   16643,  10394,     4394,    -1606,    -7855,   -14105,   -19855]
    y =     [  -3648,   -3648,   -3448,   -3848,  -3848,    -3848,    -3648,    -3848,    -3848,    -3648] 

    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    waxs_arc = [0, 20, 40]
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys, ys + 1200, 63)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_prs35deg_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="TC", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)



    yield from bps.mv(prs, prs0+55)

    names = ["SiN-0", "SiN-1", "SiN-2", "SiN-3", "SiN-4", "SiN-7",  "SiN-8",  "SiN-9", "SiN-10", "SiN-11"]
    x =     [  33500,   27399,   21549,   15550,    9150,    3149,    -2850,    -9050,   -15300,   -21050]
    y =     [  -3448,   -3448,   -3248,   -3848,   -3848,   -3848,    -3648,    -3848,    -3848,    -3648] 

    assert len(x) == len(y), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(y)})"
    assert len(x) == len(names), f"Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})"

    energies = (np.arange(2445, 2470, 5).tolist()+ np.arange(2470, 2480, 0.25).tolist()+ np.arange(2480, 2490, 1).tolist()
                + np.arange(2490, 2500, 5).tolist()+ np.arange(2500, 2560, 10).tolist())
    waxs_arc = [0, 20, 40]
    waxs_arc = [0, 20]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs,
                          piezo.y, ys)

        yss = np.linspace(ys, ys + 1200, 63)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            if wa == 0:
                dets = [pil900KW]
            else:
                dets = [pil900KW, pil1M]

            det_exposure_time(t, t)

            name_fmt = "{sample}_prs55deg_sdd1.8m_{energy}eV_wa{wax}_bpm{xbpm}"
            for e, xsss, ysss in zip(energies, xss, yss):
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)
                if xbpm2.sumX.get() < 50:
                    yield from bps.sleep(2)
                    yield from bps.mv(energy, e)
                    yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm3.sumX.get()

                sample_name = name_fmt.format(sample=name, energy="%6.2f" % e, wax=wa, xbpm="%4.3f" % bpm)
                sample_id(user_name="TC", sample_name=sample_name)
                print(f"\n\t=== Sample: {sample_name} ===\n")

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2500)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2480)
            yield from bps.sleep(2)
            yield from bps.mv(energy, 2445)



    names = ["Trmsn_14", "Trmsn_17", "Trmsn_01", "Trmsn_03",
             "Trmsn_18", "Trmsn_21", "Trmsn_22", "Trmsn_23", "Trmsn_26",  "Trmsn_29",  "Trmsn_30", "Trmsn_33", "Trmsn_34", "Trmsn_35"]
    x = [         14300,       7900,      -7800,     -14400,     
                  33400,      27400,      21500,      15900,       9300,        3000,       -3100,      -9100,     -15500,     -21700]
    y = [         -7400,      -7600,      -7300,      -7400,      
                   5000,       5100,       5000,       5100,       5300,        5300,        5400,       5200,       5200,       5200] 