# command for running the code
# %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Cai.py 
# RE(run_giwaxs_cai(2))

                        
def run_giwaxs_cai(t=1): 
    dets = [pil300KW, pil1M, rayonix]
    xlocs1 = [-40000,-29000,-17000,-5000, 6000, 20000, 31000, 42000]
    xlocs2 = [-42000,-29500,-16000,-5000, 6000, 19500, 30000, 42000]
    xlocs3 = [-43000,-33000,-19000,-5000, 7500, 22500, 31500, 45000]
    xlocs4 = [-42000,-29500,-16000,-5000, 7000, 19500, 31000, 44400]
    xlocs5 = [-43000,-29500,-19200,-5000, 6200, 17400, 31500, 43800]
    xlocs6 = [-42000,-26500,-16000,-6300, 6000, 21000, 29500, 44000]
    xlocs7 = [-44500,-33500,-22000,-9000, 4000, 15500, 34000, 47400]
    xlocs8 = [-43600,-27100,-17500,-7600, 7800, 19200, 29500, 41800]
    xlocs9 = [-44300,-34300,-25800,-15800, -800, 7000, 17000, 28200, 38200, 48200]
    
    
    names1 = ['BBdot8k_500k_PBMA_2x21k_40mgmL', 'BBdot8k_500k_PBMA_2x21k_20mgmL', 'BBdot8k_500k_PBMA_2x21k_10mgmL', 'BBdot8k_500k_PBMA_2x21k_5mgmL', 'BB1k_500k_PBMA_2x31k_40mgmL', 'BB1k_500k_PBMA_2x31k_20mgmL', 'BB1k_500k_PBMA_2x31k_10mgmL', 'BB1k_500k_PBMA_2x31k_5mgmL']
    names2 = ['BB1k_500k_PBMA_2x47k_40mgmL', 'BB1k_500k_PBMA_2x47k_20mgmL', 'BB1k_500k_PBMA_2x47k_10mgmL', 'BB1k_500k_PBMA_2x47k_5mgmL', 'BB5k_500k_PBMA_2x21k_40mgmL', 'BB5k_500k_PBMA_2x21k_20mgmL', 'BB5k_500k_PBMA_2x21k_10mgmL', 'BB5k_500k_PBMA_2x21k_5mgmL']
    names3 = ['BB5k_500k_PBMA_2x50k_40mgmL', 'BB5k_500k_PBMA_2x50k_20mgmL', 'BB5k_500k_PBMA_2x50k_10mgmL', 'BB5k_500k_PBMA_2x50k_5mgmL', 'BB5k_1M_PBMA_2x10k_40mgmL', 'BB5k_1M_PBMA_2x10k_20mgmL', 'BB5k_1M_PBMA_2x10k_10mgmL', 'BB5k_1M_PBMA_2x10k_5mgmL']
    names4 = ['BB10k_500k_PS_2x2k_40mgmL', 'BB10k_500k_PS_2x2k_20mgmL', 'BB10k_500k_PS_2x2k_10mgmL', 'BB10k_500k_PS_2x2k_5mgmL', 'BB1k_500k_r_PBMA_64k_PBMA_2x16k_40mgmL', 'BB1k_500k_r_PBMA_64k_PBMA_2x16k_20mgmL', 'BB1k_500k_r_PBMA_64k_PBMA_2x16k_10mgmL', 'BB1k_500k_r_PBMA_64k_PBMA_2x16k_5mgmL']
    names5 = ['BB5k_1M_r_PBMA_46k_PBMA_2x10k_40mgmL', 'BB5k_1M_r_PBMA_46k_PBMA_2x10k_20mgmL', 'BB5k_1M_r_PBMA_46k_PBMA_2x10k_10mgmL', 'BB5k_1M_r_PBMA_46k_PBMA_2x10k_5mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_40mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_20mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_10mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_5mgmL']
    names6 = ['PHMA_51k_PS_2x5100_40mgmL', 'PHMA_51k_PS_2x5100_20mgmL', 'PHMA_51k_PS_2x5100_10mgmL', 'PHMA_51k_PS_2x5100_5mgmL', 'PHMA_51k_PS_2x3300_40mgmL', 'PHMA_51k_PS_2x3300_20mgmL', 'PHMA_51k_PS_2x3300_10mgmL', 'PHMA_51k_PS_2x3300_5mgmL']
    names7 = ['PHMA_51k_PS_2x1100_40mgmL', 'PHMA_51k_PS_2x1100_20mgmL', 'PHMA_51k_PS_2x1100_10mgmL', 'PHMA_51k_PS_2x1100_5mgmL', 'PAAPAHA_40k_PS_2x1800_40mgmL', 'PAAPAHA_40k_PS_2x1800_20mgmL', 'PAAPAHA_40k_PS_2x1800_10mgmL', 'PAAPAHA_40k_PS_2x1800_5mgmL']
    names8 = ['BB5k_1M_r_PBMA_46k_PBMA_2x10k_40mgmL_2', 'BB5k_1M_r_PBMA_46k_PBMA_2x10k_20mgmL_2', 'BB5k_1M_r_PBMA_46k_PBMA_2x10k_10mgmL_2', 'BB5k_1M_r_PBMA_46k_PBMA_2x10k_5mgmL_2', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_40mgmL_2', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_20mgmL_2', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_10mgmL_2', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_5mgmL_2']
    names9 = ['BB5k_500k_PBMA_2x21k_40mgmL_2', 'BB5k_500k_PBMA_2x21k_20mgmL_2', 'BB5k_500k_PBMA_2x21k_10mgmL_2', 'BB5k_1M_PBMA_2x10k_40mgmL_2', 'BB5k_1M_PBMA_2x10k_20mgmL_2', 'BB5k_1M_PBMA_2x10k_10mgmL_2', 'BB10k_500k_PS_2x5k_40mgmL_2', 'BB10k_500k_PS_2x5k_20mgmL_2', 'BB10k_500k_PS_2x5k_10mgmL_2', 'PAAPAHA_40k_PS_2x1800_5mgmL_2']
    
    
        
    #what we run now
    curr_tray = xlocs9
    curr_names = names9
    assert len(curr_tray) == len(curr_names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    waxs_arc = [0, 19.5, 4]
    for x, name in zip(curr_tray, curr_names):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.th, 0)
        yield from bps.mv(pil1m_pos.x, -2.3)
        #time.sleep(2)
        yield from alignement_gisaxs(0.1)
        yield from bps.mv(pil1m_pos.x, 0.7)
        #time.sleep(2)
        plt.close('all')
        angle_offset = [0.125, 0.2]
        a_off = piezo.th.position
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{angle}deg'
        for j, ang in enumerate( a_off + np.array(angle_offset) ):
            yield from bps.mv(piezo.x, (x+j*400))
            real_ang = angle_offset[j]
            yield from bps.mv(piezo.th, ang)
            sample_name = name_fmt.format(sample=name, angle=np.float('%.3f'%real_ang))
            sample_id(user_name='LC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_arc)

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3)


