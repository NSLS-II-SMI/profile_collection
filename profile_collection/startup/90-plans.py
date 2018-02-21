from bluesky.plan_stubs import one_1d_step, abs_set, wait, sleep
import bluesky.plans as bp
import time
from collections import ChainMap



def ramya1():
    sample_id(user_name='BSpec_RT_FullSample_Meso_Endo', sample_name='Coarse_Scan')
    RE(bp.outer_product_scan([pil1M, pil300KW, pil1mroi2, pil1mroi3, pil300kwroi2, pil300kwroi3, pil300kwroi4, ssacurrent], sample.x, 16.723, 16.775, 3, sample.y, -4.134, -3.134, 21, 0,  waxs.arc, 5, 29, 5, 1))



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
        bp.scan(detectors, motor, start, stop, num, per_step=per_step, md=md))
        #LiveTable(detectors + [motor]))
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


def dummy_one_nd_step(detectors, step, pos_cache ):
    """
    Jan 18, created by Yugang@SMI

    Use for adding some functions between each step of nd scan

    """
    from bluesky.plans import Msg
    from bluesky.preprocessors import trigger_and_read
    from bluesky.plan_stubs import mv, _short_uid
    def move():
        yield Msg('checkpoint')
        grp = _short_uid('set')
        for motor, pos in step.items():
            if pos == pos_cache[motor]:
                # This step does not move this motor.
                continue
            yield Msg('set', motor, pos, group=grp)
            pos_cache[motor] = pos
        yield Msg('wait', None, group=grp)
    motors = step.keys()
    yield from move()
    ret = (yield from trigger_and_read(list(detectors) + list(motors)))
    return ret


def dummy_mesh(detectors, motor1, start1, stop1, num1, motor2, start2, stop2, num2, snake2, motor3, start3, stop3, num3,snake3, idle_time=0):
    def per_step( dmx,dmy,dmz):
        #yield from bps.one_nd_step(detectors, step, pos_cache)
        yield from dummy_one_nd_step( dmx,dmy,dmz )
        yield from sleep(idle_time)
        #print('Sleep %s sec here'%idle_time)
    #print(  md, pos_cache )
    yield from bp.grid_scan(detectors, motor1, start1, stop1, num1,  motor2, start2, stop2, num2, snake2, motor3, start3, stop3, num3,snake3, per_step=per_step)


def __dummy_mesh(detectors, *arg, idle_time=0, md=None):
    def per_step( dmx,dmy,dmz):
        yield from dummy_one_nd_step( dmx,dmy,dmz )
        yield from sleep(idle_time)
        print('Sleep %s sec here'%idle_time)
    yield from bp.grid_scan(detectors, *arg,per_step=per_step, md=md )


class FakeDetector(Device):
    acq_time = Cpt(Signal, value=10)

    _default_configuration_attrs = ('acq_time', )
    _default_read_attrs = ()

    def trigger(self):
        st = self.st = DeviceStatus(self)

        from threading import Timer

        self.t = Timer(self.acq_time.get(), st._finished)
        self.t.start()
        return st

fd = FakeDetector(name='fd')
