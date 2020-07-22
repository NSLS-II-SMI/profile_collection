


def run_saxs_capsRPI(t=1): 
    x_list  = [ 6908,13476,19764,26055]#
    # Detectors, motors:
    dets = [pil1M]
    y_range = [2000, -8000, 11] #[2.64, 8.64, 2]
    samples = [    'LC-O38-6-100Cto40C', 'LC-O37-7-100Cto40C', 'LC-O36-9-100Cto40C', 'LC-O35-8-100Cto40C']
    #    param   = '16.1keV'
    assert len(x_list) == len(samples), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    det_exposure_time(t)
    for x, sample in zip(x_list, samples):
        yield from bps.mv(piezo.x, x)
        sample_id(user_name=sample, sample_name='') 
        yield from bp.scan(dets, piezo.y, *y_range)
          
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5) 
#,'SL-PS3','SL-PS3_98_8_PS33','SL-PS3_97_0_PS33','SL-PS3_94_9_PS33','SL-PS3_93_0_PS33','SL-PS3_89_9_PS33','SL-PS3_79_8_PS33','SL-PS3_70_1_PS33','SL-PS3_60_0_PS33','SL-PS3_49_9_PS33','SL-PS3_40_0_PS33','SL-PS3_29_8_PS33','SL-PS3_20_1_PS33','SL-PS3_10_0_PS33','SL-PS3_7_0_PS33','SL-PS3_4_9_PS33','SL-PS3_3_0_PS33','SL-PS33','SL-PS148




# xlocs = [42000,33000,24000,15000,5000,-4000,-13000,-22000,-32000,-41000,42000,33000,24000,15000,5000,-4000,-13000,-22000,-32000,-41000]
    #ylocs = [8800,8800,8800,8800,8800,8800,8800,8800,8800,8800,-7200,-7200,-7200,-7200,-7200,-7200,-7200,-7200,-7200,-7200]

# xlocs = [42000,33000,24000,15000,5000,-4000,-13000,-22000,-30000,42000,32000,24000,15000,4000,-4000,-12000]
   # ylocs = [8500,8500,8500,8500,8500,8500,8500,8500,8500,-6800,-6800,-6800,-6800,-6800,-6800,-6800]
  #  names = ['EPTD-y0.9-2s','EPTD-y1.0-2s','EPG-X0.8-2s','EPG-X0.9-2s','ETP-x0-2s','ETP-x0.1-2s','ETP-x0.2-2s','ETP-x0.3-2s','ETP-x0.4-2s','ETP-x0.6-2s','ETP-x0.7-2s','ETP-x0.8-2s','ETP-x0.9-2s','ETP-x1.0-2s','ETP-x0.5-2s','vacuum-2s']

#  xlocs = [-37550,-37550,-37550,-38950,-38950,-38950,-41850,-41850,-41850,-42850,-42850,-42850,-16100,-16100,-16100,-18600,-18600,-18600,-20400,-20400,-20400,-22500,-22500,-22500,-24100,-24100,-24100, -26100,-26100,-26100,-28300,-28300,-28300,-29300,-29300,-29300,-32900,-32900,-32900,-34900,-34900,-34900]
 #   ylocs = [8000, 8500,9000, 8000, 8500,9000, 8000, 8500,9000, 8000, 8500,9000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000,-7000, -7500, -8000]
 #   names = ['PACM-1','PACM-2','PACM-3','EPON828-1','EPON828-2','EPON828-3','DDS-1','DDS-2','DDS-3','B8O1-3-1','B8O1-3-2','B8O1-3-3','D2000-1','D2000-2','D2000-3','T3000-1','T3000-2','T3000-3','PPG-1','PPG-2','PPG-3','D230-1','D230-2','D230-3','blank-1mm-1','blank-1mm-2','blank-1mm-3','B8O1-1-1','B8O1-1-2','B8O1-1-3','B8O1-2-1','B8O1-2-2','B8O1-2-3','B9O1-1-1','B9O1-1-2','B9O1-1-3','B10O1-1-1','B10O1-1-2','B10O1-1-3','vacuum-1s-1','vacuum-1s-2','vacuum-1s-3']


