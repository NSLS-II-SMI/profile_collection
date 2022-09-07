##Collect data:

#SMI: 2022/7/13
# SAF:    Standard   
# proposal_id('2022_2', '309562_Dinca')


 
# Energy: 16.1 keV, 0.77009 A, low divergence
# SAXS distance , 5 meter 
# WAXS in air
#   setthreshold energy 16100 autog 11000


# WAXS range [ 0, 10, 20 ,40  ]   #[ 0, 5, 15, 25, 45 ]

#  RE( shopen() )  # to open the beam and feedback
#  RE( shclose()) 

#  %run -i    
# for 900kw, 
# move_waxs( 0 )  #the beamstop is 15.7
# put att  14-18keV, Sn 60 um, 7X, move beamstop  -10  
# for waxs=0 --> find the beam center is [218, 308] on albula
# for waxs=1 --> find the beam center is [218, 280] on albula
# for waxs=2 --> find the beam center is [218, 252] on albula
# for waxs=3 --> find the beam center is [218, 223] on albula
# for waxs=4 --> find the beam center is [218, 194] on albula, part block by chip
# for waxs=5 --> find the beam center is [218, 166] on albula
# for waxs=6 --> find the beam center is [218, 138] on albula
# for waxs=7 --> find the beam center is [218, 110] on albula
# for waxs=8 --> find the beam center is [218, 81] on albula 
# for waxs=9 --> find the beam center is [218, 53] on albula 
# for waxs=10 --> find the beam center is [218, 25] on albula 
# for waxs=11 --> find the beam center touch the edge
# for waxs=12 --> find the beam center is out of the detector



# The beam center on SAXS:  
# 5 meter in air, change from  [454, 798 ] with  1M, X -5, Y -20 to:
# 5m, 1M, x=1.04, Y = -61.4   and the correspond beam center is [ 490, 557 ] 
# Using rod:  1.747,  -13    #pindiol, X, -198.5, Y 8.7 
# beamstop_save()
# PZ: -4900 



# in vaccum, 8.3 m,  beam stop postion, X  1.0958 ,  1M, x= 0.74, Y = -61.4   and the correspond beam center is [ 490, 557 ] 
#  beamstop_save()
# PUT YAG in, motor position, X: -30800,Y: 0, HEX X=0, Y=2

# change from 8.3 m to 5 in vacuum,  
# 5m, 1M, x=1.44, Y = -61.4   and the correspond beam center is [ 490, 557 ] 
# Using rod: 2.047,  -13    #pindiol, X, -198.5, Y 8.7 
# beamstop_save()
# PZ: -4900 






from datetime import datetime



# if change anything in this file (macro), please reload it by doing the following line
#     %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Dinca2022C2.py
# change sample name to test
#   sample_id(user_name='test', sample_name='test')

 
smi = SMI_Beamline()


user_name = 'Dinca'
username = 'Dinca'



##Run1,  
# #x,y,z=0,4,0; pizeo,    z=8900 
# sample_dict = {   1:  'AgBH',   }

# ypos = 200
# pxy_dict = {       
# 1:  ( -1200, -3470  ) , 
# }


# Run2 
#sample_dict = {   1:  'Cu_Zn_2_3',   2: 'Zn_S', 3: 'Cu_Zn_3_2', 4: 'Cu_Zn_4_1', 5: 'Mg', 6: 'Cu'}



#ypos = 200
#pxy_dict = {       
#1:  ( -44300, -1000  ) , 2: ( -37900, -1000  ) , 3: (-31500+100, -1000) , 4: (-25100+100, -1000) ,5: (-18800+100, -500) , 6: (-12500, -500)
#}
# t0=time.time();RE(measure_series_multi_angle_wsaxs());run_time(t0)

