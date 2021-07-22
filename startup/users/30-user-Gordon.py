
def alignement_gordon_2021_1():
    global names, x_piezo, z_piezo, incident_angles, y_piezo_aligned
    
    # names =   ['p3ht', 'p3rse', 'p3rt', 'p3rte', 'p3ht_doped', 'p3rse_doped', 'p3rt_doped', 'p3rte_doped']
    # x_piezo = [ 50000,  37000,   25000,   10000,        -7000,        -22000,       -37000,        -48000]
    # y_piezo = [  6800,   6800,   6800,     6800,         6800,          6800,         6800,          6800]
    # z_piezo = [ -1300,  -1300,   -1300,   -1300,          700,           700,          700,           700]

    # incident_angles = [-0.130468, -0.005243, -0.097427, 0.132971,    0.179, -0.008362, 0.036502, 0.020989]
    # y_piezo_aligned = [ 6641.484,  6689.479,   6755.62, 6802.845, 6888.982,  6995.038, 7078.288, 7129.521]


    names =   ['p3rse_2',  'p3rse_doped_2']
    x_piezo = [  36000,         -23000]
    y_piezo = [   6800,           6800]
    z_piezo = [  -1300,            700]

    incident_angles = [-0.005243,-0.008362]
    y_piezo_aligned = [ 6689.479,   6995.038]


    # smi = SMI_Beamline()
    # yield from smi.modeAlignment(technique='gisaxs')

    # for name, xs_piezo, ys_piezo, zs_piezo in zip(names, x_piezo, y_piezo, z_piezo):
    #     yield from bps.mv(piezo.x, xs_piezo)
    #     yield from bps.mv(piezo.y, ys_piezo)
    #     yield from bps.mv(piezo.z, zs_piezo)

    #     yield from alignement_gisaxs_multisample(angle = 0.1)

    #     incident_angles = incident_angles + [piezo.th.position]
    #     y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    # yield from smi.modeMeasurement()

    # print(incident_angles)



def run_gordon_2021_1(t=1): 
   
    waxs_range = np.linspace(0, 26.0, 5)
    dets = [pil300KW, pil1M]

    for name, xs, zs, aiss, ys in zip(names, x_piezo, z_piezo, incident_angles, y_piezo_aligned):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, aiss)

        ai0 = piezo.th.position

        # yield from bps.mvr(piezo.th, angl)
        name_fmt = '{sample}_16.1keV_ai{angle}deg_wa{wax}'

        det_exposure_time(t,t)
        angl = [0.12, 0.15, 0.2]

        for wa in waxs_range:
            yield from bps.mv(waxs, wa)
            for i, ang in enumerate(angl):
                yield from bps.mv(piezo.th, ai0 + ang)
                yield from bps.mv(piezo.x, xs + i * 200)

                sample_name = name_fmt.format(sample=name, angle='%3.2f'%ang, wax = '%2.1f'%wa)
                sample_id(user_name='MG', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3)



def waxs_S_edge_gordon_2021_2(t=1):
    dets = [pil300KW]

    # names = ['pbTTT_neat', 'p3RT_neat', 'pbTTT_dopped', 'p3RT_dopped']
    # x = [   26200, 20400, 14100, 7300]
    # y = [     700,   500,   900,  500]
    

    names = ['p3RT_dopped']
    x = [  7300]
    y = [   500]

    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(0, 39, 7)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 400, 31)
        xss = np.array([xs, xs + 400])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)

            det_exposure_time(t,t)

            if wa == 0 and name != 'pbTTT_neat':
                yield from bps.mv(energy, 2450)
                name_fmt = 'int_cor_{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
                for e, xsss, ysss in zip(energies, xss, yss): 
                    yield from bps.sleep(0.5)

                    yield from bps.mv(piezo.y, ysss)
                    yield from bps.mv(piezo.x, xsss)

                    bpm = xbpm2.sumX.value
                    sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                    sample_id(user_name='GF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')

                    yield from bp.count(dets, num=1)


            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                yield from bps.mv(energy, e)
                yield from bps.sleep(2)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


