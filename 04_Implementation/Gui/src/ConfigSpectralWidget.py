

from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ConfigSpectralWidget(QtGui.QWidget):
    def __init__(self):
        super(ConfigSpectralWidget, self).__init__()
	self.setMinimumWidth(640)

	self.spectralConfigFrame = QtGui.QFrame()
        self.spectralConfigFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.spectralConfigFrame.setFrameShadow(QtGui.QFrame.Raised)
			
        self.spectralConfigLayout = QtGui.QGridLayout(self)
	self.spectralConfigLayout.setColumnMinimumWidth(0, 10)
	self.spectralConfigLayout.setColumnMinimumWidth(2, 10)
	self.spectralConfigLayout.setColumnMinimumWidth(4, 10)
	self.spectralConfigLayout.setColumnMinimumWidth(6, 10)
	self.spectralConfigLayout.setColumnMinimumWidth(8, 10)
	self.spectralConfigLayout.setColumnMinimumWidth(10, 10)
	self.spectralConfigLayout.setColumnMinimumWidth(12, 10)
        self.spectralConfigLayout.setRowMinimumHeight(1, 7)
        self.spectralConfigLayout.setRowMinimumHeight(3, 7)
	self.spectralConfigLayout.addWidget(self.spectralConfigFrame, 0, 0, 4, 13)

	self.spectralStatusLabel = QtGui.QLabel()
	self.spectralStatusLabel.setText("X")
	self.spectralConfigLayout.addWidget(self.spectralStatusLabel, 2, 1)

	self.spectralColourLabel = QtGui.QLabel()
	self.spectralColourLabel.setText("Spectral:")
	self.spectralConfigLayout.addWidget(self.spectralColourLabel, 2, 3)
	
	self.spectralLineEdit = QtGui.QLineEdit()
	self.spectralConfigLayout.addWidget(self.spectralLineEdit, 2, 5)

	self.spectralTimesLabel = QtGui.QLabel()
	self.spectralTimesLabel.setText("Times:")
	self.spectralConfigLayout.addWidget(self.spectralTimesLabel, 2, 7)

	self.spectralTimesLineEdit = QtGui.QLineEdit()
	self.spectralConfigLayout.addWidget(self.spectralTimesLineEdit, 2, 9)
	
	self.spectralTakeButton = QtGui.QPushButton()
	self.spectralTakeButton.setText("Take All")
	self.spectralConfigLayout.addWidget(self.spectralTakeButton, 2, 11)