def run_giwaxs_cai_temp(t=2): 
    dets = [pil300KW, pil1M, rayonix]
    xlocs1 = [-7500,6300]
   
    names1 = ['PHMA_51k_PS_2x3300_20mgmL_T_cool', 'PAAPAHA_40k_PS_2x1800_20mgmL_T_cool']
   
        
    #what we run now
    curr_tray = xlocs1
    curr_names = names1
    assert len(curr_tray) == len(curr_names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    waxs_arc = [0, 19.5, 4]
    for x, name in zip(curr_tray, curr_names):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.th, 0)
        yield from bps.mv(pil1m_pos.x, -2.3)
        #time.sleep(2)
        yield from alignement_gisaxs_shorter(0.1)
        yield from bps.mv(pil1m_pos.x, 0.7)
        #time.sleep(2)
        plt.close('all')
        angle_offset = [0.125, 0.2]
        a_off = piezo.th.position
        det_exposure_time(t,t)
        temper = ls.ch1_read.value  
        name_fmt = '{sample}_{temper}C_{angle}deg'
        for j, ang in enumerate( a_off + np.array(angle_offset) ):
            yield from bps.mv(piezo.x, (x+j*200))
            real_ang = angle_offset[j]
            yield from bps.mv(piezo.th, ang)
            sample_name = name_fmt.format(sample=name, temper = temper, angle=np.float('%.3f'%real_ang))
            sample_id(user_name='LC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_arc)

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3)






