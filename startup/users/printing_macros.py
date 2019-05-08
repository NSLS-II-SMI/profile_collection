# how to reload macro: %run -i /XF11ID/analysis/2018_3/petrash/printing_macros.py
print("re-loaded printing_macros.py")

# define PVs to monitor status pv, communicate triggers, etc.
# Note: these PVs are hosted on the beamline ioc and will not be available in the lab...
try:
    pressure_pv = 'XF:11ID-CT{ES:1}ai1'
    caget(pressure_pv)
    monitor_pv = 'XF:11ID-CT{ES:1}bi1'   #xray_eye_printer.roi3.enable.put(1) # set up monitor condition
    caget(monitor_pv)
    ready_for_trigger_pv = 'XF:11ID-CT{ES:1}bi2'     #xray_eye_printer.roi2.enable.put(1) # this function is ready for triggers
    caget(ready_for_trigger_pv)
    trigger_signal_pv = 'XF:11ID-CT{ES:1}bi3'    #xray_eye_printer.roi1.enable.put(0) #
    caget(trigger_signal_pv)
    print('Successfully defined and connected PVs for status and trigger signals.')
except:
    print('Failed defining PVs for status and trigger signals.')
    # should define local PVs for lab use...


# acquisition macros:
def dynamics_in_nozzle():
    h_top_printer = -3.5
    h_top_diff = -1.86168  # Kapton tape
    #h_top_diff = -2.16  # 200 Si wafer on double sided sticky tape
    h_bot_printer = 3.0
    h_bot_diff = -2.16015
    h_top_total=h_top_printer+h_top_diff
    h_bot_total=h_bot_printer+h_bot_diff
    RE.md['substrate']='Kapton 50um'
    RE.md['nozzle']='Nordson pn 7005009'
    RE.md['nozzle_diameter']=580
    printer_z_pos = caget('alexHost:smaract2Mtr.RBV')
    if printer_z_pos < -.5 and printer_z_pos > -9.:  # printing on top platform
        RE.md['platform']='top'
        RE.md['height']= h_top_total - caget('alexHost:smaract2-ax3Mtr.RBV')-diff.yh.user_readback.value
    elif printer_z_pos < 9.5 and printer_z_pos > .5:  # printing on bottom platform
        RE.md['height']= h_bot_total - caget('alexHost:smaract2-ax3Mtr.RBV')-diff.yh.user_readback.value
        RE.md['platform']='bottom'
    else:
        RE.md['height']='N.A.'
        RE.md['platform']='N.A.'
    function_triggered(trigger_num=1)
    
def long_relaxation_multi_substrate():
  sample_dict={'bare Si wafer':{'xy':[-7.1,0.5685]},'hydrophobic Si wafer':{'xy':[7.9,0.5633]},'Si wafer + crystalbond':{'xy':[22.9,.5591]}}
  heights=[.05,.42,.235]
  for i in range(10):
    RE(mvr(diff.xh,-.03))
    for k in list(sample_dict.keys()):
      print('taking data for:'+k)
      caput('alexHost:smaract2-ax2Mtr.VAL',sample_dict[k]['xy'][0])
      for h in heights:
        RE(mv(diff.yh,sample_dict[k]['xy'][1]-h))
        RE(mv(diff.yh,sample_dict[k]['xy'][1]-h)) # moving twice reduces the deadband...
        RE.md['substrate']=k
        RE.md['nozzle']='Nordson pn 7005009'
        RE.md['nozzle_diameter']=580
        RE.md['platform']='top'
        att2.set_T(.0068)
        series(expt=.25,imnum=1000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True,comment='long relaxation multi substrate: '+k+'  height='+str(h)+' .25s 1000 T=.0068, run no.'+str(i)+' '+RE.md['sample'])

        

