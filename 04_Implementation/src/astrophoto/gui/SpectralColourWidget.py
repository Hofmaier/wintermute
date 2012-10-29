import sys, os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SpectralColourWidget(QtGui.QWidget):
    def __init__(self, mainGui):
        super(SpectralColourWidget, self).__init__(mainGui)
        self.spectralLayout = QtGui.QGridLayout()
        self.numberValidator = QtGui.QIntValidator(1, 100)

        self.setLayout(self.spectralLayout)

        self.frame = QtGui.QFrame()
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.spectralLayout.addWidget(self.frame, 0, 0, 10, 12)

        self.deleteSpectralColourButton = QtGui.QPushButton()
        self.deleteSpectralColourButton.setIcon(QtGui.QIcon(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.spectralLayout.addWidget(self.deleteSpectralColourButton, 2, 10)


        self.imageTypeLabel = QtGui.QLabel()
        self.imageTypeLabel.setText("Image Type:")
        self.spectralLayout.addWidget(self.imageTypeLabel, 2, 1)
        self.imageTypeComboBox = QtGui.QComboBox()
        self.spectralLayout.addWidget(self.imageTypeComboBox, 2, 3, 1, 7)

        self.spectralLabel = QtGui.QLabel()
        self.spectralLabel.setText("Spectral:")
        self.spectralLayout.addWidget(self.spectralLabel, 3, 1)
        self.spectralLineEdit = QtGui.QComboBox()
        self.spectralLayout.addWidget(self.spectralLineEdit, 3, 3)
        
        self.numberOfImagesLabel = QtGui.QLabel()
        self.numberOfImagesLabel.setText("Number of Images:")
        self.spectralLayout.addWidget(self.numberOfImagesLabel, 3, 5)
        self.numberOfImagesLineEdit = QtGui.QLineEdit()
        self.numberOfImagesLineEdit.setValidator(self.numberValidator)
        self.spectralLayout.addWidget(self.numberOfImagesLineEdit, 3, 7, 1, 3)

        self.durationLabel = QtGui.QLabel()
        self.durationLabel.setText("Duration:")
        self.spectralLayout.addWidget(self.durationLabel, 4, 1)
        self.durationLineEdit = QtGui.QLineEdit()
        self.durationLineEdit.setValidator(self.numberValidator)
        self.spectralLayout.addWidget(self.durationLineEdit, 4, 3)

        self.binningLabel = QtGui.QLabel()
        self.binningLabel.setText("Binning:")
        self.spectralLayout.addWidget(self.binningLabel, 4, 5)
        self.binning2Radio = QtGui.QRadioButton()
        self.binning2Radio.setText("2x2")
        self.spectralLayout.addWidget(self.binning2Radio, 4, 7)
        self.binning4Radio = QtGui.QRadioButton()
        self.binning4Radio.setText("4x4")
        self.spectralLayout.addWidget(self.binning4Radio, 4, 9)

        self.flatFieldLabel = QtGui.QLabel()
        self.flatFieldLabel.setText("Flat Field:")
        self.spectralLayout.addWidget(self.flatFieldLabel, 5, 1)

        self.flatFieldResultLabel = QtGui.QLabel()
        self.flatFieldResultLabel.setText("X")
        self.spectralLayout.addWidget(self.flatFieldResultLabel, 5, 3)

        self.collectFlatFieldButton = QtGui.QPushButton()
        self.collectFlatFieldButton.setText("Collect")
        self.spectralLayout.addWidget(self.collectFlatFieldButton, 5, 5)

        self.useFlatForAllButton = QtGui.QPushButton()
        self.useFlatForAllButton.setText("Use for all")
        self.spectralLayout.addWidget(self.useFlatForAllButton, 5, 7, 1, 3)

        QtCore.QObject.connect(self.deleteSpectralColourButton, QtCore.SIGNAL(_fromUtf8("clicked()")),  mainGui.deleteSpectralColourWidget)
