print(f'Loading {__file__}')

import warnings
import nslsii
from databroker import Broker
from ophyd import Signal

nslsii.configure_base(get_ipython().user_ns, 'smi')
# nslsii.configure_olog(get_ipython().user_ns, subscribe=False)


from bluesky.utils import PersistentDict

#Implement a new path here
RE.md = PersistentDict('some/path/here')

RE.md['beamline_name'] = 'SMI'
RE.md['facility'] = 'NSLS-II'
RE.md['optinal_comments'] = '' #Any comment can be added if needed

