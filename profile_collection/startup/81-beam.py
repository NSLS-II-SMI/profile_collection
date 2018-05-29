#!/usr/bin/python
# -*- coding: utf-8 -*-
# vi: ts=4 sw=4




################################################################################
#  Code for querying and controlling beamline components that 'affect' the
# beam. (Beam energy, beam flux, etc.)
################################################################################
# Known Bugs:
#  N/A
################################################################################
# TODO:
#  Search for "TODO" below.
################################################################################


# Notes
################################################################################
# verbosity=0 : Output nothing
# verbosity=1 : Output only final (minimal) result
# verbosity=2 : Output 'regular' amounts of information/data
# verbosity=3 : Output all useful information
# verbosity=4 : Output marginally useful things (e.g. essentially redundant/obvious things)
# verbosity=5 : Output everything (e.g. for testing)



# These imports are not necessary if part of the startup sequence.
# If this file is called separately, some of these may be needed.
#import numpy as np
#from epics import caget, caput
#from time import sleep

#from ophyd import EpicsMotor, Device, Component as Cpt
#from ophyd.commands import * # For mov, movr

#define pilatus_name and _Epicsname, instead of pilatus300 or pilatus2M
#moved to 20-area-detectors.py
#pilatus_name = pilatus2M
#pilatus_Epicsname = '{Det:PIL2M}'


class BeamlineDetector(object):
    
    def __init__(self, detector, **md):
        
        self.detector = detector
        
        self.md = md
        
    
    def get_md(self, prefix='detector_', **md):
        '''Returns a dictionary of the current metadata.
        The 'prefix' argument is prepended to all the md keys, which allows the
        metadata to be grouped with other metadata in a clear way. (Especially,
        to make it explicit that this metadata came from the beamline.)'''
        
        md_return = self.md.copy()
    
        # Include the user-specified metadata
        md_return.update(md)

        # Add an optional prefix
        if prefix is not None:
            md_return = { '{:s}{:s}'.format(prefix, key) : value for key, value in md_return.items() }
    
        return md_return
            
            
class CMS_SAXS_Detector(BeamlineDetector):

    def setCalibration(self, direct_beam, distance, detector_position=None, pixel_size=0.172):
        
        self.direct_beam = direct_beam
        self.distance = distance
        if detector_position is None:
            self.detector_position = [SAXSx.user_readback.value, SAXSy.user_readback.value]
        else:
            self.detector_position = detector_position
        self.pixel_size = pixel_size
        
    
    def get_md(self, prefix='detector_SAXS_', **md):
        
        md_return = self.md.copy()
    
        x0, y0 = self.direct_beam
        position_defined_x, position_defined_y = self.detector_position
        position_current_x, position_current_y = SAXSx.user_readback.value, SAXSy.user_readback.value
        
            
        md_return['name'] = self.detector.name

        #if pilatus_name==pilatus300k:
            #md_return['x0_pix'] = round( x0 + (position_current_x-position_defined_x)/self.pixel_size , 2 )
            #md_return['y0_pix'] = round( y0 + (position_current_y-position_defined_y)/self.pixel_size , 2 )
        if pilatus_name==pilatus2M:
            md_return['x0_pix'] = round( x0 + (position_current_x-position_defined_x)/self.pixel_size , 2 )
            md_return['y0_pix'] = round( y0 - (position_current_y-position_defined_y)/self.pixel_size , 2 )
        md_return['distance_m'] = self.distance
    
        md_return['ROI1_X_min'] = caget('XF:11BMB-ES{}:ROI1:MinX'.format(pilatus_Epicsname))
        md_return['ROI1_X_size'] = caget('XF:11BMB-ES{}:ROI1:SizeX'.format(pilatus_Epicsname))
        md_return['ROI1_Y_min'] = caget('XF:11BMB-ES{}:ROI1:MinY'.format(pilatus_Epicsname))
        md_return['ROI1_Y_size'] = caget('XF:11BMB-ES{}:ROI1:SizeY'.format(pilatus_Epicsname))

        md_return['ROI2_X_min'] = caget('XF:11BMB-ES{}:ROI2:MinX'.format(pilatus_Epicsname))
        md_return['ROI2_X_size'] = caget('XF:11BMB-ES{}:ROI2:SizeX'.format(pilatus_Epicsname))
        md_return['ROI2_Y_min'] = caget('XF:11BMB-ES{}:ROI2:MinY'.format(pilatus_Epicsname))
        md_return['ROI2_Y_size'] = caget('XF:11BMB-ES{}:ROI2:SizeY'.format(pilatus_Epicsname))

        md_return['ROI3_X_min'] = caget('XF:11BMB-ES{}:ROI3:MinX'.format(pilatus_Epicsname))
        md_return['ROI3_X_size'] = caget('XF:11BMB-ES{}:ROI3:SizeX'.format(pilatus_Epicsname))
        md_return['ROI3_Y_min'] = caget('XF:11BMB-ES{}:ROI3:MinY'.format(pilatus_Epicsname))
        md_return['ROI3_Y_size'] = caget('XF:11BMB-ES{}:ROI3:SizeY'.format(pilatus_Epicsname))

        md_return['ROI4_X_min'] = caget('XF:11BMB-ES{}:ROI4:MinX'.format(pilatus_Epicsname))
        md_return['ROI4_X_size'] = caget('XF:11BMB-ES{}:ROI4:SizeX'.format(pilatus_Epicsname))
        md_return['ROI4_Y_min'] = caget('XF:11BMB-ES{}:ROI4:MinY'.format(pilatus_Epicsname))
        md_return['ROI4_Y_size'] = caget('XF:11BMB-ES{}:ROI4:SizeY'.format(pilatus_Epicsname))
        
        # Include the user-specified metadata
        md_return.update(md)

        # Add an optional prefix
        if prefix is not None:
            md_return = { '{:s}{:s}'.format(prefix, key) : value for key, value in md_return.items() }
    
        return md_return


class BeamlineElement(object):
    '''Defines a component of the beamline that (may) intersect the x-ray beam.'''
    
    def __init__(self, name, zposition, description="", pv=None, **args):
        
        self.name = name
        self.zposition = zposition
        self.description = description
        
        self.conversion_factor = 1
        
        self._pv_main = pv
        
        self.has_flux = True
        
        
    def state(self):
        """
        Returns the current state of the beamline element. Common states:
        out - Element is out of the way of the beam (and should not be blocking).
        in - Element is in the beam (but should not be blocking).
        block - Element is in the beam, and should be blocking the beam.
        undefined - Element is in an unexpected state.
        """
        
        return "out"

    
    def transmission(self, t=None, verbosity=0):
        """
        Returns the predicted transmission of this beamline element, based on 
        its current state.
        """
        
        if t is not None:
            print("WARNING: To change transmission, use 'setTransmission'.")
            print("WARNING: Beam transmission was not changed.")
            return
        
        tr_tot = 1.0
        
        if verbosity>=2:
            print('{:s} transmission = {:.6g}'.format(self.name, tr_tot))
        
        
        # Assume a generic beamline element doesn't block/perturb the beam
        return tr_tot
        
        
    def flux(self, verbosity=3):
        
        reading = self.reading(verbosity=0)
        flux = self.conversion_factor*reading # ph/s
        
        if verbosity>=2:
            print('flux = {:.4g} ph/s'.format(flux))
        
        return flux
    
    
        
        
class Shutter(BeamlineElement):
    
    # Example
    #          XF:11BMA-PPS{PSh}Enbl-Sts
    #  Status: XF:11BMA-PPS{PSh}Pos-Sts       0 for open, 1 for close
    #  Open:   XF:11BMA-PPS{PSh}Cmd:Opn-Cmd
    #  Close:  XF:11BMA-PPS{PSh}Cmd:Cls-Cmd
    
    def __init__(self, name, zposition, description="", pv=None, **args):
        
        super().__init__(name=name, zposition=zposition, description=description, pv=pv, **args)
        self.has_flux = False
        
    
    def state(self):
        """
        Returns the current state of the beamline element. Common states:
        out - Element is out of the way of the beam (and should not be blocking).
        in - Element is in the beam (but should not be blocking).
        block - Element is in the beam, and should be blocking the beam.
        undefined - Element is in an unexpected state.
        """
        
        state_n = caget(self._pv_main+'Pos-Sts')
        
        if state_n is 0:
            return "out"
        elif state_n is 1:
            return "block"
        else:
            return "undefined" 
        
        
    def open(self, verbosity=3):
        
        if verbosity>=3:
            print('Opening {:s}...'.format(self.name))
        
        # E.g. #XF:11BMB-VA{Slt:4-GV:1}Cmd:Opn-Cmd
        pv = self._pv_main + 'Cmd:Opn-Cmd'
        #caput(pv, 1) # TODO: Test this.
    
    def close(self, verbosity=3):
        
        if verbosity>=3:
            print('Closing {:s}...'.format(self.name))
            
        pv = self._pv_main + 'Cmd:Cls-Cmd'
        #caput(pv, 1) # TODO: Test this.

        



class GateValve(Shutter):
    
    # Example
    #  Status: XF:11BMB-VA{Slt:4-GV:1}Pos-Sts        1 for open, 0 for close
    #  Open:   XF:11BMB-VA{Slt:4-GV:1}Cmd:Opn-Cmd
    #  Close:  XF:11BMB-VA{Slt:4-GV:1}Cmd:Cls-Cmd
    
    
    def state(self):
        """
        Returns the current state of the beamline element. Common states:
        out - Element is out of the way of the beam (and should not be blocking).
        in - Element is in the beam (but should not be blocking).
        block - Element is in the beam, and should be blocking the beam.
        undefined - Element is in an unexpected state.
        """
        
        state_n = caget(self._pv_main+'Pos-Sts')
        
        if state_n is 1:
            return "out"
        elif state_n is 0:
            return "block"
        else:
            return "undefined"     
    


class ThreePoleWiggler(BeamlineElement):
    
    def __init__(self, name='3PW', zposition=0.0, description='Three-pole wiggler source of x-rays', **args):
        
        
        super().__init__(name=name, zposition=zposition, description=description, **args)
        
        # TODO: Find out the right conversion factor
        self.conversion_factor = 3e18/500.0 #(ph/s)/mA
        

    def state(self):
        """
        Returns the current state of the beamline element. Common states:
        out - Element is out of the way of the beam (and should not be blocking).
        in - Element is in the beam (but should not be blocking).
        block - Element is in the beam, and should be blocking the beam.
        undefined - Element is in an unexpected state.
        """
        
        position = caget('SR:C11-ID:G5{3PW:1}Mtr.RBV')
        
        # TODO: Instead use the 'inserted' flag?
        # caget('SR:C11-ID:G5{3PW:1}InsertedFlag')
        
        if abs(position-0)<3:
            return "in"
        
        elif abs(position - -189.0)<10:
            return "out"
        
        else:
            return "undefined"
        
        
    def reading(self, verbosity=3):
        
        if self.state() is 'in':
            
            ring_current = caget('SR:OPS-BI{DCCT:1}I:Real-I')
            if verbosity>=2:
                print('{:s} is inserted; ring current = {:.1f} mA'.format(self.name, ring_current))
                
            return ring_current
        
        else:
            if verbosity>=2:
                print('{:s} is not inserted.'.format(self.name))
                
            return 0
        

class Monitor(BeamlineElement):
    
    def quickReading(self, verbosity=3, delay=1.0):
        """
        Puts the diagnostic into the beam, takes a reading, and removes the
        diagnostic.
        """
        
        self.insert()
        time.sleep(delay)
        value = self.reading(verbosity=verbosity)
        
        self.retract()
        time.sleep(delay)
        
        return value
    
    
    
class DiagnosticScreen(Monitor):
    
    #XF:11BMB-BI{FS:4}Pos-Sts
    
    def __init__(self, name, zposition, description="", pv=None, epics_signal=None, **args):
        
        super().__init__(name=name, zposition=zposition, description=description, pv=pv, **args)
        self.epics_signal = epics_signal
        self.has_flux = False
        
    
    def state(self):
        """
        Returns the current state of the beamline element. Common states:
        out - Element is out of the way of the beam (and should not be blocking).
        in - Element is in the beam (but should not be blocking).
        block - Element is in the beam, and should be blocking the beam.
        undefined - Element is in an unexpected state.
        """
        
        state_n = caget(self._pv_main+'Pos-Sts')
        
        if state_n is 0:
            return "out"
        elif state_n is 1:
            return "block"
        else:
            return "undefined" 
            
    
    def insert(self, verbosity=3):
        
        if verbosity>=3:
            print('Inserting {:s}...'.format(self.name))
        
        # E.g. #XF:11BMB-VA{Slt:4-GV:1}Cmd:Opn-Cmd
        pv = self._pv_main + 'Cmd:In-Cmd'
        caput(pv, 1)
    
    def retract(self, verbosity=3):
        
        if verbosity>=3:
            print('Retracting {:s}...'.format(self.name))
            
        pv = self._pv_main + 'Cmd:Out-Cmd'
        caput(pv, 1)
        
        
    def reading(self, verbosity=3):
        
        value = self.epics_signal.stats1.total.value
        
        if self.state() is 'block':
            
            ring_current = caget('SR:OPS-BI{DCCT:1}I:Real-I')
            if verbosity>=2:
                print('{:s} is inserted; reading = {:.4g}'.format(self.name, value))
                
            return value
        
        else:
            if verbosity>=2:
                print('{:s} is not inserted.'.format(self.name))
                
            return 0
        
        
        
        
