# E. Marino (UPenn, Murray)
# ref: Chopra, Clark
# 
# ======================================================================
#
# %run -i /home/xf12id/.ipython/profile_collection/startup/users/30-user-Marino.py
# RE(insitu_EM(t=1, name = 'insitu_S1_run1', wait_time_sec=30) 
#
# if do ctrl+C: RE.abort()
#
# RE(shopen())
# RE(shclose())
#
# Data: /nsls2/xf12id2/data/images/users/2021_2/305435_Murray/
# Analysis: /nsls2/xf12id2/analysis/2021_2/305435_Murray/
#
# ======================================================================

import numpy as np
import sys, time

#det = [pil1M, pdcurrent, pdcurrent1, pdcurrent2]
# dets = [pil300KW, pil1M]

def insitu_EM(t=1, name = 'insitu_S1_run1', wait_time_sec=30, number_start=149, use_waxs=0, interval_waxs=5):

    dets = [pil1M, pdcurrent, pdcurrent1, pdcurrent2]
    det_exposure_time(t,t) 

    t0 = time.time()
    number = number_start
    while number < 2000: 
        #yield from bps.mv(stage.y, yss[number])
        #yield from bps.mv(stage.x, xss[number])       

        #### Insert atten & Get pindiode reading
        dets = [pdcurrent, pdcurrent1, pdcurrent2]

        yield from bps.mv(att1_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att1_10.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att1_9.open_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att1_10.open_cmd, 1)
        yield from bps.sleep(1)
        fs.open()
        yield from bps.sleep(0.3)
        pd_curr = pdcurrent1.value
        fs.close()
        print( '--------- Current pd_curr {}\n'.format(pd_curr))
        #### Remove atten
        yield from bps.mv(att1_9.close_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att1_10.close_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att1_9.close_cmd, 1)
        yield from bps.sleep(1)
        yield from bps.mv(att1_10.close_cmd, 1)
        yield from bps.sleep(1)

        dets = [pil1M]

        #### Get temperature reading
        curr_tempC = ls.input_A_celsius.value
        ii = 1
        while curr_tempC > 200 and ii<50:  #Sometimes reading can be off
            yield from bps.sleep(0.2)
            curr_tempC = ls.input_A_celsius.value
            ii = ii+1
        print( '---------  Current temperature (degC)\n {}'.format(curr_tempC))

        #### Take a waxs every 10 measurements
        if use_waxs==1:
            if number%interval_waxs == 0:
                yield from bps.mv(waxs, 0)
                dets = [pil300KW]
            else:
                yield from bps.mv(waxs, 13)    
                dets = [pil1M] 
            det_exposure_time(t,t) 

        #### Define sample name & Measure
        t1 = time.time()
        name_fmt = '{sample}_{number}_{temperature}C_t{time}_pd{pd_curr}'
        sample_name = name_fmt.format(sample=name, number=number, temperature='%3.1f'%(curr_tempC), time = '%3.1f'%(t1-t0), pd_curr='%5.5d'%(pd_curr))
        print(f'\n\t=== Sample: {sample_name} ===\n')
        sample_id(user_name='EM', sample_name=sample_name) 

        yield from bp.count( dets, num=1)

        #### Wait
        yield from bps.sleep(wait_time_sec)
        number=number+1


#####################
## Bar1  (Labelled BAR 4)
user_name = 'EM2_Bar1' ## Enter different Bar number!
sample_list = [ 'S12_Tol', 'S11_PbS51_0p1pc', 'S10_PbS51_01pc', 'S09_PbS51_02pc', 'S08_PbS51_03pc',
                'S07_PbS51_04pc', 'S06_PbS51_05pc', 'S05_PbS51_06pc', 'S04_PbS51_07pc','S03_PbS51_08pc',
                'S02_PbS51_09pc', 'S01_PbS51_10pc'
                ]
x_list = [  27000, 20400, 14400, 7950, 1650,
            -4850, -10950, -17350, -23300, -30000,
            -36100, -42050
       ]

