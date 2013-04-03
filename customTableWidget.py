from os import system
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class customTableWidget(QTableWidget):

#function to initialize the Table Widget
    def __init__(self, order):
        self.default, self.word = zip(*order)
        super(QTableWidget, self).__init__(0, len(self.default))

        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setGridStyle(Qt.PenStyle(0))
        self.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.setHorizontalHeaderLabels(self.word)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setFocusPolicy(Qt.NoFocus)

        self.doubleClicked.connect(self.startApplicationWithPath)

#funtion to start an application when double clicked
    def startApplicationWithPath(self, item):
        system("start " + self.item(item.row(), self.default.index('path')).text());

#funtion to remove all rows from the table and create new ones for a new directory
    def setItems(self, items):
        self.setSortingEnabled(False)

        for i in range(self.rowCount()):
            self.removeRow(0)

        for item in items:
            self.insertRow(0)
            for i, c in enumerate(self.default):
                self.setItem(0, i, QTableWidgetItem(str(item[c])))

        self.setSortingEnabled(True)
