
from PyQt4 import QtCore, QtGui
from astrophoto.gui.NewProject import NewProject
from astrophoto import workflow
from astrophoto.gui.MainWindow import Ui_MainWindow
from astrophoto.gui.LoadProject import LoadProject
from astrophoto.gui.MainFrame import MainFrame
import sys


class StartUpScreen(QtGui.QWidget):
    def __init__(self):
        super(StartUpScreen, self).__init__()
        self.startUpScreenLayout = QtGui.QGridLayout()
        self.setLayout(self.startUpScreenLayout)
        self.setWindowTitle("AstroPhoto")

        self.session = workflow.Session()
        self.session.workspace.load()

        self.loadProjectLabel = QtGui.QLabel()
        self.loadProjectLabel.setText("Load Project")
        self.startUpScreenLayout.addWidget(self.loadProjectLabel, 1, 1)

        self.projectList = QtGui.QListWidget()
        self.startUpScreenLayout.addWidget(self.projectList, 2, 1, 1, 3)

        for project in self.session.workspace.projectList:
            self.projectList.addItem(project.name)

        self.loadProjectButton = QtGui.QPushButton()
        self.loadProjectButton.setText("Load Project")
        self.startUpScreenLayout.addWidget(self.loadProjectButton, 3, 3)

        self.openNewProjectButton = QtGui.QPushButton()
        self.openNewProjectButton.setText("New Project")
        self.startUpScreenLayout.addWidget(self.openNewProjectButton, 4, 3)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.startUpScreenLayout.addWidget(self.cancelButton, 4, 2)

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
        for project in self.session.workspace.projectList:
            if project.name == self.projectList.currentItem().text():
                self.session.currentProject = project
        from astrophoto.gui.MainWindow import Ui_MainWindow
        self.MainWindow = MainFrame(self.session)
        self.mainWindow_ui = Ui_MainWindow()
        self.mainWindow_ui.setupUi(self.MainWindow, self.session)
        self.MainWindow.show()
        self.mainWindow_ui.planWidget.loadProject()
        self.mainWindow_ui.spectralWidget.loadAllSpectralColourWidgets()
        self.hide()
        self.deleteLater()

app = QtGui.QApplication(sys.argv)
startUp = StartUpScreen()
startUp.show()
sys.exit(app.exec_())
