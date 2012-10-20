# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4 import QtCore, QtGui
from ConfigSpectralWidget import ConfigSpectralWidget

class ConfigWidget(QtGui.QWidget):
    def __init__(self):
        super(ConfigWidget, self).__init__()
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
       
	self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)

	self.configSpectralWidgetList = []
	
	


    def updateConfigWidget(self, spectralWidget):
	self.verticalLayoutWidget.deleteLater()
	self.verticalLayoutWidget = QtGui.QWidget(self)
	self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
	for spectral in spectralWidget.spectralColourWidgetList:
		self.configSpectralWidget = ConfigSpectralWidget()
		self.verticalLayout.addWidget(self.configSpectralWidget)
	