def second_layer(sleep_time):
     RE(sleep(sleep_time))
     RE.md['sleep time between layer deposition']=sleep_time
     cur_printer_y=caget('alexHost:smaract2-ax3Mtr.RBV')
     caput('alexHost:smaract2-ax3Mtr.VAL',cur_printer_y-.580,wait=True)
     caput('alexHost:smaract2-ax4Mtr.VELO',0)
     caput('alexHost:smaract2-ax4Mtr.VAL',6)
     #caput('alexHost:smaract2-ax4Mtr.VELO',0)
     caput('alexHost:smaract2-ax4Mtr.VELO',.5)
     RE(mvr(diff.yh,.58))
     RE(movr(diff.xh,-.05))
     att2.set_T(.01)
     series(expt=.05,imnum=3000,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='ins-situ slow .05s 3000 T=.01 '+RE.md['sample'])
     RE(movr(diff.xh,-.05))
     att2.set_T(.01)
     series(expt=.05,imnum=3000,OAV_mode='single',feedback_on=True,analysis='phi', auto_compression=True, comment='post_printing1 .05s 3000 T=.01 '+RE.md['sample'])
     print('Waiting for 300 s.')
     RE(sleep(300))
     RE(movr(diff.xh,-.05))
     att2.set_T(.01)
     series(expt=.05,imnum=3000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True, comment='post_printing2 .05s 3000 T=.01 '+RE.md['sample'])	 
     RE(movr(diff.xh,.1))
     a=RE.md.pop('sleep time between layer deposition')
    
def post_printing():
    print('MAKE SURE diff.yh POSISION WAS SET TO 0 AFTER HEIGHT SCAN!!!')
    pos=[.02,0.07,.12,.2,.27,.37,.47]
    x_count=0
    for i in pos:
        print('taking data: 0.05sx2000fr for height'+str(i))
        RE(mvr(diff.xh,-.03));x_count=x_count+.03
        RE(mv(diff.yh,-1*i))
        RE(mv(diff.yh,-1*i))
        att2.set_T(.036)
        RE.md['height']=i
        series(expt=.05,imnum=5000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True,comment='post_printing_I at h='+str(i)+' .05s 5000 T=.036 '+RE.md['sample'])
    for i in pos:
        print('taking data: 0.05sx800fr for height'+str(i))
        RE(mvr(diff.xh,-.03));x_count=x_count+.03
        RE(mv(diff.yh,-1*i))
        RE(mv(diff.yh,-1*i))
        att2.set_T(.0068)
        RE.md['height']=i
        series(expt=.25,imnum=1000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True,comment='post_printing_II at h='+str(i)+' .25s 1000 T=.0068 '+RE.md['sample'])
    for i in pos:
        print('taking data: 0.05sx1200fr for height'+str(i))
        RE(mvr(diff.xh,-.03));x_count=x_count+.03
        RE(mv(diff.yh,-1*i))
        RE(mv(diff.yh,-1*i))
        att2.set_T(.0068)
        RE.md['height']=i
        series(expt=.25,imnum=1000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True,comment='late_post_printing_III at h='+str(i)+' .25s 2000 T=.0068 '+RE.md['sample'])
    RE(mvr(diff.xh,x_count))
    
def set_abs_plat_height():
    """
    getting printer3d.Y and diff.yh position (after scanning platform height and moving to half attenuation position)
    storing value printer3d.Y + diff.yh (=absolute platform height) as RE.md['platform_height'] for calculation of platform height in experiment
    """
    h_printer=caget('alexHost:smaract2-ax3Mtr.VAL')
    h_diff=diff.yh.user_readback.value
    RE.md['platform_height']=h_printer+h_diff
    
def get_plat_height():
    """
    calculate current distance between platform and beam, using RE.md['platform_height']
    """
    h=RE.md['platform_height'] - (caget('alexHost:smaract2-ax3Mtr.RBV')+diff.yh.user_readback.value)
    print('current height of the printing platform is: '+str(h))
    return h
    
def mov_plat_height(height):
    """
    move platform to desired position (height) with respect to the beam
    """
    cur_h=get_plat_height()
    rel_height=cur_h-height
    #print('RE(movr(diff.yh,%s))'%rel_height)
    RE(movr(diff.yh,rel_height))
    sh=diff.yh.user_readback.value
    RE(mv(diff.yh,sh))
    print('requested platform height: '+str(height)+'  current height: '+str(get_plat_height()))


def printing_wall_bottomlayer(scantype=None):
    '''
    '''
    

