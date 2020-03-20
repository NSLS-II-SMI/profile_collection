

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
    
    
def collect_data( exposure_time=1, filename="test", dets= [  pil1M   ]  ): 
        '''
        dets: [pil1M], collect SAXS data
              [rayonix ] collect MAXS data
              [pil300KW] collect WAXS data
              
              the combination  will collect detectors data  simultineously 
              e..g, [ pil1M, pil300KW] simultineously collect SAXS and WAXS             
              
        '''   
         #inc = stage.th.position
        inc = sample.al.position
        arc =   waxs.arc.position
        Att_Shutter.set("Retract")
        for detector in dets:                                
                detector.cam.file_name.put(filename) 
                detector.cam.acquire_time.put(exposure_time)
                detector.cam.acquire_period.put(exposure_time) 
                
        #time.sleep(1)
        Att_Shutter.set("Insert")
                
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
        RE(bp.rel_scan([pil1M,pil1mroi1,pil1mroi2], sample.y, -rang, rang, point ) )      
        ps()
        mov(sample.y, ps.cen)    

def align_gisaxs_th(  rang = 0.3, point = 21   ):             
        RE(bp.rel_scan([pil1M], sample.al, -rang, rang, point ) )    
        ps()
        mov(sample.al, ps.peak)
        
        
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
      

def grating_rana(det, motor, name='Water_upRepeat', cycle=1, cycle_t=11, n_cycles=20):
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
                yield from bps.mv(attn_shutter, 'Retract')
                yield from count([det], num=1)
                sample_id(user_name=name, sample_name=f'{sample_name}_sweep20')
                print(f'\n\t=== Sample: {sample_name}_sweep20 ===\n')
                print('... doing fly_scan here ...')
                for i in range(n_cycles):
                    yield from fly_scan(det, motor, cycle, cycle_t, phi[i_s])
                yield from bps.sleep(1)
                yield from bps.mv(attn_shutter, 'Insert')
                
def run_saxs_caps(t=1): 
    x_list  = [-15,-12.8,-6.45,-0.25, 6.43, 12.5, 19.05,25.2]#
    # Detectors, motors:
    dets = [pil1M]
    y_range = [0, 0, 1]#beginning, end, num pnts
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
    
    
    
    
    
    
    
    
    
    
    
    
    
Att_Align1 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-9}', name='Att_Align1')
Att_Align2 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-10}', name='Att_Align2')
Att_Shutter = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-4}', name='Att_Shutter')
ROIsizey = "XF:12IDC-ES:2{Det:1M}ROI1:SizeY"
ROIMiny = "XF:12IDC-ES:2{Det:1M}ROI1:MinY"
ROIsizex = "XF:12IDC-ES:2{Det:1M}ROI1:SizeX"
ROIMinx = "XF:12IDC-ES:2{Det:1M}ROI1:MinX"


def alignmentmodeNIST():
        if Att_Align1.status.value=='Not Open':
                Att_Align1.set("Insert")
                time.sleep(1)
                Att_Align2.set("Insert")
                time.sleep(1)
                pos = pil1m_bs_rod.x.position
                pil1m_bs_rod.x.move(pos+10)
        Att_Shutter.set("Retract")
        if waxs.arc.position < 12 :
                mov(waxs.arc,12)
        pil1M.cam.file_name.put("NISTsnap")
        pil300KW.cam.file_name.put("NISTsnap")
        
def measurementmodeNIST():
        if Att_Shutter.status.value=='Not Open':
                Att_Shutter.set("Insert")
                pos = pil1m_bs_rod.x.position
                pil1m_bs_rod.x.move(pos-10)
        time.sleep(1)
        Att_Align1.set("Retract")
        time.sleep(1)
        Att_Align2.set("Retract")
        #mov(waxs.arc,3)

def snapNIST(t=1,dets=[pil1M,]):
        openedalready=0
        if Att_Shutter.status.value=='Not Open':
                openedalready = 1
        det_exposure_time(t)
        x = stage.x.position
        x_range  = [x, x, 1]
        yield from escan(dets, stage.x, *x_range)
        if openedalready==1:
                Att_Shutter.set("Retract")
        

