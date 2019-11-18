print(f'Loading {__file__}')

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
    
            
                        
class SMI_SAXS_Detector(BeamlineDetector):
    def setCalibration(self):
        self.pixel_size = 0.172
        self.direct_beam_0_0 = [0, 0]
        self.distance =  pil1m_pos.z.position
        self.beamstop = [pil1m_bs.x.position, pil1m_bs.y.position]
        self.detector_position = [pil1m_pos.x.position, pil1m_pos.y.position]
        self.direct_beam = [np.round((self.direct_beam_0_0[0] - self.detector_position[0]) / self.pixel_size), np.round((self.direct_beam_0_0[1] - self.detector_position[1]) / self.pixel_size)]
        print(self.pixel_size)
    
    def get_md(self, prefix='detector_SAXS_', **md):
        
        md_return = self.md.copy()    
        x0, y0 = self.direct_beam
        
        #Read the detector position
        position_defined_x, position_defined_y = self.detector_position
        position_current_x, position_current_y = SAXS.x.user_readback.value, SAXS.y.user_readback.value
        
            
        md_return['name'] = self.detector.name

        md_return['x0_pix'] = round( x0 + (position_current_x-position_defined_x)/self.pixel_size , 2 )
        md_return['y0_pix'] = round( y0 + (position_current_y-position_defined_y)/self.pixel_size , 2 )
        md_return['distance_m'] = self.distance
               
        for roi in [roi1, roi2, roi3, roi4]:
            ROI = yield from bps.mv(pil1M)
            md_return['ROI{}_X_min'.format(i)]  = ROI['pil1M_{}_min_xyz_min_x'.format(roi)]['value']
            md_return['ROI{}_X_size'.format(i)] = ROI['pil1M_{}_size_x'.format(roi)]['value']
            md_return['ROI{}_Y_min'.format(i)]  = ROI['pil1M_{}_min_xyz_min_y'.format(roi)]['value']
            md_return['ROI{}_Y_size'.format(i)] = ROI['pil1M_{}_size_y'.format(roi)]['value']
        
        # Include the user-specified metadata
        md_return.update(md)

        # Add an optional prefix
        if prefix is not None:
            md_return = { '{:s}{:s}'.format(prefix, key) : value for key, value in md_return.items() }
    
        return md_return
      

