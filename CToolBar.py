from PyQt4.QtGui import QToolBar, QAction, QIcon
from PyQt4.QtCore import SIGNAL, SLOT

class CToolBar(QToolBar):

    def __init__(self, parent=0):
        super(CToolBar, self).__init__()
        self.setMovable(False)

        self.dir = QAction(QIcon('icons/dir.png'), 'Change directory', self)
        self.tab = QAction(QIcon('icons/tab.png'), 'Add tab', self)
        self.exit = QAction(QIcon('icons/exit.png'), 'close applicatiob', self)

        self.addAction(self.dir)
        self.addAction(self.tab)
        self.addAction(self.exit)

        self.connect(self.dir, SIGNAL('triggered()'), SLOT('close()'))
        self.connect(self.tab, SIGNAL('triggered()'), SLOT('close()'))
        self.connect(self.exit, SIGNAL('triggered()'), SLOT('close()'))