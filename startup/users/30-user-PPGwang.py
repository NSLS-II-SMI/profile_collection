#Align GiSAXS sample
import numpy as np

def capillaries_saxs_PPG(t=0.3): 
    #samples = ['4-1','4-2','4-3','4-4','4-5','4-6','4-7','4-8','4-9','4-10','4-11','4-12','4-13','4-14']
    
    #x_list = [42700, 36400, 30300, 23800, 17400, 11300, 4700, -1700, -8100, -14200, -21100, -27000, -33300, -39700]
    #y_list = [9000,   9000,  9000,  9000,  9000,  9000, 9000,  9000,  7000,   9000,   9000,   9000,   9000,  9000]
    #z_list = [1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400]

    samples = ['012_film','181_film','175_film','210_film','215_film']
    
    x_list = [39300, 20250, 1150, -17900, -37000]
    y_list = [-7000, -7000, -7000, -7000, -7000]
    z_list = [5400, 5400, 5400, 5400, 5400]

  # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for x, y, z, sample in zip(x_list, y_list, z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)

        sample_id(user_name='CW_8.3m_6.51keV_RT_0.6', sample_name=sample) 
        yield from bp.count(dets, num=1)
   
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)


def slide_linkam_PPG(t=0.15): 
    samples = '83B_ramp'
    #samples = ['LTC_ramp']
    #samples = ['LTC_15minwait']
    hexa_y = -4.8
    

  # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    #assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    sample_id(user_name='CW_8.3m_6.51keV', sample_name=samples) 
    yield from bps.mv(stage.y, hexa_y)
    
    for i in range (130):
      yield from bp.count(dets, num=1)
      yield from bps.mvr(stage.y, 0.005)
      yield from bps.sleep(28)
   
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

