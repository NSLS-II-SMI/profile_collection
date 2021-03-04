#Align GiSAXS sample
import numpy as np



def mapping_saxs_Thed(t=1): 
    samples = ['PT10E-001La','PT10E-001M','PT10E-001G','PT10E-001H','PT10E-001I']
    x_list = [-45700,-45700,-17600,-2600,27200]
    y_list = [-1900,5200,-2600,-1600,-2900]
    
    name = 'PT'
    
    x_range=[[0, 26000, 261], [0, 26000, 261], [0, 10100, 102], [0, 24400, 245],  [0, 18100, 182]]
    y_range=[[0, 0, 1], [0, 1000, 11], [0, 8500, 86], [0, 8000, 81], [0, 9300, 94]]
    
    
    # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name=name, sample_name=sample) 
        yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r, 0)

    #     for yrs in np.linspace(y_r[0], y_r[1], y_r[2]):
    #         yield from bps.mv(piezo.y, y+yrs)
    #         for xrs in np.linspace(x_r[0], x_r[1], x_r[2]):
    #             yield from bps.mv(piezo.x, x+xrs)
    #             name_fmt = '{sam}_x{x}_y{y}'
    #             sample_name = name_fmt.format(sam=sample, x='%6.6d'%(x+xrs), y='%6.6d'%(y+yrs))
    #             sample_id(user_name=name, sample_name=sample_name) 
    #             #print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.count(dets, num=1)
        
    # #yield from bp.rel_grid_scan(dets, piezo.x, *x_r, piezo.y, *y_r, 0) #1 = snake, 0 = not-snake
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def mapping2_saxs_Thed(t=1): 
    samples = ['PT10E-001A','PT10E-001B','PT10E-001C','PT10E-001D','PT10E-001E', 'PT10E-001F']
    x_list = [37500, 28000, 10100, -4600,-17500, -37100]
    y_list = [-2800, -3100, -2800, 0, -400, -2100]
    
    name = 'PT'
    
    x_range=[[0, 9200, 93], [0, 5000, 51], [0, 14000, 141], [0, 8300, 84],  [0, 6900, 70], [0, 14600, 147]]
    y_range=[[0, 7000, 71], [0, 9600, 97], [0, 9000, 91], [0, 6500, 66], [0, 6900, 70], [0, 7500, 76]]
    
    
    # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name=name, sample_name=sample) 
        yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r, 0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def mapping3_saxs_Thed(t=1): 
    samples = ['PT10E-001B','PT10E-001C','PT10E-001D','PT10E-001E', 'PT10E-001F', 'PT10E-001J']
    x_list = [34000, 12700, 1100, -9800,-28600, -42600]
    y_list = [0, -3000, -3100, -2600, -3200, -2400]
    
    name = 'PT'
    
    x_range=[[0, 10000, 101],[0, 15600, 157], [0, 7000, 71], [0, 7000, 71],  [0, 14000, 141], [0, 14600, 147]]
    y_range=[[0, 4500, 46], [0, 9000, 91], [0, 7000, 71], [0, 6500, 66], [0, 6700, 68], [0, 6500, 66]]
    
    
    # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name=name, sample_name=sample) 
        yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r, 0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)




def capillaries_saxs_Thed(t=1): 
    samples = ['LT666','LT670','LT671','LT671-2','LT672', 'LT673','LT676','LT677','LT678','LT679', 'LT679-2','LT679-3','LT680','LT682',
    'LT683','LT684', 'LT686','LT690', 'LT691']
    
    x_list = [39300, 32900,26500,20200, 13900, 7500, 1000, -5400, -11600, -18100, -24300, -30700, -37100, -43300, 36000, 29900, 23300, 17300, 10800]
    y_list = [3100, 3100, 3100,3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100, 3100]
    z_list = [2600,2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 11600, 11600, 11600, 11600, 11600]

  # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for x, y, z, sample in zip(x_list, y_list, z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)

        sample_id(user_name='PT_2ndseries', sample_name=sample) 
        yield from bp.count(dets, num=10)
   
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)


