##Collect data:

#SMI: 2021/1/31
# SAF: 306158   Standard        Beamline 12-ID   proposal:  304231


# create proposal:  proposal_id( '2021-1', '308052_Dinca' )    #create the proposal id and folder


#  RE( shopen() )  # to open the beam and feedback
#  RE( shclose()) 

#  %run -i    

# The beam center on SAXS:  [459, 567 ]
# Energy: 16.1 keV, 0.77009 A
# SAXS distance 5000



sample_dict = {   1: 'Jason_Conc_1', 2: 'Jason_Conc_10',
               3: 'Jason_Conc_40', 4: 'Jason_Conc_60', 
               5:    'Dinca_Zn_PDI', 6: 'Dinca_Mn_PDI', 7: 'Dinca_PDI_Ligand',
               8: 'Dinca_RW_1315', 9:  'Dinca_Zn_PDI_2',
               10: 'Dinca_Mn_PDI_32', 11: 'Dinca_NiBHT', 
              12:  'Dinca_NiBHT_Neg', 13:  'Dinca_NiBHT_Pos',
              14:   'Dinca_TIBQ_COF_DMA', 15:     'Dinca_TIBA_COF_CTAB',      
      
         }
           


pxy_dict = {    1:  (-43499.91,  -5019.78) , 2:  (-37199.98,  -5019.78),  3:(-31099.93,  -5019.78), 4: (-24599.85,  -5019.78),
5: (-17999.94, -5019.78), 6:   (-11600.02, -5019.9), 7: (-5400, -5019.9), 8: (  1100 , -5019.9),  9: (  7600 , -5019.9),  10: ( 13900  , -5019.9), 
 11: (  20200 , -5019.9),  12: (  26500 , -5019.9),  13: (  32800 , -5019.9),  14: (  39200 , -5019.9), 15: ( 45400   , -5019.9),  
   }







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
    yield from bp.count(dets, num=1)
    #att_out( att ) 
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)    
    
    

def measure_series_saxs(       ):
    ks = list( sample_dict.keys() ) [4:]
    for k in ks:
        mov_sam( k )        
        RE( measure_saxs( t = .1, att= 'None',  move_y= True, user_name='' ) )
    


def measure_waxs_loop_sample( t = 1, att='None', move_y=False, user_name='',  
                              saxs_on = False,   waxs_angles =   np.linspace(0, 65, 11), inverse_angle = False   ): 
    
    #waxs_angles = np.linspace(0, 65, 11)   #the max range
    #[ 0. ,  6.5, 13. , 19.5]
    ks = list( sample_dict.keys() )  [4:]      
    waxs_angle_array = np.array( waxs_angles )
    dets = [  pil300KW ]  
    max_waxs_angle = np.max(  waxs_angle_array )  

    for waxs_angle in waxs_angle_array:
        yield from bps.mv(waxs, waxs_angle)  
        for pos in ks:
            #mov_sam( k )    
            px,py = pxy_dict[ pos ]

            py += 200



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
    

