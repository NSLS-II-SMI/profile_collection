def gradient_sample(exp_time):
    dets = [pil300KW, pil1M]
    sam = ['ZnTi_gradient']
    
    xst = 25500         #step 2000
    xsto = -24200
    
    waxs_arc = [2.95, 38.95, 7]
    alph_na = ['0.1', '0.2']
    alphai = [0.617, 0.717]
    
    det_exposure_time(exp_time, exp_time)
    
    x = xst
    while x > xsto:
        yield from bps.mv(piezo.x, x)
        for i, ai in enumerate(alphai):
            yield from bps.mv(piezo.th, ai)

            name_fmt = '{sam}_xpos{x_pos}_ai{ai}deg'
            sample_name = name_fmt.format(sam=sam[0], x_pos='%5.5d'%x, ai = alph_na[i])
                
            sample_id(user_name= 'ES', sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')

            yield from bp.scan(dets, waxs, *waxs_arc)
            
        x -= 200



def MOF_measure(exp_time):
    dets = [pil300KW, pil1M]
    names = ['E07_130nm', 'F07_70nm']#, 'Ref_ZnO']
    #names = ['Ref_ZnO_npos']
    xs = [30000, 0]
    
    inc_angle = [0.10, 0.15, 0.20]
    waxs_arc = [2.93, 26.93, 5]
    for name, x in zip(names, xs):
        yield from bps.mv(piezo.x, x)
        yield from alignement_gisaxs(angle = 0.15)
        yield from bps.mvr(piezo.th, -0.15)
        
        for incident_angle in inc_angle:
            name_fmt = '{sample}_{angle}deg'
            yield from bps.mvr(piezo.th, incident_angle)
            sample_name = name_fmt.format(sample=name, angle=incident_angle)
            sample_id(user_name='GF', sample_name=sample_name)
            det_exposure_time(exp_time, exp_time)
            yield from bp.scan(dets, waxs, *waxs_arc)
            yield from bps.mvr(piezo.th, -incident_angle)
        
def guigui(meas_t=0.3):
        det = [pil1M]
        '''
        names = ['Diag_ver_10-50nm', 'DX_10-50nm',
        'Diag_ver_2-8nm', 'DX_2-8nm',
        'CDUp_10-50nm', 'CDUm_10-50nm', 'Mxp_10-50nm', 'Mx-_10-50nm',
        ]
              
        x = [11200, 11200, 11200, 5900, 627, -4873, -4873, -4873]
        y = [-2660, 2450,  7749,  7749, 7749,-2660,  2450,  7749]

        
        names = ['CDUp_2-8nm', 'CDUm_2-8nm', 'Mxp_2-8nm', 'Mx-_2-8nm',
        ]
              
        x = [11550, 7250, 2050, -3350]
        y = [8758, 8758, 8758]

        names = ['Mx-_2-8nm']
              
        x = [-3350]
        y = [8758]
        '''
        names = ['Mx-_2-8nm', 'Mxp_2-8nm', 'CDUm_2-8nm','CDUp_2-8nm', 'Mx-_10-50nm', 'Mxp_10-50nm', 'CDUm_10-50nm','CDUp_10-50nm', 'Diag_ver_2-8nm', 'DX_2-8nm','Diag_ver_10-50nm', 'DX_10-50nm']
        x = [11550, 7250, 2050, -3350, 11550, -3350, 11550, -3350, 11550,  7250,  2050, -3350]
        y = [8758,  8758, 8758,  8758, 3458,   3458, 3458,   3458, -1742, -1742, -7041, -7041 ]
        
        for a in range(0, 12, 1):
                yield from bps.mv(piezo.x, x[a])
                yield from bps.mv(piezo.y, y[a])
                yield from align_gui()
                plt.close('all')
                det_exposure_time(meas_t)
                name_fmt = '{sample}_{num}'
                sample_name = name_fmt.format(sample=names[a], num=a)
                sample_id(user_name='GF_11.8keV_8.3m_ref', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(det, num = 1)



        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5)

def align_gui():
        det_exposure_time(0.5)
        sample_id(user_name='test', sample_name='test')
        yield from bps.mv(pil1M.roi1.min_xyz.min_x,162)
        yield from bps.mv(pil1M.roi1.size.x, 20)
        yield from bps.mv(pil1M.roi1.min_xyz.min_y,895)
        yield from bps.mv(pil1M.roi1.size.y, 20)
        
        
        yield from align_x(250, 30, der=True)     
        yield from align_y(250, 30, der=True)

                  
def align_gisaxs_height(  rang = 0.3, point = 31 ,der=False  ):     
        yield from bp.rel_scan([pil1M], piezo.y, -rang, rang, point )
        ps(der=der)
        yield from bps.mv(piezo.y, ps.cen)

def align_gisaxs_th(  rang = 0.3, point = 31   ):             
        yield from bp.rel_scan([pil1M], piezo.th, -rang, rang, point )
        ps()
        yield  from bps.mv(piezo.th, ps.peak)  
        
def test_test(angle = 0.15):      
        yield from remove_suspender( susp_xbpm2_sum )

        
        
## SMI config file
import pandas as pds


def optics_config_save():
    '''
    Save the optics configuration for a given set-up
    Save a panda DataFrame to track the evolution with time
    '''
    #TODO: Do a list of a what motor we need to be stored
    #Cryocooler, HFM/VFM/VDM Stripe, SSA position, Slits and etc


def optics_config_load():
    '''
    Load the optics configuration for a given set-up
    Allow to move to the previous motor position
    '''
    #TODO: Do a list of a what motor we need to be stored
        
            
def calc_metadata():
    #TODO: List of metadata needed for the analysis
    #SDD, Energy, Direct beam, BS_position, waxs_arc_pos, detector, geometry, alphai
    
    read_bs_x = yield from bps.read(pil1m_bs_rod.x)


def test_test():
    yield from move_new_config('16p1keV_microfocused')
    
    
def waxs_S_edge_guil(t=1):
    dets = [pil300KW]
    

    names = ['sample02', 'sample03', 'sample04', 'sample05', 'sample06', 'sample07', 'sample08', 'sample09', 'sample10', 'sample11', 'sample12']
    x = [26500, 21500, 16000, 10500, 5000, 0, -5500, -10500, 16000, -21000, -26500]#, -34000, -41000]
    y = [600, 600, 800, 700, 700, 600, 600, 600, 600, 900, 900]#, 700, 800]

    
    energies = np.linspace(2450, 2500, 26)
    waxs_arc = [0, 6.5, 13]
    
    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        
        yss = np.linspace(ys, ys + 1300, 26)
        
        if int(waxs.arc.position) == 0:
                waxs_arc = [0, 6.5, 13]
        elif int(waxs.arc.position) == 13:
                waxs_arc = [13, 6.5, 0]
        
        if name == 'sample02':
            waxs_arc = [6.5, 0]
        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}'
            for e, ysss in zip(energies, yss): 
                yield from bps.sleep(1)
                yield from bps.mv(energy, e)
                yield from bps.mv(piezo.y, ysss)
                sample_name = name_fmt.format(sample=name, energy=e, wax = wa)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

       
            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)


    
