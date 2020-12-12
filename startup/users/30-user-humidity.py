import time
from ophyd import Device



def readHumidity(temperature=25, voltage_supply=5, verbosity=3):        

    voltage_out = moxa_out.ch8_read.value
    corr_voltage_out = voltage_out * (5.0 / voltage_supply)

    coeff_offset = 0.816887
    coeff_slope = 0.028813

    sensor_RH = (corr_voltage_out - coeff_offset) / coeff_slope

    true_RH = sensor_RH / (1.0546 - 0.00216 * temperature)      # T in [degC]
    
    if verbosity >= 3:
        print('Raw sensor RH = {:.3f} pct.'.format(sensor_RH))
        print('T-corrected RH = {:.3f} pct at {:.3f} degC.'.format(true_RH, temperature))
    return true_RH


def setDryFlow(voltage=None):
    if voltage==None or voltage>5 or voltage <0:
        print('Input voltage betwee 0 and 5V')
    moxa_in.ch1_sp.put(0)
    time.sleep(0.5)
    moxa_in.ch1_sp.put(voltage)

def setWetFlow(voltage=0):
    if voltage==None or voltage>5 or voltage <0:
        print('Input voltage betwee 0 and 5V')
    moxa_in.ch2_sp.put(0)
    time.sleep(0.5)
    moxa_in.ch2_sp.put(voltage)



'''

humidity list


humidity,    wet,     dry         2nd day, recheck
48           3         3

71           3         2.5                      
80           3         2.4/2.35        ###        

56           3         2.8  
60           3         2.7              ### 

43           3         3.3              
41           3         3.4              
40           3         3.45/3.6       ### 

20       2.5/2.4       3             ### 

humidity_list=[100, 80, 60,   40,  20, 0,100,0]
wetFlow_list= [ 5,  3,   3,   3,  2.5, 0, 5, 0]
dryFlow_list= [ 0, 2.35, 2.7, 3.6, 3,  5, 0, 5]
hol.alignSamples()
for ii in range(8):    
    hol1.setDryFlow(dryFlow_list[ii])
    hol1.setWetFlow(wetFlow_list[ii])
    post_to_slack('set to humidity  {}'.format(humidity_list[ii]))
    time.sleep(30*60)
    post_to_slack('start the measurement at humidity {}'.format(hol1.humidity(verbosity=0)))
    hol1.measureSamples()
'''
'''


humidity_list=[100,  75,   50,  25,   0,   100,0]
wetFlow_list= [ 5,   3,    3,   2.5,  0,    5, 0]
dryFlow_list= [ 0,  2.47,  3,    3,   5,    0, 5]
hol.alignSamples()
for ii in range(8):    
    hol1.setDryFlow(dryFlow_list[ii])
    hol1.setWetFlow(wetFlow_list[ii])
    post_to_slack('set to humidity  {}'.format(humidity_list[ii]))
    time.sleep(30*60)
    post_to_slack('start the measurement at humidity {}'.format(hol1.humidity(verbosity=0)))
    hol1.measureSamples()'''
