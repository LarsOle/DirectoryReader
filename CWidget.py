from PyQt4.QtGui import QWidget, QTabWidget, QVBoxLayout

from CTableWidget import CTableWidget
from FileListOperations import listFiles, filterFiles

class CWidget(QWidget):

    def __init__(self, parent=None):
        super(CWidget, self).__init__()

        self.tabWidget = QTabWidget()

        files = listFiles('.')

        allFilesTable = CTableWidget(("Filename", "Filesize", "Path"))
        allFilesTable.setItems(files)
        self.tabWidget.addTab(allFilesTable, "All Files")

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabWidget)

        self.setLayout(vbox)
        
        table1 = CTableWidget(("Filename", "Filesize"))
        self.tabWidget.addTab(table1, "Python Files")
        table1.setItems(filterFiles(files, '*.py'))
        
        table2 = CTableWidget(("Filename", "Path"))
        self.tabWidget.addTab(table2, "Readme")
        table2.setItems(filterFiles(files, 'README'))
        
    def addTab(self, tabLabel, tableHeaderLabels):
        table = CTableWidget(tableHeaderLabels)
        self.tabWidget.addTab(table, tabLabel)