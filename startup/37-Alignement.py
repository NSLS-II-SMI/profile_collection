import matplotlib.pyplot as plt
import numpy as np

print(f'Loading {__file__}')

def align_gisaxs_height(rang=0.3, point=31, der=False):
        yield from bp.rel_scan([pil1M], piezo.y, -rang, rang, point)
        ps(der=der, plot = False)
        yield from bps.mv(piezo.y, ps.cen)


def align_gisaxs_height_rb(rang=0.3, point=31, der=False):
        yield from bp.rel_scan([pil1M], piezo.y, -rang, rang, point)
        ps(der=der, plot = False)
        yield from bps.mv(piezo.y, ps.peak)


def align_gisaxs_th(rang=0.3, point=31):
        yield from bp.rel_scan([pil1M], piezo.th, -rang, rang, point)
        ps(plot = False)
        yield from bps.mv(piezo.th, ps.peak)


def align_xrr_prs(rang=0.3, point=31):
        yield from bp.rel_scan([pil1M], prs, -rang, rang, point)
        ps(plot = False)
        yield from bps.mv(prs, ps.peak)


def align_xrr_height(rang=0.3, point=31, der=False):
        yield from bp.rel_scan([pil1M], piezo.x, -rang, rang, point)
        ps(der=der, plot = False)
        yield from bps.mv(piezo.x, ps.peak)


def align_gisaxs_height_hex(rang=0.3, point=31, der=False):
        yield from bp.rel_scan([pil1M], stage.y, -rang, rang, point)
        ps(der=der,plot = False)
        yield from bps.mv(stage.y, ps.cen)


def align_gisaxs_th_hex(rang=0.3, point=31):
        yield from bp.rel_scan([pil1M], stage.th, -rang, rang, point)
        ps(plot = False)
        yield from bps.mv(stage.th, ps.peak)


