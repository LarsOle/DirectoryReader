from PyQt4.QtGui import QMainWindow

from CWidget import CWidget
from CToolBar import CToolBar

class CMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(CMainWindow, self).__init__()
        self.setMinimumSize(1280, 720)

        self.cWidget = CWidget()
        self.CToolBar = CToolBar()

        self.setCentralWidget(self.cWidget)
        self.addToolBar(self.CToolBar)