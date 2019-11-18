
def run_simple(exp=0.05, t=10):
    name = 'JW'
    sample = 'recheck_90c_0.1mms'
    pil1M.cam.file_path.put(f"/ramdisk/images/users/2019_3/304549_Headrick/1M/%s"%sample)
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/2019_3/304549_Headrick2/300KW/%s"%sample)
    name_fmt = '{samp}_{temperature}C'
    temp = ls.ch1_read.value
    det_exposure_time(exp, t)
    sample_name = name_fmt.format(samp = sample, temperature=temp)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name)
    yield from bps.mv(waxs, 12) 
    yield from bp.count([pil1M, pil300KW], num = 1)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)

def run_fullgiwaxs(t=0.5):
    name = 'JW'
    sample = 'recheck_90c_0.1mms'
    pil1M.cam.file_path.put(f"/ramdisk/images/users/2019_3/304549_Headrick/1M/%s"%sample)
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/2019_3/304549_Headrick2/300KW/%s"%sample)
    waxs_range = [0, 19.5, 4] #up to 3.2 A-1
    #waxs_range = [0, 13, 3] #up to 2.3 A-1
    name_fmt = '{samp}_{temperature}C'
    temp = ls.ch1_read.value
    det_exposure_time(t, t)
    sample_name = name_fmt.format(samp = sample, temperature=temp)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name) 
    yield from bp.scan([pil1M, pil300KW], waxs, *waxs_range)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)

def run_BD(t=0.2):
    num = 300
    name = 'JW'
    sample = '60c_0.2mms'
    pil1M.cam.file_path.put(f"/ramdisk/images/users/2019_3/304549_Headrick/1M/%s"%sample)
    pil300KW.cam.file_path.put(f"/GPFS/xf12id1/data/images/users/2019_3/304549_Headrick/300KW/%s"%sample)
    name_fmt = '{samp}_{temperature}C'
    temp = ls.ch1_read.value
    det_exposure_time(t, t)
    yield from bps.mv(waxs, 12) 
    sample_name = name_fmt.format(samp = sample, temperature=temp)
    print(f'\n\t=== Sample: {sample_name} ===\n')
    sample_id(user_name=name, sample_name=sample_name) 
    yield from bp.count([pil300KW, pil300kwroi2, pil300kwroi3, pil300kwroi4], num=num)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)



