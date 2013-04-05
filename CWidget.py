from PyQt4.QtGui import QWidget, QTabWidget, QVBoxLayout

from CTableWidget import CTableWidget
from FileListOperations import listFiles, filterFiles

class CWidget(QWidget):

    def __init__(self, parent=None):
        super(CWidget, self).__init__()

        self.cTabWidget = QTabWidget()

        files = listFiles('.')

        allFilesTable = CTableWidget(("Filename", "Filesize", "Path"))
        allFilesTable.setItems(files)
        self.cTabWidget.addTab(allFilesTable, "All Files")

        vbox = QVBoxLayout()
        vbox.addWidget(self.cTabWidget)

        self.setLayout(vbox)
        
        table1 = CTableWidget(("Filename", "Filesize"))
        self.cTabWidget.addTab(table1, "Python Files")
        table1.setItems(filterFiles(files, '*.py'))
        
        table2 = CTableWidget(("Filename", "Path"))
        self.cTabWidget.addTab(table2, "Readme")
        table2.setItems(filterFiles(files, 'README'))
        
    def addTab(self, tabLabel, tableHeaderLabels):
        table = CTableWidget(tableHeaderLabels)
        self.cTabWidget.addTab(table, tabLabel)