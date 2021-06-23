def run_caps_fastRPI(t=1): 
    x_list  = [ 6908,13476,19764,26055]#
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 45.5, 8)
    samples = [    'LC-O38-6-100Cto40C', 'LC-O37-7-100Cto40C', 'LC-O36-9-100Cto40C', 'LC-O35-8-100Cto40C']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t,t)
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x in zip(samples, x_list):
            yield from bps.mv(piezo.x, x)            
            name_fmt = '{sam}_wa{waxs}'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 


def run_saxs_capsRPI(t=1): 
    x_list  = [ 6908,13476,19764,26055]#
    # Detectors, motors:
    dets = [pil1M]
    y_range = [2000, -8000, 11] #[2.64, 8.64, 2]
    samples = [    'LC-O38-6-100Cto40C', 'LC-O37-7-100Cto40C', 'LC-O36-9-100Cto40C', 'LC-O35-8-100Cto40C']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(piezo.x, x)
        sample_id(user_name=sample, sample_name='') 
        yield from bp.scan(dets, piezo.y, *y_range)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 
#,'SL-PS3','SL-PS3_98_8_PS33','SL-PS3_97_0_PS33','SL-PS3_94_9_PS33','SL-PS3_93_0_PS33','SL-PS3_89_9_PS33','SL-PS3_79_8_PS33','SL-PS3_70_1_PS33','SL-PS3_60_0_PS33','SL-PS3_49_9_PS33','SL-PS3_40_0_PS33','SL-PS3_29_8_PS33','SL-PS3_20_1_PS33','SL-PS3_10_0_PS33','SL-PS3_7_0_PS33','SL-PS3_4_9_PS33','SL-PS3_3_0_PS33','SL-PS33','SL-PS148




# xlocs = [42000,33000,24000,15000,5000,-4000,-13000,-22000,-32000,-41000,42000,33000,24000,15000,5000,-4000,-13000,-22000,-32000,-41000]
    #ylocs = [8800,8800,8800,8800,8800,8800,8800,8800,8800,8800,-7200,-7200,-7200,-7200,-7200,-7200,-7200,-7200,-7200,-7200]

# xlocs = [42000,33000,24000,15000,5000,-4000,-13000,-22000,-30000,42000,32000,24000,15000,4000,-4000,-12000]
   # ylocs = [8500,8500,8500,8500,8500,8500,8500,8500,8500,-6800,-6800,-6800,-6800,-6800,-6800,-6800]
  #  names = ['EPTD-y0.9-2s','EPTD-y1.0-2s','EPG-X0.8-2s','EPG-X0.9-2s','ETP-x0-2s','ETP-x0.1-2s','ETP-x0.2-2s','ETP-x0.3-2s','ETP-x0.4-2s','ETP-x0.6-2s','ETP-x0.7-2s','ETP-x0.8-2s','ETP-x0.9-2s','ETP-x1.0-2s','ETP-x0.5-2s','vacuum-2s']

#  xlocs = [-37550,-37550,-37550,-38950,-38950,-38950,-41850,-41850,-41850,-42850,-42850,-42850,-16100,-16100,-16100,-18600,-18600,-18600,-20400,-20400,-20400,-22500,-22500,-22500,-24100,-24100,-24100, -26100,-26100,-26100,-28300,-28300,-28300,-29300,-29300,-29300,-32900,-32900,-32900,-34900,-34900,-34900]
 #   ylocs = [8000, 8500,9000, 8000, 8500,9000, 8000, 8500,9000, 8000, 8500,9000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000]
 #   names = ['PACM-1','PACM-2','PACM-3','EPON828-1','EPON828-2','EPON828-3','DDS-1','DDS-2','DDS-3','B8O1-3-1','B8O1-3-2','B8O1-3-3','D2000-1','D2000-2','D2000-3','T3000-1','T3000-2','T3000-3','PPG-1','PPG-2','PPG-3','D230-1','D230-2','D230-3','blank-1mm-1','blank-1mm-2','blank-1mm-3','B8O1-1-1','B8O1-1-2','B8O1-1-3','B8O1-2-1','B8O1-2-2','B8O1-2-3','B9O1-1-1','B9O1-1-2','B9O1-1-3','B10O1-1-1','B10O1-1-2','B10O1-1-3','vacuum-1s-1','vacuum-1s-2','vacuum-1s-3']



