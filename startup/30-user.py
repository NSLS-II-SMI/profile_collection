print(f'Loading {__file__}')

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
    
    
    
    
def collect_data( exposure_time=1, meta_string=['X','Y', 'Exp'], dets= [  pil1M   ]  ): 
        '''
        dets: [pil1M], collect SAXS data
              [rayonix ] collect MAXS data
              [pil300KW] collect WAXS data
              
              the combination  will collect detectors data  simultineously 
              e..g, [ pil1M, pil300KW] simultineously collect SAXS and WAXS             
              
        '''   
        posy = stage.y.position
        posx =  stage.x.position
        #inc = stage.th.position
        inc = sample.al.position
        arc =   waxs.arc.position
        #md = 'sample: %s, x=%.2f, y=%0.2f, inc=%0.2f, arc=%.2f, exp=%s s.'%(RE.md['sample_name'],posx, posy, inc, arc,  exposure_time )
                 
        posx_ =  create_string(posx)
        posy_ =  create_string(posy) 
        exposure_time_ =  create_string(exposure_time)         
        inc_ = create_string(inc)
        arc_ =   create_string(arc)
        #filename= '%s_%s'%( RE.md['user_name'], RE.md['sample_name'] )
        
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
        print(filename)
        for detector in dets:                                
                detector.cam.file_name.put(filename) 
                detector.cam.acquire_time.put(exposure_time)
                detector.cam.acquire_period.put(exposure_time)                 
                RE( count( [detector] ),  
                Measurement = '%s'%md)  
                
                
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
 	waxs_arc = [7.0, ], dets=[pil1M, pil300KW],   ):
 	
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
    x_list  = [11.4, 7.5, 1.8, -2.17, -11.1]
    samples = [
                'POPC352_A_full',
                'POPC352_A_half',
                'POPC352_B_full',
                'POPC352_B_half',
                'water352',
              ]
    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'

    # Detectors, motors:
    dets = [pil1M, pil300KW, ssacurrent]
    waxs_arc = [11, 11, 1]
    stage_y = [y, y+4, 81]

    for x, sample in zip(x_list, samples):
        yield from bps.mv(stage.x, x)
        yield from bps.mv(stage.y, y)
        det_exposure_time(t)
        sample_id(user_name=sample,
                  sample_name=param)
        # print(RE.md)
        yield from e_grid_scan(dets, waxs.arc, *waxs_arc, stage.y, *stage_y, 0)

    sample_id(user_name='test', sample_name='test')


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
 
    
    
def move_pos(  pos=1  ):
    sam = sample_list[pos-1]
    posx = posx_list[pos-1]    
    print('Move to sample: %s (sample holder position: %s) with posx at: %s.'%(sam,pos,posx) )
    stage.x.move( posx )
    sample_id(  user_name = user_name, sample_name= sam )    
  
            
#Aligam GiSAXS sample
#        
def align_gisaxs_height(  rang = 0.3, point = 21   ):     
        RE(bp.rel_scan([pil1M], sample.y, -rang, rang, point ) )      
        ps()
        mov(sample.y, ps.cen)    

def align_gisaxs_th(  rang = 0.2, point = 21   ):             
        RE(bp.rel_scan([pil1M], sample.al, -rang, rang, point ) )    
        ps()
        mov(sample.al, ps.cen) 

def align_gisaxs_manual(  rang = 0.3, point = 21   ):     
        RE(bp.rel_scan([pil1M], sample.y, -rang, rang, point ) )      
        ps()
        mov(sample.y, ps.cen)        
        RE(bp.rel_scan([pil1M], sample.al, -rang, rang, point ) )    
        ps()
        mov(sample.al, ps.cen)       
        
def align_gisax( ):     
      align_gisaxs_manual(  rang = 0.3, point = 31   ) 
      align_gisaxs_manual(  rang = 0.2, point = 21   )
      align_gisaxs_manual(  rang = 0.1, point = 11   )
      

