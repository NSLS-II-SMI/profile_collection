import time
#ls.ch1_read gives motor status, read.value gives only temperature

def run_articulatus_test1(t=5, name = 'TD'):
    x_list = [0.75]       
    y_range  = [4.9, 5.125,10]
    #y_offset   
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 42, 7]
    samples = ['RZ_T4_Tooth']
    name_fmt = '{sample}'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        sample_name = name_fmt.format(sample=sample)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.x, x)
        sample_id(user_name=name, sample_name=sample_name)                       
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)
        
def run_articulatus_test2(t=5, name = 'TD'):
    x_list = [0.65]       
    y_range  = [4.3, 4.9,12]
    #y_offset   
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 42, 7]
    samples = ['RZ_T4_Stylus']
    name_fmt = '{sample}'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        sample_name = name_fmt.format(sample=sample)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.x, x)
        sample_id(user_name=name, sample_name=sample_name)                       
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)     



def run_articulatus_test3(t=5, name = 'TD'):
    x_list = [0.65]       
    y_range  = [3.825, 3.95,6]
    #y_offset   
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 42, 7]
    samples = ['RZ_T5_Tooth']
    name_fmt = '{sample}'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        sample_name = name_fmt.format(sample=sample)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.x, x)
        sample_id(user_name=name, sample_name=sample_name)                       
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)
        
def run_articulatus_test4(t=5, name = 'TD'):
    x_list = [0.65]       
    y_range  = [3.7, 3.825,6]
    #y_offset   
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 42, 7]
    samples = ['RZ_T5_Sytlus']
    name_fmt = '{sample}'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        sample_name = name_fmt.format(sample=sample)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.x, x)
        sample_id(user_name=name, sample_name=sample_name)                       
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)       
        
        
        
        
        
        

    


    
def run_chitont7(t=10, name = 'TD', s_name = 'Cryptochiton_stellerit7'): 
    y_range  = [3.725, 3.825, 3]
    x_list = np.linspace(-8.225, -7.75, 20)
    dets = [pil300KW, pil1M]
    waxs_arc = [4, 58, 10]
    samples = [s_name]
    name_fmt = '{s_name}_{x_position}'
    #    param   = '16.1keV'
    #assert len(y_list) == len(samples), f'Number of X coordinates ({len(y_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x in x_list:
        yield from bps.mv(stage.x, x)
        x = stage.x.position
        sample_name = name_fmt.format(s_name=s_name, x_position = x)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)  
    
def run_chitont15(t=10, name = 'TD', s_name = 'Cryptochiton_stellerit15'): 
    y_range  = [3.35, 3.5, 4]
    x_list = np.linspace(-4.15, -3.125, 42)
    dets = [pil300KW, pil1M]
    waxs_arc = [4, 58, 10]
    samples = [s_name]
    name_fmt = '{s_name}_{x_position}'
    #    param   = '16.1keV'
    #assert len(y_list) == len(samples), f'Number of X coordinates ({len(y_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x in x_list:
        yield from bps.mv(stage.x, x)
        x = stage.x.position
        sample_name = name_fmt.format(s_name=s_name, x_position = x)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)            
    
def run_chitont30(t=10, name = 'TD', s_name = 'Cryptochiton_stellerit30'): 
    y_range  = [3.025, 3.425, 9]
    x_list = np.linspace(-1.9, -0.85, 43)
    dets = [pil300KW, pil1M]
    waxs_arc = [4, 58, 10]
    samples = [s_name]
    name_fmt = '{s_name}_{x_position}'
    #    param   = '16.1keV'
    #assert len(y_list) == len(samples), f'Number of X coordinates ({len(y_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x in x_list:
        yield from bps.mv(stage.x, x)
        x = stage.x.position
        sample_name = name_fmt.format(s_name=s_name, x_position = x)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)             
    
    
def run_chitont45(t=10, name = 'TD', s_name = 'Cryptochiton_stellerit45'): 
    y_range  = [3, 3.45, 19]
    x_list = np.linspace(-1.9, -0.85, 43)
    dets = [pil300KW, pil1M]
    waxs_arc = [4, 58, 10]
    samples = [s_name]
    name_fmt = '{s_name}_{x_position}'
    #    param   = '16.1keV'
    #assert len(y_list) == len(samples), f'Number of X coordinates ({len(y_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x in x_list:
        yield from bps.mv(stage.x, x)
        x = stage.x.position
        sample_name = name_fmt.format(s_name=s_name, x_position = x)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)             
    
    
    
