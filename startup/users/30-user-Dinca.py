#Align GiSAXS sample
import numpy as np
import epics      



def run_giwaxs_ZB(t=.5):     
    user_name = 'ZB2' #not change the positon (same as ZB)
    user_name = 'ZB3' #change postion 
    user_name='ZB4'  #for new samples
    user_name = ''  #for YG three drop cast NPs samples
    # define names of samples on sample bar
 

    sample_list = [    'YG_Au5nm_930nM' ] #,   'YG_Au10nm_486nM',   'YG_FeO_10nm_SHS_Wat'   ]
    x_list = [       26500  ]#,  35000,  44500 ]
                       
    sample_list = [      'YG_Au10nm_486nM', ] #  'YG_FeO_10nm_SHS_Wat'   ]
    x_list = [        35200  ]                       

    sample_list = [        'YG_FeO_10nm_SHS_Wat'   ]
    x_list = [        44500  ]  

    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'

    #angle_arc = np.array([0.1, 0.15, 0.19]) # incident angles
    #angle_arc = np.array([0.08, 0.10, 0.12,  0.15]) # incident angles
    angle_arc = np.array([0.05, 0.08, 0.10,  0.12, 0.15,  ]) # incident angles
    #waxs_angle_array = np.linspace(0, 84, 15)
    waxs_angle_array = np.linspace(0, 19.5, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
                                               # if 12, 3: up to q=2.199
                                               # if 18, 4: up to q=3.04
                                               # if 24, 5: up to q=3.87
                                               # if 30, 6: up to q=4.70
                                               # 52/6.5 +1 =8
    dets = [pil300KW, pil1M] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]
    
    #x_shift_array = np.linspace(-500, 500, 3) # measure at a few x positions  
    #x_shift_array = np.array( [0]  ) # measure at a few x positions    
    for x, sample in zip(x_list,sample_list): #loop over samples on bar
  
        yield from bps.mv(piezo.x, x) #move to next sample                
        yield from alignement_gisaxs(0.1) #run alignment routine

        th_meas = angle_arc + piezo.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
        th_real = angle_arc	

        det_exposure_time(t,t) 
        #x_pos_array = x + x_shift_array            
        for waxs_angle in waxs_angle_array: # loop through waxs angles
            yield from bps.mv(waxs, waxs_angle)                
            for i, th in enumerate(th_meas): #loop over incident angles
                yield from bps.mv(piezo.th, th)   
                x_meas = x + (1+i) * 200  
                #for x_meas in x_pos_array: # measure at a few x positions
                yield from bps.mv(piezo.x, x_meas)                                 
                                                
                sample_name = '{sample}_{th:5.4f}deg_waxs{waxs_angle:05.2f}_x{x}_{t}s'.format(sample = sample, th=th_real[i], waxs_angle=waxs_angle, x=x_meas, t=t)
                sample_id(user_name=user_name, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')                        
                            
                #yield from bp.scan(dets, energy, e, e, 1)
                #yield from bp.scan(dets, waxs, *waxs_arc)
                yield from bp.count(dets, num=1)                                   

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)


