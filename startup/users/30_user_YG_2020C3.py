##Collect data:

#SMI: 2020/10/29
# SAF: 306460   Standard        Beamline 12-ID   proposal:  308052


# create proposal:  proposal_id( ‘2020-3’, ‘308052_YZhang’ )   #create the proposal id and folder
#  RE( shopen() )  # to open the beam and feedback
#  RE( shclose()) 

#  %run -i   /nsls2/xf12id2/analysis/2020_2/304231_Dinca/For_2020_C3/30_user_YG_2020C3.py


import numpy as np
#import epics      

#    https://drive.google.com/drive/folders/15wPQSS7Yb2wZ5GoTx-9JoZNSxrvAMoj1
#    https://docs.google.com/document/d/1eFpFRN5HJ_l2nazW8xhwPi9cdxiZXZ_NwRl01ZTjL9U/edit    
#    https://docs.google.com/document/d/1arOvFhw9EqUReIXSSqxq4s44RZKGtMVt4EPXn9AtBtc/edit


T = True
F = False


#def sample dict and sample position for T saxs/waxs

sample_dict =  {  1: 'Fang_OC1', 2: 'Fang_CB1',  }
pxy_dict = {    1: (-43449.85, -5850.11), 2: (-37250.02, -5649.95) }



samples = [ 'T1_nPTFE_Pd_Precursor_t0', 'T2_nPTFE_Pd_Cube_Nwash', 'T3_oPTFE_Pd_Precursor_t0', 'T4_oPTFE_Pd_Cube_Nwash', 
'T5_oPTFE_Pd_Cube_Nwash_inDrop','T6_oPTFE_Pd_Cube_Awash','T7_oPTFE_Pd_Cube_Sup1', 'T8_oPTFE_Pd_Cube_Sup2', 
'T9_oPTFE_Pd_Cube_Sup3', 'T10_oPTFE_water', 'T11_oPTFE_oil', 'T12_oPTFE_ethanol',  ]

samples = [ 'Cap1_Cube_Awash', 'Cap2_Cube_Nwash','Cap3_Pd_Precursor_t0', 
            'Cap4_Au50_solution_30',  'Cap5_Ag40_solution_30','Cap6_Au50Ag40_20_10',
            'Cap7_Au50Ag40_15_15','Cap8_Au50Ag40_20_10',]

samples = [  'HB_Cell_1', 'HB_Cell_2','HB_Cell_3', ] 


samples = [ 'AM_S53_80nM_60min',  'AM_S61_80nM_10min', 'AM_S69_80nM_30min', 'AM_S41_Origami_units_form_factor',  ]

samples = [  'SW_Ag100nm_1min', 'SW_Ag100nm_30min','SW_Ag100nm_60min',
            'SW_Ag16nm_1min', 'SW_Ag16nm_30min','SW_Ag16nm_60min' ]    


samples = [  'CW1_3D_Octa_peptoid_NP10_EDTA12', 'CW2_3D_Octa_peptoid_NP2_EDTA12', 'CW3_3D_Octa_peptoid_NP0.5_EDTA12',
           'CW4_3D_Octa_peptoid_NP0.1_EDTA12', 'CW5_3D_Octa_EDTA12', 'CW6_3D_Octa_peptoid_NP10_EDTA6', 'Cw7_3D_Octa_peptoid_NP2_EDTA6',
           'CW8_3D_Octa_peptoid_NP0.5_EDTA6', 'CW9_3D_Octa_peptoid_NP0.1_EDTA6', 'CW10_3D_Octa_EDTA6',
           'CW11_3D_Octa_peptoid_NP10', 'CW12_3D_Octa_peptoid_NP2', 'CW13_3D_Octa_peptoid_NP0.5',
           'CW14_3D_Octa_peptoid_NP0.1', 'CW15_3D_Octa',
           'CW16_3D_Octa_peptoid_NP10_EDTA3', ]
samples = [        
           'CW17_3D_Octa_peptoid_NP2_EDTA3', 'CW18_3D_Octa_peptoid_NP0.5_EDTA3', 'CW19_3D_Octa_peptoid_NP0.1_EDTA3', 
    'CW20_3D_Octa_EDTA3', 'CW21_3D_Octa', 'CW22_Buffer_peptoid_NP10_EDTA_12', 'CW23_Buffer_peptoid_NP2_EDTA_12',
    'CW24_Buffer_peptoid_NP0.5_EDTA_12', 'CW25_Buffer_peptoid_NP0.1_EDTA_12', 'CW26_Buffer_EDTA_12', 
    'CW27_Buffer_peptoid_NP10_EDTA_6',    'CW28_Buffer_peptoid_NP2_EDTA_6', 'CW29_Buffer_peptoid_NP0.5_EDTA_6',
    'CW30_Buffer_peptoid_NP0.1_EDTA_6',            
          ]
           
           
