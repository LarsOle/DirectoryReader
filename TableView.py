import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

app = QApplication(sys.argv)

order = [("filename", "Filename")
        ,("filesize", "Filesize")
        ,("path", "Path")
        ]
        
default, word = zip(*order)

tableWidget = QTableWidget(0, len(order))
tableWidget.resize(800,600)
tableWidget.verticalHeader().setVisible(False)
tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

tableWidget.setGridStyle(Qt.PenStyle(0))
tableWidget.setHorizontalHeaderLabels(word)
tableWidget.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)

from FileReader import *

for f in listFiles('D:\Downloads', '*.mkv'):
    tableWidget.insertRow(0)
    for i, c in enumerate(default):
        tableWidget.setItem(0, i, QTableWidgetItem(str(f[c])))

tableWidget.setSortingEnabled(True)
tableWidget.show()

from os import system

def command(item):
    system("start " + item.text());

tableWidget.itemClicked.connect(command)

sys.exit(app.exec_())