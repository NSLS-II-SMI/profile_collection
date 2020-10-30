def ex_situ_hardxray(t=1):
    # samples = ['PLA2','PLA1','CON6','CON5', 'CON4','CON3','CON2','CON1',
    # '05_Ca_1', '05_Ca_2', '05_UT_1', '05_UT_2', 'PLA6','PLA4','PLA3',
    # ]

    # samples = ['B5_1','B5_2','B5_3', 'B6_1','B6_2','B6_3','B7_1','B7_2','B7_3','B12_1','B12_2','B12_3']
    # x_list  = [45550, 41200, 35600, 25600, 20900, 15400, -1900, -7900, -14000, -24100, -28200, -32700, ]
    # y_list =  [-9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300]

    # samples = ['A1_1','A1_2','A1_3', 'A1_4','A2_5','A2_6','A2_7','A2_8','A3_9','A3_10','A3_11','A3_12','A3_13','A3_14','A4_15', 'A4_16', 'A4_17', 'A4_19']
    # x_list  = [45950, 43250, 37250, 31650, 24400, 18850, 12500, 8000, -3400, -7300, -11300, -16800, -20900, -26400, -33000,  -37400, -41900, -45200]
    # y_list =  [3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,   3500,   3500,    3500, 3500, 3500, 3500]

    # samples = ['C8_32', 'C8_33', 'C8_34', 'C8_35', 'C9_36', 'C9_37', 'C9_38', 'C9_39', 'C10_40', 'C10_41', 'C10_42', 'C10_43',
    # 'C10_44', 'C10_45', 'C11_46', 'C11_47', 'C11_48', 'C11_49', 'C11_50']
    # x_list  = [43700, 38300, 34000, 27800, 20900, 16200, 12100, 7100, -2700, -6700, -10500, -15700, -20000,
    # -24200, -29300, -32700, -36700, -41000, -45000]
    # y_list =  [3700,  3700,  3700,  3700,  3700,  3700,  3700,  3700, 3700,  3700,  3700,   3700,   3700,
    # 3700,   3700,    3700,   3700,  3700,  3700]
    

    samples = ['D13_51','D13_52','D13_53','D14_54','D14_55','D14_56','D15_57','D15_58','D15_59','D16_60','D16_61','D16_62','D16_63','D16_64',
    'D17_65','D17_66','D17_67']
    x_list  = [43700, 38400, 34000, 25200, 20000, 15400, 6700,  2500,  -2300, -6800, -14000, -19000, -23300, -28500,
    -34700, -39300, -43600]
    y_list =  [-9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880,  -9880,  -9880,  -9880,
    -9880, -9880, -9880]



    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(13, 0, 3)
    
    ypos = [0, 400, 3]    
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'

    det_exposure_time(t,t)

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y in zip(samples, x_list, y_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            
            name_fmt = '{sam}_wa{waxs}'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name='OS', sample_name=sample_name) 
            yield from bp.rel_scan(dets, piezo.y, *ypos)
            
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)