def gisaxsCaiTempOLD(meas_t=1):
        temperatures = [190]
        waxs_arc = [8, 8, 1]
        dets = [pil1M, pil300KW, xbpm3.sumY]
       # glob_xoff = 1000
        xlocs1 = [-39000, -28000, -18000, -7000, 2000, 13000, 24000, 35000, 46000]
        xlocs2 = [-44000, -33000, -22000, -11000, 0, 11000, 22000, 33000, 44000]
        xlocs3 = [-44500, -33000, -22000, -11000, 0, 11000, 22000, 33000, 43800]
        xlocs4 = [-44000, -33000, -23000, -10000, 0, 11000, 22000, 33000, 44000]
        xlocs5 = [-44000, -33000, -24000, -11000, 0, 11000, 22000, 32000, 43000]
        xlocs6 = [-43000, -34000, -22000, -10000, 1000, 10500, 22000]
        
        xlocsT = [50500, 40500, 28500, 18500, 7500, -2500, -17500, -27500, -37500, -47500 ]
       
        names1 = ['M11_500kDa_100mgmL','M11_500kDa_50mgmL','M11_500kDa_25mgmL','M11_500kDa_12mgmL','M11_500kDa_6mgmL','M11_500kDa_3mgmL','M11_500kDa_1.6mgmL','M11_1MDa_80mgmL','M11_1MDa_40mgmL']
        names2 = ['M11_1MDa_20mgmL','M11_1MDa_10mgmL','M11_1MDa_5mgmL','M11_1MDa_2.5mgmL','M11_1MDa_1.25mgmL','M11_1MDa_0.6mgmL','M17_500kDa_100mgmL','M17_500kDa_50mgmL','M17_500kDa_25mgmL']
        names3 = ['M17_500kDa_12.5mgmL','M17_500kDa_6.25mgmL','M17_500kDa_3.1mgmL','M17_500kDa_1.6mgmL','M22_500kDa_40mgmL','M22_500kDa_20mgmL','M22_500kDa_10mgmL','M22_1MDa_5mgmL','M22_1MDa_2.5mgmL']
        names4 = ['M22_500kDa_1.25mgmL_new','M22_500kDa_0.6mgmL','M07_1MDa_80mgmL','M07_1MDa_40mgmL','M07_1MDa_20mgmL','M07_1MDa_10mgmL','M07_1MDa_5mgmL','M07_1MDa_2.5mgmL','M07_1MDa_1.25mgmL']
        names5 = ['M07_1MDa_0.6mgmL','M11_500kDa_NoA_100mgmL','M11_500kDa_NoA_50mgmL','M11_500kDa_NoA_25mgmL','M11_500kDa_NoA_12.5mgmL','M11_500kDa_NoA_6.25mgmL',
                  'M11_500kDa_NoA_3.1mgmL','M11_500kDa_NoA_1.6mgmL','M11_1MDa_NoA_80mgmL']
        names6 = ['M11_1MDa_NoA_40mgmL','M11_1MDa_NoA_20mgmL','M11_1MDa_NoA_10mgmL','M11_1MDa_NoA_5mgmL','M11_1MDa_NoA_2.5mgmL','M11_1MDa_NoA_1.25mgmL','M11_1MDa_NoA_0.6mgmL']
        
        namesT = ['M11_500kDa_1.6mgmL_8', 'M11_1MDa_1.25mgmL_8', 'M11_1MDa_0.6mgmL_8', 'M17_500kDa_1.6mgmL_8', 'M22_500kDa_1.25mgmL_8', 'M22_500kDa_0.6mgmL_8', 'M07_1MDa_1.25mgmL_8', 'M07_1MDa_0.6mgmL_8', 'M11_500kDa_NoA_1.6mgmL_8', 'M11_1MDa_NoA_0.6mgmL_8']
        
        #what we run now
        curr_tray = xlocsT
        curr_names = namesT
        for i_t, t in enumerate(temperatures):
            yield from bps.mv(ls.ch1_sp, t)
            if i_t > 0:
                yield from bps.sleep(600)
            for x, name in zip(curr_tray, curr_names):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.th,0.05-1)
                yield from alignCai()
                plt.close('all')
                angle_offset = [0.0, 0.025]
                a_off = piezo.th.position
                det_exposure_time(meas_t) 
                name_fmt = '{sample}_{temperature}C_{angle}deg'
                temp = ls.ch1_read.value
                for j, ang in enumerate( a_off + np.array(angle_offset) ):
                    yield from bps.mv(piezo.x, (x+j*200))
                    real_ang = 0.1 + angle_offset[j]
                    yield from bps.mv(piezo.th, ang)
                    sample_name = name_fmt.format(sample=name, temperature=temp, angle=real_ang)
                    sample_id(user_name='LC', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.scan(dets, waxs.arc, *waxs_arc)

        yield from bps.mv(ls.ch1_sp, 20)
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5)


