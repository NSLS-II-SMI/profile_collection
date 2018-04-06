

def export_scan( sid, filename='', path='/home/xf12id/tmp/',verbose=True ):
    '''Export table by giving a scan id'''
    hdr = db[sid]
    d = hdr.table()
    output = path + 'sid=%s_%s.csv'%(sid,filename)
    d.to_csv( output )
    if verbose:
        print( 'The table of sid=%s is saved as %s.'%(sid, output) )

def find_peaks( x, y, thres= 0.5e7 ):
    x= np.array(x)
    xi = np.arange( len(y) )
    w = np.array( np.where(y>thres)[0] )
    w1 = np.diff(w)>1
    #print( len(w), len(w1) )
    pos = (w[1:].ravel())[w1]
    ind = []
    ind.append( w[0] )
    for p in pos:
        #print(p)
        ind.append( xi[p-1] )
    ind.append( w[-1] )   
    xmax = []   
    for i in range( len(ind ) -1 ):
        index_x =  np.argmax( y[ ind[i]: ind[i+1]] )
        xmax.append( round(x[ index_x ],2)   )   
      
    print(ind) 
    return( xmax )

def mvrx( rx ):   
     posx = stage.x.position
     stage.x.move( posx + rx )
def mvry( ry ):         
     posy =  stage.y.position 
     stage.y.move( posy + ry )
     
def mov(motor, pos):
    motor.move(pos)
def mvr(motor,val):
    cur = motor.position
    mov( motor, cur + val )  
    
     
def create_string( d  ): 
    d = round(d,2)
    s = str( '%0.8f'%d )[:5]
    return s
    
    
def collect_data( exposure_time=1, meta_string=['X','Y','Inc','Arc', 'Exp'], dets= [  pil300KW   ]  ): 
        '''
        dets: [pil1M], collect SAXS data
              [rayonix ] collect MAXS data
              [pil300KW] collect WAXS data
              
              the combination  will collect detectors data  simultineously 
              e..g, [ pil1M, pil300KW] simultineously collect SAXS and WAXS             
              
        '''   
        posy = stage.y.position
        posx =  stage.x.position
        inc = stage.th.position
        arc =   waxs.arc.position
        md = 'sample: %s, x=%.2f, y=%0.2f, inc=%0.2f, arc=%.2f, exp=%s s.'%(
                 RE.md['sample_name'],posx, posy, inc, arc,  exposure_time )
                 
        posx_ =  create_string(posx)
        posy_ =  create_string(posy) 
        exposure_time_ =  create_string(exposure_time)         
        inc_ = create_string(inc)
        arc_ =   create_string(arc)
        filename= '%s_%s'%( RE.md['user_name'], RE.md['sample_name'] )
        if 'X' in meta_string:
            filename +='_X%s'%posx_
        if 'Y' in meta_string:
            filename +='_Y%s'%posy_
        if 'Inc' in meta_string:
            filename += '_Inc%s'%inc_
        if 'Arc' in meta_string:
            filename += '_arc%s'%arc_            
        if 'Exp' in meta_string:
            filename +='_Exp%s'%exposure_time_

        for detector in dets:                                
                detector.cam.file_name.put(filename) 
                detector.cam.acquire_time.put(exposure_time)
                detector.cam.acquire_period.put(exposure_time)                 
                RE( count( [detector] ),  Measurement = '%s'%md)  
                
                
## For a series of sample, only run transmission SAXS 
def run_saxs_sample( sample_list, posx_list, user_name,   exposure_time = 2,
	ystep = 0.05, ynum=5, dets= [pil1M, pil300KW],   ):
 	
    ''' 
     For a series of samples, only run transmission SAXS  using SAXS det
         For each sample, collect ynum points along y direction with ystep
    
	theta corresponds to 0.1, this would be only parameter to be changed for each sample
        xstep: x step in mm
 	waxs_arc: the waxs arc angle for WAXS data collection
        
    '''
    cur_y = stage.y.position
    for i, sam in enumerate(sample_list):
        posx = posx_list[i]         
        sample_id(  user_name = user_name, sample_name= sample_list[i] )
        print('Start measurement for position x as: %s....'%posx)
        stage.x.move( posx )
        for yi in range(ynum):
            posy = cur_y + yi * ystep
            stage.y.move( posy  )            
            collect_data( exposure_time= exposure_time, dets = dets  )
        stage.y.move( cur_y )
   
   

