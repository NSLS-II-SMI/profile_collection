##Collect data:


""" 
#SMI: 2021/10/30

SAF: 308214  Standard        Beamline 12-ID   proposal:   (CFN, 307961)
create proposal:  proposal_id( '2021_3', '307961_Dinca' )    #create the proposal id and folder

%run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Dinca2021C2B.py



RE( shopen() )  # to open the beam and feedback
RE( shclose()) 

  


# Energy: 16.1 keV, 0.77009 A
# SAXS distance 5000
##for the run >=5 
# 5 m, beam stop:  1.9  
# 5m, 1M, x=-5, Y = -40
# the correspond beam center is [ 454, 682  ]
# beamstop_save()


 

FOR MIT CELL,
Cables:
Cell A:
#3, red to red
#2 orange to blue

Cell B:
#9 black to black
#4 brown to brown


 




"""


username = "Dinca"
#####First Run
sample_dict = {
    1: "Cell01_NaCl_Electrolyte",
    2: "Cell03_AlCl3_Electrolyte",
}


#####Second Run
sample_dict = {
    1: "Cell05_MgCl2_Electrolyte",
    2: "Cell06_AlCl3_Electrolyte",
}


#####Third Run
sample_dict = {
    1: "Cell04_NH4Cl_Electrolyte",
    2: "Cell07_NaCl_Electrolyte_PH1",
}


pxy_dict = {
    1: (35800, 800),
    2: (-23400, 1200),
}


PZ = -1500
# Plan
#  measure at RT without apply V,
#  -0.7 V, measure
# keep 30 min, measure
#############
## For sample 1
# Without V,

#  Manually measure one by one
#  measure_pos_noV()
# apply V = -0.7
# measure_pos_V()


user_name = "Dinca"


pos = 1


def _measure(sample):
    if abs(waxs.arc.user_readback.value - 20) < 2:
        RE(
            measure_wsaxs(
                t=1, waxs_angle=20, att="None", dy=0, user_name=user_name, sample=sample
            )
        )
        RE(
            measure_waxs(
                t=1, waxs_angle=0, att="None", dy=0, user_name=user_name, sample=sample
            )
        )
    else:
        RE(
            measure_waxs(
                t=1, waxs_angle=0, att="None", dy=0, user_name=user_name, sample=sample
            )
        )
        RE(
            measure_wsaxs(
                t=1, waxs_angle=20, att="None", dy=0, user_name=user_name, sample=sample
            )
        )


def measure_pos_noV(pos):
    mov_sam(pos)
    samplei = RE.md["sample"]
    _measure(samplei)


def measure_pos_V(pos, N=20, wait_time=5 * 60, start_time=2):
    mov_sam(pos)
    t0 = time.time()
    for i in range(N):
        dt = (time.time() - t0) / 60 + start_time
        samplei = RE.md["sample"] + "ApplyN0p7_t_%.1fmin" % dt
        print(i, samplei)
        _measure(samplei)
        print("Sleep for 5 min...")
        time.sleep(wait_time)


def _measure_one_potential(V=""):
    mov_sam(2)
    RE.md["sample"] += V
    print(RE.md["sample"])
    RE(measure_waxs())
    time.sleep(3)
    RE(measure_saxs(1, move_y=False))


##################################################
############ Some convinent functions#################
#########################################################


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
    print("Move to pos=%s for sample:%s..." % (pos, sample))
    RE.md["sample"] = sample


def check_saxs_sample_loc(sleep=5):
    ks = list(sample_dict.keys())
    for k in ks:
        mov_sam(k)
        time.sleep(sleep)


def measure_saxs(t=1, att="None", dx=0, dy=0, user_name=username, sample=None):
    if sample is None:
        sample = RE.md["sample"]
    dets = [pil1M]
    if dy:
        yield from bps.mvr(piezo.y, dy)
    if dx:
        yield from bps.mvr(piezo.x, dx)
    name_fmt = "{sample}_x{x:05.2f}_y{y:05.2f}_z{z_pos:05.2f}_det{saxs_z:05.2f}m_expt{t}s_sid{scan_id:08d}"
    sample_name = name_fmt.format(
        sample=sample,
        x=np.round(piezo.x.position, 2),
        y=np.round(piezo.y.position, 2),
        z_pos=piezo.z.position,
        saxs_z=np.round(pil1m_pos.z.position, 2),
        t=t,
        scan_id=RE.md["scan_id"],
    )
    det_exposure_time(t, t)
    # sample_name='test'
    sample_id(user_name=user_name, sample_name=sample_name)
    print(f"\n\t=== Sample: {sample_name} ===\n")
    print("Collect data here....")
    yield from bp.count(dets, num=1)
    sample_id(user_name="test", sample_name="test")


def measure_waxs(
    t=1, waxs_angle=0, att="None", dx=0, dy=0, user_name=username, sample=None
):
    if sample is None:
        sample = RE.md["sample"]
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
    t=1, waxs_angle=20, att="None", dx=0, dy=0, user_name=username, sample=None
):
    if sample is None:
        sample = RE.md["sample"]
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