def ex_situ_hardxray_2020_3(t=1):
    yield from bps.mv(stage.y, 0)
    yield from bps.mv(stage.th, 0)
    samples = ['F22_83','F22_84','F22_85','F23_86','F23_87','F23_88','F24_89','F24_90','F24_91','F24_92','F24_93','F24_94','F25_95','F25_96','F25_97','F25_98']
    x_list  = [45100, 38750, 33500, 26450, 21600, 17300,  7800,  3600, -2300, -7800, -13400, -18500, -28800, -32400, -36700, -42500]
    y_list =  [-1500, -1500, -1500, -1500, -1500, -1500, -1500, -1500, -1500, -1500,  -1500,  -1500,  -1500,  -1500,  -1500,  -1500]
    z_list =  [ 2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,   2700,   2700,   2700,   2700,   2700,   2700]


    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 32.5, 6)
    
    ypos = [0, 400, 3]    
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'

    det_exposure_time(t,t)

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z in zip(samples, x_list, y_list, z_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            name_fmt = '{sam}_wa{waxs}'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name='OS', sample_name=sample_name) 
            yield from bp.rel_scan(dets, piezo.y, *ypos)
            
    sample_id(user_name='test', sample_name='test')
    # det_exposure_time(0.3,0.3)

    yield from bps.mv(stage.th, 1.5)
    yield from bps.mv(stage.y, -11)
    samples = ['E18_67','E18_68','E18_69','E19_70','E19_71','E19_72','E19_73','E19_74','E19_75','E20_76','E20_77','E20_78','E21_79','E21_80','E21_81','E22_82']
    x_list  = [43500, 37500, 32100, 23600, 18350, 13000,  7200,  3300,  -450, -9400, -14300, -19400, -25900, -31300, -36200, -43200]
    y_list =  [-9700, -9700, -9700, -9700, -9700, -9700, -9700, -9700, -9700, -9700,  -9700,  -9700,  -9700,  -9700,  -9700,  -9700]
    z_list =  [ 4200,  4200,  4200,  4200,  4200,  4200,  4200,  4200,  4200,  4200,   4200,   4200,   4200,   4200,   4200,   4200]

    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 32.5, 6)
    
    ypos = [0, 400, 3]    
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'

    det_exposure_time(t,t)

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z in zip(samples, x_list, y_list, z_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            name_fmt = '{sam}_16.1keV_wa{waxs}'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name='OS', sample_name=sample_name) 
            yield from bp.rel_scan(dets, piezo.y, *ypos)
            
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def ex_situ_hardxray_josh(t=1):
    
    yield from bps.mv(stage.th, 2.5)
    yield from bps.mv(stage.y, -12)
    samples = ['J01', 'J02', 'J03', 'J04', 'J05', 'J06', 'J07', 'J08', 'J09', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20']
    x_list  = [44000, 40000, 36500, 32600, 26850, 22800, 18700, 14700, 9250,  4850,  1100,  -3200, -9100, -12000, -15600, -18900, -23150, -26150, -29600, -32700]
    y_list =  [-9000, -9000, -9000, -9000, -9000, -9000, -9000, -9000, -9000, -9000, -9000, -9000, -9000, -9000,  -9000, -9000 , -9000 , -9000 , -9000 , -9000]
    z_list =  [2000,  2000,  2000,  2000,  2000,  2000,  2000,  2000,  2000,  2000,  2000,  2000,  2000,  2000,   2000,   2000,  2000,   2000,   2000,   2000]

    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(19.5, 0, 4)
    
    ypos = [0, 400, 3]    
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'

    det_exposure_time(t,t)

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z in zip(samples, x_list, y_list, z_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            name_fmt = '{sam}_wa{waxs}'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name='JDM', sample_name=sample_name) 
            yield from bp.rel_scan(dets, piezo.y, *ypos)
            
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)

    yield from bps.mv(stage.th, 2.5)
    yield from bps.mv(stage.y, -5)
    samples = ['K01', 'K02', 'K03', 'K04', 'K05', 'K06', 'K07', 'K08', 'K09', 'K10', 'K11', 'K12']
    x_list  = [44100, 39400, 34400, 29400, 24000, 20300, 17250, 12900, 10100,  2000, -4000, -7250]
    y_list =  [3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500]
    z_list =  [4000,  4000,  4000,  4000,  4000,  4000,  4000,  4000,  4000,  4000,  4000,  4000]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y, z in zip(samples, x_list, y_list, z_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            name_fmt = '{sam}_wa{waxs}'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name='JDM', sample_name=sample_name) 
            yield from bp.rel_scan(dets, piezo.y, *ypos)
            
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)



def run_saxs_nexafs(t=1):
    # yield from saxs_prep_multisample(t=0.5)
    # yield from bps.sleep(10)
    yield from nexafs_prep_multisample(t=0.5)


