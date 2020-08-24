#Align GiSAXS sample
import numpy as np

def align_gisaxs_th_stage(  rang = 0.3, point = 31   ):             
        yield from bp.rel_scan([pil1M], stage.th, -rang, rang, point )
        ps()
        yield  from bps.mv(stage.th, ps.peak)  

def alignement_gisaxs_stage(angle = 0.15):      
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment_gisaxs()
        
        #Set direct beam ROI
        yield from smi.setDirectBeamROI()

        #Scan theta and height
        yield from align_gisaxs_height(700, 16, der=True)
        yield from align_gisaxs_th_stage(0.7, 11)
        yield from align_gisaxs_height(300, 11, der=True)
        yield from align_gisaxs_th_stage(0.4, 16)
        
        #move to theta 0 + value
        yield from bps.mv(stage.th, ps.peak + angle)

        #Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=0.165/2+0.515/2
)
        
        #Scan theta and height
        yield from align_gisaxs_th_stage(0.2, 31)
        yield from align_gisaxs_height(200, 21)
        yield from align_gisaxs_th_stage(0.05, 21)
        
        #Close all the matplotlib windows
        plt.close('all')
        
        #Return angle
        # TODO: Should we return to 0
        yield from bps.mv(stage.th, ps.cen - angle)
        yield from smi.modeMeasurement_gisaxs()


def run_tomo_ET(t=0.5): #2020C1
    
    sample = 'SampleDario_TOMO'
    #x_list = [47200.000,37200.000,23700.000,15700.000]
    x_list = np.arange(-4.158-0.5, 3.842+0.01+0.5, 0.2)
    
    #assert len(x_list) == len(sample_list), f'Sample name/position list is borked'

    angle_arc = 0.1 #np.array([0.08, 0.1, 0.15, 0.2]) # incident angles
    #waxs_angle_array = np.linspace(0, 19.5, 4) #(0, 18, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
                                               ## if 12, 3: up to q=2.199
                                               ## if 18, 4: up to q=3.04
                                               
    waxs_angle_array = np.arange(6.5, 75, 6.5) #(0, 18, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
    prs_angles_zig = [-90, 90.1, 120]
    prs_angles_zag = [90, -90-0.1, 120]
    dets = [pil300KW, pil1M] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]
    
        #yield from bps.mv(piezo.th, 0)              
        #yield from alignement_gisaxs(0.1) #run alignment routine
        
        ##yield from bps.mv(waxs, 4)
        #try: 
            #yield from bps.mv(waxs, 0)
        #except:
            #print('ERROR with WAXS, trying again..')
            #yield from bps.mv(waxs, 0)

    #stage.th.position = 0.382
    th_meas = angle_arc + 0.282 # stage.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
    th_real = angle_arc	
			

           
    for waxs_angle in waxs_angle_array: # loop through waxs angles
        yield from bps.mv(waxs, waxs_angle)

        if waxs_angle == 0:
            det_exposure_time(0.1,0.1) 
        else:
            det_exposure_time(t,t) 
        for ii, x in enumerate(x_list): #loop over samples on bar
            yield from bps.mv(stage.x, x) #move to next sample  
                    
            sample_name = '{sample}_{th:5.4f}deg_waxs{waxs_angle:05.2f}_x{x}_{t}s'.format(sample = sample, th=th_real, waxs_angle=waxs_angle, x=x, t=t)
            sample_id(user_name='ET2', sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')                        

            if ii%2==0:
                yield from bp.scan(dets, prs, *prs_angles_zig)
            else:
                yield from bp.scan(dets, prs, *prs_angles_zag)
                    

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)


def run_gisaxsAngle_ET(t=1): #2020C1
    # define names of samples on sample bar

    sample_list = ['tomosample']
    

    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'

    angle_arc = np.array([0.08, 0.1, 0.15, 0.2]) # incident angles
    waxs_angle_array = np.linspace(0, 19.5, 4) #(0, 18, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
                                               # if 12, 3: up to q=2.199
                                               # if 18, 4: up to q=3.04
    dets = [pil300KW] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]
    
    #for x, sample in zip(x_list,sample_list): #loop over samples on bar
    if 1:
        #yield from bps.mv(piezo.x, x) #move to next sample  
        yield from bps.mv(piezo.th, 0)              
        yield from alignement_gisaxs(0.1) #run alignment routine
        
        yield from bps.mv(waxs, 4)
        try: 
            yield from bps.mv(waxs, 0)
        except:
            print('ERROR with WAXS, trying again..')
            yield from bps.mv(waxs, 0)



        th_meas = angle_arc + piezo.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
        th_real = angle_arc	
			

        det_exposure_time(t,t) 
        x_meas = x;
            
        #for waxs_angle in waxs_angle_array: # loop through waxs angles
        for i, th in enumerate(th_meas): #loop over incident angles
            yield from bps.mv(piezo.th, th)
                
            for jj in [0, 1, 2, 3]:	
                if i==0 and jj==0:
                   x_meas = x_meas - 50   # shift a bit in x
                else:
                    x_meas = x_meas - 200   # shift a bit in x
                yield from bps.mv(piezo.x, x_meas) 

                for waxs_angle in waxs_angle_array:
                    yield from bps.mv(waxs, waxs_angle)
                                                
                    sample_name = '{sample}_{th:5.4f}deg_x{x}_waxs{waxs_angle:05.2f}_{t}s'.format(sample = sample, th=th_real[i], x=x_meas, waxs_angle=waxs_angle, t=t)
                    sample_id(user_name='AB2', sample_name=sample_name) 
                    print(f'\n\t=== Sample: {sample_name} ===\n')                        
                            
                    #yield from bp.scan(dets, energy, e, e, 1)
                    #yield from bp.scan(dets, waxs, *waxs_arc)
                    yield from bp.count(dets, num=1)
                    

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)




def piezo_pos(): 
    for ii in [piezo.x, piezo.y, piezo.z, piezo.th, piezo.ch]: 
        print(ii.name, ii.position) 
def stage_pos(): 
    for ii in [stage.x, stage.th, prs]: 
        print(ii.name, ii.position)
        
#### 

# 
# Modify file (sample name, x pos), Save file
# Check sample stage (SmarAct Y) is aroundre 6500
# xxCheck bsx at 0.7

# %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Tsai.py
#
# Data: /GPFS/xf12id1/data/images/users/2020_1/Tsai


'''
phi=prs stage
1st round
prs = 90, stage.th = 0.375
prs = -90, stage.th = 0.385
2nd round
prs = 90, stage.th = 0.3825
prs = -90, stage.th = 0.3775

move piezo.ch to stage.th=0.38
%mov stage.th 
The stage.th is tuned well

tune piezo.th at prs = 0 (the rotation is limied bewtwee -95  and 95deg)

align the stage.th again at prs = 0

================alignment is done==============
================start measurement==============


In [238]: stage.th.position                                                                                           
Out[238]: 0.28200000000000003

aligned position: 0.1deg incident angle

In [263]: for ii in [piezo.x, piezo.y, piezo.z, piezo.th, piezo.ch]: 
     ...:     print(ii.name, ii.position) 
     ...:      
     ...:                                                                                                             
piezo_x -711.0120000000001
piezo_y 6711.778
piezo_z -190.161
piezo_th -0.1095
piezo_ch -0.138699

In [268]: stage_pos()                                                                                                 
stage_x -0.158
stage_th 0.382
prs 90.0







'''
  