# sample_dict = {   1:  'TC',   2: 'JO', 3: 'Cu_Zn_1_4', 4: 'Cu_Zn_1_1', 5: 'Zn_B'}
# #ypos = 200
# pxy_dict = {       
# 1:  ( -44200, -1000  ) , 2: ( -37900, -1000  ) , 3: (-31800, -1000) , 4: (-24800, -1000) ,5: (-18800, -1000) 
# }
#t0=time.time();RE(measure_series_multi_angle_wsaxs());run_time(t0)


# Run3,
# sample_dict = {   1:  'BTABQ_Li_FDC' , 2:   'BTABQ_NA_FD_BAD'  }
# #ypos = 200
# pxy_dict = {       
# 1:  ( -31000, -4500  ) , 2: ( 28900 + 500,  -5000 )     
# }

# Run4,

#sample_dict = {    2:   'BTABQ_Li_FDC2'  }
#ypos = 200
#pxy_dict = {     2: ( 28900 ,  -4500 )   }



# Run5,

#sample_dict = {    2:   'BTABQ_Li_DC_ON_TEST'  }
#ypos = 200
#pxy_dict = {     2: ( 27900 ,  -4500 )   }

# # Run6,
# sample_dict = {    2:   'BTABQ_Li_DC_ON'  }
# #ypos = 200
# pxy_dict = {     2: ( 28900 ,  -5000 )   }

# Run7,
#sample_dict = {    2:   'test'  }
#ypos = 200
#pxy_dict = {     2: ( 28900 ,  -5000 )   }
#  overnight_discharge_charge(  2, t=.1, N = 2 ,  sleep_time = 1 * 60 , waxs_angles= [ 0,   5   ])  

# Run8,
#sample_dict = {    2:   'test'  }
#ypos = 200
#pxy_dict = {     2: ( 27900 ,  -4400 )   }

# Run9,  #FOR THE CELL THE MOTOR POSITIONS:  HEX, Y = -9;  pY:  -4500 PZ: 4000 
# sample_dict = {    2:   'BTABQ_Li_DC_ON'  }
# #ypos = 200
# pxy_dict = {     2: ( 28900 ,  -5000 )   }
# # starting: sid00267451


# Run 10:   change sample to detector distance to 8.3 meter, remove the Kaption window and put WAXS in vacuum
# #FOR THE CELL THE MOTOR POSITIONS:  HEX, Y = -9;  pY:  -4500 PZ: 4000 
# beam stop postion, X 1.145 , beam center [433, 554] for 1M in [ -8.96, -61.4 ]
# 8.3 m,  beam stop postion, X  1.0958 ,  1M, x= 0.74, Y = -61.4   and the correspond beam center is [ 490, 557 ] 
#  beamstop_save()
# PUT YAG in, motor position, X: -30800,Y: 0, HEX X=0, Y=2

# sample_dict = {        
#     1: 'MC_HDPE',  2:   'MC_1',   3:   'MC_2',   4:   'MC_3',   5:   'MC_4',  6:   'MC_5',   7:   'MC_6',   8:   'MC_7',   
#     9: 'MC_8',   10:   'MC_9',  11:   'MC_10',  

#     12:  'PNNL_Eampty' ,  13:   'PNNL_B2',   14:   'PNNL_B1',   15:  'PNNL_S15',

#  }  
# dx, dy = 600, 400 
# pxy_dict = {  1:  ( -44600, 600   ),  2:  ( -38000, 500  ),  3:  (  -32000, 500  ),  
# 4:  (  -25800, 400  ),    5:  (  -19300, 200  ),    6:  (  -12800, 300  ),    7:  (  -6400, 0  ),  
# 8:  (  -300, 0  ),    9:  (  6000, -100  ),  
# 10:  (  12400, -100  ),    11:  ( 18800, -200  ),   

#  12:  (  25100, 200  ),    13:  (  31500, -100  ),  
# 14:  (  38150, -100  ),    15:  (  44200, -100  ),  
#             } 
 
#   t0=time.time();RE(measure_series_multi_angle_wsaxs( t=[  1 ], waxs_angles= [ 40, 20, 0 ] , dys = [ 0 ] ));run_time(t0) 
    