class PointDiode_CMS(Monitor):
    
    def __init__(self, name='bim6 point diode', zposition=59.1, description="Bar holding a point-diode, downstream of sample.", pv='XF:11BMB-BI{IM:2}EM180:Current1:MeanValue_RBV', epics_signal=None, **args):
        
        super().__init__(name=name, zposition=zposition, description=description, pv=pv, **args)
        self.has_flux = True
        
        if epics_signal is None:
            
            #bim6 = EpicsSignalROWait("XF:11BMB-BI{IM:2}EM180:Current1:MeanValue_RBV", wait_time=1, name='bim6')
            #bim6_integrating = EpicsSignalROIntegrate("XF:11BMB-BI{IM:2}EM180:Current1:MeanValue_RBV", wait_time=0.5, integrate_num=8, integrate_delay=0.1, name='bim6')
            
            self.epics_signal = bim6_integrating
            
        else:
            self.epics_signal = epics_signal
        
        
        # The beam (at the ion chamber) is roughly 0.50x0.50 mm.
        # If we slit down to 0.20x0.05 mm, we are capturing 0.4*0.25 = 0.1 of the beam.
        # bim6 reads 70000 cts (of course this depends on settings) when ion chamber reads 1.3e11 ph/s.
        # (settings: trans = 5e-4)
        # So conversion_factor is roughly:
        self.conversion_factor = 1.3e11*0.1/70000. # (ph/s)/cts
        
        self.in_position_x = 0.0
        self.in_position_y = 0.0

        self.out_position_x = 0.0
        self.out_position_y = -16.0
        
        self.position_tolerance = 0.1
        
    
    def state(self):
        """
        Returns the current state of the beamline element. Common states:
        out - Element is out of the way of the beam (and should not be blocking).
        in - Element is in the beam (but should not be blocking).
        block - Element is in the beam, and should be blocking the beam.
        undefined - Element is in an unexpected state.
        """
        
        position_x = DETx.user_readback.value
        position_y = DETy.user_readback.value
        
        if abs(position_x-self.out_position_x)<self.position_tolerance and abs(position_y-self.out_position_y)<self.position_tolerance: 
            return "out"
        if abs(position_x-self.in_position_x)<self.position_tolerance and abs(position_y-self.in_position_y)<self.position_tolerance: 
            return "block"
        else:
            return "undefined" 
                
    def insert(self, verbosity=3):
        
        if verbosity>=3:
            print('Inserting {:s}...'.format(self.name))
        
        #mov( [DETx, DETy], [self.in_position_x, self.in_position_y] )
        DETx.move = self.in_position_x
        DETy.move = self.in_position_y
    
    def retract(self, verbosity=3):
        
        if verbosity>=3:
            print('Retracting {:s}...'.format(self.name))
            
        #mov( [DETx, DETy], [self.out_position_x, self.out_position_y] )
        DETx.move = self.out_position_x
        DETy.move = self.out_position_y        
        
    def reading(self, verbosity=3):
        
        value = self.epics_signal.read()[self.epics_signal.name]['value']
        
        if self.state() is 'block':
            
            if verbosity>=2:
                print('{:s} is inserted; reading = {:.4g}'.format(self.name, value))
                
            return value
        
        else:
            if verbosity>=2:
                print('{:s} is not inserted.'.format(self.name))
                
            return value
                
        

class IonChamber_CMS(Monitor):
    
    def __init__(self, name='bim3 ionchamber', zposition=49, description="Ion chamber (FMB Oxford I404) at start of endstation hutch", pv=None, beam=None, **args):
        
        super().__init__(name=name, zposition=zposition, description=description, pv=pv, **args)
        self.has_flux = True
        
        self.beam = beam
        
        # PVs
        import epics
        self.v1 = epics.PV('XF:11BMB-BI{IM:3}:IC1_MON')
        self.v2 = epics.PV('XF:11BMB-BI{IM:3}:IC2_MON')
        self.h1 = epics.PV('XF:11BMB-BI{IM:3}:IC3_MON')
        self.h2 = epics.PV('XF:11BMB-BI{IM:3}:IC4_MON')

        
    def state(self):
        
        return "in"
    
    
    def v_position(self):
        
        total = self.v1.value+self.v2.value
        if total>0:
            return (self.v1.value-self.v2.value)/(total)
        else:
            return 0

    def h_position(self):
        
        total = self.h1.value+self.h2.value
        if total>0:
            return (self.h1.value-self.h2.value)/(total)
        else:
            return 0
    
    def reading(self, verbosity=3):
        
        total = self.h1.value + self.h2.value + self.v1.value + self.v2.value
        
        if verbosity>=3:
            print('Reading for {:s} ({:s})'.format(self.name, self.description))
            print('  Horizontal:  {:9.4g}  +  {:9.4g}  =  {:9.4g}'.format(self.h1.value, self.h2.value, self.h1.value+self.h2.value))
            print('    position: {:.3f}'.format(self.h_position()))
            print('  Vertical:    {:9.4g}  +  {:9.4g}  =  {:9.4g}'.format(self.v1.value, self.v2.value, self.v1.value+self.v2.value))
            print('    position: {:.3f}'.format(self.v_position()))

        if verbosity>=2:
            
            print('  Total:  {:9.4g}'.format(total))
            
        return total
    
    
    def current_to_flux(self, current):
        
        energy_keV = self.beam.energy(verbosity=0)
        
        V_ion = 0.036       ## ionization energy of N2 gas in [keV]
        IC_len = 6.0        ## active length of Ion Chamber in [cm]
        qe = 1.602e-19      ## electron charge in [C]

        ## Absorption length [cm] of gas N2 (1 atm, 1.131 g/L) vs E [keV]
        # based on polynomial fit to the calculated abs length data from: henke.lbl.gov/optical_constants/atten2.html 
        # see /home/xf11bm/masa/atten_len_N2* 
        abs_len = 355.21 - 112.26*energy_keV + 11.200*np.square(energy_keV) - 0.10611*np.power(energy_keV,3.0)

        N_abs = current*V_ion/(qe*energy_keV)
        flux = N_abs / (1.0 - np.exp(-IC_len/abs_len))

        return flux
    
    
    def flux(self, verbosity=3):
        
        if self.reading(verbosity=0) < 5e-10:
            return 0.0
        
        h1 = self.current_to_flux(self.h1.value)
        h2 = self.current_to_flux(self.h2.value)
        h_total = h1 + h2
        v1 = self.current_to_flux(self.v1.value)
        v2 = self.current_to_flux(self.v2.value)
        v_total = v1 + v2
        
        total = h_total + v_total
        avg = total*0.5
        
        if verbosity>=3:
            print('Flux for {:s} ({:s})'.format(self.name, self.description))
            print('  Horizontal:  {:9.4g}  +  {:9.4g}  =  {:9.4g} ph/s'.format(h1, h2, h1+h2))
            print('    position: {:.3f}'.format(self.h_position()))
            print('  Vertical:    {:9.4g}  +  {:9.4g}  =  {:9.4g} ph/s'.format(v1, v2, v1+v2))
            print('    position: {:.3f}'.format(self.v_position()))

        if verbosity>=2:
            
            print('  Average:  {:9.4g} ph/s'.format(avg))
            
        return avg 
    
    
    
#ionchamber = IonChamber_CMS(beam=beam)


class Scintillator_CMS(Monitor):
    
    def __init__(self, name='bim4 scintillator', zposition=57, description="Scintillation detector (FMB Oxford C400) between S3 and KB tank in endstation hutch. Captures scattering off of a Kapton film at 45 degrees.", pv=None, beam=None, **args):
        
        super().__init__(name=name, zposition=zposition, description=description, pv=pv, **args)
        self.has_flux = True
        
        self.beam = beam
        
        # PVs
        import epics
        self.sec = epics.PV('XF:11BMB-BI{IM:4}:GET_PERIOD')    # integration time in [sec]
        self.cts = epics.PV('XF:11BMB-BI{IM:4}:C1_1')    # raw counts


    def state(self):
        
        return "in"

    
    def reading(self, verbosity=3):
        
        if self.sec.value == 0.0:
            print('Counting time set to zero. Check CSS settings for FMB Oxford C400.')
            return 0 
        else:
            sec = self.sec.value
            cts = self.cts.value
            cps = cts/sec
        
        if verbosity>=3:
            print('Reading for {:s} ({:s})'.format(self.name, self.description))
            print('  Count time:  {:9.4g} sec'.format(sec))
            print('  Raw counts:  {:9.4g} counts'.format(cts))

        if verbosity>=2:
            print('  Count rate:  {:9.4g} counts/sec'.format(cps))
            
        return cps
    
    
    def cps_to_flux(self, cps):

        ### Ratio between estimated beam flux to raw scintillator counts 
        # (see Olog entry on July 7, 2017)
        # For unslitted, unattenuated beam at 13.5 keV, 
        # BIM4 yields 2.86E5 cts/sec for 1.85E11 ph/s at BIM3:
        # 1.85E11 / 2.86E5 = 647000 (ph/s)/(cts/sec).
        #cps_to_flux_factor = 647000.
        
        ### Ratio between estimated beam flux to raw scintillator counts (see Olog entry on January 18, 2018)
        # For unslitted beam with absorber 4 and evacuated chamber, 
        # BIM4 yields 1.978E5 cts/sec for 1.73E11 ph/s at BIM3 and 1.55e11 ph/s at Pilatus2M:
        # Scale factor = (1.545e11 ph/sec) / (1.978e+05 ph/s) = 7.786e5.
        cps_to_flux_factor = 7.786E5

        flux = cps_to_flux_factor * cps

        return flux
    
    
    def flux(self, verbosity=3):
        
        if self.reading(verbosity=0) < 5e-10:
            return 0.0

        flux = self.cps_to_flux(self.reading(verbosity=0))        
        
        
        if verbosity>=3:
            print('Flux for {:s} ({:s})'.format(self.name, self.description))

        if verbosity>=2:
            print('  Beam flux:  {:9.4g} ph/s'.format(flux))
            
        return flux 
    
    
class DiamondDiode_CMS(Monitor):
    
    def __init__(self, name='bim5 diamonddiode', zposition=58.2, description="Diamond diode BPM (Dectris RIGI via FMB Oxford F460) between KB tank and sample chamber in endstation hutch. Needs to be insered into beam via IM:5.", pv=None, beam=None, **args):
        
        super().__init__(name=name, zposition=zposition, description=description, pv=pv, **args)
        self.has_flux = True
        
        self.beam = beam
        
        # PVs
        import epics
        self.i0 = epics.PV('XF:11BMB-BI{BPM:1}Cur:I0-I')    # upper left
        self.i1 = epics.PV('XF:11BMB-BI{BPM:1}Cur:I1-I')    # upper right
        self.i2 = epics.PV('XF:11BMB-BI{BPM:1}Cur:I2-I')    # lower left
        self.i3 = epics.PV('XF:11BMB-BI{BPM:1}Cur:I3-I')    # lower right
        
    def state(self):

        # TODO: fix this so it queries state of IM:5        
        return "in"
    
    
    def v_position(self):
        
        total = self.i0.value + self.i1.value + self.i2.value + self.i3.value
        if total>0:
            return (self.i0.value + self.i1.value - self.i2.value - self.i3.value)/(total)
        else:
            return 0

    def h_position(self):
        
        total = self.i0.value + self.i1.value + self.i2.value + self.i3.value
        if total>0:
            return (self.i1.value + self.i3.value - self.i0.value - self.i2.value)/(total)
        else:
            return 0
    
    def reading(self, verbosity=3):
        
        #total = self.i0.value + self.i1.value + self.i2.value + self.i3.value
        ## 07/12/2017  Total dark current with beam off is ~9.3e-10 A.
        dark_current = 9.3e-10
        total = self.i0.value + self.i1.value + self.i2.value + self.i3.value - dark_current
        
        if verbosity>=3:
            print('Reading for {:s} ({:s})'.format(self.name, self.description))
            print('  Horizontal:')
            print('    Right:  {:9.4g}  +  {:9.4g}  =  {:9.4g} A'.format(self.i1.value, self.i3.value, self.i1.value+self.i3.value))
            print('    Left:  {:9.4g}  +  {:9.4g}  =  {:9.4g} A'.format(self.i0.value, self.i2.value, self.i0.value+self.i2.value))
            print('    Position [-1(L) to 1(R), 0 at center]: {:.3f}'.format(self.h_position()))
            print('  Vertical:')
            print('    Top:  {:9.4g}  +  {:9.4g}  =  {:9.4g} A'.format(self.i0.value, self.i1.value, self.i0.value+self.i1.value))
            print('    Bottom:  {:9.4g}  +  {:9.4g}  =  {:9.4g} A'.format(self.i2.value, self.i3.value, self.i2.value+self.i3.value))
            print('    Position [-1(B) to 1(T), 0 at center]: {:.3f}'.format(self.v_position()))

        if verbosity>=2:
            
            print('  Total current:  {:9.4g} A'.format(total))
            
        return total
    
    
    def current_to_flux(self, current):

        ### Ratio between estimated beam flux to raw TOTAL current for the 4 quadrants 
        # (see Olog entry on July 7, 2017).
        # For unslitted, unattenuated beam at 13.5 keV, 
        # BIM5 yields a TOTAL current of 4.8E-8 A at ~230 mA ring current, 
        # corresponding to 1.38E11 ph/s at BIM3:
        # 1.38E11 / 4.8E-8 = 0.29E19 (ph/s)/A.
        # With dark current (total = 9.3e-10 A = 0.093e-8 A) taken into account, 
        # 1.38E11 / 4.7E-8 = 0.294E19 (ph/s)/A.
        #current_to_flux_factor = 2.94E18

        ### Ratio between estimated beam flux to raw TOTAL current for the 4 quadrants 
        # (see Olog entry on January 18, 2018).
        # For unslitted beam with absorber 4 and evacuated chamber, 
        # BIM5 yields 5.09e-8 A for for 1.73E11 ph/s at BIM3 and 1.55e11 ph/s at Pilatus2M:
        # Scale factor = (1.545e11 ph/sec) / (5.0902e-08 A) = 3.025e+18
        current_to_flux_factor = 3.025E18

        flux = current_to_flux_factor * current

        return flux

    
    def flux(self, verbosity=3):
        
        if self.reading(verbosity=0) < 1e-11:
            return 0.0
        
        right = self.current_to_flux(self.i1.value+self.i3.value)
        left = self.current_to_flux(self.i0.value+self.i2.value)
        top = self.current_to_flux(self.i0.value+self.i1.value)
        bottom = self.current_to_flux(self.i2.value+self.i3.value)
        total = self.current_to_flux(self.reading(verbosity=0))
        
        if verbosity>=3:
            print('Flux for {:s} ({:s})'.format(self.name, self.description))
            print('  Horizontal:')
            print('    Right:  {:9.4g} ph/s'.format(right))
            print('    Left:  {:9.4g} ph/s'.format(left))
            print('    Position [-1(L) to 1(R), 0 at center]: {:.3f}'.format(self.h_position()))
            print('  Vertical:')
            print('    Top:  {:9.4g} ph/s'.format(top))
            print('    Bottom:  {:9.4g} ph/s'.format(bottom))
            print('    Position [-1(B) to 1(T), 0 at center]: {:.3f}'.format(self.v_position()))

        if verbosity>=2:
            
            print('  Total flux:  {:9.4g} ph/s'.format(total))
            
        return total 


