def saxs_waxs_yuchung(t=1):
    dets = [pil300KW, pil1M]

    # waxs_arc = np.linspace(13, 26, 3)

    # yield from bps.mv(stage.y, 0)
    # yield from bps.mv(stage.th, 0)

    # names = ['20H-5', '12H-5', '8H-5', '9010_F1200', '9010_F7200',]
    # x = [-39000, -12500, -2500, 23500, 41500]
    # y = [ 1200,    1200,  1200,  1100,  1300]
    # z = [  1000,   1000,  1000,  1000,  1000]
    # det_exposure_time(t,t) 

    # for wa in waxs_arc:
    #     yield from bps.mv(waxs, wa)    
        
    #     for name, xs, ys, zs in zip(names, x, y, z):
    #         yield from bps.mv(piezo.x, xs)
    #         yield from bps.mv(piezo.y, ys)
    #         yield from bps.mv(piezo.z, zs)

    #         xss = np.linspace(xs - 500, xs + 500, 3)
    #         yss = np.linspace(ys - 500, ys + 500, 51)
    #         yss, xss = np.meshgrid(yss, xss)
    #         yss = yss.ravel()
    #         xss = xss.ravel()

    #         name_fmt = '{sample}_16100eV_sdd8.3_wa{wax}'
    #         sample_name = name_fmt.format(sample=name, wax = wa)
    #         sample_id(user_name='GF', sample_name=sample_name)
    #         print(f'\n\t=== Sample: {sample_name} ===\n')
    #         yield from bp.list_scan(dets, piezo.x, xss.tolist() , piezo.y, yss.tolist())


    waxs_arc = np.linspace(0, 26, 5)

    yield from bps.mv(stage.th, 1.5)
    yield from bps.mv(stage.y, -8)
    names = ['99PL_1PP', '99.75_PLA0.25PP', '75PP25PS']
    x = [-20000, 4000, 21000]
    y = [ -8900,-8900, -9380]
    z = [  3000, 3000,  3000]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        
        for name, xs, ys, zs in zip(names, x, y, z):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            yield from bps.mv(piezo.z, zs)

            xss = np.linspace(xs - 500, xs + 500, 3)
            yss = np.linspace(ys - 500, ys + 500, 51)
            yss, xss = np.meshgrid(yss, xss)
            yss = yss.ravel()
            xss = xss.ravel()

            name_fmt = '{sample}_16100eV_sdd8.3_wa{wax}'
            sample_name = name_fmt.format(sample=name, wax = wa)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.list_scan(dets, piezo.x, xss.tolist() , piezo.y, yss.tolist())



