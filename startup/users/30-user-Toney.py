def zihan_alignment():
    """
    Align sample using hexapod
    """
    proposal_id('2023_1', '000000_tests')

    try:
        yield from alignement_gisaxs_hex(angle=0.5, rough_y=0.5)
    except:
        yield from alignement_gisaxs_hex(angle=0.1, rough_y=0.5)

    proposal_id('2023_1', '311645_Zhang')


def zihan_giwaxs_2023_1(t=0.5, name='test', dist='unspecified'):
    """
    GIWAXS measurement on a custom stage mounted on the hexapod
    GU-311645 SAF: 310633

    Manually enter the sample name and the squeeze distance
    """


    incident_angles = [0.5, 1.5, 4.36,6.2]
    waxs_arc = [0, 20]
    user_name = "ZZ"

    # Sample flat at ai0
    ai0 = stage.th.position

    for wa in waxs_arc:
        yield from bps.mv(waxs, wa)
        
        dets = [pil900KW] #if waxs.arc.position < 15 else [pil900KW, pil1M]
        det_exposure_time(t, t)

        for ai in incident_angles:
            yield from bps.mv(stage.th, ai0 + ai)

            # Metadata
            e = energy.position.energy / 1000
            sdd = pil1m_pos.z.position / 1000
            wa = waxs.arc.position + 0.001
            wa = str(np.round(float(wa), 1)).zfill(4)

            # Sample name
            name_fmt = "{sample}_{dist}mm_{energy}keV_wa{wax}_sdd{sdd}m_ai{ai}"
            sample_name = name_fmt.format(
                sample=name,
                dist=dist,
                energy="%.2f" % e,
                wax=wa,
                sdd="%.1f" % sdd,
                ai=ai,
            )
            sample_name = sample_name.translate(
                {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =,"}
            )
            sample_id(user_name=user_name, sample_name=sample_name)
            print(f"\n\n\n\t=== Sample: {sample_name} ===")
            yield from bp.count(dets)

    yield from bps.mv(stage.th, ai0)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)


def turn_off_heating(temp=23):
    """
    Turn off the heating and set temperature to 23 deg C for Lakeshore
    """
    print(f'Setting temp to {temp} deg C and turning off the heater')
    t_kelvin = temp + 273.15
    yield from ls.output1.mv_temp(t_kelvin)
    yield from ls.output1.turn_off()

def align_gisaxs_th_zihan(rang=0.3, point=31):
    th0 = piezo.th.position
    yield from bp.rel_scan([pil1M], piezo.th, -rang, rang, point)
    try:
        ps(plot=False)
        yield from bps.mv(piezo.th, ps.peak)
    except:
        print('\n\n\n\n\Could not aligned well with theta')
    yield from bps.mv(piezo.th, th0)

def zihan_giwaxs_alignment(angle=0.1):
    """
    Quicker alignment
    """

    # Activate the automated derivative calculation
    bec._calc_derivative_and_stats = True

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)

    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique="gisaxs")

    # Set direct beam ROI
    yield from smi.setDirectBeamROI()

    # Scan theta and height
    yield from align_gisaxs_height(800, 16, der=True)
    yield from align_gisaxs_th_zihan(1.5, 27)

    # move to theta 0 + value
    yield from bps.mv(piezo.th, ps.peak + angle)

    # Set reflected ROI
    yield from smi.setReflectedBeamROI(total_angle=angle, technique="gisaxs")

    # Scan theta and height
    yield from align_gisaxs_th_zihan(0.2, 11)
    yield from align_gisaxs_height_rb(150, 16)
    yield from align_gisaxs_th_zihan(0.1, 21) 

    # Close all the matplotlib windows
    plt.close("all")

    # Return angle
    yield from bps.mv(piezo.th, ps.cen - angle)
    yield from smi.modeMeasurement()

    # Deactivate the automated derivative calculation
    bec._calc_derivative_and_stats = False

