# Remote access:
#n2sn_list_users
# n2sn_add_user --login yuzhang guacctrl
# n2sn_add_user --login yuzhang guacview

#  https://www.nsls2.bnl.gov/docs/remote/N2SNUserTools.html


#/nsls2/xf12id2/data/images/users/2022_1/308251_Nam


# For 1M
# det2, setthreshold energy 16100 autog 11000

# For 900KW
# camonly
# det3,  setthreshold energy 16100 autog 11000


##Collect data:

#SMI: 2022/7/12 Afternoon around 5:00 
# SAF: 308071   Standard        Beamline 12-ID   proposal:  308251
# create proposal: proposal_id( '2022_2', '308251_Nam' ) #create the proposal id and folder



# Data is saved in 
#/nsls2/xf12id2/data/images/users/2022_2/308251_Nam

# Load Samples
# Check locations -X
# pump down,  Auto Evacuate
# Open valves

##Old one
#  go to the second window under,  det@xf12id2-det3:~> camonly
# change the energy threshold:  setthreshold energy 16100 autog 11000
## New one
# ssh -X det@xf12id2-det3 (pwd: Pilatus2)
# ./start_camserver 
# setthreshold energy 16100 autog 11000


# det 1M, X -5, Y -20 , Z: 5000 (5 meter)
#  beam center: [ 455, 797  ]
# beam stop, X 1.748 , Y -13 


# align the gisaxs beam stop
# then save it:  beamstop_save()
# for 900kw, 



# Y: 4000, Z: 2500  
# Energy: 16.1 keV, 0.77009 A
# when finish the one batch, before bleed to air, 
# shut down the camserver of 900 kw first
# go the camonly, exit (twice)
# the Auto Bleed to Air

#make the height pizo.y = 4000, Z= 2500
# manually measure sample 1 and 2 

#Then run macro for all 19 samples 
#     angle_arc = np.array([0.05, 0.08, 0.10, 0.15, 0.2, 0.3 ]) # incident angles 
#     waxs_angle_array = np.array( [ 7, 27, 47 ] ) ,





# when finish one batch of measurement
# 1)  RE(shclose())    #close the beam,  # 
# 2) click 900 kw on the css screen to shut down the 900 kw detector # the Detectro outlet LED should change from green to gray
# 3) click Auto Bleed to Air, after half minute, click WAXS full vent, # you should see the TCG:7 should increase and the LED changes from green to yellow
# 4) you can wait until TCG:9 goes to 780, then you can open the sample chamber
# 


# open the hutch
# load samples, do vacuum, by clicking 'auto evacuate',  
# during the vacuum, you can check sample postion, 
# go to the det3 terminal, enter ctrl + X,  wait until see the * , then copy and paste    setthreshold energy 16100 autog 11000
#  RE(shopen())  #open the beam
# wait unitil 2:TCG:7 turn into green, you can open GV7 
# manual alignment
#  1)  RE(SMI.modeAlignment())     
#       #you  will see under 14-18 kev filter 4X, 2X, 1X in ,
#       also SAXS 3 mm beamstop, X will change from 1.74 to 6.74
# 2)  sample_id(user_name='test', sample_name='test')  # change sample name to test 
# 3)  manually tweek SmarAct Y, up or down using a small step size (such 100 um ), trying to block the beam, 
#     for example, + 100 um block the beam, -100 um see the beam
# 4)   RE( run_giwaxs_Kim() )




## NOTE:
# every time when change this file (macro), reload it to the terminal by 
#    %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Kim_2022C2.py
# RE.abort() 


# # ## First RUN, 15 samples,  y = 1000, Z= 5000 
# sample_list = [  'S15', 'S14', 'S13', 'S12', 'S11', 'S10', 'S9', 'S8', 'S7', 'S6', 'S5', 'S4', 'S3', 'S2', 'S1'     ] [9:]  #[1:2 ]
# x_list = [ -45500 ,  -37500,  -31000, -23200, -15100, -7800, -1700, 4999, 12599, 19199, 25399, 32399, 39199, 45799, 52598 ] [9:] # [1:2]  


