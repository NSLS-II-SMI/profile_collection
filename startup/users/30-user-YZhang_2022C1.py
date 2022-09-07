##Collect data:

# SMI: 2022/3/7
# SAF:    Standard        Beamline 12-ID   proposal:  308052


# proposal_id('2022_1', '308052_YZhang')
# proposal_id('2022_1', '308052_YZhang2')
# Energy: 16.1 keV, 0.77009 A
# SAXS distance
# SAXS in  and WAXS in

# WAXS range [ 0, 5, 15, 25, 45 ]

#  RE( shopen() )  # to open the beam and feedback
#  RE( shclose())

#  %run -i
# for 900kw,
# move_waxs( 0 )  #the beamstop is 15.7
# put att  14-18keV, Sn 60 um, 7X, move beamstop  -10
# for waxs=0 --> find the beam center is [218, 308] on albula
# for waxs=1 --> find the beam center is [218, 280] on albula
# for waxs=2 --> find the beam center is [218, 252] on albula
# for waxs=3 --> find the beam center is [218, 223] on albula
# for waxs=4 --> find the beam center is [218, 194] on albula, part block by chip
# for waxs=5 --> find the beam center is [218, 166] on albula
# for waxs=6 --> find the beam center is [218, 138] on albula
# for waxs=7 --> find the beam center is [218, 110] on albula
# for waxs=8 --> find the beam center is [218, 81] on albula
# for waxs=9 --> find the beam center is [218, 53] on albula
# for waxs=10 --> find the beam center is [218, 25] on albula
# for waxs=11 --> find the beam center touch the edge
# for waxs=12 --> find the beam center is out of the detector


# The beam center on SAXS:
# 5 meter in vacuum, [462, 559 ]
# Using pindiol, X, -198.5, Y 8.7
# beamstop_save()


user_name = "YZ"


##Run1,
## change Hexpod , x,   z to 0 and y to 4
## change pz to 5400
# in vacuum
sample_dict = {
    1: "Wat_GCap1p5mm",
    2: "Gao_S1_7",
    3: "Xu_SBK_1",
    4: "Xu_SBK_2",
    5: "Xu_S5",
    6: "Xu_S6",
    7: "Xu_S7",
    8: "Xu_S8",
    9: "Xu_S9",
    10: "Xu_S10",
    11: "Xu_S11",
    12: "Xu_S12",
    13: "Xu_S13",
    14: "Xu_S14",
    15: "Xu_S15",
    16: "Au5_Stock_GCap1p5mm",
    17: "Au10_Stock_GCap1p5mm",
    18: "Au15_Stock_GCap1p5mm",
    19: "Au20_Stock_GCap1p5mm",
    20: "Au30_Stock_GCap1p5mm",
    21: "Au50_Stock_GCap1p5mm",
    22: "Al2O3",
    23: "AgBH",
    24: "YM_blue_powder",
}

ypos = 100
pxy_dict = {
    1: (-43500, ypos),
    2: (-40500, ypos),
    3: (-36800, ypos),
    4: (-33300, ypos),
    5: (-29500, ypos),
    6: (-26400, ypos),
    7: (-22600, ypos),
    8: (-18800, ypos),
    9: (-15600, ypos),
    10: (-11800, ypos),
    11: (-8000, ypos),
    12: (-4500, ypos),
    13: (-900, ypos),
    14: (2500, ypos),
    15: (6100, ypos),
    16: (10400, ypos),
    17: (13600, ypos),
    18: (16800, ypos),
    19: (21100, ypos),
    20: (24700, ypos),
    21: (27700, ypos),
    22: (32400, ypos),
    23: (35100, ypos),
    24: (38300, -1000),
}

# setthreshold energy 16100 autog 11000
# measure_XS(   dx=0, dy=0 ,  t=1   )
##Run2,
## change Hexpod , x,   z to 0 and y to 5
## change pz to 1400 #due to a large capillary diamter, not 5400
# RE(pil1m_bs_rod.mv_out())
# RE(pil1m_bs_pd.mv_in())
# in vacuum
sample_dict = {
    1: "Xu_S1",
    2: "Xu_S2",
    3: "Xu_S3",
    4: "Xu_S4",
}

ypos = 4000
pxy_dict = {
    1: (-35900, ypos),
    2: (-30600, 0),
    3: (-25200, 5000),
    4: (-19900, ypos),
}
#  measure_XS(   dx=0, dy=0 ,  t=1   )


