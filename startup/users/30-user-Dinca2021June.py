##Collect data:

#SMI: 2021/6/7
# SAF: 307522  Standard        Beamline 12-ID   proposal:  308023


# create proposal:  proposal_id('2021_2', '308023_Dinca')    #create the proposal id and folder
# Energy: 16.1 keV, 0.77009 A
# SAXS distance 5000
# SAXS in vacuum and WAXS in air






#  RE( shopen() )  # to open the beam and feedback
#  RE( shclose()) 

#  %run -i    

# The beam center on SAXS:  [ 485, 566 ]
# Energy: 16.1 keV, 0.77009 A
# SAXS distance 5000
## For pindiol: 
#   No filter, it's saturated ( 125257)
#   Sn30 um, X1, still saturated ( 125257 )  #RE(bps.mv(att1_9.open_cmd, 1))
#   Sn30 um, X2, still saturated ( 125256 )  #RE(bps.mv(att1_10.open_cmd, 1))
#   Sn30 um, X3 (X1 + X2) ,  (67713 ) 
#   Sn30 um, X4,  (27456)
# Sn30 um, X5,  (11334 )
#   Sn30 um, X8,  (722) 


# For WAXS, 
#WAXS beam center: [  87, 97   ], there is bad pixel here  could check later,  (BS: X: -20.92 )
#Put Att and move bs to check the BC_WAXS, --> [ 87, 97 ]



########################
#First Run for StanWong

sample_dict = {    2: 'Wong_Blank',
               3: 'Wong_AgNRs1_0P2mM', 4: 'Wong_AgNRs1_0P6mM', 5: 'Wong_AgNRs1_0P8mM', 6: 'Wong_AgNRs1_1P0mM', 7: 'Wong_AgNRs1_1P2mM',
               8: 'Wong_AgNRs2_1P0mM', 9: 'Wong_AgNRs2_1P25mM', 10: 'Wong_AgNRs2_1P5mM',  12: 'Wong_AgNRs1_1P5mM',        
               13: 'Wong_AgNRs2_1P75mM',14: 'Wong_AgNRs2_2P0mM',                   
      
         }

pxy_dict = {   2: ( 40100 , -5000 ),  3: ( 33900 , -5000  ), 4: ( 27600 , -5000  ), 5: ( 21200 , -5300  ), 
6: ( 14700 , -5000 ),  7: ( 8600 , -5300  ), 8: ( 2300 , -5000  ), 9: ( -4000 , -5300  ), 
10: ( -10300 , -5300 ),  12: ( -22900 , -4900  ), 13: ( -29200, -4900  ), 14: ( -35500 , -5200  ), 
   }

# run SAXS and WAXS, # the pizo.z is 1400
# RE(measure_waxs_loop_sample( t = 1, att='None', move_y=False, user_name='',  saxs_on = True,  waxs_angles= np.linspace(0, 65, 11), inverse_angle = False   ))

#############


########################
#Second Run for StanWong

sample_dict = {   
               3: 'Wong_AgNRs1_1P2mM_t10', 4: 'Wong_AgNRs1_1P2mM_t20', 5: 'Wong_AgNRs1_1P2mM_t30', 6: 'Wong_AgNRs1_1P2mM_t45', 7: 'Wong_AgNRs1_1P2mM_t60',
               8: 'Wong_AgNRs1_0P6mM_t10', 9: 'Wong_AgNRs1_0P6mM_t20', 10: 'Wong_AgNRs1_0P6mM_t30', 11: 'Wong_AgNRs1_0P6mM_t45', 12: 'Wong_AgNRs1_0P6mM_t60',              
      
         }

pxy_dict = {      3: ( 33900 , -5000  ), 4: ( 27600 , -5000  ), 5: ( 21200 , -5300  ), 
6: ( 14900 , -5000 ),  7: ( 8700 , -5300  ), 8: ( 2300 , -5000  ), 9: ( -3800 , -5000  ), 
10: ( -10300 , -5000 ), 11: (-16600, -5000),  12: ( -22800 , -4900  ), }
          
# RE(measure_waxs_loop_sample( t = 1, att='None', move_y=False, user_name='',  saxs_on = True,  waxs_angles= np.linspace(0, 65, 11), inverse_angle = False   ))

##NOTE, the first two experiments are conducted with (wrongly) putting attenuator Sn30umX1 in the beam



########################
#Third Run for YG, Au10, 50 nm in PTFE tubing

sample_dict = {   
               1: 'YG_Au10nm_PTFE_WT0P8mm', 2: 'YG_Au50nm_PTFE_WT0P8mm', 3: 'YG_Au10nm_PETF_WT20um', 4: 'YG_Au50nm_PETF_WT20um',  
         }