def run_giwaxs_Taylor(t=.5): 
    #user_name = 'Taylor'
    user_name = 'ZB'
    # define names of samples on sample bar
    
    sample_list = [    'S1_P3PS_1p10_40mgml_Drop',    'S2_P3SIS_1p10_40mgml_Drop',  'S3_P3PS_1p10_6mgml_Drop3',
                        'S4_P3SIS_1p10_6mgml_Drop', 'S5_P3PS_1p10_6mgml_Spin', 'S6_P3SIS_1p10_6mgml_Spin', 'JM17'  ]
    x_list = [           -33000,     -24000,    -11000,   1000,     11000,    22000,     35000,           ]  



    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'

    #angle_arc = np.array([0.1, 0.15, 0.19]) # incident angles
    #angle_arc = np.array([0.08, 0.10, 0.12,  0.15]) # incident angles
    angle_arc = np.array([0.08,  0.12]) # incident angles
    #waxs_angle_array = np.linspace(0, 84, 15)
    waxs_angle_array = np.linspace(0, 19.5, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
                                               # if 12, 3: up to q=2.199
                                               # if 18, 4: up to q=3.04
                                               # if 24, 5: up to q=3.87
                                               # if 30, 6: up to q=4.70
                                               # 52/6.5 +1 =8
    dets = [pil300KW, pil1M] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]
    
    #x_shift_array = np.linspace(-500, 500, 3) # measure at a few x positions  
    #x_shift_array = np.array( [0]  ) # measure at a few x positions    
    for x, sample in zip(x_list,sample_list): #loop over samples on bar
        if sample == 'JM17':
            user_name = 'Taylor'
        yield from bps.mv(piezo.x, x) #move to next sample                
        yield from alignement_gisaxs(0.1) #run alignment routine

        th_meas = angle_arc + piezo.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
        th_real = angle_arc	

        det_exposure_time(t,t) 
        #x_pos_array = x + x_shift_array            
        for waxs_angle in waxs_angle_array: # loop through waxs angles
            yield from bps.mv(waxs, waxs_angle)                
            for i, th in enumerate(th_meas): #loop over incident angles
                yield from bps.mv(piezo.th, th)   
                x_meas = x + (1+i) * 200  
                #for x_meas in x_pos_array: # measure at a few x positions
                yield from bps.mv(piezo.x, x_meas)                                 
                                                
                sample_name = '{sample}_{th:5.4f}deg_waxs{waxs_angle:05.2f}_x{x}_{t}s'.format(sample = sample, th=th_real[i], waxs_angle=waxs_angle, x=x_meas, t=t)
                sample_id(user_name=user_name, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')                        
                            
                #yield from bp.scan(dets, energy, e, e, 1)
                #yield from bp.scan(dets, waxs, *waxs_arc)
                yield from bp.count(dets, num=1)                                   

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)



     
def run_saxs_waxs_Dinca(t=.5): 
    user_name = 'Dinca' 
    # define names of samples on sample bar
    
    sample_list = ['JM10',   'JM11',    'JM12',     'JM13',    'JM14',    'JM15',   'JM16'  ]
    x_list = [      -45000,     -34000,    -19000,   -5000,     11000,    26000,     41000,             ]  
 

    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'
    #waxs_angle_array = np.linspace(0, 84, 15)
    waxs_angle_array = np.linspace(0, 19.5, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
                                               # if 12, 3: up to q=2.199
                                               # if 18, 4: up to q=3.04
                                               # if 24, 5: up to q=3.87
                                               # if 30, 6: up to q=4.70
                                               # 52/6.5 +1 =8
    dets = [pil300KW, pil1M] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]
    
    #x_shift_array = np.linspace(-500, 500, 3) # measure at a few x positions  
    #x_shift_array = np.array( [0]  ) # measure at a few x positions    
    for x, sample in zip(x_list,sample_list): #loop over samples on bar

        yield from bps.mv(piezo.x, x) #move to next sample                
        yield from alignement_gisaxs(0.1) #run alignment routine

        th_meas = angle_arc + piezo.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
        th_real = angle_arc	

        det_exposure_time(t,t) 
        #x_pos_array = x + x_shift_array            
        for waxs_angle in waxs_angle_array: # loop through waxs angles
            yield from bps.mv(waxs, waxs_angle)                
            for i, th in enumerate(th_meas): #loop over incident angles
                yield from bps.mv(piezo.th, th)   
                x_meas = x + (1+i) * 200  
                #for x_meas in x_pos_array: # measure at a few x positions
                yield from bps.mv(piezo.x, x_meas)                                 
                                                
                sample_name = '{sample}_{th:5.4f}deg_waxs{waxs_angle:05.2f}_x{x}_{t}s'.format(sample = sample, th=th_real[i], waxs_angle=waxs_angle, x=x_meas, t=t)
                sample_id(user_name=user_name, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')                        
                            
                #yield from bp.scan(dets, energy, e, e, 1)
                #yield from bp.scan(dets, waxs, *waxs_arc)
                yield from bp.count(dets, num=1)                                   

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)


## NOTE
## for GiSAXS, Pil1M, X = -6, Y = -10, Z = 5000;  Y = 7000
#              beam stop:  X 1.499, Paddle: 288.99, Y 13  (beamstop out: X=6.5)
##      SAXS, pil1M,          Y = -61.45, direct beam (   450, 558  ) , Y ~ = -5649.5 
##                           for saxs holder the hole distance is 6299.860


def _waxs_mode(   ):
    RE( bps.mv(piezo.y, 7000 ) )  # :2{Det:1M-Ax:Y}Mtr.VAL', -61.45




def movx( dx ):
    RE(  bps.mvr(piezo.x, dx) )


def movy( dy ):
    RE( bps.mvr(piezo.y, dy) )

def get_posxy( ):
    return  round( piezo.x.user_readback.value, 2 ),round( piezo.y.user_readback.value , 2 )

def move_waxs_off( waxs_angle=8.0 ):
    RE(  bps.mv(waxs, waxs_angle)    )
def move_waxs_on( waxs_angle=0.0 ):
    RE(  bps.mv(waxs, waxs_angle)  )