def gratings_S_edge(t=1):
    dets = [pil300KW]
    
    names = ['1908_J3030_40p20cd']
    
    energies = [2400, 2432, 2433, 2434, 2435, 2436, 2437, 2438, 2439, 2440, 2441, 2442, 2443, 2444, 2445, 2446, 2447, 2448, 2449, 2450]
    
    for name in names:
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)


def gratings_Sn_edge(t=1):
    dets = [pil300KW]
    
    names = ['1908_YAHY_40p11cd']
    
    energies = [3900, 3920, 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3940]
    
    for name in names:
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_ai0.7deg'
        for e in energies:                              
            yield from bps.mv(energy, e)
            sample_name = name_fmt.format(sample=name, energy=e)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)


def nikhil_Zn_edge(t=1):
    dets = [pil300KW, pil300kwroi2]
    
    names = ['Zn0_unexposed', 'Zn0_exposed']
    xs = [14000, -8000]
    
    energies = np.linspace(9620, 9700, 81)
    
    for x, name in zip(xs, names):
        bps.mv(piezo.x, x)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_{energy}eV_ct{xbpm}_ai0.1deg'
        for e in energies:                              
            yield from bps.mv(energy, e)
            xbpm = xbpm3.sumX.value
            sample_name = name_fmt.format(sample=name, energy=e, xbpm ='%3.2f'%xbpm)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            #yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 9680)
        yield from bps.mv(energy, 9660)
        yield from bps.mv(energy, 9640)
        yield from bps.mv(energy, 9620)
        
        