def gisaxs_Thed1(t=1): 
    samples = ['FY5','FY6','FY7','FY8','FY9', 'FY10','FY11','FY12','FY13','FY14']
    
    x_list = [-48000, -34000,-23000,-13000, -3000, 9000, 17000, 27000, 38000, 50000]

    waxs_arc = np.linspace(0, 58.5, 10)
    angle = [0.1, 0.15, 0.2]

  # Detectors, motors:
    dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for x, sample in zip(x_list,samples):
        yield from bps.mv(piezo.x, x)

        sample_id(user_name='PT_gisaxs', sample_name=sample) 

        yield from alignement_gisaxs(0.08)
        
        det_exposure_time(t, t) 
        name_fmt = '{sample}_ai{angle}deg_wa{waxs}'
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            
            for an in angle:
                yield from bps.mvr(piezo.th, an)
                sample_name = name_fmt.format(sample=sample, angle='%3.2f'%an, waxs='%2.1f'%wa)
                sample_id(user_name='PT', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=2)
                yield from bps.mvr(piezo.th, -an)                   
                

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)



def saxs_well_Thed_2021(t=1): 
    samples = [
    'bkg19',      'PT10E_019A', 'PT10E_019B', 'PT10E_019C', 'PT10E_019D', 'PT10E_019E',
    'PT10E_019F', 'PT10E_019G', 'PT10E_019H', 'PT10E_019I', 'PT10E_019J', 'PT10E_019K',
    'PT10E_019L', 'PT10E_019M', 'PT10E_019N', 'PT10E_019O', 'PT10E_019P', 'PT10E_019Q',
    'PT10E_019R', 'PT10E_019S', 'PT10E_019T', 'PT10E_019U', 'PT10E_019V', 'PT10E_019W',

                  'PT10E_024A', 'PT10E_024B', 'PT10E_024C', 'PT10E_024D', 'PT10E_024E',
    'PT10E_024F', 'PT10E_024G', 'PT10E_024H', 'PT10E_024I', 'PT10E_024J', 'PT10E_024K',
    'PT10E_024L', 'PT10E_024M', 'PT10E_024N', 'PT10E_024O', 'PT10E_024P', 'PT10E_024Q']

    x_list = [
       56600,  47300,  38300,  29500,  20500,  11500,
       56600,  47300,  38600,  29600,  20700,  11500,
       56500,  47300,  38400,  29500,  20800,  12000,
       56300,  47300,  38400,  29600,  20600,  12000,

              -18000, -27000, -36000, -44500, -54000,
       -9500, -17500, -26500, -35500, -44500, -54900,
       -9000, -18000, -27000, -36000, -45000, -54000]

    y_list = [
       -7100,  -6200,  -6200,  -6800,  -6800,  -6800, 
       -1500,  -1700,  -1800,  -1800,  -1600,  -1600,
        3300,   3800,   3600,   3400,   3800,   3800,
        8800,   8800,   8800,   8700,   8700,   8800,

               -7400,  -7400,  -7400,  -7400,  -7400, 
        -1700, -1700,  -1700,  -1700,  -1700,  -1700,
         3800,  3800,   3800,   3800,   3800,   3800]

    waxs_arc = np.linspace(13, 13, 1)

  # Detectors, motors:
    dets = [pil1M]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_list)})'

    for j, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
    
        for x, y, sample in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            sample_id(user_name='PT', sample_name=sample) 
            
            det_exposure_time(t, t) 
            name_fmt = '{sample}_sdd5m_14keV_wa{waxs}'

            sample_name = name_fmt.format(sample=sample, waxs='%2.1f'%wa)
            sample_id(user_name='PT', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.count(dets, num=1)
                

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)



