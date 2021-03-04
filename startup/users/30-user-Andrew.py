def giwaxs_andrew(t=1):
    #sample alignement
    global names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, xs_hexa
    names = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'Si_big', 'S9', 'S10',   'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23']
    x_piezo = [59000,52000,39000,27000,14000,2000,-11000,-23000,-35000,-49000,-58000,   59000,54000,42000,28000,17000,4000,-7000,-17000,-27000,-38000,-48000,-58000,-58000 ]
    y_piezo = [6900,6900,6900,6900,6900,6900,6900,6900,6900,6900,6900,   -1800,-1800,-1800,-1800,-1800,-1800,-1800,-1800,-1800,-1800,-1800,-1800,-1800 ]
    z_piezo = [ 0,0,0,0,0,0,0,0,0,0,0,    5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000]
    x_hexa =  [ 6,0,0,0,0,0,0,0,0,0,-4,   6,0,0,0,0,0,0,0,0,0,0,0,-10]

    incident_angles = [0.104651,  -0.10827, 0.125697, 0.646015, -1.634348, 0.492098, 0.200656, 0.646859, 0.092759, 0.073346, 0.168562,
    -0.518632, -0.439084]
    y_piezo_aligned = [6915.668,  6943.117, 6938.048, 6906.885,  6818.453,  6895.66, 6896.007, 6869.887, 6883.025, 6866.073, 6883.329,
    -1835.888, -1835.596]

    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique='gisaxs')

    for name, xs_piezo, zs_piezo, ys_piezo, xs_hexa in zip(names[13:], x_piezo[13:], z_piezo[13:], y_piezo[13:], x_hexa[13:]):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)
        yield from bps.mv(piezo.z, zs_piezo)
        yield from bps.mv(piezo.th, -0.5)

        yield from alignement_gisaxs_multisample_special(angle = 0.08)

        incident_angles = incident_angles + [piezo.th.position]
        y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    yield from smi.modeMeasurement()

    print(incident_angles)
    print(y_piezo_aligned)

    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(1)
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(1)
    

    dets = [pil300KW]
    waxs_arc = np.linspace(0, 26, 5)
    angle = [0.1, 0.12, 0.15]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    

        for name, xs, zs, aiss, ys, xs_hexa in zip(names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, x_hexa):
            yield from bps.mv(stage.x, xs_hexa)
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            yield from bps.mv(piezo.z, zs)
            yield from bps.mv(piezo.th, aiss)

            det_exposure_time(t,t) 
            name_fmt = '{sample}_ai{angle}deg_wa{waxs}'

            for num, an in enumerate(angle):
                yield from bps.mv(piezo.th, aiss + an)
                yield from bps.mv(piezo.x, xs - num * 300)

                sample_name = name_fmt.format(sample=name, angle='%3.2f'%an, waxs='%2.1f'%wa)
                sample_id(user_name='PT', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)




def Andrew_temp_2021_1(tim=0.5): 
    temperatures = [105, 145, 190]
    name = 'GF'

    # names = ['sample04', 'sample07', 'sample10', 'sample14', 'sample03', 'sample06', 'sample11', 'sample15']
    # x_piezo  = [     47500,      32500,      20000,       6000,      -5000,     -19000,     -32000,     -44000]
    # y_piezo =  [      7000,       7000,       7000,       7000,       7000,       7000,       7000,       7000]
    # assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of Y coordinates ({len(y_list)})'
    # assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    
    #Detectors, motors:
    dets = [pil300KW] #ALL detectors

    waxs_arc = np.linspace(0, 26, 5)
    angle = [0.1, 0.12, 0.15]

    name_fmt = '{sample}_ai{angle}_{temperature}C_wa{waxs}'

    det_exposure_time(tim, tim)
    for i_t, t in enumerate(temperatures):
        
        t_kelvin = t + 273.15
        print(t_kelvin)
        yield from ls.output1.mv_temp(t_kelvin)

        temp = ls.input_A.value
        while abs(temp - t_kelvin) > 1:
            print(abs(temp - t_kelvin))
            yield from bps.sleep(10)
            temp = ls.input_A.get()

        t_celsius = temp - 273.15

        yield from quick_alignement_tscan()

        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            for i, (name, xs_piezo, ys_piezo, aiss) in enumerate(zip(names, x_piezo, y_piezo_aligned, incident_angles)):
                yield from bps.mv(piezo.x, xs_piezo)
                yield from bps.mv(piezo.y, ys_piezo)
                yield from bps.mv(piezo.th, aiss)

                for num, an in enumerate(angle):
                    yield from bps.mv(piezo.th, aiss + an)
                    yield from bps.mv(piezo.x, xs_piezo - num * 300)

                    sample_name = name_fmt.format(sample=name, angle='%3.2f'%an, temperature='%3.1f'%t, waxs='%2.1f'%wa)

                    sample_id(user_name='PT', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')

                    yield from bp.count(dets, num=1)


    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)
    yield from ls.output1.mv_temp( 28 + 273.13)



def full_alignement_tscan(t=1):
    #sample alignement
    global names, x_piezo, incident_angles, y_piezo_aligned
    names = ['sample04', 'sample07', 'sample10', 'sample14', 'sample03', 'sample06', 'sample11', 'sample15']
    x_piezo = [   47500,      32500,      20000,       6000,      -5000,     -19000,     -32000,     -44000]
    y_piezo = [    7000,       7000,       7000,       7000,       7000,       7000,       7000,       7000]

    incident_angles = []
    y_piezo_aligned = []

    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique='gisaxs')

    for name, xs_piezo, ys_piezo in zip(names, x_piezo, y_piezo):
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)

        yield from alignement_gisaxs_multisample(angle = 0.08)

        incident_angles = incident_angles + [piezo.th.position]
        y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    yield from smi.modeMeasurement()

    print(incident_angles)
    print(y_piezo_aligned)

    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(1)
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(1)


def quick_alignement_tscan():
    # incident_angles = [0.0499, 0.10198, 0.126005, 0.65, 0.173994, 0.205969, 0.205972, 0.173947] 
    # y_piezo_aligned = [6784.191, 6946.063, 6947.799, 6860.963, 6952.249, 6951.685, 6951.321, 6946.413]
    
    yield from bps.mv(GV7.open_cmd, 1 )
    yield from bps.sleep(1)
    yield from bps.mv(GV7.open_cmd, 1 )
    yield from bps.sleep(1)

    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique='gisaxs')

    for i, (name, xs_piezo, ys_piezo, aiss) in enumerate(zip(names, x_piezo, y_piezo_aligned, incident_angles)):
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)
        yield from bps.mv(piezo.th, aiss)

        yield from quick_alignement_gisaxs_multisample(angle = 0.08)

        incident_angles[i] = piezo.th.position
        y_piezo_aligned[i] = piezo.y.position

    yield from smi.modeMeasurement()

    print(incident_angles)
    print(y_piezo_aligned)

    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(1)
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(1)