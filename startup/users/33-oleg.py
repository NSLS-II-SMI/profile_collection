####line scan

def aaron_rot(t=8):
    sample_id(user_name='AM', sample_name='tetrahedral')
    det_exposure_time(t)
    yield from bp.inner_product_scan([pil1M], 24, prs, 45, 22, stage.x, 0.23, 0.15, piezo.y, -1792.6, -1792.6)
    yield from bp.inner_product_scan([pil1M], 22, prs, 21, 0, stage.x, 0.15, 0.11, piezo.y, -1792.6, -1792.6)
    yield from bp.inner_product_scan([pil1M], 11, prs, -1, -11, stage.x, 0.11, 0.1, piezo.y, -1792.6, -1792.1)
    yield from bp.inner_product_scan([pil1M], 11, prs, -12, -22, stage.x, 0.1, 0.1, piezo.y, -1792.1, -1791.6)
    yield from bp.inner_product_scan([pil1M], 11, prs, -23, -33, stage.x, 0.1, 0.114, piezo.y, -1791.6, -1790.9)
    yield from bp.inner_product_scan([pil1M], 12, prs, -34, -45, stage.x, 0.114, 0.134, piezo.y, -1790.9, -1790.9)
    
    
def brian_caps(t=1): 
    x_list  = [-36500, -30150, -23800, -17450, -11100, -4750, 1600, 7950,  14400, 20700, 27050, 33400, 39850]#
    y_list =  [      0,     0,      0,      0,      0,     0,    0,     0,      0]
    samples = [ 'test', 'LC-O36-6','LC-O36-7','LC-O36-8','LC-O36-9','LC-O37-6','LC-O37-7','LC-O37-8','LC-O37-9']
    # Detectors, motors:
    dets = [pil1M]
    y_range = [0, 0, 1]
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t,t)
    for x, y, sample in zip(x_list,y_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        sample_id(user_name='BM', sample_name=sample) 
        #yield from bp.scan(dets, piezo.y, *y_range)
        yield from bp.count(dets, num=1)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)
