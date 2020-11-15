  

def run_Thomas_temp(t=1,name = 'HarvPoly'): 
    # Slowest cycle:
    x_list  = [13300,  -12100]
    y_list =  [-3400, -3400]
    samples = ['thermal1', 'thermal2']

    # Detectors, motors:
    dets = [pil1M]

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t, t)

    t0 = time.time()
    for i in range(2000):
        t1 = time.time()
        temp = ls.ch1_read.value
        for x, y, names in zip(x_list, y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            
            name_fmt = '{sample}_11.15keV_7.5m_{time}s_{temperature}C_{i}'
            sample_name = name_fmt.format(sample=names, time = '%1.1f'%(t1-t0), temperature='%1.1f'%temp, i = '%3.3d'%i)

            xss = np.linspace(x - 500, x + 500, 3)
            yss = np.linspace(y - 300, y + 300, 3)
            yss, xss = np.meshgrid(yss, xss)
            yss = yss.ravel()
            xss = xss.ravel()
            
            print(f'\n\t=== Sample: {sample_name} ===\n')
            sample_id(user_name=name, sample_name=sample_name) 
            yield from bp.list_scan(dets, piezo.x, xss.tolist() , piezo.y, yss.tolist())

        time.sleep(1800)

    sample_id(user_name='test', sample_name='test')
    