
import sys
import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SelectCameraInterface(QtGui.QDialog):
    def __init__(self, planWidget, session):
        super(SelectCameraInterface, self).__init__()
        self.setModal(True)
        self.planWidget = planWidget
        self.session = session
        self.selectCameraLayout = QtGui.QGridLayout()
        self.setLayout(self.selectCameraLayout)
        self.interfaceList = QtGui.QListWidget()
        self.selectCameraLayout.setColumnMinimumWidth(0, 10)
        self.selectCameraLayout.setColumnMinimumWidth(3, 10)
        self.selectCameraLayout.addWidget(self.interfaceList, 3, 1, 1, 2)

        self.interfaceList.addItems(self.session.getInterfaceNames())

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.selectCameraLayout.addWidget(self.cancelButton, 5, 1)

        self.okButton = QtGui.QPushButton()
        self.okButton.setText("OK")
        self.okButton.setDefault(True)
        self.selectCameraLayout.addWidget(self.okButton, 5, 2)

        self.setFixedSize(self.sizeHint())

        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeAndSave)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)


    def closeAndSave(self):
        self.planWidget.createCameraConfiguration(self.interfaceList.currentItem())
        self.close()