samples = [  'CW%s' for i in range(31, 44) ]

'''Buffer_EDTA_6
Buffer_peptoid_NP10
Buffer_peptoid_NP2
Buffer_peptoid_NP0.5
Buffer_peptoid_NP0.1
Buffer
Buffer_peptoid_NP10_EDTA_3
Buffer_peptoid_NP2_EDTA_3
Buffer_peptoid_NP0.5_EDTA_3
Buffer_peptoid_NP0.1_EDTA_3
Buffer_EDTA_3
Octa20_3D1
3D_Octa        
           
'''


#beam center:  [486, 560 ]

##first run
sample_dict =  {  1:'CW1_3D_Octa_peptoid_NP10_EDTA12', 2: 'CW2_3D_Octa_peptoid_NP2_EDTA12', 3: 'CW3_3D_Octa_peptoid_NP0.5_EDTA12',
           4:'CW4_3D_Octa_peptoid_NP0.1_EDTA12', 5:'CW5_3D_Octa_EDTA12', 6:'CW6_3D_Octa_peptoid_NP10_EDTA6', 
                7: 'Cw7_3D_Octa_peptoid_NP2_EDTA6', 8:'CW8_3D_Octa_peptoid_NP0.5_EDTA6', 
                9:'CW9_3D_Octa_peptoid_NP0.1_EDTA6', 10:'CW10_3D_Octa_EDTA6', 11:'CW11_3D_Octa_peptoid_NP10', 
                12:'CW12_3D_Octa_peptoid_NP2', 13: 'CW13_3D_Octa_peptoid_NP0.5',
                14: 'CW14_3D_Octa_peptoid_NP0.1', 15: 'CW15_3D_Octa',  }

##second run
            
sample_dict = {   1: 'CW16_3D_Octa_peptoid_NP10_EDTA3', 2: 'CW17_3D_Octa_peptoid_NP2_EDTA3',
               3: 'CW18_3D_Octa_peptoid_NP0.5_EDTA3', 4: 'CW19_3D_Octa_peptoid_NP0.1_EDTA3', 
               5:    'CW20_3D_Octa_EDTA3', 6: 'CW21_3D_Octa', 7: 'CW22_Buffer_peptoid_NP10_EDTA_12',
               8: 'CW23_Buffer_peptoid_NP2_EDTA_12', 9:  'CW24_Buffer_peptoid_NP0.5_EDTA_12',
               10: 'CW25_Buffer_peptoid_NP0.1_EDTA_12', 11: 'CW26_Buffer_EDTA_12', 
              12:  'CW27_Buffer_peptoid_NP10_EDTA_6', 13:  'CW28_Buffer_peptoid_NP2_EDTA_6',
              14:   'CW29_Buffer_peptoid_NP0.5_EDTA_6', 15:      'CW30_Buffer_peptoid_NP0.1_EDTA_6',     
      
         }
           

pxy_dict = {    1:  (-43004.21, -5099.91) , 2: (-36809.79, -5340.42),
            
            3: (-30409.24, -5240.42),             
            4: (-24108.99, -5240.34),
            5: (-17808.47, -5100.3), 
            
            6: (-11108.52, -5300.21),
            7: (-4707.9, -5100.22),
            8: (1392.26, -5100.23),
            
            9:(7692.53, -5100.2),
            10:  (14193.11, -5000.21), 
            11: (20393.36, -5300.21),            
            12 : (26793.74, -5200.11),            13 : (32894.22, -4800.08),
            14: (39494.99, -4599.97),
            15: (45895.71, -4699.95),
                   
           
           }

## third run
sample_dict = { i-30: 'CW%s'%i for i in range( 31, 44) }

## fourth run
sample_dict = { i: 'GB%s'%i for i in range( 1, 16) }

## fifth run, finished at 1:30 pm
sample_dict = { i - 15: 'GB%s'%i for i in range( 16, 31) }


# sixth run
sample_dict = { 2: 'AM_S61_80nM_10min', 3: 'AM_S69_80nM_30min', 
               5: 'Al_125um_window',
                4: 'AM_S53_80nM_60min',  6: 'AM_S41_Origami_units_form_factor', 
                               
                }


# seventh run
sample_dict = {  2:  'SW_Ag16nm_1min'   }

# only measure the second one
#  RE(measure_waxs(  t = 1, att='None', move_y=False, user_name='', sample= None, 
#                    saxs_on = True,   waxs_angles =   np.linspace(0, 65, 11), inverse_angle = False    ))   



sample_dict = {}

