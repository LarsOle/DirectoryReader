from PyQt4.QtGui import QToolBar, QAction, QIcon
from PyQt4.QtCore import SIGNAL, SLOT

from CDialogs import AddPathDialog, AddTabDialog

class CToolBar(QToolBar):

    def __init__(self, parent=0):
        super(CToolBar, self).__init__()
        self.setMovable(False)

        self.dir = QAction(QIcon('icons/dir.png'), 'Change directory', self)
        self.tab = QAction(QIcon('icons/tab.png'), 'Add tab', self)

        self.addAction(self.dir)
        self.addAction(self.tab)

        self.connect(self.dir, SIGNAL('triggered()'), self.addPath)
        self.connect(self.tab, SIGNAL('triggered()'), self.addTab)
        
    def addPath(self):
        dialog = AddPathDialog()
        dialog.exec()
        
    def addTab(self):
        dialog = AddTabDialog()
        dialog.exec()