def run_saxs_capsRPI_2021_1(t=1): 

    # samples = ['J1_S01_14wt_q55_01', 'J1_S02_14wt_q45_01', 'J1_S03_14wt_q35_01', 'J1_S04_14wt_q25_01', 'J1_S05_14wt_q25_h45_01', 'J1_S06_15wt_q60_01',
    # 'J1_S07_15wt_q55_01', 'J1_S08_15wt_q50_01', 'J1_S09_15wt_q40_01', 'J1_S10_15wt_q25_01', 'J1_S11_15wt_q25_h55_01', 'J1_S12_16wt_q65_01',
    # 'J1_S13_16wt_q60_01', 'J1_S14_16wt_q55_01', 'J1_S15_16wt_q50_01']
    # xlocs = [ 44000, 38000, 31600, 25200, 19100, 12900, 6500, 200, -6350, -12700, -19050, -25350, -31200, -37800, -44250]
    # y_range = [-4100, 1030, 20]
    
    # samples = ['J2_S01_16wt_q45_01', 'J2_S02_16wt_q40_01', 'J2_S03_16wt_q25_01', 'J2_S04_16wt_q25_h60_01', 'J2_S05_16wt_q25_h55_01', 
    # 'J2_S06_16wt_q25_h50_01', 'J2_S07_17wt_q65_01', 'J2_S08_17wt_q50_01', 'J2_S09_17wt_q40_01', 'J2_S10_17wt_q25_01', 'J2_S11_17wt_q25_h65_01', 
    # 'J2_S12_17wt_q25_h50_01', 'J2_S13_18wt_q77_01', 'J2_S14_18wt_q70_01', 'J2_S15_18wt_q65_01']
    # xlocs = [ 44200, 37950, 31700, 25450, 19250, 12750, 6100, 0, -6100, -12450, -18800, -25150, -31300, -37900, -43850]
    # y_range = [-4100, 1030, 20]

    # samples = ['J3_S01-18wt_q60_01', 'J3_S02_18wt_q40_01', 'J3_S03_18wt_q25_01', 'J3_S04_18wt_q25_h70_01', 'J3_S05_18wt_q25_h50_01', 'J3_S06_19wt_q65_01',
    # 'J3_S07_19wt_q55_01', 'J3_S08_19wt_q40_01', 'J3_S09_19wt_q25_01', 'J3_S10_19wt_q25_h77_01', 'J3_S11_19wt_q25_h70_01', 'J3_S12_20wt_q82_01', 
    # 'J3_S13_20wt_q79_01', 'J3_S14_20wt_q75_01', 'J3_S15_20wt_q60_01']
    # xlocs = [ 44000, 38100, 31750, 25100, 18750, 12400, 6550, -100, -6000, -12400, -19000, -25100, -31300, -37650, -44150]
    # y_range = [-4100, 1030, 20]

    # samples = ['J4_S01_20wt_q40_01', 'J4_S02_20wt_q25_01', 'J4_S03_20wt_q25_h79_01', 'J4_S04_20wt_q25_h70_01', 'J4_S05_21wt_q84_01', 'J4_S06_21wt_q81_01',
    # 'J4_S07_21wt_q75_01', 'J4_S08_21wt_q70_01', 'J4_S09_21wt_q50_01', 'J4_S10_21wt_q25_01', 'J4_S11_21wt_q25_h81_01', 'J4_S12_21wt_q25_h70_01',
    # 'J4_S13_22wt_q86_01', 'J4_S14_22wt_q83_01', 'J4_S15_22wt_q80_01']
    # xlocs = [ 44000, 37450, 31200, 24900, 18850, 12700, 6400, -50, -6400, -12650, -18950, -25300, -31700, -38050, -44550]
    # y_range = [-4100, 1030, 20]

    # samples = ['J5_S01_22wt_q75_01', 'J5_S02_22wt_q60_01', 'J5_S03_22wt_q40_01', 'J5_S04_22wt_q25_01', 'J5_S05_22wt_q25_h83_01', 'J5_S06_22wt_q25_h75_01',
    # 'J5_S07_23wt_q88_01', 'J5_S08_23wt_q84_01', 'J5_S09_23wt_q80_01', 'J5_S10_23wt_q75_01', 'J5_S11_23wt_q60_01', 'J5_S12_23wt_q40_01', 
    # 'J5_S13_23wt_q25_01', 'J5_S14_23wt_q25_h84_01', 'J5_S15_23wt_q25_h75_01']
    # xlocs = [ 44050, 37950, 31600, 25450, 19150, 12900, 6350, 0, -6300, -12500, -18800, -25150, -31200, -37800, -43900]
    # y_range = [-4100, 1030, 20]

    # samples = ['J6_S01_24wt_q93_01', 'J6_S02_24wt_q90_01', 'J6_S03_24wt_q80_01', 'J6_S04_24wt_q75_01', 'J6_S05_24wt_q60_01', 'J6_S06_24wt_q40_01',
    # 'J6_S07_24wt_q25_01', 'J6_S08_24wt_q25_h90_01', 'J6_S09_24wt_q25_h75_01', 'J6_S10_12wt_q40_01', 'J6_S11_12wt_q35_01', 'J6_S12_12wt_q25_01',
    # 'J6_S13_12wt_q25_h40_01', 'J6_S14_127wt_q45_01', 'J6_S15_127wt_q40_01']
    # xlocs = [ 44300, 38050, 31700, 25350, 19050, 12700, 6550, 0, -5900, -12550, -18650, -24950, -31100, -37450, -43800]
    # y_range = [-4100, 1030, 20]

    # samples = ['J7_S01_127wt_q35_01', 'J7_S02_127wt_q25_01', 'J7_S03_127wt_q25_h40_01', 'J7_S04_137wt_q55_01', 'J7_S05_137wt_q45_01',
    # 'J7_S06_137wt_q35_01', 'J7_S07_137wt_q25_01', 'J7_S08_137wt_q25_h45_01', 'J7_S09_S_water_01', 'J7_S10_blank_cap_01']
    # xlocs = [ 44100, 37450, 31200, 25200, 18750, 12600, 6100, 0, -6550, -12800]
    # y_range = [-4100, 1030, 20]

    samples = ['CT1_1_Blank_S_11', 'CT1_2_QAT2C_S_11', 'CT1_3_QAT3C_S_11', 'CT1_4_QAT5C_S_11', 'CT1_5_QAT6C_S_11', 'CT1_6_QAT7C_S_11',
    'CT1_12_QAS7C_S_11', 'CT1_13_QAS9C_S_11', 'CT1_14_QAS10C_S_11', 'CT1_15_QAS11C_S_11']
    xlocs = [44400, 38100, 31600, 25200, 19200, 12700, -24900, -31300, -37800, -44000]
    y_range = [-3000, 0, 4]
    
    # samples = ['CT2_1_QAT2CP_S_11', 'CT2_2_QAT3CP_S_11', 'CT2_3_QAT5CP_S_11', 'CT2_4_QAT6CP_S_11', 'CT2_5_QAT7CP_S_11', 
    # 'CT2_9_QAS7CP_S_11', 'CT2_11_QAS9CP_S_11', 'CT2_12_QAS10CP_S_11', 'CT2_14_QAS11CP_S_11']
    # xlocs = [ 44100, 37450, 31200, 25200, 18750, 12600, 6100, 0, -6550, -12800]
    # y_range = [-4100, 1030, 20]




    assert len(xlocs) == len(samples), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(samples)})'
    
    dets = [pil1M]
    det_exposure_time(t)

    for x, sample in zip(xlocs, samples):
        yield from bps.mv(piezo.x, x)
        sample_id(user_name=sample, sample_name='') 
        yield from bp.scan(dets, piezo.y, *y_range)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 


