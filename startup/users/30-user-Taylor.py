def do_twaxs_scanx(meas_t = 1):
    #x_list = [-37000]
    #sample_list = ['blank_kapton']
    #x_list = [-19000, -1000, 17000 ]
    #sample_list = ['2_mg_ml_freestanding_1','2_mg_ml_freestanding_2', '1_5_mg_ml_freestanding_1'] 
    
    
    #x_list = [-32000, -14000, 2000, 22000, 41000]
    #sample_list = ['Kapton_blank_ambient','3_mg_ml_freestanding_annealed_ambient', '3_mg_ml_freestanding_ambient','2_5_mg_ml_freestanding_annealed_ambient','2_5_mg_ml_freestanding_ambient'] 
    
    x_list = [11719]
    sample_list = ['ultimate_MXene_2',] 
    
    #x_list = [-38280, -23279, 34719]
    #sample_list = ['mechanically_exfoliated_mxene_1', 'mechanically_exfoliated_mxene_2', 'mechanically_exfoliated_on_glass'] 
    
    
    dets = [pil300KW] #, pil1M, rayonix] 
        
    #waxs_angle_array = np.linspace(0, 24, 5) 
    waxs_angle_array = np.linspace(0, 12, 1)    
    #x_shift_array = np.linspace(-1000, 1000, 9)
    x_shift_array = np.linspace(-300, 600, 31)
    #y_shift_array = np.linspace(-300, 600, 31)
    
    name_fmt = '{sample}_waxs{waxsangle}_x{xpos}_y{ypos}_saxs4m_{meas_t}s' #was 5.1m
    
    for x, sample in zip(x_list,sample_list): #loop over samples on bar
        x_pos_array = x + x_shift_array
        
        for waxs_angle in waxs_angle_array:
            yield from bps.mv(waxs, waxs_angle)

            for x_meas in x_pos_array:
                yield from bps.mv(piezo.x, x_meas) 
                det_exposure_time(meas_t, meas_t) 

                sample_name = name_fmt.format(sample=sample, waxsangle = '%05.2f'%waxs_angle, xpos = '%07.1f'%piezo.x.position, ypos = '%07.1f'%piezo.y.position,meas_t = '%04.1f'%meas_t)                
                sample_id(user_name='AT', sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')

                #yield from bp.scan(dets, waxs, *waxs_arc)
                yield from bp.count(dets, num=1)
      

 
 # - Close the hutch
 # RE(shopen())  
 # - Edit the file 30-user-Taylor.py and save
 # %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Taylor.py
 # RE(do_giwaxs_scanx(meas_t=1))
 #
 # if do ctrl+C: RE.abort()
 #
 # - Before opening hutch:
 # RE(shclose())
            
    