#note by YG
# the data is saved in 
#/nsls2/data/smi/legacy/results/data/2022_3/308251_Nam/ 



####################### 2022 Oct 25 
#
# RE(run_giwaxs_Kim(t=1), user_name = 'Kim_2022C3')
# #
# sample_list = [ 'B1s1_TMA_HQ_sam1' , 'B1s2_TMA_HQ_sam2' , 'B1s3_TMA_HQ_sam3' , 'B1s4_TMA_HQ_sam4' , 'B1s5_TMA_HQ_sam5',
# 		'B1s6_HfxZr1-xO2_sam1' , 'B1s7_HfxZr1-xO2_sam2' , 'B1s8_HfxZr1-xO2_sam3' , 'B1s9_HfxZr1-xO2_sam4' , 'B1s10_HfxZr1-xO2_sam5', 
# 		'B1s11_HfxZr1-xO2_sam6' , 'B1s12_HfxZr1-xO2_sam7' , 'B1s13_HfxZr1-xO2_sam8' , 'B1s14_HfxZr1-xO2_sam9' , 'B1s15_HfxZr1-xO2_sam10', 
# 	 	] 
# #pos = np.array([ 3, 11, 19, 26, 33,
# #		40, 48, 54, 61, 67, 
# #		73, 80, 86, 93, 101])
# #x_list =   -50000 + (pos-pos[0]) * 1000
# x_list = [-47000, -38500, -31000, -25000, -19000, 
#           -12000,  -6000,  1000, 7500, 14500,
#           22000, 30000, 36000, 44000, 52000]


####################### 2022 Oct 25 , night around 10:30 pm
# RE(run_giwaxs_Kim(t=1), user_name = 'Kim_2022C3')

sample_list = [ 'B2s1_HfxZr1-xO2_sam11' , 'B2s2_HfxZr1-xO2_sam12' , 'B2s3_HfxZr1-xO2_sam13' , 'B2s4_HfxZr1-xO2_sam14' , 'B2s5_HfxZr1-xO2_sam15',
		'B2s6_HfxZr1-xO2_sam16' , 'B2s7_HfxZr1-xO2_sam17' , 'B2s8_HfxZr1-xO2_sam18' , 'B2s9_HfxZr1-xO2_sam19' , 'B2s10_HfxZr1-xO2_sam20', 
		'B2s11_HfxZr1-xO2_sam21' , 'B2s12_HfxZr1-xO2_sam22' , 'B2s13_HfxZr1-xO2_sam23' , 'B2s14_HfxZr1-xO2_sam24' , 'B2s15_HfxZr1-xO2_sam25', 
	 	] 

# pos = np.array([ 4, 12, 20, 26, 33,
# 		42, 49, 56, 63, 70, 
# 		77, 83, 90, 96, 102])
#x_list =   -48100 + (pos-pos[0]) * 1000

x_list = [-48100, -41800, -35600, -29400, -22800, -15600, #1-6
         -8600, -2000, 5600, 13000, 21500, 29000, 35000, #7-13, 
          43000,  50500  #14, 15   
]



#pos = np.array(  [   ]) 
#x_list =   -50300 + (pos-pos[0]) * 1000


smi = SMI_Beamline()

def alignement_gisaxs(angle=0.15):        
        sample_id(user_name='test', sample_name='test')
        det_exposure_time(0.3, 0.3)        
        smi = SMI_Beamline()
        yield from smi.modeAlignment(technique='gisaxs')        
        # Set direct beam ROI
        yield from smi.setDirectBeamROI()
        # Scan theta and height
        yield from align_gisaxs_height(500, 21, der=True)
        yield from align_gisaxs_th(1.5, 27)
        #yield from align_gisaxs_height(300, 11, der=True)
        #yield from align_gisaxs_th(0.5, 16)        
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
        yield from smi.modeMeasurement()


