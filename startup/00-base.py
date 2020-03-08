print(f'Loading {__file__}')

import nslsii
nslsii.configure_base(get_ipython().user_ns, 'smi')
# nslsii.configure_olog(get_ipython().user_ns, subscribe=False)

#Optional: set any metadata that rarely changes.
#list of what we should put
#Cycle, proposal number, main_proposer, beamline name, optinal comments

'''
from ophyd import Signal
beamline_name = Signal(name='beamline_name', value = 'SMI')

#Need here a way of checking if a value is there. If not ask for a new value
cycle = db[-1].table(stream_name='baseline')['cycle'][1]
proposal_number = db[-1].table(stream_name='baseline')['proposal_number'][1]
main_proposer = db[-1].table(stream_name='baseline')['main_proposer'][1]
optinal_comments = db[-1].table(stream_name='baseline')['optinal_comments'][1]

cycle = Signal(name='cycle', value = cycle)
proposal_number = Signal(name='proposal_number', value = proposal_number)
main_proposer = Signal(name='main_proposer', value = main_proposer)
optinal_comments = Signal(name='optinal_comments', value = optinal_comments)


sd.baseline = [beamline_name, cycle, proposal_number, main_proposer, optinal_comments]
'''

