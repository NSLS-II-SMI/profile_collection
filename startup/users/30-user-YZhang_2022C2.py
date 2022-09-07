##Collect data:

# SMI: 2022/7/9
# SAF:    Standard        Beamline 12-ID   proposal:  308052


#  proposal_id('2022_2', '308052_YZhang1')
#  proposal_id('2022_2', '308052_YZhang2')
#  proposal_id('2022_2', '308052_YZhang3')


##Run1,
# gix, move detector 1M  to x= -5, Y =  -20  , beam center is [ 453,  798     ]
# 4 m, beam stop:  2.2  paddle 289l Y: -13
#  beamstop_save()
# for heating setup of thin film, PY 3000, hexY = 1, use one post
# for thin film ex-situ, PY 2500 , hexY = 1


user_name = "YZ"
username = "YZ"

user_name = "HU"
username = "HU"


# sample_dict = {  1:  'Gao_S1_Origin', 2: 'Gao_S2_400_10min', 3: 'Gao_S3_450_10min', 4: 'Gao_S4_475_10min', 5: 'Gao_S5_500_10min',
#  6: 'Gao_S6_525_10min', 7:'Gao_S7_550_10min',
# }

# ypos = 100
# pxy_dict = {
#      1:  ( -48800, ypos  ) ,
# 2:  ( -34800, ypos  ),
# 3:   (-19800, ypos  ),
# 4: ( -6800, ypos  ),
# 5: ( 7200, ypos   ),
#  6: ( 21200,ypos ),
# 7: (   39200, ypos  )  ,
# }


sample_dict = {
    1: "D5",
    2: "D4",
    3: "D3",
    4: "D2",
    5: "D1",
    6: "I9",
    7: "I8",
    8: "I7",
    9: "I6",
    10: "I5",
    11: "I4",
    12: "I3",
    13: "I2",
    14: "I1",
    15: "S11",
    16: "S10",
    17: "S9",
    18: "S8",
    19: "S7",
    20: "S6",
    21: "S5",
    22: "S4",
    23: "S3",
    24: "S2",
    25: "S1",
}

ypos = -5300
pxy_dict = {
    1: (-41600, ypos),
    2: (-37900, ypos),
    3: (-34700, ypos),
    4: (-31200, ypos),
    5: (-27300, ypos),
    6: (-23800, ypos),
    7: (-20300, ypos),
    8: (-16500, ypos),
    9: (-12950, ypos),
    10: (-9399.94, ypos),
    11: (-5849.98, ypos),
    12: (-2300, ypos),
    13: (1250, ypos),
    14: (4900, ypos),
    15: (8450, ypos),
    16: (12200, ypos),
    17: (15750, ypos),
    18: (19300, ypos),
    19: (23150, ypos),
    20: (26700, ypos),
    21: (30250, ypos),
    22: (33800, ypos),
    23: (37550, ypos),
    24: (41100, ypos),
    25: (44650, ypos),
}


x_list = np.array(list((pxy_dict.values())))[:, 0]
y_list = np.array(list((pxy_dict.values())))[:, 1]
sample_list = np.array(list((sample_dict.values())))
ks = np.array(list((sample_dict.keys())))

##################################################
############ Some convinent functions#################
#########################################################


def run_time(t0):
    dt = (time.time() - t0) / 60
    print("The Running time is: %.2f min." % dt)


def measure_series_multi_angle_wsaxs(t=[1], waxs_angles=[0, 10, 15], dys=[0, 200]):

    """t0=time.time();measure_series_multi_angle_wsaxs();run_time(t0)"""

    ks = list(sample_dict.keys())  # [:8 ]
    maxA = np.max(waxs_angles)
    for waxs_angle in waxs_angles:
        for k in ks:
            mov_sam(k)
            for dy in dys:
                for ti in t:
                    RE.md["sample_name"] = sample_dict[k]
                    if waxs_angle == maxA:
                        RE(
                            measure_wsaxs(
                                t=ti, waxs_angle=waxs_angle, att="None", dy=dy
                            )
                        )
                    else:
                        RE(measure_waxs(t=ti, waxs_angle=waxs_angle, att="None", dy=dy))


