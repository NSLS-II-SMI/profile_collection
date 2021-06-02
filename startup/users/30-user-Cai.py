# command for running the code
# %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Cai.py 

def mapping_saxs_Cai(t=1): 
    samples = ['3Dprinted_filament_sr3','3Dprinted_filament_sr30','3Dprinted_filament_sr300','3Dprinted_filament_sr3000',
    'Interface_3Dpr_sp0.5', 'Interface_3Dpr_sp0.7', 'Interface_3Dpr_sp0.9', 'Interface_3Dpr_sp1.1']
    
    x_list = [38000,26000,13200,2600,
    -10600, -22600, -32600, -43600]
    y_list = [100,-450,600,-100,
    -300, -2300, -2000, -2100]
    
    name = 'PT'
    
    x_range=[[0, 5000, 11],[0, 5000, 11],[0, 5000, 11],[0, 5000, 11], 
    [0, 5000, 11],[0, 5000, 11],[0, 5000, 11],[0, 5000, 11]]
    y_range=[[0, 800, 41], [0, 1000, 51], [0, 1100, 56], [0, 1000, 51],
    [0, 3400, 171], [0, 4500, 226], [0, 5200, 261], [0, 6300, 316]]
    
    
    # Detectors, motors:
    dets = [pil1M]# dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, y, sample, x_r, y_r in zip(x_list, y_list, samples, x_range, y_range):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name=name, sample_name=sample) 
        yield from bp.rel_grid_scan(dets, piezo.x, *x_r, piezo.y, *y_r, 0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def saxs_cap_cai(t=1): 
    #xlocs = [-38000, -25000,-12500, -6800, -200, 6600, 12900, 19200, 25900, 32300, 44800]
    xlocs = [-44300]
    #ylocs = [-6800, -1700,-9600, 9000, 300, -2200, 9000, 9000, 9000, 6600, 5000, 7000]
    ylocs = [-9300]
    #names = ['BnMA0.0','BnMA0.3','BnMA0.6','BnMA0.80','BnMA0.85','BnMA1.1','BnMA2.0','BnMA3.0','BnMA5.5','BnMA0.54','BnMA1.1_new'][::-1]
    names = ['Cap_bkg',]
        
    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(13, 0, 3)
    
    #x_off = [-1000, 0, 1000]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y in zip(names, xlocs, ylocs):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)

            # for xx, x_of in enumerate(x_off):
            #     yield from bps.mv(piezo.x, x+x_of)
            #     xxa = xx+1

            name_fmt = '{sam}_cap_wa{waxs}'
            sample_name = name_fmt.format(sam=sam,  waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 




def saxs_cai_2020_3(t=1): 
    # xlocs = [-43000, -31000, -20000, -7500, 7000,  19200, 30500, 42500, 
    #         -44000,  -36000, -26500, -16000, -5500, 4000, 14000, 25000, 35500, 46000]
    # ylocs = [-9000,   -9000,  -9000,  -9000, -9000, -9500, -8400, -9000,
    #           8700,    8900,   8900,   8900,  8900,  9100, 9100,  9100,  9100, 8700]
    # zlocs = [2900,    2900,    2900,   2900,  2900,  2900,  2900,  2900, 
    #         -1100,   -1100,   -1100,  -1100, -1100, -1100, -1100, -1100, -1100,  -1100]
    # names = ['BMMB_1.74', 'BMMB_1.14', 'BMMB_0.84', 'BMMB_0.434', 'BMMB_0.35', 'M17n_0.04', 'M17n_0.05', 'M17n_0.06', 
    #          'M17n_0.08', 'M17n_0.12', 'M17n_0.17', 'M17n_0.21', 'M17n_0.24', 'M17n_0.28', 'M17n_0.30', 'M17n_0.34', 'M17n_0.35', 'M17n_0.40' ]
    
    # xlocs = [-43000, -30500, -17500, -3420,  6880, 12140, 27340, 38240]
    # ylocs = [  8700,   8700,   8700,  8900, -9000, -7600,  7315,  9515]
    # zlocs = [-1100,   -1100,  -1100, -1100, -1100, -1100, -1100, -1100]
    # names = ['M17n_0.44', 'LhBBL_0.64', 'bbPDMS_1', 'hDPDMS_0.64', 'hDPDMS_0.84', 'hDPDMS_0.94', 'hDPDMS_1.08', 'bbPDMS_5']
    
    xlocs = [-11820, ]
    ylocs = [   -8400]
    zlocs = [  3700 ]
    names = ['BM_0.875']

    # xlocs = [-43740, -37440, -31100, -24640, -18460, -5680,  600, 6940, 13200, 19660, 26160, 32780, 38940, 45020]
    # ylocs = [   200,    200,    200,    200,    200,   200,  200,  200,   600,   200,   200,   200,   200,   200]
    # zlocs = [  3700,   3700,   3700,   3700,   3700,  3700, 3700, 3700,  3700,  3700,  3700,  3700,  3700,  3700]
    # names = ['BM_2.15', 'BM_1.475', 'BM_1.42', 'BM_1.26', 'BM_1.00', 'BM_0.825', 'BM_0.6', 'BM_0.31', 'PDMS', 'MM_1.74', 'MM_1.14', 'MM_0.84', 
    # 'MM_0.434', 'MM_0.35']
    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 32.5, 6)
    #waxs_range = np.linspace(32.5, 32.5, 1)

    ypos = [-200, 200, 3]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z in zip(names, xlocs, ylocs, zlocs):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            name_fmt = '{sam}_16.1keV_sdd8.3m_wa{waxs}'
            sample_name = name_fmt.format(sam=sam,  waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.rel_scan(dets, piezo.y, *ypos)
            yield from bps.sleep(2)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 




def saxs_cai_2021_1(t=1): 
    # names = ['glass_bkg', 'M11_LBBL_0.26', 'M11_LBBL_0.30', 'M11_LBBL_0.34', 'M11_LBBL_0.38', 'M11_LBBL_0.44', 'M17_LBBL_200k','M17_LBBL_500k',
    # 'M17_LBBL_1000k', 'HA_251_f_10', 'HA_251_f_25', 'HA_988_f_11', 'HA_909_AAPA_89_f_12', 'HA_239_AAPA_23_f_12', 'HA_239_AAPA_23_f_26']
    # xlocs = [39000, 44000, 31000, 16000,  3000, -10000, -23000, -37000, 42000, 26000, 14000,    0, -13000, -27000, -41000]
    # ylocs = [-7000, -7000, -7000, -7000, -6000,  -6000,  -6000,  -6000,  6000,  6000,  6000, 6000,   6000,   6000,   6000]
    # zlocs = [ 2700,  2700,  2700,  2700,  2700,   2700,   2700,   2700,  2700,  2700,  2700, 2700,   2700,   2700,   2700]

    # names = ['HA_180_AAPA_60_f_11', 'HA_188_AAPA_62_f_32', 'BMB_6per', 'BMB_17per', 'BMB_1.1', 'Si']
    # xlocs = [38000, 24000, 10000, -2000, -14000, -25000]
    # ylocs = [    0,     0,     0,     0,      0,      0]
    # zlocs = [ 2700,  2700,  2700,  2700,   2700,   2700]

    # names = ['HA_251', 'HA_988', 'HA_239_AAPA_23', 'HA_180_AAPA_60', 'HA_188_AAPA_62', 'HA_909_AAPA_89']
    # xlocs = [-39000, -23600, -14600,  9000, 26500, 38000]
    # ylocs = [ -9500,   2800,   2800,  2800,  2800,  2000]
    # zlocs = [  2700,  -6100,  -5900, -5900, -5900,  -200]

    names = ['Cap_blank', 'HA_988_2', 'HA_239_AAPA_23_2', 'HA_180_AAPA_60_2', 'HA_188_AAPA_62_2']
    xlocs = [     -38900,    -24000,              -13800,               8100,              25900]
    ylocs = [      -2500,     -2500,               -6000,              -8300,              -9500]
    zlocs = [        500,     -6100,               -5900,              -5900,              -5900]
  
    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 32.5, 6)

    ypos = [-200, 200, 3]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z in zip(names, xlocs, ylocs, zlocs):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            name_fmt = '{sam}_16.1keV_sdd8.3m_wa{waxs}'
            sample_name = name_fmt.format(sam=sam,  waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.rel_scan(dets, piezo.y, *ypos)
            yield from bps.sleep(2)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 

def saxs_cai(t=1): 
    # xlocs = [-40000,-29000,-18500, -5500,8500,16500,32500,42500, -37000,-24500,-14000, -6000,-2500,9000, 19000, 34000, 44000]
    # y_top = -5900
    # y_bot = 6500
 
    # ylocs = [y_top,y_top,y_top,y_top,y_top,y_top,y_top,y_top,   y_bot,y_bot,y_bot,y_bot,y_bot,y_bot,y_bot, y_bot, y_bot ]
 
    # names = ['HA_123_AAPA_133', 'HA_64_AAPA_191', 'AAPA_247', 'AAPA_280', 'LhBBL_tBuMA_x_0.6', 'LhBBL_tBuMA_x_1', 'LhBBL_tBuMA_x_1.44', 'LhBBL_tBuMA_x_2.3',
    # 'LBBL_378', 'LhBBL_306_BnMA_x_0.83', 'LhBBL_402_BnMA_x_0.84', 'LhBBL_508_BnMA_x_0.83', 'M17_LBBL_0.45','glass_bkg', 'M17_LBBL_0.49', 'M17_LBBL_0.54', 'HA_188_AAPA_62_f_27']
    

    xlocs = [1000, -8000, -21000, -31500, -41500]
    ylocs = [6500,  5900,   5900,   5900,   5000]
 
    names = ['LhBBL_207_BnMA_x_2.39', 'LhBBL_200_BnMA_x_3.46', 'hPDMS_207_BnMA_x_2.39', 'hPDMS_200_BnMA_x_3.46', 'hPDMS_198_BnMA_x_6.2']

    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(32.5, 0, 6)
    
    x_off = [-500, 0, 500]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y in zip(names, xlocs, ylocs):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)

            for xx, x_of in enumerate(x_off):
                yield from bps.mv(piezo.x, x+x_of)
                xxa = xx+1

                name_fmt = '{sam}_pos{pos}_wa{waxs}_16.1keV_sdd8.3m'
                sample_name = name_fmt.format(sam=sam, pos='%1.1d'%xxa, waxs='%2.1f'%wa)
                sample_id(user_name=user, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 
    

def gisaxs_cai(t=1): 
    #samples = ['LhBBL_0_80','LhBBL_0.3_80','LhBBL_0.6_80','LhBBL_0.8_80','LhBBL_0.85_80', 'LhBBL_1.1_80','LhBBL_2_80','LhBBL_3_80','LhBBL_5.5_80','LhBBL_0.54_80', 'LhBBL_1.1new_80']
    samples = ['LhBBL_0_40','LhBBL_0.3_40','LhBBL_0.6_40','LhBBL_0.8_40','LhBBL_0.85_40', 'LhBBL_1.1_40','LhBBL_2_40','LhBBL_3_40','LhBBL_5.5_40','LhBBL_0.54_40', 'LhBBL_1.1new_40']
    x_list = [-49000, -39000,-30000,-18000, -7000, 3000, 12000, 22000, 32000, 42000, 52000]
    waxs_arc = [13, 6.5, 0]
    angle = [0.08, 0.125, 0.2]

  # Detectors, motors:
    dets = [pil1M, pil300KW]
    
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for x, sample in zip(x_list,samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(pil1m_pos.x, -2.3)
        yield from alignement_gisaxs(0.08)
        yield from bps.mv(pil1m_pos.x, 0.8)
        
        det_exposure_time(t, t) 
        name_fmt = '{sample}_ai{angle}deg_wa{wax}'
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            for an in angle:
                yield from bps.mvr(piezo.th, an)
                sample_name = name_fmt.format(sample=sample, angle='%3.3f'%an, wax = '%2.2d'%wa)
                sample_id(user_name='ZG', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                yield from bps.mvr(piezo.th, -an)                   
                

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


                        
def run_giwaxs_cai(t=1): 
    #run with WAXS
    dets = [pil300KW, pil1M]
    waxs_arc = [13, 0, 3]
    
    #run with SAXS only
    #dets = [pil1M]
    #redo this but subtract another 800 um from X
    xlocs1 = [-51000,-40200,-24800,-14200, -3600, 6600, 16400, 24000, 35600, 50000]
    names1 = ['3_100_80mgmL', '3_104_80mgmL', '3_106_80mgmL', '3_107_80mgmL', '3_108_80mgmL', '3_100_40mgmL', '3_104_40mgmL', '3_106_40mgmL', '3_107_40mgmL', '3_108_40mgmL']
    
    xlocs2 = [-15000, -3500, 7500, 19500]
    xlocs3 = [-46000,-40000,-28000,-18000, -7000, 3000, 14000, 24000, 35000, 45000]
    xlocs4 = [-50000,-40000,-29000,-18000, -7000, 4000, 14000, 25500, 36000, 47000]
    xlocs5 = [-50000,-38000,-25500,-17000, -5000, 8000, 16000, 27000, 37000, 48000]
    xlocs6 = [-50000,-39000,-29000,-15000, -6000, 5000, 15000, 26000, 37000, 48000]
    xlocs7 = [-49000,-37000,-24000,-11000, 6500, 16500, 29000, 4100]
    xlocs8 = [29500, 41000]
    xlocs9 = [-44300,-34300,-25800,-15800, -800, 7000, 17000, 28200, 38200, 48200]
    
    
    names2 = ['BzMA_5.5_M11_80mgmL', 'BzMA_M11_BzMA_40mgmL', 'BzMA_BzMA_0.3_M11_BzMA_40mgmL', 'BzMA_BzMA_0.6_M11_BzMA_40mgmL', 'BzMA_BzMA_0.8_M11_BzMA_40mgmL', 'BzMA_BzMA_1.1_M11_BzMA_40mgmL', 'BzMA_BzMA_2.0_M11_BzMA_40mgmL', 'BzMA_BzMA_3.0_M11_BzMA_40mgmL', 'BzMA_BzMA_5.5_M11_BzMA_40mgmL', 'BzMA_BzMA_3.2_M11_BzMA_40mgmL']
    names3 = ['BB5k_900k_PS_2x14k_80mgmL', 'BB5k_900k_PS_2x14k_40mgmL', 'BB5k_900k_PS_2x14k_20mgmL', 'BB5k_900k_PS_2x14k_10mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_80mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_40mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_20mgmL', 'NBPS160k_NBPDMS_4dot5M_NBPS_160k_10mgmL', 'NBPS300k_NBPDMS_8M_NBPS_300k_80mgmL', 'NBPS300k_NBPDMS_8M_NBPS_300k_40mgmL']
    names4 = ['BB5k_50k_BzMA_2x45_80mgmL', 'BB5k_50k_BzMA_2x115_80mgmL', 'BB5k_50k_BzMA_2x382_80mgmL', 'BB5k_50k_BzMA_2x580_80mgmL', 'BB5k_42k_BzMA_2x168_80mgmL', 'BB5k_50k_BzMA_2x45_40mgmL', 'BB5k_50k_BzMA_2x115_40mgmL', 'BB5k_50k_BzMA_2x382_40mgmL', 'BB5k_50k_BzMA_2x580_40mgmL', 'BB5k_42k_BzMA_2x168_20mgmL']
    names5 = ['BzMA_BzMA_0.8_M11_BzMA_80mgmL_2nd', 'BzMA_3.0_M11_80mgmL_2nd', 'BzMA_5.5_M11_80mgmL_2nd', 'BzMA_BzMA_0.8_M11_BzMA_40mgmL_2nd']
    names6 = ['PHA10NH_37k_PS_2x3536_80mgmL', 'PHA10NH_37k_PS_2x3536_40mgmL', 'PHA10NH_37k_PS_2x3536_20mgmL', 'PHA10NH_37k_PS_2x3536_10mgmL', 'PHA10NH_43k_PS_2x6552_80mgmL', 'PHA10NH_43k_PS_2x6552_40mgmL', 'PHA10NH_43k_PS_2x6552_20mgmL', 'PHA10NH_43k_PS_2x6552_10mgmL', 'PHA25NH_38dot5k_PS_2x5928_80mgmL', 'PHA25NH_38dot5k_PS_2x5928_40mgmL']
    names7 = ['PHA25NH_38dot5k_PS_2x5928_20mgmL', 'PHA25NH_38dot5k_PS_2x5928_10mgmL', 'PHA100NH_65k_80mgmL', 'PHA100NH_65k_40mgmL', 'PHA100NH_65k_20mgmL', 'PHA100NH_65k_10mgmL', 'Shifeng_1', 'Shifeng_2']
    names8 = ['NBPS300k_NBPDMS_8M_NBPS_300k_20mgmL', 'NBPS300k_NBPDMS_8M_NBPS_300k_10mgmL']

    #what we run now
    curr_tray = xlocs2
    curr_names = names5
    assert len(curr_tray) == len(curr_names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    for x, name in zip(curr_tray, curr_names):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.th, 0.5)
        yield from bps.mv(pil1m_pos.x, -2.3)
        #yield from bps.sleep(2)
        yield from alignement_gisaxs(0.1)
        yield from bps.mv(pil1m_pos.x, 0.7)
        #yield from bps.sleep(2)
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
            #yield from bp.count(dets, num=1)
            yield from bp.scan(dets, waxs, *waxs_arc)

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3)

def run_trans_cai(t=1): 
    #run with WAXS
    dets = [pil300KW, pil1M]
    waxs_arc = [0, 6.5, 13]
    
    #run with SAXS only
    #dets = [pil1M]

    x_list  = [34000, 24200, 13200, 1200, -9800, -20800, -42800, -31800, -20800, -9800, 1200, 13200, 24200, 34000]
    y_list =  [-10000, -10000, -10000, -10000, -10000, -10000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000]
    samples = [ 'BzMA_3.0_M11_Trans_2nd', 'BB5k_50k_BzMA_2x45_Trans_2nd', 'BB5k_50k_BzMA_2x115_Trans_2nd', 'BB5k_42k_BzMA_2x168_Trans_2nd', 'BB5k_50k_BzMA_2x382_Trans_2nd', 'BB5k_50k_BzMA_2x580_Trans_2nd', 'BzMA_BzMA_5.5_M11_BzMA_Trans_2nd','BzMA_BzMA_3.0_M11_BzMA_Trans_2nd','BzMA_BzMA_2_M11_BzMA_Trans_2nd','BzMA_BzMA_1.1_M11_BzMA_Trans_2nd','BzMA_BzMA_0.8_M11_BzMA_Trans_2nd','BzMA_BzMA_0.6_M11_BzMA_Trans_2nd','BzMA_BzMA_0.3_M11_BzMA_Trans_2nd', 'BzMA_M11_BzMA_Trans_2nd']
    
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coordinates ({len(y_list)})'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    #what we run now
    
    for wa in waxs_arc[::-1]:
        yield from bps.mv(waxs, wa)

        for x, y, s in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.sleep(2)

            det_exposure_time(t,t) 
            name_fmt = '{sample}_wa{wax}'
            sample_name = name_fmt.format(sample=s, wax = '%2.2d'%wa) 
            sample_id(user_name='LC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
            sample_id(user_name='test', sample_name='test')
            det_exposure_time(0.3,0.3)



def run_giwaxs_cai_temp(t=1): 
    dets = [pil300KW, pil1M]
    xlocs1 = [2800,-8600]
   
    names1 = ['BzMA_3.0_M11_80mgmL', 'BzMA_5.5_M11_80mgmL']
   
        
    #what we run now
    curr_tray = xlocs1
    curr_names = names1
    assert len(curr_tray) == len(curr_names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    waxs_arc = [0, 6.5, 13.0, 19.5]
    for x, name in zip(curr_tray, curr_names):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.th, 0)
        yield from bps.mv(pil1m_pos.x, -2.3)
        #yield from bps.sleep(2)
        yield from alignement_gisaxs_shorter(0.1)
        yield from bps.mv(pil1m_pos.x, 0.7)
        #yield from bps.sleep(2)
        plt.close('all')
        angle_offset = [0.125, 0.2]
        a_off = piezo.th.position
        det_exposure_time(t,t)
        temper = ls.ch1_read.value
        for wa in waxs_arc:
            name_fmt = '{sample}_{temp}_{angle}deg_wa{wax}'
            #name_fmt = '{sample}_{angle}deg_wa{wax}'

            for j, ang in enumerate( a_off + np.array(angle_offset) ):
                yield from bps.mv(piezo.x, (x+j*200))
                real_ang = angle_offset[j]
                yield from bps.mv(piezo.th, ang)
                sample_name = name_fmt.format(sample=name, temp = '%5.2f'%temper, angle=np.float('%.3f'%real_ang), wax = '%2.2d'%wa)
                #sample_name = name_fmt.format(sample=name, angle=np.float('%.3f'%real_ang), wax = '%2.2d'%wa)

                sample_id(user_name='LC', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

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
                    yield from bp.scan(dets, waxs, *waxs_arc)

        yield from bps.mv(ls.ch1_sp, 20)
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5)





def Cai_saxs_tensile_hard(t=0.2):
    dets = [pil1M, pil300KW]

    names = 'LhBBL_insitu_0.85_new2'

    t0 = time.time()
    for i in range(2000):

        det_exposure_time(t,t) 
        name_fmt = '{sample}_14000eV_sdd8p3_waxs8.0_{time}_{i}'
        t1 = time.time()
        sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), i = '%3.3d'%i)
        sample_id(user_name='SN', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)

        time.sleep(20)




def saxs_cai_2021_2(t=1): 
 
    # xlocs = [45800, 42800, 35500, 29000, 17500, 12900,  1400, -7300, -13400, -17700, -24200, -30500, -35500, -40500]
    # ylocs = [ 3000,  1500, -1800, -1200,  3600,  5500,  5700,  4900,   5800,   5800,   2600,  -8400,  -2400,   3000]
    # zlocs = [ 2000,  -700,  -700,  -700,  -700,  -700, -3500,  5000,   5000,   5000,   -700,   -700,   -700,   -700]
    # ystage = [-2.99,-2.99, -2.99, -2.99, -2.99, -2.99, -2.99, -2.99,  -2.99,  -2.99,  -2.99,   -6.0,   -2.99, -2.99]
    # names = ['HA_251', 'HA_229_AAPA_21', 'HA_189_AAPA_64', 'HA_1009', 'HA_927_AAPA_93', 'HA_725_AAPA_255', 'hPDMS_tBuMA_x_0.6', 'hPDMS_tBuMA_x_1', 
    # 'hPDMS_tBuMA_x_1.44', 'hPDMS_tBuMA_x_2.3', 'PDMS_378', 'hPDMS_306_BnMA_x_0.83', 'hPDMS_402_BnMA_x_0.84', 'hPDMS_508_BnMA_x_0.83']
  
  
    names = ['LhBBL _207_BnMA_x_2.39', 'LhBBL _200_BnMA_x_3.46', 'hPDMS_207_BnMA_x_2.39', 'hPDMS_200_BnMA_x_3.46', 'hPDMS_198_BnMA_x_6.2']
  
    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})'
    assert len(xlocs) == len(ylocs), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(ylocs)})'
    assert len(xlocs) == len(zlocs), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(zlocs)})'
    assert len(xlocs) == len(ystage), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(ystage)})'
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})'

    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(32.5, 0, 6)
    #waxs_range = np.linspace(32.5, 32.5, 1)

    ypos = [-200, 200, 3]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z, y_sta in zip(names, xlocs, ylocs, zlocs, ystage):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)
            yield from bps.mv(stage.y, y_sta)

            name_fmt = '{sam}_16.1keV_sdd8.3m_wa{waxs}'
            sample_name = name_fmt.format(sam=sam,  waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.rel_scan(dets, piezo.y, *ypos)
            yield from bps.sleep(2)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 