#For one smaple, run gi_saxs with different incident angle and different waxs_arc using SAXS and WAXS det        
def run_gi_sample(user_name='X90', sample='2472-2480eV', theta= -0.344, exposure_time = 0.5,
	xstep = 0.500,  off_v_01 = [0, -0.12],
 	waxs_arc = [12.0], dets=[pil1M, pil300KW],   ):
 	
    ''' 
        For one smaple, run gi_saxs with different incident angle and different waxs_arc using SAXS and WAXS det
    
	theta corresponds to 0.1, this would be only parameter to be changed for each sample
        xstep: x step in mm
 	waxs_arc: the waxs arc angle for WAXS data collection        
    '''
    sample_id(  user_name = user_name, sample_name= sample )
    for detector in dets:
        detector.cam.acquire_time.put(exposure_time)
        detector.cam.acquire_period.put(exposure_time)
    for ang in off_v_01:
        act_ang = theta + ang 
        print('Start measurement for incident angle as: %s....'%ang)
        stage.th.move( act_ang )
        

    cur_xh = stage.x.position
    stage.x.move( cur_xh + xstep )
    for arc in waxs_arc:
        waxs.arc.move( arc )
        md = 'inc_ang=%s, waxs_arc=%s, xh=%.3f, exp=%s s.'%(ang, arc, cur_xh + xstep, exposure_time )
        collect_data( exposure_time= exposure_time, dets = dets  )            
        #RE( count( dets ),  Measurement = '%s'%md)
            

def run_gi_energy (angle, t=1, name='test'):
    posx = stage.x.position
    stage.th.move(angle)
    det_exposure_time(t)
    sample='0.1deg_waxs'
    sample_id( user_name = name, sample_name= sample)
    RE(escan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], waxs.arc, 5, 43, 7))
    stage.th.move(angle-0.1)
    posx = stage.x.position
#    stage.x.move(posx-0.4)
    sample='0.2deg_waxs'
    sample_id( user_name = name, sample_name= sample)
    RE(escan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], waxs.arc, 5, 43, 7))
    stage.th.move(angle-0.2)
    posx = stage.x.position
#    stage.x.move(posx-0.4)
    sample='0.4deg_waxs'
    sample_id( user_name = name, sample_name= sample)
    RE(escan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], waxs.arc, 5, 43, 7))
    sample_id( user_name = 'test', sample_name= 'test')
   