# Run 11: Using a 3D printed holder for PNNL, PZ = 2500
# HEX -4, Y 0, 
# sample_dict = {        
#     1: 'PNNL_S2',  2:   'PNNL_S3',   3:   'PNNL_S4',   4:  'PNNL_S5_1',   5:   'PNNL_S5_2',  6:    'PNNL_S6',   7:   'PNNL_S7',   
#     8:   'PNNL_S8',     9:  'PNNL_S9',   10:  'PNNL_S10',  11:   'PNNL_S11',  12: 'PNNL_S12', 13: 'PNNL_S13',
#     14: 'PNNL_S14',  15:  'PNNL_Eampty' ,  16:   'PNNL_B1',   17:   'PNNL_B2',   18:  'PNNL_S1',

#  }  
# dx, dy = 0, 0

# pxy_dict = {  1:  ( -35900, 0   ),  2:  ( -32700, 0  ),  3:  (  -29300, 0  ),  
# 4:  (  -25300, 0  ),    5:  (  -21800, 0  ),    6:  (  -18600, 0  ),    7:  (  -14500, 0  ),  
# 8:  (  -11200, 0  ),    9:  (  -7900, 0  ),  
# 10:  (  -4100, 0  ),    11:  ( -400, 0  ),   
#  12:  (  3100, 0  ),    13:  ( 6600, 0  ),  
# 14:  ( 10200, 0  ),    15:  ( 13900, 0  ),  16: (17600, 0), 17: (21300, 0 ), 18: (28300, 0 )}
# user_name = 'Xu'
# username = 'Xu'

#  t0=time.time();RE(measure_series_multi_angle_wsaxs_PNNL());run_time(t0) 


# Run 12: Using a 3D printed holder for PNNL
# HEX -4, Y 0, 
# move detector back to 5 meter
# 

# sample_dict = {        
#     1: 'PNNL_S2',  2:   'PNNL_S3',   3:   'PNNL_S4',   4:  'PNNL_S5_1',   5:   'PNNL_S5_2',  6:    'PNNL_S6',   7:   'PNNL_S7',   
#     8:   'PNNL_S8',     9:  'PNNL_S9',   10:  'PNNL_S10',  11:   'PNNL_S11',  12: 'PNNL_S12', 13: 'PNNL_S13',
#     14: 'PNNL_S14',  15:  'PNNL_Eampty' ,  16:   'PNNL_B1',   17:   'PNNL_B2',   18:  'PNNL_S1',

#  }  
# dx, dy = 0,  -50 * 21

# pxy_dict = {  1:  ( -35900, 0   ),  2:  ( -32700, 0  ),  3:  (  -29300, 0  ),  
# 4:  (  -25300, 0  ),    5:  (  -21800, 0  ),    6:  (  -18600, 0  ),    7:  (  -14500, 0  ),  
# 8:  (  -11200, 0  ),    9:  (  -7900, 0  ),  
# 10:  (  -4100, 0  ),    11:  ( -400, 0  ),   
#  12:  (  3100, 0  ),    13:  ( 6600, 0  ),  
# 14:  ( 10200, 0  ),    15:  ( 13900, 0  ),  16: (17600+200, 0), 17: (21300+200, 0 ), 18: (28300, 0 )}
# user_name = 'Xu'
# username = 'Xu'
#  t0=time.time();RE(measure_series_saxs_PNNL());run_time(t0)  


# RUN 13, test beam damage for sample 1

# sample_dict = {   1:   'CuHHTT_Test_damage', 2:  'CuHHTT_multi_V'  } 
# #ypos = 200
# pxy_dict = {     1: ( -31000, -4300)   , 2:    ( 28900 ,  -5200 ) }
# # test_beam_damage( 1 )


