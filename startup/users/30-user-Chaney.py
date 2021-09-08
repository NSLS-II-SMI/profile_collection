def giwaxs_chaney_2021_3(t=1): 
    
    # names = ['sam01', 'sam02', 'sam03', 'sam04', 'sam05', 'sam06', 'sam07', 'sam08', 'sam09', 'sam10', 'sam11', 'sam12', 'sam13',
    #          'sam14', 'sam15', 'sam17', 'sam18', 'sam19', 'sam20', 'sam21', 'sam22', 'sam23', 'sam24', 'sam25', 'sam26', 'sam27']
    # names = ['sam28', 'sam29', 'sam30', 'sam31', 'sam33', 'sam34', 'sam35', 'sam36', 'sam37', 'sam38', 'sam39', 'sam40', 'sam41',
    #          'sam42', 'sam43', 'sam44', 'sam45', 'sam46', 'sam47', 'sam50', 'sam51', 'sam52', 'sam53', 'sam54', 'sam55', 'sam56']
    # names = ['sam57', 'sam58', 'sam59', 'sam60', 'sam61', 'sam62', 'sam63', 'sam64', 'sam65', 'sam66', 'sam67', 'sam68', 'sam69',
    #          'sam70', 'sam73', 'sam74', 'sam77', 'sam78',    'S1',    'S2',   'S3',    'S4',   'S5']
    # names = [  'S6',    'S7',    'S8',    'S9',    'S10',   'S11',   'S12',   'S13',  'S14',  'S15' ]
    # names = [ 'JH-CGE',  'TT1',  'TT3',  'SC1',   'SC2',   'MO3',   'MO4',   'ZZ1']
    # names = [ '1MEO',   '1FS',  'N2200', '10MEO', '10FS',   '5FS',   '20MEO',  '20FS', '5MEO']


    names = [      'T1',     'T2',     'O',    'C2',     'C1',  'Wenhan1', 'Wenhan2']
    x_piezo = [    51000,   48000,   38000,   26000,   14000,   -6000,  -17000]
    y_piezo = [     7000,    7000,    7000,    7000,     7000,    7300,   7300]
    z_piezo = [     2300,    2300,    2300,    2300,     2300,    2300,    2300]
    x_hexa =  [      9,       0,       0,       0,       0,       0,       0]

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'
    assert len(x_piezo) == len(z_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(z_piezo)})'
    assert len(x_piezo) == len(x_hexa), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(x_hexa)})'

    waxs_arc = [10.6]
    angle = [0.11, 0.14]

    dets = [pil900KW, pil300KW]
    det_exposure_time(t,t)

    for name, xs, zs, ys, xs_hexa in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(stage.x, xs_hexa)
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)
        yield from bps.mv(piezo.th, 0)
        
        yield from alignement_gisaxs(angle = 0.11)

        ai0 = piezo.th.position
        det_exposure_time(t,t)
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)  

            for i, an in enumerate(angle):
                yield from bps.mv(piezo.x, xs + 200)
                yield from bps.mv(piezo.th, ai0 + an)                
                name_fmt = '{sample}_14keV_ai{angl}deg_wa{waxs}'
                sample_name = name_fmt.format(sample=name, angl='%3.2f'%an, waxs='%2.1f'%wa)
                sample_id(user_name='PT', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                yield from bp.count(dets, num=1)
            
            yield from bps.mv(piezo.th, ai0)