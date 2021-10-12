print(f'Loading {__file__}')

import warnings
import time as ttime
import os
import numpy as np
from ophyd import (PVPositioner, EpicsSignal, EpicsSignalRO, EpicsMotor,
                   Device, Signal, PseudoPositioner, PseudoSingle)
from ophyd.utils.epics_pvs import set_and_wait
from ophyd.status import StatusBase, MoveStatus
from ophyd.pseudopos import (pseudo_position_argument, real_position_argument)
from ophyd import Component as Cpt
from scipy.interpolate import InterpolatedUnivariateSpline

ANG_OVER_EV = 12398.42  # A*eV
# TODO move inside energy class
D_Si111 = 3.1293
#D_Si111 = 3.135555


# Converters:
def energy_to_gap(target_energy, undulator_harmonic=1):
    fundamental_energy = target_energy / float(undulator_harmonic)
    f = fundamental_energy
    #measured fundamnetal harmonic on the 20th September 2018
    a = 24.31415 #-53.025391 values until 20Sep'18
    b1 = -0.08224 #0.220837
    b2 = 1.38266e-4 #-3.537803e-4
    b3 = -1.18903e-7 #-13.105219e-7
    b4 = 5.90784e-11 #-1.587795e-10
    b5 = -1.70272e-14 #4.734179e-14
    b6 = 2.64385e-18 #-7.633003e-18
    b7 = -1.70455e-22 #5.14881e-22
    gap_mm = a + b1*f + b2*f**2 + b3 * f**3 + b4 * f**4 + b5 * f**5 + b6 * f**6 + b7 * f**7
    gap = gap_mm*1000 - 21 #-30 for 12.62; -33 for 14 keV; -21 for 16.1 keV; -50 for 9540eV; -20 for 2450eV; -45 for 4050eV
    #-50 for 9700 keV -- 11.150 keV, -55 for 6.55 keV, -35 for 7.7 keV
    return gap


def energy_to_bragg(target_energy, delta_bragg=0):
    bragg_angle = np.arcsin((ANG_OVER_EV / target_energy) / (2 * D_Si111)) / np.pi * 180 - delta_bragg
    return bragg_angle


def wait_all(motors_list, sleep=0.0, debug=False):
    """Wait until the last motor finished movement.
    :param motors_list: the list of all motors to wait.
    :return: None
    """
    while True:
        motor_statuses = []
        for m in motors_list:
            motor_statuses.append(m.moving)
        if debug:
            print('Motor statuses: {}'.format(motor_statuses))
        if True in motor_statuses:
            yield from bps.sleep(sleep)
        else:
            break


def move_dcm(target_energy, delta_bragg=0):
    bragg_angle = energy_to_bragg(target_energy, delta_bragg)
    dcm_gap_value = (12.5)/np.cos(bragg_angle * np.pi / 180)
    dcm.bragg.move(bragg_angle, wait=False)
    dcm.dcmgap.move(dcm_gap_value, wait=True)

    wait_all([dcm.bragg, dcm.dcmgap], sleep=0, debug=False)

    print('DCM gap calculated      : {:.5f}'.format(dcm_gap_value))
    print('DCM gap from PV         : {:.5f}'.format(dcm.dcmgap.get().user_readback))

    print('Bragg angle calculated  : {:.5f}'.format(bragg_angle))
    print('Bragg angle from PV     : {:.5f}'.format(dcm.bragg.get().user_readback))



class DCMInternals(Device):
    height = Cpt(EpicsMotor, 'XF12ID:m66')
    pitch = Cpt(EpicsMotor, 'XF12ID:m67')
    roll = Cpt(EpicsMotor, 'XF12ID:m68')
    theta = Cpt(EpicsMotor, 'XF12ID:m65')


class Energy(PseudoPositioner):
    # synthetic axis
    energy = Cpt(PseudoSingle, kind='hinted', labels=['mono'])
    # real motors
    dcmgap = Cpt(EpicsMotor, 'XF12ID:m66', read_attrs=['user_readback'])
    bragg = Cpt(EpicsMotor, 'XF12ID:m65', read_attrs=['user_readback'], labels=['mono'])