def meas_gels(t=1):
    dets = [pil300KW, pil1M]
    
    names = ['DIwater', 'bkg_wat']
    #names = ['sam48', 'sam49', 'sam50', 'sam51', 'sam52', 'sam53', 'sam54']
    xs = [27000, -15000]
    
    waxs_arc = [0, 13, 3]
    
    for x, name in zip(xs, names):
        yield from bps.mv(piezo.x, x)
        det_exposure_time(t,t) 
        name_fmt = '{sample}_16p1keV_8p3m_'
        sample_name = name_fmt.format(sample=name)
        sample_id(user_name='GF', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.scan(dets, waxs, *waxs_arc)
        




def sin_generation():
    x = np.linspace(0, 30000, 30000)
    gx = 50000 * np.sin(x/5)  #20000, 15000, 6000

    # plt.figure()
    # plt.plot(x, gx)
    # plt.show()

    for gs in gx:
        yield from bps.sleep(0.01)
        trigger_signal = 'XF:12IDB-BI:2{EM:BPM3}fast_pidY.VAL'
        yield from bps.mv(trigger_signal, gs)



def run_Liheng(t=1): 
    # samples = ['LBBL_0.09_sdd8.3m_16.1keV', 'LBBL_0.32_sdd8.3m_16.1keV']

    # x_list  = [37000, 24000]
    # y_list =  [-200, -200]

    # # Detectors, motors:
    # dets = [pil1M]
    # assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    # assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'
    
    # ypos = [0, 200, 2]

    # det_exposure_time(t,t)
    # for x, y, sample in zip(x_list,y_list,samples):
    #     yield from bps.mv(piezo.x, x)
    #     yield from bps.mv(piezo.y, y)
    #     sample_id(user_name='LC', sample_name=sample) 
    #     yield from bp.rel_scan(dets, piezo.y, *ypos)
    #     # yield from bp.count(dets, num=3)
          

    samples = ['LhBBL_1.08', 'LhBBL_0.94', 'LhBBL_0.84', 'glass_only']

    x_list  = [-4500, -20000, -32000, -37000 ]
    y_list =  [-500, -500, -500, -500]

    ypos = [0, 200]

    waxs_range = np.linspace(13, 0, 3)
    det_exposure_time(t,t)
    dets = [pil1M, pil300KW]

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)

        for x, y, sample in zip(x_list,y_list, samples):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)

            for yy, y_of in enumerate(ypos):        
                yield from bps.mv(piezo.y, y+y_of)
            
                name_fmt = '{sam}_wa{waxs}_yloc{yy}'
                sample_name = name_fmt.format(sam=sample, yy='%2.2d'%yy, waxs='%2.1f'%wa)
                sample_id(user_name='LC', sample_name=sample_name) 


                yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)



def batch_caps(t=1): 
    samples = [
    '0.5RLPF',  '0.5RLPW',   '1.0RLPW',    'W2F2-G6',  'W2F-GL',  'W2F4-G6', 'W2F3-G6', 
       '0.5RLPF_4AC','0.5RLPW_4AC','1.0RLPW_4AC', 'W2F3-G8', 'F3Y3-G8', 'W2F6-G8', 

    # 'S2_CuHHTT_TEBF4_Soaked', 'S3_CuHHTT_KNO2_Soaked', 'S5_CuHHTT_TEBF4_Pos', 'S6_CuHHTT_KNO2_Pos','S7_CuHHTT_CsBr_Pos','S9_CuHHTT_KNO2_Neg','S10_CuHHTT_CsBr_Neg'
    # 'S2_CuHHTT_TEBF4_Bare','S4_CuHHTT_CsBr_Soaked','S8_CuHHTT_TEBF4_Neg','S11',
    ]

    x_list  = [38110, 31700, 25500, 18810, 12640, 6420, -2000,
                   35600, 29260, 22920, 16400, 10230, 2370, 
    # -6600, -13000, -19800, -26000, -32400, -38500, -44800, 
    # -9250, -21950, -28200, -34500, 
    ]

    y_list =  [1100, 1100, 1100, 1100, 1100, 1100, 1100,
                1100, 1100, 1100, 1100, 1100, 1100, 
    # 2000, 2000, 2000, 2000, 2000, 1000, 2000, 
    # 2000, 2000, 2000, 2000, 
    ]
    
    z_list = [2600, 2600, 2600, 2600, 2600, 2600, -1400,
                11600, 11600, 11600, 11600, 11600, 11600,
    # 2600, 2600, 2600, 2600, 2600, 2600, 2600,
    # 11600, 11600, 11600, 11600, 
    ]

    # Detectors, motors:
    dets = [pil1M]
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'
    assert len(x_list) == len(z_list), f'Number of X coordinates ({len(x_list)}) is different from number of Z coord ({len(z_list)})'
    ypos = [0, 50, 2]

    det_exposure_time(t,t)
    for x, y, z, sample in zip(x_list,y_list,z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)
        sample_id(user_name='KK_sdd1.8m', sample_name=sample) 
        yield from bp.rel_scan(dets, piezo.y, *ypos)
        # yield from bp.count(dets, num=3)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)

