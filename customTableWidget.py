from os import system
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class customTableWidget(QTableWidget):

    def __init__(self, order):
        super(QTableWidget, self).__init__()

        self.default, self.word = zip(*order)
        self.tableWidget = QTableWidget(0, len(self.default))
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGridStyle(Qt.PenStyle(0))
        self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        
        self.tableWidget.setHorizontalHeaderLabels(self.word)

        self.tableWidget.doubleClicked.connect(self.startApplicationWithPath)
        
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.setFocusPolicy(Qt.NoFocus)

    def startApplicationWithPath(self, item):
        system("start " + tableWidget.item(item.row(), default.index('path')).text());
        
    def setItems(self, items):
        self.tableWidget.setSortingEnabled(False)
        for item in items:
            self.tableWidget.insertRow(0)
            for i, c in enumerate(self.default):
                self.tableWidget.setItem(0, i, QTableWidgetItem(str(item[c])))
        self.tableWidget.setSortingEnabled(True)