def run_waxs_fastRPI(t=1):

    xlocs = [-20600,-14600,-6600, 1400,7600,14000,21500,28500,33900,39900, -34600,-25100,-15100,-6100,2900,12900,21900,31900,41900]
    y_top = -9300
    y_bot = 8100
    ylocs = [y_bot,y_bot,y_bot,y_bot,y_bot,y_bot,y_bot,y_bot,y_bot,y_bot,   y_top,y_top,y_top,y_top,y_top,y_top,y_top,y_top,y_top]
    ## A rack
    # names = ['A_EPTD_40_y0.6','A_EPTD_40_y0.5','A_EPTD_40_y0.4','A_EPTD_40_y0.3','A_EPTD_40_y0.2','A_EPTD_40_y0.1','A_EPTD_40_y0.0','A_EPTD_40_y1.0','A_EPTD_40_y0.9',
    #         'A_EPTD_100_y0.8','A_EPTD_100_y0.7','A_EPTD_100_y0.6','A_EPTD_100_y0.5','A_EPTD_100_y0.4','A_EPTD_100_y0.3','A_EPTD_100_y0.2','A_EPTD_100_y0.1', 'A_EPTD_100_y0.0']
    
    ## C rack
    # names = ['C_EITD_y0.6','C_EITD_y0.5','C_EITD_y0.4','C_EITD_y0.3','C_EITD_y0.2','C_EITD_y0.1','C_EITD_y0.0','C_EITD_y1.0','C_EITD_y0.9',
    #        'C_EIT_y0.8','C_EIT_y0.7','C_EIT_y0.6','C_EPTD_20_y1.0','C_EPTD_20_y0.9','C_EPTD_20_y0.8','C_EPTD_20_y0.7','C_EPTD_20_0.6', 'C_EPTD_20_y0.5']
    
    ## D rack    
    # names = ['D_ETTD_y0.8','D_ETTD_y0.7','D_ETTD_y0.6','D_ETTD_y0.5','D_ETTD_y0.4','D_ETTD_y0.3','D_ETTD_y0.2','D_ETTD_y0.1','D_ETTD_y0.0',
    #       'D_ETT_x1.0','D_ETT_x0.9','D_ETT_x0.8','D_ETT_x0.7','D_ETT_x0.6','D_EITD_y1.0','D_EITD_y0.9','D_EITD_y0.8', 'D_EITD_y0.7']
    
    ## E rack    
    # names = ['E_EXTD_y1.0','E_EXTD_y0.9','E_EXTD_y0.8','E_EXTD_y0.7','E_EXTD_y0.6','E_EXTD_y0.5','E_EXTD_y0.4','E_EXTD_y0.3','E_EXTD_y0.2',
    #       'E_EXTD_y0.1','E_EXTD_y0.0','E_EXT_x1.0','E_EXT_x0.9','E_EXT_x0.8','E_EXT_x0.7','E_EXT_x0.6','E_ETTD_y1.0','E_ETTD_y0.9']
    
    ## B rack    
    names = ['B_EPTD_e1.0','B_EPTD_e0.9','B_EPTD_e0.8','B_EPTD_e0.7','B_EPTD_e0.6','B_EPT_e1.0','B_EPT_e0.9','B_EPT_e0.8','B_EPT_e0.7','B_EPT_e0.6',
          'B_EPTD_20_y0.4','B_EPTD_20_y0.3','B_EPTD_20_y0.2','B_EPTD_20_y0.1','B_EPTD_20_y0.0','B_EPTD_40_y1.0','B_EPTD_40_y0.9','B_EPTD_40_y0.8','B_EPTD_40_y0.7']
    
    
    x_off = [-1000, 0, 1000]
    y_off = [-500, 500] 
    user = 'SL'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 45.5, 8)
    
    #yield from bps.mv(GV7.open_cmd, 1 )
    #time.sleep(10)
    #yield from bps.mv(GV7.open_cmd, 1 )
    #time.sleep(10)
    #yield from bps.mv(GV7.open_cmd, 1 )
    #time.sleep(10)
    
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y in zip(names, xlocs, ylocs):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)
            for yy, y_of in enumerate(y_off):        
                yield from bps.mv(piezo.y, y+y_of)
                for xx, x_of in enumerate(x_off):
                    yield from bps.mv(piezo.x, x+x_of)
                    xxa = xx+1
                    yya = yy+1 
                    name_fmt = '{sam}_wa{waxs}_locYX_{yy}{xx}'
                    sample_name = name_fmt.format(sam=sam, xx='%1.1d'%xxa, yy='%1.1d'%yya, waxs='%2.1f'%wa)
                    sample_id(user_name=user, sample_name=sample_name) 
                    print(f'\n\t=== Sample: {sample_name} ===\n')
                    yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 
    
