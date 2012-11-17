
from PyQt4 import QtCore, QtGui


class NewAdapter(QtGui.QDialog):
    def __init__(self, PlanWidget):
        super(NewAdapter, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(True)
        self.planWidget = PlanWidget
        self.adapterLayout = QtGui.QGridLayout()
        self.setLayout(self.adapterLayout)

        self.adapterLayout.setRowMinimumHeight(2, 7)
        self.adapterNameLabel = QtGui.QLabel()
        self.adapterNameLabel.setText("Adapter Name:")
        self.adapterLayout.addWidget(self.adapterNameLabel, 1, 1)

        self.adapterNameLineEdit = QtGui.QLineEdit()
        self.adapterLayout.addWidget(self.adapterNameLineEdit, 1, 3, 1, 3)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.adapterLayout.addWidget(self.cancelButton, 3, 3)

        self.okButton = QtGui.QPushButton()
        self.okButton.setText("OK")
        self.okButton.setDefault(True)
        self.adapterLayout.addWidget(self.okButton, 3, 5)

        self.setFixedSize(self.sizeHint())
        point = QtGui.QCursor.pos()
        self.move(point)

        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.saveAndClose)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.close)


    def saveAndClose(self):
        self.planWidget.createAdapter(self.adapterNameLineEdit.text())
        self.close()

class NewTelescope(QtGui.QDialog):
    def __init__(self, PlanWidget):
        super(NewTelescope, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(True)
        self.planWidget = PlanWidget
        self.move(PlanWidget.pos())
        self.adapterLayout = QtGui.QGridLayout()
        self.setLayout(self.adapterLayout)

        self.adapterLayout.setRowMinimumHeight(2, 7)
        self.telescopeNameLabel = QtGui.QLabel()
        self.telescopeNameLabel.setText("Telescope Name:")
        self.adapterLayout.addWidget(self.telescopeNameLabel, 1, 1)

        self.telescopeNameLineEdit = QtGui.QLineEdit()
        self.adapterLayout.addWidget(self.telescopeNameLineEdit, 1, 3, 1, 3)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.adapterLayout.addWidget(self.cancelButton, 3, 3)

        self.okButton = QtGui.QPushButton()
        self.okButton.setText("OK")
        self.okButton.setDefault(True)
        self.adapterLayout.addWidget(self.okButton, 3, 5)

        self.setFixedSize(self.sizeHint())

        point = QtGui.QCursor.pos()
        self.move(point)

        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.saveAndClose)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.close)


    def saveAndClose(self):
        self.planWidget.createTelescope(self.telescopeNameLineEdit.text())
        self.close()