#    dcmpitch = Cpt(EpicsMotor, 'XF12ID:m67', read_attrs=['readback'])

    ivugap = Cpt(InsertionDevice,
                 'SR:C12-ID:G1{IVU:1-Ax:Gap}-Mtr',
                 read_attrs=['user_readback'],
                 configuration_attrs=[],
                 labels=['mono'])

    enableivu = Cpt(Signal, value=True)
    enabledcmgap = Cpt(Signal, value=True)

    # this is also the maximum harmonic that will be tried
    target_harmonic =  Cpt(Signal, value=19)
    harmonic =  Cpt(Signal, kind='hinted')

    # TODO make this a derived component

    # TODO: if the energy.move is commanded to go to the current energy, then it will wait forever because nothing moves.

    # wlambda = Cpt(Signal, value=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hints = None
        try:
            previous_harmonic = db[-1].table(stream_name='baseline')['energy_harmonic'][1]
        except Exception:
            warnings.warn(f'Previous databroker record was not read. '
                          f'Setting harmonic to the default value {self.target_harmonic.get()}')
            previous_harmonic = self.target_harmonic.get()

        self.target_harmonic.put(previous_harmonic)

    @pseudo_position_argument
    def forward(self, p_pos):
        energy = p_pos.energy
        self.harmonic.put(self.target_harmonic.get())

        #Needs to refine the default target_harmonic for each energy range
        # if 13500 < energy < 24000: self.harmonic.put(15)
        # elif 13000 < energy < 13500: self.harmonic.put(13)
        # elif 10000 < energy < 13000: self.harmonic.put(11) #Selenium edge
        # elif 9000 < energy < 10000: self.harmonic.put(7) #OPLS energy
        # elif 6000 < energy < 9000: self.harmonic.put(5)
        # elif 5000 < energy < 6000: self.harmonic.put(3) #This needs to be verified but from my notes La edge was reach with harm 3 
        # elif 3000 < energy < 5000: self.harmonic.put(3)
        # elif 2050 < energy < 3000: self.harmonic.put(1)
        # else: raise ValueError("The energy you entered is not in an accessible energy range ({} eV). "
        #                         "2050 - 24000 eV".format(energy))

        if not self.harmonic.get() % 2:
            raise RuntimeError('harmonic must be odd')

        if energy <= 2050:
            raise ValueError("The energy you entered is too low ({} eV). "
                             "Minimum energy = 2050 eV".format(energy))
        if energy >= 24001:
            raise ValueError('The energy you entered is too high ({} eV). '
                             'Maximum energy = 24000 eV'.format(energy))

        # compute where we would move everything to in a perfect world

        target_ivu_gap = energy_to_gap(energy, self.harmonic.get())
        while not (6200 <= target_ivu_gap < 15100):
             self.harmonic.put(self.harmonic.get() - 2)
             if self.harmonic.get() < 1:
                 raise RuntimeError('can not find a valid gap')
             target_ivu_gap = energy_to_gap(energy, self.harmonic.get())

        target_bragg_angle = energy_to_bragg(energy)

        dcm_offset = 25
        target_dcm_gap = (dcm_offset/2)/np.cos(target_bragg_angle * np.pi / 180)

        # sometimes move the crystal gap
        if not self.enabledcmgap.get():
            target_dcm_gap = self.dcmgap.position

        # sometimes move the undulator
        if not self.enableivu.get():
            target_ivu_gap = self.ivugap.position

        return self.RealPosition(bragg=target_bragg_angle,
                                 ivugap=target_ivu_gap,
                                 dcmgap=target_dcm_gap)

    @real_position_argument
    def inverse(self, r_pos):
        bragg = r_pos.bragg
        try:
            e = ANG_OVER_EV / (2 * D_Si111 * math.sin(math.radians(bragg)))
        except ZeroDivisionError:
            e = -1.e23
        return self.PseudoPosition(energy=float(e))

    @pseudo_position_argument
    def set(self, position):
        energy, = position
        # print(position, self.position)
        if np.abs(energy - self.position[0]) < .01:
            return MoveStatus(self, energy, success=True, done=True)
        return super().set([float(_) for _ in position])


energy = Energy(prefix='', name='energy',
                read_attrs=['energy', 'ivugap', 'bragg', 'harmonic'],
                configuration_attrs=['enableivu', 'enabledcmgap', 'target_harmonic'])

dcm = energy
ivugap = energy.ivugap
# DCM motor shortcuts. Early scans used the names at right (p2h, etc).
dcm_gap = dcm.dcmgap  # Height in CSS # EpicsMotor('XF12ID:m66', name='p2h')
dcm_pitch = EpicsMotor('XF12ID:m67', name='dcm_pitch')
# dcm_roll = dcm.roll  # Roll in CSS # EpicsMotor('XF12ID:m68', name='p2r')
bragg = dcm.bragg  # Theta in CSS  # EpicsMotor('XF12ID:m65', name='bragg')
# dcm_x = dcm.x  # E Mono X in CSS

dcm_config = DCMInternals('', name='dcm_config')

bragg.read_attrs = ['user_readback']

new_ivu_gap = EpicsMotor('SR:C12-ID:G1{IVU:1-Ax:Gap}-Mtr', name='new_ivu_gap')
