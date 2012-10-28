import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SpectralColourWidget(QtGui.QWidget):
    def __init__(self, mainGui):
        super(SpectralColourWidget, self).__init__(mainGui)
        self.spectralLayout = QtGui.QGridLayout()

        self.setLayout(self.spectralLayout)
        self.spectralLayout.setRowMinimumHeight(1, 2)
        self.spectralLayout.setRowMinimumHeight(3, 2)
        self.spectralLayout.setRowMinimumHeight(5, 2)
        self.spectralLayout.setRowMinimumHeight(7, 2)
        self.spectralLayout.setRowMinimumHeight(9, 2)
        self.spectralLayout.setColumnMinimumWidth(0, 8)
        self.spectralLayout.setColumnMinimumWidth(2, 8)
        self.spectralLayout.setColumnMinimumWidth(4, 8)
        self.spectralLayout.setColumnMinimumWidth(6, 8)
        self.spectralLayout.setColumnMinimumWidth(8, 8)
        self.spectralLayout.setColumnMinimumWidth(10, 8)
        self.spectralLayout.setColumnMinimumWidth(11, 2)
        
        self.frame = QtGui.QFrame()
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.spectralLayout.addWidget(self.frame, 0, 0, 10, 12)

        self.deleteSpectralColourButton = QtGui.QPushButton()
        self.deleteSpectralColourButton.setText("-")
        self.spectralLayout.addWidget(self.deleteSpectralColourButton, 2, 10)

        self.spectralLabel = QtGui.QLabel()
        self.spectralLabel.setText("Spectral:")
        self.spectralLayout.addWidget(self.spectralLabel, 4, 1)
        self.spectralLineEdit = QtGui.QLineEdit()
        self.spectralLayout.addWidget(self.spectralLineEdit, 4, 3)
        
        self.numberOfImagesLabel = QtGui.QLabel()
        self.numberOfImagesLabel.setText("Number of Images:")
        self.spectralLayout.addWidget(self.numberOfImagesLabel, 4, 5)
        self.numberOfImagesLineEdit = QtGui.QLineEdit()
        self.spectralLayout.addWidget(self.numberOfImagesLineEdit, 4, 7, 1, 3)

        self.durationLabel = QtGui.QLabel()
        self.durationLabel.setText("Duration:")
        self.spectralLayout.addWidget(self.durationLabel, 6, 1)
        self.durationLineEdit = QtGui.QLineEdit()
        self.spectralLayout.addWidget(self.durationLineEdit, 6, 3)

        self.binningLabel = QtGui.QLabel()
        self.binningLabel.setText("Binning:")
        self.spectralLayout.addWidget(self.binningLabel, 6, 5)
        self.binning2Radio = QtGui.QRadioButton()
        self.binning2Radio.setText("2x2")
        self.spectralLayout.addWidget(self.binning2Radio, 6, 7)
        self.binning4Radio = QtGui.QRadioButton()
        self.binning4Radio.setText("4x4")
        self.spectralLayout.addWidget(self.binning4Radio, 6, 9)

        self.flatFieldLabel = QtGui.QLabel()
        self.flatFieldLabel.setText("Flat Field:")
        self.spectralLayout.addWidget(self.flatFieldLabel, 8, 1)
	
	

        QtCore.QObject.connect(self.deleteSpectralColourButton, QtCore.SIGNAL(_fromUtf8("clicked()")),  mainGui.deleteSpectralColourWidget)
