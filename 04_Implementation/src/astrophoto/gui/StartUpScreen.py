
from PyQt4 import QtCore, QtGui
from NewProject import NewProject
from MainWindow import Ui_MainWindow
import workflow
import sys


class StartUpScreen(QtGui.QWidget):
    def __init__(self):
        super(StartUpScreen, self).__init__()
        self.horizontalLayout = QtGui.QVBoxLayout()
        self.setLayout(self.horizontalLayout)
        self.openNewProjectButton = QtGui.QPushButton()
        self.openNewProjectButton.setText("New Project")
        self.horizontalLayout.addWidget(self.openNewProjectButton)

        self.loadProjectButton = QtGui.QPushButton()
        self.loadProjectButton.setText("Load Project")
        self.horizontalLayout.addWidget(self.loadProjectButton)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.setFixedSize(self.sizeHint())

        QtCore.QObject.connect(self.openNewProjectButton, QtCore.SIGNAL("clicked()"), self.newProject)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), sys.exit)

    def newProject(self):
        self.session = workflow.Session()
        self.newProject = NewProject(self.session)
        self.hide()
        self.newProject.show()

app = QtGui.QApplication(sys.argv)
startUp = StartUpScreen()
startUp.show()
sys.exit(app.exec_())
