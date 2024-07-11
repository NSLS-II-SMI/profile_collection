from ophyd import (
    EpicsMotor,
    EpicsSignalRO,
    EpicsSignal,
    Device,
    Component as Cpt,
    PseudoPositioner,
    PVPositioner,
)

class ThorlabsMotor(PVPositioner):
    readback = Cpt(EpicsSignal,'.RBV')
    setpoint = Cpt(EpicsSignal,'.VAL')
    done = Cpt(EpicsSignal,'.DMOV')
    done_value=0

thorlabs_su = ThorlabsMotor('XF:12ID2-ES{DDSM100-Ax:X1}Mtr',name='thorlabs_su')


########## motor classes ##########
class MotorCenterAndGap(Device):
    "Center and gap using Epics Motor records"
    xc = Cpt(EpicsMotor, "-Ax:XC}Mtr")
    yc = Cpt(EpicsMotor, "-Ax:YC}Mtr")
    xg = Cpt(EpicsMotor, "-Ax:XG}Mtr")
    yg = Cpt(EpicsMotor, "-Ax:YG}Mtr")


class Blades(Device):
    "Actual T/B/O/I and virtual center/gap using Epics Motor records"
    tp = Cpt(EpicsMotor, "-Ax:T}Mtr")
    bt = Cpt(EpicsMotor, "-Ax:B}Mtr")
    ob = Cpt(EpicsMotor, "-Ax:O}Mtr")
    ib = Cpt(EpicsMotor, "-Ax:I}Mtr")
    xc = Cpt(EpicsMotor, "-Ax:XCtr}Mtr")
    yc = Cpt(EpicsMotor, "-Ax:YCtr}Mtr")
    xg = Cpt(EpicsMotor, "-Ax:XGap}Mtr")
    yg = Cpt(EpicsMotor, "-Ax:YGap}Mtr")


class DetMortor(Device):
    x = Cpt(EpicsMotor, "X}Mtr")
    y = Cpt(EpicsMotor, "Y}Mtr")
    z = Cpt(EpicsMotor, "Z}Mtr")


class SAXSBeamStop(Device):
    x = Cpt(EpicsMotor, "IBB}Mtr")
    pad = Cpt(EpicsMotor, "OBT}Mtr")
    y = Cpt(EpicsMotor, "IBM}Mtr")


class SAXSPindiode(Device):
    x = Cpt(EpicsMotor, "OBB}Mtr")
    y = Cpt(EpicsMotor, "OBM}Mtr")

class MDriveMortor(Device):
    '''
    Added by YZhang@2023Nov9
    '''
    m1 = Cpt(EpicsMotor, "1}Mtr")
    m2 = Cpt(EpicsMotor, "2}Mtr")
    m3 = Cpt(EpicsMotor, "3}Mtr")
    m4 = Cpt(EpicsMotor, "4}Mtr")
    m5 = Cpt(EpicsMotor, "5}Mtr")
    m6 = Cpt(EpicsMotor, "6}Mtr")
    m7 = Cpt(EpicsMotor, "7}Mtr")
    m8 = Cpt(EpicsMotor, "8}Mtr")

## for MDrive, YZhang
MDrive =  MDriveMortor("XF:12ID2-ES{Mdrive-Ax:", name = "MDrive")

## SAXS det position
SAXS = DetMortor("XF:12IDC-ES:2{Det:1M-Ax:", name="SAXS")
## stages for SAXS beamstops
SBS = SAXSBeamStop("XF:12IDC-ES:2{BS:SAXS-Ax:", name="SBS")