# CMSBeam
################################################################################
class CMSBeam(object):
    """
    This class represents the 'beam' at the beamline. This collects together aspects
    of querying or changing beam properties, including the energy (or wavelength), 
    the beam intensity (or measuring flux), and so forth.
    """
    
    def __init__(self):
        
        self.mono_bragg_pv = 'XF:11BMA-OP{Mono:DMM-Ax:Bragg}Mtr.RBV'
        
        # (planck constant * speed of light)/(electronic charge)
        self.hc_over_e = 1.23984197e-6 # m^3 kg s^-3 Amp^-1 = eV*m
        self.hc_over_e_keVpA = self.hc_over_e*1e7 # = 12.4 keV*Angstrom
        
        # DMM bilayer pitch in Angstroms, according to Rigaku metrology report
        self.dmm_dsp = 20.1 # Angstroms
        
        
        
        self.mono = BeamlineElement('monochromator', 26.5)
        def transmission(verbosity=0):
            return 1e-7
        self.mono.transmission = transmission

        
        self.attenuator = BeamlineElement('attenuator', 53.8, description="Attenuator/filter box")
        self.attenuator.has_flux = False
        def reading(verbosity=0):
            return self.transmission(verbosity=verbosity)
        self.attenuator.reading = reading
        self.attenuator.transmission = self.transmission
        
        self.attenuator2 = BeamlineElement('attenuator2', 58.6, description="Nb foil absorber")
        self.attenuator2.has_flux = False
        def reading(verbosity=0):
            return self.absorber(verbosity=verbosity)[1]
        self.attenuator2.reading = reading
        self.attenuator2.transmission = reading
        #define the original position of aborber (6 Nb foils for XRR)
        #the position is defined in 'config_update'. This position is a good reference. 
        self.armr_absorber_o = -55.1
        self.absorber_transmission_list_13p5kev = [1, 0.041, 0.0017425, 0.00007301075, 0.00000287662355, 0.000000122831826, 0.00000000513437]    # at E = 13.5keV
        self.absorber_transmission_list_17kev = [1, 1.847e-1, 3.330e-2, 6.064e-3, 1.101e-3, 1.966e-4, 3.633e-5]    # at E = 13.5keV
        #TODO: make this energy dependent
        
        if False:
            self.fs1 = DiagnosticScreen( 'fs1', 27.2, pv='XF:11BMA-BI{FS:1}', epics_signal=StandardProsilica('XF:11BMA-BI{FS:1-Cam:1}', name='fs1') )
            #self.fs2 = DiagnosticScreen( 'fs2', 29.1, pv='XF:11BMA-BI{FS:2}', epics_signal=StandardProsilica('XF:11BMA-BI{FS:2-Cam:1}', name='fs2') )
            self.fs3 = DiagnosticScreen( 'fs3', 55.8, pv='XF:11BMB-BI{FS:3}', epics_signal=StandardProsilica('XF:11BMB-BI{FS:3-Cam:1}', name='fs3') )
            self.fs4 = DiagnosticScreen( 'fs4', 58.2, pv='XF:11BMB-BI{FS:4}', epics_signal=StandardProsilica('XF:11BMB-BI{FS:4-Cam:1}', name='fs4') )
            self.fs5 = DiagnosticScreen( 'fs5', 70.0, pv='XF:11BMB-BI{FS:Test-Cam:1}', epics_signal=StandardProsilica('XF:11BMB-BI{FS:4-Cam:1}', name='fs5') )
        else:
            # Rely on the fact that these are defined in 20-area-detectors.py
            self.fs1 = DiagnosticScreen( 'fs1', 27.2, pv='XF:11BMA-BI{FS:1}', epics_signal=fs1 )
            #self.fs2 = DiagnosticScreen( 'fs2', 29.1, pv='XF:11BMA-BI{FS:2}', epics_signal=fs2 )
            self.fs3 = DiagnosticScreen( 'fs3', 55.8, pv='XF:11BMB-BI{FS:3}', epics_signal=fs3 )
            self.fs4 = DiagnosticScreen( 'fs4', 58.2, pv='XF:11BMB-BI{FS:4}', epics_signal=fs4 )
            self.fs5 = DiagnosticScreen( 'fs5', 70.0, pv='XF:11BMB-BI{FS:Test-Cam:1}', epics_signal=fs5 )
            
            
        self.bim3 = IonChamber_CMS(beam=self)
        self.bim4 = Scintillator_CMS()
        self.beam_defining_slit = s4
        self.bim5 = DiamondDiode_CMS()
        self.bim6 = PointDiode_CMS()
        
        self.GVdsbig = GateValve('GV ds big', 60.0, pv='XF:11BMB-VA{Chm:Det-GV:1}')
        
        
        
        self.elements = []
        
        # Front End
        self.elements.append(ThreePoleWiggler())
        #SR:C03-EPS{PLC:1}Sts:BM_BMPS_Opn-Sts BMPS
        self.elements.append(GateValve('GV1', 20.0, pv='FE:C03A-VA{GV:1}DB:'))
        self.elements.append(GateValve('GV2', 21.0, pv='FE:C03A-VA{GV:2}DB:'))
        
        
        # FOE
        self.elements.append(Shutter('FE shutter', 25.0, pv='XF:11BM-PPS{Sh:FE}'))
        self.elements.append(GateValve('GV', 26.0, pv='FE:C11B-VA{GV:2}'))
        self.elements.append(self.mono)
        self.elements.append(self.fs1)
        # bim1
        # slit0
        # bim2
        self.elements.append(GateValve('GV', 28.0, pv='XF:11BMA-VA{Slt:0-GV:1}'))
        self.elements.append(BeamlineElement('mirror', 29.1))
        self.elements.append(GateValve('GV', 30.5, pv='XF:11BMA-VA{Mir:Tor-GV:1}'))
        self.elements.append(BeamlineElement('fs2 (manual)', 30.9)) # self.elements.append(self.fs2)
        self.elements.append(Shutter('photon shutter', 33.7, pv='XF:11BMA-PPS{PSh}'))
        self.elements.append(GateValve('GV', 34.0, pv='XF:11BMA-VA{PSh:1-GV:1}'))
        
        # Endstation
        self.elements.append(self.bim3)
        # Experimental shutter 49.5
        self.elements.append(self.attenuator)
        self.elements.append(self.fs3)
        self.elements.append(self.bim4) # scintillation detector
        self.elements.append(BeamlineElement('KB mirrors', 57.8))
        self.elements.append(self.fs4)
        self.elements.append(self.bim5) # diamond diode BPM
        # im4
        #self.elements.append(GateValve('GV us small', 58.5, pv='XF:11BMB-VA{Slt:4-GV:1}'))
        self.elements.append(self.attenuator2)
        
        self.elements.append(BeamlineElement('sample', 58.8))
        self.elements.append(self.bim6) # dsmon
        self.elements.append(BeamlineElement('WAXS detector', 59.0))
        self.elements.append(self.GVdsbig)
        self.elements.append(BeamlineElement('SAXS detector', 58.8+5))
        
        
        
        # Sort by position along the beam
        self.elements.sort(key=lambda o: o.zposition, reverse=False)
    
    
    # Monochromator
    ########################################
    
    def energy(self, verbosity=3):
        """
        Returns the current x-ray photon energy (in keV).
        """
        
        # Current angle of monochromator multilayer crystal
        Bragg_deg = caget(self.mono_bragg_pv)
        Bragg_rad = np.radians(Bragg_deg)
        
        wavelength_A = 2.*self.dmm_dsp*np.sin(Bragg_rad)
        wavelength_m = wavelength_A*1e-10

        energy_eV = self.hc_over_e/wavelength_m
        energy_keV = energy_eV/1000.
        
        if verbosity>=3:
            print('E = {:.2f} keV, wavelength = {:.4f} Å, Bragg = {:.6f} rad = {:.4f} deg'.format(energy_keV, wavelength_A, Bragg_rad, Bragg_deg))
            
        elif verbosity>=1:
            print('E = {:.3f} keV'.format(energy_keV))
        
        return energy_keV
        
        
    def wavelength(self, verbosity=3):
        """
        Returns the current x-ray photon wavelength (in Angstroms).
        """
        
        # Current angle of monochromator multilayer crystal
        Bragg_deg = caget(self.mono_bragg_pv)
        Bragg_rad = np.radians(Bragg_deg)
        
        wavelength_A = 2.*self.dmm_dsp*np.sin(Bragg_rad)
        wavelength_m = wavelength_A*1e-10

        # (planck constant * speed of light)/(electronic charge)
        
        energy_eV = self.hc_over_e/wavelength_m
        energy_keV = energy_eV/1000.
        
        if verbosity>=3:
            print('wavelength = {:.4f} Å, E = {:.2f} keV, Bragg = {:.6f} rad = {:.4f} deg'.format(wavelength_A, energy_keV, Bragg_rad, Bragg_deg))
            
        elif verbosity>=1:
            print('wavelength = {:.5f} Å'.format(wavelength_A))
        
        return wavelength_A
    
    
    def setEnergy(self, energy_keV, verbosity=3):
        """
        Set the x-ray beam to the specified energy (by changing the
        monochromator angle.
        """
        
        energy_eV = energy_keV*1000.
        wavelength_m = self.hc_over_e/energy_eV
        wavelength_A = wavelength_m*1.e10
        
        self.setWavelength(wavelength_A, verbosity=verbosity)
        
        return self.energy(verbosity=0)
    
    
    def setWavelength(self, wavelength_A, verbosity=3):
        """
        Set the x-ray beam to the specified wavelength (by changing the
        monochromator angle.
        """
        
        Bragg_deg_initial = caget(self.mono_bragg_pv)
        wavelength_m = wavelength_A*1.e-10
        Bragg_rad = np.arcsin(wavelength_A/(2.*self.dmm_dsp))
        Bragg_deg = np.degrees(Bragg_rad)
        
        print('mono_bragg will move to {:.4f}g deg'.format(Bragg_deg))
        response = input('    Are you sure? (y/[n]) ')
        if response is 'y' or response is 'Y':
            
            #mov(mono_bragg, Bragg_deg)
            #mono_bragg.move = Bragg_deg
            mono_bragg.move(Bragg_deg)
            
            if verbosity>=1:
                print('mono_bragg moved from {:.4f} deg to {:.4f} deg'.format(Bragg_deg_initial, Bragg_deg))
        
        elif verbosity>=1:
            print('No move was made.')
            
        return self.wavelength(verbosity=verbosity)

    
    # Slits
    ########################################
    
    def size(self, verbosity=3):
        """
        Returns the current beam size (rough estimate).
        The return is (size_horizontal, size_vertical) (in mm).
        """
        size_h = self.beam_defining_slit.xg.user_readback.value
        size_v = self.beam_defining_slit.yg.user_readback.value
        
        if verbosity>=3:
            print('Beam size:')
            print('  horizontal = {:.3f} mm'.format(size_h))
            print('  vertical   = {:.3f} mm'.format(size_v))
        
        return size_h, size_v

    
    def setSize(self, horizontal, vertical, verbosity=3):
        """
        Sets the beam size.
        """
        
        h, v = self.size(verbosity=0)
        
        if verbosity>=3:
            print('Changing horizontal beam size from {:.3f} mm to {:.3f} mm'.format(h, horizontal))
        self.beam_defining_slit.xg.user_setpoint.value = horizontal
        
        if verbosity>=3:
            print('Changing vertical beam size from {:.3f} mm to {:.3f} mm'.format(v, vertical))
        
        self.beam_defining_slit.yg.user_setpoint.value = vertical
    
    
    def divergence(self, verbosity=3):
        """
        Returns the beamline divergence.
        This is based on the Front End (FE) slits. The return is
        (horizontal, vertical) (in mrad).
        """
        
        distance_m = 10.0 # distance from source to slits
        
        horizontal_mm = caget('FE:C11B-OP{Slt:12-Ax:X}t2.C')
        vertical_mm = caget('FE:C11B-OP{Slt:12-Ax:Y}t2.C')
        
        horizontal_mrad = horizontal_mm/distance_m
        vertical_mrad = vertical_mm/distance_m
        
        if verbosity>=3:
            print('Beam divergence:')
            print('  horizontal = {:.3f} mrad'.format(horizontal_mrad))
            print('  vertical   = {:.3f} mrad'.format(vertical_mrad))
        
        return horizontal_mrad, vertical_mrad
        
    
    def setDivergence(self, horizontal, vertical, verbosity=3):
        """
        Set beamline divergence (in mrad).
        This is controlled using the Front End (FE) slits.
        """
        
        h, v = self.divergence(verbosity=0)

        distance_m = 10.0 # distance from source to slits
        
        horizontal_mm = horizontal*distance_m
        vertical_mm = vertical*distance_m
        
        if horizontal<0:
            if verbosity>=1:
                print("Horizontal divergence less than zero ({}) doesn't make sense.".format(horizontal))
            
        elif horizontal>1.5:
            if verbosity>=1:
                print("Horizontal divergence should be less than 1.5 mrad.")
                
        else:
            if verbosity>=3:
                print('Changing horizontal divergence from {:.3f} mrad to {:.3f} mrad.'.format(h, horizontal))
            caput('FE:C11B-OP{Slt:12-Ax:X}size', horizontal_mm)
        
        
        if vertical<0:
            if verbosity>=1:
                print("Vertical divergence less than zero ({}) doesn't make sense.".format(vertical))
            
        elif vertical>0.15:
            if verbosity>=1:
                print("Vertical divergence should be less than 0.15 mrad.")
                
        else:
            if verbosity>=3:
                print('Changing vertical divergence from {:.3f} mrad to {:.3f} mrad.'.format(v, vertical))
            caput('FE:C11B-OP{Slt:12-Ax:Y}size', vertical_mm)
        

    
    # Experimental Shutter
    ########################################
    
    def is_on(self, verbosity=3):
        '''Returns true if the beam is on (experimental shutter open).'''
        
        blade1 = caget('XF:11BMB-OP{PSh:2}Pos:1-Sts')
        blade2 = caget('XF:11BMB-OP{PSh:2}Pos:2-Sts')
        
        if blade1==1 and blade2==1:
            if verbosity>=4:
                print('Beam on (shutter open).')
            
            return True
        
        else:
            if verbosity>=4:
                print('Beam off (shutter closed).')
            
            return False
    
    
    def on(self, verbosity=3, wait_time=0.1, poling_period=0.10, retry_time=2.0, max_retries=5):
        '''Turn on the beam (open experimental shutter).
        update: 090517, RL: change the wait_time from 0.005 to 0.1, change sleep to time.sleep'''
        
        if self.is_on(verbosity=0):
            if verbosity>=4:
                print('Beam on (shutter already open.)')
                
        else:
            
            itry = 0
            while (not self.is_on(verbosity=0)) and itry<max_retries:
            
                # Trigger the shutter to toggle state
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M112=1')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M111=1')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M112=0')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M111=1')
                time.sleep(wait_time)
                
                # Give the system a chance to update
                start_time = time.time()
                while (not self.is_on(verbosity=0)) and (time.time()-start_time)<retry_time:
                    if verbosity>=5:
                        print('  try {:d}, t = {:02.2f} s, state = {:s}'.format(itry+1, (time.time()-start_time), 'OPEN_____' if self.is_on(verbosity=0) else 'CLOSE===='))
                    time.sleep(poling_period)
                
                itry += 1
                

            if verbosity>=4:
                if self.is_on(verbosity=0):
                    print('Beam on (shutter opened).')
                else:
                    print("Beam off (shutter didn't open).")

    
    def off(self, verbosity=3, wait_time=0.1, poling_period=0.10, retry_time=2.0, max_retries=5):
        '''Turn off the beam (close experimental shutter).
        update: 090517, RL: change the wait_time from 0.005 to 0.1, change sleep to time.sleep'''
        
        if self.is_on(verbosity=0):
            
            itry = 0
            while self.is_on(verbosity=0) and itry<max_retries:
                # Trigger the shutter to toggle state
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M112=1')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M111=1')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M112=0')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M111=1')
                time.sleep(wait_time)

                # Give the system a chance to update
                start_time = time.time()
                while self.is_on(verbosity=0) and (time.time()-start_time)<retry_time:
                    if verbosity>=5:
                        print('  try {:d}, t = {:02.2f} s, state = {:s}'.format(itry+1, (time.time()-start_time), 'OPEN_____' if self.is_on(verbosity=0) else 'CLOSE===='))
                    time.sleep(poling_period)
                
                itry += 1



            if verbosity>=4:
                if self.is_on(verbosity=0):
                    print("Beam on (shutter didn't close).")
                else:
                    print('Beam off (shutter closed).')
                
        else:
            if verbosity>=4:
                print('Beam off (shutter already closed).')
                
    def blade1_is_on(self, verbosity=3):
        '''Returns true if the beam is on (experimental shutter open).'''
        
        blade1 = caget('XF:11BMB-OP{PSh:2}Pos:1-Sts')
        
        if blade1==1:
            if verbosity>=4:
                print('Beam on (shutter open).')
            
            return True
        
        else:
            if verbosity>=4:
                print('Beam off (shutter closed).')
            
            return False

    def blade2_is_on(self, verbosity=3):
        '''Returns true if the beam is on (experimental shutter open).'''
        
        blade2 = caget('XF:11BMB-OP{PSh:2}Pos:2-Sts')
        
        if blade2==1:
            if verbosity>=4:
                print('Beam on (shutter open).')
            
            return True
        
        else:
            if verbosity>=4:
                print('Beam off (shutter closed).')
            
            return False
                
    def _test_on(self, verbosity=3, wait_time=0.1, poling_period=0.10, retry_time=2.0, max_retries=5):
        '''Turn on the beam (open experimental shutter).'''
 
        #print('1')
        #print(sam.clock())
        if self.is_on(verbosity=0):
            if verbosity>=4:
                print('Beam on (shutter already open.)')
                
        else:
            
            itry = 0
            while (not self.blade1_is_on(verbosity=0)) and itry<max_retries:
            
                # Trigger the shutter to toggle state
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M112=1')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M111=1')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M112=0')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M111=1')
                time.sleep(wait_time)
                
                # Give the system a chance to update
                start_time = time.time()
                
                #print('2')
                #print(sam.clock())
                
               
                while (not self.blade1_is_on(verbosity=0)) and (time.time()-start_time)<retry_time:
                    if verbosity>=5:
                        print('  try {:d}, t = {:02.2f} s, state = {:s}'.format(itry+1, (time.time()-start_time), 'OPEN_____' if self.is_on(verbosity=0) else 'CLOSE===='))
                    sleep(poling_period)
                    #print('3')
                    #print(sam.clock())
                
                itry += 1
                

            if verbosity>=4:
                if self.blade1_is_on(verbosity=0):
                    print('Beam on (shutter opened).')
                else:
                    print("Beam off (shutter didn't open).")
        #print('4')
        #print(sam.clock())
        
        
    def _test_off(self, verbosity=3, wait_time=0.1, poling_period=0.10, retry_time=2.0, max_retries=5):
        '''Turn off the beam (close experimental shutter).'''
        
        #print('1')
        #print(sam.clock())
        
        if self.is_on(verbosity=0):
            
            itry = 0
            while self.is_on(verbosity=0) and itry<max_retries:
                # Trigger the shutter to toggle state
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M112=1')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M111=1')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M112=0')
                time.sleep(wait_time)
                caput('XF:11BMB-CT{MC:06}Asyn.AOUT','M111=1')
                time.sleep(wait_time)

                # Give the system a chance to update
                start_time = time.time()
                
                #print('2')
                #print(sam.clock())
                
                while self.is_on(verbosity=0) and (time.time()-start_time)<retry_time:
                    if verbosity>=5:
                        print('  try {:d}, t = {:02.2f} s, state = {:s}'.format(itry+1, (time.time()-start_time), 'OPEN_____' if self.is_on(verbosity=0) else 'CLOSE===='))
                    time.sleep(poling_period)
                    
                    #print('3')
                    #print(sam.clock())
                
                itry += 1



            if verbosity>=4:
                if self.blade1_is_on(verbosity=0):
                    print("Beam on (shutter didn't close).")
                else:
                    print('Beam off (shutter closed).')
            #print('4')
            #print(sam.clock())
                
        else:
            if verbosity>=4:
                print('Beam off (shutter already closed).')    

        #print('5')
        #print(sam.clock())


    # Attenuator/Filter Box
    ########################################

    def transmission(self, verbosity=3):
        """
        Returns the current beam transmission through the attenuator/filter box.
        To change the transmission, use 'setTransmission'.
        """
        
        energy_keV = self.energy(verbosity=0)
        
        if energy_keV < 6.0 or energy_keV > 18.0:
            print('Transmission data not available at the current X-ray energy ({.2f} keV).'.format(energy_keV))
            
        else:
            
            # The states of the foils in the filter box
            N = [ caget('XF:11BMB-OP{{Fltr:{:d}}}Pos-Sts'.format(ifoil)) for ifoil in range(1, 8+1) ]
            
            tr_tot = self.calc_transmission_filters(N, verbosity=verbosity)
                    
            return tr_tot


    def calc_transmission_filters(self, filter_settings, energy_keV=None, verbosity=3):
        """
        Returns the computed transmission value for the given configuration of
        foils. Note that the foils are not actually moved. This is just a
        calculation.
        
        Parameters
        ----------
        filter_settings : array of length 8
            Each element must be either a zero (foil removed) or a 1 (foil blocking 
            beam)
        energy_keV : float
            If 'None', the current energy is used. If specified, the calculation 
            is performed for the requested energy.
            
        Returns                
                

        -------
        transmission : float
            The computed transmission value of the x-ray beam through the filter box.
        """
        
        if energy_keV is None:
            energy_keV = self.energy(verbosity=0)
            
        if len(filter_settings) != 8:
            print('States for all eight foils must be specified.')

        else:
            N = filter_settings
            
            E = energy_keV
            E2 = np.square(E)
            E3 = np.power(E, 3)
                        

            # foil thickness blocking the beam
            N_Al = N[0] + 2*N[1] + 4*N[2] + 8*N[3]
            N_Nb = N[4] + 2*N[5] + 4*N[6] + 8*N[7]

            d_Nb = 0.1      # Thickness [mm] of one Nb foil 
            d_Al = 0.25     # Thickness [mm] of one Al foil 

            # Absorption length [mm] based on fits to LBL CXRO data for 6 < E < 19 keV
            l_Nb = 1.4476e-3 - 5.6011e-4 * E + 1.0401e-4 * E2 + 8.7961e-6 * E3
            l_Al = 5.2293e-3 - 1.3491e-3 * E + 1.7833e-4 * E2 + 1.4001e-4 * E3

            # transmission factors
            tr_Nb = np.exp(-N_Nb*d_Nb/l_Nb)
            tr_Al = np.exp(-N_Al*d_Al/l_Al)
            tr_tot = tr_Nb*tr_Al
                
            if verbosity>=5:
                print('  state:      {} T = {:.6g}'.format(filter_settings, tr_tot))
            if verbosity>=4:
                print('{:d} × 0.25 mm Al ({:.4g}) and {:d} × 0.10 mm Nb ({:.4g})'.format(N_Al, tr_Al, N_Nb, tr_Nb) )
            if verbosity>=1:
                print('transmission = {:.6g}'.format(tr_tot))
                
            return tr_tot
            
        

    def set_attenuation_filters(self, filter_settings, verbosity=3):
        """
        Sets the positions (in/out) for each of the foils in the attenuator/
        filter box. The input 'filter_settings' should be an array of length
        8, where each element is either a zero (foil removed) or a 1 (foil
        blocking beam).
        """
        
        if verbosity>=4:
            print('Filters:')
            # The states of the foils in the filter box
            filters_initial = [ caget('XF:11BMB-OP{{Fltr:{:d}}}Pos-Sts'.format(ifoil)) for ifoil in range(1, 8+1) ]
            print('  initial:    {} T = {:.6g}'.format(filters_initial, self.calc_transmission_filters(filters_initial, verbosity=0)))
            print('  requested:  {} T = {:.6g}'.format(filter_settings, self.calc_transmission_filters(filter_settings, verbosity=0)))
        
        if len(filter_settings) != 8:
            print('States for all eight foils must be specified.')
            
        else:
            
            for i, state in enumerate(filter_settings):
                
                ifoil = i+1
                
                if state==1:
                    # Put foil #ifoil into the beam
                    caput( 'XF:11BMB-OP{{Fltr:{:d}}}Cmd:In-Cmd'.format(ifoil) , 1 )
                    
                elif state==0:
                    # Remove foil #ifoil
                    caput( 'XF:11BMB-OP{{Fltr:{:d}}}Cmd:Out-Cmd'.format(ifoil) , 1 )
                    
                else:
                    if verbosity>=3:
                        state_actual = caget( 'XF:11BMB-OP{{Fltr:{:d}}}Pos-Sts'.format(ifoil) )
                        state_actual_str = 'IN' if state_actual is 1 else 'OUT'
                        print('WARNING: Filter state {} not recognized. Filter {:d} is {:s}.'.format(state, ifoil, state_actual_str))
                    

        
            time.sleep(1.) # Wait for filter box to settle
            
        if verbosity>=4:
            filters_final = [ caget('XF:11BMB-OP{{Fltr:{:d}}}Pos-Sts'.format(ifoil)) for ifoil in range(1, 8+1) ]
            print('  final:      {} T = {:.6g}'.format(filters_final, self.calc_transmission_filters(filters_final, verbosity=0)))

        
    def setTransmission(self, transmission, retries=3, tolerance=0.5, verbosity=3):
        """
        Sets the transmission through the attenuator/filter box.
        Because the filter box has a discrete set of foils, it is impossible to
        exactly match a given transmission value. A nearby value will be
        selected.
        """
        
        energy_keV = self.energy(verbosity=0)
        
        if energy_keV < 6.0 or energy_keV > 18.0:
            print('Transmission data not available at the current X-ray energy ({.2f} keV).'.format(energy_keV))
            
        elif transmission > 1.0:
            print('A transmission above 1.0 is not possible.')
            
        elif transmission < 1e-10:
            print('A transmission this low ({:g}) cannot be reliably achieved.'.format(transmission))
            
        else:
            
            E = energy_keV
            E2 = np.square(E)
            E3 = np.power(E, 3)
            
            d_Nb = 0.1      # Thickness [mm] of one Nb foil 
            d_Al = 0.25     # Thickness [mm] of one Al foil 

            # Absorption length [mm] based on fits to LBL CXRO data for 6 < E < 19 keV
            l_Nb = 1.4476e-3 - 5.6011e-4 * E + 1.0401e-4 * E2 + 8.7961e-6 * E3
            l_Al = 5.2293e-3 - 1.3491e-3 * E + 1.7833e-4 * E2 + 1.4001e-4 * E3

            d_l_Nb = d_Nb/l_Nb
            d_l_Al = d_Al/l_Al

            # Number of foils to be inserted (equivalent to "XIA_attn.mac" from X9) 
            #N_Nb = int(-log(transmission)/d_l_Nb)
            ##N_Al = int((-log(transmission) - N_Nb*d_l_Nb)/(d_l_Al-0.5))
            #N_Al = int((-log(transmission) - N_Nb*d_l_Nb)/d_l_Al)

            # Number of foils to be inserted (picks a set that gives smallest deviation from requested transmission)
            dev = []
            for i in np.arange(16):
                for j in np.arange(16):
                    dev_ij = abs(transmission - exp(-i*d_l_Nb)*exp(-j*d_l_Al))
                    dev.append(dev_ij)
                    if (dev_ij == min(dev)):
                        N_Nb = i                    # number of Nb foils selected
                        N_Al = j                    # number of Al foils selected
                
                


            N = []
            state = N_Al
            for i in np.arange(4):
                N.append(state % 2)
                state = int(state/2)

            state = N_Nb
            for i in np.arange(4):
                N.append(state % 2)
                state = int(state/2)

            self.set_attenuation_filters(N, verbosity=verbosity)
            
        
        # Check that transmission was actually correctly changed
        if abs(self.transmission(verbosity=0)-transmission)/transmission > tolerance:
            if retries>0:
                #time.sleep(0.5)
                # Try again
                return self.setTransmission(transmission, retries=retries-1, tolerance=tolerance, verbosity=verbosity)
            
            else:
                print("WARNING: transmission didn't update correctly (request: {}; actual: {})".format(transmission, self.transmission(verbosity=0)))

        
        return self.transmission(verbosity=verbosity)

    
    ## Nb foil absorber, before slit s5
    ########################################
    
    def absorber(self, verbosity=3):
        """
        Returns the current absorber position and absorption transmission.
        To change the absorption for XRR, use 'setabsorber'.
        """
        
        energy_keV = self.energy(verbosity=0)
        
        if energy_keV < 6.0 or energy_keV > 18.0:
            print('Transmission data not available at the current X-ray energy ({.2f} keV).'.format(energy_keV))
            
        else:
            
            # The foil layers 
            slot = np.floor((armr.position - self.armr_absorber_o+3-.1)/6)
                    
            return self.absorberCalcTransmission(slot, verbosity=verbosity)

    def absorberCalcTransmission(self, slot, verbosity=3):
        
        energy_keV = self.energy(verbosity=0)
        
        E = energy_keV
        E2 = np.square(E)
        E3 = np.power(E, 3)
            
        d_Nb = 0.110      # Thickness [mm] of one Nb foil (nominally 0.1 mm); this yields one-foil transmission of 0.041 at 13.5 keV, close to measured value 

        # Absorption length [mm] based on fits to LBL CXRO data for 6 < E < 19 keV
        l_Nb = 1.4476e-3 - 5.6011e-4 * E + 1.0401e-4 * E2 + 8.7961e-6 * E3
        d_l_Nb = d_Nb/l_Nb

        absorber_transmission = exp(-slot*d_l_Nb)
        
        if abs(E - 13.5) < 0.01:
            self.absorber_transmission_list = [1, 0.041, 0.0017425, 0.00007301075, 0.00000287662355, 0.000000122831826, 0.00000000513437]    # at E = 13.5keV
        else:
            tmp_list = []
            for i in np.arange(6+1):
                tmp_list.append(exp(-i*d_l_Nb))
            self.absorber_transmission_list = tmp_list

        if verbosity>=1:
            print('transmission = {:.6g}'.format(absorber_transmission))
        
        return slot, absorber_transmission
        
    def setAbsorber(self, slot, retries=3, tolerance=0.5, verbosity=3):
        """
        Set the aborber of Nb foils for XRR measurements.
        There are 6 layers of foil which gives the attenuation rate ~5-6% at 13.5kev.
        """
        
        energy_keV = self.energy(verbosity=0)
        
        if energy_keV < 6.0 or energy_keV > 18.0:
            print('Transmission data not available at the current X-ray energy ({.2f} keV).'.format(energy_keV))
        elif slot < 0 or slot > 6:
            print('Absorber cannot move beyond [0, 6]')
                          
        else:
            
            #move to slot # for correct attenuation.
            armr.move(self.armr_absorber_o+slot*6)  # 6 mm wide per slot
                
        # Check that absorber was actually correctly moved
        if abs(armr.position-(self.armr_absorber_o+slot*6)) > tolerance:
            if retries>0:
                #time.sleep(0.5)
                # Try again
                return self.absorberCalcTransmission(slot), self.setAbsorber(transmission, retries=retries-1, tolerance=tolerance, verbosity=verbosity)
            
            else:
                print("WARNING: transmission didn't update correctly (request: {}; actual: {})".format(transmission, self.transmission(verbosity=0)))        

        else:
            return self.absorberCalcTransmission(slot)
        
        
    # Flux estimates at various points along the beam
    ########################################
    
    # TBD
    
    
    # Flux diagnostics
    ########################################
    
    def fluxes(self, verbosity=3):
        """
        Outputs a list of fluxes at various points along the beam. Also checks 
        the state (in or out of the beam) of various components, to help identify
        if anything could be blocking the beam.
        """
        
        if verbosity>=1:
            print('+--------+------------------+-----+-------------+-------------+-------------+')
            print('| pos    | name             |path | reading     | flux (ph/s) | expected    |')
            print('|--------|------------------|-----|-------------|-------------|-------------|')
            
        
        last_z = -100
        beam = True
        
        flux_expected = None
        
        for element in self.elements:
            
            state = element.state()
            if state is 'block':
                beam = False
            
            if verbosity>=4:
                if element.zposition >= 0 and last_z < 0:
                    print('| Front End                 |     |             |             |             |')
                if element.zposition > 25 and last_z < 25:
                    print('| FOE                       |     |             |             |             |')
                if element.zposition > 50 and last_z < 50:
                    print('| Endstation                |     |             |             |             |')
            last_z = element.zposition
            flux_expected
            if verbosity>=1:
                
                
                if state is 'in':
                    if beam:
                        path = '(|)'
                    else:
                        path = '(-)'
                elif state is 'out':                
                

                    if beam:
                        path = ' | '
                    else:
                        path = '---'
                elif state is 'block':
                    path = '[X]'
                    beam = False
                
                elif state is 'undefined':
                    if beam:
                        path = '?|?'
                    else:
                        path = '?-?'
                
                else:
                    path = '???'
                    


                
                
                if flux_expected is None or not beam:
                    flux_expected_str = ''
                else:
                    flux_expected_str = '{:11.3g}'.format(flux_expected)
                    flux_expected *= element.transmission(verbosity=0)


                
                
                if callable(getattr(element, 'reading', None)):
                    reading_str = '{:11.3g}'.format(element.reading(verbosity=0))
                    state = element.state()
                    if element.has_flux and (state=='in' or state=='block'):
                        flux_cur = element.flux(verbosity=0)
                        flux_expected = flux_cur
                        flux_str = '{:11.3g}'.format(flux_cur)
                    else:
                        flux_str = ''
                    
                else:
                    reading_str = ''
                    flux_str = ''
                    
            
                
                print('|{:5.1f} m | {:16.16} | {:s} | {:11.11} | {:11.11} | {:11.11} |'.format(element.zposition, element.name, path, reading_str, flux_str, flux_expected_str))
                
                
            #beam = True # For testing
                
                
        if verbosity>=1:
            print('+--------+------------------+-----+-------------+-------------+-------------+')

            
            


    # End class CMSBeam(object)
    ########################################
    