##Run3,
# in air, low-divergency, pindiode in , beam on YAG, hexpod, x,y,z=0,0,0; pizeo, x=0, y=0, z=3900
# look at the beam size using the YAG top edge to do scan, hexpod Y = -4, pz = -6000
# The beam center on SAXS:  5 meter in air, [462, 559 ],  Using pindiol, X, -198.5, Y 8.7,  beamstop_save()

# x,y,z=0,4,0; pizeo,    z=1400
sample_dict = {  # 1: 'Xu_S1_InAir',  #broken
    2: "Xu_S2_InAir",
    3: "Xu_S3_InAir",
    4: "Xu_S4_InAir",
}

ypos = 4100
pxy_dict = {
    # 1:  ( -35900, ypos  ) ,
    2: (-30600 + 200, 0),
    3: (-25200 + 200, 5000),
    4: (-19900 + 200, ypos),
}
#  measure_XS(   dx=0, dy=0 ,  t=1   )


##Run4,
## change Hexpod , x,   z to 0 and y to 4
## change pz to 5400
# in air
sample_dict = {
    1: "Wat_GCap1p5mm_InAir",
    2: "Gao_S1_7_InAir",
    3: "Xu_SBK_1_InAir",
    4: "Xu_SBK_2_InAir",
    5: "Xu_S5_InAir",
    6: "Xu_S6_InAir",
    7: "Xu_S7_InAir",
    8: "Xu_S8_InAir",
    9: "Xu_S9_InAir",
    10: "Xu_S10_InAir",
    11: "Xu_S11_InAir",
    12: "Xu_S12_InAir",
    13: "Xu_S13_InAir",
    14: "Xu_S14_InAir",
    15: "Xu_S15_InAir",
    16: "Au5_Stock_GCap1p5mm_InAir",
    17: "Au10_Stock_GCap1p5mm_InAir",
    18: "Au15_Stock_GCap1p5mm_InAir",
    19: "Au20_Stock_GCap1p5mm_InAir",
    20: "Au30_Stock_GCap1p5mm_InAir",
    21: "Au50_Stock_GCap1p5mm_InAir",
    22: "Al2O3_InAir",
    23: "AgBH_InAir",
    24: "YM_blue_powder_InAir",
}
ypos = 100
dx = 0
pxy_dict = {
    1: (-44300, ypos),
    2: (-40500 - 200, ypos),
    3: (-36600, ypos),
    4: (-33300 - 200, ypos),
    5: (-29400, ypos),
    6: (-26400 - 200, ypos),
    7: (-22500, ypos),
    8: (-18700, ypos),
    9: (-15500, ypos),
    10: (-11500, ypos),
    11: (-7800, ypos),
    12: (-4500, ypos),
    13: (-600, ypos),
    14: (2500 + dx, ypos),
    15: (6100 + 300, ypos),
    16: (10400 + dx, ypos),
    17: (13600 + 400, ypos),
    18: (16800 + dx, ypos),
    19: (21100 - 300, ypos),
    20: (24700 + dx, ypos),
    21: (27700 + 300, ypos),
    22: (32400 + 300, ypos),
    23: (35100 + dx, ypos),
    24: (38300 + dx, -1000),
}


##Run5,
# Fang's pin sample
# x,y,z=0,-6,0; pizeo,    z=2200
# move detector to 8000 mm,  direct beam position [ 466, 557  ]
sample_dict = {
    1: "Fang_HXNPin_Sample",
}
pxy_dict = {
    1: (-200, -5350),
}
# measure_prs_rotate( 1 ,  wa=0,  t=.1 )  #for saxs, dont' find signal
# measure_prs_rotate_waxs( 1 ,  wa=0,  t=.1 ) #for waxs


## Try to do microfoucing on 16.1 keV  NOT WORKing

# load YAG
# feedback('off')  #turn off the feedback
# put CRL in ( on the CSS screen, click the third one from left in, Encode is 1.45650 mm)
# change the voltage of the mirror
#


##Run6,
sample_dict = {
    1: "YM_Crab_Test_Air",
}
pxy_dict = {
    1: (2200, 0),
}


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


x_list = np.array(list((pxy_dict.values())))[:, 0]
y_list = np.array(list((pxy_dict.values())))[:, 1]
sample_list = np.array(list((sample_dict.values())))
ks = np.array(list((sample_dict.keys())))

##################################################
############ Some convinent functions#################
#########################################################


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
