from PySide2.QtCore import QAbstractTableModel
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class DetailTableModel():

    def __init__(self, detailTable: QTableView):
        self.model = QStandardItemModel(0, 4, detailTable)
        # 设置表头
        self.model.setHorizontalHeaderItem(0, QStandardItem("bvid"))
        self.model.setHorizontalHeaderItem(1, QStandardItem("up"))
        self.model.setHorizontalHeaderItem(2, QStandardItem("更新时间"))
        self.model.setHorizontalHeaderItem(3, QStandardItem("是否打开"))

    def add_data(self, datas):
        for i in range(len(datas)):
            item = datas[i]
            table_row = TableRow(item['bvid'], item['up'], item['time'], item['is_open'])
            table_row.setItem(i, model=self.model)

    def get_model(self):
        return self.model

    def get_data(self):
        a = self.model.data(QModelIndex())


class TableRow():

    def __init__(self, bivd, up, update_time, is_open:bool):
        self.bivd = bivd
        self.up = up
        self.update_time = update_time
        self.is_open = is_open

    def setItem(self, index:int, model:QStandardItemModel):
        model.setItem(index, 0, QStandardItem(str(self.bivd)))
        model.setItem(index, 1, QStandardItem(str(self.up)))
        model.setItem(index, 2, QStandardItem(str(self.update_time)))

        is_open_item = QStandardItem()
        is_open_item.setCheckable(True)
        is_open_item.setCheckState(Qt.CheckState.Checked)
        model.setItem(index, 3, is_open_item)
