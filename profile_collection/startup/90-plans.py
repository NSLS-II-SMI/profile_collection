from bluesky.plans import one_1d_step
import bluesky.plans as bp
from collections import ChainMap

def cam_scan(detectors, motor, start, stop, num, *, md=None, idle_time=0):
    
    def per_step(dets, motor, step):
        yield from one_1d_step(dets, motor, step)
        yield from bp.sleep(idle_time)

    if md is None:
        md = {}
    md = ChainMap(
        md,
        {'plan_args': {'detectors': list(map(repr, detectors)), 'num': num,
                       'motor': repr(motor),
                       'start': start, 'stop': stop,
                       'per_step': repr(per_step),
                       'idle_time': float(idle_time)},
         'plan_name': 'cam_scan',
         })

    return (yield from bp.subs_wrapper(
        bp.scan(detectors, motor, start, stop, num, per_step=per_step, md=md),
        LiveTable(detectors + [motor]))
    )

