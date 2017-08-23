from bluesky.callbacks.broker import LiveTiffExporter
from bluesky.callbacks.broker import post_run


# a template that sorts files into directories based user and scan ID
template_1M = "/data/1M/images/user/{start[remark]}_{event[seq_num]}_{i}.tiff"
template_300KW = "/data/300KW/images/user/{start[remark]}_{event[seq_num]}_{i}.tiff"

exporter_1M = LiveTiffExporter('pil1M_image', template_1M, db=db)
exporter_300KW = LiveTiffExporter('pil300KW_image', template_300KW, db=db)

try:
    token1
except NameError:
    # first time running the file -- nothing to unsubscribe
    pass
else:
    # remove old subscriptions before adding new ones, below
    RE.unsubscribe(token1)
    RE.unsubscribe(token2)


token1 = RE.subscribe('all', post_run(exporter_1M, db=db))
token2 = RE.subscribe('all', post_run(exporter_300KW, db=db))
