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
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
                yield from bp.count(det, num = 1)
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
        yield from alignement_gisaxs(angle)