## Bar2 (Labelled BAR 1) 
user_name = 'EM2_Bar2' 
sample_list = [ 'S13_Tol', 'S12_PbS46_0p1pc', 'S11_PbS46_01pc', 'S10_PbS46_02pc', 'S08_PbS46_03pc',
                'S07_PbS46_04pc', 'S06_PbS46_05pc', 'S05_PbS46_06pc', 'S04_PbS46_07pc','S03_PbS46_08pc',
                'S02_PbS46_09pc', 'S01_PbS46_10pc'
                ]
x_list = [  33700, 27200, 20900, 14600, 2050,
            -4200, -10300, -16700, -23000, -29400,
            -35600, -41700
       ]

## Bar3 (Labelled BAR 2)
user_name = 'EM2_Bar3' 
sample_list = [ 'S15_PbS48_07pc', 'S14_PbS48_08pc', 'S13_PbS48_09pc', 'S12_PbS48_10pc', 'S11_PbS47_0p1pc', 
                'S10_PbS47_01pc', 'S09_PbS47_02pc', 'S08_PbS47_03pc', 'S07_PbS47_04pc', 'S06_PbS47_05pc', 
                'S05_PbS47_06pc', 'S04_PbS47_07pc','S03_PbS47_08pc',  'S02_PbS47_09pc', 'S01_PbS47_10pc'
                ]
x_list = [  45800, 39600, 33200, 26800, 20500, 
            14300, 8300, 1500, -4500, -10700, 
            -17200, -23500, -29700, -36000, -42400
       ]

user_name = 'EM2_Bar3' 
sample_list = [ ' S03_PbS47_08pc' ]
x_list = [  -29700  ]

## Bar4 (Labelled BAR 3)
user_name = 'EM2_Bar4' 
sample_list = [ 'S15_PbS52_03pc', 'S14_PbS52_04pc', 'S13_PbS52_05pc', 'S12_PbS52_06pc', 'S11_PbS52_07pc', 
                'S10_PbS52_08pc', 'S09_PbS52_09pc', 'S08_PbS52_10pc',  'S07_PbS48_0p1pc', 'S06_PbS48_01pc', 
                'S05_PbS48_02pc', 'S04_PbS48_03pc','S03_PbS48_04pc', 'S02_PbS48_05pc', 'S01_PbS48_06pc'
                ]
x_list = [  46000, 39800, 33500, 27500, 21200, 
            14700, 8500, 2300, -4300, -10500, 
            -16600, -23100, -29500, -35800, -42200
       ]

## Bar5 (Labelled BAR 5)
user_name = 'EM2_Bar5' 
sample_list = [ 'S15_Fe3O4_no2_01pc', 'S14_Fe3O4_no2_02pc', 'S13_Fe3O4_no2_03pc', 'S12_Fe3O4_no2_04pc', 'S11_Fe3O4_no2_05pc', 
                'S10_Fe3O4_no2_06pc', 'S09_Fe3O4_no2_07pc', 'S08_Fe3O4_no2_08pc',  'S07_Fe3O4_no2_09pc', 'S06_Fe3O4_no2_10pc', 
#                'S05_PbS52_0p1pc', 'S04_PbS52_01pc','S03_PbS52_02pc', 
                ]
x_list = [  45700, 39700, 33100, 26800, 20600, 
            14300, 8100, 1800, -4500, -10700, 
#            -17100, -23400, -29800, 
       ]
#sample_list = [ 'S05_PbS52_0p1pc', 'S04_PbS52_01pc', 'S03_PbS52_02pc', 
#                ]
#x_list = [  
#            -17100, -23400, -29800, 
#       ]

## Bar6 (Labelled BAR 1)
user_name = 'EM2_Bar6' 
sample_list = [ 'S14_Tol', # 'S13_Fe3O4_no6_0p1pc', 'S12_Fe3O4_no6_01pc', 'S11_Fe3O4_no6_02pc', 'S10_Fe3O4_no6_03pc', 
                #'S08_Fe3O4_no6_04pc',  'S07_Fe3O4_no6_05pc', 'S06_Fe3O4_no6_06pc', 'S05_Fe3O4_no6_07pc', 'S04_Fe3O4_no6_08pc',
                #'S03_Fe3O4_no6_09pc', 'S02_Fe3O4_no6_10pc', 'S01_Fe3O4_no2_0p1pc'
                ]
