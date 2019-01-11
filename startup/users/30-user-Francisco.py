


            

        
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

    
    
    
    
    
#Aligam GiSAXS sample
#        
    
def align_gisaxs_height_Yale(  rang = 0.3, point = 31 ,der=False  ):     
        RE(bp.rel_scan([pil1M,pil1mroi1,pil1mroi2], piezo.y, -rang, rang, point ) )      
        ps(der=der)
        mov(piezo.y, ps.cen)

def align_gisaxs_th_Yale(  rang = 0.3, point = 31   ):             
        RE(bp.rel_scan([pil1M], piezo.th, -rang, rang, point ) )    
        ps()
        mov(piezo.th, ps.peak)
        
def align_gisaxs_height_Yale1(  rang = 0.3, point = 31 ,der=False  ):     
        yield from bp.rel_scan([pil1M,pil1mroi1,pil1mroi2], piezo.y, -rang, rang, point )
        ps(der=der)
        yield from bps.mv(piezo.y, ps.cen)

def align_gisaxs_th_Yale1(  rang = 0.3, point = 31   ):             
        yield from bp.rel_scan([pil1M], piezo.th, -rang, rang, point )
        ps()
        yield  from bps.mv(piezo.th, ps.peak)
            
    
    
    
Att_Align1 = att2_6 #att1_12
Att_Align2 = att2_11 #att1_9
GV7 = TwoButtonShutter('XF:12IDC-VA:2{Det:1M-GV:7}', name='GV7')
alignbspos = 11.3
measureBSpos = 1.3
ROIsizey = "XF:12IDC-ES:2{Det:1M}ROI1:SizeY"
ROIMiny = "XF:12IDC-ES:2{Det:1M}ROI1:MinY"
ROIsizex = "XF:12IDC-ES:2{Det:1M}ROI1:SizeX"
ROIMinx = "XF:12IDC-ES:2{Det:1M}ROI1:MinX"


def alignmentmodeYale():
        #Att_Align1.set("Insert")
        #time.sleep(1)
        yield from bps.mv(att1_3, 'Insert')
        time.sleep(1)
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from bps.mv(pil1m_bs.x, alignbspos)
        if waxs.arc.position < 12 :
                yield from bps.mv(waxs.arc,12)
        sample_id(user_name='test', sample_name='test')
        
def measurementmodeYale():
        yield from bps.mv(pil1m_bs.x,measureBSpos)
        time.sleep(1)
        #Att_Align1.set("Retract")
        #time.sleep(1)
        yield from bps.mv(att1_3, 'Retract')
        time.sleep(1)
        yield from bps.mv(GV7.close_cmd, 1 )
        time.sleep(1)
        #mov(waxs.arc,3)

def snapYale(t=1,dets=[pil1M,]):
        det_exposure_time(t)
        yield from bp.count(dets,num=1)

def ROI_yale():
        yield from bps.mv(att2_11, 'Insert')
        time.sleep(5)
        yield from bps.mv(att2_11, 'Retract')
        

def alignYalegi():
        det_exposure_time(0.5)
        sample_id(user_name='test', sample_name='test')
        yield from alignmentmodeYale()
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, 863)
        yield from bps.mv(pil1M.roi1.size.y, 100)
        yield from bps.mv(pil1M.roi1.size.x, 100)
        
        yield from align_gisaxs_height_Yale1(1000,16,der=True)
        yield from align_gisaxs_th_Yale1(1000,11)
        yield from align_gisaxs_height_Yale1(500,11,der=True)
        yield from align_gisaxs_th_Yale1(500,11)
        yield from bps.mv(piezo.th, ps.peak -100)
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, 778)
        yield from bps.mv(pil1M.roi1.size.y, 10)
        yield from align_gisaxs_th_Yale1(300,31)
        yield from align_gisaxs_height_Yale1(200,21)
        yield from align_gisaxs_th_Yale1(100,21)
        yield from bps.mv(piezo.th, ps.cen)
        yield from measurementmodeYale()
        
       