def run_waxs_fastRPIy(t=1):

    xlocs = [13000,6700,400,-5950,-12400,-18700,-25200,-31600]
    ylocs = [0,0,0,0,0,0,0,0]
    names = ['O134A-1-N','O134A-2-N','O134A-3-N','O134A-4-N','O133A-1-N','O133A-2-N','O133A-3-N','O133A-4-N']

    
    y_off = [8000,7000,6000,5000,4000,3000,2000] 
    user = 'LC'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_locs)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(13, 13, 1)
    
    #yield from bps.mv(GV7.open_cmd, 1 )
    #time.sleep(10)
    #yield from bps.mv(GV7.open_cmd, 1 )
    #time.sleep(10)
    #yield from bps.mv(GV7.open_cmd, 1 )
    #time.sleep(10)
    
    for wa in waxs_range:
        yield from bps.mv(waxs, wa)
        for sam, x, y in zip(names, xlocs, ylocs):
            yield from bps.mv(piezo.x, x)            
            yield from bps.mv(piezo.y, y)
            for yy, y_of in enumerate(y_off):        
                yield from bps.mv(piezo.y, y+y_of)
            
                name_fmt = '{sam}_wa{waxs}_yloc{yy}'
                sample_name = name_fmt.format(sam=sam, yy='%2.2d'%yy, waxs='%2.1f'%wa)
                sample_id(user_name=user, sample_name=sample_name) 
                print(f'\n\t=== Sample: {sample_name} ===\n')
                yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3)     
    
    #yield from bps.mv(GV7.close_cmd, 1 )
    #time.sleep(10)
    #yield from bps.mv(GV7.close_cmd, 1 )
    #time.sleep(10)
    #yield from bps.mv(GV7.close_cmd, 1 )
    #time.sleep(10)



def run_waxs_cap_temp(t=1):
    ylocs = [3.9]	# Between 3.1 and 4.1
    name = 'nPEO_isothermal40'
    user = 'DW'    


    det_exposure_time(t,t)         
    dets = [pil1M, pil300KW]
    waxs_range = np.linspace(0, 13, 3)
    
    for wa in waxs_range:
        if wa == 0:
            temp = ls.ch1_read.value
        yield from bps.mv(waxs, wa)
        for y in ylocs:
            yield from bps.mv(stage.y, y)
            #temp = ls.ch1_read.value
            name_fmt = '{sam}_wa{waxs}_temp{tem}'
            sample_name = name_fmt.format(sam=name, tem=temp, waxs='%2.1f'%wa)
            sample_id(user_name=user, sample_name=sample_name) 
            print(f'\n\t=== Sample: {sample_name} ===\n')
            yield from bp.count(dets, num=1)

    yield from bps.mv(waxs, 0)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 
    




