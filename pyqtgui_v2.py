from PyQt4 import QtCore, QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        mainLayout = QtGui.QVBoxLayout()

        widget = QtGui.QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        topFiller = QtGui.QWidget()
        topFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

        bottomFiller = QtGui.QWidget()
        bottomFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

        vbox = QtGui.QVBoxLayout()
        vbox.setMargin(5)
        vbox.addWidget(topFiller)
        vbox.addWidget(bottomFiller)
        widget.setLayout(vbox)

        #Table
        headers = ("File Name", "File Size", "Directory", "Year","Comments")
        self.fileTable = QtGui.QTableWidget(0, 5)
        self.fileTable.setHorizontalHeaderLabels(headers)
        self.fileTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.fileTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        mainLayout.addWidget(self.fileTable)

        self.fileTable.insertRow(1)
        self.fileTable.setItem(1, 0, "test.py")
        self.fileTable.setItem(1, 1, "120mb")
        self.fileTable.setItem(1, 2, "C:/Benutzer")
        self.fileTable.setItem(1, 3, "12032")
        self.fileTable.setItem(1, 4, "Hello")

        self.createActions()
        self.createMenus()

        message = "Infobar"
        self.statusBar().showMessage(message)

        self.setWindowTitle("Ultimate File Viewer")
        self.setMinimumSize(800,600)
        self.resize(800,600)


    def newFile(self):
        3+3

    def open(self):
        3+3
        	
    def save(self):
        3+3

    def undo(self):
        3+3

    def redo(self):
        3+3

    def settings(self):
        3+3

    def about(self):
        QtGui.QMessageBox.about(self, "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    def aboutQt(self):
        3+3

    def createActions(self):
        self.newAct = QtGui.QAction("&New", self,
                shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new file", triggered=self.newFile)

        self.openAct = QtGui.QAction("&Open...", self,
                shortcut=QtGui.QKeySequence.Open,
                statusTip="Open an existing file", triggered=self.open)

        self.saveAct = QtGui.QAction("&Save", self,
                shortcut=QtGui.QKeySequence.Save,
                statusTip="Save the document to disk", triggered=self.save)

        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

        self.undoAct = QtGui.QAction("&Undo", self,
                shortcut=QtGui.QKeySequence.Undo,
                statusTip="Undo the last operation", triggered=self.undo)

        self.redoAct = QtGui.QAction("&Redo", self,
                shortcut=QtGui.QKeySequence.Redo,
                statusTip="Redo the last operation", triggered=self.redo)

        self.settingsAct = QtGui.QAction("&Settings", self,
                statusTip="Open the settings", triggered=self.settings)


        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=self.aboutQt)
        self.aboutQtAct.triggered.connect(QtGui.qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.settingsAct)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())