def printing_and_recovery(scantype = None):

    '''
    scantype = 'slow':
        att2.set_T(0.01)
        series(expt=.05,imnum=3000,OAV_mode='movie',feedback_on=True,analysis='phi',comment='in-situ printing '+RE.md['sample'])
    	two post-print scans, moving 50 micron in between and also wait for 5 min....
   
    scantype = 'fast':
        att2.set_T(1)
        series(expt=.00134,imnum=4000,OAV_mode='movie',feedback_on=True,analysis='phi',comment='in-situ printing '+RE.md['sample'])
    '''

    if scantype is None:
    	print('please specify scantype, fast or slow')
    #RE.md['substrate']='Si-wafer'
    RE.md['substrate']='Crystallbond'
    #RE.md['substrate']='Au on Si wafer 500um'
    RE.md['nozzle']='Nordson pn 7005009'
    RE.md['nozzle_diameter']=580
    printer_z_pos = caget('alexHost:smaract2Mtr.RBV')
    if printer_z_pos < -2. and printer_z_pos > +2.:  # printing on top platform
        RE.md['platform']='top'
        #RE.md['height']= h_top_total - caget('alexHost:smaract2-ax3Mtr.RBV')-diff.yh.user_readback.value
    elif printer_z_pos < 10. and printer_z_pos > 6.:  # printing on bottom platform
        #RE.md['height']= h_bot_total - caget('alexHost:smaract2-ax3Mtr.RBV')-diff.yh.user_readback.value
        RE.md['platform']='bottom'
    else:
        RE.md['height']='N.A.'
        RE.md['platform']='N.A.'
    RE.md['height']=RE.md['platform_height'] - caget('alexHost:smaract2-ax3Mtr.RBV')-diff.yh.user_readback.value   # scan platform height for each measurement
    monitor_trigger(trigger_num=1, scantype = scantype)  # in-situ printing!!! This is executing series 'triggered_series'!
    
    x_count=0
    if scantype == '4m' or scantype == 'double_layer': 
    # post printing series below....change to your hearts content
	    print('Sleeping for 4 min')
	    RE(sleep(240))
	    RE(movr(diff.xh,-.05))
	    x_count=x_count+.05
	    att2.set_T(.036)
	    series(expt=.05,imnum=1000,OAV_mode='single',feedback_on=True,analysis='phi', auto_compression=True, comment='post_printing1 .05s 1000 T=.036 '+RE.md['sample'])
	    print('Sleeping for 4 min')
	    RE(sleep(240))
	    RE(movr(diff.xh,-.05))
	    x_count=x_count+.05
	    att2.set_T(.036)
	    series(expt=.05,imnum=1000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True, comment='post_printing2 .05s 1000 T=.036 '+RE.md['sample'])
	    print('Sleeping for 4 min')
	    RE(sleep(240))
	    RE(movr(diff.xh,-.05))
	    x_count=x_count+.05
	    att2.set_T(.036)
	    series(expt=.05,imnum=1000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True, comment='post_printing3 .05s 1000 T=.036 '+RE.md['sample'])
	    #series(expt=.25,imnum=1000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True, comment='post_printing3 .25s 1000 T=.0068 '+RE.md['sample'])
	    #RE(movr(diff.xh,.1))
    elif scantype == 'Si_mono':
        RE(movr(diff.xh,-.05))
        x_count=x_count+.05
        att2.set_T(1)
        series(expt=.00134,imnum=2000,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='post_printing_1 1.34ms 2000 T=1 '+RE.md['sample'])
        RE(movr(diff.xh,-.05))
        x_count=x_count+.05
        att2.set_T(.036)
        series(expt=.050,imnum=1000,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='post_printing_2 50ms 1000 T=0.036 '+RE.md['sample'])
        print('Sleeping for 2 min')
        #RE(sleep(120))
        #att2.set_T(1)
        #series(expt=.00134,imnum=2000,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='post_printing_2 1.34ms 2000 T=1 '+RE.md['sample'])
        print('Sleeping for 3 min')
        RE(sleep(180))
        att2.set_T(.036)
        series(expt=.05,imnum=1000,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='post_printing_3 50ms 1000 T=0.036 '+RE.md['sample'])
        #print('Sleeping for 10 min')
        #RE(sleep(600))
        #att2.set_T(.0068)
        #series(expt=.25,imnum=1000,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='post_printing_4 250ms 1000 T=0.0068 '+RE.md['sample'])
	

    caput('XF:11IDB-BI{Cam:10}cam1:NumImages',1)
    RE(count([OAV]),Measurement='single OAV image at end of last run') 
    RE(movr(diff.xh,x_count))
    #if scantype is '500k':
    #    RE(movr(diff.xh,0.05))
   