def run_saxs_fastRPI(t=1):

    xlocs = [42500,38300,29300,22900,16400,9000,2500,-3800,-7800,-11800,-15400,-19400,-23200,-27700,-31600,-34900,-38600]
    ylocs = [5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500,5500]
    names = ['BPSAW','FLSAW','DW-01','DW-02','DW-03','DW-04','blank-capillary','mTPSAW','BPSArSA-DMACw','BPSArSA-DMSOW','BPSOArSAW','pTPSAW','XW-1-35-1wd','XW-1-35-2w','XW-1-35-3w','XW-1-35-4w','blankW']   

    user = 'LC_SAXS_ONLY'    
    det_exposure_time(t,t)     
    
    assert len(xlocs) == len(names), f'Number of X coordinates ({len(x_list)}) is different from number of samples ({len(samples)})'
    
    # Detectors, motors:
    dets = [pil1M]
    for sam,x, y in zip(names, xlocs, ylocs):
        yield from bps.mv(piezo.y, y)
        yield from bps.mv(piezo.x, x)
        name_fmt = '{sam}'
        sample_name = name_fmt.format(sam=sam)
        sample_id(user_name=user, sample_name=sample_name) 
        print(f'\n\t=== Sample: {sample_name} ===\n')
        yield from bp.count(dets, num=1)

    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.3, 0.3) 



def run_contRPI(t=1, numb = 100, sleep = 5):

    det_exposure_time(t,t)
    dets = [pil1M,pil300KW]
    #dets = [pil300Kw]
    for i in range(numb):
        yield from bp.count(dets, num=1)
        time.sleep(sleep)
        
def acq_tem(t = 0.2):
        sam = '0122A-11-lk5.5m-1s'

        dets = [pil1M]
        det_exposure_time(t,t)
        temp = ls.ch1_read.value 
        name_fmt = '{sam}_{temp}C'
        sample_name = name_fmt.format(sam=sam, temp='%4.1f'%temp)
        sample_id(user_name='LC', sample_name=sample_name) 
        yield from bp.scan(dets, stage.y,5.3,5.9, 4)

def acq_bd(t = 0.2):
        sam = '0122A-10-lk5.5m-0.2s-4'

        dets = [pil1M]
        det_exposure_time(t,t)
        temp = ls.ch1_read.value 
        name_fmt = '{sam}_{temp}C'
        sample_name = name_fmt.format(sam=sam, temp='%4.1f'%temp)
        sample_id(user_name='LC', sample_name=sample_name) 
        yield from bp.scan(dets, piezo.th, 0, 0, 1)

#Sample set 1        
#xlocs = [60000,38700,31700,25700,20700,11900,2899,-13100,-28100,-37100,-42099,-35100,-28100,-23000,-16000,-8200,-2200,3800,12800,19800,25800,33800,41800]
#ylocs = [7300,7300,7300,7300,7300,7300,7300,7300,7300,7300,7300,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700,-8700]
# names = ['blank','XW-01-033','NF150-1A','NF150-2A','NF150-1B','NF150-2B','DW-13','DW-14','DW-15','DW-nPEO','Blank Kapton','XW-01-40','XW-1-35-4d','XW-1-35-3d','XW-1-35-2d','XW-1-35-1d','Fenton-BPSOArSA','Fenton-BPSArSA','Fenton-mTPSA','Fenton-BPSA','BPSArSA-DMSOd','pTPSAd','FLSAd']



# ylocs = [5000,5000,5000,5000,5000]
 #   xlocs = [29500,23000,16500,9000,2600]
  #  names = ['DW-1','DW-2','DW-3','DW-4','blankcap-1.5-vacuum']

#Sample set 3
# xlocs = [43800,33100,24100,14800,4400,-6900,-16600,-18200,-27400,-28400,-36400,-40400,44800,39800,34800,31800,25800,21800,16800,13000,6800,4000,-2200,-5200,-11200,-14400,-21200,-23400,-31200,-33400,-40000,-43000]
  #  ylocs = [8400,8400,8400,8400,8400,8400,8400,8400,8400,8000,8400,8400,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000,-6000]
   # names = ['m-TPN1-11-1','m-TPN1-11-2','m-TPN1-CNC-13','m-TPN1-CNC-14','m-TPN1-CNC-15-5','m-TPN1-CNC-15-m','SP59-1','SP59-2','P59-1','P59-2','828-T3000-PAM-X0.0-1','828-T3000-PAM-X0.0-2','828-T3000-PAM-X0.1-1','828-T3000-PAM-X0.1-2','828-T3000-PAM-X0.3-1','828-T3000-PAM-X0.3-2','828-T3000-PAM-X0.4-1','828-T3000-PAM-X0.4-2','828-T3000-PAM-X0.5-1','828-T3000-PAM-X0.5-2','828-T3000-PAM-X0.6-1','828-T3000-PAM-X0.6-2','828-T3000-PAM-X0.7-1','828-T3000-PAM-X0.7-2','828-T3000-PAM-X0.8-1','828-T3000-PAM-X0.8-2','828-T3000-PAM-X0.9-1','828-T3000-PAM-X0.9-2','828-T3000-PAM-X1.0-1','828-T3000-PAM-X1.0-2']
 
 
