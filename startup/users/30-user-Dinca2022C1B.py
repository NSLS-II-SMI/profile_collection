##Collect data:

#SMI: 2022/3/7
# SAF:    Standard   
# proposal_id('2022_1', '308214_Dinca')


 
# Energy: 16.1 keV, 0.77009 A
# SAXS distance 
# SAXS in  and WAXS in 

# WAXS range [ 0, 5, 15, 25, 45 ]

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
# 5 meter in vacuum, [462, 559 ]
# Using pindiol, X, -198.5, Y 8.7 
# beamstop_save()
 


user_name = 'Dinca'
username = 'Dinca'


##Run1,  
#x,y,z=0,4,0; pizeo,    z=8900 
sample_dict = {   1:  'TC_NiT2HQ', 2: 'TC_NiTIBPRT', 3: 'TC_NiTIBPE' , 4: 'TC_ZnOHToC', 5: 'TC_ASMOF',
6: 'TC_TABQSA', 7: 'Zn2', 8: 'Ni1', 9: 'Zn1', 10: 'Ni2', 11: 'Cu' }

ypos = 200
pxy_dict = {       
1:  ( -38700, -3000  ) ,
2:  ( -31900,  -3000  ),
3:   ( -19350, -750  ), 
4: (  -12650, -2500  ), 
5: (  -5950, -950 ),
6: ( 250, -5000 ),
7: ( 6250, -5000  ), 
8: ( 12250, -5000  ), 
9: ( 18850, -2000  ), 
10: (  31550, -1150  ), 
11: ( 37150, -7700 )


}

#  measure_XS(   dx=0, dy=0 ,  t=1   )







 

x_list = np.array(list( ( pxy_dict.values()) ) )[:,0]
y_list = np.array(list( ( pxy_dict.values()) ) )[:,1]
sample_list =  np.array(list( ( sample_dict.values()) ) )
##################################################
############ Some convinent functions#################
#########################################################




def measure_XS(   dx=0, dy=0 ,  t=1   ):
    '''suppose the waxs is off the beam'''
    ks = list( sample_dict.keys() )  # [:1]
    measure_WAXS(  ks=ks,  dx=dx, dy=dy ,  t=t   )    
    dy=100
    measure_SAXS(  ks=ks,  dx=dx, dy=dy ,  t=t   )





def measure_WAXS(   ks, dx=0, dy=0 ,  t=1   ):
    WA = np.array( [ 0, 5, 15, 25, 45 ])   # [:1]
    for wa in WA:
        move_waxs( wa  )
        _measure_one(   ks=ks, dets=[pil900KW], waxs_angle = wa, dx=dx, dy=dy ,  t=t   )


def measure_SAXS(   ks, wa=45,  dx=0, dy=0 ,  t= 1   ):
    move_waxs( wa  )
    _measure_one(   ks=ks, dets=[pil1M],waxs_angle = wa,  dx=dx, dy=dy ,  t=t   )
    RE( bps.mvr(  SAXS.y, 30 * 0.172  ) ) 
    _measure_one(    ks=ks, dets=[pil1M],waxs_angle = wa,  dx=dx, dy=dy ,  t=t   )
    RE( bps.mvr(  SAXS.y, -30 * 0.172  ) ) 


def _measure_one(  ks, dets, waxs_angle, dx=0, dy=0 ,  t =  1    ):
    for k in ks:
        mov_sam( k )                
        sample = RE.md['sample']       
        u = sample.split('_')[0]
        if u in [ 'Gao', 'Xu', 'YM']:
            User_name = u
            sample = '_'.join( sample.split('_')[1:] )
        else: 
            User_name = user_name  
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



def name_sam( pos ):    
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s'%(pos, sample ))
    RE.md['sample']  = sample      


def check_sample_loc( sleep = 5 ):
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
def mov_sam( pos ):    
    px,py = pxy_dict[ pos ]
    RE(  bps.mv(piezo.x, px) )
    RE(  bps.mv(piezo.y, py) )
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s'%(pos, sample ))
    RE.md['sample']  = sample   
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


 




