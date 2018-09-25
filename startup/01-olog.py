print(f'Loading {__file__}')

from bluesky.callbacks.olog import logbook_cb_factory
from functools import partial
from pyOlog import SimpleOlogClient
import queue
import threading
from warnings import warn

# Set up the logbook. This configures bluesky's summaries of
# data acquisition (scan type, ID, etc.).

LOGBOOKS = ['Commissioning']  # list of logbook names to publish to
simple_olog_client = SimpleOlogClient()
generic_logbook_func = simple_olog_client.log
configured_logbook_func = partial(generic_logbook_func, logbooks=LOGBOOKS)

# This is for ophyd.commands.get_logbook, which simply looks for
# a variable called 'logbook' in the global IPython namespace.
logbook = simple_olog_client

cb = logbook_cb_factory(configured_logbook_func)



def submit_to_olog(queue, cb):
    while True:
        name, doc = queue.get()  # waits until document is available
        try:
            cb(name, doc)
        except Exception as exc:
            warn('This olog is giving errors. This will not be logged.'
                 'Error:' + str(exc))

olog_queue = queue.Queue(maxsize=100)
olog_thread = threading.Thread(target=submit_to_olog, args=(olog_queue, cb), daemon=True)
olog_thread.start()

def send_to_olog_queue(name, doc):
    try:
        olog_queue.put((name, doc), block=False)
    except queue.Full:
        warn('The olog queue is full. This will not be logged.')

RE.subscribe(send_to_olog_queue, 'start')
