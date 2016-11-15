from bluesky.plans import one_1d_step
import bluesky.plans as bp

def cam_scan(detectors, motor, start, stop, num, *, md=None, idle_time=0):
    
    def per_step(dets, motor, step):
        print('INNER STEP', step)
        yield from one_1d_step(dets, motor, step)
        yield from bp.sleep(idle_time)

    return (yield from bp.subs_wrapper(
        bp.scan(detectors, motor, start, stop, num, per_step=per_step, md=md),
        LiveTable(detectors + [motor]))
    )