x_list = [  40000, #33700, 27300, 20900, 14700, 
            #2150,  -4100, -10200, -16700, -22900, 
            #-29300, -35600, -41700
       ]


## Bar 7 (Labelled BAR 2)
user_name = 'EM2_Bar7'
sample_list = [ 'S15_Fe3O4_no2105186_06pc', 'S14_Fe3O4_no2105186_08pc', 'S13_Fe3O4_no2105186_10pc', 'S12_Fe3O4_no210511B_0p1pc', 'S11_Fe3O4_no210511B_02pc', 
                'S10_Fe3O4_no210511B_04pc', 'S09_Fe3O4_no210511B_06pc', 'S08_Fe3O4_no210511B_08pc', 'S07_Fe3O4_no210511B_10pc', 'S06_Fe3O4_no9_0p1pc', 
                'S05_Fe3O4_no9_02pc', 'S04_Fe3O4_no9_04pc','S03_Fe3O4_no9_06pc',  'S02_Fe3O4_no9_08pc', 'S01_Fe3O4_no9_10pc'
                ]
x_list = [  45800, 39600, 33200, 26800, 20600, 
            14300, 8300, 1500, -4600, -10600, 
            -17200, -23300, -29600, -36000, -42500
       ]

## Bar 8 (Labelled BAR 3)
user_name = 'EM2_Bar8'
sample_list = [ 'S09_Fe3O4_no2105187_0p1pc', 'S08_Fe3O4_no2105187_02pc',  'S07_Fe3O4_no2105187_04pc', 'S06_Fe3O4_no2105187_06pc', 
                'S05_Fe3O4_no2105187_08pc', 'S04_Fe3O4_no2105187_10pc','S03_Fe3O4_no2105186_0p1pc', 'S02_Fe3O4_no2105186_02pc', 'S01_Fe3O4_no2105186_04pc'
                ]
x_list = [  8100, 1900, -4500, -10500, 
            -16700, -23300, -29700, -35500, -41700
       ]


## Bar 9 (Labelled BAR 4)
user_name = 'EM2_Bar9'
sample_list = [ 'S15_Fe3O4_210511A2_06pc', 'S14_Fe3O4_210511A2_08pc', 'S13_Fe3O4_210511A2_10pc',
                'S12_Fe3O4_210511A1_0p1pc', 'S11_Fe3O4_210511A1_02pc', 'S10_Fe3O4_210511A1_04pc', 'S09_Fe3O4_210511A1_06pc', 'S08_Fe3O4_210511A1_08pc',
                'S07_Fe3O4_210511A1_10pc', 'S06_Fe3O4_4p5nm_0p1pc', 'S05_Fe3O4_4p5nm_02pc', 'S04_Fe3O4_4p5nm_2p5pc','S03_Fe3O4_4p5nm_03pc',
                'S02_Fe3O4_4p5nm_3p5pc', 'S01_Fe3O4_4p5nm_04pc'
                ]
x_list = [  45850, 39600, 33300, #(1198-1646), (1242-1650), (1173-1635) capillary width in pixels on on-axis camera; 1343-1523 is roi3
            26900, 20400, 14200, 7850, 1650, #(1223-1690), (1227-1631), (1238-1642), (1231-1622), (1234-1650)
            -4750, -10850, -17250, -23400, -29900, #(1202-1650), (1213-1610), (1191-1656), (1213-1620), (1170-1640)
            -36100, -42100 #(1225-1640), (1220-1674)
       ]