def alignement_gisaxs(angle=0.15):
        """
        Regular alignement routine for gisaxs and giwaxs. First, scan of the sample height and incident angle on the direct beam. 
        Then scan of teh incident angle, height and incident angle again on the reflected beam.

        param angle: np.float. Angle at which the alignement on the reflected beam will be done

        """

        #Activate the automated derivative calculation
        bec._calc_derivative_and_stats = True

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(800, 21, der=True)
        yield from align_gisaxs_th(1.5, 27)
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 21)
        yield from align_gisaxs_height_rb(150, 16)
        yield from align_gisaxs_th(0.025, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()
        
        #Deactivate the automated derivative calculation
        bec._calc_derivative_and_stats = False


def alignement_gisaxs_doblestack(angle=0.15):
        """
        Modification of teh regular alignement routine for the doble-stack. Since top row is out of the center of rotation of of theta, the alignement on teh direc does not work.
        Therefore, only teh height is aligned on the direct beam but the incident angle is aligned on the reflected beam with a small incident angle.
        The alignement on the reflected beam is the same as for regular alignement.

        param angle: np.float. Angle at which the alignement on the reflected beam will be done

        """
        #Activate the automated derivative calculation
        bec._calc_derivative_and_stats = True
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan height on the DB only
        yield from align_gisaxs_height(800, 21, der=True)
        
        # alignement of incident angle at ai = 0.1 deg so the alignement use the reflected roi not sitting on the db position
        yield from smi.setReflectedBeamROI(total_angle=0.1, technique='gisaxs')
        yield from align_gisaxs_th(1.5, 27)
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 21)
        yield from align_gisaxs_height_rb(150, 16)
        yield from align_gisaxs_th(0.025, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()

        #Deactivate the automated derivative calculation
        bec._calc_derivative_and_stats = False


def alignement_gisaxs_multisample(angle=0.15):
        """
        This is design to align several samples at the same time. The attenuators, bs motion, ... needs to be done outside of this maccro, so there is no back and forth in term 
        of motor motion from sample to sample.

        param angle: np.float. Angle at which the alignement on the reflected beam will be done

        """
        #Activate the automated derivative calculation
        bec._calc_derivative_and_stats = True

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        # yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(700, 16, der=True)
        yield from align_gisaxs_th(1, 15)
        yield from align_gisaxs_height(300, 11, der=True)
        yield from align_gisaxs_th(0.5, 16)
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 31)
        yield from align_gisaxs_height_rb(150, 21)
        yield from align_gisaxs_th(0.025, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        # yield from smi.modeMeasurement()

        #Deactivate the automated derivative calculation
        bec._calc_derivative_and_stats = False


def alignement_gisaxs_hex(angle=0.1):
        """
        Regular alignement routine for gisaxs and giwaxs using the hexapod. First, scan of the sample height and incident angle on the direct beam. 
        Then scan of teh incident angle, height and incident angle again on the reflected beam.

        param angle: np.float. Angle at which the alignement on the reflected beam will be done

        """

        #Activate the automated derivative calculation
        bec._calc_derivative_and_stats = True

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment()
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height_hex(0.5, 21, der=True)
        yield from align_gisaxs_th_hex(0.5, 11)
        
        # move to theta 0 + value
        yield from bps.mv(stage.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th_hex(0.3, 21)
        yield from align_gisaxs_height_hex(0.1, 21)
        yield from align_gisaxs_th_hex(0.05, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(stage.th, ps.cen - angle)
        yield from smi.modeMeasurement()

        #Deactivate the automated derivative calculation
        bec._calc_derivative_and_stats = False


def alignement_gisaxs_hex_short(angle = 0.12):
        """
        Short alignement routine for gisaxs and giwaxs using the hexapod. First, scan of the sample height and incident angle on the direct beam. 
        Then scan of teh incident angle, height and incident angle again on the reflected beam.

        param angle: np.float. Angle at which the alignement on the reflected beam will be done

        """

        #Activate the automated derivative calculation
        bec._calc_derivative_and_stats = True
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment()
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height_hex(0.500, 21, der=True)
        
        # move to theta 0 + value
        yield from bps.mvr(stage.th, angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle)
        
        # Scan theta and height
        yield from align_gisaxs_th_hex(0.7, 23)
        yield from align_gisaxs_height_hex(0.15, 31)
        yield from align_gisaxs_th_hex(0.06, 25)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(stage.th, ps.cen-angle)
        yield from smi.modeMeasurement()

        #Deactivate the automated derivative calculation
        bec._calc_derivative_and_stats = False


def quickalign_gisaxs(angle = 0.15):        
        """
        Short alignement with only alignement on the reflected beam.

        param angle: np.float. Angle at which the alignement on the reflected beam will be done

        """

        #Activate the automated derivative calculation
        bec._calc_derivative_and_stats = True
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment()
        
        # move to theta 0 + value
        yield from bps.mvr(piezo.th, angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle)
        
        # Scan theta and height
        yield from align_gisaxs_height_rb(200, 31)
        yield from align_gisaxs_th(0.1, 21)

        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()

        #Deactivate the automated derivative calculation
        bec._calc_derivative_and_stats = False


def alignement_xrr(angle=0.15):
        """
        This routine is for samples mounted at 90 degrees, so the alignement is done using prs stage as incident angle and piezo.x as height

        param angle: np.float. Angle at which the alignement on the reflected beam will be done

        """

        #Activate the automated derivative calculation
        bec._calc_derivative_and_stats = True

        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='xrr')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI(technique='xrr')

        # Scan theta and height
        yield from align_xrr_height(800, 16, der=True)

        # For XRR alignment, a poor results was obtained at incident angle 0. To improve the alignment success
        # the prs alignment is done at an angle of 0.15 deg
        yield from smi.setReflectedBeamROI(total_angle=-0.15, technique='xrr')
        yield from align_xrr_prs(1, 20)

        yield from smi.setDirectBeamROI()
        yield from align_xrr_height(500, 13, der=True)

        yield from smi.setReflectedBeamROI(total_angle=-0.15, technique='xrr')
        yield from align_xrr_prs(0.5, 21)
        
        yield from bps.mv(prs, ps.peak + 0.0725)

        # move to theta 0 + value
        yield from bps.mv(prs, ps.peak - angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=-2*angle, technique='xrr')
        
        # Scan theta and height
        yield from align_xrr_prs(0.2, 31)
        yield from align_xrr_height(200, 21)
        yield from align_xrr_prs(0.05, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(prs, ps.cen + angle)
        yield from smi.modeMeasurement()
        
        #Deactivate the automated derivative calculation
        bec._calc_derivative_and_stats = False
