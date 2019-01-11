

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
    
    
   
def move_pos(  pos=1  ):
    sam = sample_list[pos-1]
    posx = posx_list[pos-1]    
    print('Move to sample: %s (sample holder position: %s) with posx at: %s.'%(sam,pos,posx) )
    stage.x.move( posx )
    sample_id(  user_name = user_name, sample_name= sam )    
  
            
#Aligam GiSAXS sample
#        
def align_gisaxs_heightRPI(  rang = 0.3, point = 21   ):     
        RE(bp.rel_scan([pil1M,pil1mroi1,pil1mroi2], sample.y, -rang, rang, point ) )      
        ps()
        mov(sample.y, ps.cen)    

def align_gisaxs_thRPI(  rang = 0.3, point = 21   ):             
        RE(bp.rel_scan([pil1M], sample.al, -rang, rang, point ) )    
        ps()
        mov(sample.al, ps.peak)
        
        ali
def align_gisaxs_manualRPI(  rang = 0.3, point = 21   ):     
        RE(bp.rel_scan([pil1M], sample.y, -rang, rang, point ) )      
        ps()
        mov(sample.y, ps.cen)        
        RE(bp.rel_scan([pil1M], sample.al, -rang, rang, point ) )    
        ps()
        mov(sample.al, ps.cen)       
        
def align_gisaxsRPI( ):     
      #align_gisaxs_manualRPI(  rang = 0.3, point = 31   ) 
      align_gisaxs_manualRPI(  rang = 0.2, point = 31   )
      align_gisaxs_manualRPI(  rang = 0.1, point = 21   )
      
def run_saxs_capsRPI(t=1): 
    x_list  = [ -18.9,-14.16,-8.8,-4.2,0.08,6.13,11.6,18.4]#
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [2.94, 8.94, 2] #[2.64, 8.64, 2]
    samples = [   'LCF-FILM-1', 'LCF-FILM-2', 'LCF-FILM-3', 'LCF-FILM-4', 'LCF-FILM-5', 'LCF-FILM-6', 'LCF-FILM-7', 'LCF-FILM-8']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(stage.x, x)
        sample_id(user_name=sample, sample_name='') 
        yield from escan(dets, waxs.arc, *waxs_arc)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 

def run_saxsRPI(t=1): 
    name = 'LC'
    x_list  = [-18.63,-12.2,-5.85,0.7, 6.9, 12.95]#
    # Detectors, motors:
    dets = [pil1M]
    y_range = [-3, -6, 11]
    samples = [ 'LC-O38-6','LC-O37-6','LC-O35-7','LC-O36-6','LC-O35-6','LC-O35-8']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(stage.x, x)
        sample_id(user_name=name, sample_name=sample) 
        yield from escan(dets, stage.y, *y_range)
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 
   
    
def run_giwaxs_RPI(t=2):
    name = 'Fink'
    measurementmodeRPI()
    # Parameters:
    aligned_075 = [0.011, -0.07741, -0.079]
    x_list  = [16, 4, -9]
    y_list  = [1.943, 2.003240, 2.026]
    chi_list = [0, 0, 0]
    angles = [0.075, 0.1, 0.12, 0.15]
    angle_offset = [0, 0.025, 0.045, 0.075]
    samples = [ 'TD1_24h_200mM_1.0mgml_8.50', 'TiO2_Control_Berkeley', 'TiO2_control_HeatTreated_Berkeley']
    name_fmt = '{sample}_{angle}deg'
    
    x_last = -20.8
    y_last = 2.20
    chi_last = 0
    ang_last = -0.663
    sample_last = 'PDA_Heat_Treated_Berkeley'
    name_fmt_last = '{sample}_{angle}deg'
    
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'

    # Detectors, motors:
    dets = [pil1M,pil300KW,xbpm3.sumX]
    waxs_arc = [6, 18, 3]
    det_exposure_time(t)
    for x, y, a_off, chi, samp in zip(x_list, y_list, aligned_075, chi_list, samples):
        yield from bps.mv(stage.x, x)
        yield from bps.mv(sample.y, y)
        yield from bps.mv(stage.ch, chi)        
        for j, ang in enumerate((a_off - np.array(angle_offset))):
            yield from bps.mv(sample.al, ang)
            sample_name = name_fmt.format(sample=samp, angle=angles[j])
            print(f'\n\t=== Sample: {sample_name} ===\n')
            sample_id(user_name=name, sample_name=sample_name)
            yield from escan(dets, waxs.arc, *waxs_arc)
            yield from bps.mv(stage.x, x-0.2*(j+1))
    '''
    #last sample starts here      
    yield from bps.mv(sample.x, x_last)
    yield from bps.mv(sample.y, y_last)
    yield from bps.mv(stage.ch, chi_last)
    for j, ang in enumerate((ang_last - np.array(angle_offset))):
            yield from bps.mv(sample.al, ang)
            sample_name = name_fmt_last.format(sample=sample_last, angle=angles[j])
            sample_id(user_name=name, sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from escan(dets, waxs.arc, *waxs_arc)
            yield from bps.mv(sample.x, x_last-0.2*(j+1))
    '''
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)

def linkam_fast(n=6):
    yield from bps.mv(attn_shutter, 'Retract')
    yield from bp.scan([pil1M], stage.y, 0.1, 0.9, n)
    yield from bps.mv(attn_shutter, 'Insert')
    
    
   
    

Att_Align1 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-5}', name='Att_Align1')
Att_Align2 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-6}', name='Att_Align2')
Att_Align3 = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-7}', name='Att_Align3')
Att_Shutter = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-4}', name='Att_Shutter')
ROIsizey = "XF:12IDC-ES:2{Det:1M}ROI1:SizeY"
ROIMiny = "XF:12IDC-ES:2{Det:1M}ROI1:MinY"
ROIsizex = "XF:12IDC-ES:2{Det:1M}ROI1:SizeX"
ROIMinx = "XF:12IDC-ES:2{Det:1M}ROI1:MinX"


def alignmentmodeRPI():
        if Att_Align3.status.value=='Not Open':
               Att_Align1.set("Insert")
               time.sleep(1)
               Att_Align2.set("Insert")
               time.sleep(1)
               Att_Align3.set("Insert")
               time.sleep(1)
               pos = pil1m_bs.x.position
               pil1m_bs.x.move(pos+10)
        Att_Shutter.set("Retract")
        if waxs.arc.position < 12 :
                mov(waxs.arc,12)
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(1)

        
def measurementmodeRPI():
        if Att_Shutter.status.value=='Not Open':
                Att_Shutter.set("Insert")
                pos = pil1m_bs.x.position
                pil1m_bs.x.move(pos-10)
        time.sleep(1)
        Att_Align1.set("Retract")
        time.sleep(1)
        Att_Align2.set("Retract")
        time.sleep(1)
        Att_Align3.set("Retract")
        time.sleep(1)
        #mov(waxs.arc,3)

def snapRPI(t=1,dets=[pil1M,]):
        openedalready=0
        if Att_Shutter.status.value=='Not Open':
                openedalready = 1
        det_exposure_time(t)
        x = stage.x.position
        x_range  = [x, x, 1]
        yield from escan(dets, stage.x, *x_range)
        if openedalready==1:
                Att_Shutter.set("Retract")
        

def alignRPIgi():
        alignmentmodeRPI()
        align_gisax_RPI()
        
        
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


