

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
def align_gisaxs_height_NIST(  rang = 0.3, point = 21 ,der=False  ):     
        RE(bp.rel_scan([pil1M,pil1mroi1,pil1mroi2], piezo.y, -rang, rang, point ) )      
        ps_nist(der=der)
        mov(piezo.y, ps.cen)

def align_gisaxs_th_NIST(  rang = 0.3, point = 21   ):             
        RE(bp.rel_scan([pil1M], piezo.th, -rang, rang, point ) )    
        ps_nist()
        mov(piezo.th, ps.peak)
        

        
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
    
    
    
    
    
    
    
    
    
    
    
    
    
Att_Align1 = att2_6#att1_12
Att_Align2 = att2_11#att1_9
alignbspos = 11.7
measureBSpos = 1.7
ROIsizey = "XF:12IDC-ES:2{Det:1M}ROI1:SizeY"
ROIMiny = "XF:12IDC-ES:2{Det:1M}ROI1:MinY"
ROIsizex = "XF:12IDC-ES:2{Det:1M}ROI1:SizeX"
ROIMinx = "XF:12IDC-ES:2{Det:1M}ROI1:MinX"


def alignmentmodeNIST():
        Att_Align1.set("Insert")
        time.sleep(1)
        Att_Align2.set("Insert")
        time.sleep(1)
        pil1m_bs_rod.x.move(alignbspos)
        if waxs.arc.position < 12 :
                mov(waxs.arc,12)
        pil1M.cam.file_name.put("NISTsnap")
        pil300KW.cam.file_name.put("NISTsnap")
        
def measurementmodeNIST():
        pil1m_bs_rod.x.move(measureBSpos)
        time.sleep(1)
        Att_Align1.set("Retract")
        time.sleep(1)
        Att_Align2.set("Retract")
        time.sleep(1)
        att2_12.set("Insert")
        time.sleep(1)
        #mov(waxs.arc,3)

def snapNIST(t=1,dets=[pil1M,]):
        det_exposure_time(t)
        yield from bp.count(dets,num=1)
        

def alignNISTgi():
        alignmentmodeNIST()
        caput(ROIMiny,863)#902
        caput(ROIsizey,100)
        caput(ROIMinx,366)
        caput(ROIsizex,100)
        
        align_gisaxs_height_NIST(1000,16,der=True)
        align_gisaxs_th_NIST(1000,11)
        align_gisaxs_height_NIST(500,11,der=True)
        align_gisaxs_th_NIST(500,11)
        mov(piezo.th, ps.peak -150)
        caput(ROIMiny,750)#606
        caput(ROIsizey,10)
        caput(ROIMinx,366)
        caput(ROIsizex,100)
        align_gisaxs_th_NIST(500,31)
        align_gisaxs_height_NIST(200,11)
        align_gisaxs_th_NIST(200,11)
        align_gisaxs_th_NIST(100,21)
        mov(piezo.th, ps.cen+300)
        measurementmodeNIST()
        
        
def ctNIST(): 
    x = stage.x.position
    x_range  = [x, x, 1]
    dets = [pil1M]
    yield from escan(dets, stage.x, *x_range)
       
def NISTdoGrazing():
        #xlocs = [48403]
        #names = ['BW30-CH-Br-1']
   
        xlocs = [56000,44000,34000,23000,8000,-4000]
        names = ['BW30-CH-2-5keVb','BW30-CH-Br-2-5keVb','BWXLE-CH-2-5keVb','BWXLE-CH-Br-2-5keVb','NF90-CH-2-5keVb','NF90-CH-Br-2-5keVb']
        prealigned = [0,0,0,0,0,0]
        for xloc, name, aligned in zip(xlocs, names, prealigned):
                mov(piezo.x,xloc)
                mov(piezo.th,ps.peak+150)
                if aligned==0 :
                        alignNISTgi()
                        plt.close('all')
                NIST_gi_sample('DOW_',name,ps.peak+150,1,20,[-50, -200, -400, -600],[pil300KW,pil1M,xbpm3.sumY,pil1mroi2,pil1mroi3,pil1mroi4],waxsangles = [3,9,15,21,27,33,39,45], energies= [5015,5020,5025])

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
                
                #sample_id(user_name='DOW', sample_name='NF90-CH-Br-1-En-thp3-correct') 
                #mov(waxs.arc,12)
                #RE(bp.scan([pil1M,pil1mroi2,pil1mroi4,pil1mroi3,xbpm3.sumY], energy,4900, 5100, 41))  
                #mov(waxs.arc,3)
                #RE(bp.scan([pil300KW,pil300kwroi2,pil300kwroi4,pil300kwroi3,xbpm3.sumY], energy,4900, 5100, 41))
                #energy sca
                #
                #sample_id(user_name='DOW', sample_name='NF90-CH-Br-1-En-thp3-correct') 
                #mov(waxs.arc,12)
                #RE(bp.scan([pil1M,pil1mroi2,pil1mroi4,pil1mroi3,xbpm3.sumY], piezo.th,-100, -1000, 41))  
                #mov(waxs.arc,3)
                #RE(bp.scan([pil300KW,pil300kwroi2,pil300kwroi4,pil300kwroi3,xbpm3.sumY], piezo.th,-100, -1000, 41))
                #alpha scan
                
                #mov(piezo.th, ps.peak - alphaangle) #move incident angle
                
                
                
                
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
                                mov(piezo.th, actual_alpha)
                                cur_xh = piezo.x.position
                                piezo.x.move( cur_xh + xstep )
                    
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