#Sample set 4
#names = ['828-T3000-D230-PACM-X0.7-Y0.0-1','828-T3000-D230-PACM-X0.7-Y0.0-2','828-T3000-D230-PACM-X0.7-Y0.1-1','828-T3000-D230-PACM-X0.7-Y0.1-2','828-T3000-D230-PACM-X0.7-Y0.2-1','828-T3000-D230-PACM-X0.7-Y0.2-2','828-T3000-D230-PACM-X0.7-Y0.3-1','828-T3000-D230-PACM-X0.7-Y0.3-2','828-T3000-D230-PACM-X0.7-Y0.4-1','828-T3000-D230-PACM-X0.7-Y0.4-2','828-T3000-D230-PACM-X0.7-Y0.5-1','828-T3000-D230-PACM-X0.7-Y0.5-2','828-T3000-D230-PACM-X0.7-Y0.6-1','828-T3000-D230-PACM-X0.7-Y0.6-2','828-T3000-D230-PACM-X0.7-Y0.7-1','828-T3000-D230-PACM-X0.7-Y0.7-2','828-T3000-D230-PACM-X0.7-Y0.8-1','828-T3000-D230-PACM-X0.7-Y0.8-2','828-T3000-D230-PACM-X0.7-Y0.9-1','828-T3000-D230-PACM-X0.7-Y0.9-2','828-T3000-D230-PACM-X0.7-Y1.0-1','828-T3000-D230-PACM-X0.7-Y1.0-2','828-EK3140-PACM-X0.0-1','828-EK3140-PACM-X0.0-2','828-EK3140-PACM-X0.1-1','828-EK3140-PACM-X0.1-2','828-EK3140-PACM-X0.2-1','828-EK3140-PACM-X0.2-2','828-EK3140-PACM-X0.3-1','828-EK3140-PACM-X0.3-2','828-EK3140-PACM-X0.4-1','828-EK3140-PACM-X0.4-2','828-EK3140-PACM-X0.5-1','828-EK3140-PACM-X0.5-2','828-EK3140-PACM-X0.6-1','828-EK3140-PACM-X0.6-2','828-EK3140-PACM-X0.7-1','828-EK3140-PACM-X0.7-2','828-EK3140-PACM-X0.8-1','828-EK3140-PACM-X0.8-2']

#ylocs =        [8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000] 
   #xlocs = [44000,39800,34800,31500,25800,21800,16800,13000,6800,4000,-2200,-5200,-12200,-14400,-21200,-23400,-31200,-33400,-40000,-43000,44000,39800,34800,31500,25800,21800,16600,13000,6800,4000,-2200,-5200,-12200,-14400,-21200,-23400,-32000,-33400,-40000,-42500]