def run_saxs_lipids(y=1, t=2):
    # Parameters:
    x_list  = [20.20, 17.17, 13.87, 10.01, 6.07, 2.68, -0.84, -5.61, -11.08]
    samples = [
                'DOPC226a_A_full',
                'DOPC226a_A_half',
                'DOPC226a_B_full',
                'DOPC226a_B_half',
                'POPC622a_A_full',
                'POPC622a_A_half',
                'POPC622a_B_full',
                'POPC622a_B_half',
                'water',
              ]
    param   = '8.3m'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'

    # Detectors, motors:
    dets = [pil1M, pil300KW, ssacurrent]
    waxs_arc = [11, 11.1, 1]
    stage_y = [y, y+1, 21]

    for x, sample in zip(x_list, samples):
        yield from bps.mv(stage.x, x)
        yield from bps.mv(stage.y, y)
        det_exposure_time(t)
        sample_id(user_name=sample,
                  sample_name=param)
        # print(RE.md)
        yield from e_grid_scan(dets, waxs.arc, *waxs_arc, stage.y, *stage_y, 0)

    sample_id(user_name='test', sample_name='test')

    """
    stage.x.move(8.55)
    stage.y.move(y)
    det_exposure_time(t)
    sample='B_full'
    sample_id( user_name = name, sample_name= sample)
    RE(e_grid_scan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1, stage.y, y, y+1, 21, 0))
    stage.x.move(3.77)
    stage.y.move(y)
    det_exposure_time(t)
    sample='B_half'
    sample_id( user_name = name, sample_name= sample)
    RE(e_grid_scan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1, stage.y, y, y+1, 21, 0))
    ''' 
    stage.x.move(5.54)
    stage.y.move(y)
    det_exposure_time(t)
    sample='B_third'
    sample_id( user_name = name, sample_name= sample)
    RE(e_grid_scan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1, stage.y, y, y+1, 21, 0))
#    
    stage.x.move(1.44)
    stage.y.move(y)
    det_exposure_time(t)
    sample='C_full'
    sample_id( user_name = name, sample_name= sample)
    RE(e_grid_scan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1, stage.y, y, y+1, 21, 0))
    stage.x.move(-2)
    stage.y.move(y)
    det_exposure_time(t)
    sample='C_half'
    sample_id( user_name = name, sample_name= sample)
    RE(e_grid_scan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1, stage.y, y, y+1, 21, 0))
    stage.x.move(-6.7)
    stage.y.move(y)
    det_exposure_time(t)
    sample='C_third'
    sample_id( user_name = name, sample_name= sample)
    RE(e_grid_scan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1, stage.y, y, y+1, 21, 0))
    '''
#
#    stage.x.move(-16.27)
#    stage.y.move(y)
#    det_exposure_time(t)
#    sample='water'
#    sample_id( user_name = name, sample_name= sample)
#    RE(escan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1))
#    stage.y.move(y-0.05)
#    RE(escan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1))
#    stage.y.move(y-0.1)
#    RE(escan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1))
#    stage.y.move(y-0.15)
#    RE(escan([pil300KW, pil1M, ssacurrent], waxs.arc, 11, 11, 1))
#
    """


def run_giwaxs_res (angle, name='test'):
    stage.th.move(angle-0.24)
    energy.move(2472)
    posx = stage.x.position
    sample='2472eV'
    sample_id( user_name = name, sample_name= sample)
    RE(e_inner_scan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], 1, energy, 2472, 2472, hfm.th, -0.17390, -0.17390, vdm.th, -0.35710, -0.35710))
    energy.move(2450)
    sample='2450eV'
    sample_id( user_name = name, sample_name= sample)
    RE(e_inner_scan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], 1, energy, 2450, 2450, hfm.th, -0.17375, -0.17375, vdm.th, -0.35725, -0.35725))
    energy.move(2400)
    sample='2400eV'
    sample_id( user_name = name, sample_name= sample)
    RE(e_inner_scan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], 1, energy, 2400, 2400, hfm.th, -0.17355, -0.17355, vdm.th, -0.3576, -0.3576))
    stage.x.move(posx+0.5)
    sample='2400eV_offset05'
    sample_id( user_name = name, sample_name= sample)
    RE(e_inner_scan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], 1, energy, 2400, 2400, hfm.th, -0.17355, -0.17355, vdm.th, -0.3576, -0.3576))
    energy.move(2450)
    sample='2450eV_offset05'
    sample_id( user_name = name, sample_name= sample)
    RE(e_inner_scan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], 1, energy, 2450, 2450, hfm.th, -0.17375, -0.17375, vdm.th, -0.35725, -0.35725))
    sample='2472eV_offset05'
    sample_id( user_name = name, sample_name= sample)
    energy.move(2472)
    RE(e_inner_scan([pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent], 1, energy, 2472, 2472, hfm.th, -0.17390, -0.17390, vdm.th, -0.35710, -0.35710))
    sample_id( user_name = 'test', sample_name= 'test')




 
