from PyQt4 import QtCore, QtGui
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MainFrame(QtGui.QMainWindow):
    def __init__(self, session):
        super(MainFrame, self).__init__()
        self.session = session

    def closeEvent(self, event):
        project = self.session.currentProject
        for adapter in self.session.workspace.adapterList:
            self.session.workspace.persFacade.persistAdapter(adapter)
        for telescope in self.session.workspace.telescopeList:
            self.session.workspace.persFacade.persistTelescope(telescope)
        self.session.workspace.persFacade.persistcameraconfiguration(project.cameraconfiguration, project)
        for shotdesc in project.shotdescriptions:
            self.session.workspace.persFacade.persistshotdescription(shotdesc, project)
        sys.exit()