def saxs_well_rot_Thed_2021(t=1): 
    waxs_arc = np.linspace(0, 58.5, 10)
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)
   
    for j, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
    

        samples = ['PT10E_019H_0deg', 'PT10E_019J_0deg', 'PT10E_019K_0deg', 'PT10E_019M_0deg', 'PT10E_019N_0deg', 'PT10E_019P_0deg', 'PT10E_019T_0deg', 'PT10E_019U_0deg']
        x_list = [        26200,         8200,         -800,        35000,        26000,         8400,        26000,        17500]
        y_list = [         -800,         -800,        -1000,         4700,         4400,         4600,         9500,         9600]
        assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
        assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_list)})'
        
        yield from bps.mv(prs, 0)
        for x, y, sample in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            
            name_fmt = '{sample}_wa{waxs}'
            sample_name = name_fmt.format(sample=sample, waxs='%2.1f'%wa)
            sample_id(user_name='PT', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.count(dets, num=1)
                

        samples = ['PT10E_019H_-30deg', 'PT10E_019J_-30deg', 'PT10E_019K_-30deg', 'PT10E_019M_-30deg', 'PT10E_019N_-30deg', 'PT10E_019P_-30deg', 'PT10E_019T_-30deg', 'PT10E_019U_-30deg']
        x_list = [        26800,         9600,          600,        35000,        26900,         9500,        27000,        18500]
        y_list = [         -800,         -800,        -1000,         4700,         4400,         4600,         9500,         9600]
        assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
        assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_list)})'

        yield from bps.mv(prs, -30)
        for x, y, sample in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            
            name_fmt = '{sample}_wa{waxs}'
            sample_name = name_fmt.format(sample=sample, waxs='%2.1f'%wa)
            sample_id(user_name='PT', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.count(dets, num=1)
    
        samples = ['PT10E_019H_30deg', 'PT10E_019J_30deg', 'PT10E_019K_30deg', 'PT10E_019M_30deg', 'PT10E_019N_30deg', 'PT10E_019P_30deg', 'PT10E_019T_30deg', 'PT10E_019U_30deg']
        x_list = [        25500,         7600,        -1800,        34200,        25400,         7500,        25200,        16700]
        y_list = [         -800,         -800,        -1000,         4700,         4400,         4600,         9600,         9600]
        assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
        assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(y_list)})'

        yield from bps.mv(prs, 30)
        for x, y, sample in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            
            name_fmt = '{sample}_wa{waxs}'
            sample_name = name_fmt.format(sample=sample, waxs='%2.1f'%wa)
            sample_id(user_name='PT', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.count(dets, num=1)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)

