from bluesky.plans import one_1d_step, abs_set, wait
import bluesky.plans as bp
import time
from collections import ChainMap

def itscan(detectors, motor, start, stop, num, md=None, idle_time=0):
    '''Idle time scan
    
    This is a stanard bp.scan with the addition of

      - idle_time between points
      - a LiveTable subscription by default
    
    '''

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
         'plan_name': 'itscan',
         })

    table = LiveTable(detectors + [motor])
    # liveplot = LivePlot('detectors', 'motor')
    @subs_decorator(table)
    # @subs_decorator(liveplot)
    def inner():
        yield from bp.scan(detectors, motor, start, stop, num,
                           per_step=per_step, md=md)
    yield from inner()


def cam_scan(detectors, camera, motor, start, stop, num, md=None, idle_time=0):
    
    def per_step(dets, motor, step):
        yield from one_1d_step(dets, motor, step)
        yield from bp.abs_set(camera, 1, wait=True)
        yield from bp.abs_set(camera, 0, wait=True)
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

