import re
from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner

class HFM_voltage(Device):
    ch0 = Cpt(EpicsSignal, 'VOUT0')
    ch1 = Cpt(EpicsSignal, 'VOUT1')
    ch2 = Cpt(EpicsSignal, 'VOUT2')
    ch3 = Cpt(EpicsSignal, 'VOUT3')
    ch4 = Cpt(EpicsSignal, 'VOUT4')
    ch5 = Cpt(EpicsSignal, 'VOUT5')
    ch6 = Cpt(EpicsSignal, 'VOUT6')
    ch7 = Cpt(EpicsSignal, 'VOUT7')
    ch8 = Cpt(EpicsSignal, 'VOUT8')
    ch9 = Cpt(EpicsSignal, 'VOUT9')
    ch10 = Cpt(EpicsSignal, 'VOUT10')
    ch11 = Cpt(EpicsSignal, 'VOUT11')
    ch12 = Cpt(EpicsSignal, 'VOUT12')
    ch13 = Cpt(EpicsSignal, 'VOUT13')
    ch14 = Cpt(EpicsSignal, 'VOUT14')
    ch15 = Cpt(EpicsSignal, 'VOUT15')
    shift_rel = Cpt(EpicsSignal, 'ALLSHIFT')

    #This is the default hfm mirror voltage for smi swaxs hutch
    default_hfm_v2 = [-151, 261, 250, 293, 175, 236, 168, 231, 242, 200, 291, 222, 215, 157, 311, 36]

    def shift_relative(self, relative_value=0):
        yield from bps.mv(self.shift_rel, relative_value)

    def set_abs_default(self):
        ch_pattern = re.compile("ch(?P<number>\d{1,2})")
        for att_an in dir(self):
            ch_pattern_match = ch_pattern.match(att_an)
            if ch_pattern_match:
                #-80 to move directly to teh good voltag for lowdiv configuration
                yield from bps.mv(getattr(self, att_an), -80 + self.default_hfm_v2[int(ch_pattern_match[1])])
                yield from bps.sleep(3)

hfm_voltage = HFM_voltage('HFM:SET-', name='hfm_voltage')


class VFM_voltage(Device):
    ch0 = Cpt(EpicsSignal, 'VOUT0')
    ch1 = Cpt(EpicsSignal, 'VOUT1')
    ch2 = Cpt(EpicsSignal, 'VOUT2')
    ch3 = Cpt(EpicsSignal, 'VOUT3')
    ch4 = Cpt(EpicsSignal, 'VOUT4')
    ch5 = Cpt(EpicsSignal, 'VOUT5')
    ch6 = Cpt(EpicsSignal, 'VOUT6')
    ch7 = Cpt(EpicsSignal, 'VOUT7')
    ch8 = Cpt(EpicsSignal, 'VOUT8')
    ch9 = Cpt(EpicsSignal, 'VOUT9')
    ch10 = Cpt(EpicsSignal, 'VOUT10')
    ch11 = Cpt(EpicsSignal, 'VOUT11')
    ch12 = Cpt(EpicsSignal, 'VOUT12')
    ch13 = Cpt(EpicsSignal, 'VOUT13')
    ch14 = Cpt(EpicsSignal, 'VOUT14')
    ch15 = Cpt(EpicsSignal, 'VOUT15')
    shift_rel = Cpt(EpicsSignal, 'ALLSHIFT')

    #This is the default vfm mirror voltage for smi swaxs hutch
    default_vfm_v2 = [39, -102, 277, 234, 325, 163, 392, 280, 365, 273, 196, 400, 219, 304, 51, -327]

    #This is the default vfm mirror voltage for opls hutch
    default_vfm_opls = [-206, -191, 6, 71, -316, 184, -223, 120, 45, -130, 202, -111, 17, 62, -75, -553]

    def shift_relative(self, relative_value=0):
        yield from bps.mv(self.shift_rel, relative_value)

    def set_abs_default(self, mode='SWAXS'):
        ch_pattern = re.compile("ch(?P<number>\d{1,2})")
        for att_an in dir(self):
            ch_pattern_match = ch_pattern.match(att_an)
            if ch_pattern_match:
                if mode == 'SWAXS':
                    yield from bps.mv(getattr(self, att_an), self.default_vfm_v2[int(ch_pattern_match[1])])
                    yield from bps.sleep(3)
                elif mode == 'OPLS':
                    yield from bps.mv(getattr(self, att_an), self.default_vfm_opls[int(ch_pattern_match[1])])
                    yield from bps.sleep(3)
                else:
                    print('Unknown mode, your should choose between SWAXS or OPLS')

vfm_voltage = VFM_voltage('VFM:SET-', name='vfm_voltage')