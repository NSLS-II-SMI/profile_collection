 
def saxsafrl( t = 2): 
    # Slowest cycle:
    name = 'AS'
    x_list  = -6.308
    # Detectors, motors:
    dets = [pil1M, ls.ch1_read, xbpm3.sumY, pdcurrent2]
    y_range = [-0.0, 0.0, 1]
    sample = 'Gl_capillary_blank_EtOAc'
    num = 3
    
    pil1M.cam.file_path.put(f"/ramdisk/images/users/2019_3/304562_Schantz/1M/%s"%sample)
    name_fmt = '{i}_{temperature}C_{pinread}uA'
    #    param   = '20.4'
    #assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t,t)
    for i in range(num): 
            temp = ls.ch1_read.value
            fs.open()
            time.sleep(0.25)
            #pin = pin_diode.read()['pin_diode_current2_mean_value']['value']
            pin = pdcurrent2.value
            print(pin)
            time.sleep(0.25)
            fs.close()
            sample_name = name_fmt.format(temperature=temp, pinread = np.float('%.1f'%pin), i = '%4.4d'%i)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            sample_id(user_name=sample, sample_name=sample_name) 
            #yield from bp.count(dets)
            yield from bp.rel_scan(dets, stage.y, *y_range)
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3)


    
