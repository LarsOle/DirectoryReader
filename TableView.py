import sys
from PyQt4.QtGui import *

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
tableWidget.setHorizontalHeaderLabels(word)
tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch)

from FileReader import *

for f in listFiles('D:\Downloads', '*.mkv'):
    tableWidget.insertRow(0)
    for i, c in enumerate(default):
        tableWidget.setItem(0, i, QTableWidgetItem(str(f[c])))

tableWidget.show()


sys.exit(app.exec_())