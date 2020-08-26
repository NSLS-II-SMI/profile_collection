import numpy as np
import pandas as pd

from databroker.core import SingleRunCache
from event_model import RunRouter


def export_spectra_to_csv(run, file, columns=None):
    """Export spectra to a CSV file based on databroker.v2 run.
    Parameters:
    -----------
    run: BlueskyRun
        a BlueskyRun, retrieved such as ``run = db.v2['eac4a441']``
    file: string or buffer
        a filename of the target file
    columns: list or None, optional
        a list of columns to export to the CSV file. If None, all
        columns will be attempted to be exported (must have the same
        dimensions)
    Returns:
    --------
    df: pandas.DataFrame
        the resulted pandas DataFrame with the columns.
    """
    xr = run.primary.read()
    if columns is None:
        columns = list(xr.keys())
    xr = xr[columns]
    data = np.vstack(list(xr.data_vars.values())).T
    df = pd.DataFrame(data=data, columns=columns)
    df.to_csv(file, index=False)
    return df


def factory(name, doc):
    src = SingleRunCache()

    def export_on_stop(name, doc):
        if name == "stop":
            run = src.retrieve()
            if 'amptek' in run.metadata['start']['detectors']:
                export_spectra_to_csv(run, f"/tmp/CSV-export/{run.metadata['start']['uid']}.csv",
                                      ['amptek_energy_channels', 'amptek_mca_spectrum'])

    return [src.callback, export_on_stop], []


rr = RunRouter([factory])
RE.subscribe(rr)