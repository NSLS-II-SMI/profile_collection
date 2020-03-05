print(f'Loading {__file__}')

import nslsii
nslsii.configure_base(get_ipython().user_ns, 'smi')
# nslsii.configure_olog(get_ipython().user_ns, subscribe=False)

#Optional: set any metadata that rarely changes.
#list of what we should put
#Cycle, proposal number, main_proposer, beamline name, optinal comments
RE.md['beamline_id'] = 'SMI'


