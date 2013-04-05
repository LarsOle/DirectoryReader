from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTableWidget, QAbstractItemView, QHeaderView, QTableWidgetItem

from FileListOperations import enToIntern

class CTableWidget(QTableWidget):

    def __init__(self, labels, parent=None):
        super(CTableWidget, self).__init__()
        for i in range(len(labels)):
            self.insertColumn(0)
        self.labels = labels
        self.setHorizontalHeaderLabels(labels)
        
        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setGridStyle(Qt.PenStyle(0))
        self.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setFocusPolicy(Qt.NoFocus)

        self.doubleClicked.connect(self.doubleClickedRow)

    def doubleClickedRow(self):
        #system("start " + self.item(item.row(), self.default.index('path')).text());
        pass
  
    def setItems(self, items):
        self.items = items
        self.setSortingEnabled(False)

        self.setRowCount(0)
        for item in items:
            self.insertRow(0)
            for i in range(0, self.columnCount()):
                internVar = enToIntern[self.horizontalHeaderItem(i).text()]
                if internVar in item:
                    self.setItem(0, i, QTableWidgetItem(str(item[internVar])))

        self.setSortingEnabled(True)