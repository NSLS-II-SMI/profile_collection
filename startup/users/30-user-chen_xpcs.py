def grid_scan_xpcs():
    
    folder = "301000_Chen34"
    xs = np.linspace(-9350, -9150, 2)
    ys = np.linspace(1220, 1420, 2)
    names=['PSBMA5_200um_grid']
    
    
    
    
    energies = [2450, 2472, 2476, 2490]
    
    x_off = [0, 60, 0, 60]
    y_off = [0, 0, 60, 60]
    
    xxs, yys = np.meshgrid(xs, ys)
    
    dets = [pil1M]
    for name in names:
        for ener, xof, yof in zip(energies, x_off, y_off):
            yield from bps.mv(energy, ener)
            yield from bps.sleep(10)
            for i, (x, y) in enumerate(zip(xxs.ravel(), yys.ravel())):
                
                pil1M.cam.file_path.put(f"/ramdisk/images/users/2019_3/%s/1M/%s_pos%s"%(folder, name, i))
            

                yield from bps.mv(piezo.x, x+xof)
                yield from bps.mv(piezo.y, y+yof)
                
                name_fmt = '{sample}_{energy}eV_pos{pos}'
                sample_name = name_fmt.format(sample=name, energy=ener, pos = '%2.2d'%i)
                sample_id(user_name='Chen', sample_name=sample_name)
                yield from bps.sleep(5)
                
                det_exposure_time(0.03, 30)
                
                print(f'\n\t=== Sample: {sample_name} ===\n')
                 
                pil1M.cam.acquire.put(1)
                yield from bps.sleep(5)
                pv = EpicsSignal('XF:12IDC-ES:2{Det:1M}cam1:Acquire', name="pv")

                while pv.get() == 1:
                        yield from bps.sleep(5)
                    
        yield from bps.mv(energy, 2475)
        yield from bps.mv(energy, 2450)
        



def NEXAFS_SAXS_S_edge(t=1):
        dets = [pil300KW]
        name = 'sample_thick_waxs'

        energies = [2450, 2480, 2483, 2484, 2485, 2486, 2500]

        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_wa{wa}'

        waxs_an = np.linspace(0, 26, 5)
        
        yss = np.linspace(1075, 1575, 5)
        
        
        for wax in waxs_an:
                yield from bps.mv(waxs, wax)
                for e, ys in zip(energies, yss):                              
                    yield from bps.mv(energy, e)
                    yield from bps.mv(piezo.y, ys)
                    sample_name = name_fmt.format(sample=name, energy=e, wa = '%3.1f'%wax)
                    sample_id(user_name='Chen', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

                yield from bps.mv(energy, 2475)
                yield from bps.mv(energy, 2450)        

    

def grid_scan_static():

    names=['PSBMA30_10um_static']
    
    x_off = -36860+np.asarray([-200, 200])
    y_off = 1220+np.asarray([-100, 0, 100])
    
    energies = np.linspace(2500, 2450, 51)
    xxs, yys = np.meshgrid(x_off, y_off)
    
    dets = [pil300KW, pil1M]
    for name in names:
        for i, (x, y) in enumerate(zip(xxs.ravel(), yys.ravel())):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            energies = energies[::-1]            
            yield from bps.sleep(2)
            
            for ener in energies:           
                yield from bps.mv(energy, ener)

                yield from bps.sleep(0.1)
                
                name_fmt = '{sample}_{energy}eV_pos{pos}_xbpm{xbpm}'
                sample_name = name_fmt.format(sample=name, energy=ener, pos = '%2.2d'%i, xbpm='%3.1f'%xbpm3.sumY.value)
                sample_id(user_name='Chen', sample_name=sample_name)
        
                det_exposure_time(0.1, 0.1)
                yield from bp.count(dets, num=1)

