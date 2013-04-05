from PyQt4.QtGui import QMainWindow

from CWidget import CWidget

class CMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(CMainWindow, self).__init__()
        self.setMinimumSize(1280, 720)

        self.cWidget = CWidget()
        #self.cMenuBar = CMenuBar()

        self.setCentralWidget(self.cWidget)