def run_waxs_fastRPI_2021_(t=1):
    # samples = ['CT1_1_Blank_S_11', 'CT1_2_QAT2C_S_11', 'CT1_3_QAT3C_S_11', 'CT1_4_QAT5C_S_11', 'CT1_5_QAT6C_S_11', 'CT1_6_QAT7C_S_11',
    # 'CT1_12_QAS7C_S_11', 'CT1_13_QAS9C_S_11', 'CT1_14_QAS10C_S_11', 'CT1_15_QAS11C_S_11']
    # xlocs = [44400, 38100, 31600, 25200, 19200, 12700, -24900, -31300, -37800, -44000]
    # y_range = [-3000, 0, 4]
    
    samples = ['CT2_1_QAT2CP_S_11', 'CT2_2_QAT3CP_S_11', 'CT2_3_QAT5CP_S_11', 'CT2_4_QAT6CP_S_11', 'CT2_5_QAT7CP_S_11', 
    'CT2_9_QAS7CP_S_11', 'CT2_11_QAS9CP_S_11', 'CT2_12_QAS10CP_S_11', 'CT2_14_QAS11CP_S_11']
    xlocs = [ 44500, 38400, 32000, 25600, 19400, -5600, -18600, -24700, -37400]
    y_range = [-3000, 0, 4]

    user = 'SL'    

    #Check if the length of xlocs, ylocs and names are the same 
    assert len(xlocs) == len(samples), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(samples)})'

    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 45.5, 8)
    
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x in zip(samples, xlocs):
            yield from bps.mv(piezo.x, x)            
            
            name_fmt = '{sam}_wa{waxs}'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name)

            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, piezo.y, *y_range)