def measure_waxs(
    t=1, waxs_angle=0, att="None", dx=0, dy=0, user_name=username, sample=None
):
    """RE( measure_waxs( sample = 'AgBH_12keV' ) )"""

    if sample is None:
        # sample = RE.md['sample']
        sample = RE.md["sample_name"]
    yield from bps.mv(waxs, waxs_angle)
    dets = [pil900KW, pil300KW]
    # att_in( att )
    if dx:
        yield from bps.mvr(piezo.x, dx)
    if dy:
        yield from bps.mvr(piezo.y, dy)
    name_fmt = "{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}"
    sample_name = name_fmt.format(
        sample=sample,
        x_pos=piezo.x.position,
        y_pos=piezo.y.position,
        z_pos=piezo.z.position,
        waxs_angle=waxs_angle,
        expt=t,
        scan_id=RE.md["scan_id"],
    )
    det_exposure_time(t, t)
    sample_id(user_name=user_name, sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    print("Collect data here....")
    yield from bp.count(dets, num=1)
    # att_out( att )
    # sample_id(user_name='test', sample_name='test')


def measure_wsaxs(
    t=1, waxs_angle=15, att="None", dx=0, dy=0, user_name=username, sample=None
):
    """RE( measure_wsaxs( sample = 'AgBH_12keV' ) )"""

    if sample is None:
        # sample = RE.md['sample']
        sample = RE.md["sample_name"]
    yield from bps.mv(waxs, waxs_angle)
    dets = [pil900KW, pil300KW, pil1M]
    if dx:
        yield from bps.mvr(piezo.x, dx)
    if dy:
        yield from bps.mvr(piezo.y, dy)
    name_fmt = "{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_det{saxs_z}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}"

    sample_name = name_fmt.format(
        sample=sample,
        x_pos=piezo.x.position,
        y_pos=piezo.y.position,
        z_pos=piezo.z.position,
        saxs_z=np.round(pil1m_pos.z.position, 2),
        waxs_angle=waxs_angle,
        expt=t,
        scan_id=RE.md["scan_id"],
    )

    det_exposure_time(t, t)
    sample_id(user_name=user_name, sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    print("Collect data here....")
    yield from bp.count(dets, num=1)
    # att_out( att )
    # sample_id(user_name='test', sample_name='test')


def measure_prs_rotate_waxs(k, wa=0, t=0.1):
    move_waxs(wa)
    rota = np.linspace(0, -90, 91)
    for ra in rota:
        RE(bps.mv(prs, ra))
        _measure_one_prs_waxs(k=k, dets=[pil900KW], t=t)


def _measure_one_prs_waxs(k, dets, t=1):
    mov_sam(k)
    sample = RE.md["sample"]
    u = sample.split("_")[0]
    if u in ["Gao", "Xu", "YM"]:
        User_name = u
        sample = "_".join(sample.split("_")[1:])
    else:
        User_name = user_name
    prsa = prs.user_readback.value
    waxs_angle = waxs.arc.user_readback.value
    name_fmt = "{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_det{saxs_y}_{saxs_z}_prs{prsa:.1f}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}"
    sample_name = name_fmt.format(
        sample=sample,
        x_pos=piezo.x.position,
        y_pos=piezo.y.position,
        z_pos=piezo.z.position,
        saxs_y=np.round(pil1m_pos.y.position, 2),
        saxs_z=np.round(pil1m_pos.z.position, 2),
        prsa=prsa,
        waxs_angle=waxs_angle,
        expt=t,
        scan_id=RE.md["scan_id"],
    )
    det_exposure_time(t, t)

    sample_id(user_name=User_name, sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    print("Collect data here....")
    RE(bp.count(dets, num=1))


def measure_prs_rotate(k, t=0.1):
    rota = np.linspace(0, -90, 91)
    for ra in rota:
        RE(bps.mv(prs, ra))
        _measure_one_prs(k=k, dets=[pil1M], t=t)


def _measure_one_prs(k, dets, t=1):
    mov_sam(k)
    sample = RE.md["sample"]
    u = sample.split("_")[0]
    if u in ["Gao", "Xu", "YM"]:
        User_name = u
        sample = "_".join(sample.split("_")[1:])
    else:
        User_name = user_name
    prsa = prs.user_readback.value
    name_fmt = "{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_det{saxs_y}_{saxs_z}_prs{prsa:.1f}_expt{expt}s_sid{scan_id:08d}"
    sample_name = name_fmt.format(
        sample=sample,
        x_pos=piezo.x.position,
        y_pos=piezo.y.position,
        z_pos=piezo.z.position,
        saxs_y=np.round(pil1m_pos.y.position, 2),
        saxs_z=np.round(pil1m_pos.z.position, 2),
        prsa=prsa,
        expt=t,
        scan_id=RE.md["scan_id"],
    )
    det_exposure_time(t, t)

    sample_id(user_name=User_name, sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    print("Collect data here....")
    RE(bp.count(dets, num=1))


## For gisaxs

smi = SMI_Beamline()


def alignement_gisaxs(angle=0.15):
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.3, 0.3)
    smi = SMI_Beamline()
    yield from smi.modeAlignment(technique="gisaxs")
    # Set direct beam ROI
    yield from smi.setDirectBeamROI()
    # Scan theta and height
    yield from align_gisaxs_height(500, 21, der=True)
    yield from align_gisaxs_th(1.5, 27)
    # yield from align_gisaxs_height(300, 11, der=True)
    # yield from align_gisaxs_th(0.5, 16)
    # move to theta 0 + value
    yield from bps.mv(piezo.th, ps.peak + angle)
    # Set reflected ROI
    yield from smi.setReflectedBeamROI(total_angle=angle, technique="gisaxs")
    # Scan theta and height
    yield from align_gisaxs_th(1.5, 31)
    # yield from align_gisaxs_th(0.2, 31)
    yield from align_gisaxs_height(150, 21)
    yield from align_gisaxs_th(0.2, 31)
    yield from align_gisaxs_th(0.025, 21)
    # Close all the matplotlib windows
    plt.close("all")
    # Return angle
    yield from bps.mv(piezo.th, ps.cen - angle)
    yield from smi.modeMeasurement()


def run_giwsaxs(
    x_list=x_list,
    sample_list=sample_list,
    t=1,
    username=username,
    inc_angles=[0.05, 0.1, 0.12, 0.15, 0.2, 0.3, 0.5],
    waxs_angles=[0, 10, 20],
    x_shift_array=[-1000, 0, 1000],
    YPOS={},
    ThPOS={},
    saxs_on=True,
    align=True,
    T=25,
):

    """RE( run_giwsaxs() )"""

    # define names of samples on sample bar
    assert len(x_list) == len(sample_list), f"Sample name/position list is borked"
    inc_angles = np.array(inc_angles)  # incident angles
    th_real = inc_angles
    waxs_angles = np.array(waxs_angles)  # arc waxs angles
    # 4*3.14/(12.39842/16.1)*np.sin((7*6.5+3.5)*3.14/360) = 6.760 A-1
    x_shift_array = np.array(x_shift_array)
    max_waxs_angle = np.max(waxs_angles)
    inverse_angle = False
    cts = 0

    for ii, (x, sample) in enumerate(
        zip(x_list, sample_list)
    ):  # loop over samples on bar
        yield from bps.mv(piezo.x, x)  # move to next sample
        if align:
            # RE( bps.mv(piezo.th, 0 ) )
            yield from alignement_gisaxs(0.15)  # run alignment routine
            YPOS[ii] = piezo.y.position
            ThPOS[ii] = piezo.th.position
            print(YPOS, ThPOS)
        else:
            yield from bps.mv(piezo.y, YPOS[ii])
            yield from bps.mv(piezo.th, ThPOS[ii])
        TH = ThPOS[ii]  # piezo.th.position
        th_meas = inc_angles + ThPOS[ii]  # piezo.th.position

        det_exposure_time(t, t)
        x_pos_array = x + x_shift_array
        if inverse_angle:
            Waxs_angles = waxs_angles[::-1]
        else:
            Waxs_angles = waxs_angles
        for waxs_angle in Waxs_angles:  # loop through waxs angles
            yield from bps.mv(waxs, waxs_angle)
            if waxs_angle == max_waxs_angle:
                if saxs_on:
                    dets = [pil900KW, pil1M, pil300KW]
                else:
                    dets = [pil900KW, pil300KW]
                print("Meausre both saxs and waxs here for w-angle=%s" % waxs_angle)
            else:
                dets = [pil900KW, pil300KW]
            for x_meas in x_pos_array:  # measure at a few x positions
                yield from bps.mv(piezo.x, x_meas)
                for i, th in enumerate(th_meas):  # loop over incident angles
                    yield from bps.mv(piezo.th, th)
                    if inverse_angle:
                        name_fmt = "{sample}_{th:5.4f}deg_waxsN{waxs_angle:05.2f}_x{x:05.2f}_y{y:05.2f}_z{y:05.2f}_det{saxs_z:05.2f}m_expt{t}s_T{T}_sid{scan_id:08d}"
                    else:
                        name_fmt = "{sample}_{th:5.4f}deg_waxsP{waxs_angle:05.2f}_x{x:05.2f}_y{y:05.2f}_z{y:05.2f}_det{saxs_z:05.2f}m_expt{t}s_T{T}_sid{scan_id:08d}"
                    sample_name = name_fmt.format(
                        sample=sample,
                        th=th_real[i],
                        waxs_angle=waxs_angle,
                        x=np.round(piezo.x.position, 2),
                        y=np.round(piezo.y.position, 2),
                        z=np.round(piezo.z.position, 2),
                        saxs_z=np.round(pil1m_pos.z.position, 2),
                        t=t,
                        T=T,
                        scan_id=RE.md["scan_id"],
                    )
                    sample_id(user_name=username, sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    # yield from bp.scan(dets, energy, e, e, 1)
                    # yield from bp.scan(dets, waxs, *waxs_arc)
                    print(dets)
                    yield from bp.count(dets, num=1)
                    # print( 'HERE#############')
        inverse_angle = not inverse_angle
        cts += 1
    yield from bps.mv(piezo.th, TH)
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5)


def run_giwsaxs2(
    x_list=x_list,
    sample_list=sample_list,
    t=1,
    username=username,
    inc_angles=[0.05, 0.1, 0.12, 0.15, 0.2, 0.3, 0.5],
    waxs_angles=[0, 10, 20],
    x_shift_array=[-1000, 0, 1000],
    YPOS={},
    ThPOS={},
    saxs_on=True,
    T=25,
):

    """RE( run_giwsaxs2() )"""

    # define names of samples on sample bar
    assert len(x_list) == len(sample_list), f"Sample name/position list is borked"
    inc_angles = np.array(inc_angles)  # incident angles
    th_real = inc_angles
    waxs_angles = np.array(waxs_angles)  # arc waxs angles
    # 4*3.14/(12.39842/16.1)*np.sin((7*6.5+3.5)*3.14/360) = 6.760 A-1
    x_shift_array = np.array(x_shift_array)
    max_waxs_angle = np.max(waxs_angles)

    cts = 0

    if Waxs_angles[0] != max_waxs_angle:
        Waxs_angles = Waxs_angles[::-1]

    for (wi, waxs_angle) in enumerate(Waxs_angles):  # loop through waxs angles
        yield from bps.mv(waxs, waxs_angle)
        if waxs_angle == max_waxs_angle:
            if saxs_on:
                dets = [pil900KW, pil1M, pil300KW]
            else:
                dets = [pil900KW, pil300KW]
            print("Meausre both saxs and waxs here for w-angle=%s" % waxs_angle)
        else:
            dets = [pil900KW, pil300KW]

        if wi == 0:
            align = True
        else:
            align = False
        for ii, (x, sample) in enumerate(
            zip(x_list, sample_list)
        ):  # loop over samples on bar
            yield from bps.mv(piezo.x, x)  # move to next sample
            if align:
                # RE( bps.mv(piezo.th, 0 ) )
                yield from alignement_gisaxs(0.15)  # run alignment routine
                YPOS[ii] = piezo.y.position
                ThPOS[ii] = piezo.th.position
                print(YPOS, ThPOS)
            else:
                yield from bps.mv(piezo.y, YPOS[ii])
                yield from bps.mv(piezo.th, ThPOS[ii])
            TH = ThPOS[ii]  # piezo.th.position
            th_meas = inc_angles + ThPOS[ii]  # piezo.th.position
            det_exposure_time(t, t)
            x_pos_array = x + x_shift_array
            for x_meas in x_pos_array:  # measure at a few x positions
                yield from bps.mv(piezo.x, x_meas)
                for i, th in enumerate(th_meas):  # loop over incident angles
                    yield from bps.mv(piezo.th, th)
                    name_fmt = "{sample}_{th:5.4f}deg_waxsP{waxs_angle:05.2f}_x{x:05.2f}_y{y:05.2f}_z{y:05.2f}_det{saxs_z:05.2f}m_expt{t}s_T{T}_sid{scan_id:08d}"
                    sample_name = name_fmt.format(
                        sample=sample,
                        th=th_real[i],
                        waxs_angle=waxs_angle,
                        x=np.round(piezo.x.position, 2),
                        y=np.round(piezo.y.position, 2),
                        z=np.round(piezo.z.position, 2),
                        saxs_z=np.round(pil1m_pos.z.position, 2),
                        t=t,
                        T=T,
                        scan_id=RE.md["scan_id"],
                    )
                    sample_id(user_name=username, sample_name=sample_name)
                    print(f"\n\t=== Sample: {sample_name} ===\n")
                    print(dets)
                    yield from bp.count(dets, num=1)
                    # print( 'HERE#############')
            cts += 1
            yield from bps.mv(piezo.th, TH)
        sample_id(user_name="test", sample_name="test")
        det_exposure_time(0.5)


####for transimission


def measure_XS(dx=0, dy=0, t=1):
    """suppose the waxs is off the beam"""
    ks = list(sample_dict.keys())  # [:1]
    measure_WAXS(ks=ks, dx=dx, dy=dy, t=t)
    dy = 100
    measure_SAXS(ks=ks, dx=dx, dy=dy, t=t)


def measure_WAXS(ks, dx=0, dy=0, t=1, WA=np.array([0, 5, 15, 25, 45])):
    for wa in WA:
        move_waxs(wa)
        _measure_one(ks=ks, dets=[pil900KW], waxs_angle=wa, dx=dx, dy=dy, t=t)


def measure_SAXS(ks, wa=45, dx=0, dy=0, t=1):
    move_waxs(wa)
    _measure_one(ks=ks, dets=[pil1M], waxs_angle=wa, dx=dx, dy=dy, t=t)
    RE(bps.mvr(SAXS.y, 30 * 0.172))
    _measure_one(ks=ks, dets=[pil1M], waxs_angle=wa, dx=dx, dy=dy, t=t)
    RE(bps.mvr(SAXS.y, -30 * 0.172))


def _measure_one(ks, dets, waxs_angle, dx=0, dy=0, t=1):
    for k in ks:
        mov_sam(k)
        sample = RE.md["sample"]
        u = sample.split("_")[0]
        if u in ["Gao", "Xu", "YM"]:
            User_name = u
            sample = "_".join(sample.split("_")[1:])
        else:
            User_name = user_name
        movx(dx)
        movy(dy)
        tcur = time.time()
        name_fmt = "{sample}_x{x_pos:05.2f}_y{y_pos:05.2f}_z{z_pos:05.2f}_det{saxs_y}_{saxs_z}_waxs{waxs_angle:05.2f}_expt{expt}s_sid{scan_id:08d}"
        sample_name = name_fmt.format(
            sample=sample,
            x_pos=piezo.x.position,
            y_pos=piezo.y.position,
            z_pos=piezo.z.position,
            saxs_y=np.round(pil1m_pos.y.position, 2),
            saxs_z=np.round(pil1m_pos.z.position, 2),
            waxs_angle=waxs_angle,
            expt=t,
            scan_id=RE.md["scan_id"],
        )
        det_exposure_time(t, t)

        sample_id(user_name=User_name, sample_name=sample_name)
        print(f"\n\t=== Sample: {sample_name} ===\n")
        print("Collect data here....")
        RE(bp.count(dets, num=1))


def snap_waxs(t=0.1):
    dets = [pil900KW]
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(t)
    yield from (bp.count(dets, num=1))


def snap_saxs(t=0.1):
    dets = [pil1M]
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(t)
    yield from (bp.count(dets, num=1))


def name_sam(pos):
    sample = sample_dict[pos]
    print("Move to pos=%s for sample:%s" % (pos, sample))
    RE.md["sample"] = sample


def check_sample_loc(sleep=5):
    ks = list(sample_dict.keys())
    for k in ks:
        mov_sam(k)
        time.sleep(sleep)


def movx(dx):
    RE(bps.mvr(piezo.x, dx))


def movy(dy):
    RE(bps.mvr(piezo.y, dy))


def get_posxy():
    return round(piezo.x.user_readback.value, 2), round(piezo.y.user_readback.value, 2)


def move_waxs(waxs_angle=8.0):
    RE(bps.mv(waxs, waxs_angle))


def move_waxs_off(waxs_angle=8.0):
    RE(bps.mv(waxs, waxs_angle))


def move_waxs_on(waxs_angle=0.0):
    RE(bps.mv(waxs, waxs_angle))


def mov_sam(pos):
    px, py = pxy_dict[pos]
    RE(bps.mv(piezo.x, px))
    RE(bps.mv(piezo.y, py))
    sample = sample_dict[pos]
    print("Move to pos=%s for sample:%s" % (pos, sample))
    RE.md["sample"] = sample


def snap_waxs(t=0.1):
    dets = [pil300KW]
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(t)
    yield from (bp.count(dets, num=1))


def snap_saxs(t=0.1):
    dets = [pil1M]
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(t)
    yield from (bp.count(dets, num=1))


def measure_pindiol_current():
    fs.open()
    yield from bps.sleep(0.3)
    pd_curr = pdcurrent1.value
    fs.close()
    print("--------- Current pd_curr {}\n".format(pd_curr))
    return pd_curr
