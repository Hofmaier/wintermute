
from PyQt4 import QtCore, QtGui
from MainWindow import Ui_MainWindow
from NewProject import NewProject
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

    def newProject(self):
        self.newProject = NewProject()
        self.hide()
        self.newProject.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    startUp = StartUpScreen()
    startUp.show()
    sys.exit(app.exec_())