def ps_nist(uid='-1',det='default',suffix='default',shift=.5,logplot='off', der  = False ):
    '''
    YG Copied from CHX beamline@March 18, 2018
    function to determine statistic on line profile (assumes either peak or erf-profile)
    calling sequence: uid='-1',det='default',suffix='default',shift=.5)
    det='default' -> get detector from metadata, otherwise: specify, e.g. det='eiger4m_single'
    suffix='default' -> _stats1_total / _sum_all, otherwise: specify, e.g. suffix='_stats2_total'
    shift: scale for peak presence (0.5 -> peak has to be taller factor 2 above background)
    '''
    #import datetime
    #import time
    #import numpy as np
    #from PIL import Image
    #from databroker import db, get_fields, get_images, get_table
    #from matplotlib import pyplot as pltfrom
    #from lmfit import  Model
    #from lmfit import minimize, Parameters, Parameter, report_fit
    #from scipy.special import erf

    # get the scan information:
    if uid == '-1':
        uid=-1
    if det == 'default':
        if db[uid].start.detectors[0] == 'elm' and suffix=='default':
            intensity_field='elm_sum_all'
        elif db[uid].start.detectors[0] == 'elm':
            intensity_field='elm'+suffix
        elif suffix == 'default':
            intensity_field= db[uid].start.detectors[0]+'_stats1_total'
        else:
            intensity_field= db[uid].start.detectors[0]+suffix
    else:
        if det=='elm' and suffix == 'default':
            intensity_field='elm_sum_all'
        elif det=='elm':
            intensity_field = 'elm'+suffix
        elif suffix == 'default':
            intensity_field=det+'_stats1_total'
        else:
            intensity_field=det+suffix

    field = db[uid].start.motors[0]

    #field='dcm_b';intensity_field='elm_sum_all'
    [x,y,t]=get_data(uid,field=field, intensity_field=intensity_field, det=None, debug=False)  #need to re-write way to get data
    x=np.array(x)
    y=np.array(y)
    #print(t)
    if der:
        y = np.diff( y )
        x = x[1:]
        
    PEAK=x[np.argmax(y)]
    PEAK_y=np.max(y)
    COM=np.sum(x * y) / np.sum(y)

    ### from Maksim: assume this is a peak profile:
    def is_positive(num):
        return True if num > 0 else False

    # Normalize values first:
    ym = (y - np.min(y)) / (np.max(y) - np.min(y)) - shift  # roots are at Y=0

    positive = is_positive(ym[0])
    list_of_roots = []
    for i in range(len(y)):
        current_positive = is_positive(ym[i])
        if current_positive != positive:
            list_of_roots.append(x[i - 1] + (x[i] - x[i - 1]) / (abs(ym[i]) + abs(ym[i - 1])) * abs(ym[i - 1]))
            positive = not positive
    if len(list_of_roots) >= 2:
        FWHM=abs(list_of_roots[-1] - list_of_roots[0])
        CEN=list_of_roots[0]+0.5*(list_of_roots[1]-list_of_roots[0])
        ps.fwhm=FWHM
        ps.cen=CEN
        #return {
        #    'fwhm': abs(list_of_roots[-1] - list_of_roots[0]),
        #    'x_range': list_of_roots,
       #}
    else:    # ok, maybe it's a step function..
        print('no peak...trying step function...')
        ym = ym + shift
        def err_func(x, x0, k=2000, A=1,  base=0 ):     #### erf fit from Yugang
            return base - A * erf(k*(x-x0))
        mod = Model(  err_func )
        ### estimate starting values:
        x0=np.mean(x)
        #k=0.1*(np.max(x)-np.min(x))
        pars  = mod.make_params( x0=x0, k=2000,  A = 1000000, base = 0. )
        result = mod.fit(ym, pars, x = x )
        CEN=result.best_values['x0']
        FWHM = result.best_values['k']
        ps.cen = CEN
        ps.fwhm = x0

    ### re-plot results:
    if logplot=='on':
        plt.close(999)
        plt.figure(999)
        plt.semilogy([PEAK,PEAK],[np.min(y),np.max(y)],'k--',label='PEAK')
        plt.hold(True)
        plt.semilogy([CEN,CEN],[np.min(y),np.max(y)],'r-.',label='CEN')
        plt.semilogy([COM,COM],[np.min(y),np.max(y)],'g.-.',label='COM')
        plt.semilogy(x,y,'bo-')
        plt.xlabel(field);plt.ylabel(intensity_field)
        plt.legend()
        plt.title('uid: '+str(uid)+' @ '+str(t)+'\nPEAK: '+str(PEAK_y)[:8]+' @ '+str(PEAK)[:8]+'   COM @ '+str(COM)[:8]+ '\n FWHM: '+str(FWHM)[:8]+' @ CEN: '+str(CEN)[:8],size=9)
        plt.show()
    else:
        plt.close(999)
        plt.figure(999)
        plt.plot([PEAK,PEAK],[np.min(y),np.max(y)],'k--',label='PEAK')
        plt.hold(True)
        plt.plot([CEN,CEN],[np.min(y),np.max(y)],'r-.',label='CEN')
        plt.plot([COM,COM],[np.min(y),np.max(y)],'g.-.',label='COM')
        plt.plot(x,y,'bo-')
        plt.xlabel(field);plt.ylabel(intensity_field)
        plt.legend()
        plt.title('uid: '+str(uid)+' @ '+str(t)+'\nPEAK: '+str(PEAK_y)[:8]+' @ '+str(PEAK)[:8]+'   COM @ '+str(COM)[:8]+ '\n FWHM: '+str(FWHM)[:8]+' @ CEN: '+str(CEN)[:8],size=9)
        plt.show()

    ### assign values of interest as function attributes:
    ps.peak=PEAK
    ps.com=COM
    #return x, y 


