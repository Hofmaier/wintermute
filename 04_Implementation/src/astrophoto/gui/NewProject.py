
from PyQt4 import QtCore, QtGui
from MainWindow import Ui_MainWindow


class NewProject(QtGui.QWidget):
    def __init__(self):
        super(NewProject, self).__init__()
        self.widgetLayout = QtGui.QGridLayout()
        self.setLayout(self.widgetLayout)

        self.widgetLayout.setRowMinimumHeight(2, 7)
        self.projectNameLabel = QtGui.QLabel()
        self.projectNameLabel.setText("Project Name:")
        self.widgetLayout.addWidget(self.projectNameLabel, 1, 1)

        self.projectNameLineEdit = QtGui.QLineEdit()
        self.widgetLayout.addWidget(self.projectNameLineEdit, 1, 3, 1, 3)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.widgetLayout.addWidget(self.cancelButton, 3, 3)

        self.okButton = QtGui.QPushButton()
        self.okButton.setText("OK")
        self.widgetLayout.addWidget(self.okButton, 3, 5)

        self.setFixedSize(self.sizeHint())

        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.openMainWindow)

    def openMainWindow(self):
        self.MainWindow = QtGui.QMainWindow()
        self.bla = Ui_MainWindow()
        self.bla.setupUi(self.MainWindow)
        self.hide()
        self.MainWindow.show()

