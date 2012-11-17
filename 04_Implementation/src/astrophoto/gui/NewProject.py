
from PyQt4 import QtCore, QtGui
from astrophoto.gui.MainWindow import Ui_MainWindow

class NewProject(QtGui.QWidget):
    def __init__(self, session, lastWidget):
        super(NewProject, self).__init__()
        self.session = session
        self.setWindowTitle("New Project")
        self.lastWidget = lastWidget
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
        self.okButton.setDefault(True)
        self.widgetLayout.addWidget(self.okButton, 3, 5)

        self.setFixedSize(self.sizeHint())

        self.frameGeometry = self.frameGeometry()
        desktopGeometry = QtGui.QDesktopWidget().availableGeometry().center()
        self.frameGeometry.moveCenter(desktopGeometry)
        self.move(self.frameGeometry.topLeft())

        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.createNewProject)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.showLastScreen)

    def createNewProject(self):
        newProject = self.session.createProject(self.projectNameLineEdit.text())
        self.MainWindow = QtGui.QMainWindow()
        self.mainWindow_ui = Ui_MainWindow()
        self.mainWindow_ui.setupUi(self.MainWindow, self.session)
        self.deleteLater()
        self.lastWidget.deleteLater()
        self.MainWindow.show()

    def showLastScreen(self):
        self.hide()
        self.lastWidget.show()