def triggered_series(scantype = None):   # gets executed by monitor_trigger!

    RE.md['speed']= caget('alexHost:smaract2-ax4Mtr.VELO')
    RE.md['pressure']=  caget(pressure_pv)
    #get_abs_plat_height()
    
    print(scantype)
    # change series below: this is insitu printing
    if scantype is 'test':
        series(expt=.01,imnum=100,comment='just testing something') 
    if scantype is 'Si_mono':
        att2.set_T(1)
        series(expt=.00134,imnum=5000,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='in-situ printing 1.34ms T=1 5000fr '+RE.md['sample'])
    if scantype is 'first_layer':
        att2.set_T(0.0068)
        series(expt=.05,imnum=100,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='in-situ printing slow short (first layer) '+RE.md['sample'])
    if scantype is '4m':
        att2.set_T(.19)
        series(expt=.02,imnum=1000,OAV_mode='movie',feedback_on=True,analysis='phi',auto_compression=True,comment='in-situ printing fast 20ms 1k fr T=.19 '+RE.md['sample'])
    elif scantype is 'double_layer':
        delay=caget('XF:11ID-CT{ES:1}ai2')
        RE.md['delay between double layer depositions [s]']=delay
        att2.set_T(.19)
        series(expt=.02,imnum=1000,OAV_mode='movie',feedback_on=True,analysis='phi',auto_compression=True,comment='in-situ printing fast 20ms 1k fr T=.19 DOUBLE LAYER '+RE.md['sample'])
        cc=RE.md.pop('delay between double layer depositions [s]')
    elif scantype is 'fast':
        att2.set_T(1)
        series(expt=.00134,imnum=6000,OAV_mode='movie',feedback_on=True,analysis='phi', auto_compression=True, comment='in-situ printing fast '+RE.md['sample'])
#    elif scantype is '500k':
#        att2.set_T(1)
#        #series(expt=.00012,imnum=4000,OAV_mode='movie',feedback_on=True,analysis='phi',comment='printing 100um inside of nozzle '+RE.md['sample'])
#        series(det='eiger500k',expt=.00012,imnum=40000,OAV_mode='movie',feedback_on=True,analysis='phi',auto_compression=True,comment='fast 500k series '+RE.md['sample'])
#    elif scantype is 'in_nozzle_1_mm':
#        att2.set_T(1)
#        #series(expt=.00134,imnum=4000,OAV_mode='movie',feedback_on=True,analysis='phi',comment='printing 100um inside of nozzle '+RE.md['sample'])
#        series(det='eiger500k',expt=.00012,imnum=10000,OAV_mode='movie',feedback_on=True,analysis='phi',auto_compression=True,comment='printing 1 mm inside of nozzle fast 500k '+RE.md['sample'])
    else:
    	print('please sepcify scantype!')
    


def reset_after_printing(platform_move,printhead_start_pos):
    """
    platform_move: relative negative movement of X_platform to available printing location (note: should be larger than printhead_move)
    printhead_move: relative negative movement of printhead to starting dispensing position (note: should equal travel+travel_after_pump_stop "from timed_move")
    """
    curr_plat_pos=caget('alexHost:smaract2-ax2Mtr.RBV')
    caput('alexHost:smaract2-ax2Mtr.VAL',curr_plat_pos+platform_move,wait=True)
    #curr_printhead_pos=caget('alexHost:smaract2-ax4Mtr.RBV')
    caput('alexHost:smaract2-ax4Mtr.VELO',0)
    caput('alexHost:smaract2-ax4Mtr.VAL',printhead_start_pos,wait=True)

