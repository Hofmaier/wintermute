
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

        self.nameLabel = QtGui.QLabel()
        self.nameLabel.setText("Camera Name:")
        self.selectCameraLayout.addWidget(self.nameLabel, 1, 1)

        self.cameraNameLineEdit = QtGui.QLineEdit()
        self.selectCameraLayout.addWidget(self.cameraNameLineEdit, 1, 2)

        self.availPlugin = QtGui.QLabel()
        self.availPlugin.setText("Available Plugins:")
        self.selectCameraLayout.addWidget(self.availPlugin, 2, 1)

        self.interfaceList = QtGui.QListWidget()
        self.selectCameraLayout.setColumnMinimumWidth(0, 10)
        self.selectCameraLayout.setColumnMinimumWidth(3, 10)
        self.selectCameraLayout.addWidget(self.interfaceList, 3, 1, 1, 2)

        for interfaceName in self.session.getInterfaceNames():
            self.interfaceList.addItem(interfaceName)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.selectCameraLayout.addWidget(self.cancelButton, 5, 1)

        self.okButton = QtGui.QPushButton()
        self.okButton.setText("OK")
        self.okButton.setDefault(True)
        self.selectCameraLayout.addWidget(self.okButton, 5, 2)

        self.setFixedSize(self.sizeHint())

        point = QtGui.QCursor.pos()
        self.move(point.x() - 200, point.y())

        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeAndSave)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)


    def closeAndSave(self):
        self.planWidget.createCameraConfiguration(self.cameraNameLineEdit.text(), self.interfaceList.currentItem())
        self.close()
