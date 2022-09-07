from ophyd import Component as Cpt, EpicsSignal, EpicsSignalRO, PVPositioner


class Linkam(PVPositioner):
    """
    An ophyd wrapper around the Linkam T96 controller
    """

    ## following https://blueskyproject.io/ophyd/positioners.html#pvpositioner
    readback = Cpt(EpicsSignalRO, "TEMP")
    setpoint = Cpt(EpicsSignal, "SETPOINT:SET")
    status_code = Cpt(EpicsSignal, "STATUS")

    ## all the rest of the Linkam signals
    init = Cpt(EpicsSignal, "INIT")
    model_array = Cpt(EpicsSignal, "MODEL")
    serial_array = Cpt(EpicsSignal, "SERIAL")
    stage_model_array = Cpt(EpicsSignal, "STAGE:MODEL")
    stage_serial_array = Cpt(EpicsSignal, "STAGE:SERIAL")
    firm_ver = Cpt(EpicsSignal, "FIRM:VER")
    hard_ver = Cpt(EpicsSignal, "HARD:VER")
    ctrllr_err = Cpt(EpicsSignal, "CTRLLR:ERR")
    config = Cpt(EpicsSignal, "CONFIG")
    stage_config = Cpt(EpicsSignal, "STAGE:CONFIG")
    disable = Cpt(EpicsSignal, "DISABLE")
    dsc = Cpt(EpicsSignal, "DSC")
    RR_set = Cpt(EpicsSignal, "RAMPRATE:SET")
    RR = Cpt(EpicsSignal, "RAMPRATE")
    ramptime = Cpt(EpicsSignal, "RAMPTIME")
    startheat = Cpt(EpicsSignal, "STARTHEAT")
    holdtime_set = Cpt(EpicsSignal, "HOLDTIME:SET")
    holdtime = Cpt(EpicsSignal, "HOLDTIME")
    power = Cpt(EpicsSignalRO, "POWER")
    lnp_speed = Cpt(EpicsSignal, "LNP_SPEED")
    lnp_mode_set = Cpt(EpicsSignal, "LNP_MODE:SET")
    lnp_speed_set = Cpt(EpicsSignal, "LNP_SPEED:SET")
