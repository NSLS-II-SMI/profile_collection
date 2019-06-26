print(f'Loading {__file__}')

from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner


class STG(Device):
    x = Cpt(EpicsMotor, 'X}Mtr', labels=['stage'])
    y = Cpt(EpicsMotor, 'Y}Mtr', labels=['stage'])
    z = Cpt(EpicsMotor, 'Z}Mtr', labels=['stage'])
    th = Cpt(EpicsMotor, 'theta}Mtr', labels=['stage'])
    ph = Cpt(EpicsMotor, 'phi}Mtr', labels=['stage'])
    ch = Cpt(EpicsMotor, 'chi}Mtr', labels=['stage'])


class SMPL(Device):
    x = Cpt(EpicsMotor, 'X}Mtr', labels=['sample'])
    y = Cpt(EpicsMotor, 'Y}Mtr', labels=['sample'])
    z = Cpt(EpicsMotor, 'Z}Mtr', labels=['sample'])
    al = Cpt(EpicsMotor, 'alpha}Mtr', labels=['sample'])
    az = Cpt(EpicsMotor, 'azimuth}Mtr', labels=['sample'])
    ka = Cpt(EpicsMotor, 'kappa}Mtr', labels=['sample'])


class HEXAPOD(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')
    a = Cpt(EpicsMotor, 'A}Mtr')
    b = Cpt(EpicsMotor, 'B}Mtr')
    c = Cpt(EpicsMotor, 'C}Mtr')

class SMARACT(Device):
    x = Cpt(EpicsMotor, '0}Mtr', labels = ['piezo'])
    y = Cpt(EpicsMotor, '3}Mtr', labels = ['piezo'])
    z = Cpt(EpicsMotor, '6}Mtr', labels = ['piezo'])
    th = Cpt(EpicsMotor, '4}Mtr', labels = ['piezo'])
    ch = Cpt(EpicsMotor, '1}Mtr', labels = ['piezo'])
    

   
class BDMStage(Device):
    x = Cpt(EpicsSignal, 'ACT2:POSITION', write_pv='ACT2:CMD:TARGET',kind='hinted')
    y = Cpt(EpicsSignal, 'ACT1:POSITION', write_pv='ACT1:CMD:TARGET',kind='hinted')
    th = Cpt(EpicsSignal, 'ACT0:POSITION', write_pv='ACT0:CMD:TARGET',kind='hinted')

bdm = BDMStage('XF:12IDC-ES:2:', name='bdm')

  
stage = STG('XF:12IDC-OP:2{HEX:Stg-Ax:', name='stage')
sample = SMPL('XF:12IDC-OP:2{HEX:Sam-Ax:', name='sample')
hp140 = HEXAPOD('XF:12IDC-OP:2{HEX:140-Ax:', name='hp140')
hp430 = HEXAPOD('XF:12IDC-OP:2{HEX:430-Ax:', name='hp430')
piezo = SMARACT('XF:12IDC-ES:2{MCS:1-Ax:', name='piezo')


for hp in [stage, sample, hp140, hp430]:
    hp.configuration_attrs = hp.read_attrs

for pz in [piezo]:
    pz.configuration_attrs = pz.read_attrs

prs = EpicsMotor('XF:12IDC-OP:2{HEX:PRS-Ax:Rot}Mtr', name='prs', labels=['prs'])

for pr in [prs]:
    pr.configuration_attrs = pr.read_attrs


class WAXS(Device):
    arc = Cpt(EpicsMotor, 'WAXS:1-Ax:Arc}Mtr')
    x = Cpt(EpicsMotor, 'BS:WAXS-Ax:x}Mtr')

    def set(self, arc_value):
        st_arc = self.arc.set(arc_value)

        if self.arc.limits[0] <= arc_value <= 3.5:
            calc_value = self.calc_waxs_bsx(arc_value)
        else:
            calc_value = -2
        st_x = self.x.set(calc_value)
        return st_arc & st_x
        
    def calc_waxs_bsx(self, arc_value):
        bsx_pos =-21.6 + 264 * np.tan(np.deg2rad(arc_value))
        return bsx_pos


waxs = WAXS('XF:12IDC-ES:2{', name='waxs')
