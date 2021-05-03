import re
from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, Device, Component as Cpt, PseudoPositioner

class HFM_bimorphsvolt(Device):
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

    #This is the default hfm mirror voltage for smi swaxs hutch
    default_hfm_vector = [-151, 261, 250, 293, 175, 236, 168, 231, 242, 200, 291, 222, 215, 157, 311, 36]

    def set_relative(self, relative_value=0):
        #pattern matching to pick only the attributes with ch + a number
        ch_pattern = re.compile("ch\d{1,2}")
        for att_an in dir(self):
            ch_pattern_match = ch_pattern.match(att_an)
            if ch_pattern_match:
                yield from bps.mvr(getattr(self, att_an), relative_value)
                yield from bps.sleep(5)

    def set_abs_default(self):
        ch_pattern = re.compile("ch(?P<number>\d{1,2})")
        for att_an in dir(self):
            ch_pattern_match = ch_pattern.match(att_an)
            if ch_pattern_match:
                yield from bps.mv(getattr(self, att_an), self.default_hfm_vector[int(ch_pattern_match[1])])
                yield from bps.sleep(10)

hfm_bimorphsvolt = HFM_bimorphsvolt('HFM:SET-', name='hfm_bimorphsvolt')

