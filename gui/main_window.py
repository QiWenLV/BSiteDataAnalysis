import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from browser.open_dynamic import to_obtain_dynamic_list
from gui.ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.click_event()

    def init_attr(self):
        # 初始化属性
        self.ui.dateTimeEdit.setDateTime(QDateTime(2021, 7, 20, 12, 0, 0))
        self.ui.limitNum.setRange(-1, 100)

    def click_event(self):
        # 点击事件
        self.ui.openBtn.clicked.connect(self.open_dynamic_click)

    def open_dynamic_click(self):
        # 一键打开动态按钮
        last_time = self.ui.dateTimeEdit.dateTime().toPython()
        limit = self.ui.limitNum.value()
        to_obtain_dynamic_list(last_time, limit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()

    main.init_attr()

    main.show()
    sys.exit(app.exec_())