def batch_caps_yugang(t=1): 
    samples = [
    # '2', '3', '5', '6',  '7',  '9', '10', 
    #    '1',     '4', '8',  '11',  

    'S2_CuHHTT_TEBF4_Soaked', 'S3_CuHHTT_KNO2_Soaked', 'S5_CuHHTT_TEBF4_Pos', 'S6_CuHHTT_KNO2_Pos','S7_CuHHTT_CsBr_Pos','S9_CuHHTT_KNO2_Neg','S10_CuHHTT_CsBr_Neg',
    'S2_CuHHTT_TEBF4_Bare','S4_CuHHTT_CsBr_Soaked','S8_CuHHTT_TEBF4_Neg','S11'
    ]

    x_list  = [
        # 38110, 31700, 25500, 18810, 12640, 6420, -2000,
        #            35600,        22920, 16400, 10230, 
    -6520, -12920, -19680, -25860, -32260, -38440, -44740, 
    -8970, -21650, -27940, -34270, 
    ]

    y_list =  [
        # 600, 600, 600, 600, 600, 600, 600,
        #           600,      600, 600, 600,  
    2000, 2000, 2000, 2000, 2000, 1000, 2000, 
    2000, 2000, 2000, 2000
    ]
    
    z_list = [
        # 2600, 2600, 2600, 2600, 2600, 2600, -1400,
        #         11600, 11600, 11600, 11600, 11600, 11600,
    2600, 2600, 2600, 2600, 2600, 2600, 2600,
    11600, 11600, 11600, 11600
    ]

    # Detectors, motors:
    dets = [pil1M]
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    assert len(x_list) == len(y_list), f'Number of X coordinates ({len(x_list)}) is different from number of Y coord ({len(y_list)})'
    assert len(x_list) == len(z_list), f'Number of X coordinates ({len(x_list)}) is different from number of Z coord ({len(z_list)})'
    ypos = [0, 50, 2]

    det_exposure_time(t,t)
    for x, y, z, sample in zip(x_list,y_list,z_list, samples):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)
        sample_id(user_name='YZ', sample_name=sample) 
        yield from bp.rel_scan(dets, piezo.y, *ypos)
        # yield from bp.count(dets, num=3)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)



def run_night_gui():
    # proposal_id('2020_3', '307283_Zhang3')
    # yield from song_waxs_Sedge_2020_3(1)

    proposal_id('2020_3', '307283_Zhong2')
    yield from waxs_S_edge_wenkai(1)

    proposal_id('2020_3', '305401_Gomez2')
    yield from NEXAFS_S_edge(0.5)
    yield from gomez_S_edge(1)

    proposal_id('2020_3', '000000_Su')
    yield from Su_nafion_waxs_S_edge(1)
    yield from Su_nafion_waxs_S_edge_extra(0.5)



def song_waxs_Sedge_2020_3(t=1):
    
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1 )

    dets = [pil300KW]
    waxs_arc = np.linspace(0, 19.5, 4)
    energies = np.linspace(2460, 2490, 16)

    yield from bps.mv(stage.th, 0)
    yield from bps.mv(stage.y, 0)

    names = ['G4', 'H1', 'H2', 'H3', 'H4', 'H5']
    x = [44250, 38900, 32300, 26300, 20300, 14300]
    y = [-2450, -2450, -2350, -2350, -2350, -2350]
    z = [2700,  2700,  2700,   2700,  2700,  2700]

    for name, xs, ys, zs in zip(names, x, y, z):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yss = np.linspace(ys, ys + 500, 8)
        xss = np.linspace(xs, xs + 250, 2)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                try: 
                    yield from bps.mv(energy, e)
                except:
                    print('energy failed to move, sleep for 30 s')
                    yield from bps.sleep(30)
                    print('Slept for 30 s, try move energy again')
                    yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2475)
            yield from bps.mv(energy, 2460)




def waxs_S_edge_wenkai(t=1):
    
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1 )

    dets = [pil300KW]

    names = ['Rxbai-P', 'Rxbai-C']
    x = [-9500, -16000]
    y = [-2500, -2500]
    z = [2700, 2700]

    names = ['Rxbai-C']
    x = [-16000]
    y = [-2500]
    z = [2700]
    
    energies = np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist()
    waxs_arc = np.linspace(19.5, 39, 4)

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 29)
        xss = np.array([xs, xs + 500])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                try: 
                    yield from bps.mv(energy, e)
                except:
                    print('energy failed to move, sleep for 30 s')
                    yield from bps.sleep(30)
                    print('Slept for 30 s, try move energy again')
                    yield from bps.mv(energy, e)
                
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='WZ', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def NEXAFS_S_edge(t=0.5):
    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1 )

    yield from bps.mv(waxs, 52)
    dets = [pil300KW]
    names = ['sample1', 'sample2', 'sample3']
    x = [9300, 3900, -2000]
    y = [-2100, -2100, -1900]


    energies = np.linspace(2430, 2500, 71)
    
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        for e in energies:                              
            try: 
                yield from bps.mv(energy, e)
            except:
                print('energy failed to move, sleep for 30 s')
                yield from bps.sleep(30)
                print('Slept for 30 s, try move energy again')
                yield from bps.mv(energy, e)        
            yield from bps.sleep(1)

            sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, xbpm = '%3.1f'%xbpm3.sumY.value)
            sample_id(user_name='SR', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)
        
        yield from bps.mv(energy, 2470)
        yield from bps.mv(energy, 2450)
  