# RUN 14, test voltage scan code
# dx, dy = 0, 0
# sample_dict = {     2:  'CuHHTT_multi_V'  } 
# #ypos = 200
# pxy_dict = {      2:    ( 28900 ,  -5200 ) }
# #   t0=time.time();RE(measure_series_multi_angle_wsaxs());run_time(t0)


# # RUN 15 
# dx, dy = 0, 0
# sample_dict = {     2:  'CuHHTT_multi_V'  } 
# #ypos = 200
# pxy_dict = {      2:    ( 28900 ,  -6000  ) }
# #  step_voltage_scan(  2, t=2, N = 10 ,    waxs_angles= [ 0,    20,   40   ])



# ## RUN 16, test beam damage for sample 1
# dx, dy = 0, 0
# sample_dict = {   1:   'NiHHTT_Test_damage', 2:  'NiHHTT_multi_V'  } 
# #ypos = 200
# pxy_dict = {     1: ( -31000, -3200)   , 2:    ( 28900 ,  -5200 ) }
# # test_beam_damage( 1 )


# # # RUN 17 
# dx, dy = 0, 0
# sample_dict = {   2:  'NiHHTT_multi_V'  } 
# #ypos = 200
# pxy_dict = {     2:    ( 28900 ,  -5200 ) }
# # #  step_voltage_scan(  2, t=2, N = 10 ,    waxs_angles= [ 0,    20,   40   ])

# Run18, test
#dx, dy = 0, 0
#sample_dict = {    1:   'BTABQ_Na_FDC'  }
# ypos = 200
#pxy_dict = {     1: ( -31000 ,  -4400 )   }
#  overnight_discharge_charge_new(  2, t=2, N = 72 ,  sleep_time = 10 * 60 , waxs_angles= [ 0,    20,   40   ])

# Run19, overnight discharge and charge
dx, dy = 0, 0
sample_dict = {    2:   'BTABQ_Na_ON'  }
# ypos = 200
pxy_dict = {     2: ( 28900 ,  -6300 )   }
#  overnight_discharge_charge_new(  2, t=2, N = 72 ,  sleep_time = 10 * 60 , waxs_angles= [ 0,    20,   40   ])





#  t0=time.time();RE(measure_series_multi_angle_wsaxs());run_time(t0)
#  test_beam_damage( )s
 
 #   t0=time.time();RE(measure_series_multi_angle_wsaxs(t= [  2 ] , waxs_angles= [ 0,    20,   40   ] ,  dys = [ 0  ] ));run_time(t0)







ks =  np.array(list( ( sample_dict.keys()) ) )
pxy_dict =  { k: [ pxy_dict[k][0] + dx,  pxy_dict[k][1] + dy ]  for k in ks   }

x_list = np.array(list( ( pxy_dict.values()) ) )[:,0]
y_list = np.array(list( ( pxy_dict.values()) ) )[:,1]
sample_list =  np.array(list( ( sample_dict.values()) ) )
##################################################
############ Some convinent functions#################
#########################################################



def test_beam_damage( sam, t = 3, N = 30, sleep_time  = 3 ):  
    '''  test_beam_damage( 1 )  '''


    mov_sam( sam  )
    #user_name = 'YZ'    
    #sample = RE.md['sample']  
    for i in range ( N ): 
        print('This is the %s th measurements.'%(i+1))
        RE( measure_waxs( t = t, waxs_angle=0, att='None', dx=0, dy=0, user_name=username, sample= None )  )
        time.sleep( sleep_time )


def get_current_time():
    return datetime.today().strftime("%Y-%m-%d-%H-%M-%S")