pxy_dict = {      1: ( 21600, -6000  ), 2: (4100, -6000), 3: (-11800, -6000), 4: (-27000, -6000 )  }

#  measure_series_saxs(  t= [ 0.1, 1, 10  ]    )
#  measure_series_saxs(  t= [ 0.1, 1, 10  ] , move_y=True   )  #do a repeat
# Manually measure
#  RE( measure_saxs(  t = 1 ) )

#### Then start the battery setup


#########################
#June 8, setup cell ready
# Fourth Run

sample_dict = {  1: 'Dinc_Cell1_BTABQ1', 2: 'Dinc_Cell2_BTABQ2',  }
#pxy_dict = {      1: ( 33100, -4900 ), 2:  ( -26300, -4900 ),  } #good position
#pxy_dict = {      1: ( 33100, -6800 ), 2:  ( -26300, -4900 ),  } #this position is not good
pxy_dict = {      1: ( 32300, -4000 ), 2:  ( -26300, -4900 ),  } #this position is good

## Fifth Run
# Reconnect the cell, and found a problem with one holder
# After adding a washer to the other holder, the conections looks good,
#  1) do a CV for cell2
# 2) apply -0.2V for 1200 s, 
# 3) after applying valtage 120 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P2_1_' )

# 4) apply -0.3V for 1200 s, 
# 5) after applying valtage 90 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P3_1_' )


# 6) apply -0.4V for 1200 s, 
# 7) after applying valtage 90 sec, do  measure_one_potential(  sam_pos=2, t=1,   V ='N0P4_1_' )

# 8) apply -0.2V for 1200 s, 
# 9) after applying valtage 120 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P2_2_' )

# 10) apply -0.8V for 1200 s, 
# 11 after applying valtage 120 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P8_1_' )


# 12) apply noV for 1200 s, 
# 13) after applying valtage 120 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='noV_1' )


## Six Run
sample_dict = {  1: 'Dinc_Cell5_NiTIBQ2', 2: 'Dinc_Cell3_BTABQ3',  }
pxy_dict = {      1: ( 32300, -4000 ), 2:  ( -26300, -4900 ),  } #this position is  good
pxy_dict = {      1: ( 32300, -5200 ), 2:  ( -26300, -4900 ),  } #another location 
# (1)  for cell5, don't apply any potential, do measure_one_potential(  sam_pos=1, t=1,   V ='' )
# (2)  for cell5, don't apply any potential, move to a new pos, do measure_one_potential(  sam_pos=1, t=1,   V ='' )
# (3) for cell3, before apply potential, do  measure_one_potential(  sam_pos=2, t=1,   V ='' )
#pxy_dict = {      1: ( 32300, -5200 ), 2:  ( -26700, -6500 ),  } #another location 
# (4) for cell3, before apply potential, do  measure_one_potential(  sam_pos=2, t=1,   V ='' )
# Lunch
# Change back to the first postion
#  1) do a CV for cell3, looks good
# 2) after CV do a measure, measure_one_potential(  sam_pos=2, t=1,   V ='AfterCV_N0P25_' )
#apply -0.2V for 1200 s, 
# 3) after applying valtage 120 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P2_1_' )
# 4) apply -0.2V for 1200 s, 
# 5) after applying valtage 90 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P2_2_' )
# 6) apply -0.2V for 1200 s, #NOTE: apply 0.2 (wrongly), then apply -0.4V
# 7) after applying valtage 200 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P2_3_' )
# 8) apply -0.2V for 1200 s
# 9) after applying valtage 200 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P2_4_' )

# 10) apply 0.25V for 1200 s
# 11) after applying valtage 200 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='P0P25_1_' )
# 12) apply 0.2V for 1200 s
# 13) after applying valtage 200 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='P0P2_1_' )

# 14) apply -0.6V for 1200 s
# 15) after applying valtage 200 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='N0P6_1_' )

# 16) apply 0.55V for 1200 s
# 17) after applying valtage 200 sec, do measure_one_potential(  sam_pos=2, t=1,   V ='P0P55_1_' )

 

## Seven Run
sample_dict = {  1: 'Dinc_Cell6_NiTIBQ3'  }
pxy_dict = {      1:   ( -26300, -4900 ),  } #this position is  good
 
# (1)  for cell6, don't apply any potential, do measure_one_potential(  sam_pos=1, t=1,   V ='' )
# (2) Do a CV, the cell is not good
# change to cell4




## Eight Run
sample_dict = {  1: 'Dinc_Cell4_NiTIBQ1'  }
pxy_dict = {      1:   ( -26300, -4900 ),  } #this position is  good
 
