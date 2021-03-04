####line scan

def aaron_rot(t=8):
    sample_id(user_name='AM', sample_name='tetrahedral')
    det_exposure_time(t)
    yield from bp.inner_product_scan([pil1M], 24, prs, 45, 22, stage.x, 0.23, 0.15, piezo.y, -1792.6, -1792.6)
    yield from bp.inner_product_scan([pil1M], 22, prs, 21, 0, stage.x, 0.15, 0.11, piezo.y, -1792.6, -1792.6)
    yield from bp.inner_product_scan([pil1M], 11, prs, -1, -11, stage.x, 0.11, 0.1, piezo.y, -1792.6, -1792.1)
    yield from bp.inner_product_scan([pil1M], 11, prs, -12, -22, stage.x, 0.1, 0.1, piezo.y, -1792.1, -1791.6)
    yield from bp.inner_product_scan([pil1M], 11, prs, -23, -33, stage.x, 0.1, 0.114, piezo.y, -1791.6, -1790.9)
    yield from bp.inner_product_scan([pil1M], 12, prs, -34, -45, stage.x, 0.114, 0.134, piezo.y, -1790.9, -1790.9)
    
    
def brian_caps(t=1): 
    x_list  = [-36500, -30150, -23800, -17450, -11100, -4750, 1600, 7950,  14400, 20700, 27050, 33400, 39850]#
    y_list =  [      0,     0,      0,      0,      0,     0,    0,     0,      0]
    samples = [ 'test', 'LC-O36-6','LC-O36-7','LC-O36-8','LC-O36-9','LC-O37-6','LC-O37-7','LC-O37-8','LC-O37-9']
    # Detectors, motors:
    dets = [pil1M]
    y_range = [0, 0, 1]
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t,t)
    for x, y, sample in zip(x_list,y_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name='BM', sample_name=sample) 
        #yield from bp.scan(dets, piezo.y, *y_range)
        yield from bp.count(dets, num=1)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)