### For one smaple, collect all detector data for different incident angle and different waxs_arc
def run(  inc_list = [  -0.07,   -0.11, -0.22 ],  arc_list=[4, 10, 16], exposure_time=0.5,  step=-0.03, axis='x'  ):

    '''For one smaple, collect all detector data for different incident angle and different waxs_arc
       Only collect  SAXS/MAXS for the second arc in arc_list. By default for waxs_arc =10
       Collect WAXS for all points
       
    '''

    arc_listc = np.array(arc_list).copy()
    for i, inc in enumerate(inc_list):
        mov( stage.th, inc ) 
        print('*'*50)
        print('The incident angle is: %s.'%inc)
        if i%2:
            arc_list = arc_listc[::-1]
        else:
            arc_list = arc_listc    
        print(arc_list)
        for j, arc in enumerate(arc_list):
            mov(waxs.arc, arc) 
            if j==1:
                collect_data( exposure_time, det =[ pil300KW, pil1M, rayonix ]   )                
                print('Collect SAXS, MAXS and WAXS here with inc=%s,arc=%s'%(inc,arc))
            else:
                collect_data( exposure_time,det =[ pil300KW ] )
                print('Collect WAXS here with   inc=%s,arc=%s'%(inc,arc))             
        print('#'*50)  
        if axis=='x':
            mvr( stage.x, step )
        elif aixs=='y':
            mvr( stage.y, step )
        else:
            print('Error!!!, Please give axis either x or y.' )                    
                    
 
 
    
#  %run -i /home/xf12id/.ipython/profile_collection/startup/30-user.py 

#try:
#    hdr = db[  -1 ]
#    d = hdr.table()
#    x= d['stage_x']
#    y= d['pil300KW_stats1_total']
#except:
#    x=[0]
#    y=[0]
       
#user_name = 'LC'
#sample_list=['O22-E-0Cto25C','O27-5-0Cto25C','O22-I-quenchto0C-5Cmin','O27-9-quenchto0C-1Cmin','027-8-quenchto0C-fast','O22-G-quenchto0C-15Cmin','O22-L-quenchto0C-30Cmin']
#posx_list = [8.68, 11.22,13.75, 16.41, 19.3, 21.85,24]
#sample_list=['test3']
#posx_list = [7]
# 2018 Cycle 1
#Xrange [-15, 25]  --> center = 5.0
#Y range [-2.3, 4.3 ] --> center = 1.0
# RE(bp.scan([pil300KW], stage.x, -15,25, 301))  #WAXS det, for capillary sample
# RE(bp.scan([pil1M], stage.x, -15,25, 301))  #SAXS det, for Kapton sample
       
    
def move_pos(  pos=1  ):
    sam = sample_list[pos-1]
    posx = posx_list[pos-1]    
    print('Move to sample: %s (sample holder position: %s) with posx at: %s.'%(sam,pos,posx) )
    stage.x.move( posx )
    sample_id(  user_name = user_name, sample_name= sam )    
  
            
            
#Aligam GiSAXS sample
#        
def align_gisaxs_height(  rang = 0.3, point = 21   ):     
        RE(bp.rel_scan([pil1M], stage.y, -rang, rang, point ) )      
        ps()
        mov(stage.y, ps.cen)    

def align_gisaxs_th(  rang = 0.3, point = 21   ):             
        RE(bp.rel_scan([pil1M], stage.th, -rang, rang, point ) )    
        ps()
        mov(stage.th, ps.cen) 
        
        
def align_gisaxs_manual(  rang = 0.3, point = 21   ):     
        RE(bp.rel_scan([pil1M], stage.y, -rang, rang, point ) )      
        ps()
        mov(stage.y, ps.cen)        
        RE(bp.rel_scan([pil1M], stage.th, -rang, rang, point ) )    
        ps()
        mov(stage.th, ps.cen)       
        
def align_gisax( ):     
      align_gisaxs_manual(  rang = 0.3, point = 31   ) 
      align_gisaxs_manual(  rang = 0.2, point = 21   )
      align_gisaxs_manual(  rang = 0.1, point = 11   )
      





            
            
