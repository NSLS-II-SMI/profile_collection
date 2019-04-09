def align_gisaxs_height(  rang = 0.3, point = 31 ,der=False  ):   
        yield from bp.rel_scan([pil1M], piezo.y, -rang, rang, point )
        ps(der=der)
        yield from bps.mv(piezo.y, ps.cen)


def align_gisaxs_th(  rang = 0.3, point = 31   ):             
        yield from bp.rel_scan([pil1M], piezo.th, -rang, rang, point )
        ps()
        yield  from bps.mv(piezo.th, ps.peak)  
        
def alignement_gisaxs(angle = 0.15):      
        smi = SMI_Beamline()
        yield from smi.modeAlignment_gisaxs()
        
        #Set direct beam ROI
        yield from smi.setDirectBeamROI()

        #Scan theta and height
        yield from align_gisaxs_height(700, 16, der=True)
        yield from align_gisaxs_th(1, 11)
        yield from align_gisaxs_height(300, 11, der=True)
        yield from align_gisaxs_th(0.5, 16)
        
        #move to theta 0 + value
        yield from bps.mv(piezo.th, ps.peak + angle)

        #Set reflected ROI
        yield from smi.setReflectedBeamROI(total_angle=angle)
        
        #Scan theta and height
        yield from align_gisaxs_th(0.3, 31)
        yield from align_gisaxs_height(200, 21)
        yield from align_gisaxs_th(0.05, 21)
        
        #Return angle
        # TODO: Should we return to 0
        yield from bps.mv(piezo.th, ps.cen)
        yield from smi.modeMeasurement_gisaxs()