def brian_caps_2020_3(t=1): 
    # samples = ['buffer1', 'GB01', 'GB02', 'GB03', 'GB04', 'GB05', 'GB06', 'GB08', 'GB09', 'GB10', 'GB11', 'GB12']
    # samples = ['Y01', 'Y02', 'Y03', 'Y04', 'Y05', 'Y06']

    # x_list = [-22300, -18600, -11000, -4500, 2300, 8500, 14500, 21000, 27500, 33800, 40300, 46700]
    # y_list = [2500,     2500,   2500,  2500, 2500, 2500,  2500,  2500,  2500,  2500,  2500,  2500]
    # z_list = [4000,     2500,   2500,  2500, 2500, 2500,  2500,  2500,  2500,  2500,  2500,  2500]

    samples = ['S1_43', 'S1_44', 'S1_45', 'S1_46', 'S1_47', 'S1_48', 'S1_49', 'S1_50', 'S1_51', 'S1_52', 'S1_53', 'S1_54', 'S1_55', 'S1_56', 'S1_57',
    'S1_58', 'S1_59', 'S1_60', 'S1_61', 'S1_62', 'S2_63', 'S2_67', 'S2_68', 'S2_69', 'S2_70', 'S2_71']

    x_list = [-39100, -32820, -26400, -20240, -13880, -7020,  -720, 5390, 11680, 18180, 24560, 31040, 37360, 43820, -37780,
    -31530, -24530, -17840, -12100, -5800, 790, 7170, 13000, 19420, 25840, 32260]
    y_list = [  200,       0,      0,     0,   0,    0,     0,     0,     0,     0,     0,      0,      0,      0,    0,
         0,      0,      0,      0,     0,   0,    0,     0,     0,     0,     0]
    z_list = [ 12500,  12500,  12500,  12500,  12500, 12500,  12500,12500, 12500, 12500, 12500, 12500, 12500, 12500,   2000,
      2000,   2000,   2000,   2000,  2000,2000, 2000,  2000,  2000,  2000,  2000]


    # Detectors, motors:
    dets = [pil1M]
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'
    assert len(x_list) == len(z_list), f'Number of X coordinates ({len(x_list)}) is different from number of Z coord ({len(z_list)})'
    ypos = [0, 50, 2]

    det_exposure_time(t,t)
    for x, y, z, sample in zip(x_list,y_list,z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)
        sample_id(user_name='BM', sample_name=sample + '_test_18.25keV') 
        # yield from bp.rel_scan(dets, piezo.y, *ypos)
        yield from bp.count(dets, num=240)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def brian_caps_damage_2021_1(t=1): 

    samples = ['V1_01', 'V1_02', 'V1_03', 'V1_04', 'V1_05', 'V1_06', 'V1_07', 'V1_08', 'V1_09', 'V1_10', 'V1_11', 'V1_12', 'V1_13',
    'V1_14', 'V1_15', 'V1_16', 'V1_17', 'V1_18', 'V1_19', 'V1_20', 'V1_21', 'V1_22', 'V1_23', 'V1_24', 'V1_25', 'V1_26',
    'V1_27', 'V1_28', 'V1_29', 'V1_30', 'V1_31', 'V1_32', 'V1_33', 'V1_35', 'V1_36']

    x_list = [41600, 35500, 28950, 22600, 16600, 10050, 3600, -2750, -9050, -15350, -21650, -28100, -34450,
    40500, 34500, 27600, 21000, 15150, 8650, 2700, -4000, -10250, -16600, -22850, -28950, -35500,
    38900, 32950, 26900, 19900, 13350, 7100, 1000, -5500, -11700]
    y_list = [ 3000,  3000,  2700,  2700,  2700,  2700, 2700,  2700,  2700,   2700,   2700,   2700,   2700,
     2700,  2700,  2700,  2700,  2700, 2700, 2700,  2700,   2700,   2700,   2700,   2700,   2700,
     2700,  2700,  2700,  2700,  2700, 2700, 2700,  2700,   2700]
    z_list = [-9000, -9000, -9000, -9000, -9000, -9000,-9000, -9000, -9000,  -9000,  -9000,  -9000,  -9000, 
      900,   900,   900,   900,   900,  900,  900,   900,    900,    900,    900,    900,    900,  
    10900, 10900, 10900, 10900, 10900,10900,10900, 10900,  10900]


    # Detectors, motors:
    dets = [pil1M]
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'
    assert len(x_list) == len(z_list), f'Number of X coordinates ({len(x_list)}) is different from number of Z coord ({len(z_list)})'
    ypos = [0, 50, 2]

    det_exposure_time(1, 180)
    for x, y, z, sample in zip(x_list,y_list,z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)
        sample_id(user_name='BM', sample_name=sample + '_11.85keV_8.3m_1s') 
        caput('XF:12IDC-ES:2{Det:1M}cam1:Acquire', 1)
        yield from bps.sleep(200)

          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def brian_caps_2021_1(t=1): 
    # samples = ['buffer1', 'GB01', 'GB02', 'GB03', 'GB04', 'GB05', 'GB06', 'GB08', 'GB09', 'GB10', 'GB11', 'GB12']
    # samples = ['Y01', 'Y02', 'Y03', 'Y04', 'Y05', 'Y06']

    # x_list = [-22300, -18600, -11000, -4500, 2300, 8500, 14500, 21000, 27500, 33800, 40300, 46700]
    # y_list = [2500,     2500,   2500,  2500, 2500, 2500,  2500,  2500,  2500,  2500,  2500,  2500]
    # z_list = [4000,     2500,   2500,  2500, 2500, 2500,  2500,  2500,  2500,  2500,  2500,  2500]

    # samples = ['NPT_Blank', 'NPT_09', 'NPT_13', 'NPT_14', 'NPT_16', 'NPT_59', 'NPT_60', 'NPT_61', 'NPT_62', 'NPT_63', 'NPT_64', 'MLE_blank', 'MLE_01', 'MLE_02',
    # 'MLE_03', 'MLE_05', 'MLE_06', 'MLE_07', 'MLE_08', 'MLE_09', 'MLE_10', 'MLE_11', 'MLE_12', 'MLE_13', 'MLE_14', 'MLE_15', 'MLE_04']

    samples = ['NT_Blank', 'NT_05', 'NT_06', 'NT_07', 'NT_08', 'NT_17', 'NT_18', 'NT_19', 'NT_20', 'NT_21', 'NT_22', 'NT_23', 'NT_24', 'NT_25', 'NT26',
    'NT_27', 'NT_28', 'NT_29', 'NT_30', 'NT_31', 'NT_32', 'NT_33', 'NT_34', 'NT_35', 'NT_36', 'NT_37', 'NT_38', 'NT_39', 'NT_40']

    x_list = [47000, 40650, 34300, 27950, 21600, 15350, 9000, 2650, -3700, -10250, -16450, -22750, -29300, -35650, -42100,
    45300, 38750, 32500, 26550, 19800, 13450, 7200,  650, -5500, -11850, -18200, -24450, -30900, -37250]
    y_list = [ 3000,  3000,  3000,  3700,  3700,  3700, 3700, 3700,  3700,   3700,   3700,   3700,   3700,   3700,   3300,
     3300,  3700,  3700,  3700,  3700, 3700, 3700,  3700,  3700,   3700,   3700,   3700,   3700,  3700]
    z_list = [  900,   900,   900,   900,   900,   900,  900, 900,   900,    900,    900,    900,    900,    900,     900,
    10900, 10900, 10900, 10900, 10900,10900,10900, 10900, 10900,  10900,  10900,  10900,  10900, 10900]

    # Detectors, motors:
    dets = [pil1M]
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'
    assert len(x_list) == len(z_list), f'Number of X coordinates ({len(x_list)}) is different from number of Z coord ({len(z_list)})'
    ypos = [0, 50, 2]
    ypos1 = [100, 150, 2]

    det_exposure_time(t,t)
    for x, y, z, sample in zip(x_list,y_list,z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)

        det_exposure_time(1,1)

        sample_id(user_name='BM', sample_name=sample + '_16.1keV_8.3m_1s_pos1') 
        yield from bps.mv(piezo.y, y + 0)
        caput('XF:12IDC-ES:2{Det:1M}cam1:Acquire', 1)
        yield from bps.sleep(2)

        sample_id(user_name='BM', sample_name=sample + '_16.1keV_8.3m_1s_pos2') 
        yield from bps.mv(piezo.y, y + 50)
        caput('XF:12IDC-ES:2{Det:1M}cam1:Acquire', 1)
        yield from bps.sleep(2)

        det_exposure_time(2,2)

        sample_id(user_name='BM', sample_name=sample + '_16.1keV_8.3m_2s_pos1') 
        yield from bps.mv(piezo.y, y + 100)
        caput('XF:12IDC-ES:2{Det:1M}cam1:Acquire', 1)
        yield from bps.sleep(2)

        sample_id(user_name='BM', sample_name=sample + '_16.1keV_8.3m_2s_pos2') 
        yield from bps.mv(piezo.y, y + 150)
        caput('XF:12IDC-ES:2{Det:1M}cam1:Acquire', 1)
        yield from bps.sleep(2)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def run_mesh_aaron_2021(t=1): 
    name = 'AM'
    dets = [pil1M]
    det_exposure_time(t,t)
    
    samples = ['sample_fe1']
    x_list = [-25100]
    y_list = [3600]
    x_range=[[-25100, -24900, 9]]
    y_range=[[3600, 3800, 81]]
    
    i = 0
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    
    yield from bps.mv(pil1m_pos.y, -60.0)
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)

        for xs in np.linspace(x_r[0], x_r[1], x_r[2]):
            for ys in np.linspace(y_r[0], y_r[1], y_r[2]):
                yield from bps.mv(piezo.x, xs)
                yield from bps.mv(piezo.y, ys)

                name_fmt = '{sam}_8.3m_16.1keV_pos{pos}_up'
                sample_name = name_fmt.format(sam=sample, pos ='%4.4d'%i)

                sample_id(user_name=name, sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                caput('XF:12IDC-ES:2{Det:1M}cam1:Acquire', 1)
                yield from bps.sleep(1)

                i+=1


    yield from bps.mv(pil1m_pos.y, -55.7)
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)

        for xs in np.linspace(x_r[0], x_r[1], x_r[2]):
            for ys in np.linspace(y_r[0], y_r[1], y_r[2]):
                yield from bps.mv(piezo.x, xs)
                yield from bps.mv(piezo.y, ys)

                name_fmt = '{sam}_8.3m_16.1keV_pos{pos}_dn'
                sample_name = name_fmt.format(sam=sample, pos ='%4.4d'%i)

                sample_id(user_name=name, sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                caput('XF:12IDC-ES:2{Det:1M}cam1:Acquire', 1)
                yield from bps.sleep(2)

                i+=1

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)



