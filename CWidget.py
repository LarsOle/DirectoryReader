from PyQt4.QtGui import QWidget, QTabWidget

class CWidget(QWidget):

	def __init__(self, parent=None):
		super(CWidget, self).__init__()

		self.cTabWidget = QTabWidget()

		self.tab1 = QWidget()
		self.tab2 = QWidget()

		self.cTabWidget.resize(330, 220)
		self.cTabWidget.move(300, 300)

		self.cTabWidget.addTab(self.tab1, "Test1")
		self.cTabWidget.addTab(self.tab2, "Test2")