# eigth run
sample_dict = {  2:  'SW_Ag100nm_5min', 3: 'SW_Ag100nm_10min', 4: 'SW_Ag100nm_15min' ,   
                 5:  'SW_Ag100nm_20min',6: 'SW_Ag100nm_25min',7: 'SW_Ag100nm_30min',  
                 8:  'SW_Ag100nm_40min',9: 'SW_Ag100nm_60min',10: 'SW_Ag100nm_1min',
                 11:  'SW_Ag16nm_5min',12: 'SW_Ag16nm_10min',13: 'SW_Ag16nm_25min',
                 14:  'SW_Ag16nm_30min',15: 'SW_Ag16nm_40min',               }
pxy_dict = {  2: (-37009.72, -5140.4),
            3: (-30709.35, -5140.41),             
            4: (-24409.03, -5140.41),
            5: (-17908.56, -5000.29),             
            6: (-11708.57, -5000.3),
           7: (-5308.09, -4900.21),
            8: (1192.19, -5100.25),            
            9: (7392.38, -4900.18),           
            10:  (13793.12, -4800.27),             
            11:  (20093.12, -4500.22),            
            12 : (26493.79, -5000.25),
            13 : (32894.19, -4600.07),
            14: (39194.69, -4999.98),
            15: (45595.46, -4299.93), } 



samples = [ 'Cap1_Cube_Awash', 'Cap2_Cube_Nwash','Cap3_Pd_Precursor_t0', 
            'Cap4_Au50_solution_30',  'Cap5_Ag40_solution_30','Cap6_Au50Ag40_20_10',
            'Cap7_Au50Ag40_15_15','Cap8_Au50Ag40_20_10',]



sample_dict = {}
# nineth run
sample_dict = {  1:  'SW_Ag100nm_50min', 2: 'SW_Ag100nm_60min', 3: 'SW_Ag100nm_90min' ,   
                 4: 'YG_R1_Cap4_Au50_solution_30', 6: 'YG_R3_Cap6_Au50Ag40_20_10',  
                 7:  'YG_R4_Cap7_Au50Ag40_15_15'  ,8: 'YG_R5_Cap8_Au50Ag40_10_20',
                 9: 'YG_Cap2_PdCubeA_Nwash',10: 'YG_Cap1_PdCubeB_wash',
                 11:  'YG_Cap3_Pd_Precursor_t0',13: 'FL_CB4', 14: 'FL_OC4',               }
pxy_dict = {   1: (-43104.35, -5199.92) ,    
    2: (-36809.88, -5440.41),
            3: (-30409.31, -5140.41),             
            4: (-24409.03, -5140.41),
            #5: (-17708.71, -5400.3),             
            6: (-11708.57 + 300, -5000.3),
           7: (-5308.09 +300, -4900.21),
            8: (1192.19 +200, -5100.25),            
            9: (7392.38+300, -4900.18 - 200),           
            10:  (13793.12 + 300, -4800.27),             
            11:  (20093.12 +300 , -4500.22 - 400),            
            #12 : (26493.79, -5000.25),
            13 : (33194.04, -4900.06),
            14: (39494.76, -4799.97), }
            #15: (45595.46, -4299.93), } 


# 10 -th run
#change sdd from 6.5 to 5 meter
#SAXS 2 mm beam stop: X from -199.7 to -199.1, Y keep same ( 8.799)
#SAXS 3 mm keep same (X -205, paddle, 288.998, Y 0, )
#pil1M X change from -0.5 to 0.9 (beam center is roughly the gap center), Y keep same -61, Z 5000
# New beam cetner [ 490, 561 ]
#Then change back to 6.5 meter
#pizeo_z: 1400 (same for all above)
# then change pil1M X to 0.5 (shoud be -0.5 )


sample_dict = {}
sample_dict = {   3: 'YG_GlassCap',   4: 'YG_QuartzCap', 5: 'YG_R2_Cap3_Ag40_solution_30', }
                 # 7: 'FL_CB4', 8: 'FL_OC4',               }
pxy_dict = {  3: ( -30809.2, -4840.45 ) ,                
            4: (-24509.22, -4640.39),
            5: ( -18108.84, -4900.29 ),  
           7: ( (-5408.18, -4900.27) ),
            8: ( (992.01, -4900.24) ),     } 

#RE(measure_waxs_loop_sample()) , the frist run is probably wrongly put the attenuators
# take the att out and run again,   RE(measure_waxs_loop_sample(  inverse_angle = True ))


# 11 -th run
# investigate the smarAct Z for WAXS using FLCB4 and FLOC4
#pizeo_z: 1400 (same for all above)

sample_dict = {}
sample_dict = { #  3: 'YG_GlassCap',   4: 'YG_QuartzCap', 5: 'YG_R2_Cap3_Ag40_solution_30', }
                   7: 'FL_CB4', 8: 'FL_OC4',               }
