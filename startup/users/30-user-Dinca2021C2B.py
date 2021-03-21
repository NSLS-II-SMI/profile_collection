##Collect data:


''' 
#SMI: 2021/2/9

SAF: 307138   Standard        Beamline 12-ID   proposal:  308023 (CFN, 307961)
create proposal:  proposal_id( '2021_1', '307138_Dinca' )    #create the proposal id and folder

%run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Dinca2021C2B.py



RE( shopen() )  # to open the beam and feedback
RE( shclose()) 

  


# Energy: 16.1 keV, 0.77009 A
# SAXS distance 8300
# The beam center on SAXS:  [ 490, 565 ]  Or [ 491, 565 ]  #1M X: 1.2, Y -60,  Z: 8300, BS: x: 1.5 ,  

#March 9 night 11:00pm change detector distance to 5000 mm,
# BS change to 2.0 mm , 1M X change to 1.3, Y change t0 -60.3, to make the beam center same as    [ 490, 565 ] 


#March 9 night 11:22 pm change detector distance to 1600 mm,
# BS change to 2.3 mm , 1M X change to 1.6, Y change t0 -60.8, to make the beam center same as    [ 490, 565 ] 



#March 10, 10AM, change back to 5 meter for MIT
detector distance to 5000 mm,
# BS change to 2.0 mm , 1M X change to 1.3, Y change t0 -60.3, to make the beam center same as    [ 490, 565 ] 




FOR MIT CELL,
Cables:
Cell A:
#3, red to red
#2 orange to blue

Cell B:
#9 black to black
#4 brown to brown


WAXS beam center: [  87, 96   ], there is bad pixel here  could check later,  (BS: X: -20.92 )
Put Att and move bs to check the BC_WAXS, --> [ 87, 96 ]




'''

