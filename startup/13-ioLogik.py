import time
from ophyd import Device


class ioLogik1241(Device):
    ch1_read = Cpt(EpicsSignal, '1-RB')
    ch1_sp = Cpt(EpicsSignal, '1-SP')
    ch2_read = Cpt(EpicsSignal, '2-RB')
    ch2_sp = Cpt(EpicsSignal, '2-SP')
    ch3_read = Cpt(EpicsSignal, '3-RB')
    ch3_sp = Cpt(EpicsSignal, '3-SP')
    ch4_read = Cpt(EpicsSignal, '4-RB')
    ch4_sp = Cpt(EpicsSignal, '4-SP')

class ioLogik1240(Device):
    ch1_read = Cpt(EpicsSignal, '1-I')
    ch2_read = Cpt(EpicsSignal, '2-I')
    ch3_read = Cpt(EpicsSignal, '3-I')
    ch4_read = Cpt(EpicsSignal, '4-I')
    ch5_read = Cpt(EpicsSignal, '5-I')
    ch6_read = Cpt(EpicsSignal, '6-I')
    ch7_read = Cpt(EpicsSignal, '7-I')
    ch8_read = Cpt(EpicsSignal, '8-I')


moxa_in = ioLogik1241('XF:12IDC-ES:2{IO}AO:', name='moxa_in')
moxa_out = ioLogik1240('XF:12IDC-ES:2{IO}AI:', name='moxa_out')

moxa_in.ch1_read.kind = 'hinted'
moxa_out.ch1_read.kind = 'hinted'
moxa_in.ch1_sp.kind = 'hinted'