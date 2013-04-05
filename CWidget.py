from PyQt4.QtGui import QWidget, QTabWidget, QVBoxLayout

from CTableWidget import CTableWidget

class CWidget(QWidget):

    def __init__(self, parent=None):
        super(CWidget, self).__init__()

        self.cTabWidget = QTabWidget()

        self.table1 = CTableWidget()
        self.cTabWidget.addTab(self.table1, "All Files")

        vbox = QVBoxLayout()
        vbox.addWidget(self.cTabWidget)

        self.setLayout(vbox)