def mov_sam(  i  ):
    i -=1
    px = x_list[i]       
    RE(  bps.mv(piezo.x, px) )
    print('Move to pos=%s for sample:%s...'%(i+1, sample_list[i] ))

def check_sample_loc( sleep = 5 ):
    ks = sample_list
    i = 1
    for k in ks: 
        mov_sam( i )
        time.sleep( sleep  )
        i += 1

 
def movx( dx ):
    RE(  bps.mvr(piezo.x, dx) )    
def movy( dy ):
    RE( bps.mvr(piezo.y, dy) )
def get_posxy( ):
    return  round( piezo.x.user_readback.value, 2 ),round( piezo.y.user_readback.value , 2 )

def move_waxs( waxs_angle=8.0):
    RE(  bps.mv(waxs, waxs_angle)    )
       
def move_waxs_off( waxs_angle=8.0 ):
    RE(  bps.mv(waxs, waxs_angle)    )
def move_waxs_on( waxs_angle=0.0 ):
    RE(  bps.mv(waxs, waxs_angle)  )

def mov_sam_dict( pos ):    
    px,py = pxy_dict[ pos ]
    RE(  bps.mv(piezo.x, px) )
    RE(  bps.mv(piezo.y, py) )
    sample = sample_dict[pos]  
    print('Move to pos=%s for sample:%s...'%(pos, sample ))
    RE.md['sample']  = sample 
       
       
       



#Align GiSAXS sample
import numpy as np
      
username = 'Kim_2022C3'
user_name = 'Kim_2022C3'



def snap_waxs( t=0.1  ):     
    dets=  [  pil900KW ] 
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(t)
    yield from( bp.count(dets, num=1) )
    
def snap_saxs( t=0.1  ):     
    dets=  [  pil1M ] 
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(t)
    yield from( bp.count(dets, num=1) )






