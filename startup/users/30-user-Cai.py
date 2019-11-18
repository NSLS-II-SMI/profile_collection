# command for running the code
# %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Cai.py 
# RE(run_giwaxs_cai(2))

                        
def run_giwaxs_cai(t=2): 
    dets = [pil300KW, pil1M]
    xlocs1 = [-48000,-38000,-28000,-18000, -7800, 4000, 14000, 25000, 35000, 45000]
    xlocs2 = [-50000,-40000,-29000,-19000, -8000, 2000, 13000, 23000, 35000, 45000]
    xlocs3 = [-46000,-40000,-28000,-18000, -7000, 3000, 14000, 24000, 35000, 45000]
    xlocs4 = [-50000,-40000,-29000,-18000, -7000, 4000, 14000, 25500, 36000, 47000]
    xlocs5 = [-50000,-38000,-25500,-17000, -5000, 8000, 16000, 27000, 37000, 48000]
    xlocs6 = [-50000,-39000,-29000,-15000, -6000, 5000, 15000, 26000, 37000, 48000]
    xlocs7 = [-49000,-37000,-24000,-11000, 6500, 16500, 29000, 4100]
    xlocs8 = [29500, 41000]
    xlocs9 = [-44300,-34300,-25800,-15800, -800, 7000, 17000, 28200, 38200, 48200]
    
    
    names1 = ['BB5k_100k_PBMA_2x3k_80mgmL', 'BB5k_100k_PBMA_2x3k_40mgmL', 'BB5k_100k_PBMA_2x3k_20mgmL', 'BB5k_100k_PBMA_2x3k_10mgmL', 'BB5k_200k_PBMA_2x5k_80mgmL', 'BB5k_200k_PBMA_2x5k_40mgmL', 'BB5k_200k_PBMA_2x5k_20mgmL', 'BB5k_200k_PBMA_2x5k_10mgmL', 'BB5k_560k_PBMA_2x20k_80mgmL', 'BB5k_560k_PBMA_2x20k_40mgmL']
    names2 = ['BB5k_560k_PBMA_2x20k_20mgmL', 'BB5k_560k_PBMA_2x20k_10mgmL', 'BB5k_1000k_PBMA_2x15k_80mgmL', 'BB5k_1000k_PBMA_2x15k_40mgmL', 'BB5k_1000k_PBMA_2x15k_20mgmL', 'BB5k_1000k_PBMA_2x15k_10mgmL', 'BB5k_1500k_PBMA_2x31k_80mgmL', 'BB5k_1500k_PBMA_2x31k_40mgmL', 'BB5k_1500k_PBMA_2x31k_20mgmL', 'BB5k_1500k_PBMA_2x15k_10mgmL']
    names3 = ['BB5k_900k_PS_2x14k_80mgmL', 'BB5k_900k_PS_2x14k_40mgmL', 'BB5k_900k_PS_2x14k_20mgmL', 'BB5k_900k_PS_2x14k_10mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_80mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_40mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_20mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_10mgmL', 'NBPS300k_NBPDMS_8M_NBPS_300k_80mgmL', 'NBPS300k_NBPDMS_8M_NBPS_300k_40mgmL']
    names4 = ['PHA0NH_34k_PS_2x3536_80mgmL', 'PHA0NH_34k_PS_2x3536_40mgmL', 'PHA0NH_34k_PS_2x3536_20mgmL', 'PHA0NH_34k_PS_2x3536_10mgmL', 'PHA0NH_40k_PS_2x5720_80mgmL', 'PHA0NH_40k_PS_2x5720_40mgmL', 'PHA0NH_40k_PS_2x5720_20mgmL', 'PHA0NH_40k_PS_2x5720_10mgmL', 'PHA0NH_42k_PS_2x9880_80mgmL', 'PHA0NH_42k_PS_2x9880_40mgmL']
    names5 = ['PHA0NH_42k_PS_2x9880_20mgmL', 'PHA0NH_42k_PS_2x9880_10mgmL', 'PHA5NH_47dot5k_PS_2x3432_80mgmL', 'PHA5NH_47dot5k_PS_2x3432_40mgmL', 'PHA5NH_47dot5k_PS_2x3432_20mgmL', 'PHA5NH_47dot5k_PS_2x3432_10mgmL', 'PHA5NH_43k_PS_2x6968_80mgmL', 'PHA5NH_43k_PS_2x6968_40mgmL', 'PHA5NH_43k_PS_2x6968_20mgmL', 'PHA5NH_43k_PS_2x6968_10mgmL']
    names6 = ['PHA10NH_37k_PS_2x3536_80mgmL', 'PHA10NH_37k_PS_2x3536_40mgmL', 'PHA10NH_37k_PS_2x3536_20mgmL', 'PHA10NH_37k_PS_2x3536_10mgmL', 'PHA10NH_43k_PS_2x6552_80mgmL', 'PHA10NH_43k_PS_2x6552_40mgmL', 'PHA10NH_43k_PS_2x6552_20mgmL', 'PHA10NH_43k_PS_2x6552_10mgmL', 'PHA25NH_38dot5k_PS_2x5928_80mgmL', 'PHA25NH_38dot5k_PS_2x5928_40mgmL']
    names7 = ['PHA25NH_38dot5k_PS_2x5928_20mgmL', 'PHA25NH_38dot5k_PS_2x5928_10mgmL', 'PHA100NH_65k_80mgmL', 'PHA100NH_65k_40mgmL', 'PHA100NH_65k_20mgmL', 'PHA100NH_65k_10mgmL', 'Shifeng_1', 'Shifeng_2']
    names8 = ['NBPS300k_NBPDMS_8M_NBPS_300k_20mgmL', 'NBPS300k_NBPDMS_8M_NBPS_300k_10mgmL']

    
    
        
    #what we run now
    curr_tray = xlocs8
    curr_names = names8
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
    dets = [pil300KW, pil1M]
    xlocs1 = [-6000,5500]
   
    names1 = ['PHA5NH_47dot5k_PS_2x3432_40mgmL', 'NBPS300k_NBPDMS_8M_NBPS_300k_20mgmL']
   
        
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