def gisaxs_Thed_2021_1(t=1): 
    
    global names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, xs_hexa

    # names =  ['FY01','FY02','FY03','FY04','FY05','FY06','FY07','FY08','FY09', 'FY10','FY11', 'FY12', 'FY13', 'FY14', 'FY15', 'FY16',]    
    # x_piezo = [60000, 53000, 45000, 38000, 31000, 22000, 15500,  9000,  1000, -7000, -17000, -27000, -36000, -44000, -52000, -60000,]
    # y_piezo = [ 6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,   6900,   6900,   6900,   6900,   6900,   6900,]
    # z_piezo = [    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,      0,      0,      0,      0,      0,      0,]   
    # x_hexa =  [    6,     6,     6,     6,     6,     6,     6,     6,     6,     0,      0,      0,      0,      0,      0,      0,]
    # incident_angles = [0.225457, 0.07311, 0.13644, 0.131744, 0.090663, 0.203624, 0.140589, 0.117837,
    # 0.066659, 0.060986, 0.083272, 0.055102, 0.472708, 0.080632, 0.063615]
    # y_piezo_aligned = [6674.616, 6664.133, 6655.723, 6652.42, 6628.407, 6619.978, 6615.386, 6607.622, 6604.918, 6625.53,
    # 6612.155, 6594.748, 6568.487, 6559.445, 6552.764, 6552.231]
    
    # names = ['FY32', 'FY33','FY34','FY35','FY36','DVC1', 'DVC2','DVC3','DVC4','DVC5','DVC6', 'DVC7',
    #     'FY17','FY18','FY19', 'FY20','FY21','FY22','FY23','FY24', 'FY25','FY26','FY27','FY28','FY29','FY30','FY31']
    
    # x_piezo = [58000, 45000, 34000, 28000, 24000, 13000, 2000, -13000,-25000,-40000,-47000, -55000, 
    #            58000, 45000, 31000, 25000, 19000, 13000,  5000, -1000, -8000, -7000,-14000, -27000, -44000, -55000, -60000]
    # y_piezo = [ 6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,   6900,
    #            -2200, -2200, -2200, -2200, -2200, -2200, -2200, -2200, -2200, -2200, -2200,  -2200,  -2200,  -2200,  -2200]
    # z_piezo = [    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,      0,
    #                0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,      0,      0,      0,      0]
    # x_hexa =  [    6,      6,    6,     6,     6,     6,     6,     6,     6,     6,     0,     -5,
    #                6,      6,    6,     6,     6,     6,     6,     6,     6,     0,     0,      0,     0,      0,      -5]


    # names = ['FY16', 'FY37','FY38','FY39','FY40', 'FY41', 'FY42','FY43','FY44','FY45', 'FY46','FY47','FY48', 'FY49','FY50',
    # 'FY51','FY52','FY53', 'FY54','FY55','FY56','FY57','FY58','FY59','FY60', 'FY61','FY62','FY63','FY64','FY65','FY66', 'FY67','FY68','FY69', 'DVC8']
    
    # x_piezo = [60000, 51000, 43000, 35500, 30500, 23000, 17500, 13200,  7000,  2000, -4000, -15000, -21500, -23000, -29000, -35000, -41000, -48000, -54000,
    #            60000, 48000, 35500, 29500, 25000, 21500, 17500, 13200,  8000, -6000,-15000, -17500, -29000, -38000, -48000, -56000]
    # y_piezo = [ 6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,  6900,   6900,   6900,   6900,   6900,   6900,   6900,   6900,   6900,
    #            -2200, -2200, -2200, -2200, -2200, -2200, -2200, -2200, -2200, -2200, -2200,  -2200,  -2200,  -2200,  -2200,  -2200]
    # z_piezo = [    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,      0,      0,      0,      0,      0,      0,      0,      0,
    #                0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,      0,      0,      0,      0,      0]
    # x_hexa =  [    7,     7,     7,     7,     7,     7,     7,     7,     7,     7,     7,      7,      7,      0,      0,      0,      0,      0,      0,
    #                7,     7,     7,     7,     7,     7,     7,     7,     7,     7,     7,      0,     0,       0,      0,     -5]


    names = ['DVC9', 'DVC10','DVC11','DVC12','DVC13', 'DVC14', 'DVC15','DVC16','DVC17','DVC18',
    'WEE1', 'WEE2', 'WEE3', 'WEE4','WEE5', 'WEE6']
    
    x_piezo = [58000, 43000, 29000, 15000,  1000,-11000,-18000,-32000,-46000,-58000,
               58000, 43000, 29000, 15000,  1000,-11000]
    y_piezo = [ 6200,  6200,  6200,  6200,  6200,  6200,  6200,  6200,  6200,  6200,
               -2900, -2900, -2900, -2900, -2900, -2900]
    z_piezo = [    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
                   0,     0,     0,     0,     0,     0]
    x_hexa =  [    7,     7,     7,     7,     7,     7,     0,     0,     0,    -4,
                   7,     7,     7,     7,     7,     7]


    incident_angles = []
    y_piezo_aligned = []


    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(x_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})'

    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique='gisaxs')

    for name, xs_piezo, zs_piezo, ys_piezo, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs_piezo)
        yield from bps.mv(piezo.y, ys_piezo)
        yield from bps.mv(piezo.z, zs_piezo)
        yield from bps.mv(piezo.th, 0)


        # if ys_piezo>0:
        yield from alignement_gisaxs_multisample(angle = 0.08)
        # else:
        #     yield from bps.mv(piezo.th, -1)
        #     yield from alignement_gisaxs_multisample_special(angle = 0.08)

        incident_angles = incident_angles + [piezo.th.position]
        y_piezo_aligned = y_piezo_aligned + [piezo.y.position]

    yield from smi.modeMeasurement()


    waxs_arc = np.linspace(0, 58.5, 10)
    angle = [0.1, 0.15, 0.2]

    dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    

        for name, xs, zs, aiss, ys, xs_hexa in zip(names, x_piezo, z_piezo, incident_angles, y_piezo_aligned, x_hexa):
            yield from bps.mv(stage.x, xs_hexa)
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            yield from bps.mv(piezo.z, zs)
            yield from bps.mv(piezo.th, aiss)
            
            for an in angle:
                yield from bps.mv(piezo.th, aiss + an)                
                name_fmt = '{sample}_sdd5m_14keV_ai{angl}deg_wa{waxs}'
                sample_name = name_fmt.format(sample=name, angl='%3.2f'%an, waxs='%2.1f'%wa)
                sample_id(user_name='PT', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)
                

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)