pxy_dict = {  3: ( -30809.2, -4840.45 ) ,                
            4: (-24509.22, -4640.39),
            5: ( -18108.84, -4900.29 ),  
           7: ( (-5408.18, -4800.27) ),
            8: ( (992.01, -4800.24) ),     } 

#RE(measure_waxs_loop_sample_investigate_pz()) , the frist run is wrongly put the attenuators
# take the att out and run again,


 
 
# 12 th run 
# for the tubing samples

sample_dict = { 1: 'T1_nPTFE_Pd_Precursor_t0', 2: 'T2_nPTFE_Pd_Cube_Nwash', 3: 'T3_oPTFE_Pd_Precursor_t0', 
           4: 'T4_oPTFE_Pd_Cube_Nwash', 5: 'T5_oPTFE_Pd_Cube_Nwash_inDrop',
           6: 'T6_oPTFE_Pd_Cube_Awash', 7: 'T7_oPTFE_Pd_Cube_Sup1', 8:  'T8_oPTFE_Pd_Cube_Sup2',
           9: 'T9_oPTFE_Pd_Cube_Sup3', 10: 'T10_oPTFE_water', 11: 'T11_oPTFE_oil',  12: 'T12_oPTFE_ethanol',  }

pxy_dict = {   1: ( -36109.85, -2140),
            2: (-31110, -2140) ,    
            3: (-24109, -2140), 
            4: ( -15909.92, -2140),
            5: ( -8109.86, -2140),              
            6: (-1109.61  , -2140 + 100 ),
            7: ( 4390.76, -2140),  
            8: ( 10691.15, -2140),             
            9: (17491.22, -2140),              
            10: (24391.19, -2140 + 100),
            11: ( 31091.43, -2140),              
            12: (36591.37, -2140 )              
 } 
          
 #  measure_waxs_loop_sample( t = 5, att='None', move_y=False, user_name='YG', saxs_on = True, waxs_angles=np.linspace(0, 65, 11), inverse_angle = False   )          
#    measure_series_saxs(       )  #measure 1 sec
 

 
# 13 th run 
# for the cell samples


sample_dict = { 1: 'HB_Cell_1', 2: 'HB_Cell_2', 3: 'HB_Cell_3', }

pxy_dict = {   1: (29888.53, -4640.22),
            2:  (8988.29, -4240.08),    
            3:  (-12411.09, -5939.8),             
            }

# measure_waxs_loop_sample( t = 5, att='None', move_y=False, user_name='', saxs_on = True, waxs_angles=np.linspace(0, 65, 11), inverse_angle = False   )          
# measure_series_saxs(       )  
  
# 14 th run, resonant scattering

sample_dict = {}
sample_dict = {  1:  'YG_R1_Cap4_Au50_solution_30', 2: 'YG_R2_Cap3_Ag40_solution_30',
                 3: 'YG_R3_Cap6_Au50Ag40_20_10',    4:  'YG_R4_Cap7_Au50Ag40_15_15',
                 5:  'YG_R5_Cap8_Au50Ag40_10_20', }

pxy_dict = {    1:  ( -43404.15, -5100.2) , 2: (-37109.74, -4840.49),            
            3: (-30709.16, -4940.52),             
            4: (-24409.05, -4940.43),
            5: (-18008.63, -4800.29),             
            }
            
#    energy.move(14000) 
# lose the beam, then change DCM pitch from 1.0576 to 1.0696, change the BMP2 intensity back to X (4.42), Y (4.42)
# can open the feedback using ( RE( shopen())
#    energy.move(14000) #this time is good
#   energy.move(11918.7)
# go to the cam server, (both waxs and saxs), change the energy threshold by doing: setthreshold energy 11918 autog 5959
# put att 11-14, X6 
# 
#   measure_saxs_energy_eLarge_step( t = 1, att='None', move_y=False, user_name='', sample= None ) 
#   measure_saxs_energy_eSmall_step( t = 1, att='None', move_y=False, user_name='', sample= None ) 
  
  
  



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

       
#def _waxs_mode(   ):
#    RE( bps.mv(piezo.y, 7000)
#    epics.caput(   'XF:12IDC-ES:2{Det:1M-Ax:Y}Mtr.VAL', -61.45  ) 
#def _saxs_mode(   ):
#    RE( bps.mv(piezo.y, -5649.5 ) )
#    epics.caput( 'XF:12IDC-ES:2{Det:1M-Ax:Y}Mtr.VAL', -61.45  )
       
       
#for attentuator
#todolist: find out all the other attenuators       
def att_Sn60X1_in(    ): 
    RE(bps.mv(att1_5, 'Insert'))
def att_Sn60X1_out(    ): 
    RE(bps.mv(att1_5, 'Retract'))
  
       
def att_in(   att ): 
    att_dict = { 'Sn60X1': att1_5,  }  
       
    RE(bps.mv( att_dict[att], 'Insert'))