## Bar 10 (Labelled BAR 5)
user_name = 'EM2_Bar10'
sample_list = [ 'S15_Fe3O4_210511A4_02pc', 'S14_Fe3O4_210511A4_04pc', 'S13_Fe3O4_210511A4_06pc', 'S12_Fe3O4_210511A4_08pc', 'S11_Fe3O4_210511A4_10pc', 
                'S10_Fe3O4_210511A3_0p1pc', 'S09_Fe3O4_210511A3_02pc', 'S08_Fe3O4_210511A3_04pc',    'S06_Fe3O4_210511A3_06pc', 
                'S05_Fe3O4_210511A3_08pc', 'S04_Fe3O4_210511A3_10pc','S03_Fe3O4_210511A2_0p1pc', 'S02_Fe3O4_210511A2_02pc', 'S01_Fe3O4_210511A2_04pc'
                ]
x_list = [  45700, 39700, 33100, 26800, 20600, 
            14300, 8000, 1800,  -10600, 
            -17100, -23400, -29800, -35800, -42100
       ]

## Bar 11 (Labelled BAR 1)
user_name = 'EM2_Bar11'
sample_list = [ 'S13_Fe3O4_210511C6_02pc', 'S12_Fe3O4_210511C6_04pc', 'S11_Fe3O4_210511C6_06pc', 'S10_Fe3O4_210511C6_08pc', 
                'S08_Fe3O4_210511C6_10pc',  
                'S07_Fe3O4_210511A5_0p1pc', 'S06_Fe3O4_210511A5_02pc', 'S05_Fe3O4_210511A5_04pc', 'S04_Fe3O4_210511A5_06pc',
                'S03_Fe3O4_210511A5_08pc', 'S02_Fe3O4_210511A5_10pc', 'S01_Fe3O4_210511A4_0p1pc'
                ]
x_list = [  33700, 27300, 20900, 14700, 
            2150,  
            -4100, -10100, -16600, -22900, 
            -29300, -35600, -41600
       ]

## Bar 12 (Labelled BAR 2)
user_name = 'EM2_Bar12'
sample_list = [ 'S15_Fe3O4_210511C9_08pc', 'S14_Fe3O4_210511C9_10pc', 'S13_Fe3O4_210511C8_0p1pc', 'S12_Fe3O4_210511C8_02pc', 'S11_Fe3O4_210511C8_04pc', 
                'S10_Fe3O4_210511C8_06pc', 'S09_Fe3O4_210511C8_08pc', 'S08_Fe3O4_210511C8_10pc', 'S07_Fe3O4_210511C7_0p1pc', 'S06_Fe3O4_210511C7_02pc', 
                'S05_Fe3O4_210511C7_04pc', 'S04_Fe3O4_210511C7_06pc','S03_Fe3O4_210511C7_08pc',  'S02_Fe3O4_210511C7_10pc', 'S01_Fe3O4_210511C6_0p1pc'
                ]
x_list = [  45800, 39700, 33200, 26800, 20400, 
            14300, 8300, 1600, -4500, -10800, 
            -17200, -23400, -29700, -36100, -42200
       ]

## Bar 13 (Labelled BAR 3)
user_name = 'EM2_Bar13'
sample_list = [ 'S15_PbS49_04pc_OA2pc', 'S14_PbS49_06pc_OA2pc', 'S13_PbS49_08pc_OA2pc', 'S12_PbS49_10pc_OA2pc', 'S11_OA0pc', 
                'S10_PbS49_0p1pc_OA0pc', 'S09_PbS49_02pc_OA0pc', 'S08_PbS49_04c_OA0pc',  'S07_PbS49_06pc_OA0pc', 'S06_PbS49_08pc_OA0pc', 
                'S05_PbS49_10pc_OA0pc', 
                #'S04_Fe3O4_210511C9_0p1pc','S03_Fe3O4_210511C9_02pc', 'S02_Fe3O4_210511C9_04pc', 'S01_Fe3O4_210511C9_06pc'
                ]
x_list = [  46000, 40000, 33600, 27400, 21000, 
            14400, 8300, 2000, -4200, -10000, 
            -16500, 
            #-22900, -29700, -35900, -42100
       ]