def capillaries_saxs_Thed_2021_1(t=1): 
    samples = ['LT830','LT830MB','LT830MB-1','LT831','LT831M', 'LT832','LT833','LT833-1','LT834','LT835', 'LT836','LT836-1','LT837','LT837-1',
    'LT838','LT840M', 'LT841M','LT842', 'LT842M','LT843', 'LT844-1','LT844-2', 'LT844-3', 'LT845', 'LT846-1', 'LT846-2']
    
    x_list = [39500, 32500, 26100, 19900, 13600, 7500, 1000, -5000, -12300, -18500, -24700, -31200, -37300,
    43200, 36400, 30000, 23300, 17200, 11000,  4000, -2950, -8050, -13700, -20350, -26500, -32650]
    y_list = [ 8000,  8000,  8000,  8000,  8000, 8000, 8000,  8000,   8000,   8000,   8000,   8000,   8000,
     8000,  8000,  8000,  8000,  8000,  8000,  8000,  8000,  8000,   8000,   8000,   8000,   8000]
    z_list = [  500,   500,   500,   500,   500,  500,  500,   500,    500,    500,    500,    500,    500, 
    10500, 10500, 10500, 10500, 10500, 10500, 10500, 10500, 10500,  10500,  10500,  10500,  10500]

  # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for x, y, z, sample in zip(x_list, y_list, z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)

        sample_id(user_name='PT_5m_14keV', sample_name=sample) 
        yield from bp.count(dets, num=10)
   
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)



def gisaxs_Thed2(t=1): 
    samples = ['FY1','FY2','FY3','FY4']
    
    x_list = [-41470, -22470, 2530, 27530]

    waxs_arc = np.linspace(13, 13, 1)
    angle = [0.1, 0.15, 0.2]

  # Detectors, motors:
    dets = [pil1M]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for x, sample in zip(x_list,samples):
        yield from bps.mv(piezo.x, x)
        sample_id(user_name='PT_gisaxs', sample_name=sample) 

        yield from alignement_gisaxs(0.08)
        
        det_exposure_time(t, t) 
        name_fmt = '{sample}_ai{angle}deg_wa{waxs}'
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            
            for an in angle:
                yield from bps.mvr(piezo.th, an)
                sample_name = name_fmt.format(sample=sample, angle='%3.2f'%an, waxs='%2.1f'%wa)
                sample_id(user_name='PT', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=2)
                yield from bps.mvr(piezo.th, -an)                   
                

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)


def saxs_well_Thed(t=1): 
    samples = ['PT10E_002AgB','PT10E_002A','PT10E_002B','PT10E_002C','PT10E_002D', 'PT10E_002E',
    'PT10E_002F','PT10E_002G','PT10E_002H','PT10E_002I','PT10E_002J','PT10E_002K',
    'PT10E_002L','PT10E_002M','PT10E_002N','PT10E_002O','PT10E_002P','PT10E_002Q',
    'PT10E_002R','PT10E_002S','PT10E_002T','PT10E_002U','PT10E_002V','PT10E_002W',
    'PT10E_003AgB','PT10E_003A','PT10E_003B','PT10E_003C','PT10E_003D', 
    'PT10E_003F','PT10E_003G', 'PT10E_003H','PT10E_003I','PT10E_003J',
    'PT10E_003L','PT10E_003M','PT10E_003N','PT10E_003O','PT10E_003P',
    'PT10E_003R','PT10E_003S','PT10E_003T','PT10E_003U','PT10E_003V']
    
    x_list = [44360, 35500, 26640,17880, 9030, 230,
    44360, 35500, 26640,17880, 9030, 230,
    44360, 35500, 26640,17880, 9030, 230,
    44360, 35500, 26640,17880, 9030, 230,
    -8970, -17770, -26570, -35370, -44170,
    -8970, -17770, -26570, -35370, -44170,
    -8970, -17770, -26570, -35370, -44170,
    -8970, -17770, -26570, -35370, -44170]

    y_list = [-6640, -6640,-6640,-6640, -6640, -6640, 
    -1400, -1400,-1400,-1400, -1400, -1400,
    3840, 3840,3840,3840, 3840, 3840,
    9080, 9080,9080,9080, 9080, 9080,
    -6640, -6640,-6640,-6640, -6640, -6640, 
    -1400, -1400,-1400,-1400, -1400, -1400,
    3840, 3840,3840,3840, 3840, 3840,
    9080, 9080,9080,9080, 9080, 9080]

    waxs_arc = np.linspace(0, 58.5, 10)

  # Detectors, motors:
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for j, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
    
        for x, y, sample in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            sample_id(user_name='PT', sample_name=sample) 
            
            det_exposure_time(t, t) 
            name_fmt = '{sample}_wa{waxs}'

                

            sample_name = name_fmt.format(sample=sample, waxs='%2.1f'%wa)
            sample_id(user_name='PT', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.count(dets, num=1)
                

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)