def att_out(  att  ): 
    att_dict = { 'Sn60X1': att1_5,  }     
    RE(bps.mv( att_dict[att], 'Retract'))       
       

##Resonant scattering around Au edge, energy around L-III 11.9187
#move energy precudure
# change energy from 16.1 kev to 14 kev first, then to 11.9187
# bps.mv(energy, 14000 )

    
    
    
def measure_saxs_energy_eLarge_step( t = 1, att='None', move_y=False, user_name='', sample= None ): 
    if sample is None:
        sample = RE.md['sample']
    dets = [ pil1M ]   
    #att_in( att ) 
    #energies = np.arange( 11918 - 100, 11918 + 300,  20  ) 
    energies = np.arange( 11918 - 100, 11918 + 300,  20  )    
    #energies = np.array( [ 11918 ]   ) 
    
    for e in energies:        
        try: 
            yield from bps.mv(energy, e)
        except:
            print('energy failed to move, sleep for 10 s')
            yield from bps.sleep(10)
            print('Slept for 10 s, try move energy again')
            yield from bps.mv(energy, e)
        yield from bps.sleep(1) 
        name_fmt = '{sample}_x{x_pos}_y{y_pos}_det{saxs_z}m_expt{expt}s_att{att}_E{e}_sid{scan_id:08d}'
        sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                  saxs_z=np.round(pil1m_pos.z.position,2), expt=t, att=att, e=e, scan_id=RE.md['scan_id'])
        if move_y:
            yield from bps.mvr(piezo.y, 30  )
        det_exposure_time( t, t)  
        sample_id(user_name=user_name, sample_name=sample_name ) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)
        #att_out( att )     
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)      




def measure_saxs_energy_eSmall_step( t = 1, att='None', move_y= False, user_name='', sample= None ): 
    if sample is None:
        sample = RE.md['sample']
    dets = [ pil1M ]   
 
    energies = np.arange( 11918 - 40, 11918 + 40,  5  )    
    #energies = np.array( [ 11918 ]   ) 
    
    for e in energies:        
        try: 
            yield from bps.mv(energy, e)
        except:
            print('energy failed to move, sleep for 10 s')
            yield from bps.sleep(10)
            print('Slept for 10 s, try move energy again')
            yield from bps.mv(energy, e)
        yield from bps.sleep(1) 
        name_fmt = '{sample}_x{x_pos}_y{y_pos}_det{saxs_z}m_expt{expt}s_att{att}_E{e}_sid{scan_id:08d}'
        sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                  saxs_z=np.round(pil1m_pos.z.position,2), expt=t, att=att, e=e, scan_id=RE.md['scan_id'])
        if move_y:
            yield from bps.mvr(piezo.y, 200  )
        det_exposure_time( t, t)  
        sample_id(user_name=user_name, sample_name=sample_name ) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)
        #att_out( att )     
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)      






##################################################
############TSAXS and TWAXS ###########################
#########################################################

def measure_waxs_loop_sample_investigate_pz( t = 1, att='None', move_y=False, user_name='',  
                              saxs_on = False,   waxs_angles =   np.linspace(0, 65, 11), inverse_angle = False,
                              pz_list =   [ -14600,  -6600, -2600,  -600, 400, 900, 1150,
                                            1400, 1650, 1900, 2400, 3400,  5400,  9400, 17400  ],
                              
                              ): 
    
    #waxs_angles = np.linspace(0, 65, 11)   #the max range
    #[ 0. ,  6.5, 13. , 19.5]
    ks = list( sample_dict.keys() )        
    waxs_angle_array = np.array( waxs_angles )
    dets = [  pil300KW ]  
    max_waxs_angle = np.max(  waxs_angle_array )  
    if inverse_angle:
        Twaxs_angle_array = waxs_angle_array[::-1]
    else:
        Twaxs_angle_array = waxs_angle_array            
    for waxs_angle in Twaxs_angles:
        yield from bps.mv(waxs, waxs_angle)  
        for pos in ks:
            #mov_sam( k )    
            px,py = pxy_dict[ pos ]
            print( px, py )
            yield from  bps.mv(piezo.x, px)  
            yield from  bps.mv(piezo.y, py) 
            for pz in pz_list:
                yield from  bps.mv(piezo.z, pz)
                sample = sample_dict[pos]  
                print('Move to pos=%s for sample:%s...'%(pos, sample ))
                RE.md['sample']  = sample             
                sample = RE.md['sample']
                if inverse_angle:
                    name_fmt = '{sample}_x{x_pos}_y{y_pos}_z{z_pos}_waxsN{waxs_angle:05.2f}_expt{expt}s_att{att}_sid{scan_id:08d}'
                else:
                    name_fmt = '{sample}_x{x_pos}_y{y_pos}_z{z_pos}_waxsP{waxs_angle:05.2f}_expt{expt}s_att{att}_sid{scan_id:08d}'             
                sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                      z_pos=np.round(piezo.z.position,2),
                                      waxs_angle=waxs_angle, expt= t, att=att, scan_id=RE.md['scan_id'])   
                print( sample_name )
                if saxs_on:
                    if waxs_angle == max_waxs_angle:
                        dets = [ pil1M, pil300KW ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]                
                    else:
                        dets=  [  pil300KW ] 
                if move_y:
                    yield from bps.mvr(piezo.y, 30  )
                det_exposure_time( t, t )  
                sample_id(user_name=user_name, sample_name=sample_name ) 
                print(f'\n\t=== Sample: {sample_name} ===\n')
                #yield from bp.scan(dets, waxs, *waxs_arc)
                yield from bp.count(dets, num=1)        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 
    
    
    
    
