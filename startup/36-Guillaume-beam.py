print(f'Loading {__file__}')
from ophyd import (Signal, Component, Device, EpicsSignal, EpicsSignalRO, EpicsMotor)

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
                
        if self.dcm.energy.position < 2000:
            target_state = [att1_12]
        elif 2000 < self.dcm.energy.position < 2300:
            target_state = [att2_10]
        elif 2300 < self.dcm.energy.position < 3000:
            target_state = [att2_12, att2_11, att2_10]
        elif 3200 < self.dcm.energy.position < 3600:
            #Values updated March 10 2020
            target_state = [att2_5, att2_9]
        elif 3600 < self.dcm.energy.position < 3900:
            #Values updated March 10 2020
            target_state = [att2_5, att2_11]
        elif 3900 < self.dcm.energy.position < 4500:
            target_state = [att2_8]
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
            yield from bps.sleep(wait_time)

        
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

    def update_md(self, **md):
        '''
        Returns a dictionary of the updated metadata.
        '''
        self.md.copy()
        


class SMI_Beamline(Beamline):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Metadata
        self.md = kwargs
        self.SAXS = SMI_SAXS_Det()

        self.attenuators_state()
        self.crl_state()
        self.pressure_measurments()

        self.update_md()

    def modeAlignment_gisaxs(self, technique = 'gisaxs'):
        '''
        Set the beamline for alignement: move the beamstop out and insert the attenuators
        if technique is 'gisaxs', the reflected roi will be calculate for horizontal congif
        if technique is 'xrr', the reflected roi will be calculate for vertical congif
        '''
        # Put in attenuators
        yield from SMIBeam().insertFoils('Alignement')
        
        # Move beamstop
        yield from bps.mv(pil1m_bs_rod.x, bsx_pos + 5)
        

        self.setReflectedBeamROI(technique=technique)
        self.setDirectBeamROI()
        
        #Move the waxs detector out of the way
        if waxs.arc.position < 7.9:
            #yield from bps.mv(waxs.arc, 4)
            yield from bps.mv(waxs.arc, 13)

    def modeMeasurement_gisaxs(self, verbosity=3):
        '''
        Set the beamline for measurments: bring the beamstop in and
        remove the attenuator
        '''
        # Move beamstop
        yield from bps.mv(pil1m_bs_rod.x, bsx_pos) #2 for 4000 mm, 1.2 for 6500
        
        # Remove attenuators
        yield from SMIBeam().insertFoils('Measurement')       

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
        

    def setReflectedBeamROI(self, total_angle=0.16, technique = 'gisaxs', size=[48,8], verbosity=3):
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

        if technique == 'gisaxs':
            # Calculate the y position of the reflected beam        
            y_offset_mm = np.tan(np.radians(2*total_angle))*d
            y_offset_pix = y_offset_mm/pixel_size
            y_pos = int( y0 - size[1]/2 - y_offset_pix )

            # Define the reflected beam ROI on the pilatus 1M detector  
            yield from bps.mv(pil1M.roi1.min_xyz.min_x, int(x0-size[0]/2))
            yield from bps.mv(pil1M.roi1.size.x, int(size[0]))
            yield from bps.mv(pil1M.roi1.min_xyz.min_y, int(y_pos))
            yield from bps.mv(pil1M.roi1.size.y, int(size[1]))

        elif technique == 'xrr':
            # Calculate the x position of the reflected beam        
            x_offset_mm = np.tan(np.radians(2*total_angle))*d
            x_offset_pix = x_offset_mm/pixel_size
            x_pos = int( x0 - size[1]/2 - x_offset_pix )

            # Define the reflected beam ROI on the pilatus 1M detector  
            yield from bps.mv(pil1M.roi1.min_xyz.min_x, int(x_pos))
            yield from bps.mv(pil1M.roi1.size.x, int(size[0]))
            yield from bps.mv(pil1M.roi1.min_xyz.min_y, int(y0-size[1]/2))
            yield from bps.mv(pil1M.roi1.size.y, int(size[1]))
        else:
            raise ValueError('Unknown geometry fo alignement mode')


    def attenuators_state(self):
        self.att_state = {}
        att_ophyd = [att1_1, att1_2, att1_3, att1_4, att1_5, att1_6, att1_7, att1_8, att1_9, att1_10, att1_11, att1_12,
                     att2_1, att2_2, att2_3, att2_4, att2_5, att2_6, att2_7, att2_8, att2_9, att2_10, att2_11, att2_12]

        att_material = ['Cu_68um', 'Cu_68um', 'Cu_68um', 'Cu_68um', 'Sn_60um', 'Sn_60um', 'Sn_60um', 'Sn_60um',
                        'Sn_30um', 'Sn_30um', 'Sn_30um', 'Sn_30um',
                        'Mo_20um', 'Mo_20um', 'Mo_20um', 'Mo_20um', 'Al_102um', 'Al_102um', 'Al_102um', 'Al_102um',
                        'Al_9um', 'Al_9um', 'Al_9um', 'Al_9um']

        att_thickness = ['1x', '2x', '4x', '8x', '1x', '2x', '4x', '8x', '1x', '2x', '4x', '8x',
                         '1x', '2x', '4x', '8x', '1x', '2x', '4x', '8x', '1x', '2x', '4x', '6x']

        for att, material, thickness in zip(att_ophyd, att_material, att_thickness):
            if att.status.value == 'Open':
                self.att_state = {att.status.name: {'material': material, 'thickness': thickness}}


    def crl_state(self):
        for crl_le in [crl.lens1, crl.lens2, crl.lens3, crl.lens4, crl.lens5,
                       crl.lens6, crl.lens7, crl.lens8, crl.lens9, crl.lens10,
                       crl.lens11, crl.lens12]:

            if abs(crl_le.position) < 4:
                self.crl_state = 'micro_focusing'
                break
            else:
                self.crl_state = 'low_divergence'


    def pressure_measurments(self):
        if waxs_pressure.ch1_read.value == 'LO<E-03':
            self.pressure_state = 'in-vacuum'
        else:
            try: 
                pres = np.float(waxs_pressure.ch1_read.value)
                if pres < 1E-02:
                    self.pressure_state = 'in-vacuum'
                else:
                    self.pressure_state = 'in-air'
            except:
                self.pressure_state = 'Not read'


    def update_md(self, prefix='beamline_', **md):
        md_beamline = self.md.copy()

        RE.md[prefix + 'beamsize'] = self.crl_state
        RE.md[prefix + 'sample_environement'] = self.pressure_state
        RE.md[prefix + 'attenuators'] = self.att_state

        if prefix is not None:
            md_beamline = {'{:s}{:s}'.format(prefix, key): value for key, value in md_beamline.items()}

        self.md.update(md_beamline)

    # End class SMI_Beamline(Beamline)
    ########################################