beam = CMSBeam()


class Beamline(object):
    '''Generic class that encapsulates different aspects of the beamline.
    The intention for this object is to have methods that activate various 'standard'
    protocols or sequences of actions.'''

    def __init__(self, **kwargs):
        
        self.md = {}
        self.current_mode = 'undefined'
        
        
    def mode(self, new_mode):
        '''Tells the instrument to switch into the requested mode. This may involve
        moving detectors, moving the sample, enabling/disabling detectors, and so
        on.'''
        
        getattr(self, 'mode'+new_mode)()
        
        
    def get_md(self, prefix=None, **md):
        '''Returns a dictionary of the current metadata.
        The 'prefix' argument is prepended to all the md keys, which allows the
        metadata to be grouped with other metadata in a clear way. (Especially,
        to make it explicit that this metadata came from the beamline.)'''
        
        # Update internal md
        #self.md['key'] = value

        md_return = self.md.copy()
    
        # Add md that may change
        md_return['mode'] = self.current_mode
    
        # Include the user-specified metadata
        md_return.update(md)

        # Add an optional prefix
        if prefix is not None:
            md_return = { '{:s}{:s}'.format(prefix, key) : value for key, value in md_return.items() }
    
        return md_return
            
        
    def comment(self, text, logbooks=None, tags=None, append_md=True, **md):
        
        text += '\n\n[comment for beamline: {}]'.format(self.__class__.__name__)
        
        if append_md:
        
            # Global md
            md_current = { k : v for k, v in RE.md.items() }
            
            # Beamline md
            md_current.update(self.get_md())
            
            # Specified md
            md_current.update(md)
            
            text += '\n\n\nMetadata\n----------------------------------------'
            for key, value in sorted(md_current.items()):
                text += '\n{}: {}'.format(key, value)
        
        logbook.log(text, logbooks=logbooks, tags=tags)
        
        
    def log_motors(self, motors, verbosity=3, **md):
      
        log_text = 'Motors\n----------------------------------------\nname | position | offset | direction |\n'
      
        for motor in motors:
            offset = float(caget(motor.prefix+'.OFF'))
            direction = int(caget(motor.prefix+'.DIR'))
            log_text += '{} | {} | {} | {} |\n'.format(motor.name, motor.user_readback.value, offset, direction)
      
      
        md_current = { k : v for k, v in RE.md.items() }
        md_current.update(md)
        log_text += '\nMetadata\n----------------------------------------\n'
        for k, v in sorted(md_current.items()):
            log_text += '{}: {}\n'.format(k, v)
            
        if verbosity>=3:
            print(log_text)
            
        self.comment(log_text)
            

                



