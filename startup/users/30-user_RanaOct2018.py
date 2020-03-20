from ophyd import (PVPositioner, EpicsSignal, EpicsSignalRO, EpicsMotor,
                   Device, Signal, PseudoPositioner, PseudoSingle)



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
    

    
def move_pos(  pos=1  ):
    sam = sample_list[pos-1]
    posx = posx_list[pos-1]    
    print('Move to sample: %s (sample holder position: %s) with posx at: %s.'%(sam,pos,posx) )
    stage.x.move( posx )
    sample_id(  user_name = user_name, sample_name= sam )    
  
            
#Aligam GiSAXS sample
#        
def align_gisaxs_heightRana(  rang = 0.1, point = 21   ):     
        RE(bp.rel_scan([pil1M], stage.y, -rang, rang, point ) )      
        ps()
        mov(stage.y, ps.cen)    

def align_gisaxs_thRana(  rang = 0.1, point = 21   ):             
        RE(bp.rel_scan([pil1M], stage.th, -rang, rang, point ) )    
        ps()
        mov(sample.al, ps.cen) 

def align_gisaxs_manual(  rang = 0.3, point = 21   ):     
        RE(bp.rel_scan([pil1M], s.y, -rang, rang, point ) )      
        ps()
        mov(sample.y, ps.cen)        
        RE(bp.rel_scan([pil1M], sample.al, -rang, rang, point ) )    
        ps()
        mov(sample.al, ps.cen)       
        
def align_gisax( ):     
      align_gisaxs_manual(  rang = 0.3, point = 31   ) 
      align_gisaxs_manual(  rang = 0.2, point = 21   )
      align_gisaxs_manual(  rang = 0.1, point = 11   )
      

def grating_rana_temp_oct(det, motor, name='water-down', cycle=1, cycle_t=10, n_cycles=5):
    # Slowest cycle:
    temperatures = [37, 35, 32, 30, 27]

    # Medium cycle:
    samples = ['C11.7-NIPAM-2-DOPC', 'C24-NIPAM-2-DOPC']
    x = [10.5, -9]
    y = [-2.653, -2.653]
    align_angle01 = [-0.162, -0.216]
    phi = [1.507, 1.056]
    chi = [-0.2, -0.2]

    # Fastest cycle:
    angles = [0.2, 0.25, 0.35]
    angle_offset = [0.05, 0.1, 0.2]
    #angle_offset = [0.35 - x for x in angles]
    x_offset = [0.0, 0.2, 0.4]

    name_fmt = '{sample}_{temperature}C_{angle}deg'

    for i_t, t in enumerate(temperatures):
        yield from bps.mv(ls.ch1_sp, t)
        if i_t > 0:
            yield from bps.sleep(600)
        for i_s, s in enumerate(samples):
            for i_a, a in enumerate(angles):
                temp = ls.ch1_read.value
                yield from bps.mv(prs, 0)
                sample_name = name_fmt.format(sample=s, temperature=temp, angle=a)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bps.mv(sample.x, x[i_s])
                yield from bps.mv(sample.ka, chi[i_s])
                yield from bps.mv(stage.y, y[i_s])
                yield from bps.mv(stage.th, align_angle01[i_s] - angle_offset[i_a])
                yield from bps.mv(prs, phi[i_s])
                sample_id(user_name=name, sample_name=sample_name)
                yield from bps.mv(det.cam.acquire_time, 5)
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
                yield from bps.mv(prs, 0)
      
def grating_rana_oct(det, motor, name='SNS', cycle=1, cycle_t=10.0, n_cycles=1):
    # Medium cycle:
    samples = ['C11.7-NIPAM']
    x = [-11]
    y = [-2.575]
    align_angle01 = [-0.212]
    phi = [1.304]
    chi = [-0.2]

    # Fastest cycle:
    angles = [0.2, 0.25, 0.35]
    angle_offset = [0.05, 0.1, 0.2]
    name_fmt = '{sample}_{angle}deg'

    for i_s, s in enumerate(samples):
        for i_a, a in enumerate(angles):
            sample_name = name_fmt.format(sample=s, angle=a)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bps.mv(prs, phi[i_s])
            yield from bps.mv(sample.x, x[i_s])
            yield from bps.mv(sample.ka, chi[i_s])
            yield from bps.mv(stage.y, y[i_s])
            yield from bps.mv(stage.th, align_angle01[i_s] - angle_offset[i_a])
            sample_id(user_name=name, sample_name=sample_name)
            yield from bps.mv(det.cam.acquire_time, 0.1)
            #yield from bps.mv(pil1m_bs_rod.x, pil1m_bs_rod.x_center)
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
    yield from bps.mv(prs, 0)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)

pil1m_x = EpicsMotor('XF:12IDC-ES:2{Det:1M-Ax:X}Mtr', name='pil1m_x')
                
def alignmentmodeRana():
        if Att_Align3.status.value=='Not Open':
               #Att_Align2.set("Insert")
               #time.sleep(1)
               Att_Align3.set("Insert")
               time.sleep(1)
               pos = pil1m_bs_rod.x.position
               pil1m_bs_rod.x.move(pos+25)
        Att_Shutter.set("Retract")
        if waxs.arc.position < 12 :
                mov(waxs.arc,12)
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(1)
        pil1m_x.move(-0.8)

        
def measurementmodeRana():
        if Att_Shutter.status.value=='Not Open':
                Att_Shutter.set("Insert")
                pos = pil1m_bs_rod.x.position
                pil1m_bs_rod.x.move(pos-25)
        time.sleep(1)
        #Att_Align2.set("Retract")
        #time.sleep(1)
        Att_Align3.set("Retract")
        time.sleep(1)
        pil1m_x.move(-0.2)
        #mov(waxs.arc,3)