sample_dict =  {  1: 'Fang_OC1', 2: 'Fang_CB1',
                   3: 'YG_P1_18.0wt',   4: 'YG_P2_20.0wt',  5: 'YG_P3_22.0wt', 6: 'YG_P4_24.0wt', 
                 7: 'YG_P5_26.0wt',      8: 'YG_P6_28.0wt',    9: 'YG_P7_30.0wt',  10: 'YG_P8_0.5mM_Salt', 
                 12: 'Fang_OC4',
                 13: 'Fang_CB4',    14: 'Fang_OC5',  15: 'Fang_CB5',  }
pxy_dict = {    1: (-43449.85, -5850.11), 2: (-37250.02, -5649.95),
                3: (-30900.73, -5398.86),  4:   (-24500.77, -5198.88), 5:   (-18450.22, -5149.98), 6: (-11850.27, -4999.86),
               7: (-5350.54, -4949.91),  8:  (999.23, -4899.85),  9:  (7349.2, -4949.96),  10: (13598.5, -4849.99),
                11: (19648.87, -4899.98),  
                12: (26498.6, -4549.93),    13:  (32748.49, -4549.93),
                14: (39048.52, -4249.92), 15: (45448.18, -3999.93)
       }

## measure at 11:44 pm, 9/2/, Wednesday

## for Fang CB5, OC5, CB4, OC4, CB1, OC1,  no att, 0.1, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );
## for sample 10 - 3 : att= 'Sn60X4',    RE( measure_saxs( meas_t = 1 )   )






def measure_Dinca_waxs(     ):
    ks = list( sample_dict.keys() )
    for k in ks:
        mov_sam( k )
        waxs_angles = np.linspace(0, 65, 11)  
        RE( measure_waxs( meas_t = 1, att= 'None',  my=False, user_name='Dinca',  waxs_angles =  waxs_angles ) )
    


def check_saxs_sample_loc( sleep = 5 ):
    ks = list( sample_dict.keys() )
    for k in ks:        
        mov_sam( k )
        time.sleep( sleep  )




def mov_sam( pos ):    
    px,py = pxy_dict[ pos ]
    RE( bps.mv(piezo.x, px) )
    RE(  bps.mv(piezo.y, py) )
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s...'%(pos, sample ))
    RE.md['sample']  = sample 
    


def measure_waxs( meas_t = .1, att='Sn60X4',  my=False, user_name='', sample=None, saxs_on = False,
                  waxs_angles =  [ 0. ,  6.5, 13. , 19.5]   ):    

    if sample is None:
        sample = RE.md['sample']
    i = 0
    N = len( waxs_angles )  
    dets = [  pil300KW ]  
    for waxs_angle in waxs_angles:
        yield from bps.mv(waxs, waxs_angle)  
        name_fmt = '{sample}_x{x_pos}_y{y_pos}_degwaxs{waxs_angle:05.2f}_{meas_t}s_{att}_att_{scan_id}_sid'
        sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), 
			    y_pos=np.round(piezo.y.position,2), 			
                waxs_angle=waxs_angle,
                meas_t=meas_t, att=att, scan_id=RE.md['scan_id'])
        if saxs_on:
            if i == N-1:
                dets = [ pil1M, pil300KW ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]

                name_fmt = '{sample}_x{x_pos}_y{y_pos}_sax{saxs_z}m_degwaxs{waxs_angle:05.2f}_{meas_t}s_{att}_att_{scan_id}_sid'
                sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), 
			        y_pos=np.round(piezo.y.position,2), 
			        saxs_z=np.round(pil1m_pos.z.position,2), 
                    waxs_angle=waxs_angle,
                    meas_t=meas_t, att=att, scan_id=RE.md['scan_id'])

        if my:
            yield from bps.mvr(piezo.y, 30  )

        det_exposure_time(meas_t, meas_t)  
        sample_id(user_name=user_name, sample_name=sample_name ) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        #yield from bp.scan(dets, waxs, *waxs_arc)
        yield from bp.count(dets, num=1)
        i += 1



def measure_saxs_Dinca_noatt( meas_t = 1, att='None',  my=False, user_name='Dinca', sample=None, ):   
    print(user_name )
    RE( measure_saxs( meas_t =meas_t, att=att,  my=my, user_name=user_name, sample=sample ) )

def measure_saxs_Dinca_Sn60X1( meas_t = 1, att='Sn60X1',  my=False, user_name='Dinca', sample=None, ):   
    print(user_name )
    RE(bps.mv(att1_5, 'Insert'))
    RE( measure_saxs( meas_t =meas_t, att=att,  my=my, user_name=user_name, sample=sample ) )
    RE(bps.mv(att1_5, 'Retract'))