'''
Run1 , using the 3-D printed holder wiithout hole (the optical image quality is not good)

sample_dict = {   1: 'FT_01', 2: 'FT_02', 3:'',
               4: 'FT_04',  5: 'FT_05', 6: 'FT_06', 7:'',
               8: 'FT_07', 9: 'FT_08', 10: 'FT_09', 11:'',
               12: 'GZ_01', 13: '', 14: 'GZ_02', 15: '',16: 'GZ_03',
                17:'', 18:  'GZ_04', 19: '', 20: 'GB_05', 21:'', 22:'GB_06', 23: '', 24: 'GB07',  25: '', 26: 'GZ_08', 
   
      
         }  #All Z from 12-26 is 4800 (ALL GB), 
           



pxy_dict = {    
 
1: (  -44300, -3100),
  2: (  -42300, -2700 ),  4: ( -34300, -2000 ),    5: ( -30800, -2000 ),   
  
  6: (  -27700, -3000 ),  8: ( -19700, 1100 ),    9: ( -17400, 900 ),   
  10: (  -14500, -1100 ),  12: ( -5200, 2500 ),    14: ( 1900, 2200 ),   
  16: (  8500, 1400 ),  18: (  16100 , 3800 ),    20: ( 23000, 3000 ),  
 22: (  30200 , 1700 ),  24: (  38000 , 1500),    26: ( 44800, 1200 ),  
   }


# Run 2, using the 3-D printed holder with rectangle holes (the optical image quality is not good)

sample_dict = {   1: 'FT_03', 2: 'GB_09', 3:'',
               4: 'GB_10', 6: 'GB_11', 8: 'GB_12', 10: 'GB_13', 12: 'GB_14', 
               14: 'GB_15', 16: 'GB_16', 18: 'GB_17', 20: 'GB_18', 22: 'GB_19', 24: 'GB_20', 26: 'GB_21',
      
         }  #All Z 3800 
           

pxy_dict = {    
 
1: (  -44860, 1600 ),
  2: (  -41260, 2700 ),  4: ( -34100, 200 ),      
  
  6: (  -26500, 1100 ),  8: ( -19700, 2600 ),    
  10: (   -12800,  100 ),  12: ( -5200, -900  ),    14: ( 2100, 3200 ),   

  16: (  8800, 1900 ),  18: (  16100 , 4200 ),    20: ( 23000, 4700 ),  
 22: (  30200 , 4700 ),  24: (  38000 , -300 ),    26: ( 44800, 4800 ),  
   }
 

# RUn 3, using the CMS (traditional holder), opticla a little better

sample_dict = {   1: 'GB_22', 2: 'GB_23', 3:'GB_24',
               4: 'GB_25', 5: 'GB_26' , 6: 'GB_27', 7: 'GB_28', 8: 'GB_29', 9: 'GB_30', 10: 'GB_31',  11:'GB_32', 12: 'GB_33', 
               13: 'GB_34', 14: 'GB_35',  15: 'Dummy_Steel'
               
     
      
         }  #All Z 1400 , the direction is oposite to the previous one
           


pxy_dict = {    15:  (-43499.91,  -5019.78) ,  14:  (-37199.98,  -5019.78),  13:(-31099.93,  -5019.78), 12: (-24599.85,  -5019.78),
11: (-17999.94, -5019.78), 10:   (-11600.02, -5019.9), 9: (-5400, -5019.9), 8: (  1100 , -5019.9),  7: (  7600 , -5019.9),  6: ( 13900  , -5019.9), 
 5: (  20200 , -5019.9),  4: (  26500 , -5019.9),  3: (  32800 , -5019.9),  2: (  39200 , -5019.9),  1: ( 45400   , -5019.9),  
   
   }



# Run 4, using the 3-D printed holder with rectangle holes (the optical image quality is not good)

sample_dict = {     2: 'GB_36', 3:'',
               4: 'GB_37', 6: 'GB_38', 8: 'GB_40', 10: 'GB_41', 12: 'GB_44', 
               14: 'GB_42', 16: 'GB_43', 18: 'GB_45',  20: 'FL_UIO66', 
      
         }  #All Z 3800 
           

pxy_dict = {    
 
1: (  -44860, 1600 ),
  2: (  -41260, 2700 ),  4: ( -34100, 200 ),      
  
  6: (  -26500, 1100 ),  8: ( -19700, 2600 ),    
  10: (   -12800,  100 ),  12: ( -5200, -900  ),    14: ( 2100, 3200 ),   

  16: (  8800, 1900 ),  18: (  16100 , 4200 ),    20: ( 23000, 4700 ),  
 22: (  30200 , 4700 ),  24: (  38000 , -300 ),    26: ( 44800, 4800 ),  
   }


# Run 5, using the 3-D printed holder with 15 holes for 2mm capillary 

sample_dict = {     3: 'WX_01_PureS', 4:'WX_02_PureD',
               5: 'WX_03_Mix_SD', 6: 'WX_04_Mix_SDA', 7: 'WX_05_LHCE_1_Mix_LiFSISD', 8: 'WX_06_LHCE_2_Mix_LiFSISDA', 9: 'WX_07_LiFS_S', 10: 'WX_08_LiFS_SA',
               12: 'FL_UIo_66'
      
         }  #All Z 3800 
         #measure 8.3 meter first, measure 1 sec, 10 sec   #piezo_z = 3800 
         #Then move detecter to 5 meter   #piezo_z = 3800 
         # Then change det-dis to 1.6 meter   #piezo_z = 3800 
         # Then measure WAXS, using #piezo_z = 3800 (should use the 1400 , need to re-calibrate )
         # 

           

pxy_dict = {    
 

 3: (-30040, -1800),
 4: ( -22840, -1800),
  5: ( -17240, -1800),
 6: ( -11540, -1800),
7: (  -4140, -4600 ), 
8: (  2060, -1800 ), 
9: ( 7460, -1800),
 10:  ( 13460, 1200 ),  
12: ( 25200, 0 ),   


   }


# Run 6, using the 3-D printed holder for Cell measurements, Cell 2 (bad cell), Cell 3 (good cell )

# change the post, make the hexapod Y = 6.0 ( only change the hexpod height in +/-6 )
# Cell 3 using the Red (rough, Working) and orange (bue, smooth, Counting), the cell is good
# Cell 2 using the black (rough, Working) and brown (bue, smooth, Counting), the cell is not good


sample_dict = {  #1: 'Dinca_Cell_2_NiBHT_K2SO4_Repeat' ,  2: 'Dinca_Cell_3_NiBHT_NaNO3'
 #1: 'Dinca_Cell_2_NiBHT_K2SO4_Repeat' , 
  #2: 'Dinca_Cell_3_NiBHT_NaNO3_V_0p4'
   #2: 'Dinca_Cell_3_NiBHT_NaNO3_V_N0p4',
  #2: 'Dinca_Cell_3_NiBHT_NaNO3_V_N0p5',
    2: 'Dinca_Cell_3_NiBHT_NaNO3_V_0p5',
      
         }  #All Z 4700
         # measure SAXS at 5  meters using 0.2 sec, 1 sec
         # also measrue WAXS using 11 angles first, maybe it only be worthy to measure the zero angle 
         #
          

           

pxy_dict = {    
 

 #1: (-29400, 5400),
 2: (30200, 7200), #(29800, 7400), # (29800, 7300),  #(29600, 7300), #( 31000, 6700 ),
  
}

# Run 7, using the 3-D printed holder for Cell measurements, Cell 5 ( good cell) Cell 6 (bad cell )


sample_dict = { 
    
 #1: 'Dinca_Cell_5_CuHHTT_K2SO4' , 
 #1: 'Dinca_Cell_5_CuHHTT_K2SO4_N0p5' , 
 #1: 'Dinca_Cell_5_CuHHTT_K2SO4_0p5' , 
 #1: 'Dinca_Cell_5_CuHHTT_K2SO4_0p5_2' , 
#1: 'Dinca_Cell_5_CuHHTT_K2SO4_Np5_2' , 


 #2: 'Dinca_Cell_6_CuHHTT_TACl' 
 
 }

#measure no V first, saxs and waxs, three angles, Z=4700
# Only for cell 5, apply -0.5, saxs/waxs
#then apply 0.5 V, saxs, waxs 





pxy_dict = {    
 

 1:          (-28700, 5100), #    (-28900, 4800),       # (-28700, 5100),  #  (-28600, 5100),
 #2: ( 29700, 6000  ),
  
}

# Run 8, Cell 7 and cell 9
#measure no V first, saxs and waxs, three angles, Z=4700, there are cables block beam, open chamber and re-do it

sample_dict = { 
    
    1:  'Dinca_Cell_9_TiBQ_NaClO4' ,
    2: 'Dinca_Cell_7_CuHHTT_CsBr' ,  
}

pxy_dict = {    
 

 1:          (-30100, 5100), 
 2: ( 30800, 7100   ),
  
}


# Run 9, Cell 7 and cell 9
#measure no V first, saxs and waxs, three angles, Z=4700, 
#



sample_dict = { 
    
 # 1:  'Dinca_Cell_9_TiBQ_NaClO4' ,   #measue waxs first then saxs 
#1:  'Dinca_Cell_9_TiBQ_NaClO4_N0p5' ,  #measue waxs first then saxs 
#1:  'Dinca_Cell_9_TiBQ_NaClO4_0p5' ,  #measue waxs first then saxs 
#1:  'Dinca_Cell_9_TiBQ_NaClO4_N0p5_2' ,  #measue waxs first then saxs 

#1:  'Dinca_Cell_9_TiBQ_NaClO4_0p5_2' ,  #measue waxs first then saxs 
#1:  'Dinca_Cell_9_TiBQ_NaClO4_0p5_3' ,  #measue waxs first then saxs 
1:  'Dinca_Cell_9_TiBQ_NaClO4_N0p5_3' ,  #measue waxs first then saxs 





#2:  'Dinca_Cell_7_CuHHTT_CsBr' , 
 #   2:  'Dinca_Cell_7_CuHHTT_CsBr_N0p5'  #measure twice, between this sperate about 5 mim  
    #2:  'Dinca_Cell_7_CuHHTT_CsBr_0p5'
    #2:  'Dinca_Cell_7_CuHHTT_CsBr_0p5_2'
#    2:  'Dinca_Cell_7_CuHHTT_CsBr_N0p5_2'


## Repeat again using a different location
#2:  'Dinca_Cell_7_CuHHTT_CsBr_Repeat' , 
#2:  'Dinca_Cell_7_CuHHTT_CsBr_N0p5_Repeat'   #measue waxs first then saxs 
 # 2:  'Dinca_Cell_7_CuHHTT_CsBr_0p5_Repeat'  #measue waxs first then saxs 
   # 2:  'Dinca_Cell_7_CuHHTT_CsBr_0p5_2_Repeat'   #measue waxs first then saxs 
 #2:  'Dinca_Cell_7_CuHHTT_CsBr_N0p5_2_Repeat' #measue waxs first then saxs 


    
}

pxy_dict = {    
 

 1:          ( -29700, 5300), 

#2:   (30600, 5900), #   ( 30000, 5400   ),
  
}



'''