def alignNISTgi():
        alignmentmodeNIST()
        caput(ROIMiny,547)#902
        caput(ROIsizey,30)
        caput(ROIMinx,438)
        caput(ROIsizex,51)
        
        align_gisaxs_height(1,16)
        align_gisaxs_th(1,11)
        align_gisaxs_height(.5,11)
        align_gisaxs_th(.5,11)
        mov(sample.al, ps.peak -.3)
        caput(ROIMiny,251)#606
        caput(ROIsizey,7)
        caput(ROIMinx,424)
        caput(ROIsizex,88)
        align_gisaxs_th(.5,31)
        align_gisaxs_height(.2,11)
        align_gisaxs_th(.2,11)
        align_gisaxs_th(.1,21)
        mov(sample.al, ps.cen+.6)
        measurementmodeNIST()
        
        
def ctNIST(): 
    x = stage.x.position
    x_range  = [x, x, 1]
    dets = [pil1M]
    yield from escan(dets, stage.x, *x_range)
       
def NISTdoGrazing():
        xlocs = [-19,-12,-6,8,16]
        names = ['AB_ToSp','AB_CFSp','AB_ToBl','AB_CFBl','AB_DMBp05']
        prealigned = [1,0,0,0,0]
        for xloc, name, aligned in zip(xlocs, names, prealigned):
                mov(stage.x,xloc)
                mov(sample.al,ps.peak+.3)
                if aligned==0 :
                        alignNISTgi()
                        plt.close('all')
                NIST_gi_sample('NIST_',name,ps.peak+.3,1,.02,[-.6,-.4,-1],[pil300KW,pil1M,xbpm3.sumY],waxsangles = [2.74,8.74,14.74], energies= [2450,2480,2500])

def NISTdoTempExp(username = 'NIST', samplename = 'Alex_ToSp',sample_al = .6,en = 2478, xstep =.01, starttemp=45, endtemp=215, ramprate=2, waxsangles = [2.74,8.74,14.74], dets = [pil1M, pil300KW],align=0,exposure_time=1):
        if(align):
                alignNISTgi()
                plt.close('all')
                mov(sample.al,ps.peak+.3-sample_al) # incident angle is only set if alignment is included
        mov(waxs.arc,2.74)
        energy.move(en)
        basename = '%s_%s_%.0feV_inc%.2f'%(username, samplename, en, sample_al)
        caput("XF:12IDC:LS336:TC1:OnRamp1",0) # turn the ramp off
        ls.ch1_sp.put(starttemp) # set the setpoint to starting temperature
        caput("XF:12IDC:LS336:TC1:HTR1:Range",3) # turn on the heater
        while abs(ls.ch1_read.value - starttemp) > .1 : # wait for the temperature to reach starting temperature
                print('Temp = %.2f°C - Waiting for stage to reach %.2f°C'%(ls.ch1_read.value, starttemp))
                time.sleep(5)
        caput("XF:12IDC:LS336:TC1:HTR1:Range",0) # turn off the heater
        print('Temp = %.2f°C - Starting temperature reached, beginning %.2f°C/minute ramp'%(ls.ch1_read.value, ramprate))
        caput("XF:12IDC:LS336:TC1:RampR1",ramprate) # set the ramp speed to the imput ramprate deg / minute
        time.sleep(5)
        caput("XF:12IDC:LS336:TC1:OnRamp1",1) # turn on the ramp
        time.sleep(5)
        ls.ch1_sp.put(endtemp) # set the setpoint to ending temperature
        caput("XF:12IDC:LS336:TC1:HTR1:Range",3) # turn on the heater
        while ls.ch1_read.value < endtemp:
                currenttemperature = ls.ch1_read.value  + .15 * len(waxsangles) * ramprate  # assume the temperature will change so for this set use an adjusted current temperature
                for waxsangle in waxsangles:
                        mov(waxs.arc,waxsangle)
                        cur_xh = stage.x.position
                        stage.x.move( cur_xh + xstep )
                        filename = '%s_w%.1fdeg_%.0fdegC'%(basename, waxs.arc.position, currenttemperature)
                        print('Temp = %.2fdegC - filename : %s'%(ls.ch1_read.value, filename))
                        for detector in [pil300KW,pil1M] :
                                detector.cam.file_name.put(filename) 
                        RE(snapNIST(dets=dets,t=exposure_time))
        
        caput("XF:12IDC:LS336:TC1:OnRamp1",0)   # turn off ramping
        ls.ch1_sp.put(starttemp)                # setpoint to start temp
        caput("XF:12IDC:LS336:TC1:HTR1:Range",0)# turn off heating
        
                        #caput("XF:12IDC:LS336:TC1:OnRamp1",0) #ramp on: 1 off : 0
                        #caput("XF:12IDC:LS336:TC1:HTR1:Range",0) # heater on : 3 off:0
                        #caput("XF:12IDC:LS336:TC1:RampR1",1)#deg / min
                        #ls.ch1_sp.set(30) #sets the setpoint to 30 degrees C
                        #ls.ch1_read.value #outputs the current temperature

