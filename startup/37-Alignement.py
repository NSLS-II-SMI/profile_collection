import matplotlib.pyplot as plt
import numpy as np

print(f'Loading {__file__}')

def align_gisaxs_height(rang=0.3, point=31, der=False):
        yield from bp.rel_scan([pil1M], piezo.y, -rang, rang, point)
        ps(der=der, plot = False)
        yield from bps.mv(piezo.y, ps.cen)


def align_gisaxs_height_lee(rang=0.3, point=31, der=False):
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


def alignement_xrr(angle=0.15):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='xrr')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

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
        yield from bps.mv(prs, ps.peak + 0.15)


        # move to theta 0 + value
        yield from bps.mv(prs, ps.peak - angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=-angle, technique='xrr')
        
        # Scan theta and height
        yield from align_xrr_prs(0.2, 31)
        yield from align_xrr_height(200, 21)
        yield from align_xrr_prs(0.05, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(prs, ps.cen + angle)
        yield from smi.modeMeasurement()
        

def alignement_gisaxs(angle=0.15):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(800, 21, der=True)
        yield from align_gisaxs_th(1.5, 27)
        #yield from align_gisaxs_height(300, 11, der=True)
        #yield from align_gisaxs_th(0.5, 16)
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 31)
        yield from align_gisaxs_height(250, 21)
        yield from align_gisaxs_th(0.025, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()

def alignement_gisaxs_quickLee(angle=0.15):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(700, 16, der=True)
        yield from align_gisaxs_th(1, 15)
        # yield from align_gisaxs_height(300, 11, der=True)
        # yield from align_gisaxs_th(0.5, 16)
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 31)
        yield from align_gisaxs_height_lee(150, 21)
        # yield from align_gisaxs_th(0.025, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, piezo.th.position - angle)
        yield from smi.modeMeasurement()