def grating_rana_temp(det, motor, name='Water_upRepeat', cycle=1, cycle_t=11, n_cycles=20):
    # Slowest cycle:
    temperatures = [302, 305, 310]

    # Medium cycle:
    samples = ['RogerC12', 'C12poly']
    x = [-8.4, 12]
    y = [1.485, 1.47]
    start_angle = [-0.412, -0.35]
    phi = [-0.693, -0.773]
    chi = [0.2, -0.43]

    # Fastest cycle:
    angles = [0.35, 0.25, 0.2]
    # angle_offset = [0.0, 0.1, 0.15]
    angle_offset = [0.35 - x for x in angles]
    x_offset = [0.0, 0.2, 0.4]

    name_fmt = '{sample}_{temperature}K_{angle}deg'

    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        if i_t > 0:
            yield from bps.sleep(1800)
        for i_s, s in enumerate(samples):
            for i_a, a in enumerate(angles):
                sample_name = name_fmt.format(sample=s, temperature=t, angle=a)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bps.mv(stage.x, x[i_s] + x_offset[i_a])
                yield from bps.mv(stage.ch, chi[i_s])
                yield from bps.mv(stage.y, y[i_s])
                yield from bps.mv(stage.th, start_angle[i_s] + angle_offset[i_a])
                yield from bps.mv(prs, phi[i_s])
                sample_id(user_name=name, sample_name=sample_name)
                yield from bps.mv(det.cam.acquire_time, cycle*cycle_t)
                yield from bps.mv(pil1m_bs.x, pil1m_bs.x_center)
                yield from bps.mv(attn_shutter, 'Retract')
                yield from count([det], num=1)
                sample_id(user_name=name, sample_name=f'{sample_name}_sweep20')
                print(f'\n\t=== Sample: {sample_name}_sweep20 ===\n')
                print('... doing fly_scan here ...')
                for i in range(n_cycles):
                    yield from fly_scan(det, motor, cycle, cycle_t, phi[i_s])
                yield from bps.sleep(1)
                yield from bps.mv(attn_shutter, 'Insert')
      
def grating_rana(det, motor, name='SNS2', cycle=1, cycle_t=10.0, n_cycles=10):
    # Medium cycle:
    samples = ['C14.3-0808-150-D45','C16.7-0808-150-D45','C20-0808-150-D45', 'C14.8-2430-170P']
    x = [20, 12, 3, -12]
    y = [1.851, 1.875, 1.9, 1.88]
    align_angle01 = [0.088, 0.155, -0.061, 0.084]
    phi = [-0.405, 0.515, -1.505, -0.547]
    chi = [-0.2,-0.2, -0.2, -0.2]

    # Fastest cycle:
    angles = [0.2, 0.25, 0.35]
    angle_offset = [0.1, 0.15, 0.25]
    name_fmt = '{sample}_{angle}deg'

    for i_s, s in enumerate(samples):
        for i_a, a in enumerate(angles):
            sample_name = name_fmt.format(sample=s, angle=a)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bps.mv(prs, phi[i_s])
            yield from bps.mv(sample.x, x[i_s])
            yield from bps.mv(stage.ch, chi[i_s])
            yield from bps.mv(stage.y, y[i_s])
            yield from bps.mv(sample.al, align_angle01[i_s] - angle_offset[i_a])
            sample_id(user_name=name, sample_name=sample_name)
            yield from bps.mv(det.cam.acquire_time, 1)
            yield from bps.mv(pil1m_bs.x, pil1m_bs.x_center)
            yield from bps.mv(attn_shutter, 'Retract')
            yield from count([det], num=1)
            yield from bps.mv(det.cam.acquire_time, cycle*cycle_t)
            sample_id(user_name=name, sample_name=f'{sample_name}_sweep20')
            print(f'\n\t=== Sample: {sample_name}_sweep20 ===\n')
            print('... doing fly_scan here ...')
            for i in range(n_cycles):
                yield from fly_scan(det, motor, cycle, cycle_t, phi[i_s])
            yield from bps.sleep(1)
            yield from bps.mv(attn_shutter, 'Insert')
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
                
