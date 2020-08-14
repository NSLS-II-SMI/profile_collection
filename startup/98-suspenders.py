
print(f'Loading {__file__}')

import bluesky.plans as bp
from bluesky.suspenders import SuspendFloor, SuspendBoolLow, SuspendBoolHigh, SuspendCeil

# Temperature of the WAXS motor suspender
susp_waxs_motor = SuspendCeil(ls.ch2_read, 150, resume_thresh=120)
RE.install_suspender(susp_waxs_motor)

# Count on XBPM2 suspender
susp_xbpm2_sum = SuspendFloor(xbpm2.sumY, 0.3, resume_thresh=0.8)
RE.install_suspender(susp_xbpm2_sum)

'''
#Count on XBPM3 suspender
susp_xbpm3_sum = SuspendFloor( xbpm3.sumY, 0.3, resume_thresh= 0.8 )
RE.install_suspender( susp_xbpm3_sum )
'''

# Ring current suspender
susp_beam = SuspendFloor(ring.current, 100, resume_thresh=350)
RE.install_suspender(susp_beam)

# Front end shutter suspender
susp_smi_shutter = SuspendFloor(smi_shutter_enable, 0.1, resume_thresh=0.9)
RE.install_suspender(susp_smi_shutter)
