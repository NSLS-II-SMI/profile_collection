#phi scan
def gisaxsnetzke(meas_t=1):
    waxs_arc = np.linspace(0, 32.5, 6) #(2th_min 2th_max steps)
    dets = [pil300KW]
    
    #xlocs = [-30600, -14100, 3800, 20400, 38900]
   # xlocs = [-27990, -13700, 800, 16300, 32700, 47400]
    xlocs = [1010]
    names = ['190919-13_DELETETHISSCAN']
    angle = [0.2]
        
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 
    
    for x, name in zip(xlocs, names):
        yield from bps.mv(piezo.x, x)
        
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from alignement_gisaxs(0.15)
        yield from bps.mv(GV7.close_cmd, 1 )
        
        
        det_exposure_time(meas_t) 
        name_fmt = '{sample}_ai{angle}deg_{phi}deg_wa{waxs}'
        
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
      #  NE
            for phi in np.linspace(-5, 5, 3): #(phi_min phi_max steps)
                yield from bps.mv(prs, phi)
                
                for an in angle:
                    yield from bps.mvr(piezo.th, an)
            
                    sample_name = name_fmt.format(sample=name, angle='%3.2f'%an, phi = phi, waxs='%2.1f'%wa)
                    sample_id(user_name='LC', sample_name=sample_name)
                    
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    #Change from 4 to 1 exposure
                 #   yield from bp.count(dets, num=4)
                    yield from bp.count(dets, num=1)
                    yield from bps.mvr(piezo.th, -an)                    
                
        yield from bps.mv(prs, 0)



#incident angle scan
def gisaxsnetzke1(meas_t=1):
    waxs_arc = np.linspace(0, 32.5, 6)
    dets = [pil300KW]
    
    xlocs = [200]
    names = ['190919-12_01_aiscan']
    phi = 7
        
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 

    for x, name in zip(xlocs, names):
        yield from bps.mv(piezo.x, x)
        #yield from alignement_gisaxs(angle = 0.15)
        #yield from bps.mvr(piezo.th, angle)
        
        det_exposure_time(meas_t) 
        name_fmt = '{sample}_ai{angle}deg_{phi}deg_wa{waxs}'
        
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
        
            for th in np.linspace(0.05, 0.3, 6):
                yield from bps.mvr(piezo.th, th)
            
                sample_name = name_fmt.format(sample=name, angle='%3.2f'%an, phi = phi, waxs='%2.1f'%wa)
                sample_id(user_name='LC', sample_name=sample_name)
            
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                yield from bps.mvr(piezo.th, -th)
 
   
#incident angle scan at different position of the sample
def gisaxsnetzke2(meas_t=1):
    waxs_arc = np.linspace(0, 32.5, 6)
    dets = [pil300KW]
    
    xlocs = [-2000, 1000, 0, 1000, 2000]
    names = ['190919-12_01_aiscan_pos1', '190919-12_01_aiscan_pos2', '190919-12_01_aiscan_pos3', '190919-12_01_aiscan_pos4', '190919-12_01_aiscan_pos5']
    phi = 7
        
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 

    for x, name in zip(xlocs, names):
        yield from bps.mv(piezo.x, x)
        #yield from alignement_gisaxs(angle = 0.15)
        #yield from bps.mvr(piezo.th, angle)
        
        det_exposure_time(meas_t) 
        name_fmt = '{sample}_ai{angle}deg_{phi}deg_wa{waxs}'
        
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
        
            for th in np.linspace(0.05, 0.3, 6):
                yield from bps.mvr(piezo.th, th)
            
                sample_name = name_fmt.format(sample=name, angle='%3.2f'%th, phi = phi, waxs='%2.1f'%wa)
                sample_id(user_name='LC', sample_name=sample_name)
            
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                yield from bps.mvr(piezo.th, -th)   
                

