print(f"Loading {__file__}")

###############################################################################
# TODO: remove this block once https://github.com/bluesky/ophyd/pull/959 is
# merged/released.
from datetime import datetime
from ophyd.signal import EpicsSignalBase, EpicsSignal, DEFAULT_CONNECTION_TIMEOUT


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

# from bluesky.utils import PersistentDict
from pathlib import Path

import appdirs


try:
    from bluesky.utils import PersistentDict
except ImportError:
    import msgpack
    import msgpack_numpy
    import zict

    class PersistentDict(zict.Func):
        """
        A MutableMapping which syncs it contents to disk.
        The contents are stored as msgpack-serialized files, with one file per item
        in the mapping.
        Note that when an item is *mutated* it is not immediately synced:
        >>> d['sample'] = {"color": "red"}  # immediately synced
        >>> d['sample']['shape'] = 'bar'  # not immediately synced
        but that the full contents are synced to disk when the PersistentDict
        instance is garbage collected.
        """

        def __init__(self, directory):
            self._directory = directory
            self._file = zict.File(directory)
            self._cache = {}
            super().__init__(self._dump, self._load, self._file)
            self.reload()

            # Similar to flush() or _do_update(), but without reference to self
            # to avoid circular reference preventing collection.
            # NOTE: This still doesn't guarantee call on delete or gc.collect()!
            #       Explicitly call flush() if immediate write to disk required.
            def finalize(zfile, cache, dump):
                zfile.update((k, dump(v)) for k, v in cache.items())

            import weakref

            self._finalizer = weakref.finalize(
                self, finalize, self._file, self._cache, PersistentDict._dump
            )

        @property
        def directory(self):
            return self._directory

        def __setitem__(self, key, value):
            self._cache[key] = value
            super().__setitem__(key, value)

        def __getitem__(self, key):
            return self._cache[key]

        def __delitem__(self, key):
            del self._cache[key]
            super().__delitem__(key)

        def __repr__(self):
            return f"<{self.__class__.__name__} {dict(self)!r}>"

        @staticmethod
        def _dump(obj):
            "Encode as msgpack using numpy-aware encoder."
            # See https://github.com/msgpack/msgpack-python#string-and-binary-type
            # for more on use_bin_type.
            return msgpack.packb(obj, default=msgpack_numpy.encode, use_bin_type=True)

        @staticmethod
        def _load(file):
            return msgpack.unpackb(file, object_hook=msgpack_numpy.decode, raw=False)

        def flush(self):
            """Force a write of the current state to disk"""
            for k, v in self.items():
                super().__setitem__(k, v)

        def reload(self):
            """Force a reload from disk, overwriting current cache"""
            self._cache = dict(super().items())


runengine_metadata_dir = appdirs.user_data_dir(appname="bluesky") / Path(
    "runengine-metadata"
)
print('starting RE.md link')
# PersistentDict will create the directory if it does not exist
RE.md = PersistentDict(runengine_metadata_dir)
print('finished RE.md link')
RE.md["beamline_name"] = "SMI"
RE.md["facility"] = "NSLS-II"
RE.md["optional_comments"] = ""  # Any comment can be added if needed