def gordon_saxswaxs_2021_2(t=1):
    dets = [pil300KW, pil1M]

    waxs_arc = np.linspace(0, 32.5, 6)

    # names = ['pbTTT_neat', 'p3RT_neat', 'pbTTT_dopped', 'p3RT_dopped']
    # x = [   24600, 19300, 14500, 7700]
    # y = [    6800,  6800,  6900, 7400]


    names = ['pbTTT_dopped']
    x = [   14500]
    y = [   6900]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            xss = [0, -300]

            det_exposure_time(t,t) 
            name_fmt = '{sample}_16.1keV_pos{pos}_wa{wax}_sdd1.6m'
            for k, xsss in enumerate(xss):
                yield from bps.mv(piezo.x, xs + xsss)

                sample_name = name_fmt.format(sample=name, pos = k, wax = wa)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)




def gisaxs1_gordon_2021_2(t=1): 
    
    # names = ['sample02', 'sample03', 'sample06', 'sample07', 'sample10', 'sample12', 'sample14', 'sample15','sample18']
    # x_piezo = [55000, 40000, 25000, 12000, -3000,-18000,-33000,-45000,-55000]
    # y_piezo = [ 6800,  6800,  6800,  6800,  6800,  6800,  6800,  6800,  6800]
    # z_piezo = [    0,     0,     0,     0,     0,     0,     0,     0,     0]
    # x_hexa =  [    0,     0,     0,     0,     0,     0,     0,     0,    -4]

    names = ['sample20', 'sample21', 'sample23', 'sample24', 'sample27', 'sample28']
    x_piezo = [55000, 47000, 33000, 18000,  3000,-12000]
    y_piezo = [ 6800,  6800,  6800,  6800,  6800,  6800]
    z_piezo = [    0,     0,     0,     0,     0,     0]
    x_hexa =  [    5,     0,     0,     0,     0,     0]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(x_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})'

    waxs_arc = [0, 2, 19.5, 21.5, 39, 41]
    angle = [0.1, 0.15, 0.2]

    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t,t)

    for name, xs, zs, ys, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, 0)
        
        yield from alignement_gisaxs(angle = 0.15)

        ai0 = piezo.th.position
        det_exposure_time(t,t)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)  

            for an in angle:
                yield from bps.mv(piezo.th, ai0 + an)                
                name_fmt = '{sample}_sdd1.6m_14keV_ai{angl}deg_wa{waxs}'
                sample_name = name_fmt.format(sample=name, angl='%3.2f'%an, waxs='%2.1f'%wa)
                sample_id(user_name='PT', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)
            
            
            yield from bps.mv(piezo.th, ai0)


    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)



def gisaxs2_gordon_2021_2(t=1): 

    names = ['pedot_EHE_neat', 'pedot_EHE_FeCl3', 'pedot_EHE_rosy', 'pedot_OH_neat', 'pedot_OH_FeCl3', 'pedot_OH_rosy']
    x_piezo = [-23000, -31000, -40000, -48000, -53000, -12000]
    y_piezo = [  6800,   6800,   6800,   6800,   6800,   6800]
    z_piezo = [     0,      0,      0,      0,      0,      0]
    x_hexa =  [     0,      0,      0,      0,     -5,    -10]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(x_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})'

    waxs_arc = [0, 2, 19.5, 21.5, 39, 41]
    angle = [0.1, 0.15, 0.2]

    dets = [pil1M, pil900KW, pil300KW]
    det_exposure_time(t,t)

    for name, xs, zs, ys, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, 0)
        
        yield from alignement_gisaxs(angle = 0.15)

        ai0 = piezo.th.position
        det_exposure_time(t,t)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)  

            for an in angle:
                yield from bps.mv(piezo.th, ai0 + an)                
                name_fmt = '{sample}_sdd1.6m_14keV_ai{angl}deg_wa{waxs}'
                sample_name = name_fmt.format(sample=name, angl='%3.2f'%an, waxs='%2.1f'%wa)
                sample_id(user_name='PT', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)
            
            
            yield from bps.mv(piezo.th, ai0)


    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)


def giwaxs_several(t=1):
    yield from gisaxs1_gordon_2021_2(t=t)

    yield from bps.sleep(5)
    proposal_id('2021_2', '307830_Su6')
    yield from gisaxs2_gordon_2021_2(t=t)