class SMI_SAXS_Det(object):

    def __init__(self, **kwargs):

        #ToDo: add here the position of the gap
        self.detector_gap_x = [[830, 850], [617, 637], [405, 425], [193, 213]]
        self.detector_gap_y = [[485, 495]]

        self.pixel_size = 0.172
        self.getPositions()
        self.get_beamstop()


    def getPositions(self, **md):
        '''
        Get the interpolated sample detector distance and beam position from interpolate_db_sdds function defined in 01_load.py
        '''

        #Interpolate the distance and direct beam position
        self.distance, self.direct_beam = interpolate_db_sdds()
        self.distance *= 1000

        smi_saxs_detector.x0_pix.value = self.direct_beam[0]
        smi_saxs_detector.y0_pix.value = self.direct_beam[1]
        smi_saxs_detector.sdd.value = self.distance


    def get_beamstop(self):
        '''
        Read the positions of pindiode and gisaxs beamstop to determine which beamstop is in and which pixels to mask
        '''

        #ToDo: Calculate what pixels to mask for different beamstop positions
        if pil1m_bs_pd.x.position < 10 and pil1m_bs_rod.x.position < 10:
            smi_saxs_detector.bs_kind.value = 'rod_beamstop'

            #To be implemented with the good values, not hard-coded
            smi_saxs_detector.xbs_mask.value = 10
            smi_saxs_detector.ybs_mask.value = 10

        elif abs(pil1m_bs_pd.x.position) > 50 and abs(pil1m_bs_rod.x.position) < 50:
            smi_saxs_detector.bs_kind = 'pindiode'

            #To be implemented with the good values, not hard-coded
            smi_saxs_detector.xbs_mask.value = 10
            smi_saxs_detector.ybs_mask.value = 10

        else:
            smi_saxs_detector.bs_kind = 'None'

            #To be implemented with the good values, not hard-coded
            smi_saxs_detector.xbs_mask.value = 10
            smi_saxs_detector.ybs_mask.value = 10


    def set_beamstop(self):
        '''
        Modify the beamstop position in order to keep the beamstop aligned with the direct beam
        (Can be used when the sample detector distance is modified)
        '''
        
        self.getPositions()
        self.get_beamstop()

        # ToDo: Compare beamstop position vs direct beam position and change bs position
        pass



    #ToDo: check if gisaxs alignement still working with the new code
    '''
    def getPositions(self, **md):
        self.distance =  pil1m_pos.z.position

        #Add here also the position of the beam-diode
        #Will also need here to implement to interpolate the direct beam position with the sdd
        #Add also the interpolation of the distance when ready

        self.beamstop = [pil1m_bs_rod.x.position, pil1m_bs_rod.y.position]
        self.detector_position = [pil1m_pos.x.position, pil1m_pos.y.position]
        
        delta_pos_x = -self.detector_position[0] + self.detector_position_0_0[0]
        delta_pos_y = -self.detector_position[1] + self.detector_position_0_0[1]
        
        self.direct_beam = [np.round(self.direct_beam_0_0[0] - (delta_pos_x / self.pixel_size)), np.round(self.direct_beam_0_0[1] - (delta_pos_y / self.pixel_size))]
        return self
    '''



