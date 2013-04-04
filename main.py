from PyQt4.QtGui import *

from customTableWidget import *
from fileUtils import *

from os.path import dirname, basename


class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(QMainWindow, self).__init__()
    self.setMinimumSize(800, 800)

    self.order = [('filename', 'Filename')
            ,('filesize', 'Filesize')
            ,('path', 'Path')
            ]
    self.tableView = customTableWidget(self.order)

    self.inputBox = QLineEdit()
    self.inputBox.textChanged.connect(self.search)
    self.inputBox.setText('./*')
    
    self.vbox = QVBoxLayout()
    self.vbox.addWidget(self.inputBox)
    self.vbox.addWidget(self.tableView)
    self.setLayout(self.vbox)
    
  def search(self, path):
    self.tableView.setItems(listFiles(dirname(path), basename(path)))    

import sys

if  __name__ ==  "__main__":
  app = QApplication(sys.argv)
  main = MainWindow()
  main.show()
  sys.exit(app.exec_())