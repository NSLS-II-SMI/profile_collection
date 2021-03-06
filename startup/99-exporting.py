import logging
import os
import time as ttime

import numpy as np
import pandas as pd
from databroker.core import SingleRunCache
from event_model import RunRouter

logger = logging.getLogger('bluesky')
logger.setLevel('INFO')


def export_spectra_to_csv(run, *, dir, common_column, columns):
    """Export spectra to a CSV file based on databroker.v2 run.

    Parameters:
    -----------
    run: BlueskyRun
        a BlueskyRun, retrieved such as ``run = db.v2['eac4a441']``
    dir: str
        a directory where the target files should be saved to
    columns: list or None, optional
        a list of columns to export to the CSV file. If None, all
        columns will be attempted to be exported (must have the same
        dimensions)
    """
    xr = run.primary.read()
    if columns is None:
        columns = list(xr.keys())

    all_columns = [common_column] + columns
    xr = xr[all_columns]

    num_events = xr.dims['time']

    before_loop_time = ttime.time()
    logger.info(f'Start exporting of {num_events} spectra to {dir}')
    for i in range(num_events):
        file = os.path.join(dir,
                            f"{run.metadata['start']['uid']}-{i+1:05d}.csv")

        data = getattr(xr, common_column)[i]
        for j in range(len(columns)):
            data = np.vstack([data, getattr(xr, columns[j])[i]])
        data = data.T

        df = pd.DataFrame(data=data, columns=all_columns)

        start_time = ttime.time()
        logger.info(f'Exporting data with shape {data.shape} to {file}...')
        df.to_csv(file, index=False)
        logger.info(f'Exporting to {file} took '
                    f'{ttime.time() - start_time:.5f}s\n')

    logger.info(f'Exporting of {num_events} spectra took '
                f'{ttime.time() - before_loop_time:.5f}s')


def factory(name, doc):
    src = SingleRunCache()

    def export_on_stop(name, doc):
        if name == "stop":
            run = src.retrieve()
            if 'amptek' in run.metadata['start']['detectors']:
                export_spectra_to_csv(run, dir="/tmp/CSV-export/",
                                      common_column='amptek_energy_channels',
                                      columns=['amptek_mca_spectrum'])

    return [src.callback, export_on_stop], []


rr = RunRouter([factory])
RE.subscribe(rr)  # noqa F821