# (1)  for cell6, don't apply any potential, do measure_one_potential(  sam_pos=1, t=1,   V ='' )
pxy_dict = {      1:   ( -27000, -4500 ),  } #this position is  good
# (2)  for cell6, don't apply any potential, do measure_one_potential(  sam_pos=1, t=1,   V ='' )
pxy_dict = {      1:   ( -25900, -4200 ),  } #this position is  good
# (3)  for cell6, don't apply any potential, do measure_one_potential(  sam_pos=1, t=1,   V ='' )
pxy_dict = {      1:   ( -27100, -4500 ),  } #this position is  good
# (4)  for cell6, don't apply any potential, do measure_one_potential(  sam_pos=1, t=1,   V ='' )
# Then do a CV, Cell looks good

# (5) after CV do a measure, measure_one_potential(  sam_pos=1, t=1,   V ='AfterCV_N0P2_' )
#apply -0.2V for 1200 s, 
# 6) after applying valtage 120 sec, do measure_one_potential(  sam_pos=1, t=1,   V ='N0P2_1_' )
# 7) apply -0.2V for 1200 s, 
# 8) after applying valtage 120 sec, do measure_one_potential(  sam_pos=1, t=1,   V ='N0P2_2_' )
# 9) apply -0.2V for 1200 s, 
# 10) after applying valtage 120 sec, do measure_one_potential(  sam_pos=1, t=1,   V ='N0P2_3_' )
# 11) apply -0.25V for 1200 s, 
# 12) after applying valtage 120 sec, do measure_one_potential(  sam_pos=1, t=1,   V ='N0P25_1_' )
# 13) apply 0.3 V for 1200 s, 
# 14) after applying valtage 120 sec, do measure_one_potential(  sam_pos=1, t=1,   V ='P0P3_1_' )
# 15) apply 0.25 V for 1200 s, 
# 16) after applying valtage 120 sec, do measure_one_potential(  sam_pos=1, t=1,   V ='P0P25_1_' )
# 17) apply 0.25 V for 1200 s, 
# 18) after applying valtage 120 sec, do measure_one_potential(  sam_pos=1, t=1,   V ='P0P25_2_' )

# 19) apply -0.8 V for 7200 s, 
# 20) after applying this valtage for about 0.5h, do measure_one_potential(  sam_pos=1, t=1,   V ='N0P8_1_' )



## Nineth Run, change to cell 3

sample_dict = {  1: 'Dinc_Cell3_BTABQ3_Repeat'  }
pxy_dict = {      1:   ( -26700, -4500 ),  } #this position is  good
 
# (1)  for cell3, don't apply any potential, do measure_one_potential(  sam_pos=1, t=1,   V ='' )
# (2 ) Do a CV, looks good, (after CV, the V=-580 mV)
# (3) apply -0.4, for 7200 s, 
# (4)  after wait half hour, measure_one_potential(  sam_pos=1, t=1,   V ='N0P4_1_' )











#######Funcion for cell measurements




def measure_one_potential(  sam_pos=1, t=1,   V ='' ):
    mov_sam ( sam_pos )
    if V !='':
        RE.md['sample'] += V
    print( RE.md['sample'])
    current_waxs_arc = waxs.arc.user_readback.value
    if current_waxs_arc >=10:
        inverse_angle = True
    else:
        inverse_angle = False    
    RE( measure_waxs( t=t, waxs_angles = [ 0. ,  6.5, 13. ], saxs_on=True, inverse_angle=inverse_angle ) )
    #time.sleep(3)
    #RE(measure_saxs(1, move_y= False  ) )

 
 


##################################################
############ Some convinent functions#################
#########################################################

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
def mov_sam( pos ):    
    px,py = pxy_dict[ pos ]
    RE(  bps.mv(piezo.x, px) )
    RE(  bps.mv(piezo.y, py) )
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s...'%(pos, sample ))
    RE.md['sample']  = sample       
def check_saxs_sample_loc( sleep = 5 ):
    ks = list( sample_dict.keys() )
    for k in ks:        
        mov_sam( k )
        time.sleep( sleep  )


def measure_pindiol_current():  
    fs.open()
    yield from bps.sleep(0.3)
    pd_curr = pdcurrent1.value
    fs.close()
    print( '--------- Current pd_curr {}\n'.format(pd_curr))
    return pd_curr