## Bar 14 (Labelled BAR 4)
user_name = 'EM2_Bar14'
sample_list = [ 'S15_PbS49_02pc_OA6pc', 'S14_PbS49_04pc_OA6pc', 'S13_PbS49_06pc_OA6pc', 'S12_PbS49_08pc_OA6pc', 'S11_PbS49_10pc_OA6pc', 
                'S10_OA4pc', 'S09_PbS49_0p1pc_OA4pc', 'S08_PbS49_02pc_OA4pc',  'S07_PbS49_04pc_OA4pc', 'S06_PbS49_06pc_OA4pc', 
                'S05_PbS49_08pc_OA4pc', 'S04_PbS49_10pc_OA4pc','S03_OA2pc', 'S02_PbS49_0p1pc_OA2pc', 'S01_PbS49_02pc_OA2pc'
                ]
x_list = [  45850, 39600, 33300, 27000, 20400, 
            14250, 7950, 1750, -4750, -10850, 
            -17250, -23500, -29700, -36100, -42200 
       ]

## Bar 15 (Labelled BAR 5)
user_name = 'EM2_Bar15'
sample_list = [ 'S15_PbS49_04pc_OA10pc', 'S14_PbS49_06pc_OA10pc', 'S13_PbS49_08pc_OA10pc', 'S12_PbS49_10pc_OA10pc', 'S11_OA8pc', 
                'S10_PbS49_0p1pc_OA8pc', 'S09_PbS49_02pc_OA8pc', 'S08_PbS49_04pc_OA8pc',  'S07_PbS49_06pc_OA8pc', 'S06_PbS49_08pc_OA8pc', 
                'S05_PbS49_10pc_OA8pc', 'S04_OA6pc','S03_PbS49_0p1pc_OA6pc', 
                ]
x_list = [  45700, 39700, 33100, 26800, 20600, 
            14300, 8000, 1700, -4450, -10600, 
            -17100, -23400, -29800, 
       ]

## Bar 16 (Labelled BAR 1)
user_name = 'EM2_Bar16'
sample_list = [ 'S14_PbS49_06pc_OA14pc','S13_PbS49_08pc_OA14pc', 'S12_PbS49_10pc_OA14pc', 'S11_OA12pc', 'S10_PbS49_0p1pc_OA12pc', 
                'S08_PbS49_02pc_OA12pc',  'S07_PbS49_04pc_OA12pc', 'S06_PbS49_06pc_OA12pc', 'S05_PbS49_08pc_OA12pc', 'S04_PbS49_10pc_OA12pc',
                'S03_OA10pc', 'S02_PbS49_0p1pc_OA10pc', 'S01_PbS49_02pc_OA10pc'
                ]
x_list = [  40000, 33700, 27300, 20900, 14700, 
            2150,  -4100, -10200, -16600, -22900, 
            -29300, -35600, -41700
       ]

## Bar 17 (Labelled BAR 2)
user_name = 'EM2_Bar17'
sample_list = [ 'S15_PbS49_04pc_OA18pc', 'S14_PbS49_06pc_OA18pc', 'S13_PbS49_08pc_OA18pc', 'S12_PbS49_10pc_OA18pc', 'S11_OA16pc', 
                'S10_PbS49_0p1pc_OA16pc', 'S09_PbS49_02pc_OA16pc', 'S08_PbS49_04pc_OA16pc', 'S07_PbS49_06pc_OA16pc', 'S06_PbS49_08pc_OA16pc', 
                'S05_PbS49_10pc_OA16pc', 'S04_OA14pc','S03_PbS49_0p1pc_OA14pc',  'S02_PbS49_02pc_OA14pc', 'S01_PbS49_04pc_OA14pc'
                ]
x_list = [  45800, 39500, 33400, 27000, 20500, 
            14350, 8000, 1600, -4500, -10800, 
            -17200, -23400, -29700, -36100, -42400
       ]


