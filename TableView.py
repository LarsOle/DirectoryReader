from PyQt4.QtGui import *

app = QApplication(sys.argv)

tableWidget = QTableWidget(0, 2)
tableWidget.setHorizontalHeaderLabels(("Filename", "Filename"))
tableWidget.setItem(0, 0, QTableWidgetItem("abc"))
tableWidget.show()

import sys
sys.exit(app.exec_())