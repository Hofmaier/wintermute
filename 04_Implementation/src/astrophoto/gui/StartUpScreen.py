
from PyQt4 import QtCore, QtGui
from astrophoto.gui.NewProject import NewProject
from astrophoto import workflow
from astrophoto.gui.MainWindow import Ui_MainWindow
from astrophoto.gui.LoadProject import LoadProject
import sys


class StartUpScreen(QtGui.QWidget):
    def __init__(self):
        super(StartUpScreen, self).__init__()
        self.horizontalLayout = QtGui.QVBoxLayout()
        self.setLayout(self.horizontalLayout)
        self.setWindowTitle("StartUp")
        self.openNewProjectButton = QtGui.QPushButton()
        self.openNewProjectButton.setText("New Project")
        self.horizontalLayout.addWidget(self.openNewProjectButton)

        self.session = workflow.Session()
        self.session.workspace.load()

        self.loadProjectButton = QtGui.QPushButton()
        self.loadProjectButton.setText("Load Project")
        self.horizontalLayout.addWidget(self.loadProjectButton)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.setFixedSize(self.sizeHint())

        self.frameGeometry = self.frameGeometry()
        desktopGeometry = QtGui.QDesktopWidget().availableGeometry().center()
        self.frameGeometry.moveCenter(desktopGeometry)
        self.move(self.frameGeometry.topLeft())

        QtCore.QObject.connect(self.openNewProjectButton, QtCore.SIGNAL("clicked()"), self.newProject)
        QtCore.QObject.connect(self.loadProjectButton, QtCore.SIGNAL("clicked()"), self.loadProject)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), sys.exit)

    def newProject(self):
        self.newProject = NewProject(self.session, self)
        self.hide()
        self.newProject.show()

    def loadProject(self):
        self.loadProject = LoadProject(self.session, self)
        self.hide()
        self.loadProject.show()

app = QtGui.QApplication(sys.argv)
startUp = StartUpScreen()
startUp.show()
sys.exit(app.exec_())
