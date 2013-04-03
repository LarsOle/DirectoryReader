import sys
from customTableWidget import *
from fileUtils import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)

order = [('filename', 'Filename')
        ,('filesize', 'Filesize')
        ,('path', 'Path')
        ]

tableView = customTableWidget(order)
tableView.setItems(listFiles('D:\Downloads', '*.mkv'))
tableView.show()
sys.exit(app.exec_())