class CMS_Beamline(Beamline):
    '''This object collects together various standard protocols and sequences
    of action used on the CMS (11-BM) beamline at NSLS-II.'''
    
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
        self.beam = beam
        #self.SAXS = CMS_SAXS_Detector(pilatus300)
        #self.WAXS = CMS_WAXS_Detector()
        self.SAXS = CMS_SAXS_Detector(pilatus_name)
        
        from epics import PV
        
        self._chamber_pressure_pv = PV('XF:11BMB-VA{Chm:Det-TCG:1}P-I')
        
        self.detector = [] 
        self.PLOT_Y = []
        self.TABLE_COLS = []
        self.bsx_pos = -15.74
        self.FM_donefiles = []
    
    
    def modeAlignment_bim6(self, verbosity=3):
        
        self.current_mode = 'undefined'
        
        # TODO: Check what mode (TSAXS, GISAXS) and respond accordingly
        # TODO: Check if gate valves are open and flux is okay (warn user)
        
        
        self.beam.off()
        #self.beam.setTransmission(1e-4)
        self.beam.setTransmission(5e-4)
        
        #mov( [DETx, DETy], [0, 0] )
        self.beam.bim6.insert()
        
        caput('XF:11BMB-BI{IM:2}EM180:Acquire', 1) # Turn on bim6
        detselect(bim6, suffix='')
        
        self.current_mode = 'alignment'
        
        self.beam.bim6.reading()

        
        
    def modeMeasurement_bim6(self, verbosity=3):
        
        self.current_mode = 'undefined'
        
        self.beam.off()
        self.beam.setTransmission(1)
        
        #mov(DETy, -16)
        self.beam.bim6.retract()
        
        caput('XF:11BMB-BI{IM:2}EM180:Acquire', 0) # Turn off bim6
        #detselect(pilatus300)
        detselect(pilatus_name)
        
        #if RE.state is not 'idle':
        #    RE.abort()
        
        self.current_mode = 'measurement'
        
        # Check if gate valves are open
        if self.beam.GVdsbig.state() is not 'out' and verbosity>=1:
            print('Warning: Sample chamber gate valve (large, downstream) is not open.')
            

    def modeAlignment(self, verbosity=3):
        
        self.current_mode = 'undefined'
        
        # TODO: Check what mode (TSAXS, GISAXS) and respond accordingly
        # TODO: Check if gate valves are open and flux is okay (warn user)
        # TODO: Check list: change attenuator for different energy, change the bsx position with beamcenter accordingly
        
        
        self.beam.off()
        self.beam.setTransmission(1e-8)  #1e-6 for 13.5kev, 1e-8 for 17kev
        while beam.transmission() > 3e-8:
            time.sleep(0.5)
            self.beam.setTransmission(1e-8)
            
        #mov(bsx, -10.95)
        bsx.move(self.bsx_pos+3)
            
        #detselect(pilatus300, suffix='_stats4_total')
        #caput('XF:11BMB-ES{Det:SAXS}:cam1:AcquireTime', 0.5)
        #caput('XF:11BMB-ES{Det:SAXS}:cam1:AcquirePeriod', 0.6)

        detselect(pilatus_name, suffix='_stats4_total')
        caput('XF:11BMB-ES{}:cam1:AcquireTime'.format(pilatus_Epicsname), 0.5)
        caput('XF:11BMB-ES{}:cam1:AcquirePeriod'.format(pilatus_Epicsname), 0.6)
        #caput('XF:11BMB-ES{Det:PIL2M}:cam1:AcquirePeriod', 0.6)
       
        #TODO: Update ROI based on current SAXSx, SAXSy and the md in cms object
        
        self.current_mode = 'alignment'
        
        #self.beam.bim6.reading()


    def modeMeasurement(self, verbosity=3):   
        
        self.current_mode = 'undefined'
        
        self.beam.off()
        
        #mov(bsx, -15.95)
        bsx.move(self.bsx_pos)

        if abs(bsx.user_readback.value - self.bsx_pos)>0.1:
            print('WARNING: Beamstop did not return to correct position!')
            return
        
        self.beam.setTransmission(1)
        
        #detselect(pilatus300)
        #detselect([pilatus300, psccd])
        detselect(pilatus_name)
        #detselect(psccd)
        
        #if RE.state is not 'idle':
        #    RE.abort()

       
        self.current_mode = 'measurement'
        
        # Check if gate valves are open
        if self.beam.GVdsbig.state() is not 'out' and verbosity>=1:
            print('Warning: Sample chamber gate valve (large, downstream) is not open.')
            


   
        
    def modeBeamstopAlignment(self, verbosity=3):
        '''Places bim6 (dsmon) as a temporary beamstop.'''
        
        DETy.move(-6.1)
        
        
        
    def beamstopCircular(self, verbosity=3):
        
        self.beam.setTransmission(1e-6)
        
        bsx.move(0)
        bsphi.move(-12.0)
        bsx.move(self.bsx_pos)
        bsy.move(-15.47)
        
        # TODO: Capture image and confirm that it's okay?
        if verbosity>=1:
            print("WARNING: This routine merely puts the beamstop in the ~approximately~ correct position. You must confirm that the beam is being blocked correctly.")
            
        self.beam.transmission(verbosity=verbosity)


    def beamstopLinear(self, verbosity=3):
        
        self.beam.setTransmission(1e-6)
        
        bsx.move(0)
        bsphi.move(-223.4)
        bsx.move(self.bsx_pos)
        bsy.move(17)
        
        # TODO: Capture image and confirm that it's okay?
        if verbosity>=1:
            print("WARNING: This routine merely puts the beamstop in the ~approximately~ correct position. You must confirm that the beam is being blocked correctly.")
            
        self.beam.transmission(verbosity=verbosity)
            
        
        
    def _actuate_open(self, pv, max_tries=5, wait_time=1.0, verbosity=2):
        
        tries = 1
        if verbosity>=4:
            print('  Opening {} (try # {:d})'.format(pv, tries))
        caput(pv+'Cmd:Opn-Cmd', 1)
        time.sleep(wait_time)
        
        
        while caget(pv+'Pos-Sts')!= 1 and tries<max_tries:
            tries += 1
            if verbosity>=4:
                print('  Opening {} (try # {:d})'.format(pv, tries))
            caput(pv+'Cmd:Opn-Cmd', 1)
            time.sleep(wait_time)
            
        if verbosity>=1 and caget(pv+'Pos-Sts')!= 1:
            print('ERROR, valve did not open ({})'.format(pv))

    def _actuate_close(self, pv, max_tries=5, wait_time=1.0, verbosity=2):
        
        tries = 1
        if verbosity>=4:
            print('  Closing {} (try # {:d})'.format(pv, tries))
        caput(pv+'Cmd:Cls-Cmd', 1)
        time.sleep(wait_time)
        
        
        while caget(pv+'Pos-Sts')!= 0 and tries<max_tries:
            tries += 1
            if verbosity>=4:
                print('  Closing {} (try # {:d})'.format(pv, tries))
            caput(pv+'Cmd:Cls-Cmd', 1)
            time.sleep(wait_time)
            
        if verbosity>=1 and caget(pv+'Pos-Sts')!= 0:
            print('ERROR, valve did not close ({})'.format(pv))
        
        
    def ventChamber(self, verbosity=3):
        
        #TODO: Remove the old (commented-out) caput lines
        
        # Close large gate valve (downstream side of sample chamber)
        #caput('XF:11BMB-VA{Chm:Det-GV:1}Cmd:Cls-Cmd',1)
        self._actuate_close('XF:11BMB-VA{Chm:Det-GV:1}', verbosity=verbosity)

        # Close small gate valve (upstream side of sample chamber)
        #caput('XF:11BMB-VA{Slt:4-GV:1}Cmd:Cls-Cmd',1)
        self._actuate_close('XF:11BMB-VA{Slt:4-GV:1}', verbosity=verbosity)

        # Close valve connecting sample chamber to vacuum pump
        #caput('XF:11BMB-VA{Chm:Det-IV:1}Cmd:Cls-Cmd',1)
        self._actuate_close('XF:11BMB-VA{Chm:Det-IV:1}', verbosity=verbosity)
        
        # Soft-open the upstream vent-valve
        #caput('XF:11BMB-VA{Chm:Smpl-VV:1}Cmd:Cls-Cmd', 1)
        self._actuate_close('XF:11BMB-VA{Chm:Smpl-VV:1}', verbosity=verbosity)
        time.sleep(1.0)
        #caput('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}Cmd:Opn-Cmd', 1)
        self._actuate_open('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}', verbosity=verbosity)
        # Soft-open the downstream vent-vale
        #caput('XF:11BMB-VA{Chm:Det-VV:1_Soft}Cmd:Cls-Cmd', 1)
        self._actuate_close('XF:11BMB-VA{Chm:Det-VV:1}', verbosity=verbosity)
        time.sleep(1.0)
        #caput('XF:11BMB-VA{Chm:Det-VV:1}Cmd:Opn-Cmd', 1)
        self._actuate_open('XF:11BMB-VA{Chm:Det-VV:1_Soft}', verbosity=verbosity)
  
  
        
        self.chamberPressure(range_high=100)
        
        # Fully open the upstream vent-vale
        #caput('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}Cmd:Cls-Cmd', 1)
        self._actuate_close('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}', verbosity=verbosity)
        time.sleep(1.0)
        #caput('XF:11BMB-VA{Chm:Smpl-VV:1}Cmd:Opn-Cmd', 1)
        self._actuate_open('XF:11BMB-VA{Chm:Smpl-VV:1}', verbosity=verbosity)

        # Fully open the downstream vent-vale
        #caput('XF:11BMB-VA{Chm:Det-VV:1_Soft}Cmd:Cls-Cmd', 1)
        self._actuate_close('XF:11BMB-VA{Chm:Det-VV:1_Soft}', verbosity=verbosity)
        time.sleep(1.0)
        #caput('XF:11BMB-VA{Chm:Det-VV:1}Cmd:Opn-Cmd', 1)
        self._actuate_open('XF:11BMB-VA{Chm:Det-VV:1}', verbosity=verbosity)
        
        self.chamberPressure(range_high=950)
        
        if verbosity>=1:
            print('Sample chamber is ready to be opened.')
        
            
        
    def _old_ventChamber(self, verbosity=3):
        # TODO: deprecate and delete
        
        
        # Close large gate valve (downstream side of sample chamber)
        caput('XF:11BMB-VA{Chm:Det-GV:1}Cmd:Cls-Cmd',1)

        # Close small gate valve (upstream side of sample chamber)
        #caput('XF:11BMB-VA{Slt:4-GV:1}Cmd:Cls-Cmd',1)

        # Close valve connecting sample chamber to vacuum pump
        caput('XF:11BMB-VA{Chm:Det-IV:1}Cmd:Cls-Cmd',1)
        
        time.sleep(0.5)
        
        # Soft-open the upstream vent-valve
        caput('XF:11BMB-VA{Chm:Smpl-VV:1}Cmd:Cls-Cmd', 1)
        time.sleep(1.0)
        caput('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}Cmd:Opn-Cmd', 1)
        
        
        
        self.chamberPressure(range_high=100)
        
        # Fully open the upstream vent-vale
        caput('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}Cmd:Cls-Cmd', 1)
        time.sleep(1.0)
        caput('XF:11BMB-VA{Chm:Smpl-VV:1}Cmd:Opn-Cmd', 1)

        # Fully open the downstream vent-vale
        caput('XF:11BMB-VA{Chm:Det-VV:1_Soft}Cmd:Cls-Cmd', 1)
        time.sleep(1.0)
        caput('XF:11BMB-VA{Chm:Det-VV:1}Cmd:Opn-Cmd', 1)
        
        self.chamberPressure(range_high=1000)
        
        if verbosity>=1:
            print('Sample chamber is ready to be opened.')
        
    
        
    def chamberPressure(self, range_low=None, range_high=None, readout_period=1.0, verbosity=3):
        '''Monitors the pressure in the sample chamber, printing the current value.
        If range arguments are provided, the monitoring will end once the pressure
        is outside the range.
        '''
        
        monitor = True
        while monitor:
            
            try:
            
                if range_low is not None and self._chamber_pressure_pv.get()<range_low:
                    monitor = False
                    
                if range_high is not None and self._chamber_pressure_pv.get()>range_high:
                    monitor = False

                P_mbar = self._chamber_pressure_pv.get()
                P_atm = P_mbar*0.000986923
                P_torr = P_mbar*0.750062
                P_kPa = P_mbar*0.1
                P_psi = 0.0145038
                
                if verbosity>=4:
                    print('Sample chamber pressure: {:8.2f} mbar = {:5.3f} atm = {:7.3f} torr = {:4.1g} kPa     \r'.format(P_mbar, P_atm, P_torr, P_kPa), end='', flush=True)
                elif verbosity>=2:
                    print('Sample chamber pressure: {:8.2f} mbar ({:5.3f} atm)    \r'.format(P_mbar, P_atm), end='', flush=True)
                    
                time.sleep(readout_period)
                
                
            except KeyboardInterrupt:
                monitor = False
                
        
    def pumpChamber(self, max_tries=8, verbosity=3):
        
        
        # Close vent-valves
        #caput('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}Cmd:Cls-Cmd', 1)
        #caput('XF:11BMB-VA{Chm:Smpl-VV:1}Cmd:Cls-Cmd', 1)
        #caput('XF:11BMB-VA{Chm:Det-VV:1_Soft}Cmd:Cls-Cmd', 1)
        #caput('XF:11BMB-VA{Chm:Det-VV:1}Cmd:Cls-Cmd', 1)
        self._actuate_close('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}', verbosity=verbosity)
        self._actuate_close('XF:11BMB-VA{Chm:Smpl-VV:1}', verbosity=verbosity)
        self._actuate_close('XF:11BMB-VA{Chm:Det-VV:1_Soft}', verbosity=verbosity)
        self._actuate_close('XF:11BMB-VA{Chm:Det-VV:1}', verbosity=verbosity)
        
        # Turn on pump (if necessary)
        tries = 1
        while caget('XF:11BMB-VA{Chm:Det-Pmp:1}Sts:Enbl-Sts')==0 and tries<=max_tries:
            caput('XF:11BMB-VA{Chm:Det-Pmp:1}Cmd:Enbl-Cmd', 0)
            time.sleep(0.2)
            caput('XF:11BMB-VA{Chm:Det-Pmp:1}Cmd:Enbl-Cmd', 1)
            time.sleep(2.0)
            tries += 1
        
        # Soft-open valve to pump
        #caput('XF:11BMB-VA{Chm:Det-IV:1}Cmd:Cls-Cmd', 1)
        self._actuate_close('XF:11BMB-VA{Chm:Det-IV:1}', verbosity=verbosity)
        time.sleep(0.5)
        #caput('XF:11BMB-VA{Chm:Det-IV:1_Soft}Cmd:Opn-Cmd', 1)
        self._actuate_open('XF:11BMB-VA{Chm:Det-IV:1_Soft}', verbosity=verbosity)
        
        time.sleep(5.0)
        # Check pump again
        tries = 1
        while caget('XF:11BMB-VA{Chm:Det-Pmp:1}Sts:Enbl-Sts')==0 and tries<=max_tries:
            caput('XF:11BMB-VA{Chm:Det-Pmp:1}Cmd:Enbl-Cmd', 0)
            time.sleep(0.2)
            caput('XF:11BMB-VA{Chm:Det-Pmp:1}Cmd:Enbl-Cmd', 1)
            time.sleep(2.0)
            tries += 1
        
        
        self.chamberPressure(range_low=500)

        # Fully open valve to pump
        #caput('XF:11BMB-VA{Chm:Det-IV:1_Soft}Cmd:Cls-Cmd', 1)
        self._actuate_close('XF:11BMB-VA{Chm:Det-IV:1_Soft}', verbosity=verbosity)
        time.sleep(0.5)
        #caput('XF:11BMB-VA{Chm:Det-IV:1}Cmd:Opn-Cmd', 1)
        self._actuate_open('XF:11BMB-VA{Chm:Det-IV:1}', verbosity=verbosity)
        
        self.chamberPressure(range_low=200)
                
        
    def _old_pumpChamber(self, readout_delay=0.2):
        # TODO: deprecate and delete
        
        
        # Close vent-valves
        caput('XF:11BMB-VA{Chm:Smpl-VV:1_Soft}Cmd:Cls-Cmd', 1)
        time.sleep(0.5)
        caput('XF:11BMB-VA{Chm:Smpl-VV:1}Cmd:Cls-Cmd', 1)
        time.sleep(0.5)
        caput('XF:11BMB-VA{Chm:Det-VV:1_Soft}Cmd:Cls-Cmd', 1)
        time.sleep(0.5)
        caput('XF:11BMB-VA{Chm:Det-VV:1}Cmd:Cls-Cmd', 1)
        time.sleep(0.2)
        
        # Turn on pump (if necessary)
        if caget('XF:11BMB-VA{Chm:Det-Pmp:1}Sts:Enbl-Sts')==0:
            caput('XF:11BMB-VA{Chm:Det-Pmp:1}Cmd:Enbl-Cmd', 0)
            time.sleep(0.2)
            caput('XF:11BMB-VA{Chm:Det-Pmp:1}Cmd:Enbl-Cmd', 1)
        
        # Soft-open valve to pump
        caput('XF:11BMB-VA{Chm:Det-IV:1}Cmd:Cls-Cmd', 1)
        time.sleep(1.0)
        caput('XF:11BMB-VA{Chm:Det-IV:1_Soft}Cmd:Opn-Cmd', 1)
        time.sleep(0.2)
        
        sleep(5.0)
        # Check pump again
        if caget('XF:11BMB-VA{Chm:Det-Pmp:1}Sts:Enbl-Sts')==0:
            caput('XF:11BMB-VA{Chm:Det-Pmp:1}Cmd:Enbl-Cmd', 0)
            time.sleep(0.2)
            caput('XF:11BMB-VA{Chm:Det-Pmp:1}Cmd:Enbl-Cmd', 1)
        
        
        self.chamberPressure(range_low=500)

        # Fully open valve to pump
        caput('XF:11BMB-VA{Chm:Det-IV:1_Soft}Cmd:Cls-Cmd', 1)
        time.sleep(1.0)
        caput('XF:11BMB-VA{Chm:Det-IV:1}Cmd:Opn-Cmd', 1)
        time.sleep(0.2)
        
        self.chamberPressure(range_low=200)
        
        
    def openChamberGateValve(self):
        
        caput('XF:11BMB-VA{Chm:Det-GV:1}Cmd:Opn-Cmd', 1) # Large (downstream)
        #caput('XF:11BMB-VA{Slt:4-GV:1}Cmd:Opn-Cmd',1) # Small (upstream)


    def closeChamberGateValve(self):
        
        caput('XF:11BMB-VA{Chm:Det-GV:1}Cmd:Cls-Cmd', 1) # Large (downstream)
        #caput('XF:11BMB-VA{Slt:4-GV:1}Cmd:Cls-Cmd',1) # Small (upstream)
        
        
    # Metatdata methods
    ########################################
    
    def get_md(self, prefix=None, **md):
        
        md_current = self.md.copy()
        md_current['calibration_energy_keV'] = round(self.beam.energy(verbosity=0), 3)
        md_current['calibration_wavelength_A'] = round(self.beam.wavelength(verbosity=0), 5)
        
        h, v = self.beam.size(verbosity=0)
        md_current['beam_size_x_mm'] = h
        md_current['beam_size_y_mm'] = v
        
        #temperarily block it for bad communication. 17:30, 071617
        #h, v = self.beam.divergence(verbosity=0)
        #md_current['beam_divergence_x_mrad'] = h
        #md_current['beam_divergence_y_mrad'] = v
        
        md_current['beamline_mode'] = self.current_mode
        
        #md_current['detector'] = self.detector
        
        md_current['motor_SAXSx'] = SAXSx.user_readback.value
        md_current['motor_SAXSy'] = SAXSy.user_readback.value
        md_current['motor_DETx'] = DETx.user_readback.value
        md_current['motor_DETy'] = DETy.user_readback.value
        md_current['motor_WAXSx'] = WAXSx.user_readback.value
        md_current['motor_smx'] = smx.user_readback.value
        md_current['motor_smy'] = smy.user_readback.value
        md_current['motor_sth'] = sth.user_readback.value

        md_current['motor_bsx'] = bsx.user_readback.value
        md_current['motor_bsy'] = bsy.user_readback.value
        md_current['motor_bsphi'] = bsphi.user_readback.value
        
        md_current.update(self.SAXS.get_md(prefix='detector_SAXS_'))
        
        md_current.update(md)
        
        # Add an optional prefix
        if prefix is not None:
            md_current = { '{:s}{:s}'.format(prefix, key) : value for key, value in md_current.items() }
        
        return md_current
    

    def setMetadata(self, verbosity=3):
        '''Guides the user through setting some of the required and recommended
        meta-data fields.'''
        
        if verbosity>=3:
            print('This will guide you through adding some meta-data for the upcoming experiment.')
        if verbosity>=4:
            print('You can accept default values (shown in square [] brackets) by pressing enter. You can leave a value blank (or put a space) to skip that entry.')


        # Set some values automatically
        month = int(time.strftime('%m'))
        if month<=4:
            cycle = 1
        elif month<=8:
            cycle = 2
        else:
            cycle = 3    
        RE.md['experiment_cycle'] = '{:s}_{:d}'.format( time.strftime('%Y'), cycle )
        
        RE.md['calibration_energy_keV'] = round(self.beam.energy(verbosity=0), 3)
        RE.md['calibration_wavelength_A'] = round(self.beam.wavelength(verbosity=0), 5)
        
        # TODO:
        # RE.md['calibration_detector_distance_m'] =
        # RE.md['calibration_detector_x0'] =
        # RE.md['calibration_detector_y0'] = 
        
            
        
        # Ask the user some questions
        
        questions = [
            ['experiment_proposal_number', 'Proposal number'] ,
            ['experiment_SAF_number', 'SAF number'] ,
            ['experiment_group', 'User group (e.g. PI)'] ,
            ['experiment_user', 'The specific user/person running the experiment'] ,
            ['experiment_project', 'Project name/code'] ,
            ['experiment_alias_directory', 'Alias directory'] ,
            ['experiment_type', 'Type of experiments/measurements (SAXS, GIWAXS, etc.)'] ,
            ]
        
        
        # TBD:
        # Path where data will be stored?

        self._dialog_total_questions = len(questions)
        self._dialog_question_number = 1
        
        for key, text in questions:
            try:
                self._ask_question(key, text)
            except KeyboardInterrupt:
                return
            
        if verbosity>=4:
            print('You can also add/edit metadata directly using the RE.md object.')
        
        

    def _ask_question(self, key, text, default=None):

        if default is None and key in RE.md:
                default = RE.md[key]
        
        if default is None:
            ret = input('  Q{:d}/{:d}. {:s}: '.format(self._dialog_question_number, self._dialog_total_questions, text) )
        
        else:
            ret = input('  Q{:d}/{:d}. {:s} [{}]: '.format(self._dialog_question_number, self._dialog_total_questions, text, default) )
            if ret=='':
                ret = default
                
            
        if ret!='' and ret!=' ':
            RE.md[key] = ret
            
        self._dialog_question_number += 1
            
        
    # Logging methods
    ########################################
        
    def logAllMotors(self, verbosity=3, **md):
        log_pos()
        
        motor_list = [
                    mono_bragg ,
                    mono_pitch2 ,
                    mono_roll2 ,
                    mono_perp2 ,
                    mir_usx ,
                    mir_dsx ,
                    mir_usy ,
                    mir_dsyi ,
                    mir_dsyo ,
                    mir_bend ,
                    s0.tp ,
                    s0.bt ,
                    s0.ob ,
                    s0.ib ,
                    s1.xc ,
                    s1.xg ,
                    s1.yc ,
                    s1.yg ,
                    s2.xc ,
                    s2.xg ,
                    s2.yc ,
                    s2.yg ,
                    s3.xc ,
                    s3.xg ,
                    s3.yc ,
                    s3.yg ,
                    s4.xc ,
                    s4.xg ,
                    s4.yc ,
                    s4.yg ,
                    s5.xc ,
                    s5.xg ,
                    s5.yc ,
                    s5.yg ,
                    bim3y ,
                    fs3y ,
                    bim4y ,
                    bim5y ,
                    smx ,
                    smy ,
                    sth ,
                    schi ,
                    sphi ,
                    srot ,
                    strans ,
                    camx ,
                    camy ,
                    cam2x ,
                    cam2z ,
                    DETx ,
                    DETy ,
                    WAXSx ,
                    SAXSx ,
                    SAXSy ,
                    bsx , 
                    bsy ,
                    bsphi ,
                    armz ,
                    armx ,
                    armphi ,
                    army ,
                    armr ,
                    ]
        
        self.log_motors(motor_list, verbosity=verbosity, **md)
        
       
    # End class CMS_Beamline(Beamline)
    ########################################
        