def measure_waxs_loop_sample( t = 1, att='None', move_y=False, user_name='',  
                              saxs_on = True,   waxs_angles =   np.linspace(0, 65, 11), inverse_angle = False   ): 
    
    #waxs_angles = np.linspace(0, 65, 11)   #the max range
    #[ 0. ,  6.5, 13. , 19.5]
    ks = list( sample_dict.keys() )        
    waxs_angle_array = np.array( waxs_angles )
    dets = [  pil300KW ]  
    max_waxs_angle = np.max(  waxs_angle_array )  
    if inverse_angle:
        Twaxs_angle_array = waxs_angle_array[::-1]
    else:
        Twaxs_angle_array = waxs_angle_array            
    for waxs_angle in Twaxs_angle_array:
        yield from bps.mv(waxs, waxs_angle)  
        for pos in ks:
            #mov_sam( k )    
            px,py = pxy_dict[ pos ]
            print( px, py )
            yield from  bps.mv(piezo.x, px)  
            yield from  bps.mv(piezo.y, py) 
            sample = sample_dict[pos]  
            print('Move to pos=%s for sample:%s...'%(pos, sample ))
            RE.md['sample']  = sample             
            sample = RE.md['sample']
            if inverse_angle:
                name_fmt = '{sample}_x{x_pos}_y{y_pos}_waxsN{waxs_angle:05.2f}_expt{expt}s_att{att}_sid{scan_id:08d}'
            else:
                name_fmt = '{sample}_x{x_pos}_y{y_pos}_waxsP{waxs_angle:05.2f}_expt{expt}s_att{att}_sid{scan_id:08d}'             
            sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                      waxs_angle=waxs_angle, expt= t, att=att, scan_id=RE.md['scan_id'])   
            print( sample_name )
            if saxs_on:
                if waxs_angle == max_waxs_angle:
                    dets = [ pil1M, pil300KW ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]                
                else:
                    dets=  [  pil300KW ] 
            if move_y:
                yield from bps.mvr(piezo.y, 30  )
            det_exposure_time( t, t )  
            sample_id(user_name=user_name, sample_name=sample_name ) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            #yield from bp.scan(dets, waxs, *waxs_arc)
            yield from bp.count(dets, num=1)        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 
    
    
    
    
    
def measure_series_waxs(   waxs_angles = np.linspace(0, 65, 11)     ):
    ks = list( sample_dict.keys() )
    inverse_angle  = False
    for k in ks:
        mov_sam( k )        
        RE( measure_waxs( t = 1, att= 'None',  move_y=False, user_name='xx',  waxs_angles =  waxs_angles, saxs_on=True,
                          inverse_angle = inverse_angle   ) )
        inverse_angle  =  not inverse_angle  
        
    
def measure_series_saxs(       ):
    ks = list( sample_dict.keys() ) 
    for k in ks:
        mov_sam( k )        
        RE( measure_saxs( t = 1, att= 'None',  move_y= True, user_name='YG' ) )
  

    
    
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
    yield from bp.count(dets, num=1)
    #att_out( att ) 
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)    
    
    
    
    
    