def run_giwaxs_Kim(t=1, username = username ): 
    '''     RE( run_giwaxs_Kim() )      '''


    # define names of samples on sample bar     
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'
    angle_arc = np.array([0.05, 0.08, 0.10, 0.15, 0.2, 0.3 ]) # incident angles 
    waxs_angle_array = np.array( [ 0, 10, 20, 40, 60,  ] ) # 4*3.14/(12.39842/16.1)*np.sin((7*6.5+3.5)*3.14/360) = 6.760 A-1. 
    #waxs_angle_array = np.array( [60,  ] ) # 4*3.14/(12.39842/16.1)*np.sin((7*6.5+3.5)*3.14/360) = 6.760 A-1. 
    #waxs_angle_array = np.array( [ 0, 10, 20, 40   ] ) 
    #waxs_angle_array = np.array( [ 0, 10, 20, 40, 60,  ] )[::-1] # 4*3.14/(12.39842/16.1)*np.sin((7*6.5+3.5)*3.14/360) = 6.760 A-1.
    #dets = [pil300KW, pil1M] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]
    max_waxs_angle = np.max(  waxs_angle_array )  
    x_shift_array = np.linspace(-1000, 1000, 3) # measure at a few x positions
    inverse_angle = False
    cts = 0
    for ii, (x, sample) in enumerate(zip(x_list,sample_list)): #loop over samples on bar
        yield from bps.mv(piezo.x, x) #move to next sample  
        #yield from  bps.mv(piezo.y, 4000  ) #move y to 4000

        yield from alignement_gisaxs(0.1) #run alignment routine
        TH = piezo.th.position 
        YH = piezo.y.position 

        th_meas = angle_arc + piezo.th.position 
        th_real = angle_arc	         
        x_pos_array = x + x_shift_array
        if inverse_angle:
            Waxs_angle_array = waxs_angle_array[::-1]
        else:
            Waxs_angle_array = waxs_angle_array            
        for waxs_angle in Waxs_angle_array: # loop through waxs angles
            det_exposure_time(t,t) 
            yield from bps.mv(waxs, waxs_angle)
            dets = [ pil900KW] #, pil300KW   ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]    
            # if waxs_angle == max_waxs_angle:
            #     dets = [ pil900KW, pil300KW , pil1M ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M] 
            #     print( 'Meausre both saxs and waxs here for w-angle=%s'%waxs_angle )
            # else:
            #     dets = [pil900KW, pil300KW ]   
            for j, x_meas in enumerate( x_pos_array) : # measure at a few x positions
                yield from bps.mv(piezo.x, x_meas)                 
                for i, th in enumerate(th_meas): #loop over incident angles
                    yield from bps.mv(piezo.th, th)  
                    if inverse_angle:
                        name_fmt = '{sample}_{th:5.4f}deg_waxsN{waxs_angle:05.2f}_x{x:05.2f}_expt{t}s_sid{scan_id:08d}'
                    else:
                        name_fmt = '{sample}_{th:5.4f}deg_waxsP{waxs_angle:05.2f}_x{x:05.2f}_expt{t}s_sid{scan_id:08d}'   
                    sample_name = name_fmt.format(
                               sample = sample, th=th_real[i], waxs_angle=waxs_angle, x=x_meas, t=t, scan_id=RE.md['scan_id'])  
                    sample_id(user_name=  username , sample_name=sample_name)                     
                    print(f'\n\t=== Sample: {sample_name} ===\n')   
                    #yield from bp.scan(dets, energy, e, e, 1)
                    #yield from bp.scan(dets, waxs, *waxs_arc)
                    print( dets )
                    yield from bp.count( dets, num=1)
                    if waxs_angle == max_waxs_angle: #60: #max_waxs_angle:  #for small angle measurements
                        if i in [ 2, 5]: # , 2, 5] : 
                            if j in [1]:
                                t2 = 60
                                det_exposure_time(t2, t2) 
                                if inverse_angle:
                                    name_fmt = '{sample}_{th:5.4f}deg_waxsN{waxs_angle:05.2f}_x{x:05.2f}_expt{t}s_sid{scan_id:08d}'
                                else:
                                    name_fmt = '{sample}_{th:5.4f}deg_waxsP{waxs_angle:05.2f}_x{x:05.2f}_expt{t}s_sid{scan_id:08d}'   
                                sample_name = name_fmt.format(
                                        sample = sample, th=th_real[i], waxs_angle=waxs_angle, x=x_meas, t=t2, scan_id=RE.md['scan_id'])  
                                sample_id(user_name=  username , sample_name=sample_name)                     
                                print(f'\n\t=== Sample: {sample_name} ===\n')   

                                yield from bp.count( [ pil1M ], num=1)  #measure SAXS
                    det_exposure_time(t,t)             

        yield from  bps.mv(piezo.y, YH  )  
        yield from  bps.mv(piezo.th, TH  )        
 

                    #print( 'HERE#############')                    
        inverse_angle = not inverse_angle 
        cts += 1
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)