#DONT USE!!!! realignement of tyhe sampl at each phi
def gisaxsnetzke3(meas_t=1):
    waxs_arc = np.linspace(0, 32.5, 6) #(2th_min 2th_max steps)
    dets = [pil300KW]
    
    xlocs = [-30600, -14100, 3800, 20400, 38900]
    names = ['190919-2','190919-3','190919-4','190919-5','190919-6']
    angle = [0.1, 0.15, 0.2]
        
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 
    num = 0
    for x, name in zip(xlocs, names):
        if num > 0:
            yield from bps.mvr(piezo.th, ref_th_0)
        yield from bps.mv(piezo.x, x)
        #yield from alignement_gisaxs(0.15)
        ref_th_0 = piezo.th.position
        
        det_exposure_time(meas_t) 
        name_fmt = '{sample}_ai{angle}deg_{phi}_wa{waxs}'
        
        for phi in np.linspace(-45, 45, 10): #(phi_min phi_max steps)
            yield from bps.mv(prs, phi)
            yield from alignement_gisaxs_shorter(0.15)
            
            for j, wa in enumerate(waxs_arc):
                yield from bps.mv(waxs, wa)
                for an in angle:
                    yield from bps.mvr(piezo.th, an)
                    sample_name = name_fmt.format(sample=name, angle='%3.2f'%an, phi = phi, waxs='%2.1f'%wa)
                    sample_id(user_name='LC', sample_name=sample_name)
               
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=4)
                    yield from bps.mvr(piezo.th, -an)
                
        yield from bps.mv(prs, 0)
        num +=1
        
#realignement of tyhe sampl at each phi
def gisaxsnetzke4(meas_t=1):
    waxs_arc = np.linspace(0, 32.5, 6) #(2th_min 2th_max steps)
    dets = [pil300KW]
    
    xlocs = [1010]
    names = ['190919-13_bkgnd3']
    angle = [0.2]
        
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 
    num = 0
    for x, name in zip(xlocs, names):
        if num > 0:
            yield from bps.mvr(piezo.th, ref_th_0)
        yield from bps.mv(piezo.x, x)
        #yield from alignement_gisaxs(0.15)
        ref_th_0 = piezo.th.position
        
        det_exposure_time(meas_t) 
        name_fmt = '{sample}_phiAlign2_ai{angle}deg_{phi}_wa{waxs}'
        
        for phi in np.linspace(65, 66, 2): #(phi_min phi_max steps)
            yield from bps.mv(prs, phi)
            yield from alignement_gisaxs_shorter(0.15)
            
            for j, wa in enumerate(waxs_arc):
                yield from bps.mv(waxs, wa)
                for an in angle:
                    yield from bps.mvr(piezo.th, an)
                    sample_name = name_fmt.format(sample=name, angle='%3.2f'%an, phi = phi, waxs='%2.1f'%wa)
                    sample_id(user_name='LC', sample_name=sample_name)
               
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)
                    yield from bps.mvr(piezo.th, -an)
                
        yield from bps.mv(prs, 0)
        num +=1
        
        
#Silicon (100) scan
def gisaxsnetzkeSi(meas_t=1):
    waxs_arc = np.linspace(0, 32.5, 6) #(2th_min 2th_max steps)
    dets = [pil300KW]
    
    #xlocs = [-30600, -14100, 3800, 20400, 38900]
   # xlocs = [-27990, -13700, 800, 16300, 32700, 47400]
    xlocs = [1010]
    names = ['SiScGOOD2']
    angle = [0.2]
        
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 
    
    for x, name in zip(xlocs, names):
        yield from bps.mv(piezo.x, x)
        
        yield from bps.mv(GV7.open_cmd, 1 )
        yield from alignement_gisaxs(0.15)
        yield from bps.mv(GV7.close_cmd, 1 )
        
        
        det_exposure_time(meas_t) 
        name_fmt = '{sample}_ai{angle}deg_{phi}deg_wa{waxs}'
        
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
      #  NE
            for phi in np.linspace(-90, 90, 181): #(phi_min phi_max steps)
                yield from bps.mv(prs, phi)
                
                for an in angle:
                    yield from bps.mvr(piezo.th, an)
            
                    sample_name = name_fmt.format(sample=name, angle='%3.2f'%an, phi = phi, waxs='%2.1f'%wa)
                    sample_id(user_name='LC', sample_name=sample_name)
                    
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    #Change from 4 to 1 exposure
                    yield from bp.count(dets, num=2)
                 #   yield from bp.count(dets, num=1)
                    yield from bps.mvr(piezo.th, -an)                    
                
        yield from bps.mv(prs, 0)