def step_voltage_scan(  sam, t=2, N = 10 ,  waxs_angles= [ 0,    20,   40   ]):
    '''   

    step_voltage_scan(  2, t=2, N = 1 ,    waxs_angles= [ 0,    20,   40   ])  
    
    
      '''


    mov_sam( sam )    
    maxA = np.max(waxs_angles ) 
    t0 = time.time()
    for i in range(N):
        t0i = time.time()         
        sample = RE.md['sample']   +  '_run%s_'%i +  get_current_time()
        print( 'This is the %s th measruement for sample=%s.'%( i+1, sample )  )         
        while (time.time() - t0i  )  < 3 * 60:
            time.sleep(  5 ) 
            print('wait 5 second to start the measurement.')
        if abs( waxs.arc.position - maxA ) < 1:
            waxs_angles=  np.sort( waxs_angles )[::-1]
        else:
            waxs_angles=  np.sort( waxs_angles )     
        RE( measure_current_sample(  t=   t  , waxs_angles= waxs_angles,
                       sample = RE.md['sample']   +  '_run%s_'%(i+1) +  get_current_time()   )  ) 

        while (time.time() - t0i  )  <  5 * 60   :
            time.sleep( .5 )    
            #print('wait 5 second for the next voltage.')  
    run_time( t0 )   
        


    





def overnight_discharge_charge(  sam, t=2, N = 96 ,  sleep_time = 10 * 60 , waxs_angles= [ 0,    20,   40   ]):
    '''  #overnight_discharge_charge(  2, t=2, N = 3 ,  sleep_time = 3 * 60 , waxs_angles= [ 0,    20,   40   ]) 
        

        overnight_discharge_charge(  2, t=2, N = 96 ,  sleep_time = 10 * 60 , waxs_angles= [ 0,    20,   40   ])  
    
    
      '''


    mov_sam( sam )    
    maxA = np.max(waxs_angles ) 
    for i in range(N):
        tcur = get_current_time()
        sample = RE.md['sample']   +  '_run%s_'%i + tcur   
        if i == N//2 : 
            RE( bps.mvr(piezo.y, 500  ) ) 
        if abs( waxs.arc.position - maxA ) < 1:
            waxs_angles=  np.sort( waxs_angles )[::-1]
        else:
            waxs_angles=  np.sort( waxs_angles )     
        RE( measure_current_sample(  t=   t  , waxs_angles= waxs_angles, sample =  sample   )  ) 
        time.sleep( sleep_time - 1.38 * 60 )  #1.43 sleep time 

    

 # 2022-07-13 19:10:07

def overnight_discharge_charge_new(  sam, t=2, N = 72 ,  sleep_time = 10 * 60 , waxs_angles= [ 0,    20,   40   ]):
    '''  #overnight_discharge_charge_new(  2, t=2, N = 3 ,  sleep_time = 3 * 60 , waxs_angles= [ 0,    20,   40   ]) 
        

        overnight_discharge_charge_new(  2, t=2, N = 96 ,  sleep_time = 10 * 60 , waxs_angles= [ 0,    20,   40   ])  
    
    
      '''


    mov_sam( sam )    
    maxA = np.max(waxs_angles ) 
    for i in range(N):
        tcur = get_current_time()
        sample = RE.md['sample']   +  '_run%s_'%i + tcur   
        if i == 48 : 
            RE( bps.mvr(piezo.y, 500  ) ) 
        if abs( waxs.arc.position - maxA ) < 1:
            waxs_angles=  np.sort( waxs_angles )[::-1]
        else:
            waxs_angles=  np.sort( waxs_angles )     
        RE( measure_current_sample(  t=   t  , waxs_angles= waxs_angles, sample =  sample   )  ) 
        time.sleep( sleep_time - 1.38 * 60 )  #1.43 sleep time 

     

def measure_current_sample(  t=   2 , waxs_angles= [ 0,  20, 40 ] , sample=None   ):
    
    '''  t0=time.time();RE(measure_one_multi_angle_wsaxs());run_time(t0)   '''  
    maxA = np.max(waxs_angles )  
    for waxs_angle in waxs_angles:   
        print( 'here we go ... ')   
        if waxs_angle == maxA:
            yield from measure_wsaxs(  t = t, waxs_angle= waxs_angle , sample =  sample ) 
        else:
            yield from measure_waxs(  t = t, waxs_angle= waxs_angle , sample =  sample ) 












 

