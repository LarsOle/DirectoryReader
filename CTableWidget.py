from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTableWidget, QAbstractItemView, QHeaderView, QTableWidgetItem

from FileListOperations import enToIntern

class CTableWidget(QTableWidget):

    def __init__(self, labels=("Filename", "Filesize", "Path"), parent=None):
        super(CTableWidget, self).__init__()
        self.labels = labels
        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setGridStyle(Qt.PenStyle(0))
        self.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setFocusPolicy(Qt.NoFocus)

        self.doubleClicked.connect(self.doubleClickedRow)
        self.insertColumn(0)
        self.insertColumn(0)
        self.insertColumn(0)
        self.setHorizontalHeaderLabels(labels)

    def doubleClickedRow(self):
        #system("start " + self.item(item.row(), self.default.index('path')).text());
        pass
  
    def setItems(self, items):
        self.items = items
        self.setSortingEnabled(False)

        self.setRowCount(0)
        for item in items:
            self.insertRow(0) #self.currentRow() + 1)
            for i in range(0, self.columnCount()):
                print(self.horizontalHeaderItem(i).text())
                internVar = enToIntern[self.horizontalHeaderItem(i).text()]
                print(internVar)
                if internVar in item:
                    self.setItem(0, i, QTableWidgetItem(str(item[internVar])))

        self.setSortingEnabled(True)