def saxs_waxs_yuchung_2021_1(t=1):
    det_exposure_time(t,t)

    dets = [pil300KW, pil1M]

    waxs_arc = np.linspace(0, 26, 5)


    # names = ['90PP10GNP_245C_F200_core', '90PP10GNP_245C_F200_interface', '90PP10GNP_245C_F400_core', '90PP10GNP_245C_F400_interface', '90PP10GNP_245C_F800_core', '90PP10GNP_245C_F800_interface',
    # '90PP10GNP_245C_F1200_core', '90PP10GNP_245C_F1200_interface', '90PP10GNP_245C_F1600_core', '90PP10GNP_245C_F1600_interface', '90PP10GNP_245C_F2400_core', '90PP10GNP_245C_F2400_interface',
    # '90PP10GNP_245C_F3200_core', '90PP10GNP_245C_F3200_interface', '90PP10GNP_245C_F3600_core', '90PP10GNP_245C_F3600_interface', '90PP10GNP_230C_F200_core', '90PP10GNP_230C_F200_interface',
    # '90PP10GNP_230C_F400_core', '90PP10GNP_230C_F400_interface', '90PP10GNP_230C_F800_core', '90PP10GNP_230C_F800_interface', '90PP10GNP_230C_F1200_core', '90PP10GNP_230C_F1200_interface',
    # '90PP10GNP_230C_F1600_core', '90PP10GNP_230C_F1600_interface', '90PP10GNP_230C_F2400_core', '90PP10GNP_230C_F2400_interface', '90PP10GNP_230C_F3200_core', '90PP10GNP_230C_F3200_interface', 
    # '90PP10GNP_230C_F3600_core', '90PP10GNP_230C_F3600_interface', '90PP10GNP_200C_F200_core', '90PP10GNP_200C_F200_interface', '90PP10GNP_200C_F400_core', '90PP10GNP_200C_F400_interface',
    # '90PP10GNP_200C_F800_core', '90PP10GNP_200C_F800_interface', '90PP10GNP_200C_F1200_core', '90PP10GNP_200C_F1200_interface', '90PP10GNP_200C_F1600_core', '90PP10GNP_200C_F1600_interface',
    # '90PP10GNP_200C_F2400_core', '90PP10GNP_200C_F2400_interface', '90PP10GNP_200C_F3200_core', '90PP10GNP_200C_F3200_interface', '90PP10GNP_200C_F3600_core', '90PP10GNP_200C_F3600_interface']

    # x = [-34000, -34000, -34000, -34000, -34000, -34000, -34000, -34000, -34000, -34000, 
    # -14000, -14000, -14000, -14000, -14000, -14000, -14000, -14000, -14000, -14000,
    #   5000,   5000,   5000,   5000,   5000,   5000,   5000,   5000,   5000,   5000,
    #  24000,  24000,  24000,  24000,  24000,  24000,  24000,  24000,  24000,  24000,  
    #  45000,  45000,  45000,  45000,  45000,  45000,  45000,  45000]

    # y = [  8600,   8600,   4400,   4000,    700,    400,  -3000,  -3500,   -6900,  -6700, 
    #   9450,   9300,   6450,   6050,   1750,   1450,  -2650,  -2850,  -6500,  -6700,
    #   8550,   8350,   4150,   3950,   -100,   -300,  -5100,  -5400,  -9300,  -9050, 
    #   9450,   9300,   5800,   5500,   1200,    800,  -3250,  -3500,  -8950,  -8700,
    #   9100,   8850,   3150,   2850,  -1450,  -1750,  -7100,  -6850]

    # names = ['95PP5GNP_230C_F200_core', '95PP5GNP_230C_F200_interface', '95PP5GNP_230C_F400_core', '95PP5GNP_230C_F400_interface', '95PP5GNP_230C_F800_core', '95PP5GNP_230C_F800_interface', 
    #     '95PP5GNP_230C_F1200_core', '95PP5GNP_230C_F1200_interface', '95PP5GNP_230C_F1600_core', '95PP5GNP_230C_F1600_interface', '95PP5GNP_230C_F2400_core', '95PP5GNP_230C_F2400_interface', 
    #     '95PP5GNP_230C_F3200_core', '95PP5GNP_230C_F3200_interface', '95PP5GNP_230C_F3600_core', '95PP5GNP_230C_F3600_interface', '99PP1GNP_200C_F200_core', '99PP1GNP_200C_F200_interface', 
    #     '99PP1GNP_200C_F400_core', '99PP1GNP_200C_F400_interface', '99PP1GNP_200C_F800_core', '99PP1GNP_200C_F800_interface', '99PP1GNP_200C_F1200_core','99PP1GNP_200C_F1200_interface',
    #     '99PP1GNP_200C_F1600_core', '99PP1GNP_200C_F1600_interface', '99PP1GNP_200C_F2400_core', '99PP1GNP_200C_F2400_interface', '99PP1GNP_200C_F3200_core', '99PP1GNP_200C_F3200_interface',
    #     '99PP1GNP_200C_F3600_core', '99PP1GNP_200C_F3600_interface', '80PP20GNP_230C_F200_core', '80PP20GNP_230C_F200_interface', '80PP20GNP_230C_F400_core', '80PP20GNP_230C_F400_interface', 
    #     '80PP20GNP_230C_F800_core', '80PP20GNP_230C_F800_interface', '80PP20GNP_230C_F1200_core', '80PP20GNP_230C_F1200_interface', '80PP20GNP_230C_F1600_core', '80PP20GNP_230C_F1600_interface',
    #     '80PP20GNP_230C_F2400_core', '80PP20GNP_230C_F2400_interface','80PP20GNP_230C_F3200_core', '80PP20GNP_230C_F3200_interface', '80PP20GNP_230C_F3600_core', '80PP20GNP_230C_F3600_interface']

    # x = [   -42000, -42000, -42000, -42000, -42000, -42000, -42000, -42000, -42000, -42000, 
    # -22000, -22000, -22000, -22000, -22000, -22000, -22000, -22000, -22000, -22000,
    #   1000,   1000,   1000,   1000,   1000,   1000,   1000,   1000,   1000,   1000,   1000,  1000,
    #  22000,  22000,  22000,  22000,  22000,  22000,  22000,  22000,  22000,  22000,  
    #  45000,  45000,  45000,  45000,  45000,  45000]

    # y = [     6700,   6500,   3450,   3150,  -1250,  -1450,  -5350,  -5150,  -9350,  -9150, 
    #   7250,   6950,   3100,   2750,   -650,   -850,  -4550,  -4850,  -8950,  -8750,
    #   6850,   6450,   3000,   2700,    250,     50,  -4150,  -4450,  -6750,  -6950,  -9700,  -9400,
    #   8200,   8000,   3300,   3000,   -750,  -1000,  -4800,  -5000,  -9300,  -9100,
    #   6700,   6500,   2700,   2450,  -2100,  -2400]


    # names = ['99PLA1nwFe_230C_F200_core', '99PLA1nwFe_230C_F200_interface', '99PLA1nwFe_230C_F400_core', '99PLA1nwFe_230C_F400_interface', '99PLA1nwFe_230C_F800_core',
    # '99PLA1nwFe_230C_F800_interface', '99PLA1nwFe_230C_F1200_core', '99PLA1nwFe_230C_F1200_interface', '99PLA1nwFe_230C_F1600_core', '99PLA1nwFe_230C_F1600_interface',
    # '99PLA1nwFe_230C_F3200_core', '99PLA1nwFe_230C_F3200_interface', '95PP5GNP_200C_F200_core', '95PP5GNP_200C_F200_interface',
    # '95PP5GNP_200C_F400_core', '95PP5GNP_200C_F400_interface', '95PP5GNP_200C_F800_core', '95PP5GNP_200C_F800_interface', '95PP5GNP_200C_F1200_core', '95PP5GNP_200C_F1200_interface',
    # '95PP5GNP_200C_F1600_core', '95PP5GNP_200C_F1600_interface', '95PP5GNP_200C_F2400_core', '95PP5GNP_200C_F2400_interface', '95PP5GNP_200C_F3200_core', '95PP5GNP_200C_F3200_interface',
    # '95PP5GNP_200C_F3600_core', '95PP5GNP_200C_F3600_interface', '99PP1GNP_200C_F200_core', '99PP1GNP_200C_F200_interface', '99PP1GNP_200C_F400_core', '99PP1GNP_200C_F400_interface',
    # '99PP1GNP_200C_F800_core', '99PP1GNP_200C_F800_interface', '99PP1GNP_200C_F1200_core', '99PP1GNP_200C_F1200_interface', '99PP1GNP_200C_F1600_core', '99PP1GNP_200C_F1600_interface',
    # '99PP1GNP_200C_F2400_core', '99PP1GNP_200C_F2400_interface', '99PP1GNP_200C_F3200_core', '99PP1GNP_200C_F3200_interface', '99PP1GNP_200C_F3600_core', '99PP1GNP_200C_F3600_interface',
    # '80PP20GNP_245C_F200_core', '80PP20GNP_245C_F200_interface', '80PP20GNP_245C_F400_core', '80PP20GNP_245C_F400_interface', '80PP20GNP_245C_F800_core', '80PP20GNP_245C_F800_interface',
    # '80PP20GNP_245C_F1200_core', '80PP20GNP_245C_F1200_interface', '80PP20GNP_245C_F1600_core', '80PP20GNP_245C_F1600_interface', '80PP20GNP_245C_F2400_core', '80PP20GNP_245C_F2400_interface']




    # x = [   -42000, -42000, -42000, -42000, -42000, -42000, -42000, -42000, -42000, -42000, -42000, -42000,
    # -22000, -22000, -22000, -22000, -22000, -22000, -22000, -22000, -22000, -22000, -22000, -22000,
    #   1000,   1000,   1000,   1000,   1000,   1000,   1000,   1000,   1000,   1000,   1000,  1000,
    #  21000,  21000,  21000,  21000,  21000,  21000,  21000,  21000, 
    #  44000,  44000,  44000,  44000,  44000,  44000,  44000,  44000,  44000,  44000,  44000,  44000]

    # y = [     7500,   7200,   4900,   4700,   600,    350,  -3100,  -2900,  -5900,  -6100,  -9600,  -9800,
    #   8500,   8300,   6000,   5700,   1800,  1600,  -1900,  -2100,  -5800,  -5700,  -7900,  -8300,
    #   8500,   8300,   6000,   5750,   2100,  1800,   -900,  -1100,  -4700,  -4950,  -8600,  -8900,
    #   8100,   7900,   5000,   4800,   1700,  1500, -1200,  -1500, 
    #   8000,   7700,   4600,   4400,   1700,  1500, -1400,  -1600,   -5300,  -5500,  -8800,  -9100]



    names = ['80PP20GNP_245C_F3200_core', '80PP20GNP_245C_F3200_interface', '80PP20GNP_245C_F3600_core', '80PP20GNP_245C_F3600_interface',
    'PLAPBATGNP_8H5', 'PLAPBATGNP_12H5', 'PLAPBATGNP_16H5', 'PLAPBATGNP_20H5',
    'PLAPBATGNP_8H5_M', 'PLAPBATGNP_12H5_M', 'PLAPBATGNP_16H5_M', 'PLAPBATGNP_20H5_M',
    'PLA_M', 'PBAT_M', 'PLAPBAT_M']

    x = [   -15000, -15000, -15000, -15000,
              4000,   4000,   4000,   4000,
             24000,  24000,  24000,  24000,   
             45000,  45000,  45000]

    y = [     6050,   5800,   1600,   1850,
              7500,   4100,   -400,  -7400,
              8100,   5600,    100,  -5900,
              7600,    100,  -4900]

    assert len(x) == len(names), f'Number of X coordinates ({len(x)}) is different from number of samples ({len(names)})'
    assert len(x) == len(y), f'Number of X coordinates ({len(x)}) is different from number of y ({len(y)})'


    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)
            yield from bps.sleep(2)

            name_fmt = '{sample}_16100eV_sdd8.3_wa{wax}'
            sample_name = name_fmt.format(sample=name, wax = wa)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            # yield from bp.list_scan(dets, piezo.x, xss.tolist() , piezo.y, yss.tolist())
            yield from bp.count(dets)




def saxs_waxs_yuchung_2021_2(name='test', t=0.5):

    det_exposure_time(t,t)
    dets = [pil300KW, pil1M]
    waxs_arc = np.linspace(0, 26, 5)

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        
        name_fmt = '{sample}_full_16.1keV_sdd7m_wa{wax}'
        sample_name = name_fmt.format(sample=name, wax = wa)
        sample_id(user_name='YC', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)
    
    det_exposure_time(0.3, 90)
    yield from bps.mv(waxs, 7)    


def y_scan_yuchung_2021_2(name = 'test', t=0.5):

    det_exposure_time(t,t)
    dets = [pil300KW, pil1M]
        
    name_fmt = '{sample}_scany_16.1keV_sdd7m_wa{wax}'
    sample_name = name_fmt.format(sample=name, wax = '7')
    sample_id(user_name='YC', sample_name=sample_name)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    yield from bp.scan(dets, stage.y, 7.1, 10, 581)

    det_exposure_time(0.5, 0.5)
    yield from bps.mv(waxs, 7)