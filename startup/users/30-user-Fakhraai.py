
def gFak(meas_t=3):
        dets = [pil1M,pil300KW, rayonix, xbpm3.sumY]
        np_meas = 1
        timesleep = 0
        length = 56000
        x_edge = -19000 #middle part of gradient sample, non-greased side
        #make sure to define where the film stops using SmarAct middle row in notebook
        #Start the macro at the same time when you start heating
        #make sure to write down the temperature it starts heating and the time it arrives at the annealing temperature
        x_step = 4000
        nb_pt = (length - 500) // x_step
        xlocs1 = []
        for step in range(0, nb_pt+1, 1):
            xlocs1 += [np.round(x_edge + step * x_step)]
        #names1 = 'aaPhen_P82_D1_posttest'
        names1 = 'TNB_temp_gradient_20190301_RT'
        t0 = time.time()
        #what we run now
        curr_tray = xlocs1
        curr_names = names1
        waxs_arc = [2.83, 14.83, 3]
        yield from alignCai()
        for m in range(0, np_meas,1):
            for i, x in enumerate(curr_tray):
                yield from bps.mv(piezo.x, x)
                yield from alignfine()
                plt.close('all')
                angle_offset = [0.0]
                a_off = piezo.th.position
                det_exposure_time(meas_t) 
                name_fmt = '{sample}_x{xlocation}_{time}sec'
                yield from bps.mv(piezo.x, x)
                real_ang = 0.095                    
                t1 = time.time()-t0
                t1=np.round(t1)
                sample_name = name_fmt.format(sample=names1, xlocation=x, time=t1)
                sample_id(user_name='AZ_18.2keV', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.scan(dets, waxs.arc, *waxs_arc)
            time.sleep(timesleep)
                    
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5)  
  
def alignmentmodeCai():
        yield from SMIBeam().insertFoils(1)
        if waxs.arc.position < 8:
            yield from bps.mv(waxs.arc, 8)
        time.sleep(1)
        yield from bps.mv(pil1m_pos.x, -4)
        yield from bps.mv(pil1m_bs.x, alignbspos)
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5)
        
def measurementmodeCai():
        yield from bps.mv(pil1m_pos.x, -4)
        yield from bps.mv(pil1m_bs.x, measurebspos)
        time.sleep(1)
        yield from SMIBeam().insertFoils(0)
        time.sleep(1)
        
def align_gisaxs_height_Cai(  rang = 0.3, point = 31 ,der=False  ):     
        yield from bp.rel_scan([pil1M], piezo.y, -rang, rang, point )
        ps(der=der)
        yield from bps.mv(piezo.y, ps.cen)

def align_gisaxs_th_Cai(  rang = 0.3, point = 31   ):             
        yield from bp.rel_scan([pil1M], piezo.th, -rang, rang, point )
        ps()
        yield  from bps.mv(piezo.th, ps.peak)     
        
def align_gisaxsCai( ):     
      align_gisaxs_manualCai(  rang = 0.2, point = 31   )
      align_gisaxs_manualCai(  rang = 0.1, point = 21   )
      
def alignCai():
        det_exposure_time(0.5)
        sample_id(user_name='test', sample_name='test')
        yield from alignmentmodeCai()
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, 916)
        yield from align_gisaxs_height_Cai(700, 16, der=True)
        yield from align_gisaxs_th_Cai(1, 11)
        yield from align_gisaxs_height_Cai(300, 11, der=True)
        yield from align_gisaxs_th_Cai(0.5, 16)
        yield from bps.mv(piezo.th, ps.peak + 0.08)
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, 916-160)
        yield from align_gisaxs_th_Cai(0.3, 31)
        yield from align_gisaxs_height_Cai(200, 21)
        yield from align_gisaxs_th_Cai(0.1, 21)
        yield from bps.mv(piezo.th, ps.cen)
        yield from measurementmodeCai()

def alignfine():
        det_exposure_time(0.5)
        sample_id(user_name='test', sample_name='test')
        yield from alignmentmodeCai()
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, 916-160)
        yield from align_gisaxs_th_Cai(0.25, 31)
        yield from align_gisaxs_height_Cai(220, 25)
        yield from align_gisaxs_th_Cai(0.1, 21)
        yield from bps.mv(piezo.th, ps.cen)
        yield from measurementmodeCai()

