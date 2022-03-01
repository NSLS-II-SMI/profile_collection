#from tracemalloc import _TraceTupleT


def sample_alignment():
    yield from bps.mvr(piezo.th, -1)
    yield from quickalign_gisaxs(angle = 0.15)
    yield from bps.mvr(piezo.th, 1)
    yield from bps.mv(waxs, 10.3)

    ais.append([piezo.th.position])
    ys.append([piezo.y.position])



#def temp_align(cycle,temp):
def temp_align_waxs(temp):
    yield from bps.mv(waxs, 10.3)

    ai_offset = [  0,    -0.00049,   -0.010885,   -0.020069,   -0.027797,   -0.029081,   -0.038985,   -0.040642,   -0.045495,   -0.046898,  -0.050634,  -0.051935,
           -0.062148,   -0.069523,   -0.072856,    -0.07382,   -0.082091,   -0.089965,   -0.088196]
    y_offset =  [  0,  1.3417e+01, -2.9000e-02, -4.1000e-02, -5.4000e-02, -6.3000e-02, -1.3505e+01, -1.3515e+01, -1.3541e+01, -1.3544e+01, -1.3542e+01, -1.3533e+01,
         -2.6970e+01, -2.6949e+01, -2.6897e+01, -2.6899e+01, -4.0328e+01, -5.3758e+01, -6.7181e+01]
    temp_list = [ 25, 35, 45, 55, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170]
    idx = np.argmin(abs(np.asarray(temp_list)-temp))
    
    yield from bps.mvr(piezo.th, 0.2 + ai_offset[idx])
    yield from bps.mvr(piezo.y, y_offset[idx])
    yield from bps.mvr(piezo.x, 50)

    # sample_id(user_name='DD', sample_name='2CsPbBr3-insitu_RTPost%.1f_sdd275m_ai1deg_wa10.3deg_%.1fs'%(temp, time.time()-t0))


    yield from bp.count([pil900KW])


    yield from bps.mvr(piezo.th, -0.2-ai_offset[idx])
    yield from bps.mvr(piezo.y, -y_offset[idx])


#def temp_align(cycle,temp):
def temp_align_saxs(temp):
    yield from bps.mv(waxs, 20)

    ai_offset = [  0,    -0.00049,   -0.010885,   -0.020069,   -0.027797,   -0.029081,   -0.038985,   -0.040642,   -0.045495,   -0.046898,  -0.050634,  -0.051935,
           -0.062148,   -0.069523,   -0.072856,    -0.07382,   -0.082091,   -0.089965,   -0.088196]
    y_offset =  [  0,  1.3417e+01, -2.9000e-02, -4.1000e-02, -5.4000e-02, -6.3000e-02, -1.3505e+01, -1.3515e+01, -1.3541e+01, -1.3544e+01, -1.3542e+01, -1.3533e+01,
         -2.6970e+01, -2.6949e+01, -2.6897e+01, -2.6899e+01, -4.0328e+01, -5.3758e+01, -6.7181e+01]
    temp_list = [ 25, 35, 45, 55, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170]
    idx = np.argmin(abs(np.asarray(temp_list)-temp))
    
    yield from bps.mvr(piezo.th, 0.1 + ai_offset[idx])
    yield from bps.mvr(piezo.y, y_offset[idx])
    yield from bps.mvr(piezo.x, 50)

    #sample_id(user_name='DD', sample_name='2SNPB-insitucycle_num%2.2d_kapton_quenchto%.1f_ai1deg_wa10.3deg_%.1fs'%(cycle, temp, time.time()-t0))
    # sample_id(user_name='DD', sample_name='2CsPbBr3-insitu_well_%.1f_sdd4m_ai0.2deg_wa20deg_%.1fs'%(temp, time.time()-t0))

    # if temp == 120:
    #     time.sleep(60)
    #     for t in range(0,14):
    #         yield from bp.count([pil1M, pil900KW])    
    #         time.sleep(50)
    
    # else:
    yield from bp.count([pil1M, pil900KW])

    yield from bps.mvr(piezo.th, -0.1-ai_offset[idx])
    yield from bps.mvr(piezo.y, -y_offset[idx])




def temp_ramp():
    yield from bps.mv(att2_1.open_cmd, 1)
    yield from bps.sleep(1)
    yield from bps.mv(att2_1.open_cmd, 1)
    yield from bps.sleep(1)

    yield from bps.mv(waxs, 20) #10.3 deg WAXS, 20 deg. SAXS/WAXS
    # tempz = [25, 50, 75, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    # tempz = [28, 50, 75, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    tempz = [28, 50, 75, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    for i, temp in enumerate(tempz):
        if i==0:
            t_dif = 0
        else:
            diff = tempz[i] - tempz[i-1]
            t_dif = int(diff/25*60)
   
        yield from bps.sleep(80+t_dif)
        print(temp)
        sample_id(user_name='DD', sample_name='1CsPbBr3-invacuo_WAXS_heat_cycle2_%.1f_sdd4m_ai0.2deg_wa10.3deg_%.1fs'%(temp, time.time()-t0))

        # yield from temp_align_saxs(temp)
        yield from temp_align_waxs(temp)
        