def measure_waxs( t = 1, att='None', move_y=False, user_name='', sample= None, 
                  saxs_on = True,   waxs_angles =   np.linspace(0, 65, 11), inverse_angle = False   ): 
    
    #waxs_angles = np.linspace(0, 65, 11)   #the max range
    #[ 0. ,  6.5, 13. , 19.5]
    waxs_angle_array = np.array( waxs_angles )
    if sample is None:
        sample = RE.md['sample']
    dets = [  pil300KW ]  
    max_waxs_angle = np.max(  waxs_angle_array )  
    if inverse_angle:
        Twaxs_angle_array = waxs_angle_array[::-1]
    else:
        Twaxs_angle_array = waxs_angle_array            
    for waxs_angle in Twaxs_angles:
        yield from bps.mv(waxs, waxs_angle)  
        if inverse_angle:
            name_fmt = '{sample}_x{x_pos}_y{y_pos}_waxsN{waxs_angle:05.2f}_expt{expt}s_att{att}_sid{scan_id:08d}'
        else:
            name_fmt = '{sample}_x{x_pos}_y{y_pos}_waxsP{waxs_angle:05.2f}_expt{expt}s_att{att}_sid{scan_id:08d}'            
        sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                      waxs_angle=waxs_angle, expt= t, att=att, scan_id=RE.md['scan_id'])        
        if saxs_on:
            if waxs_angle == max_waxs_angle:
                dets = [ pil1M, pil300KW ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]                
            else:
                dets=  [  pil300KW ] 
        if move_y:
            yield from bps.mvr(piezo.y, 30  )
        det_exposure_time( t, t )  
        sample_id(user_name=user_name, sample_name=sample_name ) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        #yield from bp.scan(dets, waxs, *waxs_arc)
        yield from bp.count(dets, num=1)
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 
    
    
    
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
       
    
    

