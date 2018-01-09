from bluesky.plan_stubs import one_1d_step, abs_set, wait
import bluesky.plans as bp
import time
from collections import ChainMap



def ramya1():
    sample_id(user_name='BSpec_RT_FullSample_Meso_Endo', sample_name='Coarse_Scan')
    RE(bp.outer_product_scan([pil1M, pil300KW, pil1mroi2, pil1mroi3, pil300kwroi2, pil300kwroi3, pil300kwroi4, ssacurrent], sample.x, 16.723, 16.775, 3, sample.y, -4.134, -3.134, 21, 0,  waxs.arc, 5, 29, 5, 1))

'''

def scan(detectors, motor, start, stop, num, md=None, idle_time=0):

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

'''

