print(f"Loading {__file__}")

###############################################################################
# TODO: remove this block once https://github.com/bluesky/ophyd/pull/959 is
# merged/released.
from datetime import datetime
from ophyd.signal import EpicsSignalBase, EpicsSignal, DEFAULT_CONNECTION_TIMEOUT
import redis
from redis_json_dict import RedisJSONDict


def print_now():
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S.%f")


def wait_for_connection_base(self, timeout=DEFAULT_CONNECTION_TIMEOUT):
    """Wait for the underlying signals to initialize or connect"""
    if timeout is DEFAULT_CONNECTION_TIMEOUT:
        timeout = self.connection_timeout
    # print(f'{print_now()}: waiting for {self.name} to connect within {timeout:.4f} s...')
    start = time.time()
    try:
        self._ensure_connected(self._read_pv, timeout=timeout)
        # print(f'{print_now()}: waited for {self.name} to connect for {time.time() - start:.4f} s.')
    except TimeoutError:
        if self._destroyed:
            raise DestroyedError("Signal has been destroyed")
        raise


def wait_for_connection(self, timeout=DEFAULT_CONNECTION_TIMEOUT):
    """Wait for the underlying signals to initialize or connect"""
    if timeout is DEFAULT_CONNECTION_TIMEOUT:
        timeout = self.connection_timeout
    # print(f'{print_now()}: waiting for {self.name} to connect within {timeout:.4f} s...')
    start = time.time()
    self._ensure_connected(self._read_pv, self._write_pv, timeout=timeout)
    # print(f'{print_now()}: waited for {self.name} to connect for {time.time() - start:.4f} s.')


EpicsSignalBase.wait_for_connection = wait_for_connection_base
EpicsSignal.wait_for_connection = wait_for_connection
###############################################################################

from ophyd.signal import EpicsSignalBase

EpicsSignalBase.set_defaults(timeout=10, connection_timeout=10)

import warnings
import nslsii
from databroker import Broker
from ophyd import Signal

nslsii.configure_base(
    get_ipython().user_ns, "smi", bec_derivative=True, publish_documents_with_kafka=True
)
# Disable printing scan info
bec.disable_baseline()

# Populating oLog entries with scans, comment out to disable
nslsii.configure_olog(get_ipython().user_ns, subscribe=True)

from pathlib import Path
import appdirs


print('Starting linking RE.md with Redis')
redis_client = redis.Redis(host="info.smi.nsls2.bnl.gov")
RE.md = RedisJSONDict(redis_client, prefix="")
RE.md["beamline_name"] = "SMI"
RE.md["facility"] = "NSLS-II"
RE.md["optional_comments"] = ""  # Any comment can be added if needed
print('Finished linking RE.md to Redis')
