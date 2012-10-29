# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4 import QtCore, QtGui
from astrophoto.gui.CollectSpectralWidget import CollectSpectralWidget

class CollectWidget(QtGui.QWidget):
    def __init__(self):
        super(CollectWidget, self).__init__()
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
       
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)

        self.configSpectralWidgetList = []


    def updateCollectWidget(self, spectralWidget):
        self.verticalLayoutWidget.deleteLater()
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        for spectral in spectralWidget.spectralColourWidgetList:
                collectSpectralWidget = CollectSpectralWidget()
                self.verticalLayout.addWidget(collectSpectralWidget)

