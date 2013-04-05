from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddTabDialog(QDialog):
    
    def __init__(self, parent=None):
        super(AddTabDialog, self).__init__()
        self.setMaximumSize(0,0)
        self.gridLayout = QGridLayout(self)
        self.formLayout = QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_2 = QLabel(self)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QLineEdit(self)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.buttonBox)
        self.lineEdit_2 = QLineEdit(self)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)
        self.label = QLabel(self)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        QObject.connect(self.buttonBox, SIGNAL("accepted()"), self.accept)
        QObject.connect(self.buttonBox, SIGNAL("rejected()"), self.reject)
        QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Add Tab")
        self.label_2.setText("Tabname")
        self.label.setText("Pattern")


class AddPathDialog(QDialog):
    
    def __init__(self, parent=None):
        super(AddPathDialog, self).__init__()
        self.setMaximumSize(0,0)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self)
        self.formLayout = QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_2 = QLabel(self)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QLineEdit(self)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.buttonBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        QObject.connect(self.buttonBox, SIGNAL("accepted()"), self.accept)
        QObject.connect(self.buttonBox, SIGNAL("rejected()"), self.reject)
        QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Add Path")
        self.label_2.setText("Path")