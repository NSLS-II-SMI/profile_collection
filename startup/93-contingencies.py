print(f'Loading {__file__}')

import bluesky.plan_stubs as bps
#from bluesky.suspenders import SuspendBoolHigh, SuspendFloor, SuspendBoolLow
import logging
import datetime
import os
import pandas as pds
import os
import time

'''
def send_notice(email,subject,msg):
    os.system('echo '+msg+' | mail -s "'+subject+'" '+email)

def send_notice_plan(email,subject,msg):
    send_notice(email,subject,msg)
    yield from bps.sleep(.1)


def beamdown_notice():
    user_email = RE.md['user_email']
    send_notice(bls_email+','+user_email,'SMI has lost beam','Beam to RSoXS has been lost.')


def beamup_notice():
    user_email = RE.md['user_email']
    send_notice(bls_email+','+user_email,'SST-1 beam restored','Beam to RSoXS has been restored.')


class OSEmailHandler(logging.Handler):
    def emit(self, record):
        user_email = RE.md['user_email']
        send_notice(user_email, 'SST has thrown an exception', record.getMessage()) # record.stack_info



logger = logging.getLogger('bluesky.RE')
handler = OSEmailHandler()
handler.setLevel('ERROR')  # Only email for if the level is ERROR or higher (CRITICAL).
logger.addHandler(handler)
'''