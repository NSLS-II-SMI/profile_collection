#Align GiSAXS sample
import numpy as np
        
#============================ SMI GI Alignment ===============================#
alignbspos = 11
measurebspos = 1.15
GV7 = TwoButtonShutter('XF:12IDC-VA:2{Det:1M-GV:7}', name='GV7')
  
def alignmentmodeBoc():
    ''' Move gate valves, attenutators, and beamtop into GI alignment mode'''
    yield from bps.mv(waxs.arc,10) #move the waxs detector out of the way
    yield from bps.mv(GV7.open_cmd, 1 ) #open the SAXS gate valve
    yield from bps.mv(att2_6,"Retract") #make sure that atten2_6 is out
    # yield from bps.mv(att2_8,"Insert")  # (for 7.5keV) make sure that atten2_8 is out
    yield from SMIBeam().insertFoils(1)   # (for >11keV in vac) 1 = insert
    time.sleep(1)
    
    # if bragg.position<8: 
    #     yield from bps.mv(att1_5,"Insert")  
    #     time.sleep(1)
    #     yield from bps.mv(att1_7,"Insert") 
    #     # yield from SMIBeam().insertFoils(1)   # (for >11keV in vac) 1 = insert
    #     time.sleep(1)
    # elif bragg.position>8 and bragg.position<9:
    # #for 13.5 keV
    #     yield from bps.mv(att1_12,"Insert")
    #     time.sleep(1)
    yield from bps.mv(pil1m_bs.x, alignbspos) #move beamstop out of the way
    sample_id(user_name='test', sample_name='test') #don't overwrite user data
    det_exposure_time(0.5)
        
def measurementmodeBoc():
    ''' Move gate valves, attenutators, and beamtop into GI measurement mode'''
    # yield from bps.mv(att2_8,"Retract") # (for 7.5keV) 
    yield from SMIBeam().insertFoils(0)   # (for >11keV)
    yield from bps.mv(pil1m_bs.x, measurebspos)
    time.sleep(1)
    #uncomment to close SAXS gate valve during measurements
    yield from bps.mv(GV7.close_cmd, 1 ) 
    time.sleep(1)
        
def align_gisaxs_height_Boc(  rang = 0.3, point = 31 ,der=False  ):     
    yield from bp.rel_scan([pil1M], piezo.y, -rang, rang, point )
    ps(der=der)
    yield from bps.mv(piezo.y, ps.cen)

def align_gisaxs_th_Boc(  rang = 0.3, point = 31   ):             
    yield from bp.rel_scan([pil1M], piezo.th, -rang, rang, point )
    ps()
    yield  from bps.mv(piezo.th, ps.peak)     
      
def alignBoc(align_height=5000):
        '''Do GI alignment '''
        det_exposure_time(0.5)
        sample_id(user_name='test', sample_name='test')
        yield from alignmentmodeBoc()
        yield from bps.mv(piezo.y,align_height)
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, 883)
        yield from align_gisaxs_height_Boc(600, 16, der=True)
        yield from align_gisaxs_th_Boc(1, 11)
        yield from align_gisaxs_height_Boc(300, 11, der=True)
        yield from align_gisaxs_th_Boc(0.5, 11)
        yield from bps.mv(piezo.th, ps.peak + 0.2)
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, 883-336) # 336 offset = 0.4*3.14/180*8287/0.172
        yield from align_gisaxs_th_Boc(0.3, 31)
        yield from align_gisaxs_height_Boc(200, 21)
        yield from align_gisaxs_th_Boc(0.1, 21)
        yield from bps.mv(piezo.th, ps.cen)
        yield from measurementmodeBoc()

def alignBocBulk(align_height=5000):
        ''' Do GI alignment, but skip reflectivity step '''
        det_exposure_time(0.5)
        sample_id(user_name='test', sample_name='test')
        yield from alignmentmodeBoc()
        yield from bps.mv(piezo.y,align_height)
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, 883)
        yield from align_gisaxs_height_Boc(600, 16, der=True)
        yield from align_gisaxs_th_Boc(1, 11)
        yield from align_gisaxs_height_Boc(300, 11, der=True)
        yield from align_gisaxs_th_Boc(0.5, 11)
        yield from bps.mv(piezo.th, ps.peak)
        yield from measurementmodeBoc()


#============================ Custom Run Routines ===============================#