## Bar 18 (Labelled BAR 3)
user_name = 'EM2_Bar18'
sample_list = [ 'S15_PbS50_02pc_Tol', 'S14_PbS50_04pc_Tol', 'S13_PbS50_06pc_Tol', 'S12_PbS50_08pc_Tol', 'S11_PbS50_10pc_Tol', 
                'S10_OA20pc', 'S09_PbS49_0p1pc_OA20pc', 'S08_PbS49_02pc_OA20pc', 'S07_PbS49_04pc_OA20pc', 'S06_PbS49_06pc_OA20pc', 
                'S05_PbS49_08pc_OA20pc', 'S04_PbS49_10pc_OA20pc','S03_OA18pc',  'S02_PbS49_0p1pc_OA18pc', 'S01_PbS49_02pc_OA18pc'
                ]
x_list = [  45950, 39650, 33600, 27400, 20800, 
            14500, 8300, 1800, -4300, -10300, 
            -16700, -23100, -29600, -35550, -42100
       ]


## Bar 19 (Labelled BAR 4)
user_name = 'EM2_Bar19'
sample_list = [ #'S15_PbS50_0p1pc_XYLENE', 'S14_PbS50_02pc_XYLENE', 'S13_PbS50_04pc_XYLENE', 'S12_PbS50_06pc_XYLENE', 'S11_PbS50_08pc_XYLENE', 
                #'S10_PbS50_10pc_XYLENE', 
                'S09_DIOXANE', 'S08_PbS50_0p1pc_DIOXANE',  'S07_PbS50_02pc_DIOXANE',  
                'S05_PbS50_06pc_DIOXANE', 'S04_PbS50_08pc_DIOXANE','S03_PbS50_10pc_DIOXANE', 
                #'S02_Tol', 'S01_PbS50_0p1pc_Tol'
                ]
x_list = [  #45850, 39600, 33300, 26800, 20400, 
            #14250, 
            8250, 1450, -4650, 
            -17250, -23400, -29900, 
            #-36100, #-42200 
       ]

## Bar 20 (Labelled BAR 5)
user_name = 'EM2_Bar20'
sample_list = [ 'S15_PbS50_02pc_DODECANE', 'S14_PbS50_04pc_DODECANE', 'S13_PbS50_06pc_DODECANE', 'S12_PbS50_08pc_DODECANE', 'S11_PbS50_10pc_DODECANE', 
                'S10_DECALIN', 'S09_PbS50_0p1pc_DECALIN', 'S08_PbS50_02pc_DECALIN',  'S07_PbS50_04pc_DECALIN', 'S06_PbS50_06pc_DECALIN', 
                'S05_PbS50_08pc_DECALIN', 'S04_PbS50_10pc_DECALIN', 'S03_XYLENE', 
                ]
x_list = [  45700, 39700, 33100, 26800, 20600, 
            14300, 8100, 1800, -4450, -10700, 
            -17100, -23400, -29800, 
       ]

## Bar 21 (Labelled BAR 1)
user_name = 'EM2_Bar21'
sample_list = [ 'S14_PbS50_06pc_OCTANE','S13_PbS50_08pc_OCTANE', 'S12_PbS50_10pc_OCTANE', 'S11_DECANE', 'S10_PbS50_0p1pc_DECANE', 
                'S07_PbS50_02pc_DECANE', 'S06_PbS50_04pc_DECANE', 'S05_PbS50_06pc_DECANE', 'S04_PbS50_08pc_DECANE',
                'S03_PbS50_10pc_DECANE', 'S02_DODECANE', 'S01_PbS50_0p1pc_DODECANE'
                ]
x_list = [  40000, 33700, 27300, 20900, 14700, 
            -4100, -10200, -16600, -22900, 
            -29300, -35600, 
            -41650
       ]

## Bar 22 (Labelled BAR 2)
user_name = 'EM2_Bar22'
sample_list = [ #'S15_PbS50_04pc_ANISOLE', 'S14_PbS50_06c_ANISOLE', 'S13_PbS50_08pc_ANISOLE', 'S12_PbS50_10pc_ANISOLE', 
                'S11_HEPTANE', 
                'S10_PbS50_0p1pc_HEPTANE', 'S09_PbS50_02pc_HEPTANE', 'S08_PbS50_04pc_HEPTANE', 'S07_PbS50_06pc_HEPTANE', 'S06_PbS50_08pc_HEPTANE', 
                'S05_PbS50_10pc_HEPTANE', 'S04_OCTANE','S03_PbS50_0p1pc_OCTANE',  'S02_PbS50_02pc_OCTANE', 'S01_PbS50_04pc_OCTANE'
                ]
