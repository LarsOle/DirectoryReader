import sys
from customTableWidget import *
from fileUtils import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)

vbox = QVBoxLayout()
order = [('filename', 'Filename')
        ,('filesize', 'Filesize')
        ,('path', 'Path')
        ]

tableView = customTableWidget(order)

vbox.addWidget(tableView)

from os.path import dirname, basename
        
def search(path):
    print(path, dirname(path), basename(path))
    tableView.setItems(listFiles(dirname(path), basename(path)))

inputBox = QLineEdit()
inputBox.setText('D:\Downloads\*.mkv')
inputBox.textChanged.connect(search)
vbox.addWidget(inputBox)

widget = QWidget()
widget.setMinimumSize(800, 600)
widget.setLayout(vbox)
widget.show()

sys.exit(app.exec_())