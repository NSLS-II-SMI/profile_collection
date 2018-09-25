print(f'Loading {__file__}')

import nslsii
nslsii.configure_base(get_ipython().user_ns, 'smi')
nslsii.configure_olog(get_ipython().user_ns)

#Optional: set any metadata that rarely changes.
RE.md['beamline_id'] = 'SMI'