def measure_waxs_loop_sample( t = 1, att='None', move_y=False, user_name='',  
                              saxs_on = True,   waxs_angles =   np.linspace(0, 65, 11), inverse_angle = False   ): 
    
    #waxs_angles = np.linspace(0, 65, 11)   #the max range
    #[ 0. ,  6.5, 13. , 19.5]
    ks = list( sample_dict.keys() )       
    waxs_angle_array = np.array( waxs_angles )
    dets = [  pil300KW ]  
    max_waxs_angle = np.max(  waxs_angle_array )  
    for waxs_angle in waxs_angle_array:
        yield from bps.mv(waxs, waxs_angle)  
        for pos in ks:
            #mov_sam( k )    
            px,py = pxy_dict[ pos ]
            #py += 200
            print( px, py )
            yield from  bps.mv(piezo.x, px)  
            yield from  bps.mv(piezo.y, py) 
            sample = sample_dict[pos]  
            print('Move to pos=%s for sample:%s...'%(pos, sample ))
            RE.md['sample']  = sample             
            sample = RE.md['sample']
            name_fmt = '{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}'          
            sample_name = name_fmt.format(sample=sample, x_pos=piezo.x.position, y_pos=piezo.y.position, z_pos=piezo.z.position,
                                      waxs_angle=waxs_angle, expt= t,  scan_id=RE.md['scan_id'])   
            print( sample_name )
            if saxs_on:
                if waxs_angle == max_waxs_angle:
                    dets = [ pil1M, pil300KW ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]                
                else:
                    dets=  [  pil300KW ] 
            if move_y:
                yield from bps.mvr(piezo.y, 100  )
            det_exposure_time( t, t )  
            sample_id(user_name=user_name, sample_name=sample_name ) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            #yield from bp.scan(dets, waxs, *waxs_arc)
            yield from bp.count(dets, num=1)        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 



def measure_series_saxs(  t= [ 1 ] ,  move_y = False   ):
    ks = list( sample_dict.keys() )     
    for k in ks:
        mov_sam( k )    
        for ti in t:        
            RE( measure_saxs(  t = ti, att='None', move_y=move_y ) )


def measure_series_saxs_waxs(  t=1 , waxs_angles= np.linspace(0, 65, 11)    ):
    ks = list( sample_dict.keys() )
    inverse_angle = True
    for k in ks:
        mov_sam( k )    
        inverse_angle = not inverse_angle         
        RE( measure_waxs( t = t, att= 'None', saxs_on=True, move_y= False, user_name='', waxs_angles = waxs_angles  , inverse_angle = inverse_angle ) )




def measure_saxs( t = 1, att='None', move_y=False, user_name='', sample= None ): 
    if sample is None:
        sample = RE.md['sample']
    dets = [ pil1M ]   
    #att_in( att )    
    name_fmt = '{sample}_x{x_pos}_y{y_pos}_det{saxs_z}m_expt{expt}s_att{att}_sid{scan_id:08d}'
    sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                  saxs_z=np.round(pil1m_pos.z.position,2), expt=t, att=att, scan_id=RE.md['scan_id'])
    if move_y:
        yield from bps.mvr(piezo.y, -200  )
    det_exposure_time( t, t)  
    sample_id(user_name=user_name, sample_name=sample_name ) 
    print(f'\n\t=== Sample: {sample_name} ===\n')
    print('Collect data here....')
    yield from bp.count(dets, num=1)
    #att_out( att ) 
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)    
    
    
def measure_waxs( t = 1.0, att='None', move_y=False, user_name='',  
                              saxs_on = False,   waxs_angles = [ 0. ,  6.5, 13. ]  , inverse_angle = False   ): 
    
    #waxs_angles = np.linspace(0, 65, 11)   #the max range
     #waxs_angles =   np.linspace(0, 65, 11),
    #[ 0. ,  6.5, 13. , 19.5]
     
    waxs_angle_array = np.array( waxs_angles )
    if inverse_angle:
        waxs_angle_array = waxs_angle_array[::-1]
    dets = [  pil300KW ]  
    max_waxs_angle = np.max(  waxs_angle_array )  

    for waxs_angle in waxs_angle_array:
        yield from bps.mv(waxs, waxs_angle)             
        sample = RE.md['sample']
        name_fmt = '{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}'          
        sample_name = name_fmt.format(sample=sample, x_pos=piezo.x.position, y_pos=piezo.y.position, z_pos=piezo.z.position,
                                    waxs_angle=waxs_angle, expt= t,  scan_id=RE.md['scan_id'])   
        print( sample_name )
        if saxs_on:
            if waxs_angle == max_waxs_angle:
                dets = [ pil1M, pil300KW ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]                
            else:
                dets=  [  pil300KW ] 
        if move_y:
            yield from bps.mvr(piezo.y, 100  )
        det_exposure_time( t, t )  
        sample_id(user_name=user_name, sample_name=sample_name ) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        #yield from bp.scan(dets, waxs, *waxs_arc)
        yield from bp.count(dets, num=1)        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 
    