def measure_saxs( t = 1, att='None', dx=0, dy=0, user_name=username,  sample= None ): 

    ''' RE( measure_saxs( sample = 'AgBH_12keV' ) )   '''

    if sample is None:
        #sample = RE.md['sample']
        sample = RE.md['sample_name']
    dets = [ pil1M ]     
    if dy:
        yield from bps.mvr(piezo.y, dy  )
    if dx:
        yield from bps.mvr(piezo.x, dx  )       
    name_fmt = '{sample}_x{x:05.2f}_y{y:05.2f}_z{z_pos:05.2f}_det{saxs_z:05.2f}m_expt{t}s_sid{scan_id:08d}'
    sample_name = name_fmt.format(
                            sample = sample, x=np.round(piezo.x.position,2), y=np.round(piezo.y.position,2), z_pos=piezo.z.position,
                            saxs_z=np.round(pil1m_pos.z.position,2),  t=t, scan_id=RE.md['scan_id'])  
    det_exposure_time( t, t)      
    #sample_name='test'  
    sample_id(user_name=user_name, sample_name=sample_name ) 
    print(f'\n\t=== Sample: {sample_name} ===\n')
    print('Collect data here....')
    yield from bp.count(dets, num=1)
    sample_id(user_name='test', sample_name='test')


def measure_waxs( t = 1, waxs_angle=0, att='None', dx=0, dy=0, user_name=username, sample= None ): 
    '''   RE( measure_waxs( sample = 'AgBH_12keV' ) ) 
    
    RE( measure_waxs( t = 0.01  ) )
    
    
     '''

    if sample is None:
        sample = RE.md['sample']
        #sample = RE.md['sample_name']
    yield from bps.mv(waxs, waxs_angle)            
    dets = [ pil900KW, pil300KW  ]   
    #att_in( att )  
    if dx:
        yield from bps.mvr(piezo.x, dx  )       
    if dy:
        yield from bps.mvr(piezo.y, dy  )
    name_fmt = '{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}'          
    sample_name = name_fmt.format(sample=sample, x_pos=piezo.x.position, y_pos=piezo.y.position, z_pos=piezo.z.position,
                                    waxs_angle=waxs_angle, expt= t,  scan_id=RE.md['scan_id'])   
    det_exposure_time( t, t)  
    sample_id(user_name=user_name, sample_name=sample_name ) 
    print(f'\n\t=== Sample: {sample_name} ===\n')
    print('Collect data here....')
    yield from bp.count(dets, num=1)
    #att_out( att )     
    #sample_id(user_name='test', sample_name='test')   

def measure_wsaxs( t = 1, waxs_angle=15, att='None', dx=0, dy=0, user_name=username, sample= None ): 
    '''   RE( measure_wsaxs( sample = 'AgBH_12keV' ) )  '''

    if sample is None:
        #sample = RE.md['sample']
        sample = RE.md['sample_name']
    yield from bps.mv(waxs, waxs_angle)            
    dets = [ pil900KW, pil300KW , pil1M ]   
    if dx:
        yield from bps.mvr(piezo.x, dx  )   
    if dy:
        yield from bps.mvr(piezo.y, dy  )
    name_fmt = '{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_det{saxs_z}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}'

    sample_name = name_fmt.format(sample=sample, x_pos=piezo.x.position, y_pos=piezo.y.position, z_pos=piezo.z.position,
        saxs_z=np.round(pil1m_pos.z.position,2), waxs_angle=waxs_angle, expt= t,  scan_id=RE.md['scan_id'])   

    det_exposure_time( t, t)  
    sample_id(user_name=user_name, sample_name=sample_name ) 
    print(f'\n\t=== Sample: {sample_name} ===\n')
    print('Collect data here....')
    yield from bp.count(dets, num=1)
    #att_out( att )     
    #sample_id(user_name='test', sample_name='test')   


