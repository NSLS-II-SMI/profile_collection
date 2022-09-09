import logging
import os
import time as ttime

from bluesky_live.bluesky_run import BlueskyRun, DocumentCache
import numpy as np
import pandas as pd
from event_model import RunRouter

from pathlib import Path
import event_model
import tqdm


logger = logging.getLogger("bluesky")
logger.setLevel("INFO")


def export_scan(sid, filename="", path="/home/xf12id/users/", verbose=True):
    """
    Export table by giving a scan id
    """
    hdr = db[sid]
    d = hdr.table()
    output = path + "sid=%s.csv" % (filename)
    d.to_csv(output)
    if verbose:
        print("The table of sid=%s is saved as %s." % (sid, output))


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

    num_events = xr.dims["time"]

    before_loop_time = ttime.time()
    logger.info(f"Start exporting of {num_events} spectra to {dir}")
    for i in range(num_events):
        file = os.path.join(
            dir,
            f"{run.metadata['start']['sample_name']}-{run.metadata['start']['uid'].split('-')[0]}-{i+1:05d}.csv",
        )

        data = getattr(xr, common_column)[i]
        for j in range(len(columns)):
            data = np.vstack([data, getattr(xr, columns[j])[i]])
        data = data.T

        df = pd.DataFrame(data=data, columns=all_columns)

        start_time = ttime.time()
        logger.info(f"Exporting data with shape {data.shape} to {file}...")
        df.to_csv(file, index=False)
        logger.info(f"Exporting to {file} took " f"{ttime.time() - start_time:.5f}s\n")

    logger.info(
        f"Exporting of {num_events} spectra took "
        f"{ttime.time() - before_loop_time:.5f}s"
    )


def factory(name, doc):
    # We will stream documents into this cache.
    # When the run is complete, we will build an in-memory BlueskyRun from it.
    dc = DocumentCache()

    def export_on_stop(name, doc):
        if name == "stop":
            # in-memory BlueskyRun built from DocumentCache
            run = BlueskyRun(dc)
            if "amptek" in run.metadata["start"]["detectors"]:
                # retreive information from the start document
                cycle = run.metadata["start"]["cycle"]
                propos = (
                    run.metadata["start"]["proposal_number"]
                    + "_"
                    + run.metadata["start"]["main_proposer"]
                )
                direc = "/nsls2/xf12id2/data/images/users/%s/%s/Amptek/" % (
                    cycle,
                    propos,
                )

                # create a new directory
                try:
                    os.stat(direc)
                except FileNotFoundError:
                    os.makedirs(direc)
                    os.chmod(direc, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)

                export_spectra_to_csv(
                    run,
                    dir=direc,
                    common_column="amptek_energy_channels",
                    columns=["amptek_mca_spectrum"],
                )

    return [dc, export_on_stop], []


def get_symlink_pairs(target_path, *, det_map, root_map=None):
    """
    Coroutine to sort out what to link to what.

    Parameters
    ----------
    target_path : Path
        The base directory to put the symlinks in.  They will be further nested.

    det_map : dict[str, str]
        A dictionaly mapping the detector name (1M, 900KW) to the type of measurement (SAXS, WAXS)
    root_map : dict[str, str], optional
        A mapping of root in the resource document -> a new path as in databroker

    Sends
    -----
    name, doc : str, Document
        The standard event model input!

    Returns
    -------
    list[tuple[str, Path, Path]]
         A tuple of the start uid, the source path and the destination path.
    """
    if root_map is None:
        root_map = {}
    links = []
    target_template: str
    output_path: str
    resource_info = {}
    datum_info = {}
    target_keys = set()
    while True:
        inp = yield
        if inp is None:
            break
        name, doc = inp
        if name == "start":
            start_uid = doc["uid"]
            output_path = Path(*Path(doc["path"]).parts[-2:])

            target_template = f'{output_path}/{{det_name}}/{doc["user_name"]}_{doc["sample_name"]}_id{doc["scan_id"]}_{{N:06d}}_{{det_type}}.tif'

        elif name == "resource":
            # we only handle AD TIFF
            if doc["spec"] != "AD_TIFF":
                continue
            doc_root = doc["root"]
            resource_info[doc["uid"]] = {
                "path": Path(root_map.get(doc_root, doc_root)) / doc["resource_path"],
                "kwargs": doc["resource_kwargs"],
            }
        elif "datum" in name:
            if name == "datum":
                doc = event_model.pack_datum_page(doc)

            for datum_uid, point_number in zip(
                doc["datum_id"], doc["datum_kwargs"]["point_number"]
            ):
                datum_info[datum_uid] = (
                    resource_info[doc["resource"]],
                    point_number,
                )
        elif name == "descriptor":
            for k, v in doc["data_keys"].items():
                if "external" in v:
                    target_keys.add(k)
        elif "event" in name:
            if name == "event":
                doc = event_model.pack_event_page(doc)
            for key in target_keys:
                det, _, _ = key.partition("_")
                det_name = det[3:]
                det_type = det_map[det_name]

                if key not in doc["data"]:
                    continue
                for datum_id in doc["data"][key]:
                    resource_vals, point_number = datum_info[datum_id]
                    orig_template = resource_vals["kwargs"]["template"]
                    assert resource_vals["kwargs"]["frame_per_point"] == 1
                    base_fname = resource_vals["kwargs"]["filename"]
                    source_path = Path(
                        orig_template
                        % (str(resource_vals["path"]) + "/", base_fname, point_number)
                    )
                    dest_path = target_path / target_template.format(
                        det_name=det_name, N=point_number + 1, det_type=det_type
                    )
                    links.append((start_uid, source_path, dest_path))
        elif name == "stop":
            break

    return links