def gomez_S_edge(t=1):

    yield from bps.mv(GV7.close_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.close_cmd, 1 )

    dets = [pil300KW]

    energies = [2456, 2464, 2472, 2477, 2478, 2479, 2490, 2492]
    waxs_arc = np.linspace(0, 26, 5)

    yield from bps.mv(stage.th, 0)
    yield from bps.mv(stage.y, 0)

    names = ['sample1', 'sample2', 'sample3']
    x = [9100, 3700, -1800]
    y = [-2100, -2100, -1900]
    

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 400, 8)
        xss = np.array([xs])

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                try: 
                    yield from bps.mv(energy, e)
                except:
                    print('energy failed to move, sleep for 30 s')
                    yield from bps.sleep(30)
                    print('Slept for 30 s, try move energy again')
                    yield from bps.mv(energy, e)   
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)





def giwaxs_ashwant_(t=1):

    samples = [ 'sample5.0per', 'sample7.5per', 'sample10per', 'sample15per', 'sample20per']
    x_list = [43000, 26000, 7000, -13000, -32000]

    waxs_arc = np.linspace(0, 19.5, 4)
    angle = [0.45, 0.5]

  # Detectors, motors:
    dets = [pil1M, pil300KW]
    
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    for x, sample in zip(x_list,samples):
        yield from bps.mv(piezo.x, x)
        yield from alignement_gisaxs(angle = 0.3)

        # yield from bps.mv(att2_9, 'Insert')
        # yield from bps.sleep(5)
        # yield from bps.mv(att2_9, 'Insert')

        ai0 = piezo.th.position

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            det_exposure_time(t, t) 
            name_fmt = '{sample}_3.33keV_ai{angle}deg_wa{wax}'
        
            for an in angle:
                yield from bps.mv(piezo.th, ai0 + an)
                sample_name = name_fmt.format(sample=sample, angle='%3.3f'%an, wax = '%2.2d'%wa)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3,0.3)


def NEXAFS_Ag_edge(t=0.5):
    yield from bps.mv(waxs, 52)

    dets = [pil300KW]
    energies = np.linspace(3330, 3450, 121)

    name = 'nexafs_sample20per'

    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_xbpm{xbpm}'
    for e in energies:                              
        try: 
            yield from bps.mv(energy, e)
        except:
            print('energy failed to move, sleep for 30 s')
            yield from bps.sleep(30)
            print('Slept for 30 s, try move energy again')
            yield from bps.mv(energy, e)
        yield from bps.sleep(1)
        sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
        sample_id(user_name='SR', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)


def Su_nafion_waxs_hard(t=1):
    dets = [pil300KW, pil1M]

    waxs_arc = np.linspace(0, 32.5, 6)

    yield from bps.mv(stage.y, 0)
    yield from bps.mv(stage.th, 0)

    names = ['30nPA', '50nPA']
    x = [12500, -15500]
    y = [-300,  -300]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)

            det_exposure_time(t,t) 
            name_fmt = '{sample}_16100eV_sdd8.3_wa{wax}'
            sample_name = name_fmt.format(sample=name, wax = wa)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    yield from bps.mv(stage.th, 1.5)
    yield from bps.mv(stage.y, -8)
    
    names = ['70nPA', 'Nafion_xl']
    x = [32000, 1000]
    y = [-9000, -9000]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)  

            det_exposure_time(t,t) 
            name_fmt = '{sample}_16100eV_sdd8.3_wa{wax}'
            sample_name = name_fmt.format(sample=name, wax = wa)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)