# Run 9, Cell 4 and cell 8
#measure no V first, saxs and waxs, three angles, Z=4700, 
#


sample_dict = { 
    
#1:  'Dinca_Cell_4_CuHHTT_K2SO4' , 
2:  'Dinca_Cell_1_NiBH_K2S4' ,  

}

pxy_dict = {     

# 1:   ( -29700, 5000), 
2:   (30500, 5200), 
  
}



def _measure_one_potential(   V ='' ):
    mov_sam ( 2 )
    RE.md['sample'] += V
    print( RE.md['sample'])
    RE( measure_waxs() )
    time.sleep(3)
    RE(measure_saxs(1, move_y= False  ) )








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




def measure_saxs( t = .1, att='None', move_y=False, user_name='', sample= None ): 
    if sample is None:
        sample = RE.md['sample']
    dets = [ pil1M ]   
    #att_in( att )    
    name_fmt = '{sample}_x{x_pos}_y{y_pos}_det{saxs_z}m_expt{expt}s_att{att}_sid{scan_id:08d}'
    sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                  saxs_z=np.round(pil1m_pos.z.position,2), expt=t, att=att, scan_id=RE.md['scan_id'])
    if move_y:
        yield from bps.mvr(piezo.y, 30  )
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
    





def measure_series_saxs(       ):
    ks = list( sample_dict.keys() )  #[4:]
    for k in ks:
        mov_sam( k )        
        #movy( 100 )
        RE( measure_saxs( t = 1, att= 'None',  move_y= False, user_name='' ) )
        #movy( 100 )
        #RE( measure_saxs( t = 10, att= 'None',  move_y= False, user_name='' ) )   


def measure_waxs_loop_sample( t = 1.0, att='None', move_y=False, user_name='',  
                              saxs_on = False,   waxs_angles = [ 0. ,  6.5, 13. ]  , inverse_angle = False   ): 
    
    #waxs_angles = np.linspace(0, 65, 11)   #the max range
     #waxs_angles =   np.linspace(0, 65, 11),
    #[ 0. ,  6.5, 13. , 19.5]
    ks = list( sample_dict.keys() )  #[4:]      
    waxs_angle_array = np.array( waxs_angles )
    dets = [  pil300KW ]  
    max_waxs_angle = np.max(  waxs_angle_array )  

    for waxs_angle in waxs_angle_array:
        yield from bps.mv(waxs, waxs_angle)  
        for pos in ks:
            #mov_sam( k )    
            px,py = pxy_dict[ pos ]

            #py += 300


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
    