def fluorescent_screen_in():
    """
    moving 3D printer and diffractometer to pre-defined position:
    fluorescent screen in the beam
    """
    caput('alexHost:smaract2Mtr.VAL',-8.2)  #3d printer Z
    caput('alexHost:smaract2-ax2Mtr.VAL',52.5)	# 3d printer X_platform
    caput('alexHost:smaract2-ax3Mtr.VAL',2.198)   # 3d printer Y
    caput('alexHost:smaract2-ax4Mtr.VAL',0)	# 3d printer X_printhead1
    RE(mov(diff.xh,.3,diff.yh,-8.86))
    caput('XF:11IDB-BI{Cam:10}cam1:AcquirePeriod',0.4)
    caput('XF:11IDB-BI{Cam:10}cam1:AcquireTime',0.4)

def printer_origin():
    """
    moving 3D printer and diffractometer to pre-defined position:
    bottom platform at beam height, nozzle centered on bottom platform and with the beam
    """
    caput('alexHost:smaract2Mtr.VAL',5.)  #3d printer Z
    caput('alexHost:smaract2-ax2Mtr.VAL',-57.5)	# 3d printer X_platform
    caput('alexHost:smaract2-ax3Mtr.VAL',2.2)   # 3d printer Y
    caput('alexHost:smaract2-ax4Mtr.VAL',0)	# 3d printer printhead
    RE(mov(diff.xh,.3,diff.yh,-8.86))


def scanning_wafer_height(detector='eiger4m'):
    """
    detector = 'eiger4m','eiger500k'
    """
    goto_beamline_pos(position_key='4m_in', interactive=False)
    att.set_T(1E-4)
    if detector == 'eiger4m':
        det=[eiger4m_single]
        caput('XF:11IDB-ES{Det:Eig4M}cam1:AcquireTime',.1,wait=True)
        caput('XF:11IDB-ES{Det:Eig4M}cam1:NumImages',1,wait=True)
        caput('XF:11IDB-ES{Det:Eig4M}cam1:NumTriggers',1,wait=True)
    elif detector == 'eiger500k':
        det=[eiger500k_single]
        caput('XF:11IDB-ES{Det:Eig500K}cam1:AcquireTime',.1,wait=True)
        caput('XF:11IDB-ES{Det:Eig500K}cam1:NumImages',1,wait=True)
        caput('XF:11IDB-ES{Det:Eig500K}cam1:NumTriggers',1,wait=True)
    else:
        print('error: detector not defined!!')
    # make sure we're ready for scanning:
    att2.set_T(1)
    #caput('XF:11IDB-ES{Det:Eig4M}cam1:AcquireTime',.1,wait=True)
    #caput('XF:11IDB-ES{Det:Eig4M}cam1:NumImages',1,wait=True)
    #caput('XF:11IDB-ES{Det:Eig4M}cam1:NumTriggers',1,wait=True)
    RE(movr(saxs_bst.y1,5))
    RE(dscan(det,diff.yh,-.1,.1,25))
    ps()
    RE(mov(diff.yh,ps.cen))
    RE(mov(diff.yh,ps.cen))
    RE(mov(saxs_bst.y1,-100.6507))
    if saxs_bst.y1.user_readback.value >= -100.85 and saxs_bst.y1.user_readback.value < -100.45:
        (print('beamstop is back!'))
        att.set_T(1)
    else:
            raise scan_Exception('BEAMSTOP NOT IN CORRECT POSITION!!! DO NOT REMOVE ATTENUATORS!')
    print('height is '+str(diff.yh.user_readback.value))

class scan_Exception(Exception):
    pass

def nozzle_map_old():
    att2.set_T(1)
    x_c=diff.xh.user_readback.value
    for i in [-280,-250,-220,-150,-100,-50,0,100,150,200,280]:
      print('taking data for position: '+str(i))
      RE(mv(diff.xh,x_c+i/1000))
      RE.md['speed']= caget('alexHost:smaract2-ax4Mtr.VELO')
      RE.md['pressure']=  caget(pressure_pv)
      series(det='eiger500k',expt=.00012,imnum=12000,OAV_mode='movie',feedback_on=True,analysis='phi',auto_compression=True,comment='printing 250um into nozzle position: '+str(i)+'um '+RE.md['sample'])
                