def measure_series_multi_angle_wsaxs(  t= [  1 ] , waxs_angles= [ 0, 10,  20, 40 ] , 
 dys = [ 0, -500, -500 ]   ):
    
    '''  t0=time.time();RE(measure_series_multi_angle_wsaxs());run_time(t0) 
    
     measure_series_multi_angle_wsaxs(  t= [  1 ] , waxs_angles= [ 0,    20, 40 ] , 
                                         dys = [ 0 ]   ):


      '''
    
    ks = list( sample_dict.keys() )  #[:8 ] 
    maxA = np.max(waxs_angles )  
    for waxs_angle in waxs_angles:        
        for k in ks:
            print( k )
            yield from mov_sam_re( k )                          
            for dy in dys: 
                print( dy )
                print( 'here we go ... ')      
                for ti in t:  
                    RE.md['sample_name']    =     sample_dict[ k  ]  
                    if waxs_angle == maxA:
                        yield from measure_wsaxs(  t = ti, waxs_angle= waxs_angle, att='None',  dy=dy ) 
                    else:
                        yield from measure_waxs(  t = ti, waxs_angle= waxs_angle, att='None',  dy=dy ) 




def measure_series_multi_angle_wsaxs_PNNL(  t= [  0.02, 0.05, 0.1, 0.2, 0.5, 1, 10  ] , waxs_angles= [   40 , 20, 0] , 
     ):
    
    '''  t0=time.time();RE(measure_series_multi_angle_wsaxs_PNNL());run_time(t0)  
      '''    
    ks = list( sample_dict.keys() )  #[:8 ] 
    maxA = np.max(waxs_angles )  
    dy = -50
    for (i, waxs_angle) in enumerate( waxs_angles ) :        
        for k in ks:
            print( k )             
            yield from mov_sam_re( k, dy =  dy*len(t) * i   )             

            for ii, ti in enumerate( t ) :  
                    RE.md['sample_name']    =     sample_dict[ k  ]  
                    if waxs_angle == maxA:
                        yield from measure_wsaxs(  t = ti, waxs_angle= waxs_angle, att='None',  dy=dy ) 
                    else:
                        yield from measure_waxs(  t = ti, waxs_angle= waxs_angle, att='None',  dy=dy ) 



def measure_series_saxs_PNNL(  t= [  0.02, 0.05, 0.1, 0.2, 0.5, 1, 10  ]     ):
    
    '''  t0=time.time();RE(measure_series_saxs_PNNL());run_time(t0)  
      '''    
    ks = list( sample_dict.keys() )  #[:8 ]      
    dy = -50      
    for k in ks:
        print( k )             
        yield from mov_sam_re( k, dy =  0  )   
        for ii, ti in enumerate( t ) :  
                RE.md['sample_name']    =     sample_dict[ k  ]  
                yield from measure_saxs(  t = ti,  att='None',  dy=dy ) 





def run_time( t0 ):
    dt = ( time.time() - t0  ) /60
    print('The Running time is: %.2f min.'%dt )







def measure_XS(   dx=0, dy=0 ,  t=1   ):
    '''suppose the waxs is off the beam'''
    ks = list( sample_dict.keys() )  # [:1]
    measure_WAXS(  ks=ks,  dx=dx, dy=dy ,  t=t   )    
    dy=100
    measure_SAXS(  ks=ks,  dx=dx, dy=dy ,  t=t   )

# def measure_WAXS(   ks, dx=0, dy=0 ,  t=1   ):
#     WA = np.array( [ 0, 5, 15, 25, 45 ])   # [:1]
#     for wa in WA:
#         move_waxs( wa  )
#         _measure_one(   ks=ks, dets=[pil900KW], waxs_angle = wa, dx=dx, dy=dy ,  t=t   )


