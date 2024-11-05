print(f"Loading {__file__}")
from ophyd import TIFFPlugin
from ophyd.areadetector.filestore_mixins import FileStoreTIFFIterativeWrite


class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
    def __init__(self, *args, md=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._md = md
        self._asset_path = ''

    def describe(self):
        ret = super().describe()
        key = self.parent._image_name
        color_mode = self.parent.cam.color_mode.get(as_string=True)
        if color_mode == 'Mono':
            # Used by Pilatus
            ret[key]['shape'] = [
                self.parent.cam.num_images.get(),
                self.array_size.height.get(),
                self.array_size.width.get()
                ]

        elif color_mode in ['RGB1', 'Bayer']:
            # Used by cameras
            ret[key]['shape'] = [self.parent.cam.num_images.get(), *self.array_size.get()]
        else:
            raise RuntimeError("Should never be here")

        cam_dtype = self.data_type.get(as_string=True)
        type_map = {'UInt8': '|u1', 'UInt16': '<u2', 'Float32':'<f4', "Float64":'<f8', 'Int32':'<i4'}
        if cam_dtype in type_map:
            ret[key].setdefault('dtype_str', type_map[cam_dtype])

        return ret

    def get_frames_per_point(self):
        ret = super().get_frames_per_point()
        return ret

    def _update_paths(self):
        self.write_path_template = self.root_path_str + "%Y/%m/%d/"
        self.read_path_template = self.root_path_str + "%Y/%m/%d/"
        self.reg_root = self.root_path_str

    @property
    def root_path_str(self):
        return f"/nsls2/data/smi/proposals/{self._md['cycle']}/{self._md['data_session']}/assets/{self._asset_path}/"

    def stage(self):
        self._update_paths()
        return super().stage()


class TIFFPluginEnsuredOff(TIFFPlugin):
    """Add this as a component to detectors that do not write TIFFs."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stage_sigs.update([('auto_save', 'No')])
