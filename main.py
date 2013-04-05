from sys import argv, exit

from PyQt4.QtGui import QApplication

from CMainWindow import CMainWindow

if  __name__ ==  "__main__":
    app = QApplication(argv)
    main = CMainWindow()
    main.show()
    exit(app.exec_())