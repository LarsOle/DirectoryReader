from PyQt4.QtGui import QToolBar, QAction, QIcon, QStyle
from PyQt4.QtCore import SIGNAL

from CDialogs import AddPathDialog, AddTabDialog
from FileListOperations import listFiles, filterFiles

class CToolBar(QToolBar):

    def __init__(self, parent=None):
        super(CToolBar, self).__init__()
        self.setMovable(False)

        self.dir = QAction(self.style().standardIcon(QStyle.SP_DirHomeIcon), 'Change directory', self)
        self.dir.setShortcut('Ctrl+D')
        self.tab = QAction(self.style().standardIcon(QStyle.SP_ToolBarHorizontalExtensionButton), 'Add tab', self)
        self.tab.setShortcut('Ctrl+T')

        self.addAction(self.dir)
        self.addAction(self.tab)

        self.connect(self.dir, SIGNAL('triggered()'), self.addPath)
        self.connect(self.tab, SIGNAL('triggered()'), self.addTab)
        
    def addPath(self):
        dialog = AddPathDialog()
        dialog.exec()
        if dialog.lineEdit.text():
            self.parent().centralWidget().files = listFiles(dialog.lineEdit.text())
            self.parent().centralWidget().refreshTables()
        
    def addTab(self):
        dialog = AddTabDialog()
        dialog.exec()
        if dialog.lineEdit.text() and dialog.lineEdit_2.text():
            self.parent().centralWidget().addTab(dialog.lineEdit.text(), ('Filename', 'Filesize', 'Path'), dialog.lineEdit_2.text())