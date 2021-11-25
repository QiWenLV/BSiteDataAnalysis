import os
import pickle

from config.setting import Setting
from persist import persist


class PicklePersist(persist.IPersist):

    def __init__(self):
        setting = Setting()
        self.setting_dir_path = setting.setting_dir_path

    def write(self, to_sink, data, index=None):
        with open(self.setting_dir_path + os.sep + to_sink, "wb") as fp:
            pickle.dump(data, fp)

    def read(self, source):
        try:
            with open(self.setting_dir_path + os.sep + source, "rb") as fp:
                return pickle.load(fp)
        except FileNotFoundError as e:
            return {}


