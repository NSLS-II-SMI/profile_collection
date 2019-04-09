            
def gisaxsCai(meas_t=3):
        dets = [pil300KW, xbpm3.sumY]
        x_edge = -15000
        xlocs1 = [0]
        names1 = ['022819-8_Ray8']
        
        #what we run now
        curr_tray = xlocs1
        curr_names = names1
        waxs_arc = [2.83, 14.83, 3]
        for x, name in zip(curr_tray, curr_names):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.th,0.05)
                yield from alignCai()
                plt.close('all')
                angle_offset = [0.0]
                a_off = piezo.th.position
                det_exposure_time(meas_t) 
                name_fmt = '{sample}_{angle}deg'
                for j, ang in enumerate( a_off + np.array(angle_offset) ):
                    yield from bps.mv(piezo.x, (x-glob_xoff+j*200))
                    real_ang = 0.095 + angle_offset[j]
                    yield from bps.mv(piezo.th, ang)
                    sample_name = name_fmt.format(sample=name, angle=real_ang)
                    sample_id(user_name='SN_13.9keV', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.scan(dets, waxs.arc, *waxs_arc)

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5)


def gisaxsCaiTemp(meas_t=1):
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