class CMS_Beamline_GISAXS(CMS_Beamline):
    
    
    def modeAlignment(self, verbosity=3):
        
        if RE.state!='idle':
            RE.abort()
        
        self.current_mode = 'undefined'
        
        # TODO: Check what mode (TSAXS, GISAXS) and respond accordingly
        # TODO: Check if gate valves are open and flux is okay (warn user)
        
        
        self.beam.off()
        self.beam.setTransmission(1e-6)
        while beam.transmission() > 2e-6:
            time.sleep(0.5)
            self.beam.setTransmission(1e-6)
            
        #mov(bsx, -11.55)
        #mov(bsx, -11.55+2) # changed at 06/02/17, Osuji beam time
        #mov(bsx, -14.73+2) # changed at 06/04/17, SAXS, 3m, Osuji beam time
        #mov(bsx, -15.23+2) # changed at 06/04/17, GISAXS, 3m, Osuji beam time
        #mov(bsx, -17.03+3) # changed at 06/04/17, GISAXS, 3m, Osuji beam time
        #mov(bsx, -16.0+3) #change it at 07/10/17, GISAXS, 2m, LSita Beam time
        #mov(bsx, -16.53+3) # 07/20/17, GISAXS, 5m, CRoss
        #mov(bsx, self.bsx_pos+3)
        
        bsx.move(self.bsx_pos+3)
        
        self.setReflectedBeamROI()
        self.setDirectBeamROI()

        #detselect(pilatus300, suffix='_stats4_total')
        #caput('XF:11BMB-ES{Det:SAXS}:cam1:AcquireTime', 0.5)
        #caput('XF:11BMB-ES{Det:SAXS}:cam1:AcquirePeriod', 0.6)
        
        detselect(pilatus_name, suffix='_stats4_total')
        caput('XF:11BMB-ES{}:cam1:AcquireTime'.format(pilatus_Epicsname), 0.5)
        caput('XF:11BMB-ES{}:cam1:AcquirePeriod'.format(pilatus_Epicsname), 0.6)

        #TODO: Update ROI based on current SAXSx, SAXSy and the md in cms object
        
        self.current_mode = 'alignment'
        
        #self.beam.bim6.reading()


    def modeMeasurement(self, verbosity=3):   

        if RE.state!='idle':
            RE.abort()
        
        self.current_mode = 'undefined'
        
        self.beam.off()
        
        #bsx_pos=-16.74
        #mov(bsx, -16.55)
        #mov(bsx, -13.83) #change it at 06/02/17, Osuji Beam time
        #mov(bsx, -14.73) #change it at 06/04/17, SAXS, 3m, Osuji Beam time
        #mov(bsx, -15.03) #change it at 06/04/17, GISAXS, 3m, Osuji Beam time
        #mov(bsx, -16.43) #change it at 06/12/17, GISAXS, 3m, LZhu Beam time
        #mov(bsx, -16.53) #change it at 06/19/17, GISAXS, 5m, AHexemer Beam time
        #mov(bsx, -16.2) #change it at 07/07/17, GISAXS, 3m, TKoga Beam time
        #mov(bsx, -16.43) #change it at 07/10/17, GISAXS, 2m, LSita Beam time
        #mov(bsx, -16.53) # 07/20/17, GISAXS, 5m, CRoss Beam time
        #mov(bsx, -15.84) # 07/26/17, SAXS/WAXS, 2m, BVogt Beam time
        #mov(bsx, -16.34) # 08/02/17, TOMO GISAXS, 5m, LRichter Beam time
        #mov(bsx, -16.74) # 08/02/17, TOMO GISAXS, 5m, LRichter Beam time
        #mov(bsx, self.bsx_pos)
        
        bsx.move(self.bsx_pos)

        #if abs(bsx.user_readback.value - -16.74)>0.1:
        if abs(bsx.user_readback.value - self.bsx_pos)>0.1:
            print('WARNING: Beamstop did not return to correct position!')
            return
        
        self.beam.setTransmission(1)
        
        
        #mov(DETy, -16)
        #self.beam.bim6.retract()

        
        #caput('XF:11BMB-BI{IM:2}EM180:Acquire', 0) # Turn off bim6
        #detselect(pilatus300)
        #detselect([pilatus300, psccd]) 
        detselect(pilatus_name)
        #detselect(psccd)
        
        
        self.current_mode = 'measurement'
        
        # Check if gate valves are open
        if self.beam.GVdsbig.state() is not 'out' and verbosity>=1:
            print('Warning: Sample chamber gate valve (large, downstream) is not open.')
        
        
    def setDirectBeamROI(self, size=[10,4], verbosity=3):
        '''Update the ROI (stats4) for the direct beam on the Pilatus
        detector. This (should) update correctly based on the current SAXSx, SAXSy.
        
        The size argument controls the size (in pixels) of the ROI itself
        (in the format [width, height]). A size=[6,4] is reasonable.
        The size is changed to [10, 4] for possible beam drift during a user run (changed at 08/16/17)'''
        
        detector = self.SAXS

        # These positions are updated based on current detector position
        det_md = detector.get_md()
        x0 = det_md['detector_SAXS_x0_pix']
        y0 = det_md['detector_SAXS_y0_pix']
        
        #caput('XF:11BMB-ES{Det:SAXS}:ROI4:MinX', int(x0-size[0]/2))
        #caput('XF:11BMB-ES{Det:SAXS}:ROI4:SizeX', int(size[0]))
        #caput('XF:11BMB-ES{Det:SAXS}:ROI4:MinY', int(y0-size[1]/2))
        #caput('XF:11BMB-ES{Det:SAXS}:ROI4:SizeY', int(size[1]))
        
        #detselect(pilatus300, suffix='_stats4_total')

        caput('XF:11BMB-ES{}:ROI4:MinX'.format(pilatus_Epicsname), int(x0-size[0]/2))
        caput('XF:11BMB-ES{}:ROI4:SizeX'.format(pilatus_Epicsname), int(size[0]))
        caput('XF:11BMB-ES{}:ROI4:MinY'.format(pilatus_Epicsname), int(y0-size[1]/2))
        caput('XF:11BMB-ES{}:ROI4:SizeY'.format(pilatus_Epicsname), int(size[1]))
        
        detselect(pilatus_name, suffix='_stats4_total')        
        
    def setReflectedBeamROI(self, total_angle=0.16, size=[10,2], verbosity=3):
        '''Update the ROI (stats3) for the reflected beam on the Pilatus300k
        detector. This (should) update correctly based on the current SAXSx, SAXSy.
        
        The size argument controls the size (in pixels) of the ROI itself
        (in the format [width, height]). A size=[6,2] is reasonable.'''
        
        detector = self.SAXS

        # These positions are updated based on current detector position
        det_md = detector.get_md()
        x0 = det_md['detector_SAXS_x0_pix']
        y0 = det_md['detector_SAXS_y0_pix']
        
        d = detector.distance*1000.0 # mm
        pixel_size = detector.pixel_size # mm
        
        y_offset_mm = np.tan(np.radians(total_angle))*d
        y_offset_pix = y_offset_mm/pixel_size
        
        #for pilatus300k
        #y_pos = int( y0 - size[1]/2 - y_offset_pix )
        
        #for pilatus2M, placed up-side down
        y_pos = int( y0 - size[1]/2 + y_offset_pix )
        
        #caput('XF:11BMB-ES{Det:SAXS}:ROI3:MinX', int(x0-size[0]/2))
        #caput('XF:11BMB-ES{Det:SAXS}:ROI3:SizeX', int(size[0]))
        #caput('XF:11BMB-ES{Det:SAXS}:ROI3:MinY', y_pos)
        #caput('XF:11BMB-ES{Det:SAXS}:ROI3:SizeY', int(size[1]))
        
        #detselect(pilatus300, suffix='_stats3_total')
            
        caput('XF:11BMB-ES{}:ROI3:MinX'.format(pilatus_Epicsname), int(x0-size[0]/2))
        caput('XF:11BMB-ES{}:ROI3:SizeX'.format(pilatus_Epicsname), int(size[0]))
        caput('XF:11BMB-ES{}:ROI3:MinY'.format(pilatus_Epicsname), y_pos)
        caput('XF:11BMB-ES{}:ROI3:SizeY'.format(pilatus_Epicsname), int(size[1]))
        
        detselect(pilatus_name, suffix='_stats3_total')

    def setSpecularReflectivityROI(self, total_angle=0.16, size=[10,10], default_SAXSy=None, verbosity=3):
        '''Update the ROIs (stats1, stats2) for the specular reflected beam on the Pilatus
        detector. This (should) update correctly based on the current SAXSx, SAXSy.
        
        The size argument controls the size (in pixels) of the ROI itself
        (in the format [width, height]). 
        
        stats1 is centered on the specular reflected beam and has the size specified in 
        the size argument.
        
        stats2 is centered on the specular reflected beam and has the size that is twice
        as wide as specified in the size argument, for capturing background.
        
        The background-subtracted intensity for specular reflection is equal to: 
        2 * stats1 - stats2 
        '''
         
        detector = self.SAXS
        
        if default_SAXSy is not None: 
            if abs(default_SAXSy - SAXSy.position) > 0.01: 
                SAXSy.move(default_SAXSy)
                print('SAXS detector has been shifted to default SAXSy = {:.3f} mm.'.format(SAXSy.position)) 
        
        # These positions are updated based on current detector position
        det_md = detector.get_md()
        x0 = det_md['detector_SAXS_x0_pix']
        y0 = det_md['detector_SAXS_y0_pix']
        
        d = detector.distance*1000.0 # mm
        pixel_size = detector.pixel_size # mm
        
        y_offset_mm = np.tan(np.radians(total_angle))*d
        y_offset_pix = y_offset_mm/pixel_size
        
        #for pilatus300k
        #y_pos = int( y0 - size[1]/2 - y_offset_pix )
        
        #for pilatus2M, placed up-side down
        y_pos = int( y0 - size[1]/2 + y_offset_pix )

        #y pixels for intermodule gaps, for pilatus2M (195 pixels high module, 17 pixels high gap)
        y_gap_2M = []
        for i in np.arange(7): 
            for j in np.arange(17): 
                y_gap_2M.append((195+17)*(i+1)-17+j)
         
        #y pixels for Spectular Reflectivity ROI
        y_roi = []
        for i in np.arange(int(size[1]+1)):
            y_roi.append(y_pos+i)
         
        #flag for whether the ROI falls on intermodule gap 
        flag_ROIonGap = len(np.unique(y_gap_2M + y_roi)) < (len(y_gap_2M)+len(y_roi)) 
         
        #Move SAXSy if ROI falls on intermodule gap; if not, move on 
        if flag_ROIonGap == True: 
            y_shift = 17+size[1]+1	# intermodule gap is 17 pixels high 
            y_shift_mm = pixel_size*y_shift # mm
            SAXSy.move(SAXSy.position+y_shift_mm) 
            print('SAXS detector has been shifted to SAXSy = {:.3f} mm (by {:.3f} mm or {} pixels) to avoid a gap.'.format(SAXSy.position,y_shift_mm,y_shift)) 
         
            # These positions are updated based on current detector position
            det_md = detector.get_md()
            x0 = det_md['detector_SAXS_x0_pix']
            y0 = det_md['detector_SAXS_y0_pix']
           
            #for pilatus2M, placed up-side down
            y_pos = int( y0 - size[1]/2 + y_offset_pix )
        
        #caput('XF:11BMB-ES{Det:SAXS}:ROI3:MinX', int(x0-size[0]/2))
        #caput('XF:11BMB-ES{Det:SAXS}:ROI3:SizeX', int(size[0]))
        #caput('XF:11BMB-ES{Det:SAXS}:ROI3:MinY', y_pos)
        #caput('XF:11BMB-ES{Det:SAXS}:ROI3:SizeY', int(size[1]))
        
        #detselect(pilatus300, suffix='_stats3_total')
            
        # ROI1: Raw signal 
        caput('XF:11BMB-ES{}:ROI1:MinX'.format(pilatus_Epicsname), int(x0-size[0]/2))
        caput('XF:11BMB-ES{}:ROI1:SizeX'.format(pilatus_Epicsname), int(size[0]))
        caput('XF:11BMB-ES{}:ROI1:MinY'.format(pilatus_Epicsname), y_pos)
        caput('XF:11BMB-ES{}:ROI1:SizeY'.format(pilatus_Epicsname), int(size[1]))
        
        # ROI2: Raw signal+background (same as ROI1 for y, but twice as large for x) 
        caput('XF:11BMB-ES{}:ROI2:MinX'.format(pilatus_Epicsname), int(x0-size[0]))
        caput('XF:11BMB-ES{}:ROI2:SizeX'.format(pilatus_Epicsname), int(2*size[0]))
        caput('XF:11BMB-ES{}:ROI2:MinY'.format(pilatus_Epicsname), y_pos)
        caput('XF:11BMB-ES{}:ROI2:SizeY'.format(pilatus_Epicsname), int(size[1]))
        
        detselect(pilatus_name, suffix='_stats1_total')
    
    
    def out_of_beamstop(self, total_angle, size=[12,12], default_SAXSy=None):

        detector = self.SAXS
        
        #if default_SAXSy is not None: 
            #if abs(default_SAXSy - SAXSy.position) > 0.01: 
                #SAXSy.move(default_SAXSy)
                #print('SAXS detector has been shifted to default SAXSy = {:.3f} mm.'.format(SAXSy.position)) 
        
        # These positions are updated based on current detector position
        #det_md = detector.get_md()
        #y0 = det_md['detector_SAXS_y0_pix']
        
        #y_shift_mm = SAXSy.position - detector.detector_position[1]
        #y_shift_pixel = y_shift_mm/pixel_size
        
        d = detector.distance*1000.0 # mm
        pixel_size = detector.pixel_size # mm
        
        y_offset_mm = np.tan(np.radians(total_angle))*d
        y_offset_pix = y_offset_mm/pixel_size

        ##for pilatus2M, placed up-side down
        #y_pos = int( y0 - size[1]/2 + y_offset_pix )

        #y pixels for the size of circle beamstop, for pilatus2M (radius 27~28 pixels)
        y_beamstop = 15
                
        #ROI_ymin = caget('XF:11BMB-ES{}:ROI1:MinY'.format(pilatus_Epicsname))
        
        #return abs(y0 - y_shift_pixel - ROI_ymin) > y_beamstop

        return y_offset_pix  - size[1]/2 > y_beamstop
    
#cms = CMS_Beamline()
cms = CMS_Beamline_GISAXS()

def get_beamline():
    return cms


