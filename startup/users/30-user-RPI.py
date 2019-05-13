


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

def run_waxsRPI(t=5): 
    name = 'SNL'
    x_list  = [832]
    y_start, y_stop, nb_y= -4000,2500,11 
    samples = ['pre-weighed_kit_for_32per']
   
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil300KW, pil1M]
 
 
    waxs_arc = [2.9, 32.9, 6]
  
    det_exposure_time(t)
    name_fmt = '{sample}_ypos{y_pos}'
    
    y_list = np.linspace(y_start, y_stop, nb_y)
    

    for x, sample in zip(x_list, samples):
        for i, y in enumerate(y_list):
                yield from bps.mv(piezo.x, x)
                yield from bps.mv(piezo.y, y)
                               
                sample_name = name_fmt.format(sample=name, y_pos= '%5.5d'%y)
                sample_id(user_name=sample, sample_name=sample_name) 
                
                if i == 0:
                    yield from bp.scan(dets, waxs.arc, *waxs_arc)
                
                else:
                    if waxs.arc.position < 10:
                        yield from bps.mv(waxs.arc, 0)
                    det = [pil1M]
                    yield from bp.count(det, num = 1)
                

            
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 


def linkam_fast(n=6):
    yield from bps.mv(attn_shutter, 'Retract')
    yield from bp.scan([pil1M], stage.y, 0.1, 0.9, n)
    yield from bps.mv(attn_shutter, 'Insert')
    
    
   

