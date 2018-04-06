#!/usr/bin/python

import matplotlib.ticker as mtick
get_fields = db.get_fields
get_images = db.get_images
get_table = db.get_table


from lmfit import  Model
from lmfit import minimize, Parameters, Parameter, report_fit
from scipy.special import erf

# TODO: create a conda package for it and include to collection profiles
import peakutils


def get_scan(scan_id, debug=False):
    """Get scan from databroker using provided scan id.
from Maksim
    :param scan_id: scan id from bluesky.
    :param debug: a debug flag.
    :return: a tuple of scan and timestamp values.
    """
    scan = db[scan_id]
    #t = datetime.datetime.fromtimestamp(scan['start']['time']).strftime('%Y-%m-%d %H:%M:%S')
    #t = dtt.datetime.fromtimestamp(scan['start']['time']).strftime('%Y-%m-%d %H:%M:%S')
    t='N.A. conflicting with other macro'
    if debug:
        print(scan)
    print('Scan ID: {}  Timestamp: {}'.format(scan_id, t))
    return scan, t

def get_data(scan_id, field='ivu_gap', intensity_field='elm_sum_all', det=None, debug=False):
    """Get data from the scan stored in the table.
from Maksim
    :param scan_id: scan id from bluesky.
    :param field: visualize the intensity vs. this field.
    :param intensity_field: the name of the intensity field.
    :param det: the name of the detector.
    :param debug: a debug flag.
    :return: a tuple of X, Y and timestamp values.
    """
    scan, t = get_scan(scan_id)
    if det:
        imgs = get_images(scan, det)
        im = imgs[-1]
        if debug:
            print(im)

    table = get_table(scan)
    fields = get_fields(scan)

    if debug:
        print(table)
        print(fields)
    x = table[field]
    y = table[intensity_field]

    return x, y, t


def ps(uid='-1',det='default',suffix='default',shift=.5,logplot='off'):
    '''
    YG Copied from CHX beamline@March 18, 2018
    function to determine statistic on line profile (assumes either peak or erf-profile)
    calling sequence: uid='-1',det='default',suffix='default',shift=.5)
    det='default' -> get detector from metadata, otherwise: specify, e.g. det='eiger4m_single'
    suffix='default' -> _stats1_total / _sum_all, otherwise: specify, e.g. suffix='_stats2_total'
    shift: scale for peak presence (0.5 -> peak has to be taller factor 2 above background)
    '''
    #import datetime
    #import time
    #import numpy as np
    #from PIL import Image
    #from databroker import db, get_fields, get_images, get_table
    #from matplotlib import pyplot as pltfrom
    #from lmfit import  Model
    #from lmfit import minimize, Parameters, Parameter, report_fit
    #from scipy.special import erf

    # get the scan information:
    if uid == '-1':
        uid=-1
    if det == 'default':
        if db[uid].start.detectors[0] == 'elm' and suffix=='default':
            intensity_field='elm_sum_all'
        elif db[uid].start.detectors[0] == 'elm':
            intensity_field='elm'+suffix
        elif suffix == 'default':
            intensity_field= db[uid].start.detectors[0]+'_stats1_total'
        else:
            intensity_field= db[uid].start.detectors[0]+suffix
    else:
        if det=='elm' and suffix == 'default':
            intensity_field='elm_sum_all'
        elif det=='elm':
            intensity_field = 'elm'+suffix
        elif suffix == 'default':
            intensity_field=det+'_stats1_total'
        else:
            intensity_field=det+suffix

    field = db[uid].start.motors[0]

    #field='dcm_b';intensity_field='elm_sum_all'
    [x,y,t]=get_data(uid,field=field, intensity_field=intensity_field, det=None, debug=False)  #need to re-write way to get data
    x=np.array(x)
    y=np.array(y)

    PEAK=x[np.argmax(y)]
    PEAK_y=np.max(y)
    COM=np.sum(x * y) / np.sum(y)

    ### from Maksim: assume this is a peak profile:
    def is_positive(num):
        return True if num > 0 else False

    # Normalize values first:
    ym = (y - np.min(y)) / (np.max(y) - np.min(y)) - shift  # roots are at Y=0

    positive = is_positive(ym[0])
    list_of_roots = []
    for i in range(len(y)):
        current_positive = is_positive(ym[i])
        if current_positive != positive:
            list_of_roots.append(x[i - 1] + (x[i] - x[i - 1]) / (abs(ym[i]) + abs(ym[i - 1])) * abs(ym[i - 1]))
            positive = not positive
    if len(list_of_roots) >= 2:
        FWHM=abs(list_of_roots[-1] - list_of_roots[0])
        CEN=list_of_roots[0]+0.5*(list_of_roots[1]-list_of_roots[0])
        ps.fwhm=FWHM
        ps.cen=CEN
        #return {
        #    'fwhm': abs(list_of_roots[-1] - list_of_roots[0]),
        #    'x_range': list_of_roots,
       #}
    else:    # ok, maybe it's a step function..
        print('no peak...trying step function...')
        ym = ym + shift
        def err_func(x, x0, k=2, A=1,  base=0 ):     #### erf fit from Yugang
            return base - A * erf(k*(x-x0))
        mod = Model(  err_func )
        ### estimate starting values:
        x0=np.mean(x)
        #k=0.1*(np.max(x)-np.min(x))
        pars  = mod.make_params( x0=x0, k=2,  A = 1., base = 0. )
        result = mod.fit(ym, pars, x = x )
        CEN=result.best_values['x0']
        FWHM = result.best_values['k']
        ps.cen = CEN
        ps.fwhm = FWHM

    ### re-plot results:
    if logplot=='on':
        plt.close(999)
        plt.figure(999)
        plt.semilogy([PEAK,PEAK],[np.min(y),np.max(y)],'k--',label='PEAK')
        plt.hold(True)
        plt.semilogy([CEN,CEN],[np.min(y),np.max(y)],'r-.',label='CEN')
        plt.semilogy([COM,COM],[np.min(y),np.max(y)],'g.-.',label='COM')
        plt.semilogy(x,y,'bo-')
        plt.xlabel(field);plt.ylabel(intensity_field)
        plt.legend()
        plt.title('uid: '+str(uid)+' @ '+str(t)+'\nPEAK: '+str(PEAK_y)[:8]+' @ '+str(PEAK)[:8]+'   COM @ '+str(COM)[:8]+ '\n FWHM: '+str(FWHM)[:8]+' @ CEN: '+str(CEN)[:8],size=9)
        plt.show()
    else:
        plt.close(999)
        plt.figure(999)
        plt.plot([PEAK,PEAK],[np.min(y),np.max(y)],'k--',label='PEAK')
        plt.hold(True)
        plt.plot([CEN,CEN],[np.min(y),np.max(y)],'r-.',label='CEN')
        plt.plot([COM,COM],[np.min(y),np.max(y)],'g.-.',label='COM')
        plt.plot(x,y,'bo-')
        plt.xlabel(field);plt.ylabel(intensity_field)
        plt.legend()
        plt.title('uid: '+str(uid)+' @ '+str(t)+'\nPEAK: '+str(PEAK_y)[:8]+' @ '+str(PEAK)[:8]+'   COM @ '+str(COM)[:8]+ '\n FWHM: '+str(FWHM)[:8]+' @ CEN: '+str(CEN)[:8],size=9)
        plt.show()

    ### assign values of interest as function attributes:
    ps.peak=PEAK
    ps.com=COM