def run_waxs_fastRPI_2021_2(t=1):

    y_top = -8000
    y_bot = 8000
    #         1      2       3       4       5      6      7       8       9
    xlocs = [ 42000, 33000,  20000,  12000,  5000, -6500, -16000, -26000, -36000,
              42000, 34000,  23000,  12000]
    ylocs = [ y_top, y_top,  y_top,  y_top,  y_top, y_top, y_top,  y_top,  y_top,
              y_bot, y_bot,  y_bot,  y_bot]

    # xlocs = [ 42000, 33000,  22000,  12000,  5000, -6500, -16000, -25000, -34000,
    #           42000, 33000,  22000,  12000,  5000, -6500, -17500, -25000, -34000]
    # ylocs = [ y_top, y_top,  y_top,  y_top,  y_top, y_top, y_top,  y_top,  y_top,
    #           y_bot, y_bot,  y_bot,  y_bot,  y_bot, y_bot, y_bot,  y_bot,  y_bot]

    # Capillary
    #x_off = [0]
    #y_off = [-1000, -500, 0, 500, 1000] 
    
    # Plaques
    x_off = [-500, 0, 500]
    y_off = [-500, 500] 

    # # Rack N1 - Plaques
    #         1                      2                    3                     4                     5                     6                     7                     8                      9  
    #names =['N1_S01_ETTD_m04_n00','N1_S02_ETTD_m04_n01','N1_S03_ETTD_m04_n02','N1_S04_ETTD_m04_n03','N1_S05_ETTD_m04_n04','N1_S06_ETTD_m04_n05','N1_S07_ETTD_m04_n06','N1_S08_ETTD_m04_n07','N1_S09_ETTD_m04_n08',
    #        'N1_S10_ETTD_m04_n09','N1_S11_ETTD_m04_n10','N1_S12_ETTD_m05_n00','N1_S13_ETTD_m05_n01','N1_S14_ETTD_m05_n02','N1_S15_ETTD_m05_n03','N1_S16_ETTD_m05_n04','N1_S17_ETTD_m05_n05','N1_S18_ETTD_m05_n06']

    # # Rack N1 - Capillaries
    #         1       2
    #xlocs = [ -40300, -43300]
    #ylocs = [ 8500, 8500]
    #names =['E80_T20_S_25C','E50_D50_S_25C']

    # # Rack N2 - Plaques
    #        1                      2                    3                     4                     5                     6                     7                     8                      9  
    # names =['N2_S01_ETTD_m05_n07','N2_S02_ETTD_m05_n08','N2_S03_ETTD_m05_n09','N2_S04_ETTD_m05_n10','N2_S05_ETTD_m06_n00','N2_S06_ETTD_m06_n01','N2_S07_ETTD_m06_n02','N2_S08_ETTD_m06_n03','N2_S09_ETTD_m06_n04',
    #        'N2_S10_ETTD_m06_n05','N2_S11_ETTD_m06_n06','N2_S12_ETTD_m06_n07','N2_S13_ETTD_m06_n08','N2_S14_ETTD_m06_n09','N2_S15_ETTD_m06_n10','N2_S16_ETTD_m07_n00','N2_S17_ETTD_m07_n01','N2_S18_ETTD_m07_n02']

    # # Rack N3 - Plaques
    #         1                     2                     3                     4                     5                     6                     7                     8                     9  
    # names =['N3_S01_ETTD_m07_n03','N3_S02_ETTD_m07_n04','N3_S03_ETTD_m07_n05','N3_S04_ETTD_m07_n06','N3_S05_ETTD_m07_n07','N3_S06_ETTD_m07_n08','N3_S07_ETTD_m07_n09','N3_S08_ETTD_m07_n10','N3_S09_ETTD_m08_n00',
    #         'N3_S10_ETTD_m08_n01','N3_S11_ETTD_m08_n02','N3_S12_ETTD_m08_n03','N3_S13_ETTD_m08_n04','N3_S14_ETTD_m08_n05','N3_S15_ETTD_m08_n06','N3_S16_ETTD_m08_n07','N3_S17_ETTD_m08_n08','N3_S18_ETTD_m08_n09']

    # # Rack N4 - Plaques
    #         1                     2                     3                     4                     5                     6                     7                     8                      9  
    # names =['N4_S01_ETTD_m08_n10','N4_S02_ETTD_m09_n00','N4_S03_ETTD_m09_n01','N4_S04_ETTD_m09_n02','N4_S05_ETTD_m09_n03','N4_S06_ETTD_m09_n04','N4_S07_ETTD_m09_n05','N4_S08_ETTD_m09_n06','N4_S09_ETTD_m09_n07',
    #         'N4_S10_ETTD_m09_n08','N4_S11_ETTD_m09_n09','N4_S12_ETTD_m09_n10','N4_S13_DETT_e00',    'N4_S14_DETT_e01',    'N4_S15_DETT_e02',    'N4_S16_DETT_e03',    'N4_S17_DETT_e04',    'N4_S18_DETT_e05']

    # # Rack N5 - Plaques
    #         1                 2                 3                 4                 5                 6                 7                 8                 9  
    # names =['N5_S01_DETT_e06','N5_S02_DETT_e07','N5_S03_DETT_e08','N5_S04_DETT_e09','N5_S05_DETT_e10','N5_S06_ETRD_R00','N5_S07_ETRD_R01','N5_S08_ETRD_R02','N5_S09_ETRD_R03',
    #         'N5_S10_ETRD_R04','N5_S11_ETRD_R05','N5_S12_ETRD_R06','N5_S13_ETRD_R07','N5_S14_ETRD_R08','N5_S15_ETRD_R09','N5_S16_ETRD_R10','N5_S17_EDPT_R00','N5_S18_EDPT_R01']

    # # Rack N6 - Plaques
    #         1                 2                 3                 4                 5                 6                 7                 8                 9  
    names =['N6_S01_EDPT_R02','N6_S02_EDPT_R03','N6_S03_EDPT_R04','N6_S04_EDPT_R05','N6_S05_EDPT_R06','N6_S06_EDPT_R07','N6_S07_EDPT_R08','N6_S08_EDPT_R09','N6_S09_EDPT_R10',
            'N6_S10_ED',      'N6_S11_EP',      'N6_S12_D7TE',    'N6_S13_D7T3']



    user = 'SL'    
    det_exposure_time(t,t)     
    

    #Check if the length of xlocs, ylocs and names are the same 
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(names)})'
    assert len(xlocs) == len(ylocs), f'Number of X coordinates ({len(xlocs)}) is different from number of samples ({len(ylocs)})'

    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(45.5, 0, 8)
    
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y in zip(names, xlocs, ylocs):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)
            for yy, y_of in enumerate(y_off):        
                yield from bps.mv(piezo.y, y+y_of)
                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x+x_of)
                    xxa = xx+1
                    yya = yy+1 
                    name_fmt = '{sam}_wa{waxs}_loc{xx}{yy}'
                    sample_name = name_fmt.format(sam=sam, xx='%1.1d'%xxa, yy='%1.1d'%yya, waxs='%2.1f'%wa)
                    sample_id(user_name=user, sample_name=sample_name) 
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)
    
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3)