class SMIBeam(object):
    """
    This class represents the 'beam' at the beamline. This collects together aspects
    of querying or changing beam properties, including the energy (or wavelength), 
    the beam intensity (or measuring flux), and so forth.
    """
    
    def __init__(self):
        
        self._SHUTTER_CLOSED_VOLTAGE = 7
        self.hc_over_e = 1.23984197e-6  #eV*m
        self.D_Si111 = 3.1293           # Angstroms
   
        self.dcm = Energy(prefix='', name='energy', read_attrs=['energy', 'ivugap', 'bragg'], configuration_attrs=['enableivu', 'enabledcmgap','target_harmonic'])                  
           

    def energyState(self):        
        self.dcm = Energy(prefix='', name='energy', read_attrs=['energy', 'ivugap', 'bragg'], configuration_attrs=['enableivu', 'enabledcmgap','target_harmonic'])
        print('The current energy is {:.1f} keV deg'.format(self.dcm.energy.position))


    def setEnergy(self, energy_eV, verbosity=3):
        """
        Set the x-ray beam to the specified energy (by changing the monochromator angle.
        """
        print('energy will move to {:.5f} keV deg'. format(energy_eV))
        response = input('    Are you sure? (y/[n]) ')
        
        if response is 'y' or response is 'Y':
            print('energy moved from {:.4f} deg to {:.4f} deg'.format(self.energy.energy, energy_eV))
            energy.move(energy_eV)

        else:
            print('No move was made.')  
            
            
    def _foilState(self, box=1, verbosity=3): 
        current_state = []
        for foil_num in [att1_1, att1_2, att1_3, att1_4, att1_5, att1_6, att1_7, att1_8, att1_9, att1_10, att1_11, att1_12,
                         att2_1, att2_2, att2_3, att2_4, att2_5, att2_6, att2_7, att2_8, att2_9, att2_10, att2_11, att2_12]:
            foil = yield from bps.read(foil_num)
            if foil['{}_status'.format(foil_num.name)]['value'] == 'Open':
                current_state.append(foil_num)     
        return current_state    
            
            
    def _determineFoils(self):
        print(self.dcm.bragg.position)
        
        #state = 'vac' if float(waxs_pressure.ch1_read.value) < 0.1 else 'air'
        divergence = crl_state()
        
        if self.dcm.energy.position < 2000:
            target_state = [att1_12]
        elif 2000 < self.dcm.energy.position < 2300:
            target_state = [att2_10]
        elif 2300 < self.dcm.energy.position < 3000:
            target_state = [att2_12, att2_11, att2_10]
        elif 3000 < self.dcm.energy.position < 4500:
            target_state = [att2_9, att2_10, att2_11,att2_12]
        elif 4500 < self.dcm.energy.position < 5500:
            target_state = [att2_5, att2_6, att2_12]
        elif 5500 < self.dcm.energy.position < 7000:
            target_state = [att1_12]
        elif 7000 < self.dcm.energy.position < 7500:
            target_state = [att2_8]
        elif 7500 < self.dcm.energy.position < 8400:
            target_state = [att2_1, att2_3]    
        elif 8400 < self.dcm.energy.position < 8800:
            target_state = [att2_2, att2_3]  
        elif 8800 < self.dcm.energy.position < 9700:
            target_state = [att2_1, att2_2, att2_3]  
        elif 9700 < self.dcm.energy.position < 10500:
            target_state = [att2_4]    
        elif 10500 < self.dcm.energy.position < 11000:
            target_state = [att2_1, att2_4]
        elif 11000 < self.dcm.energy.position < 11500:
            target_state = [att1_10, att1_11]         
        elif 11500 < self.dcm.energy.position < 13000:
            target_state = [att1_9, att1_10, att1_11]
        elif 13000 < self.dcm.energy.position < 14000:
            target_state = [att1_10, att1_12]
        elif 14000 < self.dcm.energy.position < 14700:
            target_state = [att1_6, att1_7]
        elif 14700 < self.dcm.energy.position < 16100:
            target_state = [att1_5, att1_6, att1_7]
            #if divergence == 'low_div' and state == 'vac': target_state = [att1_5, att1_6, att1_7] 
            #if divergence == 'mic_foc' and state == 'air': target_state = [att1_7]
            #if divergence == 'mic_foc' and state == 'vac': target_state = [att1_7]
            #target_state = [att1_5, att1_6]
        elif 16100 < self.dcm.energy.position < 17500:
            target_state = [att1_8]
        elif 17500 < self.dcm.energy.position < 18500:
            target_state = [att1_1, att1_3]
        elif 18500 < self.dcm.energy.position < 20000:
            target_state = [att1_2, att1_3]
        elif 20000 < self.dcm.energy.position < 23000:
            target_state = [att1_1, att1_2, att1_3]
        return target_state   
        
    def insertFoils(self, num_foils, box=1, wait_time=0.2, verbosity=3):
        # TODO: Generalize this function to handle all foils
        
        if num_foils == 'Measurement':
            target_state = []
        else:
            target_state = self._determineFoils()
        
        current_state = yield from self._foilState()
            
        # First insert foils
        #  swith False to True
        for foil in target_state:
            if foil not in current_state:
                yield from self._actuateFoil(foil, 'Insert', verbosity=verbosity)
                
        # Then remove foils not needed
        #  switch True to False
        for foil in current_state:
            if foil not in target_state:
                yield from self._actuateFoil(foil, 'Retract', verbosity=verbosity)
                
        # Double check that it worked
        current_state = yield from self._foilState(box=box, verbosity=verbosity)
        if current_state != target_state:
            if verbosity>=1:
                print('WARNING: Foils did not actuate correctly')
                print('current state: {}'.format(current_state))
                print('target state: {}'.format(target_state))
                
                
    def _actuateFoil(self, foil, state, wait_time=1.0, max_retries=10, verbosity=3):
        if verbosity>=4:
            print('    {} box,foil = ({}), PV={}'.format(state, foil))
        itry = 0
        foil_st = yield from bps.read(foil)
                
        while itry < max_retries and ((foil_st['{}_status'.format(foil.name)]['value'] == 'Not Open' and state == 'Insert') or (foil_st['{}_status'.format(foil.name)]['value'] == 'Open' and state == 'Retract')):
            yield from bps.mv(foil, state)
            foil_st = yield from bps.read(foil)
            itry += 1
            time.sleep(wait_time)
        


    # End class SMIBeam(object)
    ########################################
    


beam = SMIBeam()


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
            

    def detselect(self, detector_object, roi=None, suffix='_stats1_total'):
        """Switch the active detector and set some internal state"""
        
        roi_lookups = [ [1, pil1mroi1], [2, pil1mroi2], [3, pil1mroi3], [4, pil1mroi4] ]

        if isinstance(detector_object, (list, tuple)):
            self.detector = detector_object
        else:
            self.detector = [detector_object]
            
        if roi is None:
            self.PLOT_Y = self.detector[0].name + suffix
        else:
            self.PLOT_Y = 'pil1mroi{}'.format(roi)
            
            for check_name, det in roi_lookups:
                if roi==check_name:
                    self.detector.append(det)
            
        self.TABLE_COLS = [self.PLOT_Y]

        return self.detector



