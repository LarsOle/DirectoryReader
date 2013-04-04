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
    tableView.setItems(listFiles(dirname(path), basename(path)))

inputBox = QLineEdit()
inputBox.textChanged.connect(search)
inputBox.setText('./*')
vbox.addWidget(inputBox)

widget = QWidget()
widget.setMinimumSize(800, 800)
widget.setLayout(vbox)
widget.show()

sys.exit(app.exec_())