def run_rz1(t=5, name = 'TD'):
    x_list = [9.44]       
    y_range  = [6.209,6.235,14]
    #y_offset   
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [4, 58, 10]
    samples = ['RZ_18-0731_Leftsection_line1']
    name_fmt = '{sample}'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        sample_name = name_fmt.format(sample=sample)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.x, x)
        sample_id(user_name=name, sample_name=sample_name)                       
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)      
    
def run_rz2(t=5, name = 'RZ'):
    x_list = [-15.337]       
    y_range  = [5.557,5.569,7]
    #y_offset   
    # Detectors, motors:
    dets = [pil300KW,ls.ch1_read]
    
    waxs_arc = [4, 58, 10]
    samples = ['18-0731_Leftsection_line2']
    name_fmt = '{sample}'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        time.sleep(300)
        sample_name = name_fmt.format(sample=sample)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.x, x)
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)      
                    
def run_td1(t=5, name = 'TD'):
    x_list = [24.9, 18.6, 12.3, 6, -0.3, -6.6, -12.9, -19.2]       
    y_list  = [-0.3]
    #y_offset   
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 42, 7]
    samples = ['NaH2PO4', 'PAN-Ni', 'PAN']
    name_fmt = '{sample}_{y_position}'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(stage.x, x)
        for y in (y_list):
            sample_name = name_fmt.format(sample=sample, y_position=y)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bps.mv(stage.y, y)
            sample_id(user_name=name, sample_name=sample_name)          
            yield from escan(dets, waxs.arc, *waxs_arc)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
    
           
def run_td2(t=10, name = 'TD'): 
    y_range = [-0.2, 0.2, 3] 
    x_list  = [24.9, 18.6, 12.3, 6, -0.3, -6.6, -12.9, -19.2]
    #y_offset    
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 42, 7]
    samples = ['PAN-Ni_5-1', 'PAN_5-1', 'PAN-Ni_5-3', 'PAN_5-3', 'PAN-Ni_8-0', 'PAN_8-0', 'PAN-Ni_8-1', 'PAN_8-1']
    name_fmt = '{sample}'
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        sample_name = name_fmt.format(sample=sample)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.x, x)
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)    
       
def run_ramya2(t=5, name = 'RM', s_name = 'BSpec_Burnt_MesoFiber_FineRes4'): 
    #x_range = [-17.20, -18.40, 49] 
    y_range  = [0.0, 0.80, 13]  #original [0.0, 0.80, 33]
    x_list = np.linspace(-14.05, -14.10, 3)  #original (-14.00, -15.20, 49)
    #y_list = np.linspace(-0.275, 0.325, 25)
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 30, 5]
    samples = [s_name]
    name_fmt = '{s_name}_{x_position}'
    #    param   = '16.1keV'
    #assert len(y_list) == len(samples), f'Number of X coordinates ({len(y_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x in x_list:
        yield from bps.mv(stage.x, x)
        x = stage.x.position
        sample_name = name_fmt.format(s_name=s_name, x_position = x)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.y, *y_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
    
          
def run_ramya3(t=5, name = 'RM', s_name = 'BSpec_Burnt_MesoEndo_FineRes'): 
    x_range = [12.77, 14.77, 81] 
    y_list  = [-0.025, 0, 0.025]
    #y_offset    
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 30, 5]
    samples = [s_name, s_name, s_name]
    name_fmt = '{sample}_{y_position}'
    #    param   = '16.1keV'
    assert len(y_list) == len(samples), f'Number of X coordinates ({len(y_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for y, sample in zip(y_list, samples):
        sample_name = name_fmt.format(sample=sample, y_position=y)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.y, y)
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.x, *x_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
    
def run_ramya4(t=5, name = 'RM', s_name = 'BSpec_Intumescence_Meso_Endo_FineRes'): 
    x_range = [-18.40, -20.0, 65] 
    y_list  = [-0.025, 0, 0.025]
    #y_offset    
    # Detectors, motors:
    dets = [pil300KW]
    waxs_arc = [6, 30, 5]
    samples = [s_name, s_name, s_name]
    name_fmt = '{sample}_{y_position}'
    #    param   = '16.1keV'
    assert len(y_list) == len(samples), f'Number of X coordinates ({len(y_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for y, sample in zip(y_list, samples):
        sample_name = name_fmt.format(sample=sample, y_position=y)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bps.mv(stage.y, y)
        sample_id(user_name=name, sample_name=sample_name)               
        yield from e_grid_scan(dets, stage.x, *x_range, waxs.arc, *waxs_arc, 1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)
           

def run_all():
    
    yield from run_articulatus_test4()
    yield from run_articulatus_test3()
    yield from run_articulatus_test2()
    yield from run_articulatus_test2()
    #yield from run_ramya1()
    #yield from run_ramya2()
    #yield from run_ramya3()
    #yield from run_ramya4()


