def run_giwaxs_Fak(t=1): 
    dets = [pil300KW, pil1M]
    xlocs1 = [-22000,3000,21500]
    names1 = ['TPD_52nm', 'TPD_42nm', 'TPD_32nm']
        
    #what we run now
    curr_tray = xlocs1
    curr_names = names1
    assert len(curr_tray) == len(curr_names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    waxs_range = [0, 13, 3]
    for x, name in zip(curr_tray, curr_names):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.th, 0.1)
        yield from alignement_gisaxs(0.1)
        plt.close('all')
        angle_offset = [0.1]
        a_off = piezo.th.position
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{angle}deg'
        for j, ang in enumerate( a_off + np.array(angle_offset) ):
            yield from bps.mv(piezo.x, (x+j*500))
            real_ang = angle_offset[j]
            yield from bps.mv(piezo.th, ang)
            sample_name = name_fmt.format(sample=name, angle=float('%.3f'%real_ang))
            sample_id(user_name='YJ', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.scan(dets, waxs, *waxs_range)

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5,0.5)

 
def gFak1(meas_t=1):
        username = 'AZ'
        names1 = 'aaA_20190926_OG_hot'
        
        dets = [pil1M,pil300KW, rayonix]
        angle_offset = [0.1]
        length = 17000
        x_edge = 31000 #make sure to define the edge as a top border of the sample on the camera using SmarAct X
        x_step = 4000
        nb_pt = (length - 500) // x_step
        xlocs1 = []
        for step in range(0, nb_pt+1, 1):
            xlocs1 += [np.round(x_edge - step * x_step)]

        #what we run now
        curr_tray = xlocs1
        waxs_range = [0, 13, 3]
        
        yield from bps.mv(piezo.x, x_edge)
        yield from bps.mv(piezo.th, 0.1)
        yield from alignement_gisaxs(0.1)
        a_off = piezo.th.position
        plt.close('all')
        for i, x in enumerate(curr_tray):
            yield from bps.mv(piezo.x, x)
            if i != 0:
                yield from bps.mv(piezo.th, a_off+ angle_offset[0])
                yield from quickalign_gisaxs(0.1)
                plt.close('all')
                a_off = piezo.th.position
            for ii, an in enumerate(angle_offset):
                yield from bps.mv(piezo.th, a_off+an)
                det_exposure_time(meas_t,meas_t)
                #temper = ls.ch1_read.value
                name_fmt = '{sample}_x{xlocation}_{angl}deg'
                sample_name = name_fmt.format(sample=names1, xlocation=x, angl = an)
                sample_id(user_name=username, sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.scan(dets, waxs, *waxs_range)
                
            
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3) 

def gFak2(meas_t=1):
        username = 'YJ'
        names1 = 'aaA_20190926_OG_middle'
        
        dets = [pil1M,pil300KW, rayonix]
        angle_offset = [0.1]
        length = 21000
        x_edge = 11000 #make sure to define the edge as a top border of the sample on the camera using SmarAct X
        x_step = 4000
        nb_pt = (length - 500) // x_step
        xlocs1 = []
        for step in range(0, nb_pt+1, 1):
            xlocs1 += [np.round(x_edge - step * x_step)]

        #what we run now
        curr_tray = xlocs1
        waxs_range = [0, 13, 3]
        
        yield from bps.mv(piezo.x, x_edge)
        yield from bps.mv(piezo.th, 0.1)
        yield from alignement_gisaxs(0.1)
        a_off = piezo.th.position
        plt.close('all')
        for i, x in enumerate(curr_tray):
            yield from bps.mv(piezo.x, x)
            if i != 0:
                yield from bps.mv(piezo.th, a_off+ angle_offset[0])
                yield from quickalign_gisaxs(0.1)
                plt.close('all')
                a_off = piezo.th.position
            for ii, an in enumerate(angle_offset):
                yield from bps.mv(piezo.th, a_off+an)
                det_exposure_time(meas_t,meas_t)
                #temper = ls.ch1_read.value
                name_fmt = '{sample}_x{xlocation}_{angl}deg'
                sample_name = name_fmt.format(sample=names1, xlocation=x, angl = an)
                sample_id(user_name=username, sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.scan(dets, waxs, *waxs_range)
                
            
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3)   

def gFak3(meas_t=1):
        username = 'AZ'
        names1 = 'aaA_20190926_OG_cold'
        
        dets = [pil1M,pil300KW, rayonix]
        angle_offset = [0.1]
        length = 17000
        x_edge = -14000 #make sure to define the edge as a top border of the sample on the camera using SmarAct X
        x_step = 4000
        nb_pt = (length - 500) // x_step
        xlocs1 = []
        for step in range(0, nb_pt+1, 1):
            xlocs1 += [np.round(x_edge - step * x_step)]

        #what we run now
        curr_tray = xlocs1
        waxs_range = [0, 13, 3]
        
        yield from bps.mv(piezo.x, x_edge)
        yield from bps.mv(piezo.th, 0.1)
        yield from alignement_gisaxs(0.1)
        a_off = piezo.th.position
        plt.close('all')
        for i, x in enumerate(curr_tray):
            yield from bps.mv(piezo.x, x)
            if i != 0:
                yield from bps.mv(piezo.th, a_off+ angle_offset[0])
                yield from quickalign_gisaxs(0.1)
                plt.close('all')
                a_off = piezo.th.position
            for ii, an in enumerate(angle_offset):
                yield from bps.mv(piezo.th, a_off+an)
                det_exposure_time(meas_t,meas_t)
                #temper = ls.ch1_read.value
                name_fmt = '{sample}_x{xlocation}_{angl}deg'
                sample_name = name_fmt.format(sample=names1, xlocation=x, angl = an)
                sample_id(user_name=username, sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.scan(dets, waxs, *waxs_range)
                
            
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3,0.3) 
        
def run_all_gFak():
    yield from gFak1()
    yield from gFak2()
    yield from gFak3()
