print(f'Loading {__file__}')

# We assume this is being run in a namespace (e.g. an IPython profile startup
# script) where an instance of databroker.Broker named `db` is already defined.


from databroker_browser.qt import BrowserWindow, CrossSection, StackViewer
from bluesky.callbacks.mpl_plotting import LivePlot


search_result = lambda h: "{start[plan_name]} ['{start[uid]:.6}']".format(**h)
text_summary = lambda h: "This is a {start[plan_name]}.".format(**h)


def fig_dispatch(header, factory):
    if 'image_det' in header['start']['detectors']:
        fig = factory('Image Series')
        cs = CrossSection(fig)
        StackViewer(cs, db.get_images(header, 'image'))
    elif len(header['start'].get('motors', [])) == 1:
        motor, = header['start']['motors']
        main_det, *_ = header['start']['detectors']
        fig = factory("{} vs {}".format(main_det, motor))
        ax = fig.gca()
        lp = LivePlot(main_det, motor, ax=ax)
        db.process(header, lp)


def browse():
    return BrowserWindow(db, fig_dispatch, text_summary, search_result)

