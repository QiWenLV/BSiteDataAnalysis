import configparser
import datetime
import os


class Setting:

    def __init__(self):
        ROOT_DIR_NAME = '.BSite'
        SETTING_FILE_NAME = 'setting.ini'
        self.cf = configparser.ConfigParser()
        self.setting_dir_path = os.path.expanduser('~') + os.sep + ROOT_DIR_NAME
        self.whole_path = self.setting_dir_path + os.sep + SETTING_FILE_NAME
        if os.path.exists(self.setting_dir_path):
            # 读取文件
            self.cf.read(self.whole_path)
        else:
            # 创建配置文件
            os.makedirs(self.setting_dir_path)
            self.set(Group.dynamic, 'last_time', datetime.datetime.now().isoformat())
            self.set(Group.dynamic, 'limit_num', '100')
            with open(self.whole_path, 'w') as fw:
                self.cf.write(fw)

    def get(self, group, key):
        return self.cf.get(group, key, raw=True)

    def set(self, group, key, value):
        if not self.cf.sections().__contains__(group):
            self.cf.add_section(group)
        self.cf.set(group, key, value)
        with open(self.whole_path, 'w') as fw:
            self.cf.write(fw)


class Group:
    config = 'config'
    dynamic = 'dynamic'

class Key:
    last_time = 'last_time'
    limit_num = 'limit_num'
    myid = 'myid'
    cookie = 'cookie'

