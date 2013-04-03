import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)

tableWidget = QTableWidget(0, 3)
tableWidget.setHorizontalHeaderLabels(("Filename", "Filsize", "Path"))
tableWidget.resize(800,600)

from FileReader import *

for f in listFiles('D:\Downloads', '*.mkv'):
    tableWidget.insertRow(0)
    tableWidget.setItem(0, 0, QTableWidgetItem(f['filename']))
    tableWidget.setItem(0, 1, QTableWidgetItem(str(f['filesize'])))
    tableWidget.setItem(0, 2, QTableWidgetItem(f['path']))

tableWidget.show()


sys.exit(app.exec_())