def run_waxs_fastRPI(t=1):

    names = ['TR_ETTD_m03_n05_S_40min_80C_0.5sx8']
    user = 'SL'    
    det_exposure_time(t,t)     
    

    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(45.5, 0, 8)
    

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        name_fmt = '{sam}_wa{waxs}'
        sample_name = name_fmt.format(sam=names[0], waxs='%2.1f'%wa)
        sample_id(user_name=user, sample_name=sample_name) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 




def run_saxs_linkamRPI(t=1):

    names = ['S66_JA-B5O2-24w-1-04']
    user = 'SL'    
    det_exposure_time(t,t)     
    
    y_range = [-4.23, -3.15, 5] 

    # Detectors, motors:
    dets = [pil1M]
    #waxs_range = np.linspace(45.5, 0, 8)
    
    name_fmt = '{sam}'
    sample_name = name_fmt.format(sam=names[0])
    sample_id(user_name=user, sample_name=sample_name) 
    print(f'\n\t=== Sample: {sample_name} ===\n')
    yield from bp.scan(dets, stage.y, *y_range)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 





def run_waxs_fastRPIy(t=1):

    xlocs = [13000,6700,400,-5950,-12400,-18700,-25200,-31600]
    ylocs = [0,0,0,0,0,0,0,0]
    names = ['O134A-1-N','O134A-2-N','O134A-3-N','O134A-4-N','O133A-1-N','O133A-2-N','O133A-3-N','O133A-4-N']

    
    y_off = [8000,7000,6000,5000,4000,3000,2000] 
    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_locs)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(13, 13, 1)
    
    #yield from bps.mv(GV7.open_cmd, 1 )
    #yield from bps.sleep(10)
    #yield from bps.mv(GV7.open_cmd, 1 )
    #yield from bps.sleep(10)
    #yield from bps.mv(GV7.open_cmd, 1 )
    #yield from bps.sleep(10)
    
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y in zip(names, xlocs, ylocs):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)
            for yy, y_of in enumerate(y_off):        
                yield from bps.mv(piezo.y, y+y_of)
            
                name_fmt = '{sam}_wa{waxs}_yloc{yy}'
                sample_name = name_fmt.format(sam=sam, yy='%2.2d'%yy, waxs='%2.1f'%wa)
                sample_id(user_name=user, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3)     
    
    #yield from bps.mv(GV7.close_cmd, 1 )
    #yield from bps.sleep(10)
    #yield from bps.mv(GV7.close_cmd, 1 )
    #yield from bps.sleep(10)
    #yield from bps.mv(GV7.close_cmd, 1 )
    #yield from bps.sleep(10)