x_list = [  #45850, 39500, 33400, 26800, 
            20500, 
            14350, 8100, 1600, -4500, -10800, 
            -17100, -23400, -29500, -35900, -42400
       ]


## Bar 23 (Labelled BAR 4)
user_name = 'EM2_Bar23'
sample_list = [  
                #'S09_Tol', 'S08_FICO6_0p004pc',  'S07_FICO6_0p08pc',  
                #'S06_FICO6_0p16pc', 
                #'S05_FICO6_0p25pc', 'S04_FICO6_0p33pc', 'S03_FICO6_0p41pc',
                'S02_CH', 'S01_PbS50_0p1pc_CH',
                ]
x_list = [   
            #7750, 1650, -4650, 
            #-10700, 
            #-17250, -23500, -29600, 
            -36000, -42300 
       ]

## Bar 24 (Labelled BAR 3)
user_name = 'EM2_Bar24'
sample_list = [ 'S15_PbS50_02pc_CH', 'S14_PbS50_04pc_CH', 'S13_PbS50_06pc_CH', 'S12_PbS50_08pc_CH', 'S11_PbS50_10pc_CH', 
                'S10_HEXANE', 'S09_PbS50_0p1pc_HEXANE', 'S08_PbS50_02pc_HEXANE', 'S07_PbS50_04pc_HEXANE', 'S06_PbS50_06pc_HEXANE', 
                'S05_PbS50_08pc_HEXANE', 'S04_PbS50_10pc_HEXANE',
                #'S03_ANISOLE',  'S02_PbS50_0p1pc_ANISOLE', 'S01_PbS50_02pc_ANISOLE'
                ]
x_list = [  46150, 40000, 33600, 27400, 21100, 
            14600, 8200, 1800, -4400, -10400, 
            -16500, -23100, 
           # -29200, -35300, -41800
       ]


## Bar 25 (Labelled BAR 5)
user_name = 'EM2_Bar25'
sample_list = [  'S13_Empty_cap_calibration', #'S12_FICO10_0p005', 'S11_FICO10_0p10', 
                #'S10_FICO10_0p20', 'S09_FICO10_0p29', 'S08_FICO10_0p39',  'S07_FICO10_0p49', 'S06_FICO9_0p02', 
                #'S05_FICO9_0p49', 'S04_FICO9_0p98', 'S03_FICO9_1p46', 'S02_FICO9_1p95', 'S01_FICO9_2p44'
                ]
x_list = [   33100, #26800, 20600, #Capillary(1202-1588)
           # 14300, 8100, 1800, -4450, -10700, 
           # -17100, -23400, -29800, -35800, -42100
       ]


## Bar 26 (Labelled BAR 5)
user_name = 'EM2_Bar26'
sample_list = [ 'S13_Water_cap_calibration', #'S12_FICO12_0p015', 'S11_FICO12_0p30', 
               #'S10_FICO12_0p60', 'S09_FICO12_0p90', 'S08_FICO12_1p20', 'S07_FICO12_1p50', 'S06_FICO4_0p01', 
               # 'S05_FICO4_0p22', 'S04_FICO4_0p44', 'S03_FICO4_0p67',  'S02_FICO4_0p88', 'S01_FICO4_1p11'
                ]
x_list = [  33400,# 27200,  20500, 
           # 14350, 8000, 1600, -4600, -10800, 
           # -17200, -23400, -29800, -36000, -42400
       ]