def sara_nafion_waxs_hard(t=1):
    dets = [pil300KW, pil1M]

    waxs_arc = np.linspace(0, 32.5, 6)

    # names = ['10nPA_sol', '30nPA_sol', '50nPA_sol', '60nPA_sol']
    # x = [-37200, -31200, -25100, -12200]
    # y = [1000,     1000,   1000,   1000]

    names = ['capillary_empty']
    x = [760]
    y = [-9000]

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)    
        
        for name, xs, ys in zip(names, x, y):
            yield from bps.mv(piezo.x, xs)
            yield from bps.mv(piezo.y, ys)

            det_exposure_time(t,t) 
            name_fmt = '{sample}_16100eV_sdd8.3_wa{wax}'
            sample_name = name_fmt.format(sample=name, wax = wa)
            sample_id(user_name='GF', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

def Su_nafion_waxs_S_edge_extra(t=1):
    dets = [pil300KW, pil1M]

    yield from bps.mv(GV7.open_cmd, 1 )
    yield from bps.sleep(5)
    yield from bps.mv(GV7.open_cmd, 1 )

    energies = 7 + np.asarray(np.arange(2445, 2470, 5).tolist() + np.arange(2470, 2480, 0.25).tolist() + np.arange(2480, 2490, 1).tolist()+ np.arange(2490, 2501, 5).tolist())
    waxs_arc = np.linspace(0, 19.5, 4)

    yield from bps.mv(stage.th, 1.5)
    yield from bps.mv(stage.y, -9)

    names = ['70nPA_inverse', '50nPA_inverse', '30nPA_inverse', '10nPA_inverse']
    x = [42000, 19000, -3000, -27000]
    y = [-8500, -8500, -8500,  -8000]

    for name, xs, ys in zip(names, x, y):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)

        yss = np.linspace(ys, ys + 1000, 15)
        xss = np.linspace(xs, xs + 1000, 4)

        yss, xss = np.meshgrid(yss, xss)
        yss = yss.ravel()
        xss = xss.ravel()

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)    

            det_exposure_time(t,t) 
            name_fmt = '{sample}_{energy}eV_wa{wax}_bpm{xbpm}'
            for e, xsss, ysss in zip(energies, xss, yss): 
                try: 
                    yield from bps.mv(energy, e)
                except:
                    print('energy failed to move, sleep for 30 s')
                    yield from bps.sleep(30)
                    print('Slept for 30 s, try move energy again')
                    yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                yield from bps.mv(piezo.y, ysss)
                yield from bps.mv(piezo.x, xsss)

                bpm = xbpm2.sumX.value

                sample_name = name_fmt.format(sample=name, energy='%6.2f'%e, wax = wa, xbpm = '%4.3f'%bpm)
                sample_id(user_name='GF', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

            yield from bps.mv(energy, 2470)
            yield from bps.mv(energy, 2450)



def run_Ca_Oskar_2020_3(t=1):
    
    dets = [pil300KW]

    energies = [4030, 4040, 4042, 4044, 4046, 4048, 4050, 4052, 4054, 4056, 4058, 4060, 4070, 4075, 4080, 4105]
    
    det_exposure_time(t,t) 
    name_fmt = '{sample}_{energy}eV_pos{posi}_wa{wa}_xbpm{xbpm}'
    waxs_range = [0]

    det_exposure_time(t,t)

    ypos = [0, 400, 3]    
    for wa in waxs_range[::-1]:
        yield from bps.mv(waxs, wa)
        yield from bps.mv(stage.th, 0)
        yield from bps.mv(stage.y, 0)

        samples = ['J32_1', 'J32_2', 'J32_3', 'J33_1', 'J33_2', 'J33_3', 'J34_1', 'J34_2', 'J34_3', 'J34_4', 'J35_1', 'J35_2', 'J35_3', 'J35_4'][::-1]
        x_list  = [45600, 41350, 34500, 29000, 19350, 15600, 11100,  6300, -7700, -13200, -19400, -27900, -35300, -42300]
        y_list =  [-1400, -1400, -1400, -1400, -1400, -1400, -1400, -1400,  -600,  -1400,  -1400,  -1400,  -1400,  -1400]
        z_list =  [ 4000,  4000,  4000,  4000,  4000,  4000,  4000,  4000,  4000,   4000,   4000,   4000,   4000,   4000]


        for name, x, y, z in zip(samples, x_list, y_list, z_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            for k, e in enumerate(energies):                              
                # try: 
                #     yield from bps.mv(energy, e)
                # except:
                #     print('energy failed to move, sleep for 30 s')
                #     yield from bps.sleep(30)
                #     print('Slept for 30 s, try move energy again')
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.rel_scan(dets, piezo.y, *ypos)
                            
            yield from bps.mv(energy, 4080)
            yield from bps.mv(energy, 4055)
            yield from bps.mv(energy, 4030)


def run_Ca_Sintu_2020_3(t=1):
    
    dets = [pil300KW]

    det_exposure_time(t,t) 
    waxs_range = [0, 6.5, 13.0]
    energies = [4000, 4030, 4040, 4050, 4055, 4075, 4100]
    det_exposure_time(t,t)

    # ypos = [0, 400, 3]    
    # for wa in waxs_range[::-1]:
    #     yield from bps.mv(waxs, wa)
    #     yield from bps.mv(stage.th, 2)
    #     yield from bps.mv(stage.y, -13)
    
    #     samples = ['Ca', 'PL', 'PLC', 'PG3', 'PG2', 'PG1']
    #     x_list = [-14400, -19800, -25800, -30800, -36300, -41800]
    #     y_list = [ -9600,  -9700,  -9600,  -9700,  -9700,  -9700]
    #     z_list = [  2700,   2700,   2700,   2700,   2700,   2700]

    #     for name, x, y, z in zip(samples, x_list, y_list, z_list):
    #         yield from bps.mv(piezo.x, x)
    #         yield from bps.mv(piezo.y, y)
    #         yield from bps.mv(piezo.z, z)

    #         for k, e in enumerate(energies):                              
    #             # try: 
    #             #     yield from bps.mv(energy, e)
    #             # except:
    #             #     print('energy failed to move, sleep for 30 s')
    #             #     yield from bps.sleep(30)
    #             #     print('Slept for 30 s, try move energy again')
    #             yield from bps.mv(energy, e)
    #             yield from bps.sleep(1)

    #             name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

    #             sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
    #             sample_id(user_name='OS', sample_name=sample_name)
    #             print(f'\n\t=== Sample: {sample_name} ===\n')
    #             yield from bp.rel_scan(dets, piezo.y, *ypos)
                            
    #         yield from bps.mv(energy, 4080)
    #         yield from bps.mv(energy, 4055)
    #         yield from bps.mv(energy, 4030)


    for wa in waxs_range[::-1]:
        yield from bps.mv(waxs, wa)
        yield from bps.mv(stage.th, 2)
        yield from bps.mv(stage.y, -13)
    
        samples = ['O5Ca1', 'O5Ca2', 'O5Ca3']
        x_list = [ 6800,   500, -6800]
        y_list = [-9700, -9700, -9700]
        z_list = [ 2700,  2700,  2700]

        for name, x, y, z in zip(samples, x_list, y_list, z_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            xss = np.linspace(x, x + 1200, 6)
            yss = np.linspace(y, y + 300, 6)

            yss, xss = np.meshgrid(yss, xss)
            yss = yss.ravel()
            xss = xss.ravel()

            xss1 = np.linspace(x, x + 600, 6)
            yss1 = np.linspace(y + 600, y + 600 + 150, 6)

            yss1, xss1 = np.meshgrid(yss1, xss1)
            yss1 = yss1.ravel()
            xss1 = xss1.ravel()

            for k, e in enumerate(energies):                              
                # try: 
                #     yield from bps.mv(energy, e)
                # except:
                #     print('energy failed to move, sleep for 30 s')
                #     yield from bps.sleep(30)
                #     print('Slept for 30 s, try move energy again')
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)

                name_fmt = 'bigmap_{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')

                print(xss)
                print(yss)


                yield from bp.list_scan(dets, piezo.x, xss.tolist(), piezo.y, yss.tolist())

                name_fmt = 'smallmap_{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.list_scan(dets, piezo.x, xss1.tolist() , piezo.y, yss1.tolist())

                # yield from bp.rel_grid_scan(dets, piezo.x, xss1, piezo.y, yss1)
                            
            yield from bps.mv(energy, 4080)
            yield from bps.mv(energy, 4055)
            yield from bps.mv(energy, 4030)
        

def run_Ca_esther_2020_3(t=1):
    proposal_id('2020_3', '000000_Esther')

    dets = [pil300KW]

    det_exposure_time(t,t) 
    waxs_range = [0, 6.5, 13.0, 19.5, 26]
    energies = [4020, 4030, 4040, 4042, 4044, 4046, 4048, 4050, 4052, 4054, 4056, 4058, 4060, 4070, 4075, 4080, 4105]
    det_exposure_time(t,t)

    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        yield from bps.mv(stage.th, 2)
        yield from bps.mv(stage.y, -13)
    
        samples = ['sample9']
        x_list = [-45400]
        y_list = [ -9400]
        z_list = [  2700]

        for name, x, y, z in zip(samples, x_list, y_list, z_list):
            yield from bps.mv(piezo.x, x)
            yield from bps.mv(piezo.y, y)
            yield from bps.mv(piezo.z, z)

            ys = np.linspace(y, y + 800, 16)

            for k, (e, yy) in enumerate(zip(energies, ys)):
                # try: 
                #     yield from bps.mv(energy, e)
                # except:
                #     print('energy failed to move, sleep for 30 s')
                #     yield from bps.sleep(30)
                #     print('Slept for 30 s, try move energy again')
                yield from bps.mv(energy, e)
                yield from bps.sleep(1)
                yield from bps.mv(piezo.y, yy)

                name_fmt = '{sample}_{energy}eV_xbpm{xbpm}_wa{wa}'

                sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value, wa='%2.1f'%wa)
                sample_id(user_name='OS', sample_name=sample_name)
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)
                            
            yield from bps.mv(energy, 4080)
            yield from bps.mv(energy, 4055)
            yield from bps.mv(energy, 4030)


    dets = [pil300KW]
    yield from bps.mv(waxs, 52)
    yield from bps.mv(stage.th, 2)
    yield from bps.mv(stage.y, -13)
    

    yield from bps.mv(att2_10, 'Retract')
    yield from bps.sleep(1)
    yield from bps.mv(att2_10, 'Retract')
    yield from bps.sleep(1)

    energies = np.linspace(4000, 4100, 101)
    det_exposure_time(0.5, 0.5) 
    name_fmt = 'nexafs2_{sample}_{energy}eV_xbpm{xbpm}'
    

    samples = ['sample9']
    x_list = [-45400]
    y_list = [ -9400]
    z_list = [  2700]

    for name, x, y, z in zip(samples, x_list, y_list, z_list):
        yield from bps.mv(piezo.x, x)
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.z, z)
        for e in energies:                              

            sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
            RE.md['filename'] = sample_name
            sample_id(user_name='OS', sample_name=sample_name)
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

        yield from bps.mv(energy, 4125)
        yield from bps.mv(energy, 4100)        
        yield from bps.mv(energy, 4075)
        yield from bps.mv(energy, 4050)
        yield from bps.mv(energy, 4030)


        # proposal_id('2020_3', '305401_Gomez4')
        # energies = np.linspace(4030, 4150, 121)
        # det_exposure_time(0.5, 0.5) 
        # name_fmt = 'nexafs_{sample}_{energy}eV_xbpm{xbpm}'
        
        # samples = ['Ca', 'PL', 'PLC', 'PG3', 'PG2', 'PG1']
        # x_list = [-14400, -19800, -25800, -30800, -36300, -41800]
        # y_list = [ -9600,  -9700,  -9600,  -9700,  -9700,  -9700]
        # z_list = [  2700,   2700,   2700,   2700,   2700,   2700]

        # for name, x, y, z in zip(samples, x_list, y_list, z_list):
        #     yield from bps.mv(piezo.x, x)
        #     yield from bps.mv(piezo.y, y)
        #     yield from bps.mv(piezo.z, z)
        #     for e in energies:                              
        #         # try: 
        #         #     yield from bps.mv(energy, e)
        #         # except:
        #         #     print('energy failed to move, sleep for 30 s')
        #         #     yield from bps.sleep(30)
        #         #     print('Slept for 30 s, try move energy again')
        #         yield from bps.mv(energy, e)
        #         yield from bps.sleep(1)

        #         sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%3.1f'%xbpm3.sumY.value)
        #         RE.md['filename'] = sample_name
        #         sample_id(user_name='OS', sample_name=sample_name)
        #         print(f'\n\t=== Sample: {sample_name} ===\n')
        #         yield from bp.count(dets, num=1)

        #     yield from bps.mv(energy, 4125)
        #     yield from bps.mv(energy, 4100)        
        #     yield from bps.mv(energy, 4075)
        #     yield from bps.mv(energy, 4050)
        #     yield from bps.mv(energy, 4030)


def run_night_Ca(t = 1):
    # yield from run_Ca_Oskar_2020_3(t)

    # yield from run_Ca_Sintu_2020_3(t)

    yield from run_Ca_esther_2020_3(t)
    


def nexafs_Se(t = 0.5):
    energies = np.linspace(12600, 12700, 101)
    det_exposure_time(0.5, 0.5) 
    name_fmt = 'nexafs_{sample}_{energy}eV_xbpm{xbpm}'
    dets = [pil300KW]

    name = 'J2_04' 

    for e in energies:                              
        # try: 
        #     yield from bps.mv(energy, e)
        # except:
        #     print('energy failed to move, sleep for 30 s')
        #     yield from bps.sleep(30)
        #     print('Slept for 30 s, try move energy again')
        yield from bps.mv(energy, e)
        yield from bps.sleep(1)

        sample_name = name_fmt.format(sample=name, energy=e, xbpm = '%1.2f'%xbpm3.sumY.value)
        RE.md['filename'] = sample_name
        sample_id(user_name='OS', sample_name=sample_name)
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)



def add_sample(bar):
    sample = {}
    sample
    piezo.x.position
