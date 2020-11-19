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
