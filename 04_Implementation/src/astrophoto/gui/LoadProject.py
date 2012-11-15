
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class LoadProject(QtGui.QDialog):
    def __init__(self, session, lastWidget):
        super(LoadProject, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Select Project")
        self.setModal(True)
        self.session = session
        self.lastWidget = lastWidget
        self.loadProjectLayout = QtGui.QGridLayout()
        self.setLayout(self.loadProjectLayout)

        self.selectProjectLabel = QtGui.QLabel()
        self.selectProjectLabel.setText("Select Project:")
        self.loadProjectLayout.addWidget(self.selectProjectLabel, 1, 1, 1, 3)

        self.projectList = QtGui.QListWidget()
        self.loadProjectLayout.addWidget(self.projectList, 2, 1, 1, 3)

        for project in self.session.workspace.projectList:
            self.projectList.addItem(project.name)

        self.okButton = QtGui.QPushButton()
        self.okButton.setText("OK")
        self.okButton.setDefault(True)
        self.loadProjectLayout.addWidget(self.okButton, 3, 3)

        self.cancelButton = QtGui.QPushButton()
        self.cancelButton.setText("Cancel")
        self.loadProjectLayout.addWidget(self.cancelButton, 3, 1)

        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.loadProject)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showLastScreen)

    def loadProject(self):
        for project in self.session.workspace.projectList:
            if project.name == self.projectList.currentItem().text():
                self.session.currentProject = project
        self.close()
        self.deleteLater()
        if isinstance( self.lastWidget, QtGui.QMainWindow ):
            self.lastWidget.loadProject()
        else:
            from astrophoto.gui.MainWindow import Ui_MainWindow
            self.MainWindow = QtGui.QMainWindow()
            self.mainWindow_ui = Ui_MainWindow()
            self.mainWindow_ui.setupUi(self.MainWindow, self.session)
            self.MainWindow.show()
            self.mainWindow_ui.planWidget.loadProject()
            self.lastWidget.deleteLater()

    def showLastScreen(self):
        if isinstance( self.lastWidget, QtGui.QMainWindow ):
            self.close()
            self.deleteLater()
        else:
            self.close()
            self.lastWidget.show()