def measure_saxs( meas_t = .1, att='Sn60X4',  my=False, user_name='', sample=None, ):   

    if sample is None:
        sample = RE.md['sample']

    dets = [ pil1M ]
    name_fmt = '{sample}_x{x_pos}_y{y_pos}_sax{saxs_z}m_{meas_t}s_{att}_att_{scan_id}_sid'
    sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), 
			y_pos=np.round(piezo.y.position,2), 
			saxs_z=np.round(pil1m_pos.z.position,2), 
            meas_t=meas_t, att=att, scan_id=RE.md['scan_id'])
    if my:
        yield from bps.mvr(piezo.y, 30  )
    det_exposure_time(meas_t, meas_t)  
    sample_id(user_name=user_name, sample_name=sample_name ) 
    print(f'\n\t=== Sample: {sample_name} ===\n')
    #yield from bp.scan(dets, waxs, *waxs_arc)
    yield from bp.count(dets, num=1)








def do_twaxs_scanx(meas_t = 1): # 2019_2
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

    epics.caput( 'XF:12IDC-ES:2{Det:1M-Ax:Y}Mtr.VAL', -10 )

def _saxs_mode(   ):
    RE( bps.mv(piezo.y, -5649.5 ) )
    epics.caput( 'XF:12IDC-ES:2{Det:1M-Ax:Y}Mtr.VAL', -61.45  )




def movx( dx ):
    RE(  bps.mvr(piezo.x, dx) )


def movy( dy ):
    RE( bps.mvr(piezo.y, dy) )

def get_posxy( ):
    return  round( piezo.x.user_readback.value, 2 ),round( piezo.y.user_readback.value , 2 )

def move_waxs_off( waxs_angle=8.0 ):
    RE(  bps.mv(waxs, waxs_angle)    )
def move_waxs_on( waxs_angle=0.0 ):
    RE(  bps.mv(waxs, waxs_angle)  )





sample_dict =  {  1: 'Fang_OC1', 2: 'Fang_CB1',
                   3: 'YG_P1_18.0wt',   4: 'YG_P2_20.0wt',  5: 'YG_P3_22.0wt', 6: 'YG_P4_24.0wt', 
                 7: 'YG_P5_26.0wt',      8: 'YG_P6_28.0wt',    9: 'YG_P7_30.0wt',  10: 'YG_P8_0.5mM_Salt', 
                 12: 'Fang_OC4',
                 13: 'Fang_CB4',    14: 'Fang_OC5',  15: 'Fang_CB5',  }
pxy_dict = {    1: (-43449.85, -5850.11), 2: (-37250.02, -5649.95),
                3: (-30900.73, -5398.86),  4:   (-24500.77, -5198.88), 5:   (-18450.22, -5149.98), 6: (-11850.27, -4999.86),
               7: (-5350.54, -4949.91),  8:  (999.23, -4899.85),  9:  (7349.2, -4949.96),  10: (13598.5, -4849.99),
                11: (19648.87, -4899.98),  
                12: (26498.6, -4549.93),    13:  (32748.49, -4549.93),
                14: (39048.52, -4249.92), 15: (45448.18, -3999.93)
       }

## measure at 11:44 pm, 9/2/, Wednesday

## for Fang CB5, OC5, CB4, OC4, CB1, OC1,  no att, 0.1, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );
## for sample 10 - 3 : att= 'Sn60X4',    RE( measure_saxs( meas_t = 1 )   )






def measure_Dinca_waxs(     ):
    ks = list( sample_dict.keys() )
    for k in ks:
        mov_sam( k )
        waxs_angles = np.linspace(0, 65, 11)  
        RE( measure_waxs( meas_t = 1, att= 'None',  my=False, user_name='Dinca',  waxs_angles =  waxs_angles ) )
    


def check_saxs_sample_loc( sleep = 5 ):
    ks = list( sample_dict.keys() )
    for k in ks:        
        mov_sam( k )
        time.sleep( sleep  )




def mov_sam( pos ):    
    px,py = pxy_dict[ pos ]
    RE( bps.mv(piezo.x, px) )
    RE(  bps.mv(piezo.y, py) )
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s...'%(pos, sample ))
    RE.md['sample']  = sample 
    


