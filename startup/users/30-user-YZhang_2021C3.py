##Collect data:

#SMI: 2021/10/30
# SAF: 308072  Standard        Beamline 12-ID   proposal:  309075


# create proposal:  proposal_id('2021_3', '30000_YZhang_Nov')    #create the proposal id and folder

# Energy: 16.1 keV, 0.77009 A
# SAXS distance 1800
# SAXS in  and WAXS in air

# WAXS range [ -4, 56 ]




#  RE( shopen() )  # to open the beam and feedback
#  RE( shclose()) 

#  %run -i    
#  WAXS, 900KW, 0 degree, beam center [ 220, 308 ]





# The beam center on SAXS:  
##for the run >=5 
# 5 m, beam stop:  1.9  
# 5m, 1M, x=-5, Y = -40
# the correspond beam center is [ 454, 682  ]
# beamstop_save()
 


username = 'YZ'



##Run1, PbS in SiO2 Oil  ( Drop 10 ul to Silicon oil in cap with different Dia. 3, 2, 1.5 )
ypos = 0
sample_dict = {   1: 'PbS_SilOil_Cap3mm' ,  2: 'PbS_SilOil_Cap2mm' , 3: 'PbS_SilOil_Cap1p5mm'    }
pxy_dict = {    1:  (-4000, 600  ) ,2:  (13000, 400  ),3:   (31000, 500  )  }

# Run2,
sample_dict = {   1: 'DropRec_20201031_Au1' ,  2: 'DropRec_20201031_Au2' , 3: 'FL_Cu_20211031_C2',    4: 'FL_Cu_20211031_C3', 
 5: 'FL_Cu_20211031_C4',   6: 'FL_Cu_20211031_C5',   7: 'FL_Cu_20211031_C8',   8: 'PbS_SilOil_Cap1p1mm'  }


 # Run3, #All in 1.5 mm Dia glass capillary
sample_dict = {   1: 'Au5_Stock_GCap1p5mm' ,  2: 'Au10_Stock_GCap1p5mm' , 3: 'Au15_Stock_GCap1p5mm',    4: 'Au20_Stock_GCap1p5mm', 
 5: 'Au30_Stock_GCap1p5mm',   6: 'Au50_Stock_GCap1p5mm',   7: 'Wat_GCap1p5mm',   8: 'Emp_GCap1p5mm',  9: 'Emp_Cap1p5mm', 
 10: 'Empty', 11: 'PbS_SilOil_Cap1p1p5mm', 12: 'FeO_SilOil_Cap1p1p5mm', 11: 'Au_SilOil_Cap1p1p5mm'  }
  


ypos = 0
pxy_dict = {   
    
     1:  ( 3200, 700  ) ,

2:  (44800, ypos  ),
3:   (38900, ypos  ), 
4: ( 31800, ypos  ), 
5: ( 25900, ypos   ), 
 6: ( 20700,ypos ), 
7: (   14700, ypos  )  ,
8: (   8600, ypos  )  ,
9: (  2100, ypos  )  ,
}





 # Run4, #All in 1.5 mm Dia glass capillary

sample_dict = {   1: 'PbS_SilOil_Cap1p1mm' , #should 1.5 mm, 
2: 'PbS_SilOil_Cap1p1mmB',


 11: 'PbS_SilOil_Cap1p1p5mm', 12: 'FeO_SilOil_Cap1p1p5mm', 13: 'Au_SilOil_Cap1p1p5mm'  }
  


ypos = 0
pxy_dict = {   
    
    1:  ( 3200, 700  ) ,


3:   (38900, ypos  ), 
4: ( 31800, ypos  ), 
5: ( 25900, ypos   ), 
 6: ( 20700,ypos ), 
7: (   14700, ypos  )  ,
8: (   8600, ypos  )  ,
9: (  2100, ypos  )  ,
}




x_list = np.array(list( ( pxy_dict.values()) ) )[:,0]
y_list = np.array(list( ( pxy_dict.values()) ) )[:,1]
sample_list =  np.array(list( ( sample_dict.values()) ) )
##################################################
############ Some convinent functions#################
#########################################################