# def measure_SAXS(   ks, wa=45,  dx=0, dy=0 ,  t= 1   ):
#     move_waxs( wa  )
#     _measure_one(   ks=ks, dets=[pil1M],waxs_angle = wa,  dx=dx, dy=dy ,  t=t   )
#     RE( bps.mvr(  SAXS.y, 30 * 0.172  ) ) 
#     _measure_one(    ks=ks, dets=[pil1M],waxs_angle = wa,  dx=dx, dy=dy ,  t=t   )
#     RE( bps.mvr(  SAXS.y, -30 * 0.172  ) ) 


def _measure_one(  ks, dets, waxs_angle, dx=0, dy=0 ,  t =  1    ):
    for k in ks:
        mov_sam( k )                
        sample = RE.md['sample']       
        u = sample.split('_')[0]
        movx( dx )
        movy( dy ) 
        tcur = time.time()
        name_fmt = '{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_det{saxs_y}_{saxs_z}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}'          
        sample_name = name_fmt.format(sample=sample, 
        x_pos=piezo.x.position, y_pos=piezo.y.position, z_pos=piezo.z.position,                   
                    saxs_y=np.round(pil1m_pos.y.position,2),
                    saxs_z=np.round(pil1m_pos.z.position,2), 
                    waxs_angle=waxs_angle, expt= t, 
                    scan_id=RE.md['scan_id'])   
        det_exposure_time( t, t)  

        sample_id(user_name=User_name, sample_name=sample_name ) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        print('Collect data here....')
        RE(  bp.count(dets, num=1)  )






def snap_waxs( t=0.1  ):     
    dets=  [  pil900KW ] 
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(t)
    yield from( bp.count(dets, num=1) )
    
def snap_saxs( t=0.1  ):     
    dets=  [  pil1M ] 
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(t)
    yield from( bp.count(dets, num=1) )

def mov_sam_re( pos , dy=0):    
    px,py = pxy_dict[ pos ]
    yield from   bps.mv(piezo.x, px)  
    yield from   bps.mv(piezo.y, py + dy )  
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s'%(pos, sample ))
    RE.md['sample']  = sample
    RE.md['sample_name']  = sample


def mov_sam( pos, dy=0 ):    
    px,py = pxy_dict[ pos ]
    RE(  bps.mv(piezo.x, px) )
    RE(  bps.mv(piezo.y, py+dy) )
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s'%(pos, sample ))
    RE.md['sample']  = sample
    RE.md['sample_name']  = sample  
    



def name_sam( pos ):    
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s'%(pos, sample ))
    RE.md['sample']  = sample
    RE.md['sample_name']  = sample     


def check_sample_loc( sleep = 1 ):
    ks = list( sample_dict.keys() )
    for k in ks:        
        mov_sam( k )
        time.sleep( sleep  )
def movx( dx ):
    RE(  bps.mvr(piezo.x, dx) )
def movy( dy ):
    RE( bps.mvr(piezo.y, dy) )
def get_posxy( ):
    return  round( piezo.x.user_readback.value, 2 ),round( piezo.y.user_readback.value , 2 )
def move_waxs( waxs_angle=8.0):
    RE(  bps.mv(waxs, waxs_angle)    )       
def move_waxs_off( waxs_angle=8.0 ):
    RE(  bps.mv(waxs, waxs_angle)    )
def move_waxs_on( waxs_angle=0.0 ):
    RE(  bps.mv(waxs, waxs_angle)  )


def snap_waxs( t=0.1  ):     
    dets=  [  pil300KW ] 
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(t)
    yield from( bp.count(dets, num=1) )    
def snap_saxs( t=0.1  ):     
    dets=  [  pil1M ] 
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(t)
    yield from( bp.count(dets, num=1) )
def measure_pindiol_current():  
    fs.open()
    yield from bps.sleep(0.3)
    pd_curr = pdcurrent1.value
    fs.close()
    print( '--------- Current pd_curr {}\n'.format(pd_curr))
    return pd_curr


def check_sample_name(name):
    """
    Convert special characters to underscore so detectors will not complain
    """
    name = name.translate({ord(c): '_' for c in '=!@#$%^&*{}:/<>?\|`~+'})
    return name