class SMI_Beamline(Beamline):

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.SAXS = SMI_SAXS_Det().getPositions()


    def modeAlignment_gisaxs(self):
        '''
        Set the beamline for alignement: move the beamstop out and
        insert the attenuators
        '''
        
        # TODO: Check if the beam is on
        '''
        #Check if the beam is on
        if RE.state!='idle':
            RE.abort()
        '''
        
        # Put in attenuators
        yield from SMIBeam().insertFoils('Alignement')
        
        # Move beamstop
        yield from bps.mv(pil1m_bs.x, bsx_pos + 5)
        
        self.setReflectedBeamROI()
        self.setDirectBeamROI()
        
        #Move the waxs detector out of the way
        if waxs.arc.position < 8:
            yield from bps.mv(waxs.arc, 8)
        
        #self.detselect(self.SAXS.detector, roi=4)
        #self.SAXS.detector.cam.acquire_time.set(0.5)
        #self.SAXS.detector.cam.acquire_period.set(0.6)
        
        #self.SAXS.detector.cam.file_name.set('align')
        #self.SAXS.detector.cam.file_number.set(1)
        
        #self.current_mode = 'alignment'

    def modeMeasurement_gisaxs(self, verbosity=3):
        '''
        Set the beamline for measurments: bring the beamstop in and
        remove the attenuator
        '''
        
        # TODO: Check if the beam is on
        '''
        #Check if the beam is on
        if RE.state!='idle':
            RE.abort()
        '''
        
        #self.current_mode = 'undefined'
        #self.beam.off()
        
        # Move beamstop
        yield from bps.mv(pil1m_bs.x, bsx_pos) #2 for 4000 mm, 1.2 for 6500
        
        # Remove attenuators
        yield from SMIBeam().insertFoils('Measurement')
        
        #self.detselect(self.detectors_measure)
        
        #self.current_mode = 'measurement'


    def setDirectBeamROI(self, size=[48,12], verbosity=3):
        '''
        Update the ROI (pil1m.roi1) for the direct beam on the SAXS detector.
        size: tuple argument: size in pixels) of the ROI [width, height]).
        '''
        
        # These positions are updated based on current detector position
        x0 = self.SAXS.direct_beam[0]
        y0 = self.SAXS.direct_beam[1]
        
        # Define the direct beam ROI on the pilatus 1M detector  
        yield from bps.mv(pil1M.roi1.min_xyz.min_x, int(x0-size[0]/2))
        yield from bps.mv(pil1M.roi1.size.x, int(size[0]))
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, int(y0-size[1]/2))
        yield from bps.mv(pil1M.roi1.size.y, int(size[1]))
        

    def setReflectedBeamROI(self, total_angle=0.16, size=[48,8], verbosity=3):
        '''
        Update the ROI (pil1m.roi3) for the reflected beam on the SAXS detector.
        total_ange: float: incident angle of the alignement in degrees
        size: tuple: size in pixels) of the ROI [width, height]
        '''
        
        # These positions are updated based on current detector position
        x0 = self.SAXS.direct_beam[0]
        y0 = self.SAXS.direct_beam[1]
        d = self.SAXS.distance   #mm
        pixel_size = self.SAXS.pixel_size # mm

        # Calculate the y position of the reflected beam        
        y_offset_mm = np.tan(np.radians(2*total_angle))*d
        y_offset_pix = y_offset_mm/pixel_size
        y_pos = int( y0 - size[1]/2 - y_offset_pix )

        # Define the reflected beam ROI on the pilatus 1M detector  
        yield from bps.mv(pil1M.roi1.min_xyz.min_x, int(x0-size[0]/2))
        yield from bps.mv(pil1M.roi1.size.x, int(size[0]))
        yield from bps.mv(pil1M.roi1.min_xyz.min_y, int(y_pos))
        yield from bps.mv(pil1M.roi1.size.y, int(size[1]))
        

    # End class SMI_Beamline(Beamline)
    ########################################



class SMI_SAXS_Det(object):

    def __init__(self, **md):
        #Metadata
        self.md = md
        
        #reference position for the 1M detector
        self.detector_name = 'Pilatus 1M'
        self.detector_position_0_0 = [-15, -40]
        self.direct_beam_0_0 = [402, 1043 - 358]
                
        self.pixel_size = 0.172
        self.energy = dcm.energy.position
    
    
    def getPositions(self, **md):
        self.distance =  pil1m_pos.z.position
        self.beamstop = [pil1m_bs.x.position, pil1m_bs.y.position]
        self.detector_position = [pil1m_pos.x.position, pil1m_pos.y.position]
        
        delta_pos_x = -self.detector_position[0] + self.detector_position_0_0[0]
        delta_pos_y = -self.detector_position[1] + self.detector_position_0_0[1]
        
        self.direct_beam = [np.round(self.direct_beam_0_0[0] - (delta_pos_x / self.pixel_size)), np.round(self.direct_beam_0_0[1] - (delta_pos_y / self.pixel_size))]
        return self


pilatus1M = SMI_SAXS_Det()

#smi = SMI_Beamline()


def get_beamline():
    return smi