def alignement_gisaxs_multisample(angle=0.15):
        
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
        yield from align_gisaxs_height(150, 21)
        yield from align_gisaxs_th(0.025, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        # yield from smi.modeMeasurement()


def alignement_gisaxs_multisample_special(angle=0.15):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        # yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()
        yield from align_gisaxs_height(700, 16, der=True)

        # Scan theta and height
        # yield from smi.setReflectedBeamROI(total_angle=0.02, technique='gisaxs')
        # yield from align_gisaxs_th(2, 30)
        # yield from smi.setDirectBeamROI()
        # yield from align_gisaxs_height(300, 11, der=True)
        # yield from smi.setReflectedBeamROI(total_angle=0.02, technique='gisaxs')
        # yield from align_gisaxs_th(0.5, 16)
        
        # move to theta 0 + value
        yield from bps.mvr(piezo.th, angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 31)
        yield from align_gisaxs_height(150, 21)
        yield from align_gisaxs_th(0.025, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mvr(piezo.th, -angle)
        # yield from smi.modeMeasurement()


def quick_alignement_gisaxs_multisample(angle=0.15):       
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()

        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        # yield from align_gisaxs_height(500, 31, der=True)

        # move to theta 0 + value
        yield from bps.mvr(piezo.th, angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_height(300, 31)
        yield from align_gisaxs_th(0.2, 51)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mvr(piezo.th, -angle)
        # yield from smi.modeMeasurement()

        
def alignement_special_P(angle=0.15):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(700, 16, der=True)

        yield from smi.setReflectedBeamROI(total_angle=0.12, technique='gisaxs')

        yield from align_gisaxs_th(1, 15)
        yield from smi.setDirectBeamROI()

        yield from align_gisaxs_height(300, 11, der=True)
        yield from smi.setReflectedBeamROI(total_angle=0.1, technique='gisaxs')

        yield from align_gisaxs_th(0.5, 16)
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)
        
        yield from bps.mv(att2_9, 'Retract')
        yield from bps.sleep(1)
        yield from bps.mv(att2_9, 'Retract')

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 31)
        yield from align_gisaxs_height(300, 21)
        yield from align_gisaxs_th(0.05, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()
        

        
def alignement_special(angle=0.15):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(700, 16, der=True)

        yield from smi.setReflectedBeamROI(total_angle=0.12, technique='gisaxs')

        yield from align_gisaxs_th(1, 15)
        yield from smi.setDirectBeamROI()

        yield from align_gisaxs_height(300, 11, der=True)
        yield from smi.setReflectedBeamROI(total_angle=0.1, technique='gisaxs')

        yield from align_gisaxs_th(0.5, 16)
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 31)
        yield from align_gisaxs_height(300, 21)
        yield from align_gisaxs_th(0.05, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()

def alignement_gisaxs_new(angle=0.15, he_ra_db=700, he_np_db=16, th_ra_db=0.7, th_np_db=11, th_ra_rb=700, th_np_rb = 16, he_ra_rb=700, he_np_rb = 16):
        """
        Standart macro for aligning the sample for GISAXS. First alignement of height and theta on the direct beam (twice with different ranges).
        Then alignememnt of theta and height on the reflected beam. At the end of teh macros, theta will return to the new zeros

        angle: incident angle at which alignement on the reflected beam will be done
        he_ra_db, he_ra_db, th_ra_db, th_np_db: height and theta range and number of point for the direct beam alignement
        he_ra_rb, he_ra_rb, th_ra_rb, th_np_rb: height and theta range and number of point for the reflected beam alignement
        """
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(he_ra_db, he_np_db, der=True)
        yield from align_gisaxs_th(th_ra_db, th_np_db)
        yield from align_gisaxs_height(np.int(0.5*he_ra_db), np.int(0.7*he_np_db), der=True)
        yield from align_gisaxs_th(np.int(0.5*th_ra_db), np.int(1.5*he_np_db))
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th(0.2, 31)
        yield from align_gisaxs_height(300, 21)
        yield from align_gisaxs_th(0.05, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()


 
def alignement_special_hex(angle=0.15):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height_hex(0.5, 21, der=True)

        # yield from smi.setReflectedBeamROI(total_angle=0.12, technique='gisaxs')

        # yield from align_gisaxs_th_hex(0.6, 15)
        # yield from smi.setDirectBeamROI()

        # yield from align_gisaxs_height_hex(0.3, 11, der=True)
        # yield from smi.setReflectedBeamROI(total_angle=0.1, technique='gisaxs')

        # yield from align_gisaxs_th_hex(0.5, 16)
        
        # move to theta 0 + value
        yield from bps.mvr(stage.th, angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle, technique='gisaxs')
        
        # Scan theta and height
        yield from align_gisaxs_th_hex(0.5, 41)
        yield from align_gisaxs_height_hex(0.3, 21)
        yield from align_gisaxs_th_hex(0.05, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(stage.th, ps.cen - angle)
        yield from smi.modeMeasurement()



def alignement_gisaxs_cdgisaxs(angle=0.1):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment()
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(700, 16, der=True)
        yield from align_gisaxs_th_hex(1, 11)
        yield from align_gisaxs_height(300, 11, der=True)
        yield from align_gisaxs_th_hex(0.4, 16)
        
        # move to theta 0 + value
        yield from bps.mvr(stage.th, angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle)
        
        # Scan theta and height
        yield from align_gisaxs_th_hex(0.5, 31)
        yield from align_gisaxs_height(200, 21, der=True)
        yield from align_gisaxs_th_hex(0.1, 31)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(stage.th, ps.cen - angle)
        yield from smi.modeMeasurement()


def alignement_gisaxs_hex(angle=0.1):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.5, 0.5)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment()
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height_hex(0.700, 16, der=True)
        # yield from align_gisaxs_th_hex(1, 11)
        # yield from align_gisaxs_height_hex(0.300, 11, der=True)
        # yield from align_gisaxs_th_hex(0.4, 16)
        
        # move to theta 0 + value
        # yield from bps.mv(stage.th, angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle)
        
        # Scan theta and height
        yield from align_gisaxs_th_hex(0.5, 31)
        yield from align_gisaxs_height_hex(0.200, 21)
        yield from align_gisaxs_th_hex(0.1, 21)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(stage.th, ps.cen - angle)
        yield from smi.modeMeasurement()


def alignement_gisaxs_hex_short(angle = 0.12):
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment()
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height_hex(0.500, 21, der=True)
        
        # move to theta 0 + value
        yield from bps.mv(stage.th, angle)

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


def quickalign_gisaxs(angle = 0.15):
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment()
        
        # move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle)
        
        # Scan theta and height
        yield from align_gisaxs_height(200, 31)
        yield from align_gisaxs_th(0.1, 21)

        # Close all the matplotlib windows
        plt.close('all')
        
        # Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()


def alignement_gisaxs_shorter(angle = 0.15):      
        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)
        
        smi = SMI_Beamline()
        yield from smi.modeAlignment()
        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()

        # Scan theta and height
        yield from align_gisaxs_height(300, 21, der=True)
        yield from align_gisaxs_th(1, 21)

        # move to theta 0 + value
        #yield from bps.mv(piezo.th, ps.peak + angle)
        # Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle)
        # Scan theta and height
        yield from align_gisaxs_th(0.5, 21)
        yield from align_gisaxs_height(150, 21)
        yield from align_gisaxs_th(0.05, 16)
        
        # Close all the matplotlib windows
        plt.close('all')
        
        #Return angle
        yield from bps.mv(piezo.th, ps.cen - angle)
        yield from smi.modeMeasurement()

