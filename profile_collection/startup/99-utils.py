#!/usr/bin/python

import matplotlib.ticker as mtick

def get_incident_angle(inc_y, ref_y, Ldet=1599, pixel_size=172 ):
   """Get incident beam angle by giving direct beam-y pixel and reflective beam-y pixel and sample-to-detector distance
      Input:
	inc_y: in pixel
        ref_y: in pixel
        Ldet: in mm
        pixel_size: in  um
   """

   return np.degrees( np.arctan2( (-ref_y + inc_y)*pixel_size*10**(-3), Ldet ) )/2


def plot_1d(scans, x='dsa_x', y='pil1M_stats1_total', grid=True, **kwargs):
    
    # plt.clf()
    # plt.cla()
    
    fig = plt.figure(figsize=(8, 5.5))
    ax = fig.add_subplot(111)    
    
    for s in scans:
        h = db[s]
        x_data = h.table()[x]
        y_data = h.table()[y]
        ax.plot(x_data, y_data, label=f"scan_id={h.start['scan_id']}", **kwargs)

    ax.legend()
    if grid:
        ax.grid()
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))    

    
class TwoButtonShutter(Device):
    # TODO this needs to be fixed in EPICS as these names make no sense
    # the vlaue comingout of the PV do not match what is shown in CSS
    open_cmd = Cpt(EpicsSignal, 'Cmd:Opn-Cmd', string=True)
    open_val = 'Open'

    close_cmd = Cpt(EpicsSignal, 'Cmd:Cls-Cmd', string=True)
    close_val = 'Not Open'

    status = Cpt(EpicsSignalRO, 'Pos-Sts', string=True)
    fail_to_close = Cpt(EpicsSignalRO, 'Sts:FailCls-Sts', string=True)
    fail_to_open = Cpt(EpicsSignalRO, 'Sts:FailOpn-Sts', string=True)
    # user facing commands
    open_str = 'Insert'
    close_str = 'Retract'

    def set(self, val):
        if self._set_st is not None:
            raise RuntimeError('trying to set while a set is in progress')

        cmd_map = {self.open_str: self.open_cmd,
                   self.close_str: self.close_cmd}
        target_map = {self.open_str: self.open_val,
                      self.close_str: self.close_val}

        cmd_sig = cmd_map[val]
        target_val = target_map[val]

        st = self._set_st = DeviceStatus(self)
        enums = self.status.enum_strs

        def shutter_cb(value, timestamp, **kwargs):
            value = enums[int(value)]
            if value == target_val:
                self._set_st._finished()
                self._set_st = None
                self.status.clear_sub(shutter_cb)

        cmd_enums = cmd_sig.enum_strs
        count = 0
        def cmd_retry_cb(value, timestamp, **kwargs):
            nonlocal count
            value = cmd_enums[int(value)]
            # ts = datetime.datetime.fromtimestamp(timestamp).strftime(_time_fmtstr)
            # print('sh', ts, val, st)
            count += 1
            if count > 5:
                cmd_sig.clear_sub(cmd_retry_cb)
                st._finished(success=False)
            if value == 'None':
                if not st.done:
                    time.sleep(.5)
                    cmd_sig.set(1)
                    ts = datetime.datetime.fromtimestamp(timestamp).strftime(_time_fmtstr)
                    print('** ({}) Had to reactuate shutter while {}ing'.format(ts, val))
                else:
                    cmd_sig.clear_sub(cmd_retry_cb)

        cmd_sig.subscribe(cmd_retry_cb, run=False)
        cmd_sig.set(1)
        self.status.subscribe(shutter_cb)


        return st

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_st = None
        self.read_attrs = ['status']

attn_shutter = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-4}', name='attn_shutter')
#fe_shutter =   TwoButtonShutter('XF:12ID-PPS{Sh:FE}', name='fe_shutter')
        
def one_nd_step_pseudo_shutter(detectors, step, pos_cache):
    """
    Inner loop of an N-dimensional step scan

    This is the default function for ``per_step`` param`` in ND plans.

    Parameters
    ----------
    detectors : iterable
        devices to read
    step : dict
        mapping motors to positions in this step
    pos_cache : dict
        mapping motors to their last-set positions
    """
    from bluesky.plans import Msg, trigger_and_read, mv, _short_uid
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
        # this means "take the attenuator out of the beam"
        yield from mv(attn_shutter, 'Retract')

    motors = step.keys()
    yield from move()
    ret = (yield from trigger_and_read(list(detectors) + list(motors)))
    # this means "put the attenuator in the beam"    
    yield from mv(attn_shutter, 'Insert')
    return ret
    

def one_1d_step_pseudo_shutter(detectors, motor, step):
    """
    Inner loop of a 1D step scan

    This is the default function for ``per_step`` param in 1D plans.
    """
    from bluesky.plans import Msg, trigger_and_read, mv, _short_uid
    def move():
        grp = _short_uid('set')
        yield Msg('checkpoint')
        yield Msg('set', motor, step, group=grp)
        yield Msg('wait', None, group=grp)
        yield from mv(attn_shutter, 'Retract')
        
    yield from move()
    ret = (yield from trigger_and_read(list(detectors) + [motor]))
    yield from mv(attn_shutter, 'Insert')
    return ret



def ring_check():
    if (ring_ops.value == 'Operations'
            and mstr_shutter_enable.value == 1
            and smi_shutter_enable.value == 1
            and ivu_permit.value == 1):
        ring_ok=1
        print('SR ring status: Operations, shutters and IVU enabled. All is OK')
    else:
        ring_ok=0
        print('SR ring status alert: check if shutters and/or IVU enabled! ')
    return ring_ok

def wait_for_ring():
        ring_ok=ring_check()
        if ring_ok==0:
                while ring_ok==0:
                        print('SR ring is down and/or beamline shutters and IVU not enabled...checking again in 5 minutes.')
                        sleep(300)
                        ring_ok=ring_check()
        if ring_ok==1: pass

#def shutter_check():

def one_nd_step_check_beam(detectors, step, pos_cache): 
    from bluesky.plans import Msg, trigger_and_read, mv, _short_uid
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
        # this means "take the attenuator out of the beam"
        yield from wait_for_ring()

    motors = step.keys()
    yield from move()
    ret = (yield from trigger_and_read(list(detectors) + list(motors)))
    # this means "put the attenuator in the beam"
    yield from mv(attn_shutter, 'Insert')
    return ret



def one_1d_step_check_beam( detectors, motor, step ):
    from bluesky.plans import Msg, trigger_and_read, mv, _short_uid
    def move():
        grp = _short_uid('set')
        yield Msg('checkpoint')
        yield Msg('set', motor, step, group=grp)
        yield Msg('wait', None, group=grp)
        #yield from mv( attn_shutter, 'Retract')
        yield from wait_for_ring()
        print('Check beam here.')

    yield from move()
    ret = (yield from trigger_and_read(list(detectors) + [motor]))
    #yield from mv(attn_shutter, 'Insert')
    return ret


def cscan(*args, **kwargs):
    return (yield from bp.scan(*args, per_step=one_1d_step_check_beam, **kwargs))

def c_inner_scan(*args, **kwargs):
    return (yield from bp.inner_product_scan(*args, per_step=one_nd_step_check_beam, **kwargs))

def escan(*args, **kwargs):
    return (yield from bp.scan(*args, per_step=one_1d_step_pseudo_shutter, **kwargs))

def e_inner_scan(*args, **kwargs):
    return (yield from bp.inner_product_scan(*args, per_step=one_nd_step_pseudo_shutter, **kwargs))