#Sample set 5
  # ylocs =        [8000,8000,8000,8200,8000,8400,8400,8400,8600,8600,8600,8600,8600,8200,8200,8200,8200,8200,8200,8200,-6600,-6600,-6600,-6600,-6600,-6600,-6600,-6600,-6600,-6600,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000] 
   
  #  xlocs = [43000,41400,34500,32800,26500,22500,17500,14500,7500,3500,-500,-5500,-10500,-14500,-20500,-23500,-29500,-33500,-39500,-42500,44000,41000,36000,33000,27000,23000,18000,14000,8000,4000,0,-6000,-10000,-13500,-20500,-23500,-30500,-32500,-39500,-42500]
   
    #names = ['828-EK3140-PACM-X0.9-1','828-EK3140-PACM-X0.9-2','828-EK3140-PACM-X1.0-1','828-EK3140-PACM-X1.0-2','828-D2000-PACM-X0.6-1','828-D2000-PACM-X0.6-2','828-D2000-PACM-X0.7-1','828-D2000-PACM-X0.7-2','828-D2000-PACM-X0.8-1','828-D2000-PACM-X0.8-2','828-D2000-PACM-X0.9-1','828-D2000-PACM-X0.9-2','828-D2000-PACM-X1.0-1','828-D2000-PACM-X1.0-2','TGPPM-2E1-0.00MDA-1','TGPPM-2E1-0.00MDA-2','TGPPM-2E1-0.25MDA-1','TGPPM-2E1-0.25MDA-2','TGPPM-2E1-0.50MDA-1','TGPPM-2E1-0.50MDA-2','TGPPM-2E1-0.75MDA-1','TGPPM-2E1-0.75MDA-2','TGPPM-2E1-1.00MDA-1','TGPPM-2E1-1.00MDA-2','TCDDA-XDT-1-1','TCDDA-XDT-1-2','TCDDA-XDT-2-1','TCDDA-XDT-2-2','TCDDA-XDT-3-1','TCDDA-XDT-3-2','TCDDA-XDT-4-1','TCDDA-XDT-4-2','TCDDA-XDT-5-1','TCDDA-XDT-5-2','TCDDA-XDT-6-1','TCDDA-XDT-6-2','TCDDA-XDT-7-1','TCDDA-XDT-7-2','TCDDA-XDT-8-1','TCDDA-XDT-8-2']



#Sample set 6-1
#names = [TCDDA-XDT-10-1,TCDDA-XDT-10-2,TCDDA-XDT-11-1,TCDDA-XDT-11-2,TCDDA-XDT-12-1,TCDDA-XDT-12-2,TCDDA-XDT-13-1,TCDDA-XDT-13-2,TCDDA-XDT-14-1,TCDDA-XDT-14-2,TCDDA-XDT-15-1,TCDDA-XDT-15-2,TCDDA-XDT-16-1,TCDDA-XDT-16-2,TCDDA-XDT-17-1,TCDDA-XDT-17-2,TCDDA-XDT-18-1,TCDDA-XDT-18-2,SP-2d-1,SP-2d-2,TCDDA-XDT-9-1,TCDDA-XDT-9-2,SP-1b-1,SP-1b-2,SP-1d-1,SP-1d-2,SP-2b-1,SP-2b-2,SP-3b-1,SP-3b-2,SP-3d-1,SP-3d-2,SP-5b-1,SP-5b-2,SP-6b-1,SP-6b-2,SP-4b-1,SP-4b-2,vacuum-10s]
#ylocs =        [8000,8000,8000,8000,8000,8000,8000,8000,8000,8000,8000,8600,8600,8000,8000,8600,8800,8000,8000,8000,-7000,-6500,-7200,-7200,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-7000,-6500,-7200,-7200,-6500] 
   
  #  xlocs = [44000,42000,36000,33000,26000,23000,17000,14000,8000,4000,-1000,-7000,-10000,-15000,-22000,-25000,-30000,-33000,-42000,-43500,45000,42000,36000,34500,29000,27000,22000,20000,12000,10000,4500,3000,-4000,-5500,-13500,-15000,-20000,-21500,-35500]
   
   

#Sample set 6-2
#ylocs=[-6500,-6500,-6500,-6500,-6500,-6500]
#xlocs=[-29500,-33200,-37200,-40200,-41600,-43600]
   # names = ['MP-FLSAW','MP-BPSAW','DW-1','DW-2','DW-3','DW-4']


#ylocs =        [8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400,8400] 
   #xlocs = [44000,39800,34800,31500,25800,21800,16800,13000,6800,4000,-2200,-5200,-12200,-14400,-21200,-23400,-31200,-33400]

