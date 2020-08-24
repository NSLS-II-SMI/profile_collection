print(f'Loading {__file__}')

def export_scan( sid, filename='', path='/home/xf12id/tmp/',verbose=True ):
    """
    Export table by giving a scan id
    """
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
    return(xmax)


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


def move_pos(  pos=1  ):
    sam = sample_list[pos-1]
    posx = posx_list[pos-1]    
    print('Move to sample: %s (sample holder position: %s) with posx at: %s.'%(sam,pos,posx) )
    stage.x.move( posx )
    sample_id(  user_name = user_name, sample_name= sam )    
  

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
                yield from bps.mv(pil1m_bs_rod.x, pil1m_bs_rod.x_center)
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
            yield from bps.mv(pil1m_bs_rod.x, pil1m_bs_rod.x_center)
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