##################################################
############GISAXS only ###########################
#########################################################
def run_gisaxs(t=.5, user_name = 'XXX'): 
    '''
    Macro to run gi-saxs    
    
    ''' 
    # define names of samples on sample bar    
    sample_list = [    'S1_P3PS_1p10_40mgml_Drop',       ]
    # define piezo-x-postion     
    x_list = [           -33000,             ]  
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'
    dets = [ 'pil1M'] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]  
    inc_angles = np.array([ 0.05,  0.08,  0.1,  0.12, 0.2, 0.3, ]) # incident angles
    for x, sample in zip(x_list,sample_list): #loop over samples on bar
        yield from bps.mv(piezo.x, x) #move to next sample                
        yield from alignement_gisaxs(0.1) #run alignment routine
        th_meas = inc_angles + piezo.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
        th_real = inc_angles    
        det_exposure_time(t,t)                 
        for i, th in enumerate(th_meas): #loop over incident angles
            yield from bps.mv(piezo.th, th)   
            x_meas = x + (1+i) * 200  #move the x-position               
            yield from bps.mv(piezo.x, x_meas) 
            name_fmt = '{sample}_inc{th:5.4f}deg_x{x}_expt{t}s_sid{scan_id:08d}'            
            sample_name = name_fmt.format(
                           sample = sample, th=th_real[i], x=x_meas, t=t, scan_id=RE.md['scan_id'])
            sample_id(user_name=user_name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n') 
            yield from bp.count(dets, num=1)     
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
    
    


##################################################
############GIWAXS-SAXS ###########################
#########################################################
def run_gixs(t=.5, user_name = 'XXX'): 
    '''
    Macro to run gi-waxs/saxs
    
    
    ''' 
    # define names of samples on sample bar    
    sample_list = [    'S1_P3PS_1p10_40mgml_Drop',       ]
    # define piezo-x-postion     
    x_list = [           -33000,             ]  
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'
    inc_angles = np.array([ 0.05,  0.08,  0.1,  0.12, 0.2, 0.3, ]) # incident angles
    #waxs_angle_array = np.linspace(0, 84, 15)
    waxs_angle_array = np.linspace(0, 19.5, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
                                               # if 12, 3: up to q=2.199
                                               # if 18, 4: up to q=3.04
                                               # if 24, 5: up to q=3.87
                                               # if 30, 6: up to q=4.70
                                               # 52/6.5 +1 =8
    max_waxs_angle = np.max(  waxs_angle_array )  
    inverse_angle = False
    for x, sample in zip(x_list,sample_list): #loop over samples on bar
        yield from bps.mv(piezo.x, x) #move to next sample                
        yield from alignement_gisaxs(0.1) #run alignment routine
        th_meas = inc_angles + piezo.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
        th_real = inc_angles    
        det_exposure_time(t,t) 
        if inverse_angle:
            Twaxs_angle_array = waxs_angle_array[::-1]
        else:
            Twaxs_angle_array = waxs_angle_array
        for waxs_angle in Twaxs_angle_array: # loop through waxs angles
            yield from bps.mv(waxs, waxs_angle)     
            if waxs_angle == max_waxs_angle:
                dets = ['pil300KW', 'pil1M'] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]  
                print( 'Meausre both saxs and waxs here for w-angle=%s'%waxs_angle )
            else:
                dets = ['pil300KW' ]             
            for i, th in enumerate(th_meas): #loop over incident angles
                yield from bps.mv(piezo.th, th)   
                x_meas = x + (1+i) * 200  #move the x-position               
                yield from bps.mv(piezo.x, x_meas) 
                if inverse_angle:
                    name_fmt = '{sample}_{th:5.4f}deg_waxsN{waxs_angle:05.2f}_x{x}_expt{t}s_sid{scan_id:08d}'
                else:
                    name_fmt = '{sample}_{th:5.4f}deg_waxsP{waxs_angle:05.2f}_x{x}_expt{t}s_sid{scan_id:08d}'                    
                sample_name = name_fmt.format(
                               sample = sample, th=th_real[i], waxs_angle=waxs_angle, x=x_meas, t=t, scan_id=RE.md['scan_id'])
                sample_id(user_name=user_name, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n') 
                yield from bp.count(dets, num=1) 
        inverse_angle = not inverse_angle       
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class Object(object):
    pass
     
    
def measure_saxs_simulate( t = .1, att='None', move_y=False, user_name='XXX', sample='S1' ):   
    if sample is None:
        sample = RE.md['sample']
    dets = [ 'pil1M' ]
    piezo = Object()
    piezo.x=Object()
    piezo.y=Object()
    piezo.x.position = 1000
    piezo.y.position = 2000
    pil1m_pos = Object()
    pil1m_pos.z= Object()
    pil1m_pos.z.position = 5000    
    RE = Object()
    RE.md = {}
    RE.md['scan_id'] =1223    
    name_fmt = '{sample}_x{x_pos}_y{y_pos}_det{saxs_z}m_expt{expt}s_att{att}_sid{scan_id:08d}'
    sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                  saxs_z=np.round(pil1m_pos.z.position,2), expt=t, att=att, scan_id=RE.md['scan_id'])
    #if move_y:
    #    yield from bps.mvr(piezo.y, 30  )
    #det_exposure_time( t, t)  
    #sample_id(user_name=user_name, sample_name=sample_name ) 
    print(f'\n\t=== Sample: {sample_name} ===\n')
    #yield from bp.count(dets, num=1)
    
    
    
    
    
def run_gixs_simulate(t=.5, user_name = 'XXX'): 
    '''
    Macro to run gi-waxs/saxs
    
    
    ''' 
    # define names of samples on sample bar    
    sample_list = [    'Sample1',   'Sample2',  'Sample3',  ]
    # define piezo-x-postion    
    x_list = [           -30000,  -24000, -10000,           ]  
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'
    #inc_angles = np.array([ 0.05,  0.08,  0.1,  0.12, 0.2, 0.3, ]) # incident angles
    inc_angles = np.array([ 0.05,   0.1,  0.15,  ]) # incident angles    
    #waxs_angle_array = np.linspace(0, 84, 15)
    waxs_angle_array = np.linspace(0, 19.5, 4)   # q=4*3.14/0.77*np.sin((max angle+3.5)/2*3.14159/180)
                                               # if 12, 3: up to q=2.199
                                               # if 18, 4: up to q=3.04
                                               # if 24, 5: up to q=3.87
                                               # if 30, 6: up to q=4.70
                                               # 52/6.5 +1 =8
    max_waxs_angle = np.max(  waxs_angle_array )  
    inverse_angle = False
    for x, sample in zip(x_list,sample_list): #loop over samples on bar
        #yield from bps.mv(piezo.x, x) #move to next sample                
        #yield from alignement_gisaxs(0.1) #run alignment routine
        th_meas = inc_angles #+ piezo.th.position #np.array([0.10 + piezo.th.position, 0.20 + piezo.th.position])
        th_real = inc_angles    
        #det_exposure_time(t,t) 
        if inverse_angle:
            Twaxs_angle_array = waxs_angle_array[::-1]
        else:
            Twaxs_angle_array = waxs_angle_array
        for waxs_angle in Twaxs_angle_array: # loop through waxs angles
            #yield from bps.mv(waxs, waxs_angle)   
            if waxs_angle == max_waxs_angle:
                dets = ['pil300KW', 'pil1M'] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]  
                print( 'Meausre both saxs and waxs here for w-angle=%s'%waxs_angle )
            else:
                dets = ['pil300KW' ]              
            for i, th in enumerate(th_meas): #loop over incident angles
                #yield from bps.mv(piezo.th, th)   
                x_meas = x + (1+i) * 200  #move the x-position               
                #yield from bps.mv(piezo.x, x_meas) 
                if inverse_angle:
                    name_fmt = '{sample}_{th:5.4f}deg_waxsN{waxs_angle:05.2f}_x{x}_expt{t}s_sid{scan_id:08d}'
                else:
                    name_fmt = '{sample}_{th:5.4f}deg_waxsP{waxs_angle:05.2f}_x{x}_expt{t}s_sid{scan_id:08d}'                  
                sample_name = name_fmt.format(
                               sample = sample, th=th_real[i], waxs_angle=waxs_angle, x=x_meas, t=t, scan_id=123)
                #sample_id(user_name=user_name, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n') 
                #yield from bp.count(dets, num=1) 
        inverse_angle = not inverse_angle       
    #sample_id(user_name='test', sample_name='test')
    #det_exposure_time(0.5)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