#######################################################
def exsitu_EM(t=1, x_range_um=0, Nx=1, Nrep=3, add_att=1, more_scans=0, use_waxs=0):

    assert len(x_list) == len(sample_list), f'Sample name/position list is incorrect!'
 
    x_shift_array = np.linspace(-x_range_um, x_range_um, Nx)
    Natt = 5 # to ensure attenuator is placed/removed

    ### SAXS
    for ii, (x, sample) in enumerate(zip(x_list,sample_list)): 
        print( '\n##### {}, {} #####\n'.format(ii, sample))

        yield from bps.mv(piezo.x, x) #move to next sample 
 
        x_pos_array = x + x_shift_array 

        for x_meas in x_pos_array: # measure at a few x positions
            yield from bps.mv(piezo.x, x_meas) 

            #### Insert atten & Get pindiode reading
            dets = [pdcurrent, pdcurrent1, pdcurrent2]

            for aa in np.arange(0,Natt):
                yield from bps.mv(att1_9.open_cmd, 1)
                yield from bps.sleep(0.5)
                yield from bps.mv(att1_10.open_cmd, 1)
                yield from bps.sleep(0.5)
                if add_att:
                    yield from bps.mv(att1_11.open_cmd, 1)
                    yield from bps.sleep(1)

            fs.open()
            yield from bps.sleep(0.3)
            pd_curr = pdcurrent1.value
            if ii==0:
                pd_curr_ref = pd_curr
            fs.close()
            print( '--------- Current pd_curr {}, pd_curr_ref {}\n'.format(pd_curr, pd_curr_ref))
            #### Remove atten
            for aa in np.arange(0,Natt):
                yield from bps.mv(att1_9.close_cmd, 1)
                yield from bps.sleep(0.5)
                yield from bps.mv(att1_10.close_cmd, 1)
                yield from bps.sleep(0.5)
                if add_att:
                    yield from bps.mv(att1_11.close_cmd, 1)
                    yield from bps.sleep(1)

            dets = [pil1M]

            if more_scans==1:
                Nscan = np.ceil(pd_curr_ref/pd_curr)
            else:
                Nscan = Nrep
            print('\n--------- Nscan = {}---------\n'.format(Nscan))

            for nn in np.arange(0,Nscan,1):
                det_exposure_time(t,t) 

                if add_att:
                    for aa in np.arange(0,Natt):
                        yield from bps.mv(att1_10.open_cmd, 1)
                        yield from bps.sleep(0.5)

                    name_fmt = '{sample}_att1-10_x{x}_n{nn}_exp{t}s_pd{pd_curr}'
                else:
                    name_fmt = '{sample}_x{x}_n{nn}_exp{t}s_pd{pd_curr}'

                #### Define sample name & Measure
                t1 = time.time()
                sample_name = name_fmt.format(sample=sample, x='%05.2f'%(x_meas), nn=nn, t='%2.2f'%(t), pd_curr='%5.5d'%(pd_curr))
                print(f'\n\t=== Sample: {sample_name} ===\n')
                sample_id(user_name=user_name, sample_name=sample_name) 

                yield from bp.count( dets, num=1)

        if add_att:
            for aa in np.arange(0,Natt):
                yield from bps.mv(att1_10.close_cmd, 1)
                yield from bps.sleep(0.5)



    ### WAXS
    if use_waxs:
        yield from bps.mv(waxs, 0) 
        for ii, (x, sample) in enumerate(zip(x_list,sample_list)): 
            yield from bps.mv(piezo.x, x) #move to next sample 
    
            x_pos_array = x + x_shift_array 

            for x_meas in x_pos_array: # measure at a few x positions
                yield from bps.mv(piezo.x, x_meas) 

                dets = [pil300KW]
                det_exposure_time(t,t) 

                #### Define sample name & Measure
                t1 = time.time()
                name_fmt = '{sample}_x{x}'
                sample_name = name_fmt.format(sample=name, x='%05.2f'%(x_meas))
                print(f'\n\t=== Sample: {sample_name} ===\n')
                sample_id(user_name='EM', sample_name=sample_name) 

                yield from bp.count( dets, num=1)
        yield from bps.mv(waxs, 13) 
 
# RE(bps.mv(waxs, 13)) 
# sample_id(user_name='test', sample_name='test')
