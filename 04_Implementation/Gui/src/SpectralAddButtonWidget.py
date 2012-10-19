import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SpectralAddButtonWidget(QtGui.QWidget):
    def __init__(self, mainGui):
        super(SpectralAddButtonWidget, self).__init__()
	self.spectralAddButtonLayout = QtGui.QGridLayout()
	self.setLayout(self.spectralAddButtonLayout)
	
	self.spectralAddButton = QtGui.QPushButton()
	self.spectralAddButton.setText("+")
	self.spectralAddButtonLayout.setColumnMinimumWidth(0, 570)
	self.spectralAddButtonLayout.setColumnMinimumWidth(2, 4)
	self.spectralAddButtonLayout.addWidget(self.spectralAddButton, 0, 1)
	
	QtCore.QObject.connect(self.spectralAddButton, QtCore.SIGNAL(_fromUtf8("clicked()")), mainGui.addSpectralColourWidget)

