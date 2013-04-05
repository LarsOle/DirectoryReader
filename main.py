from sys import argv, exit

from PyQt4 import QApplication

from QMainWindow import QMainWindow

if  __name__ ==  "__main__":
  app = QApplication(argv)
  mainWindow = QMainWindow()
  mainWindow.show()
  exit(app.exec_())