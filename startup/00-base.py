print(f'Loading {__file__}')

import warnings
import nslsii
from databroker import Broker
from ophyd import Signal

nslsii.configure_base(get_ipython().user_ns, 'smi')
# nslsii.configure_olog(get_ipython().user_ns, subscribe=False)


from bluesky.utils import PersistentDict

#Try to set this new path
RE.md = PersistentDict('~/profile_collection/startup/')

RE.md['beamline_name'] = 'SMI'
RE.md['facility'] = 'NSLS-II'
RE.md['optinal_comments'] = '' #Any comment can be added if needed