def nexafs_prep_multisample(t=1):

    yield from bps.mv(stage.th, 2.5)
    yield from bps.mv(stage.y, -13.5)

    samples = ['SA1','Na1','PL_Ca','PGA','PGA_CA','Si3N4_empty']
    x_list  = [9000, -13200,-29100,-34400,-39400,-44500]
    y_list =  [-8500, -8500, -8800, -8700, -8800, -8700]

    
    # samples = ['F22_83','F22_84','F22_85','F23_86','F23_87','F23_88','F24_89','F24_90','F24_91','F24_92','F24_93','F24_94','F25_95','F25_96','F25_97','F25_98']
    # x_list  = [44300, 38000, 32700, 25700, 20850, 16500, 6900, 2900, -3100, -8500, -14150, -19200, -29550, -33150, -37450, -43300]
    # y_list =  [-9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880,  -9880,  -9880,  -9880, -9880, -9880]

    # samples = ['D13_51','D14_54', 'D15_57','D15_58','D15_59','D16_60','D17_65']
    # x_list  = [43700, 25200, 6700,  2500,  -2300, -6800, -34700]
    # y_list =  [-9880, -9880, -9880, -9880, -9880, -9880, -9880]
    
    # samples = ['B7_1','B7_2','B12_1','B12_2']
    # x_list  = [ -1900, -7900, -24100, -28200]
    # y_list =  [-9300, -9300, -9300, -9300]

    for x, y, name in zip(x_list, y_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)

        yield from NEXAFS_Ca_edge_multi(t=t, name=name)
    

    yield from bps.mv(stage.th, 2.5)
    yield from bps.mv(stage.y, -5.5)

    samples = ['G26_99','G26_100','G26_101','G27_102','G27_103','G27_104','G27_105','G27_106','G27_107','G28_108',
    'G28_109','G28_110', 'O8_Ca', 'O8_3']
    x_list  = [45300,39600,33900,24300,19400,15900,11400,7600,2100,-9600,-17100,-23700, -34700,-40700]
    y_list =  [4100, 4100, 4100, 4100, 4100, 4100, 4100, 4100,4100, 4100, 4100,  4100,  4100,  4100]

    # samples = ['E18_67','E18_68','E18_69','E19_70','E19_71','E19_72','E19_73','E19_74','E19_75','E20_76','E20_77','E20_78','E21_79','E21_80','E21_81','E22_82',]
    # x_list  = [43300, 37300, 31700, 23200, 18000, 12700, 6900, 3000, -800, -9800, -14600, -19600, -26200, -31700, -36500, -43500 ]
    # y_list =  [3900,  3900,  3900,  3900,  3900,  3900,  3900,  3900, 3900,  3900,  3900, 3900, 3900, 3900, 3900, 3900]

    # samples = ['C8_32', 'C9_36', 'C10_40', 'C11_46']
    # x_list  = [43700, 20900, -2700, -29300]
    # y_list =  [3700,  3700,  3700,  3700]

    # samples = ['A1_1','A1_2','A2_5','A2_6','A3_9','A3_10','A4_15', 'A4_16']
    # x_list  = [45950, 43250, 24400, 18850, -3400, -7300, -33000,  -37400]
    # y_list =  [3500,  3500, 3500,  3500, 3500,  3500,  3500, 3500]

    for x, y, name in zip(x_list, y_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from NEXAFS_Ca_edge_multi(t=t, name=name)

    sample_id(user_name='test', sample_name='test')



def saxs_prep_multisample(t=1):
    dets = [pil300KW, pil1M]

    energies = np.arange(4030, 4040, 5).tolist() + np.arange(4040, 4060, 0.5).tolist() + np.arange(4060, 4080, 2).tolist()+ np.arange(4100, 4150, 5).tolist()
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_pos{posi}_wa{wa}_xbpm{xbpm}'
    waxs_range = [0, 6.5, 13.0, 19.5, 26, 32.5]

    det_exposure_time(t,t)

    ypos = [0, 400, 3]    
    for wa in waxs_range[::-1]:
        yield from bps.mv(waxs, wa)
        yield from bps.mv(stage.th, 2.5)
        yield from bps.mv(stage.y, -13.5)

        samples = ['ut', 'Ca', 'CH']
        x_list  = [45500,38500,31500]
        y_list =  [-8500,-8500,-8500]

        for name, x, y in zip(samples, x_list, y_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for k, e in enumerate(energies):                              
                yield from bps.mv(energy, e)
                name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.rel_scan(dets, piezo.y, *ypos)
                            

            yield from bps.mv(energy, 4050)
            yield from bps.mv(energy, 4030)


    dets = [pil300KW, pil1M]

    energies = [4030, 4040, 4050, 4055, 4075]
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_pos{posi}_wa{wa}_xbpm{xbpm}'
    waxs_range = [0, 6.5, 13.0, 19.5, 26, 32.5, 39.0, 45.5]
    #waxs_range = [0, 6.5, 13.0, 19.5]


    det_exposure_time(t,t)

    ypos = [0, 800, 3]    
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        yield from bps.mv(stage.th, 2.5)
        yield from bps.mv(stage.y, -13.5)

        samples = ['ut', 'Ca', 'CH', 'AC1','AC2','AC3','SA1','SA2','SA3','Na1','Na2','Na3','PL_Ca','PGA','PGA_CA','Si3N4_empty']
        x_list  = [45500,38500,31500,25500,21000,16000, 9000, 3000,-4000,-13200,-18400,-23600,-29100,-34400,-39400,-44500]
        y_list =  [-8500,-8500,-8500,-8500,-8500,-8500,-8500,-8500,-8500, -8500, -9100, -9000, -8800, -8700, -8800, -8700]


        # samples = ['F22_83','F22_84','F22_85','F23_86','F23_87','F23_88','F24_89','F24_90','F24_91','F24_92','F24_93','F24_94','F25_95','F25_96','F25_97','F25_98']
        # x_list  = [44300, 38000, 32700, 25700, 20850, 16500, 6900, 2900, -3100, -8500, -14150, -19200, -29550, -33150, -37450, -43300]
        # y_list =  [-9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880,  -9880,  -9880,  -9880, -9880, -9880]

        # samples = ['D13_51','D13_52','D13_53','D14_54','D14_55','D14_56','D15_57','D15_58','D15_59','D16_60','D16_61','D16_62','D16_63','D16_64','D17_65',
        # 'D17_66','D17_67']
        # x_list  = [43700, 38400, 34000, 25200, 20000, 15400, 6700,  2500,  -2300, -6800, -14000, -19000, -23300, -28500, -34700, -39300, -43600]
        # y_list =  [-9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880, -9880,  -9880,  -9880,  -9880, -9880, -9880, -9880]

        # samples = ['B5_1','B5_2','B5_3', 'B6_1','B6_2','B6_3','B7_1','B7_2','B7_3','B12_1','B12_2','B12_3']
        # x_list  = [45550, 41200, 35600, 25600, 20900, 15400, -1900, -7900, -14000, -24100, -28200, -32700, ]
        # y_list =  [-9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300, -9300]

        for name, x, y in zip(samples, x_list, y_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for k, e in enumerate(energies):                              
                yield from bps.mv(energy, e)
                name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.rel_scan(dets, piezo.y, *ypos)
                            

            yield from bps.mv(energy, 4050)
            yield from bps.mv(energy, 4030)

        yield from bps.mv(stage.th, 2.5)
        yield from bps.mv(stage.y, -5.5)

        samples = ['G26_99','G26_100','G26_101','G27_102','G27_103','G27_104','G27_105','G27_106','G27_107','G28_108',
        'G28_109','G28_110', 'O8_Ca', 'O8_3']
        x_list  = [45300,39600,33900,24300,19400,15900,11400,7600,2100,-9600,-17100,-23700, -34700,-40700]
        y_list =  [4100, 4100, 4100, 4100, 4100, 4100, 4100, 4100,4100, 4100, 4100,  4100,  4100,  4100]

        # samples = ['E18_67','E18_68','E18_69','E19_70','E19_71','E19_72','E19_73','E19_74','E19_75','E20_76','E20_77','E20_78','E21_79','E21_80','E21_81','E22_82',]
        # x_list  = [43300, 37300, 31700, 23200, 18000, 12700, 6900, 3000, -800, -9800, -14600, -19600, -26200, -31700, -36500, -43500 ]
        # y_list =  [3900,  3900,  3900,  3900,  3900,  3900,  3900,  3900, 3900,  3900,  3900, 3900, 3900, 3900, 3900, 3900]

        # samples = ['C8_32', 'C8_33', 'C8_34', 'C8_35', 'C9_36', 'C9_37', 'C9_38', 'C9_39', 'C10_40', 'C10_41', 'C10_42', 'C10_43',
        # 'C10_44', 'C10_45', 'C11_46', 'C11_47', 'C11_48', 'C11_49', 'C11_50']
        # x_list  = [43700, 38300, 34000, 27800, 20900, 16200, 12100, 7100, -2700, -6700, -10500, -15700, -20000, -24200, -29300, -32700, -36700, -41000, -45000]
        # y_list =  [3700,  3700,  3700,  3700,  3700,  3700,  3700,  3700, 3700,  3700,  3700,   3700,   3700, 3700,   3700,    3700,   3700,  3700,  3700]
        
        # samples = ['A1_1','A1_2','A1_3', 'A1_4','A2_5','A2_6','A2_7','A2_8','A3_9','A3_10','A3_11','A3_12','A3_13','A3_14','A4_15', 'A4_16', 'A4_17', 'A4_19']
        # x_list  = [45950, 43250, 37250, 31650, 24400, 18850, 12500, 8000, -3400, -7300, -11300, -16800, -20900, -26400, -33000,  -37400, -41900, -45200]
        # y_list =  [3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,  3500,   3500,   3500,    3500, 3500, 3500, 3500]

        for name, x, y in zip(samples, x_list, y_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for k, e in enumerate(energies):                              
                yield from bps.mv(energy, e)
                name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.rel_scan(dets, piezo.y, *ypos)
                            
            yield from bps.mv(energy, 4050)
            yield from bps.mv(energy, 4030)
            

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)




def NEXAFS_Ca_edge_multi(t=0.5, name='test'):
    yield from bps.mv(att2_11, 'Retract')
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(1)
    yield from bps.mv(att2_11, 'Retract')
    yield from bps.mv(GV7.close_cmd, 1 )

    yield from bps.mv(waxs, 52)
    # dets = [pil300KW, amptek]
    
    dets = [pil300KW]

    energies = np.linspace(4030, 4150, 121)

    det_exposure_time(t,t) 
    name_fmt = 'nexafs_{sample}_{energy}eV_xbpm{xbpm}'
    for e in energies:                              
        yield from bps.mv(energy, e)
        sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
        RE.md['filename_amptek'] = sample_name
        sample_id(user_name='OS', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)

    yield from bps.mv(energy, 4125)
    yield from bps.mv(energy, 4100)        
    yield from bps.mv(energy, 4075)
    yield from bps.mv(energy, 4050)
    yield from bps.mv(energy, 4030)

    sample_id(user_name='test', sample_name='test')

    yield from bps.mv(att2_11, 'Insert')
    yield from bps.mv(GV7.open_cmd, 1 )
    yield from bps.sleep(1)
    yield from bps.mv(att2_11, 'Insert')
    yield from bps.mv(GV7.open_cmd, 1 )