def run_giwaxsBocBoth(): 
    thresh_map = {}
    thresh_map[13400] = 10
    thresh_map[13473] = 10
    thresh_map[13550] = 10
    thresh_map[15125] = 11
    thresh_map[15199] = 11
    thresh_map[15275] = 11

    for e in [13400,13473,13550,15125,15199,15275]:
        yield from bps.mv(energy,e)
        #caput('XF:12IDC-ES:2{Det:300KW}cam1:ThresholdEnergy',thresh_map[e])
        #caput('XF:12IDC-ES:2{Det:300KW}cam1:ThresholdApply',1)
        yield from run_giwaxsBoc(t=1.0,tag=f'{e:5d}keV_air')
        #yield from run_giwaxsBocBulk(t=0.5,tag=f'{e:5d}keV_air')

def run_giwaxsBoc(t=0.5,th_step=0.001,x_list_offset=0,tag=''): 
    ''' GIWAXS Run Routine 
    
    Runs a scan along a sample bar allowing for custom waxs_arc and theta_scan
    definitions. Also allows for 'walking' on the sample during measurement to
    avoid beam damage.

    '''
    name = 'PB'
    
    # define x-positions on sample bar
    # x_list = [52000,44000,38000,30000,23000,18000,12000,6000,-2000,-12000,-23000,-35000,-44000,-51000] # GI bar 1 - Lee samples
    # x_list = [-5500,-12500,-19500,-26500,-33500] # GI bar 2 - Peter membrane dry samples
    # x_list = [49000,-5500,-13000,-20000,-27000,-33000] # GI bar 3 - Lee low priority and Nils samples
    # x_list = [40000,14000,-12000,-39000]
    # x_list = [49000,33500,23000,11500,300,-6200]
    x_list = [47500,33500,23000,9500]

    # define names of samples on sample bar
    # sample_list = ['BTBT_noAu','BTBT_noPFBT','BTBT_PFBT','BTBT_Au','NEP25_1','NEP25_2','NEP50_4','NEP50_3','DIF_noAu','DIF_Au','DIF_noPFBT','DIF_PFBT','NEP75_6','NEP100_8'] # GI bar 1 - Lee samples
    # sample_list = ['SWC4iTS_dry_7500','Dow6iTS_dry_7500','Dow7iTS_dry_7500','Dow8iTS_dry_7500', 'Dow10iTS_dry_7500'] # GI bar 2 - Peter membrane dry samples
    # sample_list = ['','','','','','','','','',''] # GI bar 2 - Peter membrane dry samples
    # sample_list = ['mLbL_dry_7500', 'SWC4iTS_dry_7500', 'Dow6iTS_dry_7500', 'Dow7iTS_dry_7500', 'Dow8iTS_dry_7500', 'Dow10iTS_dry_7500'] # GI bar 2 - Peter membrane dry samples
    # sample_list = ['SWC4iTS_dry_7500', 'Dow6iTS_dry_7500', 'Dow7iTS_dry_7500', 'Dow8iTS_dry_7500', 'Dow10iTS_dry_7500'] # GI bar 2 - Peter membrane dry samples
    # sample_list = ['Dow8-wet-100mMRbBr','Dow7-wet-100mMRbBr','Dow6-wet-100mMRbBr','mLbL-wet-100mMRbBr']
    # sample_list = ['DIF_noOx','DIF_Ox','BTBT_noOx','BTBT_Ox','NEP_75_5','NEP_100_7']
    sample_list = ['DIF_noOx','DIF_Ox','BTBT_noOx','BTBT_Ox']

    #x_list = x_list[::-1]
    #sample_list = sample_list[::-1]

    # shift xlist
    x_list = [x+x_list_offset for x in x_list]

    #sanity check
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'

    # Set up theta and waxs scans
    ## for Nils/Lee VAOI studies
    th_array = np.arange(0.08,0.280,th_step) 
    waxs_arc = [2.83, 20.83, 4] 
    # ## for non VAOI studies
    # th_array  = np.array([0.0, 0.15])
    # waxs_arc = [2.83, 2.83, 1] 

    #sanity check
    waxs_step = (waxs_arc[1] - waxs_arc[0])/(waxs_arc[2]-1)
    assert waxs_step<=6.00001,f'waxs arc step<6 for proper stitching: waxs_step = {waxs_step}'

    #need to walk around sample to avoid beam_damage
    glob_xoff = 2000 
    glob_walk_length = 2000 #microns
    glob_xstep = int(glob_walk_length/th_array.shape[0])

    dets = [pil300KW,rayonix] 
    for x,sample in zip(x_list,sample_list): #loop over samples on bar
        yield from bps.mv(piezo.x, x) #move to next sample
        yield from bps.mv(piezo.th,0.05) #set stage angle to ~0
        yield from alignBoc(6000) #run alignment routine 
        plt.close('all') #close pesky alignment plots (memory issues)

        th_start = piezo.th.position
        det_exposure_time(t) 
        for j, th in enumerate(th_start + th_array): #loop over incident angles
            #uncomment to walk around sample to avoid beam_damage
            yield from bps.mv(piezo.x, (x-glob_xoff+j*glob_xstep))

            # convert angles to "real" angles
            real_th = 0.2 + th_array[j] #0.2 = critical angle / alignment angle for Si
            yield from bps.mv(piezo.th, th)

            sample_name = sample +  '_{th:5.4f}deg'.format(th=real_th)
            if tag:
                sample_name += ('_' + tag)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.scan(dets, waxs.arc, *waxs_arc)

            #uncomment below for manual snake mode.
            waxs_arc[1],waxs_arc[0] = waxs_arc[0],waxs_arc[1]

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)

