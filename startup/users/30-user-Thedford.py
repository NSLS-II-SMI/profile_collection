#Align GiSAXS sample
import numpy as np


    
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

