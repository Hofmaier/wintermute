from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class MenuBar(QtGui.QMenuBar):
    def __init__(self, mainWindow):
        super(MenuBar, self).__init__()
        self.fileMenu = QtGui.QMenu("File")
        self.addMenu(self.fileMenu)

        loadAction = QtGui.QAction('&loadProject', self)
        loadAction.setText("Load Project")
        loadAction.triggered.connect(mainWindow.showLoadProjectWidget)

        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setText("Exit")
        exitAction.triggered.connect(mainWindow.closeApplication)

        self.fileMenu.addAction(loadAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(exitAction)
