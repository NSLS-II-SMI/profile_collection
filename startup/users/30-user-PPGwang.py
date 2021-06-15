#Align GiSAXS sample
import numpy as np

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



def capillaries_saxs_Thed_2021_1(t=1): 
    # samples = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18', 'L19', 'L20',
    # 'L21', 'L22', 'L23', 'L24', 'L25', 'L26']
    
    # x_list = [43000, 37100, 30300, 24300, 18000, 11300, 5000, -1550, -7950, -14200, -20500, -26900, -33300,
    #           40200, 33700, 27200, 20800, 14100,  8200, 1700, -4800,-11250, -17800, -24000, -29500, -36800]
    # y_list = [    0,     0,  1000,  1000,  1000,  1000, 1000,  1000,  1000,   1000,   1000,   1000,   1000,
    #            1000,  1000,  1000,  1000,  1000,  1000, 1000,  1000,  1000,   1000,   1000,   1000,   1000]
    # z_list = [-8100, -8100, -8100, -8100, -8100, -8100,-8100, -8100, -8100,  -8100,  -8100,  -8100,  -8100,
    #            1500,  1500,  1500,  1500,  1500,  1500, 1500,  1500,  1500,   1500,   1500,   1500,   1500]


    samples = ['L27','L28', 'L29', 'L30', 'L31', 'L32', 'L33', 'L35',  'L36']
    x_list = [37000, 30850, 23900, 17600, 11350,  5000, -1500, -7400, -13800]
    y_list = [    0,     0,  1000,  1000,  1000,  1000,  1000,  1000,   1000]
    z_list = [-8100, -8100, -8100, -8100, -8100, -8100, -8100, -8100,  -8100]

  # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(y_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(z_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'

    for x, y, z, sample in zip(x_list, y_list, z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)

        sample_id(user_name='PT_5.0m_16.1keV', sample_name=sample) 
        yield from bp.count(dets, num=10)
   
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)

