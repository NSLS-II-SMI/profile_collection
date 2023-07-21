from ophyd import (EpicsMotor, EpicsSignal, Device, Component as Cpt)

class bladecoater_smaract(Device):
    x1 = Cpt(EpicsMotor, "X1}Mtr", labels=["piezo"])
    x2 = Cpt(EpicsMotor, "X2}Mtr", labels=["piezo"])

bc_smaract = bladecoater_smaract("XF:12ID2-ES{DDSM100-Ax:", name="bc_smaract")


class syringe_pump(Device):
    x1 = Cpt(EpicsSignal, "Val:Vol-SP", labels=["piezo1"])
    x2 = Cpt(EpicsSignal, "Val:Rate-SP", labels=["piezo2"])
    x3 = Cpt(EpicsSignal, "Cmd:Run-Cmd", labels=["piezo3"])

syringe_pu = syringe_pump("XF:12ID2-ES{Pmp:1}", name="syringe_pu")

