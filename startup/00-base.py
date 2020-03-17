print(f'Loading {__file__}')

import warnings
import nslsii
from ophyd import Signal

nslsii.configure_base(get_ipython().user_ns, 'smi')
# nslsii.configure_olog(get_ipython().user_ns, subscribe=False)

'''
Metadata: Will be read from the last bluesky documents if bluesky crashed
This is the base of metadatawhich would be never/rarely changed : facility and beamline names
Cycle, proposal number, main proposer and comments
'''

try:
    cycle = db[-1].table(stream_name='baseline')['cycle'][1]
    proposal_number = db[-1].table(stream_name='baseline')['proposal_number'][1]
    main_proposer = db[-1].table(stream_name='baseline')['main_proposer'][1]
    optinal_comments = db[-1].table(stream_name='baseline')['optinal_comments'][1]
except:
    warnings.warn(f'Previous databroker record was not read. '
                          f'Setting cycle, proposal_numer, proposer_name to test value ')
    cycle = ''
    proposal_number = ''
    main_proposer = ''
    optinal_comments = ''

beamline_name = Signal(name='beamline_name', value = 'SMI') 
cycle = Signal(name='cycle', value = cycle)
proposal_number = Signal(name='proposal_number', value = proposal_number)
main_proposer = Signal(name='main_proposer', value = main_proposer)
optinal_comments = Signal(name='optinal_comments', value = optinal_comments)

base_md = { 'facility' : 'NSLS-II',
            'beamline_name' : 'SMI',
            'cycle': cycle.value,
            'proposal_number': proposal_number.value,
            'main_proposer': main_proposer.value,
            'optinal_comments': optinal_comments.value
            }