def measure_waxs( meas_t = .1, att='Sn60X4',  my=False, user_name='', sample=None, saxs_on = False,
                  waxs_angles =  [ 0. ,  6.5, 13. , 19.5]   ):    

    if sample is None:
        sample = RE.md['sample']
    i = 0
    N = len( waxs_angles )  
    dets = [  pil300KW ]  
    for waxs_angle in waxs_angles:
        yield from bps.mv(waxs, waxs_angle)  
        name_fmt = '{sample}_x{x_pos}_y{y_pos}_degwaxs{waxs_angle:05.2f}_{meas_t}s_{att}_att_{scan_id}_sid'
        sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), 
			    y_pos=np.round(piezo.y.position,2), 			
                waxs_angle=waxs_angle,
                meas_t=meas_t, att=att, scan_id=RE.md['scan_id'])
        if saxs_on:
            if i == N-1:
                dets = [ pil1M, pil300KW ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]

                name_fmt = '{sample}_x{x_pos}_y{y_pos}_sax{saxs_z}m_degwaxs{waxs_angle:05.2f}_{meas_t}s_{att}_att_{scan_id}_sid'
                sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), 
			        y_pos=np.round(piezo.y.position,2), 
			        saxs_z=np.round(pil1m_pos.z.position,2), 
                    waxs_angle=waxs_angle,
                    meas_t=meas_t, att=att, scan_id=RE.md['scan_id'])

        if my:
            yield from bps.mvr(piezo.y, 30  )

        det_exposure_time(meas_t, meas_t)  
        sample_id(user_name=user_name, sample_name=sample_name ) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        #yield from bp.scan(dets, waxs, *waxs_arc)
        yield from bp.count(dets, num=1)
        i += 1



def measure_saxs_Dinca_noatt( meas_t = 1, att='None',  my=False, user_name='Dinca', sample=None, ):   
    print(user_name )
    RE( measure_saxs( meas_t =meas_t, att=att,  my=my, user_name=user_name, sample=sample ) )

def measure_saxs_Dinca_Sn60X1( meas_t = 1, att='Sn60X1',  my=False, user_name='Dinca', sample=None, ):   
    print(user_name )
    RE(bps.mv(att1_5, 'Insert'))
    RE( measure_saxs( meas_t =meas_t, att=att,  my=my, user_name=user_name, sample=sample ) )
    RE(bps.mv(att1_5, 'Retract'))


def measure_saxs( meas_t = .1, att='Sn60X4',  my=False, user_name='', sample=None, ):   

    if sample is None:
        sample = RE.md['sample']

    dets = [ pil1M ]
    name_fmt = '{sample}_x{x_pos}_y{y_pos}_sax{saxs_z}m_{meas_t}s_{att}_att_{scan_id}_sid'
    sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), 
			y_pos=np.round(piezo.y.position,2), 
			saxs_z=np.round(pil1m_pos.z.position,2), 
            meas_t=meas_t, att=att, scan_id=RE.md['scan_id'])
    if my:
        yield from bps.mvr(piezo.y, 30  )
    det_exposure_time(meas_t, meas_t)  
    sample_id(user_name=user_name, sample_name=sample_name ) 
    print(f'\n\t=== Sample: {sample_name} ===\n')
    #yield from bp.scan(dets, waxs, *waxs_arc)
    yield from bp.count(dets, num=1)








