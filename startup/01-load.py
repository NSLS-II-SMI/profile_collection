print(f'Loading {__file__}')

import pandas as pd
import numpy as np


def interpolate_db_sdds():
    '''
    Load the intepolation_db_sdd2.txt from the startup folder containing the direct beam position as well as the sample detector distance measured
    at given encoded sample detctor distance. Then it interpolate the current beam position and sample detctor distance from the current detctor position
    '''

    dir = '/home/xf12id/.ipython/profile_collection/startup/' 
    data = pd.read_csv(os.path.join(dir, 'intepolation_db_sdd2.txt'), sep='\t')

    sdds_encodeded = data['sdd(mm)'].values
    sdds_calculated = data['sdd_calculated'].values

    db_x_pos_registered = data['db_x_pos'].values
    db_y_pos_registered = data['db_y_pos'].values

    det_posx = pil1m_pos.x.position
    det_posy = pil1m_pos.y.position
    det_posz = 0.001 * pil1m_pos.z.position

    current_sdd = np.interp(det_posz, sdds_encodeded, sdds_calculated)

    dbx_interp_x3 = np.interp(det_posz, sdds_encodeded, db_x_pos_registered)
    dby_interp_y0 = np.interp(det_posz, sdds_encodeded, db_y_pos_registered)

    current_dbx = dbx_interp_x3 + (det_posx - 3) / 0.172
    current_dby = dby_interp_y0 + det_posy / 0.172

    return current_sdd, [current_dbx, current_dby]




