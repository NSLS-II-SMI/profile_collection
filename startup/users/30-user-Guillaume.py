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

            yield from bp.scan(dets, waxs.arc, *waxs_arc)
            
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
            yield from bp.scan(dets, waxs.arc, *waxs_arc)
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
    
    read_bs_x = yield from bps.read(pil1m_bs.x)
    