def run_giwsaxs( x_list=x_list, sample_list=sample_list,   t=1, username =  username, 
                 inc_angles= np.array([0.05, 0.08, 0.10, 0.15, 0.2, 0.3 ]),
                   waxs_angles = np.array( [ 0, 10, 20, 40, 60,  ] ) ,
                  x_shift_array = np.linspace(-1000, 1000, 3)  ,     YPOS = {   },  ThPOS = {   },
                  saxs_on=True, align=True,  T=25    ): 
    '''     RE( run_giwaxs() )      '''


    # define names of samples on sample bar     
    assert len(x_list) == len(sample_list), f'Sample name/position list is borked'
    inc_angles = np.array( inc_angles )# incident angles 
    th_real = inc_angles    
    waxs_angles = np.array( waxs_angles )# arc waxs angles
    # 4*3.14/(12.39842/16.1)*np.sin((7*6.5+3.5)*3.14/360) = 6.760 A-1
    x_shift_array = np.array( x_shift_array )
    max_waxs_angle = np.max(  waxs_angles )       
    inverse_angle = False
    cts = 0
    for ii, (x, sample) in enumerate(zip(x_list,sample_list)): #loop over samples on bar
        yield from bps.mv(piezo.x, x) #move to next sample          
        if align:
            #RE( bps.mv(piezo.th, 0 ) )
            yield from alignement_gisaxs(0.15) #run alignment routine
            YPOS[ii] =  piezo.y.position
            ThPOS[ii] =  piezo.th.position
            print( YPOS, ThPOS )
        else:
            yield from bps.mv(piezo.y, YPOS[ii] )   
            yield from bps.mv(piezo.th, ThPOS[ii] )   

        TH = ThPOS[ii]   #piezo.th.position         
        th_meas = inc_angles + ThPOS[ii]   #piezo.th.position          


        det_exposure_time(t,t) 
        x_pos_array = x + x_shift_array
        if inverse_angle:
            Waxs_angles = waxs_angles[::-1]
        else:
            Waxs_angles = waxs_angles            
        for waxs_angle in Waxs_angles: # loop through waxs angles
            yield from bps.mv(waxs, waxs_angle)
            dets = [ pil900KW, pil300KW   ] # waxs, maxs, saxs = [pil300KW, rayonix, pil1M]    
            # if waxs_angle == max_waxs_angle:
            #     if saxs_on:
            #         dets = [ pil900KW, pil1M, pil300KW  ] 
            #     else:
            #         dets = [ pil900KW ,   pil300KW  ]              
            #     print( 'Meausre both saxs and waxs here for w-angle=%s'%waxs_angle )
            # else:
            #     dets = [pil900KW , pil300KW  ] 


            for x_meas in x_pos_array: # measure at a few x positions
                yield from bps.mv(piezo.x, x_meas)                 
                for i, th in enumerate(th_meas): #loop over incident angles
                    yield from bps.mv(piezo.th, th)  
                    if inverse_angle:
                        name_fmt = '{sample}_{th:5.4f}deg_waxsN{waxs_angle:05.2f}_x{x:05.2f}_y{y:05.2f}_z{y:05.2f}_det{saxs_z:05.2f}m_expt{t}s_T{T}_sid{scan_id:08d}'                       
                    else:
                        name_fmt = '{sample}_{th:5.4f}deg_waxsP{waxs_angle:05.2f}_x{x:05.2f}_y{y:05.2f}_z{y:05.2f}_det{saxs_z:05.2f}m_expt{t}s_T{T}_sid{scan_id:08d}'
                    sample_name = name_fmt.format(
                            sample = sample, th=th_real[i], waxs_angle=waxs_angle,  x=np.round(piezo.x.position,2), y=np.round(piezo.y.position,2), 
                            z=np.round(piezo.z.position,2),  saxs_z=np.round(pil1m_pos.z.position,2), 
                            t=t, T=T, scan_id=RE.md['scan_id'])  
                    sample_id(user_name=  username , sample_name=sample_name)                     
                    print(f'\n\t=== Sample: {sample_name} ===\n')   
                    #yield from bp.scan(dets, energy, e, e, 1)
                    #yield from bp.scan(dets, waxs, *waxs_arc)
                    print( dets )
                    yield from bp.count( dets, num=1)

                    if waxs_angle == max_waxs_angle:  #for small angle measurements
                        if i in [ 0, 2, 5] : 
                            if x_mean in [0]:
                                det_exposure_time(60,60) 
                                yield from bp.count( [ pil1M ], num=1)  #measure SAXS
                    det_exposure_time(t,t)             




                    #print( 'HERE#############')                    
        inverse_angle = not inverse_angle 
        cts += 1
    yield from bps.mv(piezo.th, TH )     
    sample_id(user_name='test', sample_name='test')
    det_exposure_time(0.5)




  