#           RE( measure_waxs(  t = 1, waxs_angle= 0, att='None',  dy= 0) )  
#           RE( measure_wsaxs(  t = 1, waxs_angle= 20, att='None',  dy=0 ) )  


def measure_one_pos():
    #t= [  1, 10, 30, 60 ] 
    t = [ 1 ]
    dys = [ 0  ]
    for dy in dys: 
        for ti in t:
            RE( measure_wsaxs(  t = ti, waxs_angle= 20, att='None',  dy=dy ) )  
    for dy in dys: 
        for ti in t:               
            RE( measure_waxs(  t = ti, waxs_angle= 0, att='None',  dy=dy ) )  

 

def measure_all():
    measure_series_wsaxs(  t= [  1, 10, 30, 60 ] , waxs_angle=20,  dys = [100,  ]   )
    measure_series_waxs(  t= [  1, 10, 30, 60 ] , waxs_angle=0,  dys = [100,  ]   )



def measure_one():
    measure_series_wsaxs(  t= [  1, 10, 30, 60 ] , waxs_angle=20,  dys = [100,  ]   )
    measure_series_waxs(  t= [  1, 10, 30, 60 ] , waxs_angle=0,  dys = [100,  ]   )




def measure_series_waxs(  t= [  1, 10 ] , waxs_angle=0,  dys = [0,  ]   ):
    ks = list( sample_dict.keys() )  
    for k in ks:
        mov_sam( k )                   
        for dy in dys: 
            for ti in t:
                RE( measure_waxs(  t = ti, waxs_angle= waxs_angle, att='None',  dy=dy ) )


def measure_series_wsaxs(  t= [  1, 10 ] , waxs_angle=20,  dys = [0,  ]   ):
    ks = list( sample_dict.keys() )  
    for k in ks:
        mov_sam( k )                   
        for dy in dys: 
            for ti in t:
                RE( measure_wsaxs(  t = ti, waxs_angle= waxs_angle, att='None',  dy=dy ) )




def measure_series_saxs(  t= [  1, 10  ] ,  dys = [  0   ]   ):
    ks = list( sample_dict.keys() )      
    for k in ks:
        mov_sam( k )                   
        for dy in dys: 
            for ti in t:
                RE( measure_saxs(  t = ti, att='None',  dy=dy ) )


def measure_saxs_scany( N ,t=1, user_name=username, sample= None, att='None', ): 
    if sample is None:
        sample = RE.md['sample']
    dets = [ pil1M , pil900KW]   
    for i in range(N):                 
        name_fmt = '{sample}_x{x_pos}_y{y_pos}_det{saxs_z}m_expt{expt}s_att{att}_sid{scan_id:08d}'
        sample_name = name_fmt.format(sample=sample, x_pos=np.round(piezo.x.position,2), y_pos=np.round(piezo.y.position,2),
                                saxs_z=np.round(pil1m_pos.z.position,2), expt=t, att=att, scan_id=RE.md['scan_id']) 
        det_exposure_time( t, t)  
        sample_id(user_name=user_name, sample_name=sample_name ) 
        yield from bp.count(dets, num=1)
        #yield from   bps.mv(piezo.y, 30)  #here is something wrong, should move a relative postion, have to redo this y scan!!!! NOTE at Thursady afternoon (9/23)
        yield from   bps.mvr(piezo.y, 1000)  #here is something wrong, should move a relative postion, have to redo this y scan!!!! NOTE at Thursady afternoon (9/23)



def measure_saxs( t = 1, att='None', dx=0, dy=0, user_name=username,  sample= None ): 
    if sample is None:
        sample = RE.md['sample']
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
    if sample is None:
        sample = RE.md['sample']
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

def measure_wsaxs( t = 1, waxs_angle=20, att='None', dx=0, dy=0, user_name=username, sample= None ): 
    if sample is None:
        sample = RE.md['sample']
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


 




