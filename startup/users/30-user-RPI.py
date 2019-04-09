


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

def run_waxsRPI(t=1): 
    name = 'SP'
    x_list  = [4000, 4500, 12000, 18000]#
    # Detectors, motors:
    dets = [pil300KW]
    y_range = [0, 0, 1]
    waxs_arc = [2.85, 44.85, 8]
    samples = ['NPS-Cu_1_Shift','NPS-Cu_2_Shift','NPS-Cu_160c_1_Shift','NPS-Cu_160c_2_Shift']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(piezo.x, x)
        sample_id(user_name=name, sample_name=sample) 
        yield from bp.scan(dets, waxs.arc, *waxs_arc)
        
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 
   

def giwaxsRPI(meas_t=1):
        dets = [pil300KW, pil300kwroi2, xbpm3.sumY, xbpm2.sumY]
        xlocs = [20000, 10000, 0, -10000, -20000]
        names = ['SF_0.5mgml_200mM_48hr_1hrETOH', 'SF_0.5mgml_200mM_48hr', 'Bare_TiO2_Ozone', 'SF_0.5mgml_200mM_0.02mM_48hr','SF_0.5mgml_200mM_0.02mM_48hr_1hrETOH']
        for xloc, name in zip(xlocs, names):
                yield from bps.mv(piezo.x,xloc)
                yield from bps.mv(piezo.th,0.2)
                yield from alignRPI()
                plt.close('all')
                
                angle_offset = [0, 0.02, 0.04, 0.07]
                a_off = piezo.th.position
                waxs_arc = [2.85, 14.85, 3]
                det_exposure_time(meas_t) 
                name_fmt = '{sample}_{angle}deg'
                for j, ang in enumerate( a_off + np.array(angle_offset) ):
                    yield from bps.mv(piezo.x, xloc)
                    real_ang = 0.08 + angle_offset[j]
                    yield from bps.mv(piezo.th, ang)
                    sample_name = name_fmt.format(sample=name, angle=real_ang)
                    sample_id(user_name='TF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.scan(dets, waxs.arc, *waxs_arc)

                sample_id(user_name='test', sample_name='test')
                det_exposure_time(0.5)



def linkam_fast(n=6):
    yield from bps.mv(attn_shutter, 'Retract')
    yield from bp.scan([pil1M], stage.y, 0.1, 0.9, n)
    yield from bps.mv(attn_shutter, 'Insert')
    
    
   

