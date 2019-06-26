def run_waxs_IC(t=1): 
    dets = [pil300KW, pil1M]
    

    names = ['W_ODPA_20cZnO_ai0.4deg']
        
    #what we run now

    curr_names = names

    
    energies = [2140, 2145, 2150, 2152, 2154, 2156, 2160]
    
    waxs_arc = [0, 13, 3]
    
    for name in curr_names:
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for i, e in enumerate(energies):
                              
            yield from bps.mv(energy, e)
            #yield from bps.mv(piezo.x, ( x + i * 300))
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='IC', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_arc)


        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5,0.5)
       
        yield from bps.mv(energy, 2153)
        time.sleep(5)
        yield from bps.mv(energy, 2145)
        time.sleep(5)
        yield from bps.mv(energy, 2140)
        time.sleep(5)