def run_saxs_caps(t=1): 
    x_list  = [-15,-12.8,-6.45,-0.25, 6.43, 12.5, 19.05,25.2]#
    # Detectors, motors:
    dets = [pil1M]
    y_range = [0, 0, 1]
    samples = [ 'LC-O36-6','LC-O36-7','LC-O36-8','LC-O36-9','LC-O37-6','LC-O37-7','LC-O37-8','LC-O37-9']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(stage.x, x)
        sample_id(user_name=sample, sample_name='') 
        yield from escan(dets, stage.y, *y_range)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(1)

def run_saxs_caps_temp(name = 'DB'): 
    # Slowest cycle:
    temperatures = [30, 36, 40, 44, 50]
    x_list  = [-31.88, -25.56, -19.27, -12.92, -6.57, -0.22, 6.05, 12.42, 18.74, 25.09]
    # Detectors, motors:
    dets = [pil1M, ls.ch1_read, xbpm3.sumY]
    y_range = [-3.4, -7.2, 77]
    samples = ['water', 'F3', 'F2', 'F1', 'F0', 'E3', 'E2', 'E0', 'D3', 'D2']
    name_fmt = '{sample}_{temperature}C'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(10)
    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        if i_t > 0:
            yield from bps.sleep(2400)
        
        for x, s in zip(x_list, samples):
            sample_name = name_fmt.format(sample=s, temperature=t)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bps.mv(stage.x, x)
            yield from bps.mv(attn_shutter, 'Retract')
            sample_id(user_name=name, sample_name=sample_name) 
            yield from bp.scan(dets, stage.y, *y_range)
            yield from bps.mv(attn_shutter, 'Insert')  
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
    yield from bps.mv(ls.ch1_sp, 30)    
    
                    
def run_waxs_multi(t=1): 
    x_range = [-3.4, -7.2, 77] 
    x_list  = [-0.025, 0, 0.025]
    #y_offset    
    # Detectors, motors:
    dets = [pil1M, pil300KW,rayonix]
    waxs_arc = [7, 31, 5]
    samples = [ 'SP_Air_in_Airmode','SP_CT_New_Vert','SP_Kapton_in_Airmode']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(stage.x, x)
        sample_id(user_name=sample,sample_name='')               
        yield from escan(dets, waxs.arc, *waxs_arc)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
    
        
def run_ben_giwaxs(t=10):
    # Parameters:
    aligned_075 = [-0.190, -0.203, -0.180]
    x_list  = [-15, -6, 4]
    y_list  = [1.465, 1.253, 1.190]
    chi_list = [-0.2, -0.2, -0.2]
    angle_offset = 0.025
    samples = [ 'Si-wafers',
                'PL1G1A',
                'PL9G1A',        
               ]
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'

    # Detectors, motors:
    dets = [pil300KW, pil300kwroi2, xbpm3.sumX]
    waxs_arc = [7, 25, 4]
    det_exposure_time(t)
    for x, y, a_off, chi, sample in zip(x_list, y_list, aligned_075, chi_list, samples):
        yield from bps.mv(stage.x, x)
        yield from bps.mv(stage.y, y)
        yield from bps.mv(stage.ch, chi)        
        for j, ang in enumerate([a_off, a_off - angle_offset]):
                if j==0:
                   real_ang = 0.075
                else:
                   real_ang = 0.075 + angle_offset
                yield from bps.mv(stage.th, ang)
                param =  'inc_%s'%( real_ang )
                #print(param)        
                sample_id(user_name=sample,
                        sample_name=param)
                #print(RE.md)
                yield from escan(dets, waxs.arc, *waxs_arc)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)

def linkam_fast(n=6):
    yield from bps.mv(attn_shutter, 'Retract')
    yield from bp.scan([pil1M], stage.y, 0.1, 0.9, n)
    yield from bps.mv(attn_shutter, 'Insert')


