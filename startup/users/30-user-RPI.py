


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


def run_waxs_fastRPI(t=1):
    xlocs = [42200,38200,35700,33200,29200,27200,23200,19200,13800,9200,3200,-2600,-7800,-12800,-18800,-26800,-30800,-36800,-40800,-44800]
    ylocs = [9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000,9000]
    names = ['SL-PS3','SL-PS3_98_8_PS33','SL-PS3_97_0_PS33','SL-PS3_94_9_PS33','SL-blank','SL-PS3_93_0_PS33','SL-PS3_89_9_PS33','SL-PS3_79_8_PS33','SL-PS3_70_1_PS33','SL-PS3_60_0_PS33','SL-PS3_49_9_PS33','SL-PS3_40_0_PS33','SL-PS3_29_8_PS33','SL-PS3_20_1_PS33','SL-PS3_10_0_PS33','SL-PS3_7_0_PS33','SL-PS3_4_9_PS33','SL-PS3_3_0_PS33','SL-PS33','SL-PS148']
    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 32.5, 6)
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam,x, y in zip(names, xlocs, ylocs):
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.x, x)
            name_fmt = '{sam}_wa{waxs}deg'
            sample_name = name_fmt.format(sam=sam, waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 

def run_saxs_fastRPI(t=1):
    xlocs = [44000]
    ylocs = [-7000]
    names = ['LC-SNL-4']
    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M]
    for sam,x, y in zip(names, xlocs, ylocs):
        yield from bps.mv(piezo.y, y+200)
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
        time.sleep(sleep)