def saxs_well2_Thed(t=1): 
    samples = [#'PT10E_003E', 'PT10E_003K','PT10E_003Q', 'PT10E_003W',
    # 'PT10E_004AgB','PT10E_004A','PT10E_004B','PT10E_004C','PT10E_004D', 'PT10E_004E',
    # 'PT10E_004F','PT10E_004G','PT10E_004H','PT10E_004I','PT10E_004J','PT10E_004K',
    # 'PT10E_004L','PT10E_004M','PT10E_004N','PT10E_004O','PT10E_004P','PT10E_004Q',
    'PT10E_004R','PT10E_004S','PT10E_004T','PT10E_004U','PT10E_004V','PT10E_004W',
    ]
    
    x_list = [#19030, 19030, 19030, 19030,
    # 2530, -6270, -15070, -23870, -32670, -41470,
    # 2530, -6270, -15070, -23870, -32670, -41470,
    # 2530, -6270, -15070, -23870, -32670, -41470,
    2530, -6270, -15070, -23870, -32670, -41470,

    ]

    y_list = [#-7540, -2300, 2940, 8180, 
    # -6640, -6640,-6640,-6640, -6640, -6640, 
    # -1400, -1400,-1400,-1400, -1400, -1400,
    # 3840, 3840,3840,3840, 3840, 3840,
    9080, 9080,9080,9080, 9080, 9080,
    ]

    waxs_arc = np.linspace(13, 13, 1)

  # Detectors, motors:
    dets = [pil1M, pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for j, wa in enumerate(waxs_arc):
        yield from bps.mv(waxs, wa)
    
        for x, y, sample in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            sample_id(user_name='PT', sample_name=sample) 
            
            det_exposure_time(t, t) 
            name_fmt = '{sample}_wa{waxs}'

                

            sample_name = name_fmt.format(sample=sample, waxs='%2.1f'%wa)
            sample_id(user_name='PT', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.count(dets, num=1)
                

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)



def run_saxsmapPT(t=1): 
    samples = ['AS1-090','AS1-100']
    x_list = [12000, 33000]
    y_list = [1500, 1400]
    
    name = 'PT'
    
    x_range=[ [0,15000,61] , [0,12500,51] ]
    y_range=[ [-5000,5000,41] , [-3750,3750,16] ]
    
    
    # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name=name, sample_name=sample) 
        
        for xrs in np.linspace(x_r[0], x_r[1], x_r[2]):
            yield from bps.mv(piezo.x, x+xrs)
            for yrs in np.linspace(y_r[0], y_r[1], y_r[2]):
                print(yrs)
                yield from bps.mv(piezo.y, y+yrs)
                name_fmt = '{sam}_x{x}_y{y}'
                sample_name = name_fmt.format(sam=sample, x='%5.5d'%(x+xrs), y='%5.5d'%(y+yrs))
                sample_id(user_name=name, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
        
    #yield from bp.rel_grid_scan(dets, piezo.x, *x_r, piezo.y, *y_r, 0) #1 = snake, 0 = not-snake
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)

def run_waxslongPT(t=1): 
    dets = [pil300KW, pil1M]
    xlocs = [-38000,-33000,-20000,-8000, 5000, 18000, 31000]
    ylocs = [-8400,0,0,0,0,0,0]
    names = ['Se_50nm', 'Se_100nm', 'Se_200nm', 'Se_300nm', 'Se_400nm', 'Se_1000nm', 'Se_2000nm']
        
    det_exposure_time(t,t)     
    #what we run now
    assert len(curr_tray) == len(curr_names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    waxs_range = [0, 58.5, 10]
    for x,y, name in zip(xlocs, ylocs, names):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name='PT', sample_name=name)
        yield from bp.scan(dets, waxs, *waxs_range)

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3)

