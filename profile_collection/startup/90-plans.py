from bluesky.plan_stubs import one_1d_step, abs_set, wait, sleep
import bluesky.plans as bp
import time
from collections import ChainMap



def ramya1():
    sample_id(user_name='plant', sample_name='mesoendo_waxd')
    RE(bp.grid_scan([pil300KW, pil1M, pil300kwroi2, pil300kwroi3, pil300kwroi4], waxs.arc, 6, 30, 5, stage.x, 7.29, 7.34, 3, 0,  stage.y, -7.35, -6.1, 251, 0))
   #sample_id(user_name='plant', sample_name='coarse1')
   #RE(bp.grid_scan([pil300KW, pil1M, pil300kwroi2, pil300kwroi3, pil300kwroi4], stage.x, 7.77, 7.82, 3, stage.y, -9, -5.9, 63, 0, waxs.arc, 6, 30, 5, 1))
   # sample_id(user_name='test', sample_name='stylusLine')
   # stage.x.move(9.74)
   # stage.y.move(-8.42)
   # RE(bp.scan([pil300KW, pil300kwroi2, pil300kwroi3, pil300kwroi4], sample.y, -8.42, -8.33, 2))
    


def scan(detectors, motor, start, stop, num, md=None, idle_time=1):

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



def cam_scan(detectors, camera, motor, start, stop, num, md=None, idle_time=1):

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