def brian_caps(t=1): 
    samples = ['sample44_1', 'sample44_2', 'sample45_1', 'sample45_2','sampleB_1', 'sampleB_2','sampleB_3', 'sampleP_1',
    'sampleP_2'
    ]

    x_list  = [-41000, -34350, -28400, -22000, -15700, -9350, -2700, 3400, 
    19200
    ]

    y_list =  [7600, 7600, 7700, 8000, 7800, 7500, 7500, 7500, 
    7500
    ]
    
    z_list = [9600,9600,9600,9600,9600,9600,9600,9600,
    2600
    ]

    # Detectors, motors:
    dets = [pil1M]
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'
    assert len(x_list) == len(z_list), f'Number of X coordinates ({len(x_list)}) is different from number of Z coord ({len(z_list)})'
    ypos = [0, 50, 2]

    det_exposure_time(t,t)
    for x, y, z, sample in zip(x_list,y_list,z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)
        sample_id(user_name='BM', sample_name=sample) 
        # yield from bp.rel_scan(dets, piezo.y, *ypos)
        yield from bp.count(dets, num=1)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)



def run_mesh_aaron(t=1): 
    name = 'AM'
    dets = [pil1M]
    det_exposure_time(t,t)
    
    
    # samples = ['sample_b1_area1', 'sample_b1_area2']
    # x_list = [45365, 46145]
    # y_list = [-1865, -1895]
    # x_range=[[0,150,7], [0,200,9]]
    # y_range=[[0,150,76],[0,150,76]]
    

    samples = ['sample_b1_area1_1','sample_b1_area2_1', 'sample_b2_area1', 'sample_b2_area2', 'sample_c1_area1', 'sample_c1_area2',
    'sample_c2_area1', 'sample_t1_area1', 'sample_t1_area2']
    x_list = [45423, 46344, 22765, 22415, 2040, 540, -19755, -43785, -42785]
    y_list = [-2035, -2135, -1165, -1765, -590, -1770, -1095, 480, -120]
    x_range=[[0,150,7],[0,150,7], [0,250,13], [0,200,9], [0,300,13],[0,300,13],[0,300,13],[0,500,21],[0,300,13], [0,150,7]]
    y_range=[[0,200,101], [0,150,76],[0,150,76],[0,150,76],[0,300,151],[0,200,101],[0,200,101],[0,300,151],[0,200,101],[0,150,76]]
    


    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        name_fmt = '{sam}'
        sample_name = name_fmt.format(sam=sample)
        sample_id(user_name=name, sample_name=sample_name) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.rel_grid_scan(dets, piezo.y, *y_r, piezo.x, *x_r,   0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)