def do_grazing(meas_t=10):
        #xlocs = [48403]
        #names = ['BW30-CH-Br-1']
        # Detectors, motors:
        dets = [pil300KW, pil300kwroi2, xbpm3.sumY, xbpm2.sumY]
        xlocs = [ -9950,5050,20050,34250,49250]
        x_offset = [-0, -0, -0, -0, 0, 0, 0, 0, 0]
        names = ['ctrl1.5_hard','ctrl0.9_hard','ODT_hard','ZnO_hard','ITO_hard']
        prealigned = [0,0,0,0,0]
        for xloc, name, aligned in zip(xlocs, names, prealigned):
                yield from bps.mv(piezo.x,xloc)
                yield from bps.mv(piezo.th,-500)
                if aligned==0 :
                    yield from alignYalegi()
                    plt.close('all')
                angle_offset = [0, 100, 300]
                e_list  = [16100]
                a_off = piezo.th.position
                waxs_arc = [3, 33, 6]
                det_exposure_time(meas_t)
                name_fmt = '{sample}_{energ}eV_{angle}deg'
                offset_idx = 0
                #yield from bps.mv(att2_9, 'Insert')
                for i_e, e in enumerate(e_list):
                    yield from bps.mv(energy, e)
                    for j, ang in enumerate( a_off - np.array(angle_offset) ):
                        yield from bps.mv(piezo.x, xloc+x_offset[offset_idx])
                        offset_idx += 1
                        real_ang = 0.1 + angle_offset[j]/1000
                        yield from bps.mv(piezo.th, ang)
                        sample_name = name_fmt.format(sample=name, angle=real_ang, energ = e)
                        #print(param)        
                        sample_id(user_name='FA', sample_name=sample_name)
                        print(f'\n\t=== Sample: {sample_name} ===\n')
                        #print(RE.md)
                        yield from bp.scan(dets, waxs.arc, *waxs_arc)

                sample_id(user_name='test', sample_name='test')
                det_exposure_time(0.5)
                #yield from bps.mv(att2_9, 'Retract')

def do_grazing1(meas_t=2):
        #xlocs = [48403]
        #names = ['BW30-CH-Br-1']
        # Detectors, motors:
        dets = [pil300KW, pil300kwroi2, xbpm3.sumY, xbpm2.sumY]
        xlocs = [-37950]
        x_offset = [-200, 0, 200]
        names = ['ctrl1_focused_recheckoldmacro']
        prealigned = [0]
        for xloc, name, aligned in zip(xlocs, names, prealigned):
                yield from bps.mv(piezo.x,xloc)
                yield from bps.mv(piezo.th,-500)
                if aligned==0 :
                    yield from alignYalegi()
                    plt.close('all')
                angle_offset = [100, 220, 300]
                e_list  = [2460, 2477, 2500]
                a_off = piezo.th.position
                waxs_arc = [3, 87, 15]
                det_exposure_time(meas_t)
                name_fmt = '{sample}_{energ}eV_{angle}deg'
                for i_e, e in enumerate(e_list):
                    yield from bps.mv(energy, e)
                    yield from bps.mv(piezo.x, xloc+x_offset[i_e])
                    for j, ang in enumerate( a_off - np.array(angle_offset) ):
                        real_ang = 0.3 + angle_offset[j]/1000
                        yield from bps.mv(piezo.th, ang)
                        sample_name = name_fmt.format(sample=name, angle=real_ang, energ = e)
                        #print(param)        
                        sample_id(user_name='FA', sample_name=sample_name)
                        print(f'\n\t=== Sample: {sample_name} ===\n')
                        #print(RE.md)
                        yield from bp.scan(dets, waxs.arc, *waxs_arc)

                sample_id(user_name='test', sample_name='test')
                det_exposure_time(0.5)











               
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



