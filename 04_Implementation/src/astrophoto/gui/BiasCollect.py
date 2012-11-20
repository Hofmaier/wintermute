
from PyQt4 import QtCore, QtGui

class BiasCollect(QtGui.QWidget):
    def __init__(self, session):
        super(BiasCollect, self).__init__()
        self.session = session
        self.setWindowTitle("Collect Bias")
        self.widgetLayout = QtGui.QGridLayout()
        self.setLayout(self.widgetLayout)

        self.widgetLayout.setRowMinimumHeight(2, 7)
        self.biasCountLabel = QtGui.QLabel()
        self.biasCountLabel.setText("Bias count")
        self.widgetLayout.addWidget(self.biasCountLabel, 1, 1)

        self.biasCountLineEdit = QtGui.QLineEdit()
        self.widgetLayout.addWidget(self.biasCountLineEdit, 1, 3, 1, 3)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.widgetLayout.addWidget(self.cancelButton, 3, 3)

        self.collectButton = QtGui.QPushButton()
        self.collectButton.setText("Collect")
        self.collectButton.setDefault(True)
        self.widgetLayout.addWidget(self.okButton, 3, 5)

        self.setFixedSize(self.sizeHint())

        self.setFixedSize(self.sizeHint())
        point = QtGui.QCursor.pos()
        self.move(point)

        QtCore.QObject.connect(self.collectButton, QtCore.SIGNAL("clicked()"), self.saveAndQuit)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.showLastScreen)

    def saveAndQuit(self):
        self.session.currentProject.cameraconfiguration.capturebias()
        self.hide()
        self.deleteLater()

    def showLastScreen(self):
        self.hide()
        self.deleteLater()