def do_single_header_symlinks(
    header,
    target_path=Path("/nsls2/data/smi/legacy/results/data"),
    *,
    overwrite_dest=False,
    det_map=None,
):
    if det_map is None:
        det_map = {"900KW": "WAXS", "1M": "SAXS"}
    gen = get_symlink_pairs(Path(target_path), det_map=det_map)
    gen.send(None)
    try:
        for name, doc in header.documents():
            gen.send((name, doc))
    except StopIteration as ex:
        links = ex.value

    return do_symlinking(links, overwrite_dest=overwrite_dest)


def get_all_symlinks(headers, target_path, det_map=None):
    """
    Get the symlinks for all of the headers in a catalog.

    Parameters
    ----------
    headers : Catalog
        Needs to support ``obj.values_inedxer``
    target_path : Path
        The base path for the symlinks

    det_map : dict[str, str], optional
        A dictionaly mapping the detector name (1M, 900KW) to the type of measurement (SAXS, WAXS)

    Returns
    -------
    list[tuple[str, Path, Path]]
         A tuple of the start uid, the source path and the destination path.
    """
    if det_map is None:
        det_map = {"900KW": "WAXS", "1M": "SAXS"}
    links = []
    for h in tqdm.tqdm(headers.values_indexer):

        gen = get_symlink_pairs(Path(target_path), det_map=det_map)
        gen.send(None)
        try:
            for name, doc in h.documents():
                gen.send((name, doc))
        except StopIteration as ex:
            links.extend(ex.value)
    return links


def do_symlinking(
    links: list[tuple[str, Path, Path]],
    overwrite_dest=False,
) -> tuple[list[tuple[str, Path, Path]], list[tuple[str, Path, Path]]]:
    """
    Create the symlinks, making target directories as needed.

    Paramaters
    ----------
    links : list of (uid, src, dest) tuples
        The uid, source file and destination files

    overwrite_dest : bool, optional
        If an existing destitation should be unlinked and replaced.

    Returns
    -------
    linked, failed : list of (uid, src, dest) tuples
        The linked (or failed) values.
    """
    failed = []
    linked = []
    for uid, src, dest in tqdm.tqdm(links, leave=False):
        if not src.exists():
            failed.append((uid, src, dest))
            continue
        try:
            dest.parent.mkdir(exist_ok=True, parents=True)
            if overwrite_dest and dest.exists():
                dest.unlink()
            dest.symlink_to(src)
        except Exception:
            failed.append((uid, src, dest))
        else:
            linked.append((uid, src, dest))
    return linked, failed


def symlink_factory_factory(target_path, det_map=None):
    """
    Build a factory to pass to RunRouter bound to the taregt path

    Parameters
    ----------
    target_path : Path
        The base directory to put the symlinks in.  They will be further nested.

    det_map : dict[str, str]
        A dictionaly mapping the detector name (1M, 900KW) to the type of measurement (SAXS, WAXS)

    Returns
    -------
    factory
        A function that matches the signature for the input to RunRouter
    """
    if det_map is None:
        det_map = {"900KW": "WAXS", "1M": "SAXS"}

    def symlink_factory(name, doc):
        """
        Set up a callback per run start.
        """
        gen = get_symlink_pairs(Path(target_path), det_map=det_map)
        gen.send(None)  # Prime the pump

        def symlink_callback(name, doc):
            """
            The actual callback that will see the documents
            """
            try:
                gen.send((name, doc))
            except StopIteration as ex:
                _, failed = do_symlinking(
                    # The list of files we need to link
                    ex.value,
                    # YOLO
                    overwrite_dest=True,
                )
                if len(failed):
                    raise Exception("failed to link some files", failed)

        return [symlink_callback], []

    return symlink_factory


rr = RunRouter(
   [
       factory,
       symlink_factory_factory("/nsls2/data/smi/legacy/results/data"),
    ]
)
export_cid = RE.subscribe(rr)  # noqa F821