def run_giwaxsBocBulk(t=1,tag=''): 
    name = 'PB'
    # x_list = [] # GI bar 1 - Lee samples
    # x_list = [50000,38000,30000,23500,11500,2500,-5500,-12500,-19500,-26500,-33500] # GI bar 2 - Peter membrane dry samples
    # x_list = [11500,2500] # GI bar 2 - Peter membrane dry samples
    # x_list = [] # GI bar 3 - Lee low priority and Nils samples
    x_list = [38000,30000,23500,11500,2500] # GI bar 2 - Peter membrane dry samples
    

    # sample_list = ['BTBT_noAu','BTBT_noPFBT','BTBT_PFBT','BTBT_Au','BTBT_NoOx','BTBT_Ox','DIF_noAu','DIF_Au','DIF_noPFBT','DIF_PFBT'] # GI bar 1 - Lee samples
    # sample_list = ['mLbL_dry_7500','Dow6bulk_dry_7500','Dow7bulk_dry_7500',
    #               'Dow8bulk_dry_7500','Dow10bulk_dry_7500','SWC4bulk_dry_7500','SWC4iTS_dry_7500',
    #               'Dow6iTS_dry_7500','Dow7iTS_dry_7500','Dow8iTS_dry_7500', 'Dow10iTS_dry_7500'] # GI bar 2 - Peter membrane dry samples
    # sample_list = ['Dow10bulk_dry_7500','SWC4bulk_dry_7500'] # GI bar 2 - Peter membrane dry samples
    sample_list = ['Dow6bulk_dry_7500','Dow7bulk_dry_7500','Dow8bulk_dry_7500','Dow10bulk_dry_7500','SWC4bulk_dry_7500'] # GI bar 2 - Peter membrane dry samples


    # th_list = np.arange(0.08,0.280,0.0005) # for Nils/Lee VAOI studies
    th_array  = np.array([0.0, 0.15])
    waxs_arc = [2.83, 2.83, 1] 

    #sanity check
    #waxs_step = (waxs_arc[1] - waxs_arc[0])/waxs_arc[2]
    #assert waxs_step<=6.00001,f'waxs arc step<6 for proper stitching: waxs_step = {waxs_step}'

    #need to walk around sample to avoid beam_damage
    glob_xoff = 1000 
    glob_xstep = 200

    dets = [pil300KW,rayonix] 
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'
    for x,sample in zip(x_list,sample_list): #loop over samples on bar
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.th,0.05)
        yield from alignBocBulk()   
        plt.close('all')
        # yield from bps.mv(att2_6,"Insert") # add in attenutator to avoid saturation 

        th_start = piezo.th.position
        det_exposure_time(t) 
        for j, th in enumerate(th_start + th_array):
            #uncomment to walk around sample to avoid beam_damage
            # yield from bps.mv(piezo.x, (x-glob_xoff+j*glob_xstep))

            # convert angles??
            real_th = 0.2 + th_array[j] #from critical angle / alignment angle for Si
            yield from bps.mv(piezo.th, th)

            sample_name = sample +  '_{th}deg'.format(th=real_th)
            if tag:
                sample_name += ('_' + tag)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.scan(dets, waxs.arc, *waxs_arc)

            #uncomment below for manual snake mode.
            waxs_arc[1],waxs_arc[0] = waxs_arc[0],waxs_arc[1]

        # yield from bps.mv(att2_6,"Retract")
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)