def zihan_quick_alignment(angle=0.15):
    """
    Short alignement with only alignement on the reflected beam.
    """

    # Activate the automated derivative calculation
    bec._calc_derivative_and_stats = True
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)

    smi = SMI_Beamline()
    yield from smi.modeAlignment()

    # move to theta 0 + value
    yield from bps.mvr(piezo.th, angle)

    # Set reflected ROI
    yield from smi.setReflectedBeamROI(total_angle=angle)

    # Scan theta and height
    yield from align_gisaxs_height_rb(200, 31)
    yield from align_gisaxs_th_zihan(0.1, 21)

    # Close all the matplotlib windows
    plt.close("all")

    # Return angle
    yield from bps.mv(piezo.th, ps.cen - angle)
    yield from smi.modeMeasurement()

    # Deactivate the automated derivative calculation
    bec._calc_derivative_and_stats = False


def zihan_temperature_giwaxs_2023_1(t=0.5):
    """
    Hard X-ray GIWAXS Lakeshore heating stage.
    """

    names =   [ 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'CS1S', 'CS2S', 'CS3S', 'CS4S']
    piezo_x = [ 52900,  43950, 32900, 22900, 12900, 2900, -7100, -17100, -28100, -38100, -47100 ]   
    piezo_y = [       -100, -100, -100, -100]
    piezo_z = [4500 for n in names]
    # piezo_z = [4200, 4100, ]

    assert len(names)   == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x) == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_z), f"Wrong list lenghts"

    user_name = "ZZ"
    temperatures = [#25, 30, 40, 50, 60, 
                    80, 100, 80, 60, 40, 25,
                    40, 60, 80, 100, 120, 140,
                    120, 100, 80, 60, 40, 25] 
    
    waxs_arc = [0, 20]
    incident_angles = [0.50, 1.50, 4.36, 6.20]
    piezo_x_offs = [0, 200, 500]

    ai0 = piezo.th.position

    for p, temperature in enumerate(temperatures):
        t_kelvin = temperature + 273.15
        yield from ls.output1.mv_temp(t_kelvin)

        # Activate heating range in Lakeshore
        if temperature < 50:
            yield from bps.mv(ls.output1.status, 1)
        else:
            yield from bps.mv(ls.output1.status, 3)

        # Equalise temperature
        print(f"Equalising temperature to {temperature:.0f} deg C")
        start = time.time()
        temp = ls.input_A.get()
        while abs(temp - t_kelvin) > 5:
            print("Difference: {:.1f} K".format(abs(temp - t_kelvin)))

            yield from bps.sleep(10)
            temp = ls.input_A.get()
            
            # Escape the loop if too much time passes
            if time.time() - start > 10 * 60:
                temp = t_kelvin
        print(
            "Time needed to equilibrate: {:.1f} min".format((time.time() - start) / 60)
        )

        # Wait extra time depending on temperature
        #if (56 < temperature) and (temperature < 160):
        #    yield from bps.sleep(300)
        #elif 160 <= temperature:
        #    yield from bps.sleep(600)

        # Read T and convert to deg C
        temp_degC = ls.input_A.get() - 273.15

        for name, x, y, z in zip(names, piezo_x, piezo_y, piezo_z):
            yield from bps.mv(piezo.x, x + p * 200,
                              piezo.y, y,
                              piezo.z, z,
                              piezo.th, ai0)
            # Align sample
            yield from zihan_giwaxs_alignment(0.1)

            # Sample flat at ai0
            ai0 = piezo.th.position

            for wa in waxs_arc:
                yield from bps.mv(waxs, wa)
                dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
                det_exposure_time(t, t)

                for ai in incident_angles:
                    yield from bps.mv(piezo.th, ai0 + ai)
                    p=0
                    for i, x_off in enumerate(piezo_x_offs):
                        yield from bps.mv(piezo.x, x + p * 200 + x_off)

                        # Metadata
                        e = energy.position.energy / 1000
                        temp = str(np.round(float(temp_degC), 1)).zfill(5)
                        wa = waxs.arc.position + 0.001
                        wa = str(np.round(float(wa), 1)).zfill(4)
                        sdd = pil1m_pos.z.position / 1000


                        name_fmt = "{sample}_{temp}degC_pos{pos}_{energy}eV_wa{wax}_sdd{sdd}m_ai{ai}"
                        sample_name = name_fmt.format(
                            sample=name,
                            pos = i + 1,
                            energy="%.2f" % e,
                            temp=temp,
                            wax=wa,
                            sdd="%.1f" % sdd,
                            ai = ai,
                        )
                        sample_name = sample_name.translate(
                            {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =, "}
                        )
                        print(f"\n\n\n\t=== Sample: {sample_name} ===")
                        sample_id(user_name=user_name, sample_name=sample_name)
                        
                        yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

    # Turn off the heating and set temperature to 23 deg C
    yield from turn_off_heating()

def zihan_giwaxs_2023_1(t=0.5):
    """
    Hard X-ray GIWAXS, samples on Lakeshore heating stage but no heating.
    """

   
    names =   [  'Si', 'PET']
    piezo_x = [  -41100, -47100 ]   
    piezo_y = [   690, 690]
    piezo_z = [4500 for n in names]
    # piezo_z = [4200, 4100, ]

    assert len(names)   == len(piezo_x), f"Wrong list lenghts"
    assert len(piezo_x) == len(piezo_y), f"Wrong list lenghts"
    assert len(piezo_y) == len(piezo_z), f"Wrong list lenghts"

    user_name = "ZZ"
    
    waxs_arc = [0, 20]
    incident_angles = [0.5,1.5,4.36,6.2]
    piezo_x_offs = [0]
    temp = 25
    ai0 = piezo.th.position


    for name, x, y, z in zip(names, piezo_x, piezo_y, piezo_z):
        yield from bps.mv(piezo.x, x,
                          piezo.y, y,
                          piezo.z, z,
                          piezo.th, ai0)
        # Align sample
        yield from zihan_giwaxs_alignment(0.1)

        # Sample flat at ai0
        ai0 = piezo.th.position

        for wa in waxs_arc:
            yield from bps.mv(waxs, wa)
            dets = [pil900KW] if waxs.arc.position < 15 else [pil1M, pil900KW]
            det_exposure_time(t, t)

            for ai in incident_angles:
                yield from bps.mv(piezo.th, ai0 + ai)
                
                p=0
                for i, x_off in enumerate(piezo_x_offs):
                    yield from bps.mv(piezo.x, x + p * 200 + x_off)

                    # Metadata
                    e = energy.position.energy / 1000
                    temp = str(np.round(float(temp), 1)).zfill(5)
                    wa = waxs.arc.position + 0.001
                    wa = str(np.round(float(wa), 1)).zfill(4)
                    sdd = pil1m_pos.z.position / 1000


                    name_fmt = "{sample}_{temp}degC_pos{pos}_{energy}eV_wa{wax}_sdd{sdd}m_ai{ai}"
                    sample_name = name_fmt.format(
                        sample=name,
                        pos = i + 1,
                        energy="%.2f" % e,
                        temp=temp,
                        wax=wa,
                        sdd="%.1f" % sdd,
                        ai = ai,
                    )
                    sample_name = sample_name.translate(
                        {ord(c): "_" for c in "!@#$%^&*{}:/<>?\|`~+ =, "}
                    )
                    print(f"\n\n\n\t=== Sample: {sample_name} ===")
                    sample_id(user_name=user_name, sample_name=sample_name)
                    
                    yield from bp.count(dets)

    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)

def Zihan_wip():
    temperatures = [#25, 30, 40, 50, 60, 
            80, 100, 80, 60, 40, 25,
            40, 60, 80, 100, 120, 140,
            120, 100, 80, 60, 40, 25]
    for p, temperature in enumerate(temperatures):
        print(p)
        print(temperature)