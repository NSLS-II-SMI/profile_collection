import time as ttime
import os
import numpy as np
from ophyd import (PVPositioner, EpicsSignal, EpicsSignalRO, EpicsMotor,
                   Device, Signal, PseudoPositioner, PseudoSingle)
from ophyd.utils.epics_pvs import set_and_wait
from ophyd.ophydobj import StatusBase, MoveStatus
from ophyd.pseudopos import (pseudo_position_argument, real_position_argument)
from ophyd import Component as Cpt
from scipy.interpolate import InterpolatedUnivariateSpline

ANG_OVER_EV = 12398.4  # A*eV
D_Si111 = 3.1293
#D_Si111 = 3.135555
delta_bragg = 0.0
dcm_offset = 25

# Converters:
def energy_to_gap(target_energy, undulator_harmonic=1):
    fundamental_energy = target_energy / float(undulator_harmonic)
    f = fundamental_energy
    a = -53.025391
    b1 = 0.220837
    b2 = -3.537803e-4
    b3 = 3.105219e-7
    b4 = -1.587795e-10
    b5 = 4.734179e-14
    b6 = -7.633003e-18
    b7 = 5.14881e-22
    gap = a + b1*f + b2*f**2 + b3 * f**3 + b4 * f**4 + b5 * f**5 + b6 * f**6 + b7 * f**7
    return gap


def energy_to_bragg(target_energy, delta_bragg=delta_bragg):
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
            ttime.sleep(sleep)
        else:
            break


def move_und_and_dcm(target_energy, undulator_harmonic, delta_bragg=delta_bragg):
    gap = energy_to_gap(target_energy, undulator_harmonic)
    bragg_angle = energy_to_bragg(target_energy, delta_bragg)
    dcm_gap = (dcm_offset/2)/np.cos(bragg_angle * np.pi / 180)

    ivugap.move(gap, wait=False)
    dcm.bragg.move(bragg_angle, wait=False)
    dcm.gap.move(dcm_gap, wait=True)

    wait_all([ivugap, dcm.bragg, dcm.gap], sleep=0, debug=False)

    print('Bragg angle calculated  : {0:.5f}'.format(bragg_angle))
    print('Bragg angle from PV     : {0:.5f}'.format(dcm.bragg.get().user_readback))

    print('Undulator gap calculated: {0:.5f}'.format(gap))
    print('Undulator gap from PV   : {0:.5f}'.format(ivugap.readback.value))


def move_dcm(target_energy, delta_bragg=delta_bragg):
    bragg_angle = energy_to_bragg(target_energy, delta_bragg)

    dcm_gap = (dcm_offset/2)/np.cos(bragg_angle * np.pi / 180)
    dcm.bragg.move(bragg_angle, wait=False)
    dcm.gap.move(dcm_gap, wait=True)

    wait_all([dcm.bragg, dcm.gap], sleep=0, debug=False)

    print('DCM gap calculated      : {:.5f}'.format(dcm_gap))
    print('DCM gap from PV         : {:.5f}'.format(dcm.gap.get().user_readback))

    print('Bragg angle calculated  : {:.5f}'.format(bragg_angle))
    print('Bragg angle from PV     : {:.5f}'.format(dcm.bragg.get().user_readback))

