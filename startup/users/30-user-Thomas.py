  

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
    



def saxs_cryo(t=0.5, tem = 25, num_max = 100):
    global num
    # Slowest cycle:
    name = 'ET'
    # Detectors, motors:
    dets = [pil300KW, pil1M]
    # sample = 'PDMS_sdd8.3m'
    sample = 'bkg_sdd8.3m'

    waxs_range = np.linspace(0, 13, 3)


    det_exposure_time(t,t)

    
    while num < num_max:
        yield from bps.mvr(stage.y, 0.02)
        num +=1
        if waxs.arc.position > 7:
            waxs_ran = waxs_range[::-1]
        else:
            waxs_ran = waxs_range


        for wa in waxs_ran:
            yield from bps.mv(waxs, wa)
            name_fmt = 'num{nu}_{temperature}C_wa{wa}'
            sample_name = name_fmt.format(nu = num, temperature='%4.2f'%tem, wa=wa)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            sample_id(user_name=sample, sample_name=sample_name) 

            yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3)



def gisaxs_Thomas(t=1): 
    samples = ['T1_A', 'T1_B', 'T2_A', 'T2_B']
    x_list = [58500, 49000, 39000, 28000]

    waxs_arc = np.linspace(0, 13, 3)
    angle = [0.12, 0.16, 0.2]

  # Detectors, motors:
    dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for x, sample in zip(x_list,samples):
        yield from bps.mv(piezo.x, x)

        sample_id(user_name='NT', sample_name=sample) 

        yield from alignement_gisaxs(0.08)
        
        ai0 = piezo.th.position
        det_exposure_time(t, t) 
        name_fmt = '{sample}_ai{angle}deg_wa{waxs}_pos{pos}'
        for j, wa in enumerate(waxs_arc[::-1]):
            yield from bps.mv(waxs, wa)
            
            for nu, num in enumerate([0, 1, 2, 3, 4]):
                yield from bps.mv(piezo.x, x - nu * 300)

                for an in angle:
                    yield from bps.mv(piezo.th, ai0 + an)
                    sample_name = name_fmt.format(sample=sample, angle='%3.2f'%an, waxs='%2.1f'%wa, pos = nu)
                    sample_id(user_name='PT', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')

                    yield from bp.count(dets, num=1)
                

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)




def waxs_Thomas(t=1, x_off = 0, user = 'NT'): 
    samples = ['sample01', 'sample02', 'sample03', 'sample04', 'sample05', 'sample06', 'sample07', 'sample08', 'sample09', 'sample10', 'sample11', 'sample12',
    'sample13', 'sample14', 'sample15', 'sample16', 'sample17', 'sample18', 'sample19', 'sample20', 'sample21', 'sample22', 'sample23', 'sample24', 'sample25', 
    'sample26', 'sample27', 'sample28', 'sample29', 'sample30', 'sample31', 'sample32', 'sample33', 'sample34', 'sample35', 'sample36', 'sample37', 'sample38', 
    'sample39', 'sample40', 'sample41']
    x_list = [44700, 41700, 37700, 32000, 28000, 21000, 15000, 10000,  5800,  2500, -1500, -4500, -6900, -11900, -16500, -19800, -23800, -27800, -33800, -37800,
    -41800, 45000, 41000, 38000, 33000, 31000, 27000, 22500, 20000, 17500, 15000, 11000, 8000, 4500, 1500, -1500, -4500, -9500, -13500, -17500, -21500]
    y_list = [-7800, -7800, -7800, -7800, -7800, -7700, -7700, -7600, -7400, -7400, -7400, -7400, -7400,  -7400,  -7400,  -7400,  -7400,  -7400,  -7400,  -7400,
     -7400,  3000,  3000,  3000,  3000,  3000,  3000,  3000,  3200,  3200,  3200,  3200, 3200, 3200, 3200,  3700,  3400,  3400,   3400,   3400,   3500]
    z_list = [ 2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,   2700,   2700,   2700,   2700,   2700,   2700,   2700,
      2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700,  2700, 2700, 2700, 2700,  2700,  2700,  2700,   2700,   2700,   2700]


    assert len(samples) == len(x_list), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(samples) == len(y_list), f'Number of X coordinates ({len(y_list)}) is different from number of samples ({len(samples)})'
    assert len(samples) == len(z_list), f'Number of X coordinates ({len(z_list)}) is different from number of samples ({len(samples)})'


    waxs_arc = np.linspace(0, 13, 3)

  # Detectors, motors:
    dets = [pil1M,pil300KW]
    det_exposure_time(t,t)

    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    

    for j, wa in enumerate(waxs_arc[::-1]):
        yield from bps.mv(waxs, wa)

        for x, y, z, sample in zip(x_list, y_list, z_list, samples):
            yield from bps.mv(piezo.x, x + x_off)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            det_exposure_time(t, t) 
            name_fmt = '{sample}_wa{waxs}_pos{pos}'
                
            for nu, num in enumerate([0, 1, 2, 3, 4]):
                yield from bps.mv(piezo.y, y + nu * 50)

                sample_name = name_fmt.format(sample=sample, waxs='%2.1f'%wa, pos = nu)
                sample_id(user_name=user, sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)
                
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.1,0.1)




def run_Thomas(t=1, x_off = 0):
    yield from waxs_Thomas(t=0.5, x_off = -500, user = 'NT_pos2_0.5s')
    yield from waxs_Thomas(t=0.5, x_off = -250, user = 'NT_pos3_0.5s')
    yield from waxs_Thomas(t=0.5, x_off = 250, user = 'NT_pos4_0.5s')