def NISTdoTransmission():
        xlocs = [14.5,9.5,3.5,-2,-7]
        ylocs = [-3.6,-3.6,-3.6,-3.6,-3.6]
        names = ['EPFL_NTP3','EPFL_BP3MI','EPFL_BJ61MI','EPFL_NTJ61','EPFL_NTMI']
        for xloc, yloc, name in zip(xlocs, ylocs, names):
                mov(stage.x , xloc)
                mov(sample.y, yloc)
                NIST_trans_sample(user_name = 'NIST',sample_name = name, exposure_time = 1 , dets=[pil300KW,pil1M,xbpm3.sumY],waxsangles = [2.74,8.74,14.74], energies= [2450,2470,2473,2475,2476,2477,2478,2479,2480,2481,2483,2485,2490,2495,2500,2510],xstep=-.02)



def waxs_S_edge(t=1):
    dets = [pil300KW, pil1M]
    
    names = ['P3MEEMT_AS','P3MEEMT_115','P3MEEMT_145','P3HT_lowMW','P3HT_1500','P3HHT_DB','P3HHT_CB','blank_Si']
    x = [52000,42700,34500,27500,18000,10500,2500,-4500]

    names_PA = ['TP100','TM100','M6','M8','M10']
    x_PA = [-13500,-24500,-28500,-41500,-47500]

    energies = [2450, 2470, 2473, 2475, 2476,2477,2478,2479,2480,2481,2483,2485,2490,2495,2500,2510]
    waxs_arc = [15, 0]
    
    for name, xs in zip(names, x):
        yield from bps.mv(piezo.x, xs)
        
        yield from alignement_gisaxs(0.25)

        yield from bps.mvr(piezo.th, 0.7)
        
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_ai0.7_wa{wax}'
        
        for wa in waxs_arc:
            if wa == 0:
                yield from bps.mv(att2_10, 'Insert')
            else:
                yield from bps.mv(att2_9, 'Insert')
            yield from bps.mv(waxs, wa)
            yield from bps.mvr(piezo.x, 500)
        
            for e in energies:                              
                yield from bps.mv(energy, e)
                sample_name = name_fmt.format(sample=name, energy=e, wax = wa)
                sample_id(user_name='PB', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num =1)

            yield from bps.mv(energy, 2490)
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)
        yield from bps.mvr(piezo.th, -0.7)
        
    yield from bps.mv(energy, 2475)
    yield from bps.mv(energy, 2500)
    yield from bps.mv(energy, 2525)
    yield from bps.mv(energy, 2550)
    yield from bps.mv(energy, 2575)
    yield from bps.mv(energy, 2600)
    yield from bps.mv(energy, 2620)
    yield from bps.mv(energy, 2630)
    yield from bps.mv(energy, 2640)
    yield from bps.mv(energy, 2650)
    
    yield from bps.mv(GV7.close_cmd, 1 )
    time.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1 )
    
    
    waxs_arc = [53.5, 60, 66.5]
    for name, xs in zip(names_PA, x_PA):
        yield from bps.mv(piezo.x, xs)

        yield from alignement_gisaxs(0.25)
        yield from bps.mvr(piezo.th, 0.7)

        det_exposure_time(30, 30) 
        name_fmt = '{sample}_2650eV_ai0.7_wa{wax}'

        for wa in waxs_arc:
                yield from bps.mv(waxs, wa)
                yield from bps.mvr(piezo.x, 500)
                sample_name = name_fmt.format(sample=name, wax = wa)

                sample_id(user_name='PB', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count([pil300KW], num =1)


                
#For one smaple, run gi_saxs with different incident angle and different waxs_arc and differen energies using SAXS and WAXS det        
def NIST_gi_sample(user_name='X90', samplename='2472-2480eV', alpha= -0.344, exposure_time = 0.5,
	xstep = 0.500,  relalphas = [0, -0.12], dets=[pil1M, pil300KW], waxsangles = [3,9,15], energies= [2452]  ):
 	
        ''' 
        For one smaple, run GISAXS/WAXS with different incident angle and different waxs_arc using SAXS and WAXS det
        alpha is the zero angle
        relalphas are the offset from the zero angle (the real incident angles you want to measure)
	xstep: x step in mm to put in slightly new spot for each step - be careful this wont wander off the sample, to a stage limit or to a bad area of the sample
 	waxs_arc: the waxs arc angle for WAXS data collection        
         '''
        sample_id(  user_name = user_name, sample_name= samplename )
        #for detector in dets:
        #        detector.cam.acquire_time.put(exposure_time)
        #        detector.cam.acquire_period.put(exposure_time)
        det_exposure_time(exposure_time)
        for en in energies:
                print('Moving to %s eV'%en)
                energy.move(en)
                for waxsangle in waxsangles:
                        print('Moving WAXS detector to %s degrees'%waxsangle)
                        mov(waxs.arc,waxsangle)
                        for aloffset in relalphas:
                                actual_alpha = alpha + aloffset 
                                print('Start measurement for incident angle %s degrees'%aloffset)
                                mov(sample.al, actual_alpha)
                                cur_xh = stage.x.position
                                stage.x.move( cur_xh + xstep )
                    
                                filename= '%s_%s'%(user_name, samplename)
                                filename += '_Inc%s'%(-aloffset)
                                filename += '_En%.6s'%(energy.position.energy)
                                filename += '_w%s'%(waxsangle)
                                for detector in [pil300KW,pil1M] :
                                        detector.cam.file_name.put(filename) 
                                RE(snapNIST(dets=dets,t=exposure_time))
def NIST_trans_sample(user_name='X90', sample_name='2472-2480eV', exposure_time = 1,
	dets=[pil1M, pil300KW], waxsangles = [2.74,8.74,14.74], energies= [2478]  ,xstep=.02):
 	
        ''' 
        For one smaple, run saxs with different waxs_arc and energies using SAXS and WAXS det
        
	waxs_arc: the waxs arc angle for WAXS data collection        
         '''
        sample_id(  user_name = user_name, sample_name= sample_name )
        det_exposure_time(exposure_time)
        for waxsangle in waxsangles:
                print('Moving WAXS detector to %s degrees'%waxsangle)
                mov(waxs.arc,waxsangle)
                for en in energies:
                        print('Moving to %s eV'%en)
                        energy.move(en)
                        cur_xh = stage.x.position
                        stage.x.move( cur_xh + xstep )
                        filename= '%s_%s'%(user_name, sample_name)
                        filename += '_En%.6s'%(energy.position.energy)
                        filename += '_w%s'%(waxsangle)
                        for detector in [pil300KW,pil1M] :
                                detector.cam.file_name.put(filename) 
                        RE(snapNIST(dets=dets,t=exposure_time))
#def NISTWAXsalign
#        #alignmentmodeNIST()
#        caput(ROIMiny,902)
#        caput(ROIsizey,30)
#        caput(ROIMinx,438)
#        caput(ROIsizex,51)
#        
#        align_gisaxs_height(1,16)
#        align_gisaxs_th(1,11)
#        align_gisaxs_height(.5,11)
#        align_gisaxs_th(.5,11)
#        mov(sample.al, ps.peak -.3)
#        caput(ROIMiny,606)
#        caput(ROIsizey,7)
#        caput(ROIMinx,424)
##        caput(ROIsizex,88)
 #       align_gisaxs_th(.5,31)
 #       align_gisaxs_height(.2,11)
 #       align_gisaxs_th(.2,11)
 #       align_gisaxs_th(.1,21)
 #       mov(sample.al, ps.cen+.6)
 #       measurementmodeNIST()
Att_al91x = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-9}', name='Att_al91x')
Att_al92x = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-10}', name='Att_al92x')
Att_al94x = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-11}', name='Att_al94x')
Att_al96x = TwoButtonShutter('XF:12IDC-OP:2{Fltr:2-12}', name='Att_al96x')
def NISTrefl(usernames=['NIST'] , samplenames=['Jacob1'],angleoffsets=[-.41], xlocs=[4.66],ylocs=[0],energies=[2470,2480,2500]):

        for username, samplename, yloc, angoff, xloc in zip(usernames, samplenames, ylocs, angleoffsets, xlocs):
                print('Moving to %s'%samplename)
                sample.y.move( yloc )
                sample.x.move( xloc )
                for en in energies:
                        print('Moving to %s eV'%en)
                        Att_al94x.set("Insert")
                        energy.move(en)
                        time.sleep(2)
                        Att_al96x.set("Retract")
                        time.sleep(2)
                        Att_al91x.set("Retract")
                        time.sleep(2)
                        Att_al92x.set("Retract")
                        time.sleep(2)
                        filename = samplename+'_En%.6s_%s_to_%s_36umAl'%(energy.position.energy, 0,2)
                        sample_id(user_name=username, sample_name=filename)
                        RE(e_inner_scan([pil300KW,pil300kwroi2,pil300kwroi1,pil300kwroi3,pil300kwroi4,xbpm3.sumY], 101, prs, 0 + angoff, -2 + angoff, waxs.arc, 0, 4))
                        
                        
                        Att_al91x.set("Insert")
                        time.sleep(2)
                        Att_al92x.set("Insert")
                        time.sleep(2)
                        Att_al94x.set("Retract")
                        time.sleep(2)
                        filename = samplename+'_En%.6s_%s_to_%s_27umAl'%(energy.position.energy, 1.7,3.7)
                        sample_id(user_name=username, sample_name=filename)
                        
                        RE(e_inner_scan([pil300KW,pil300kwroi2,pil300kwroi1,pil300kwroi3,pil300kwroi4,xbpm3.sumY], 101, prs, -1.7 + angoff, -3.7 + angoff, waxs.arc, 3.4, 7.4))  
                        
                        
                        Att_al91x.set("Retract")
                        time.sleep(2)
                        filename = samplename+'_En%.6s_%s_to_%s_18umAl'%(energy.position.energy, 3.4,7.4)
                        sample_id(user_name=username, sample_name=filename)
                        RE(e_inner_scan([pil300KW,pil300kwroi2,pil300kwroi1,pil300kwroi3,pil300kwroi4,xbpm3.sumY], 101, prs ,-3.4 + angoff, -7.4 + angoff, waxs.arc, 6.8, 14.8))
                        
                        
                        Att_al91x.set("Insert")
                        time.sleep(2)
                        Att_al92x.set("Retract")
                        time.sleep(2)
                        filename = samplename+'_En%.6s_%s_to_%s_9umAl'%(energy.position.energy, 7,11)
                        sample_id(user_name=username, sample_name=filename)
                        RE(e_inner_scan([pil300KW,pil300kwroi2,pil300kwroi1,pil300kwroi3,pil300kwroi4,xbpm3.sumY], 101, prs, -7 + angoff, -11 + angoff, waxs.arc, 14, 22))
                        
                        plt.close('all')
def NIST_writecsvs(num=10):
        headers = db[-num:]
        for header in headers:
                #header.table().to_csv('%s_%s_%.1f.csv'%(header.start['user_name'],header.start['sample_name'],header.start['time']))
                with open('%s_%s_%.1f_header.txt'%(header.start['user_name'],header.start['sample_name'],header.start['time']), "w") as text_file:
                        text_file.write('%s'%(header.start))