def run_waxs_cap_temp(t=1):
    ylocs = [3.9]	# Between 3.1 and 4.1
    name = 'nPEO_isothermal40'
    user = 'DW'    


    det_exposure_time(t,t)         
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 13, 3)
    
    for wa in waxs_range:
        if wa == 0:
            temp = ls.ch1_read.value
        yield from bps.mv(waxs, wa)
        for y in ylocs:
            yield from bps.mv(stage.y, y)
            #temp = ls.ch1_read.value
            name_fmt = '{sam}_wa{waxs}_temp{tem}'
            sample_name = name_fmt.format(sam=name, tem=temp, waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    yield from bps.mv(waxs, 0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 
    




def run_saxs_fastRPI(t=1):

    xlocs = [42500,38300,29300,22900,16400,9000,2500,-3800,-7800,-11800,-15400,-19400,-23200,-27700,-31600,-34900,-38600]
    ylocs = [5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500]
    names = ['BPSAW','FLSAW','DW-01','DW-02','DW-03','DW-04','blank-capillary','mTPSAW','BPSArSA-DMACw','BPSArSA-DMSOW','BPSOArSAW','pTPSAW','XW-1-35-1wd','XW-1-35-2w','XW-1-35-3w','XW-1-35-4w','blankW']   

    user = 'LC_SAXS_ONLY'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M]
    for sam,x, y in zip(names, xlocs, ylocs):
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.x, x)
        name_fmt = '{sam}'
        sample_name = name_fmt.format(sam=sam)
        sample_id(user_name=user, sample_name=sample_name) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 



def run_contRPI(t=1, numb = 100, sleep = 5):

    det_exposure_time(t,t)
    dets = [pil1M,pil300KW]
    #dets = [pil300Kw]
    for i in range(numb):
        yield from bp.count(dets, num=1)
        yield from bps.sleep(sleep)
        
def acq_tem(t = 0.2):
        sam = '0122A-11-lk5.5m-1s'

        dets = [pil1M]
        det_exposure_time(t,t)
        temp = ls.ch1_read.value 
        name_fmt = '{sam}_{temp}C'
        sample_name = name_fmt.format(sam=sam, temp='%4.1f'%temp)
        sample_id(user_name='LC', sample_name=sample_name) 
        yield from bp.scan(dets, stage.y,5.3,5.9, 4)

def acq_bd(t = 0.2):
        sam = '0122A-10-lk5.5m-0.2s-4'

        dets = [pil1M]
        det_exposure_time(t,t)
        temp = ls.ch1_read.value 
        name_fmt = '{sam}_{temp}C'
        sample_name = name_fmt.format(sam=sam, temp='%4.1f'%temp)
        sample_id(user_name='LC', sample_name=sample_name) 
        yield from bp.scan(dets, piezo.th, 0, 0, 1)

#Sample set 1        
#xlocs = [60000,38700,31700,25700,20700,11900,2899,-13100,-28100,-37100,-42099,-35100,-28100,-23000,-16000,-8200,-2200,3800,12800,19800,25800,33800,41800]
#ylocs = [7300,7300,7300,7300,7300,7300,7300,7300,7300,7300,7300,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700]
# names = ['blank','XW-01-033','NF150-1A','NF150-2A','NF150-1B','NF150-2B','DW-13','DW-14','DW-15','DW-nPEO','Blank Kapton','XW-01-40','XW-1-35-4d','XW-1-35-3d','XW-1-35-2d','XW-1-35-1d','Fenton-BPSOArSA','Fenton-BPSArSA','Fenton-mTPSA','Fenton-BPSA','BPSArSA-DMSOd','pTPSAd','FLSAd']



