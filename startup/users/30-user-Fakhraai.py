def run_giwaxs_Fak(t=1): 
    dets = [pil300KW, pil1M]
    xlocs1 = [-45000,-33000,-20000,-8000, 5000, 18000, 31000]
    names1 = ['Se_50nm', 'Se_100nm', 'Se_200nm', 'Se_300nm', 'Se_400nm', 'Se_1000nm', 'Se_2000nm']
        
    #what we run now
    curr_tray = xlocs1
    curr_names = names1
    assert len(curr_tray) == len(curr_names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    waxs_arc = [0, 78, 13]
    for x, name in zip(curr_tray, curr_names):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.th, 0)
        yield from alignement_gisaxs(0.15)
        plt.close('all')
        angle_offset = [0.18, 0.25]
        a_off = piezo.th.position
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{angle}deg'
        for j, ang in enumerate( a_off + np.array(angle_offset) ):
            yield from bps.mv(piezo.x, (x+j*500))
            real_ang = angle_offset[j]
            yield from bps.mv(piezo.th, ang)
            sample_name = name_fmt.format(sample=name, angle=np.float('%.3f'%real_ang))
            sample_id(user_name='AZ', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_arc)

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5,0.5)







def gFak(meas_t=1):
        names1 = 'aaA_P82_P75_SG_temp100C' #change file name!

        dets = [pil1M,pil300KW, rayonix]
        np_meas = 100
        angle_offset = 0.1
        timesleep = 0
        length = 16000
        x_edge = 9000 #middle part of gradient sample, non-greased side
        #make sure to define where the film stops using SmarAct middle row in notebook
        #Start the macro at the same time when you start heating
        #make sure to write down the temperature it starts heating and the time it arrives at the annealing temperature
        x_step = 4500
        nb_pt = (length - 500) // x_step
        xlocs1 = []
        for step in range(0, nb_pt+1, 1):
            xlocs1 += [np.round(x_edge - step * x_step)]

        t0 = time.time()
        #what we run now
        curr_tray = xlocs1
        curr_names = names1
        waxs_arc = [0, 19.5, 4]
        
        yield from alignement_gisaxs(0.1)
        a_off = piezo.th.position
        for m in range(0, np_meas,1):
            for i, x in enumerate(curr_tray):
                yield from bps.mv(piezo.x, x)
                # yield from bps.mv(piezo.th, a_off+angle_offset)
                yield from alignement_gisaxs(0.1) 
                a_off = piezo.th.position 
                # yield from quickalign_gisaxs(0.1)
                plt.close('all')
                yield from bps.mv(piezo.th, a_off+angle_offset)
                yield from quickalign_gisaxs(0.1)
                plt.close('all')
                yield from bps.mv(piezo.th, a_off+angle_offset) 
                det_exposure_time(meas_t,meas_t)
                temper = ls.ch1_read.value 
                name_fmt = '{sample}_x{xlocation}_{time}sec_{temper}C_{angl}deg'
                yield from bps.mv(piezo.x, x)
                t1 = time.time()-t0
                t1=np.round(t1)
                sample_name = name_fmt.format(sample=names1, xlocation=x, time=t1, temper = temper, angl = angle_offset)
                sample_id(user_name='AZ_18.2keV', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.scan(dets, waxs, *waxs_arc)
            time.sleep(timesleep)
                    
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3)  
        
        
        
 
def gFak1(meas_t=1):
        names1 = 'aaA_P82_P75_OG_RT'
        
        dets = [pil1M,pil300KW, rayonix]
        np_meas = 1
        angle_offset = [0.1, 0.2]
        timesleep = 0
        length = 6000
        x_edge = 0 #middle part of gradient sample, non-greased side
        #make sure to define where the film stops using SmarAct middle row in notebook
        #Start the macro at the same time when you start heating
        #make sure to write down the temperature it starts heating and the time it arrives at the annealing temperature
        x_step = 4500
        nb_pt = (length - 500) // x_step
        xlocs1 = []
        for step in range(0, nb_pt+1, 1):
            xlocs1 += [np.round(x_edge - step * x_step)]

        #what we run now
        curr_tray = xlocs1
        curr_names = names1
        waxs_arc = [0, 19.5, 4]
        yield from alignement_gisaxs(0.1)
        a_off = piezo.th.position
        for i, x in enumerate(curr_tray):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.th, a_off+ angle_offset[0])
            yield from quickalign_gisaxs(0.1)
            plt.close('all')
            a_off1 = piezo.th.position
            for i, an in enumerate(angle_offset):
                yield from bps.mv(piezo.th, a_off1+an)
                det_exposure_time(meas_t,meas_t)
                temper = ls.ch1_read.value
                name_fmt = '{sample}_x{xlocation}_{temper}C_{angl}deg'
                yield from bps.mv(piezo.x, x)
                sample_name = name_fmt.format(sample=names1, xlocation=x, temper = temper, angl = an)
                sample_id(user_name='AZ_18.2keV', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.scan(dets, waxs, *waxs_arc)
                
            
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3) 
  

