

def xrr_spol(t=1):
    names =  ['sample12a','sample12b']
    x_piezo = [58000, 58000]
    y_piezo = [ 6900,  6900]
    z_piezo = [    0,     0]
    ener = []

    assert len(x_piezo) == len(names), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(names)})'
    assert len(x_piezo) == len(y_piezo), f'Number of X coordinates ({len(x_piezo)}) is different from number of samples ({len(y_piezo)})'

    dets = [pil300KW]
    waxs_arc = [0]

    #This is the 2 section of the graph that we defined. This will need to be clustered in several lists
    #to accommodate attenuators changes
    ai_lists = [[np.linspace(0.03, 1.5, 50).tolist()] + \
                [np.linspace(1.5, 10, 171).tolist()]]


    for name, xs, zs, ys in zip(names, x_piezo, z_piezo, y_piezo, x_hexa):
        yield from bps.mv(piezo.x, xs)
        yield from bps.mv(piezo.y, ys)
        yield from bps.mv(piezo.z, zs)

        yield from alignement_gisaxs(angle = 0.14)
        ai0 = piezo.th.position

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)  

            det_exposure_time(t,t)

            #ai_list should be a list of list. No change of attenuation inside one list
            for k, ai_list in enumerate(ai_lists):
                ai_list = [round(1000 * x, 4) for x in ai_list]
                ai_list = np.asarray(ai_list) / 1000
                yield from calc_absorbers(num=k)

                #iterate over the angle stored in one list
                for l, ais in enumerate(ai_list):
                    yield from bps.mv(piezo.th, ai0 + ais)
                    det_exposure_time(t,t)

                    bpm = xbpm3.sumX.value
                    name_fmt = '{sample}_aiscan_{energy}keV_ai{angle}deg_wa{waxs}_abs{absorber}_bpm{bpm}'
                    sample_name = name_fmt.format(sample=name,
                                                  ai ='%4.3f'%ais,
                                                  waxs ='%2.1f'%wa,
                                                  absorber = k,
                                                  bpm = bpm)

                    sample_id(user_name='TF', sample_name=sample_name)
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)


#Might be worth introducing exposure time => can be modified for each range
def calc_absorbers(num):
    #This needs to be modified to the good attenuation
    if num==0:
        yield from bps.mv(att2_10.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_11.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att2_12.open_cmd, 1)
        yield from bps.sleep(1)

    elif num == 1:
        yield from bps.mv(att2_12.close_cmd, 1)
        yield from bps.sleep(1)

    if num == 2:
        yield from bps.mv(att2_11.close_cmd, 1)
        yield from bps.sleep(1)

    if num == 3:
        yield from bps.mv(att2_12.close_cmd, 1)
        yield from bps.sleep(1)