# ylocs = [5000,5000,5000,5000,5000]
 #   xlocs = [29500,23000,16500,9000,2600]
  #  names = ['DW-1','DW-2','DW-3','DW-4','blankcap-1.5-vacuum']

#Sample set 3
# xlocs = [43800,33100,24100,14800,4400,-6900,-16600,-18200,-27400,-28400,-36400,-40400,44800,39800,34800,31800,25800,21800,16800,13000,6800,4000,-2200,-5200,-11200,-14400,-21200,-23400,-31200,-33400,-40000,-43000]
  #  ylocs = [8400,8400,8400,8400,8400,8400,8400,8400,8400,8000,8400,8400,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000]
   # names = ['m-TPN1-11-1','m-TPN1-11-2','m-TPN1-CNC-13','m-TPN1-CNC-14','m-TPN1-CNC-15-5','m-TPN1-CNC-15-m','SP59-1','SP59-2','P59-1','P59-2','828-T3000-PAM-X0.0-1','828-T3000-PAM-X0.0-2','828-T3000-PAM-X0.1-1','828-T3000-PAM-X0.1-2','828-T3000-PAM-X0.3-1','828-T3000-PAM-X0.3-2','828-T3000-PAM-X0.4-1','828-T3000-PAM-X0.4-2','828-T3000-PAM-X0.5-1','828-T3000-PAM-X0.5-2','828-T3000-PAM-X0.6-1','828-T3000-PAM-X0.6-2','828-T3000-PAM-X0.7-1','828-T3000-PAM-X0.7-2','828-T3000-PAM-X0.8-1','828-T3000-PAM-X0.8-2','828-T3000-PAM-X0.9-1','828-T3000-PAM-X0.9-2','828-T3000-PAM-X1.0-1','828-T3000-PAM-X1.0-2']
 
 
#Sample set 4
#names = ['828-T3000-D230-PACM-X0.7-Y0.0-1','828-T3000-D230-PACM-X0.7-Y0.0-2','828-T3000-D230-PACM-X0.7-Y0.1-1','828-T3000-D230-PACM-X0.7-Y0.1-2','828-T3000-D230-PACM-X0.7-Y0.2-1','828-T3000-D230-PACM-X0.7-Y0.2-2','828-T3000-D230-PACM-X0.7-Y0.3-1','828-T3000-D230-PACM-X0.7-Y0.3-2','828-T3000-D230-PACM-X0.7-Y0.4-1','828-T3000-D230-PACM-X0.7-Y0.4-2','828-T3000-D230-PACM-X0.7-Y0.5-1','828-T3000-D230-PACM-X0.7-Y0.5-2','828-T3000-D230-PACM-X0.7-Y0.6-1','828-T3000-D230-PACM-X0.7-Y0.6-2','828-T3000-D230-PACM-X0.7-Y0.7-1','828-T3000-D230-PACM-X0.7-Y0.7-2','828-T3000-D230-PACM-X0.7-Y0.8-1','828-T3000-D230-PACM-X0.7-Y0.8-2','828-T3000-D230-PACM-X0.7-Y0.9-1','828-T3000-D230-PACM-X0.7-Y0.9-2','828-T3000-D230-PACM-X0.7-Y1.0-1','828-T3000-D230-PACM-X0.7-Y1.0-2','828-EK3140-PACM-X0.0-1','828-EK3140-PACM-X0.0-2','828-EK3140-PACM-X0.1-1','828-EK3140-PACM-X0.1-2','828-EK3140-PACM-X0.2-1','828-EK3140-PACM-X0.2-2','828-EK3140-PACM-X0.3-1','828-EK3140-PACM-X0.3-2','828-EK3140-PACM-X0.4-1','828-EK3140-PACM-X0.4-2','828-EK3140-PACM-X0.5-1','828-EK3140-PACM-X0.5-2','828-EK3140-PACM-X0.6-1','828-EK3140-PACM-X0.6-2','828-EK3140-PACM-X0.7-1','828-EK3140-PACM-X0.7-2','828-EK3140-PACM-X0.8-1','828-EK3140-PACM-X0.8-2']

#ylocs =        [8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000] 
   #xlocs = [44000,39800,34800,31500,25800,21800,16800,13000,6800,4000,-2200,-5200,-12200,-14400,-21200,-23400,-31200,-33400,-40000,-43000,44000,39800,34800,31500,25800,21800,16600,13000,6800,4000,-2200,-5200,-12200,-14400,-21200,-23400,-32000,-33400,-40000,-42500]


