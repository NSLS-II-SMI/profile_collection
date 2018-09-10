
sams = [ 's1_PCBM_P3HT_1_1', 's2_PCBM_P3HT:PS_1_1_10', 's3_PCBM_P3HT:PIS_1_1_10', 
's4_PCBM_P3HT:SIS_1_1_10', 's5_PCBM_P3HT:PIS_1_1_10_50Anl_150Anl']
name='ZB' 

def scan_sample( t= 1 ):        
    dets = [pil300KW, pil300kwroi3, pil300kwroi4 ]
    det_exposure_time(t)
    sample_id(user_name=name, sample_name='test') 
    RE( bp.scan( dets, stage.x, -3,2, 51) ) 
    
    
def collect_data_ZB( exposure_time=1, meta_string=['X','Y','Arc', 'Exp'], dets= [  pil300KW   ]  ): 
        '''
        dets: [pil1M], collect SAXS data
              [rayonix ] collect MAXS data
              [pil300KW] collect WAXS data
              
              the combination  will collect detectors data  simultineously 
              e..g, [ pil1M, pil300KW] simultineously collect SAXS and WAXS             
              
        '''   
        posy = stage.y.position
        posx =  stage.x.position
        inc = stage.th.position
        arc =   waxs.arc.position
        md = 'sample: %s, x=%.2f, y=%0.2f,  arc=%.2f, exp=%s s.'%(
                 RE.md['sample_name'],posx, posy,  arc,  exposure_time )
                 
        posx_ =  create_string(posx)
        posy_ =  create_string(posy) 
        exposure_time_ =  create_string(exposure_time)         
        inc_ = create_string(inc)
        arc_ =   create_string(arc)
        filename= '%s_%s'%( RE.md['user_name'], RE.md['sample_name'] )
        if 'X' in meta_string:
            filename +='_X%s'%posx_
        if 'Y' in meta_string:
            filename +='_Y%s'%posy_
        if 'Inc' in meta_string:
            filename += '_Inc%s'%inc_
        if 'Arc' in meta_string:
            filename += '_arc%s'%arc_            
        if 'Exp' in meta_string:
            filename +='_Exp%s'%exposure_time_

        for detector in dets:                                
                detector.cam.file_name.put(filename) 
                detector.cam.acquire_time.put(exposure_time)
                detector.cam.acquire_period.put(exposure_time)                 
                RE( count( [detector] ),  Measurement = '%s'%md)  
                
                    
def collect_waxs_data( sam, exposure_time ):
    sample_id(user_name=name, sample_name=sample)     
    waxs_arc = [ 4, 10, 16, 22, 28, 34 ]
    for arc in waxs_arc:
        mov(waxs.arc, arc) 
        collect_data( exposure_time, det =[ pil300KW,   rayonix ]   ) 
        print('Collect MAXS and WAXS here with arc=%s'%(arc))     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
             