def do_twaxs_scanx(meas_t = 1): # 2019_2
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
      
      
####
'''
============RUN 1===========
    sample_list = ['ED_18', 'ED_19', 'ED_20', 'Q21', 'Q22' ]
    x_list = [-37500, -15500, 8500, 33500, 48500 ]
 ============RUN 1.5===========
    sample_list = ['ED_18_Run2', 'ED_19_Run2' ]
    x_list = [-45000,  -19500  ]
============RUN 2===========
    sample_list = ['Q23',   'Q24',   'Q25',     'Q26',    'Q27',    'JM1',   'JM2'  ]
    x_list = [-46000,     -32000,    -17000,   -2000,     13000,  23000,     41000,             ]
============RUN 3===========
    sample_list = ['JM3',   'JM4',   ]
    x_list = [-45000,     -34000,              ]  
 ============RUN 3.5===========
    sample_list = [   'JM5',     'JM6',    'JM7',    'JM8',   'JM9'  ]
    x_list = [        -19000,   -5000,     11000,    26000,     41000,             ]   

============RUN 4===========
sample_dict =  { 1: 'Fang_813_OC2',   2: 'Fang_812_CB2', 3: 'YG_P1_0wt',   4: 'YG_P2_0wt',  5: 'YG_P3_0wt', 6: 'YG_P4_0wt', 
                 7: 'YG_P5_0wt',      8: 'YG_P6_0wt',    9: 'YG_P7_0wt',  10: 'YG_P8_0wt', 11: 'YG_F7_0wt', 12: 'YG_F6_0wt', 
                 13: 'YG_F5_0wt',    14: 'YG_F4_0wt',  15: 'YG_Au10Free',  }
pxy_dict = { 1: (-43949.77, -5449.94), 2: (-37649.9, -5449.95), 3:(-31250.09, -5549.94), 4: (-24950.16, -5549.99),
             5:   (-18450.22, -5449.98), 6: (-12150.34, -5349.94), 7: (-5750.47, -5349.93), 8:  (549.37, -5099.92),
             9: (6849.25, -5099.93), 10: (13348.99, -5299.99), 11: (19648.87, -4899.98), 12: (26048.75, -4799.96),
             13:  (32348.58, -4599.95), 14:  (38748.47, -4599.93), 15: (45148.37, -4599.93)
       }


#sample12 test beam damage
# sample 13 test beam damage, put Sn60X4, collect 0.1 sec, 10 images, did not see visible beam damage
#                             put Sn60X4, collect 0.5 sec, 10 images, did not see visible beam damage (114176 -- 114185 )
#                             put Sn60X4, collect 1.0 sec, 10 images, did not see visible beam damage (114186 -- 114195 )
#                             put Sn60X4, collect 1.0 sec, 10 images, did not see visible beam damage (114196 -- 114205 )
#                             put Sn60X4, collect 10.0 sec, 10 images, did not see visible beam damage (114206 -- 114215 )  #start see some beam damage!!!

#                             put Sn60X2, collect .1 sec, 10 images, did not see visible beam damage (114216 -- 114215 )  # Seems like some beam damage!!!

# sample 14,  test beam damage, put Sn60X4, collect 1.0 sec, 100 images  (114225 -- 114321 )  for i in range(100):RE( measure_saxs( 1 ) ) 
#  RE( measure_waxs(  saxs_on = True ) ) 

## sample 15 measure att=Sn60X4 and att=1
## Sample 11,  for i in range(100):RE( measure_saxs( 1 ) ) ,   
# for sample P-series, only measure one image, 0.1 sec, with att as SnO4
# for Fang_812_CB2, measure waxs, [ 0. ,  6.5, 13. , 19.5] + [ 26. , 32.5, 39. ] +  [ 45.5, 52. , 58.5, 65. ,71.5, 78. , 84.5] #crashed at angle > 71
#   then measure two SAXS, 1 sec and 0.1 sec, (1 sec is too strong) 
## 



============RUN 5===========
sample_list = ['JM10',   'JM11',    'JM12',     'JM13',    'JM14',    'JM15',   'JM16'  ]
x_list = [   -47000,     -31000,    -16000,      -1000,     11000,   29000,     41000,             ] 

============RUN 6===========
sample_dict =  {   3: 'YG_P1_0.5wt',   4: 'YG_P2_1.0wt',  5: 'YG_P3_1.5wt', 6: 'YG_P4_2.0wt', 
                 7: 'YG_P5_2.5wt',      8: 'YG_P6_3.0wt',    9: 'YG_P7_3.5wt',  10: 'YG_P8_4.0wt',   
                 13: 'Fang_812_OC2',    14: 'Fang_OC5',  15: 'Fang_CB5',  }
pxy_dict = {     3: (-31100.54, -5548.88),  4:  (-24800.7, -5498.89), 5:   (-18450.22, -5349.98), 6: (-12050.27, -5099.88),
               7: (-5750.65, -5149.92),  8: (549.37, -4899.86),  9:  (6949.16, -4949.92),  10: (13348.8, -5099.98),
                11: (19648.87, -4899.98),   12: (26048.75, -4799.96),    13:   (32448.47, -4399.91),
                14:  (38748.47, -4599.93), 15: (45148.37, -4599.93)
       }

## For sample 15, measured at 10:58 pm, measure saxs, 1, 10 sec
## For sample 14, measured at 11:00 pm, measure saxs, 1, 10 sec
## For sample 10- sample 2, measured at 11:02 pm, measure saxs, 1 sec Using att=Sn60um X 4 
## For sample 13, measured at 11:08 pm, no attenuation   RE( measure_waxs( meas_t = 1, att='None', waxs_angles = np.linspace(0, 71.5, 12)  ) )


============RUN 7===========
    sample_list = [    'S1_P3PS_1p10_40mgml_Drop',    'S2_P3SIS_1p10_40mgml_Drop',  'S3_P3PS_1p10_6mgml_Drop3',
                        'S4_P3SIS_1p10_6mgml_Drop', 'S5_P3PS_1p10_6mgml_Spin', 'S6_P3SIS_1p10_6mgml_Spin', 'JM17'  ]
    x_list = [           -33000,     -24000,    -11000,   1000,     11000,    22000,     35000,           ]  

============RUN 7.5===========
Re run ZB S5, S6 
    user_name = 'ZB2' #not change the positon (same as ZB)    
    sample_list = [      'S5_P3PS_1p10_6mgml_Spin', 'S6_P3SIS_1p10_6mgml_Spin'  ]
    x_list = [                11000,    22000          ]  

============RUN 7.52===========
Re run ZB S5, S6 
    user_name = 'ZB3' # change the positon (same as ZB)    
    sample_list = [      'S5_P3PS_1p10_6mgml_Spin', 'S6_P3SIS_1p10_6mgml_Spin'  ]
    x_list = [                13000,    25000          ]  

============RUN 8===========
#SAXS

sample_dict =  {   3: 'YG_P1_4.5wt',   4: 'YG_P2_5.0wt',  5: 'YG_P3_5.5wt', 6: 'YG_P4_6.0wt', 
                 7: 'YG_P5_6.5wt',      8: 'YG_P6_7.0wt',    9: 'YG_P7_7.5wt',  10: 'YG_P8_8.0wt',  
                 12: 'Fang_OC3',
                 13: 'Fang_CB3',    14: 'Fang_OC5',  15: 'Fang_CB5',  }
pxy_dict = {     3: (-31200.81, -5598.87),  4:  (-24800.7, -5498.89), 5:   (-18450.22, -5349.98), 6: (-12050.27, -4999.86),
               7: (-5750.65, -5149.92),  8: (599.2, -5199.87),  9:  (6949.16, -4949.92),  10: (13298.47, -4899.98),
                11: (19648.87, -4899.98),   12: (26198.73, -4799.94),    13:   (32448.47, -4399.91),
                14:  (38748.47, -4599.93), 15: (45148.37, -4599.93)
       }

## measure at 12:49 pm, 9/2/, Wednesday

## for Fang CB5 , no att, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );
#                                    movy(-200); RE( measure_saxs( meas_t = 10, att='None')   )  

## for Fang OC5 , no att, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );movy(-200); RE( measure_saxs( meas_t = 10, att='None')   ) 
## For Fang_CB3, no att, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );movy(-200); RE( measure_saxs( meas_t = 10, att='None')   )
## For Fang_OC3, no att, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );movy(-200); RE( measure_saxs( meas_t = 10, att='None')   )

## for sample 10 - 3 : att= 'Sn60X4',    RE( measure_saxs( meas_t = 1 )   )


============RUN 9===========
WAXS
    user_name='ZB4'  #for new samples
    # define names of samples on sample bar 

    sample_list = [    'S7_PS_10mgml_Spin',    'S8_SIS_10mgml_Spin', 'S9_P3HT_Trans_PIS_1p10_6mgml_Spin',
                       'S10_P3HT_Cis_PIS_1p10_6mgml_Spin', 'S11_P3HT_3mgml_Spin',
                       'S5_P3PS_1p10_6mgml_Spin', 'S6_P3SIS_1p10_6mgml_Spin', ]
                       
    x_list = [        -48000,  -36000,    -26000,  
                      -15000,   -5000,     
                       6000,    16000,   ]


============RUN 9.5===========
 sample_list = [ 'Au5nm_930nM', 'Au10nm_486nM','FeO_10nm_SHS_Wat'   ]


============RUN 10===========
SAXS

sample_dict =  {  1:'HZ_611', 2: 'HZ_614', 
                  3: 'YG_P1_9.0wt',   4: 'YG_P2_10.0wt',  5: 'YG_P3_11.0wt', 6: 'YG_P4_12.0wt', 
                 7: 'YG_P5_13.0wt',      8: 'YG_P6_14.0wt',    9: 'YG_P7_15.0wt',  10: 'YG_P8_16.wt',  
                 11: 'HZ_617',
                 12: 'Fang_OC1',
                 13: 'Fang_CB1',   
                  14: 'Fang_OC5',  15: 'Fang_CB5',  }

pxy_dict = {    1:  (-43950.14, -5749.94), 2: (-37550.02, -5449.92),
                3: (-31200.81, -5598.87),  4: (-24851.07, -5498.96), 5:  (-18450.71, -5249.96), 6: (-12200.61, -4999.91),
               7: (-5751.05, -5049.92),  8: (548.71, -4799.86),  9:  (6948.59, -4799.89),  10: (13298.47, -4899.98),
                11: (19598.28, -5200.05),   12: (26198.73, -4799.94),    13:   (32448.47, -4399.91),
                14:  (38748.47, -4599.93), 15: (45148.37, -4599.93)
       }

## measure at  5:35  pm, 9/2/, Wednesday

## for Fang CB5, OC5, CB1, OC1,  no att, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );movy(-200); RE( measure_saxs( meas_t = 10, att='None')   )  
## for sample 10 - 3 : att= 'Sn60X4',    RE( measure_saxs( meas_t = 1 )   )

## For sample 2,  att= 'Sn60X4',    RE( measure_saxs( meas_t = 1 )   ), 5 meter
##               then move detector to 8 meters,    RE( measure_saxs( meas_t = 1 )   )   test different attenuator, att =1 , 0.1 sec
#                         RE( measure_saxs( meas_t = .1, att='None    )   )   

## sample 1, attSn6X4, 1, 5 s, no att, 0.1 sec

============RUN 11===========
Dinca's sample

sample_dict =  {  2: 'S2_CuHHTT_TEPBF4_Soaked',  3: 'S3_CuHHTT_KNO2_Soaked', 4:'S4_CuHHTT_CsBr_Soaked',
                  5: 'S5_CuHHTT_TEPBF4_Pos',     6: 'S6_CuHHTT_KNO2_Pos',    7:'S7_CuHHTT_CsBr_Pos',
                  8: 'S8_CuHHTT_TEPBF4_Neg',     9: 'S9_CuHHTT_KNO2_Neg',   10:'S10_CuHHTT_CsBr_Neg',
                 11: 'S11_NiBHT_Bare',  

                 #12: 'Fang_OC1',
                 #13: 'Fang_CB1',   

                 15: 'S1_CuHHTT_Bare',  }

pxy_dict = {    1:  (-43950.14, -5749.94), 2: (-37550.02, -5149.92 ),
                3: (-31200.81, -5298.87),  4: (-24851.07, -5098.96), 5:  (-18450.71, -4949.96), 6: (-12000.61, -4999.91),
               7: (-5751.05, -4849.92),  8: (648.71, -4799.86),  9:  (6948.59, -4799.89),  10: (13398.47, -4599.98),
                11: (19698.28, -4600.05),   12: (26198.73, -4799.94),    13:   (32448.47, -4399.91),
                14:  (38748.47, -4599.93), 15: (45148.37, -4299.93)
       }



## measure at  19:18  pm, 9/2/, Wednesday

## for Fang  CB1, OC1,  no att, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );movy(-200); RE( measure_saxs( meas_t = 10, att='None')   )  

## sample all Dou's sample, first measure saxs with det-saxs = 1.600 m
#              measure_saxs_Dinca_Sn60X1( 1  );movy(200); measure_saxs_Dinca_noatt( 1  );
#  then measure waxs, with waxs_angle =  array([ 0. ,  6.5, 13. , 19.5, 26. , 32.5, 39. , 45.5, 52. , 58.5, 65. ])
# using macro,  RE( measure_Dinca_waxs(     ) ) 


============RUN 12===========
SAXS-


sample_dict =  {  1: 'Fang_OC1', 2: 'Fang_CB1',
                   3: 'YG_P1_18.0wt',   4: 'YG_P2_20.0wt',  5: 'YG_P3_22.0wt', 6: 'YG_P4_24.0wt', 
                 7: 'YG_P5_26.0wt',      8: 'YG_P6_28.0wt',    9: 'YG_P7_30.0wt',  10: 'YG_P8_0.5mM_Salt', 
                 12: 'Fang_OC4',
                 13: 'Fang_CB4',    14: 'Fang_OC5',  15: 'Fang_CB5',  }
pxy_dict = {    1: (-43449.85, -5850.11), 2: (-37250.02, -5649.95),
                3: (-30900.73, -5398.86),  4:   (-24500.77, -5198.88), 5:   (-18450.22, -5149.98), 6: (-11850.27, -4999.86),
               7: (-5350.54, -4949.91),  8:  (999.23, -4899.85),  9:  (7349.2, -4949.96),  10: (13598.5, -4849.99),
                11: (19648.87, -4899.98),  
                12: (26498.6, -4549.93),    13:  (32748.49, -4549.93),
                14: (39048.52, -4249.92), 15: (45448.18, -3999.93)
       }

## measure at 11:44 pm, 9/2/, Wednesday

## for Fang CB5, OC5, CB4, OC4, CB1, OC1,  no att, 0.1, 1, 10 sec, RE( measure_saxs( meas_t = 1, att='None')   );
## for sample 10 - 3 : att= 'Sn60X4',    RE( measure_saxs( meas_t = 1 )   )





 







'''




#### 
# proposal_id('2020_2', '304841_Kim')
# RE(shopen())
# 
# Modify file (sample name, x pos), Save file
#
# Check sample stage (SmarAct Y) is around 7000
#
# %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Kim2.py
# RE(run_giwaxs_Kim(t=1)) 
# if do ctrl+C: RE.abort()
#
# RE(shclose())
# Vent: "auto bleed to air", open WAXS soft vent at lower left
# Pump: 'Auto evacuate", when in vac, open valves before and after WAXS chamber


# Note
#
# %run -i /home/xf12id/.ipython/profile_collection/startup/36-Guillaume-beam.py
#
# Data/result: /GPFS/xf12id1/data/images/users/2019_2/304848_Kim/








  