#Sample set 5
  # ylocs =        [8000,8000,8000,8200,8000,8400,8400,8400,8600,8600,8600,8600,8600,8200,8200,8200,8200,8200,8200,8200,-6600,-6600,-6600,-6600,-6600,-6600,-6600,-6600,-6600,-6600,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000] 
   
  #  xlocs = [43000,41400,34500,32800,26500,22500,17500,14500,7500,3500,-500,-5500,-10500,-14500,-20500,-23500,-29500,-33500,-39500,-42500,44000,41000,36000,33000,27000,23000,18000,14000,8000,4000,0,-6000,-10000,-13500,-20500,-23500,-30500,-32500,-39500,-42500]
   
    #names = ['828-EK3140-PACM-X0.9-1','828-EK3140-PACM-X0.9-2','828-EK3140-PACM-X1.0-1','828-EK3140-PACM-X1.0-2','828-D2000-PACM-X0.6-1','828-D2000-PACM-X0.6-2','828-D2000-PACM-X0.7-1','828-D2000-PACM-X0.7-2','828-D2000-PACM-X0.8-1','828-D2000-PACM-X0.8-2','828-D2000-PACM-X0.9-1','828-D2000-PACM-X0.9-2','828-D2000-PACM-X1.0-1','828-D2000-PACM-X1.0-2','TGPPM-2E1-0.00MDA-1','TGPPM-2E1-0.00MDA-2','TGPPM-2E1-0.25MDA-1','TGPPM-2E1-0.25MDA-2','TGPPM-2E1-0.50MDA-1','TGPPM-2E1-0.50MDA-2','TGPPM-2E1-0.75MDA-1','TGPPM-2E1-0.75MDA-2','TGPPM-2E1-1.00MDA-1','TGPPM-2E1-1.00MDA-2','TCDDA-XDT-1-1','TCDDA-XDT-1-2','TCDDA-XDT-2-1','TCDDA-XDT-2-2','TCDDA-XDT-3-1','TCDDA-XDT-3-2','TCDDA-XDT-4-1','TCDDA-XDT-4-2','TCDDA-XDT-5-1','TCDDA-XDT-5-2','TCDDA-XDT-6-1','TCDDA-XDT-6-2','TCDDA-XDT-7-1','TCDDA-XDT-7-2','TCDDA-XDT-8-1','TCDDA-XDT-8-2']



#Sample set 6-1
#names = [TCDDA-XDT-10-1,TCDDA-XDT-10-2,TCDDA-XDT-11-1,TCDDA-XDT-11-2,TCDDA-XDT-12-1,TCDDA-XDT-12-2,TCDDA-XDT-13-1,TCDDA-XDT-13-2,TCDDA-XDT-14-1,TCDDA-XDT-14-2,TCDDA-XDT-15-1,TCDDA-XDT-15-2,TCDDA-XDT-16-1,TCDDA-XDT-16-2,TCDDA-XDT-17-1,TCDDA-XDT-17-2,TCDDA-XDT-18-1,TCDDA-XDT-18-2,SP-2d-1,SP-2d-2,TCDDA-XDT-9-1,TCDDA-XDT-9-2,SP-1b-1,SP-1b-2,SP-1d-1,SP-1d-2,SP-2b-1,SP-2b-2,SP-3b-1,SP-3b-2,SP-3d-1,SP-3d-2,SP-5b-1,SP-5b-2,SP-6b-1,SP-6b-2,SP-4b-1,SP-4b-2,vacuum-10s]
#ylocs =        [8000,8000,8000,8000,8000,8000,8000,8000,8000,8000,8000,8600,8600,8000,8000,8600,8800,8000,8000,8000,-7000,-6500,-7200,-7200,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-6500,-7200,-7200,-6500] 
   
  #  xlocs = [44000,42000,36000,33000,26000,23000,17000,14000,8000,4000,-1000,-7000,-10000,-15000,-22000,-25000,-30000,-33000,-42000,-43500,45000,42000,36000,34500,29000,27000,22000,20000,12000,10000,4500,3000,-4000,-5500,-13500,-15000,-20000,-21500,-35500]
   
   

#Sample set 6-2
#ylocs=[-6500,-6500,-6500,-6500,-6500,-6500]
#xlocs=[-29500,-33200,-37200,-40200,-41600,-43600]
   # names = ['MP-FLSAW','MP-BPSAW','DW-1','DW-2','DW-3','DW-4']


#ylocs =        [8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400] 
   #xlocs = [44000,39800,34800,31500,25800,21800,16800,13000,6800,4000,-2200,-5200,-12200,-14400,-21200,-23400,-31200,-33400]