'''
class FixedPVPositioner(PVPositioner):
    """This subclass ensures that the setpoint is really set before
    """

    def _move_async(self, position, **kwargs):
        """Move and do not wait until motion is complete (asynchronous)"""
        if self.actuate is not None:
            set_and_wait(self.setpoint, position)
            self.actuate.put(self.actuate_value, wait=False)
        else:
            self.setpoint.put(position, wait=False)

    def move(self, v, *args, **kwargs):
        kwargs['timeout'] = None
        self.done.reset(v)
        ret = super().move(v, *args, **kwargs)
        self.brake_on.subscribe(self.done._watcher,
                                event_type=self.brake_on.SUB_VALUE)
        self.readback.subscribe(self.done._watcher,
                                event_type=self.readback.SUB_VALUE)

        self.stop_signal.subscribe(self.done._stop_watcher,
                                   event_type=self.stop_signal.SUB_VALUE, run=False)
        return ret

class Energy(PseudoPositioner):
    # synthetic axis
    energy = Cpt(PseudoSingle)
    # real motors

    u_gap = ivugap
    # bragg = dcm.th  # defined in /home/xf12id/.ipython/profile_collection-17Q1.0/startup/10-motors.py

    # motor enable flags
    move_u_gap = Cpt(Signal, None, add_prefix=(), value=True)
    harmonic = Cpt(Signal, None, add_prefix=(), value=None)

    # experimental
    detune = Cpt(Signal, None, add_prefix=(), value=0)

    def energy_to_positions(self, target_energy, undulator_harmonic, u_detune):
        """Compute undulator and mono positions given a target energy

        Paramaters
        ----------
        target_energy : float
            Target energy in keV

        undulator_harmonic : int, optional
            The harmonic in the undulator to use

        uv_mistune : float, optional
            Amount to 'mistune' the undulator in keV.  Will settings such that the
            peak of the undulator spectrum will be at `target_energy + uv_mistune`.

        Returns
        -------
        bragg : float
             The angle to set the monocromotor
        """
        # set up constants
        Xoffset = self._xoffset
        d_111 = self._d_111
        delta_bragg = self._delta_bragg
        C2Xcal = self._c2xcal
        T2cal = self._t2cal
        etoulookup = self.u_gap.etoulookup


        #calculate Bragg RBV
        BraggRBV = np.arcsin((ANG_OVER_EV / target_energy)/(2 * d_111))/np.pi*180 - delta_bragg

        #calculate C2X
        Bragg = BraggRBV + delta_bragg
        T2 = Xoffset * np.sin(Bragg * np.pi / 180)/np.sin(2 * Bragg * np.pi / 180)
        dT2 = T2 - T2cal
        C2X = C2Xcal - dT2

        #calculate undulator gap
        # TODO make this more sohpisticated to stay a fixed distance off the
        # peak of the undulator energy
        ugap = float(etoulookup((target_energy + u_detune)/undulator_harmonic))

        ugap = energy_to_gap(target_energy, undulator_harmonic)

        return BraggRBV, C2X, ugap

    def undulator_energy(self, harmonic=3):
        """Return the current enegry peak of the undulator at the given harmonic

        Paramaters
        ----------
        harmanic : int, optional
            The harmonic to use, defaults to 3
        """
        ugap = self.u_gap.get().readback
        utoelookup = self.u_gap.utoelookup

        fundemental = float(utoelookup(ugap))

        energy = fundemental * harmonic

        return energy

    def __init__(self, *args,
                 xoffset=None, d_111=None, delta_bragg=None, C2Xcal=None, T2cal=None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._xoffset = xoffset
        self._d_111 = d_111
        self._delta_bragg = delta_bragg
        self._c2xcal = C2Xcal
        self._t2cal = T2cal

    def crystal_gap(self):
        """Return the current physical gap between first and second crystals
        """
        C2X = self.c2_x.get().user_readback
        bragg = self.bragg.get().user_readback

        T2cal = self._t2cal
        delta_bragg = self._delta_bragg
        d_111 = self._d_111
        c2x_cal = self._c2xcal

        Bragg = np.pi/180 * (bragg + delta_bragg)

        dT2 = c2x_cal - C2X
        T2 = dT2 + T2cal

        XoffsetVal = T2/(np.sin(Bragg)/np.sin(2*Bragg))

        return XoffsetVal

    @pseudo_position_argument
    def forward(self, p_pos):
        energy = p_pos.energy
        harmonic = self.harmonic.get()
        detune = self.detune.get()
        if energy <= 4.4:
            raise ValueError("The energy you entered is too low ({} keV). "
                             "Minimum energy = 4.4 keV".format(energy))
        if energy >= 25:
            raise ValueError('The energy you entered is too high ({} keV). '
                             'Maximum energy = 25.0 keV'.format(energy))

        if harmonic is None:
            harmonic = 3
            #choose the right harmonic
            braggcal, c2xcal, ugapcal = self.energy_to_positions(energy, harmonic, detune)
            # try higher harmonics until the required gap is too small
            while True:
                braggcal, c2xcal, ugapcal = self.energy_to_positions(energy, harmonic + 2, detune)
                if ugapcal < 6.4:
                    break
                harmonic += 2

        # compute where we would move everything to in a perfect world
        bragg, c2_x, u_gap = self.energy_to_positions(energy, harmonic, detune)

        # sometimes move the crystal gap
        if not self.move_c2_x.get():
            c2_x = self.c2_x.position

        # sometimes move the undulator
        if not self.move_u_gap.get():
            u_gap = self.u_gap.position

        return self.RealPosition(bragg=bragg, c2_x=c2_x, u_gap=u_gap)

    @real_position_argument
    def inverse(self, r_pos):
        bragg = r_pos.bragg
        e = ANG_OVER_EV / (2 * self._d_111 * math.sin(math.radians(bragg + self._delta_bragg)))
        return self.PseudoPosition(energy=float(e))

    @pseudo_position_argument
    def set(self, position):
        return super().set([float(_) for _ in position])

data = {
    'd_111': 3.135555,
    'delta_bragg': 0.317209816326,
    'C2Xcal': 3.6,
    'T2cal': 14.2470486188,
    'xoffset': 25.056582386746765,
}
'''

# energy = Energy(prefix='', name='energy', **data)