def run_giwaxsEnergyBoc(t=1,tag=''): 
    ''' GIWAXS Run Routine '''
    name = 'PB'
    
    # define x-positions on sample bar
    # x_list = [40000,14000,-12000,-39000]
    # x_list = [-12000,-39000]
    # x_list = [55000,5000,-25000,-46500,-51500]
    # x_list = [-44500,-14500,14000,41000]
    x_list = [-28000, 8000]

    # define names of samples on sample bar
    # sample_list = ['Dow8-wet-100mMRbBr','Dow7-wet-100mMRbBr','Dow6-wet-100mMRbBr','mLbL-wet-100mMRbBr']
    # sample_list = ['Dow6-wet-100mMRbBr','mLbL-wet-100mMRbBr']
    # sample_list = ['Dow10bulk-wet-100mMRbBr','Dow6bulk-wet-100mMRbBr','Dow10-wet-100mMRbBr','SWC4-wet-100mMRbBr','emptycell-wet-100mMRbBr']
    #sample_list = ['SWC4-wet-100mMRbBr','emptycell-wet-100mMRbBr']
    # sample_list = ['mLbL-wet-DIwater','mLbL-wet-100mMNaCl','mLbL-wet-100mMNaBr','mLbL-wet-100mMRbCl']
    sample_list = ['mLbL-wet-50mMRbBr','mLbL-wet-500mMRbBr']
    


    #sanity check
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'

    # # Set up theta and waxs scans
    th_array = np.array([0.0, 0.025, 0.05, 0.15])
    energy_arc = [13400,13473,13550,15125,15199,15275]

    dets = [pil300KW,rayonix] 
    for x,sample in zip(x_list,sample_list): #loop over samples on bar
        yield from bps.mv(piezo.x, x) #move to next sample
        yield from bps.mv(piezo.th,0.05) #set stage angle to ~0
        if 'bulk' in sample:
            yield from alignBocBulk(4500) #run alignment routine    
        else:
            yield from alignBoc(5200) #run alignment routine 
        plt.close('all') #close pesky alignment plots (memory issues)

        yield from bps.mv(waxs.arc,2.83) #move the waxs dectector to the measurement position

        th_start = piezo.th.position
        det_exposure_time(t) 
        for j, th in enumerate(th_start + th_array): #loop over incident angles
            # convert angles to "real" angles
            real_th = 0.2 + th_array[j] #0.2 = critical angle / alignment angle for Si
            yield from bps.mv(piezo.th, th)

            for k,e in enumerate(energy_arc):

                sample_name = sample +  '_{th:5.4f}deg_{e:5d}eV'.format(th=real_th,e=e)
                if tag:
                    sample_name += ('_' + tag)
                sample_id(user_name=name, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')
                energy.move(e)
                yield from bps.mv(energy,e)
                
                sleep(1)
                yield from bp.scan(dets, energy, e, e, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)

def run_saxsBoc(t=1): 
    '''Simple SAXS/WAXS transmission measurements

    Runs a scan along a transmission bar where, for each sample center in the
    x_list, measurements are taken in a grid defined by x_range and y_range
    about this center.
    
    '''
    name = 'PB'
    # x_list  = [43200,32700,22200,11500,1000,-9400,-19400,-27900,-37400] #tray 1
    #x_list  = [32700,22200,11500] #tray 1
    # x_list  = [44000,34000,24000,14500,5000,-5500,-15000,-25500,-33000,-43000] #tray 2
    # x_list  = [42000,33000,25000,17000,10000,1000,-8500,-18000,-24000,-32000,-42000] #tray T3
    # x_list  = [45000,32200,26000,18500,11000,2500,-6500,-15000,-22500,-31500,-42000] #tray T5
    # x_list  = [45000,35500,28000,18000,10500,2000,-8000,-16500,-24000,-31000,-41000] #tray T4
    # x_list  = [44000,35000,27500,18000,9500,1500,-7000,-14500,-23000,-31000,-40500] #tray T6
    x_list  = [31000,20500 ,7500,-4000,-13500,-22000,-32000,-42500] #tray T7 - do these positions make sense?

    # samples = ['AS1_020E','AS1-001','AS1-008','AS1-003','AS1-004Y','AS1-002','AS1-004W','AS1-009','AS1-006','AS1-010','AS1-006c'] #tray T3
    #samples = ['AS1-010C','AS1-011C','AS1-012Ac','AS1-012Bc','AS1-0012Cc','AS1-012Dc','AS1-012Ec','PT5E-007A','PT5E-007B','PT5E-007C','PT5E-007D'] #tray T5
    # samples = ['PT5E-007E','PT5E-007F','PT5E-007G','PT5E-007H','PT5E-007I','PT5E-007J','PT5E-007K','PT5E-007L','PT5E-007M','PT5E-007N','PT7E-001A'] #tray T4
    # samples = ['PT7E-001B','PT7E-001C','PT7E-003A','PT7E-003B','PT7E-003C','PT7E-003D','PT7E-003E','PT7E-003F','PT7E-003G','PT2E-015A','PT2E-015B'] #tray T6
    samples = ['PT2E-015C','PT2E-015D','PT2E-015E','PT2E-017A','PT2E-017B','PT2E-017C','PT2E-017D','PT2E-017E'] #tray T7
    
    # Detectors, motors:
    dets = [pil1M,pil300KW] # dets = [pil1M,pil300KW]
    x_range = [-500,500,11]
    y_range = [-250,250,11]

    #samples = ['PTB1-015','WTI-025I','WTI-025II','PTTE-006','PT2E-011A','PT2E-011B','PT2E-011C','PT2E-011D','PT2E-011E'] #samples 1
    #samples = ['WTI-025I-7500','WTI-025II-7500','PTTE-006-7500'] #samples 1 / lo-q
    # samples = ['AS1-020Ac','AS1-020Bc','AS1-020Cc','AS1-020Dc','AS1-020Ec','SAH','AS1-020A','AS1-020B','AS1-020C','AS1-020D'] #samples 2
    #samples = ['cap-H2Oblank','SWC4sol-RbBr20mM','SWC4sol-RbCl20mM','SWC4sol-NaBr20mM','SWC4sol-NaCl20mM','SWC4sol-RbBr100mM','SWC4sol-RbCl100mM','SWC4sol-NaBr100mM','SWC4sol-NaCl100mM','SWC4-THF','SWC4-H2OEXCH','blank-RbBr100mM','blank-RbCl100mM','blank-NaBr100mM','blank-NaCl100mM']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    yield from bps.mv(piezo.y, 0)
    yield from bps.mv(piezo.th, 0)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(piezo.x, x)
        sample_id(user_name=name, sample_name=sample) 
        # yield from bp.scan(dets, piezo.x, *x_range)  # 1 line scane 
        yield from bp.rel_grid_scan(dets, piezo.x, *x_range, piezo.y, *y_range,1) #1 = snake, 0 = not-snake
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 

def run_saxsEnergyBoc(t=1,tag=''): 
    '''Simple SAXS/WAXS transmission measurements

    Runs a scan along a transmission bar where, for each sample center in the
    x_list, measurements are taken in a grid defined by x_range and y_range
    about this center.
    
    '''
    name = 'PB'
    x_list  = [-44000,-37500,-31500,-25000,-18500,-12000,-5500,1000,7000,13000,19500,26000,32500,39000,45500] #tray 1
    # x_list  = [13000,19500,26000,32500,39000,45500] #tray 1
    samples = ['cap-H2Oblank','SWC4sol-RbBr20mM','SWC4sol-RbCl20mM','SWC4sol-NaBr20mM','SWC4sol-NaCl20mM','SWC4sol-RbBr100mM','SWC4sol-RbCl100mM','SWC4sol-NaBr100mM','SWC4sol-NaCl100mM','SWC4-THF','SWC4-H2OEXCH','blank-RbBr100mM','blank-RbCl100mM','blank-NaBr100mM','blank-NaCl100mM']
    # samples = ['SWC4-THF','SWC4-H2OEXCH','blank-RbBr100mM','blank-RbCl100mM','blank-NaBr100mM','blank-NaCl100mM']

    # Detectors, motors:
    dets = [pil300KW]
    x_range = [-500,500,11]
    energy_arc = [13400,13473,13550,15125,15199,15275]


    #sanity check
    assert len(x_list) == len(samples), f'Sample name/position list is borked'

    det_exposure_time(t)
    yield from bps.mv(piezo.y, 8000) #8000 for capillaries 
    yield from bps.mv(piezo.th, 0)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(piezo.x, x)
        
        for k,e in enumerate(energy_arc):

            sample_name = sample +  '_{e:5d}eV'.format(e=e)
            if tag:
                sample_name += ('_' + tag)
            sample_id(user_name=name, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            energy.move(e)
            yield from bps.mv(energy,e)
            sleep(1)

            yield from bp.rel_scan(dets, piezo.x, *x_range)  # 1 line scan
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 

  
   
ROIsizey = "XF:12IDC-ES:2{Det:1M}ROI1:SizeY"
ROIMiny = "XF:12IDC-ES:2{Det:1M}ROI1:MinY"
ROIsizex = "XF:12IDC-ES:2{Det:1M}ROI1:SizeX"
ROIMinx = "XF:12IDC-ES:2{Det:1M}ROI1:MinX"



