from os import system
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class customTableWidget(QTableWidget):

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

    def startApplicationWithPath(self, item):
        """ executes files with Windows only start application. Clicked row needs a valid path column """
        system("start " + self.item(item.row(), self.default.index('path')).text());


    def setItems(self, items):
        """ removes all items from table and sets new given items """
        self.setSortingEnabled(False)

        self.setRowCount(0)
        for item in items:
            self.insertRow(0)
            for i, c in enumerate(self.default):
                self.setItem(0, i, QTableWidgetItem(str(item[c])))

        self.setSortingEnabled(True)