def run_waxsshortPT(t=.25):
    dets = [pil300KW, pil1M]
    xlocs = [-36000,-25000,-16000,-44000,-36500,-27000,-18000,-8000,0,9000,18500,27000,35500,45000,-8500]
    ylocs = [-8800,-8800,-8800,6500,6500,6000,6000,6000,6000,6000,6000,6000,6000,6500,7000,-8800]
    names = ['PT7E-012A','PT5E-010A','PT5E-010B','PT5E-016D','PT5E-016E','GMB-018A','GMB-018B','GMB-019','CC1-036A','CC1-036B','CC1-036C','CC1-036D','CC1-036E','CC1-036F','offsetSAXS_tape_blank']
    user = 'PT'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 58.5, 10)
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam,x, y in zip(names, xlocs, ylocs):
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.x, x)
            name_fmt = '{sam}_wa{waxs}deg'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 
    

def gisaxs_tempPT(t=1):
    # Slowest cycle:
    temperatures = [120]
    x_list  = [-24500,-8500,7500,21500]
    y_list=[3354,3246,3068,3700]
    samples = ['DVC_3MPA','DVC_CystAm' ,'DVC_u1','KRH_u1']
    
    #Detectors, motors:
    #dets = [pil1M, rayonix, pil300KW,ls.ch1_read, xbpm3.sumY] #ALL detectors
    dets = [pil1M, pil300KW, ls.ch1_read, xbpm3.sumY] # WAXS detector ALONE
    angle_offset = [0.1, 0.15]
    waxs_range = [0, 58.5, 10]
    waxs_range_rev = [58.5, 0, 10]
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for i_t, temps in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, temps)
        #if i_t > 0:
           #yield from bps.sleep(300)
        for x, y, s in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from alignement_gisaxs_shorter(0.1)
            ##yield from quickalign_gisaxs(0.1)
            plt.close('all')
            a_off = piezo.th.position
            for i, an in enumerate(angle_offset):
                yield from bps.mv(piezo.th, a_off+an)
                det_exposure_time(t,t)
                temp = ls.ch1_read.value
                name_fmt = '{sample}_{temper}C_{angl}deg'
                yield from bps.mv(piezo.x, x+i*200)
                sample_name = name_fmt.format(sample=s, temper = temp, angl = an)
                sample_id(user_name='PT', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                if i == 0:
                    yield from bp.scan(dets, waxs, *waxs_range)
                else:
                    yield from bp.scan(dets, waxs, *waxs_range_rev)
            yield from bps.mv(piezo.th, a_off)
            
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3) 
 
 
def gisaxs_PT(t=1):
    # Slowest cycle:
    
    x_list  = [ 1500, -7500, -12500, -17500, -22500,-27000,-35000,-47000]
    samples = [ '1wtSO1YonGA','5wtSO1YonGA','1wtSO1Yonbare','5wtPS-PMMAonGA', '5wtSV129onGA','1wtSO1Yon350C','DVC48A','DVC48E']
    
    #Detectors, motors:
    #dets = [pil1M, rayonix, pil300KW,ls.ch1_read, xbpm3.sumY] #ALL detectors
    dets = [pil1M] # WAXS detector ALONE
    angle_offset = [0.1,0.15, 0.2]
    waxs_range = [0, 58.5, 10]
    
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
        
    for x, s in zip(x_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from alignement_gisaxs_shorter(0.1)
        #yield from quickalign_gisaxs(0.1)
        plt.close('all')
        a_off = piezo.th.position
        for i, an in enumerate(angle_offset):
            yield from bps.mv(piezo.th, a_off+an)
            det_exposure_time(t,t)
            name_fmt = '{sample}_{angl}deg'
            sample_name = name_fmt.format(sample=s, angl = an)
            sample_id(user_name='FY', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
                
            
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3)  

