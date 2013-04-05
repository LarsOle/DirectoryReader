from PyQt4.QtGui import QWidget, QTabWidget, QVBoxLayout
from CTableWidget import CTableWidget

class CWidget(QWidget):

    def __init__(self, parent=None):
        super(CWidget, self).__init__()

        table1 = CTableWidget()
        self.cTabWidget = QTabWidget()

        self.cTabWidget.addTab(table1, 1, "1. Liste")

        vbox = QVBoxLayout()
        vbox.addWidget(self.cTabWidget)

        self.setLayout(vbox)