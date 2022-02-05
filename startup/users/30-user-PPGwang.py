#Align GiSAXS sample
import numpy as np

def capillaries_saxs_PPG(t=0.2): 
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


def slide_linkam_PPG(t=0.3): 
    samples = '21-DJF-001H' #ramps up from 25C
    #samples = ['LTC_ramp']
    #samples = ['LTC_15minwait']
    hexa_y = -0.25
  
  # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    #assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    sample_id(user_name='CW_8.3m_6.51keV', sample_name=samples) 
    yield from bps.mv(stage.y, hexa_y)
    
    for i in range (90):
      yield from bp.count(dets, num=1)
      yield from bps.mvr(stage.y, 0.01)
      yield from bps.sleep(28)
   
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)

def PPG_temp_2022_1(tim=0.2): 
    temperatures = [28, 40, 50, 60]
    
    names = ['s16','s17','s18','s19','s20','s6a','s7a','e1','e3','e4','e5','e10','e7','e8','e9']
    x_piezo  = [-44200, -37850, -31650,  -25200, -18900, -12600, -6100, 300, 6650, 13000,19350,25700, 32050, 38400, 44750]
    # y_piezo =  [      7000,       7000,       7000,       7000,       7000,       7000,       7000,       7000]
    #assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of Y coordinates ({len(y_list)})'
    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    
    #Detectors, motors:
    dets = [pil1M] #ALL detectors

    
    name_fmt = '{sample}_{temperature}C_6.51keV_8.3m'

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
        if t_celsius>30:
            yield from bps.sleep(300)
        for name, xs_piezo in zip(names, x_piezo):
            yield from bps.mv(piezo.x, xs_piezo)
            sample_name = name_fmt.format(sample=name, temperature='%3.1f'%t)

            sample_id(user_name='CW', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.count(dets, num=1)
        #move caps in Y by 100 um for every T value
        yield from bps.mvr(piezo.y, -(i_t+1)*100) 


    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5,0.5)
    yield from ls.output1.mv_temp( 28 + 273.13)






def capillaries_saxs_ppg_2022_1(t=0.2): 
    #holder 5
    #samples = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'a13', 'a14', 'a3', 'a4',
    #'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12']

    #x_list = [-45000, -38500, -31700, -25900, -19400, -13300, -6550,   300,  6150, 12500, 18800, 24900, 31450, 37700,
    #          -41500, -34900, -28700, -21900, -15600,  -9700, -3200,  3100,  9600, 16000, 22400, 28500, 35000, 41200]
    #y_list = [ -2000,  -2000,  -2000,  -2000,  -2000,  -2000, -2000, -2000, -2000, -2000, -2000, -2000, -2000, -2000,
    #           -2000,  -2000,  -2000,  -2000,  -2000,  -2000, -2000, -2000, -2000, -2000, -2000, -2000, -2000, -2000]
    #z_list = [ -2500,  -2500,  -2500,  -2500,  -3500,  -3500, -3500, -3500, -5000, -4500, -6500, -6500, -6500, -6500,
    #            8000,   8000,   7500,   7000,   6000,   6000,  6000,  6000,  6000,  5000,  5000,  4000,  4000,   400]

    #holder 6
    #samples = [ 'a1',  'a2', 'a15', 'a16', 'a17',  'e6', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19', 'e20', 'e21', 'e22', 'e23', 'e24', 'e25', 'e26']
    
    #x_list = [-43500, -39100, -34000, -28900, -24100, -19800, -14800, -11000, -6700, -1750, 2300, 5900, 9800, 14200, 17800, 22150, 26700, 30550, 33900, 38100, 41300, 44000]
    #y_list = [  2600,   2600,   2600,   3100,   3100,   3100,   3100,   3100,  3100,  3500, 3500, 3500, 3500,  3500,  3500,  3500,  3500,  3500,  3900,  3900,  3900,  3900]
    #z_list = [  1900,   1900,   1900,   1900,   1900,   1900,   1900,   1900,  1900,  1900, 1900, 1900, 1900,  1900,  1900,  1900,   700,   700,   200,   200,  1900,  1900]

    #holder 7
    #samples = ['e27', 'e28', 'e29', 'e30', 'e31', 'e32', 'e33', 'e34', 'e35', 'e36', 'e37', 'e38', 'e39', 'DJFA', 'DJFB', 'DJFC', 'DJFD']
    
    #x_list = [-42900, -39200, -33300, -29600, -23800, -19950, -14250, -9950, -4550,  -750, 3200, 7750, 11250, 16750, 25250, 31300, 39500]
    #y_list = [  6500,   6500,   6500,   6500,   6500,   6500,   5100,  6500,  6500,  6500, 6500, 6500,  6500,  6500,  6500,  6500,  6500]
    #z_list = [  2100,   2100,   2100,   2100,   2100,   2100,   2100,  2100,  2100,  2100, 2100, 2100,  2100,  2100,  2100,  2100,  2100]    
    
    #holder 8
    #samples = ['DJFE', 'DJFF', 'DJFG', 'DJFH', 'a5a', 'e3film', 'e5film', 'e6film', 'e7film', 'e8film']
    
    #x_list = [-40600, -32600, -22000, -13500,  -8100,  100, 11100, 20100, 32100, 42100]
    #y_list = [  6200,   6200,   6200,   6200,   6200, 6200,  6200,  6200,  6200,  6200]
    #z_list = [  2500,   2500,   2500,   2500,   2500, 2500,  2500,  2500,  2500,  2500]

    #holder 9   !!! these need kapton subtraction !!!
    #samples = ['e12film', 'e13film', 'e30film', 'e28film', 'e29film']
    
    #x_list = [-40000, -15000, 5000, 30000, 40000]
    #y_list = [  6700,   6700, 6700,  6700,  6700]
    #z_list = [  2500,   2500, 2500,  2500,  2500]

    #holder 10
    #samples = ['e35a', 'e37a', 'e38a', 'e39a', 'e11a', 'e16a', 'e22a']
    
    #x_list = [-42600, -33150, -24550, -17250, -10350, -3900, 8300]
    #y_list = [  6700,   6700,   6700,   4900,   6700,  6700, 5500]
    #z_list = [  1500,   1500,   1500,   1500,   1500,  1500, 1500]

    #holder 11
    samples = ['e4film', 'e9film', 'e31film', 'e32film', 'e33film']
    
    x_list = [-40000, -15000, 5000, 22000, 35000]
    y_list = [  6700,   6700, 6700,  6700,  6700]
    z_list = [  2500,   2500, 2500,  2500,  2500]

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

        sample_id(user_name='CW_8.3m_6.51keV', sample_name=sample) 
        yield from bp.count(dets, num=1)
   
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)

