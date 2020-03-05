#phi scan
def gisaxsnetzke(meas_t=1):
    waxs_arc = np.linspace(0, 26, 5) #(2th_min 2th_max steps)
    dets = [pil300KW, pil1M]
    phi=-20
    #xlocs = [-44500, -34800, -25700, -15500, -5000, 6900, 15200, 25500, 35500, 46800]
    xlocs = [25500]
    #names = ['RY13','RY15','RY16','RY17','RY18','RY19','RY21','RY26','TiN1','TiN2']
    names = ['RY26_alphascan']
    #angle = [0.2, 0.29, 0.4, 0.45]
    angle = [0.08, 0.12, 0.2]
    energ = [16100]   
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 
    
    for x, name in zip(xlocs, names):
        yield from bps.mv(piezo.x, x)
        
        #yield from bps.mv(GV7.open_cmd, 1 )
        yield from alignement_gisaxs(0.08)
        #yield from bps.mv(GV7.close_cmd, 1 )
        
        det_exposure_time(meas_t, meas_t) 
        name_fmt = '{sample}_E{ene}eV_ai{angle}deg_phi{phi}deg_wa{waxs}'
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            for en in energ:
                yield from bps.mv(energy, en)
                #and the fastest cycle is the angle change
                for an in angle:
                    yield from bps.mvr(piezo.th, an)
                    sample_name = name_fmt.format(sample=name, ene='%2.0f'%en, angle='%3.2f'%an, phi = phi, waxs='%2.1f'%wa)
                    sample_id(user_name='SN', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=4)
                    yield from bps.mvr(piezo.th, -an)                   
                
    yield from bps.mv(prs, 0)

def netzkeall(meas_t=0.6):
    yield from gisaxsnetzke(meas_t=0.6)
    yield from gisaxsnetzke3(meas_t=0.6)


def gisaxsquick(meas_t=0.3):
    waxs_arc = np.linspace(0, 45.5, 8) #(2th_min 2th_max steps)
    dets = [pil300KW, pil1M]
    phi=-20
    xlocs = [25500]
    names = ['RY26n']
    #angle = [0.2, 0.29, 0.4, 0.45]
    angle = [0.2, 0.29, 0.4]
    energ = [9580]   
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 
    
    for x, name in zip(xlocs, names):
        yield from bps.mv(piezo.x, x)
        
        #yield from bps.mv(GV7.open_cmd, 1 )
        #yield from alignement_gisaxs(0.2)
        #yield from bps.mv(GV7.close_cmd, 1 )
        
        det_exposure_time(meas_t, meas_t) 
        name_fmt = '{sample}_E{ene}eV_ai{angle}deg_phi{phi}deg_wa{waxs}'
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
            for en in energ:
                yield from bps.mv(energy, en)
                #and the fastest cycle is the angle change
                for an in angle:
                    yield from bps.mvr(piezo.th, an)
                    sample_name = name_fmt.format(sample=name, ene='%2.0f'%en, angle='%3.2f'%an, phi = phi, waxs='%2.1f'%wa)
                    sample_id(user_name='SN', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=4)
                    yield from bps.mvr(piezo.th, -an)                   
                
    yield from bps.mv(prs, 0)

'''
#incident angle scan
def gisaxsnetzke1(meas_t=0.3):
    waxs_arc = np.linspace(0, 45.5, 8)
    dets = [pil300KW]
    
    xlocs = [12000]
    names = ['RY5']
    phi = 0
        
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 

    for x, name in zip(xlocs, names):
        yield from bps.mv(piezo.x, x)
        #yield from alignement_gisaxs(angle = 0.15)
        #yield from bps.mvr(piezo.th, angle)
        
        det_exposure_time(meas_t, meas_t) 
        name_fmt = '{sample}_ai{angle}deg_{phi}deg_wa{waxs}'
        
        for j, wa in enumerate(waxs_arc):
            yield from bps.mv(waxs, wa)
        
            for th in np.linspace(0.2, 0.4, 2):
                yield from bps.mvr(stage.th, th)
            
                sample_name = name_fmt.format(sample=name, angle='%3.2f'%th, phi = phi, waxs='%2.1f'%wa)
                sample_id(user_name='SN', sample_name=sample_name)
            
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                yield from bps.mvr(stage.th, -th)
 
   
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
        
        det_exposure_time(meas_t, meas_t) 
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
                
'''
#DONT USE!!!! realignement of tyhe sampl at each phi
def gisaxsnetzke3(meas_t=0.6):
    waxs_arc = np.linspace(0, 45.5, 8) #(2th_min 2th_max steps)
    dets = [pil300KW, pil1M]
    xlocs = [-44500, -34800, -25700, -15500, -5000, 6900, 15200, 25500, 35500, 46800]
    names = ['RY13_phioffset','RY15_phioffset','RY16_phioffset','RY17_phioffset','RY18_phioffset','RY19_phioffset','RY21_phioffset','RY26_phioffset','TiN1_phioffset','TiN2_phioffset']
    angle_off_from02 = [0, 0.09, 0.2]
    energ = [9540, 9580]
    phis = [-22.5, 22.5]    
    assert len(xlocs) == len(names), f'Sample name/position list is borked' 
    #num = 0
    for x, name in zip(xlocs, names):
        #if num > 0:
        #    yield from bps.mvr(piezo.th, ref_th_0)
        yield from bps.mv(piezo.x, x)
        #yield from alignement_gisaxs(0.15)
        #ref_th_0 = piezo.th.position
        
        det_exposure_time(meas_t, meas_t) 
        name_fmt = '{sample}_E{ene}eV_ai{angle}deg_phi{phi}deg_wa{waxs}'
        #phi is the slowest cycle:s
        for phi in phis: #(phi_min phi_max steps)
            yield from bps.mv(prs, phi)
            yield from alignement_gisaxs_hex_short(0.2)
            ref_th_0 = stage.th.position
            yield from bps.mvr(stage.th, ref_th_0+0.2)
            
            #waxs arc is scanned for a single phi
            for j, wa in enumerate(waxs_arc):
                yield from bps.mv(waxs, wa)
                #then for a single waxs arc we change angle as relative move offset
                for a, an in enumerate(angle_off_from02):
                    yield from bps.mvr(stage.th, an)
                    #and the fastest cycle is the energy
                    for en in energ:
                        yield from bps.mv(energy, en)
                        real_an = an[a]+0.2
                        sample_name = name_fmt.format(sample=name, ene='%2.0f'%en, angle='%3.2f'%real_an, phi = phi, waxs='%2.1f'%wa)
                        sample_id(user_name='SN', sample_name=sample_name)
                
                        print(f'\n\t=== Sample: {sample_name} ===\n')
                        yield from bp.count(dets, num=4)
                yield from bps.mv(stage.th, ref_th_0+0.2)
                    
        yield from bps.mv(prs, 0)
        #num +=1
'''        
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
        
        det_exposure_time(meas_t, meas_t) 
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
        
        
        det_exposure_time(meas_t, meas_t) 
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
'''