import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from browser.open_dynamic import to_obtain_dynamic_list, open_myself_dynamic, DYNAMIC_URL
from gui.ui.ui_mainwindow import Ui_MainWindow
from config.setting import *
from gui.table_model import *

class MainWindow(QMainWindow):
    def __init__(self, setting: Setting):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setting = setting
        self.click_event()

    def init_attr(self):
        # 初始化属性
        last_time = QDateTime.fromString(self.setting.get(Group.dynamic, Key.last_time), Qt.ISODate)
        self.ui.dateTimeEdit.setDateTime(last_time)
        # 初始化网页限制数
        self.ui.limitNum.setRange(-1, 200)
        self.ui.limitNum.setValue(int(self.setting.get(Group.dynamic, Key.limit_num)))

    def click_event(self):
        # 点击事件
        self.ui.openBtn.clicked.connect(self.open_dynamic_click)
        self.ui.scanBtn.clicked.connect(self.scan_dynamic_click)

    def open_dynamic_click(self):
        # 一键打开动态按钮
        # last_time = self.ui.dateTimeEdit.dateTime().toPython()
        # limit = self.ui.limitNum.value()

        # self.ui.detailTable.l

        # 打开链接
        url_list = [DYNAMIC_URL + item['bvid'] for item in self.wait_open_url_list]
        open_myself_dynamic(url_list)
        # 页面更新最近一次扫描时间
        self.ui.dateTimeEdit.setDateTime(QDateTime.fromSecsSinceEpoch(self.last_time.timestamp()))
        # 保持最近一次扫描时间
        self.setting.set(Group.dynamic, Key.last_time, self.last_time.isoformat())
        self.setting.set(Group.dynamic, Key.limit_num, str(self.ui.limitNum.value()))

    def scan_dynamic_click(self):
        # 扫描动态
        limit = self.ui.limitNum.value()
        self.wait_open_url_list = to_obtain_dynamic_list(self.ui.dateTimeEdit.dateTime().toPython(), limit)
        # 将扫描结果显示在表格控件中
        self.scan_rst_view_table(self.wait_open_url_list)
        # 修改最后扫描时间
        self.last_time = datetime.datetime.now()

    def scan_rst_view_table(self, wait_open_url_list):
        detail_table_model = DetailTableModel(self.ui.detailTable)
        for item in wait_open_url_list:
            item['is_open'] = True
        detail_table_model.add_data(wait_open_url_list)
        # model = QStandardItemModel(0, 4, self.ui.detailTable)
        #
        # model.setHorizontalHeaderItem(0, QStandardItem("bvid"))
        # model.setHorizontalHeaderItem(1, QStandardItem("up"))
        # model.setHorizontalHeaderItem(2, QStandardItem("更新时间"))
        # model.setHorizontalHeaderItem(3, QStandardItem("是否打开"))
        #
        # for i in range(len(wait_open_url_list)):
        #     item = wait_open_url_list[i]
        #     c_index = 0
        #     for k_, v_ in item.items():
        #         model.setItem(i, c_index, QStandardItem(str(v_)))
        #         c_index += 1
        #     a = QStandardItem()
        #     a.setCheckable(True)
        #     a.setCheckState()
        #     model.setItem(i, 3, a)
        self.ui.detailTable.setModel(detail_table_model.get_model())
        self.ui.detailTable.setAlternatingRowColors(True)
        # self.ui.detailTable.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow(Setting())

    main.init_attr()

    main.show()
    sys.exit(app.exec_())