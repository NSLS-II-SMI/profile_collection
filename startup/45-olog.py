from bluesky.callbacks.olog import logbook_cb_factory
import readline
from collections import defaultdict
import queue
import threading

#{{- readline.get_history_item(1)}}


simple_template = """{{- start.plan_name }} ['{{ start.uid[:6] }}'] (scan num: {{ start.scan_id }})"""
manual_count_template =  """{{- start.plan_name }} ['{{ start.uid[:6] }}'] (scan num: {{ start.scan_id }}) (Measurement: {{start.Measurement}} )"""
grid_template = """{{- start.plan_name}} :  {{ start.motors[0]}}  {{'%0.3f' %start.plan_args.start|float}}    {{'%0.3f' %start.plan_args.stop|float}} {{ start.motors[1]}}  {{'%0.3f' %start.plan_args.start|float}}    {{'%0.3f' %start.plan_args.stop|float}} {{start.plan_args.num}} ['{{ start.uid[:6] }}'] (scan num: {{ start.scan_id }})"""




 

count_template = """{{- start.plan_name}} :  {{start.plan_args.num}} ['{{ start.uid[:6] }}'] (scan num: {{ start.scan_id }}) (Measurement: {{start.Measurement}} )
Scan Plan
---------
{{ start.plan_type }}
{%- for k, v in start.plan_args | dictsort %}
    {{ k }}: {{ v }}
{%-  endfor %}
{% if 'signature' in start -%}
Call:
    {{ start.signature }}
{% endif %}
Metadata
--------
{% for k, v in start.items() -%}
{%- if k not in ['plan_type', 'plan_args'] -%}{{ k }} : {{ v }}
{% endif -%}
{%- endfor -%}
exposure time: TODO 
acquire  time: TODO 
"""


#single_motor_template = """{{- start.plan_name}} :  {{ start.motors[0]}} {{start.plan_args.start}} {{start.plan_args.stop}} {{start.plan_args.num}} ['{{ start.uid[:6] }}'] (scan num: {{ start.scan_id }})
single_motor_template = """{{- start.plan_name}} :  {{ start.motors[0]}}  {{'%0.3f' %start.plan_args.start|float}}    {{'%0.3f' %start.plan_args.stop|float}} {{start.plan_args.num}} ['{{ start.uid[:6] }}'] (scan num: {{ start.scan_id }})
Scan Plan
---------
{{ start.plan_type }}
{%- for k, v in start.plan_args | dictsort %}
    {{ k }}: {{ v }}
{%-  endfor %}
{% if 'signature' in start -%}
Call:
    {{ start.signature }}
{% endif %}
Metadata
--------
{% for k, v in start.items() -%}
{%- if k not in ['plan_type', 'plan_args'] -%}{{ k }} : {{ v }}
{% endif -%}
{%- endfor -%}
exposure time: TODO 
acquire  time: TODO 
"""

TEMPLATES = defaultdict(lambda: simple_template)
#TEMPLATES['ct'] = count_template
#TEMPLATES['count'] = count_template
#TEMPLATES['relative_scan'] = single_motor_template
#TEMPLATES['scan_nd'] = single_motor_template
#TEMPLATES['manual_count'] = manual_count_template
#TEMPLATES['dscan'] = single_motor_template
#TEMPLATES['ascan'] = single_motor_template
TEMPLATES['scan'] = single_motor_template
#TEMPLATES['ID_calibration'] = single_motor_template
TEMPLATES['grid_scan'] = grid_template


from jinja2 import Template


# connect olog
from functools import partial
from pyOlog import SimpleOlogClient


# Set up the logbook. This configures bluesky's summaries of
# data acquisition (scan type, ID, etc.).

LOGBOOKS = ['Data Acquisition']  # list of logbook names to publish to
simple_olog_client = SimpleOlogClient()
generic_logbook_func = simple_olog_client.log
configured_logbook_func = partial(generic_logbook_func, logbooks=LOGBOOKS)

# This is for ophyd.commands.get_logbook, which simply looks for
# a variable called 'logbook' in the global IPython namespace.
logbook = simple_olog_client


logbook_cb = logbook_cb_factory(configured_logbook_func, desc_dispatch=TEMPLATES)

def submit_to_olog(queue, cb):
    while True:
        name, doc = queue.get()  # waits until document is available
        try:
            cb(name, doc)
        except Exception as exc:
            warn('This olog is giving errors. This will not be logged.'
                 'Error:' + str(exc))

olog_queue = queue.Queue(maxsize=100)
olog_thread = threading.Thread(target=submit_to_olog, args=(olog_queue, logbook_cb), daemon=True)
olog_thread.start()

def send_to_olog_queue(name, doc):
    try:
        olog_queue.put((name, doc), block=False)
    except queue.Full:
        warn('The olog queue is full. This will not be logged.')

#RE.subscribe(send_to_olog_queue, 'start')