pv_th = 'XF:12IDC-OP:2{HEX:Stg-Ax:theta}'
pv_y =  'XF:12IDC-OP:2{HEX:Stg-Ax:Y}'


def set_abs_value( pv_prefix, abs_value ):
    """
    Use an absolute value for a PV
    Input
    ---
    pv_prefix:string, the prefix of a pv, e.g., 'XF:11IDB-ES{Dif-Ax:YV}' for diff.yv
    abs_value, float, the absolute value to be set

    Example:
    set_abs_value( 'XF:11IDB-ES{Dif-Ax:YV}', 0 ) #set diff.yv abolute value to 0
    """
    pv_set = pv_prefix  + 'Mtr.VAL'
    pv_use_button = pv_prefix + 'Mtr.SET'
    caput( pv_use_button, 'Set')
    old_val = caget( pv_set )
    #import bluesky.plans as bp
    #yield from bp.abs_set( pv_set, abs_value)  not working
    caput( pv_set, abs_value )
    caput( pv_use_button, 'Use')
    print('The absolute value of %s was changed from %s to %s.'%(pv_set, old_val, abs_value))










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

attn_shutter = TwoButtonShutter('XF:12IDC-OP:2{Fltr:1-8}', name='attn_shutter')
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
    from bluesky.plans import Msg
    from bluesky.preprocessors import trigger_and_read
    from bluesky.plan_stubs import mv, _short_uid
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


def one_nd_step_check_beam(detectors, step, pos_cache): 
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
    # this means "put the attenuator in the beam"
    yield from mv(attn_shutter, 'Insert')
    return ret



def one_1d_step_check_beam( detectors, motor, step ):
    from bluesky.plans import Msg
    from bluesky.preprocessors import trigger_and_read
    from bluesky.plan_stubs import mv, _short_uid
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

def e_grid_scan(*args, **kwargs):
    return (yield from bp.grid_scan(*args, per_step=one_nd_step_pseudo_shutter, **kwargs))



def find_peaks_peakutils(uid='8537b7', x='stage_x', y='pil300KW_stats1_total', plot=True):
    xx = np.array(db[uid].table()[x])
    yy = np.array(db[uid].table()[y])
    peak_idx = peakutils.interpolate(xx, yy, width=0)

    if plot:
        plt.plot(xx, yy)
        plt.grid()
        plt.scatter(xx[peak_idx], yy[peak_idx], c='r')

    print(f'Peaks indices: {peak_idx}\nX coords: {xx[peak_idx]}\nY coords: {yy[peak_idx]}')

    return peak_idx, xx[peak_idx], yy[peak_idx]

