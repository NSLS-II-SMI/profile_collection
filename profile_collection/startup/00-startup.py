# Make ophyd listen to pyepics.
from ophyd import setup_ophyd
setup_ophyd()

# Subscribe metadatastore to documents.
# If this is removed, data is not saved to metadatastore.
from bluesky.global_state import gs

from metadatastore.mds import MDS
from databroker import Broker
from databroker.core import register_builtin_handlers
from filestore.fs import FileStore
_mds_config = {"host": "xf12id-ca1",
	       "database": "datastore",
	       "port": 27017,
	       "timezone": "US/Eastern"
	       }
mds = MDS(_mds_config, auth=False)

_fs_config = {"host": "xf12id-ca1",
	      "database": "filestore",
	      "port": 27017
	      }

db = Broker(mds, FileStore(_fs_config))
register_builtin_handlers(db.fs)
# hook run engine up to metadatastore

gs.RE.subscribe_lossless('all', mds.insert)

# # At the end of every run, verify that files were saved and
# # print a confirmation message.
# from bluesky.callbacks.broker import verify_files_saved
# gs.RE.subscribe('stop', post_run(verify_files_saved))

# Import matplotlib and put it in interactive mode.
import matplotlib.pyplot as plt
plt.ion()

# Make plots update live while scans run.
from bluesky.utils import install_qt_kicker
install_qt_kicker()

# convenience imports
from ophyd.commands import *
from bluesky.callbacks import *
from bluesky.spec_api import *
from bluesky.global_state import gs, abort, stop, resume
#from databroker import (DataBroker as db, get_events, get_images,
#                        get_table, get_fields, restream, process)
from time import sleep
import numpy as np

RE = gs.RE  # convenience alias
RE.subscribe('all', mds.insert)
RE.md['beamline_id'] = 'SMI'


# Uncomment the following lines to turn on verbose messages for debugging.
# import logging
# ophyd.logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)


from functools import partial
from pyOlog import SimpleOlogClient
from bluesky.callbacks.olog import logbook_cb_factory

# Set up the logbook. This configures bluesky's summaries of
# data acquisition (scan type, ID, etc.).

LOGBOOKS = ['Commissioning']  # list of logbook names to publish to
simple_olog_client = SimpleOlogClient()
generic_logbook_func = simple_olog_client.log
configured_logbook_func = partial(generic_logbook_func, logbooks=LOGBOOKS)

cb = logbook_cb_factory(configured_logbook_func)

def safe_cb(name, doc):
    "If olog raises an error, print it and move on."
    try:
        cb(name, doc)
    except Exception as exc:
        print('Olog raised an error. We will ignore it. Error:', exc)

RE.subscribe('start', safe_cb)

# This is for ophyd.commands.get_logbook, which simply looks for
# a variable called 'logbook' in the global IPython namespace.
logbook = simple_olog_client


