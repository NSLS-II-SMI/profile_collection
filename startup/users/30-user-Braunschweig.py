#Align GiSAXS sample
import numpy as np
      
def run_gisaxsAngle_AB(t=1): 


    # define names of samples on sample bar
    #sample_list = ['sb-b_1_1'] #
    sample_list = ['5_63_d3T_NDI','5_64_d3T_dCNNDI','5_65_MeDPP_dCNNDI']
    #x_list = [42000] 
    x_list = [44000,20000,-8000]
    
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'

    angle_arc = np.array([0.08, 0.1, 0.15, 0.2]) # incident angles
    waxs_angle_array = np.linspace(0, 18, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
                                               # if 12, 3: up to q=2.199
                                               # if 18, 4: up to q=3.04
    dets = [pil300KW, rayonix, pil1M] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]
    
    for x, sample in zip(x_list,sample_list): #loop over samples on bar

        yield from bps.mv(piezo.x, x) #move to next sample                
        yield from alignement_gisaxs(0.1) #run alignment routine

        th_meas = angle_arc + piezo.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
        th_real = angle_arc	

        det_exposure_time(t,t) 
        x_meas = x;
            
        for waxs_angle in waxs_angle_array: # loop through waxs angles
            yield from bps.mv(waxs, waxs_angle)
                
            for i, th in enumerate(th_meas): #loop over incident angles
                yield from bps.mv(piezo.th, th)
                    
                x_meas = x_meas - 200   # shift a bit in x
                yield from bps.mv(piezo.x, x_meas) 
                                                
                sample_name = '{sample}_{th:5.4f}deg_waxs{waxs_angle:05.2f}_x{x}_{t}s'.format(sample = sample, th=th_real[i], waxs_angle=waxs_angle, x=x_meas, t=t)
                sample_id(user_name='AB', sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')                        
                            
                #yield from bp.scan(dets, energy, e, e, 1)
                #yield from bp.scan(dets, waxs.arc, *waxs_arc)
                yield from bp.count(dets, num=1)
                    

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)


#### 

# 
# Modify file (sample name, x pos), Save file
# Check sample stage (SmarAct Y) is aroundre 5200
# Check bsx at 0.7
#
# RE(shopen())
# 
# %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Braunschweig.py 
# RE(run_gisaxsAngle_AB(0.5)) 
#
# RE(shclose())    
#
# if do ctrl+C: RE.abort()
#
# Data: /GPFS/xf12id1/data/images/users/2019_2/304848_Braunschweig/









  