def nozzle_map(xc):
    RE(mv(diff.xh,xc))
    att2.set_T(1)
    x_c=diff.xh.user_readback.value
    # [-280,-250,-220,-150,-100,-50,0,100,150,200,280]:
    for i in [0,50,100,150,200,280]:#,-150,-100,-50,0,100,150,200,280]:
      print('taking data for position: '+str(i))
      RE(mv(diff.xh,x_c+i/1000))
      RE.md['nozzle_x_position']=i
      RE.md['speed']= caget('alexHost:smaract2-ax4Mtr.VELO')
      RE.md['platform_speed']= caget('alexHost:smaract2-ax2Mtr.VELO')
      RE.md['pressure']=  caget(pressure_pv)
      series(det='eiger500k',expt=.00012,imnum=10000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True,comment='printing 250um into nozzle position: '+str(i)+'um '+RE.md['sample'])
      #series(det='eiger500k',expt=.00012,imnum=12000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True,comment='testing printing in nozzle '+RE.md['sample'])
    RE.md.pop('nozzle_x_position')
    RE.md.pop('platform_speed')

def monitor_trigger(trigger_num=-1, scantype = None):
    """
    just for testing: path this function and have it executed at a specified trigger location
    option: trigger_num: -1 -> will never terminate itself, 5: will terminate after being triggered 5 times
    """
    caput(monitor_pv,1,wait=True) #xray_eye_printer.roi3.enable.put(1) # set up monitor condition
    caput(ready_for_trigger_pv,1,wait=True) #xray_eye_printer.roi2.enable.put(1) # this function is ready for triggers
    caput(trigger_signal_pv,0,wait=True) #xray_eye_printer.roi1.enable.put(0) # this function starts first: make sure trigger signal is reset
    #xray_eye_printer.roi3.enable.put(1) # set up monitor condition
    #caput('XF:MOBILE-BI{Mir:1}ROI3:EnableCallbacks',1)
    #xray_eye_printer.roi2.enable.put(1) # this function is ready for triggers
    #caput('XF:MOBILE-BI{Mir:1}ROI2:EnableCallbacks',1)
    #xray_eye_printer.roi1.enable.put(0) # this function starts first: make sure trigger signal is reset
    #caput('XF:MOBILE-BI{Mir:1}ROI1:EnableCallbacks',0)
    trigger_count=0
    while  caget(monitor_pv) == 1:
        if  caget(trigger_signal_pv) == 1: # trigger signal to execute
            caput(ready_for_trigger_pv,0) # that's the sign to the outside world that this function is busy
            print('this is "function_triggered"! \nGoing to trigger detector...')
            trigger_count=trigger_count=1
            #series(expt=.1,imnum=100,comment='testing eiger triggering from m1 session')
            triggered_series(scantype = scantype)
            print('function_triggered successfully executed...waiting for next call.')
            caput(trigger_signal_pv,0) # reset trigger signal
            caput(ready_for_trigger_pv,1) # that's the sign that this function is ready for the next call
            if trigger_num != -1 and trigger_count >= trigger_num:
                caput(monitor_pv,0)
                print('number of requested triggers reached, stopping monitoring...')
            else:
                pass
        RE(sleep(.5))
        print('monitoring trigger signal')

def new_spot():
    if diff.xh.user_readback.value > 2.1:
    	RE(mv(diff.xh,1.))
    	RE(mvr(diff.yh,-.025))
    RE(mvr(diff.xh,.025))
    

def curing_series(repeats=10,temperature='170C'):
    RE(mv(diff.xh,1.0));RE(mvr(diff.xh,-.025))
    for i in range(repeats):
        new_spot()
        att2.set_T(1)
        RE(count([eiger1m_single]),Measurement='WAXS single image '+temperature+' ' +RE.md['sample'])
        new_spot()
        series(expt=.00134,imnum=500,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True, comment=temperature+' .00134s 500 T=1 repeat: '+str(i)+RE.md['sample'])
        new_spot()
        att2.set_T(.19);series(expt=.01,imnum=500,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True, comment=temperature+' .01s 500 T=.19 repeat: '+str(i)+RE.md['sample'])    
        new_spot()
        att2.set_T(1)
        RE(count([eiger1m_single]),Measurement='WAXS single image '+temperature+' '+RE.md['sample'])
        new_spot()
        att2.set_T(.038);series(expt=.05,imnum=1000,OAV_mode='single',feedback_on=True,analysis='phi',auto_compression=True, comment=temperature+' .05s 1000 T=.19 repeat: '+str(i)+RE.md['sample']) 
    
    set_temperature(60)