class SMI_WAXS_detector(Device):
    prefix = 'detector_waxs_'
    pixel_size = Component(Signal, value=0.172, name=prefix+'pixel_size', kind='hinted')
    x0_pix = Component(Signal, value=97, name=prefix+'x0_pix', kind='hinted')
    y0_pix = Component(Signal, value=1386, name=prefix+'y0_pix', kind='hinted')
    sdd = Component(Signal, value=274.9, name=prefix+'sdd', kind='hinted')



class SMI_SAXS_detector(Device):
    prefix = 'detector_saxs_'
    pixel_size = Component(Signal, value=0.172, name=prefix+'pixel_size', kind='hinted')

    #Defined in the pilatus file
    pos = pil1m_pos

    #Defined in the beamstop file
    saxs_bs_pindiode = pil1m_bs_pd
    saxs_bs_rod = pil1m_bs_rod

    bs_kind = Component(Signal, value='rod', name=prefix+'bs_kind', kind='hinted')
    xbs_mask = Component(Signal, value=0, name=prefix+'xbs_mask', kind='hinted')
    ybs_mask = Component(Signal, value=0, name=prefix+'ybs_mask', kind='hinted')

    x0_pix = Component(Signal, value=0, name=prefix+'y0_pix', kind='hinted')
    y0_pix = Component(Signal, value=0, name=prefix+'y0_pix', kind='hinted')
    sdd = Component(Signal, value=8300, name=prefix+'sdd', kind='hinted')


#ToDO: add a class for teh rayonix with sdd, pixel size, binning, ...

smi_waxs_detector = SMI_WAXS_detector(name='Pilatus300kw')
smi_saxs_detector = SMI_SAXS_detector(name='Pilatus1M')

SMI = SMI_Beamline()
pilatus1M = SMI_SAXS_Det()