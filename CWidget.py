from PyQt4.QtGui import QWidget, QTabWidget, QVBoxLayout, QTabBar, QPushButton
from PyQt4.QtCore import SIGNAL

from CTableWidget import CTableWidget
from FileListOperations import listFiles, filterFiles

class CWidget(QWidget):

    def __init__(self, parent=None):
        super(CWidget, self).__init__()

        self.tabWidget = QTabWidget()
        self.tabWidget.setTabsClosable(True)

        self.tables = []
        self.files = listFiles('.')

        allFilesTable = CTableWidget(("Filename", "Filesize", "Path"))
        allFilesTable.setItems(self.files)
        self.tabWidget.addTab(allFilesTable, "All Files")        
        self.tables.append((allFilesTable, None))

        self.tabWidget.tabCloseRequested.connect(self.tabWidget.removeTab)
        self.tabWidget.tabBar().tabButton(0, QTabBar.RightSide).resize(0, 0)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabWidget)

        self.setLayout(vbox)
        
        self.addTab('PDF', ("Path", "Filename"), '*.pdf')
        
    def addTab(self, tabLabel, tableHeaderLabels, pattern):
        table = CTableWidget(tableHeaderLabels)
        table.setItems(filterFiles(self.files, pattern))
        self.tables.append((table, pattern))
        self.tabWidget.addTab(table, tabLabel)
        
    def refreshTables(self):
        for tableData in self.tables:
            if tableData[1]:
                tableData[0].setItems(filterFiles(self.files, tableData[1]))
            else:
                tableData[0].setItems(self.files)