import sys, os
from PyQt4 import QtCore, QtGui
from astrophoto.camerainterface import ImageType

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SpectralColourWidget(QtGui.QWidget):
    def __init__(self, mainGui, session, shotDescription):
        super(SpectralColourWidget, self).__init__(mainGui)
        self.spectralLayout = QtGui.QGridLayout()
#        self.numberValidator = QtGui.QIntValidator(1, 100)
        self.shotDescription = shotDescription
        self.session = session

        self.setLayout(self.spectralLayout)
        self.actualRow = 2
        self.actualColumn = 1

        self.frame = QtGui.QFrame()
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.spectralLayout.addWidget(self.frame, 0, 0, 10, 12)

        self.deleteSpectralColourButton = QtGui.QPushButton()
        self.deleteSpectralColourButton.setIcon(QtGui.QIcon(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.spectralLayout.addWidget(self.deleteSpectralColourButton, 2, 10)


        self.imageTypeLabel = QtGui.QLabel()
        self.imageTypeLabel.setText("Image Type:")
        self.spectralLayout.addWidget(self.imageTypeLabel, self.actualRow, self.actualColumn)
        self.calculatePosition()

        self.imageTypeComboBox = QtGui.QComboBox()
        for imageTyp in self.session.currentProject.cameraconfiguration.imagingfunctions.keys():
            self.imageTypeComboBox.addItem(imageTyp)
        self.spectralLayout.addWidget(self.imageTypeComboBox, self.actualRow, self.actualColumn)
        self.imageTypeComboBox.setCurrentIndex(self.imageTypeComboBox.findText(self.shotDescription.imagetype))
        self.calculatePosition()

        if self.session.currentProject.cameraconfiguration.hasFilterWheel:
            self.spectralLabel = QtGui.QLabel()
            self.spectralLabel.setText("Spectral:")
            self.spectralLayout.addWidget(self.spectralLabel, self.actualRow, self.actualColumn)
            self.calculatePosition()

            self.spectralComboBox = QtGui.QComboBox()
            self.spectralLayout.addWidget(self.spectralComboBox, self.actualRow, self.actualColumn)
            self.calculatePosition()

        self.numberOfImagesLabel = QtGui.QLabel()
        self.numberOfImagesLabel.setText("Number of Images:")
        self.spectralLayout.addWidget(self.numberOfImagesLabel, self.actualRow, self.actualColumn)
        self.calculatePosition()

        self.numberOfImagesLineEdit = QtGui.QLineEdit()
#        self.numberOfImagesLineEdit.setValidator(self.numberValidator)
        self.spectralLayout.addWidget(self.numberOfImagesLineEdit, self.actualRow, self.actualColumn)
        self.numberOfImagesLineEdit.setText(str(len(self.shotDescription.images)))
        self.calculatePosition()

        self.durationLabel = QtGui.QLabel()
        self.durationLabel.setText("Duration:")
        self.spectralLayout.addWidget(self.durationLabel, self.actualRow, self.actualColumn)
        self.calculatePosition()

        self.durationLineEdit = QtGui.QLineEdit()
#        self.durationLineEdit.setValidator(self.numberValidator)
        self.spectralLayout.addWidget(self.durationLineEdit, self.actualRow, self.actualColumn)
        self.durationLineEdit.setText(str(self.shotDescription.duration))
        self.calculatePosition()

#        self.binningLabel = QtGui.QLabel()
#        self.binningLabel.setText("Binning:")
#        self.spectralLayout.addWidget(self.binningLabel, 4, 5)
#        self.binning2Radio = QtGui.QRadioButton()
#        self.binning2Radio.setText("2x2")
#        self.spectralLayout.addWidget(self.binning2Radio, 4, 7)
#        self.binning4Radio = QtGui.QRadioButton()
#        self.binning4Radio.setText("4x4")
#        self.spectralLayout.addWidget(self.binning4Radio, 4, 9)

        self.generateNewLine()
        self.flatFieldResultLabel = QtGui.QLabel()
        self.flatFieldResultLabel.setPixmap(QtGui.QPixmap(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.spectralLayout.addWidget(self.flatFieldResultLabel, self.actualRow, self.actualColumn)
        self.calculatePosition()

        self.flatFieldLabel = QtGui.QLabel()
        self.flatFieldLabel.setText("Flat Field:")
        self.spectralLayout.addWidget(self.flatFieldLabel, self.actualRow, self.actualColumn)
        self.calculatePosition()

        self.collectFlatFieldButton = QtGui.QPushButton()
        self.collectFlatFieldButton.setText("Collect")
        self.spectralLayout.addWidget(self.collectFlatFieldButton, self.actualRow, self.actualColumn)
        self.calculatePosition()

        self.generateNewLine()
        self.darkFrameResult = QtGui.QLabel()
        self.darkFrameResult.setPixmap(QtGui.QPixmap(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.spectralLayout.addWidget(self.darkFrameResult, self.actualRow, self.actualColumn)
        self.calculatePosition()

        self.darkFrameLabel = QtGui.QLabel()
        self.darkFrameLabel.setText("Dark Frame:")
        self.spectralLayout.addWidget(self.darkFrameLabel, self.actualRow, self.actualColumn)
        self.calculatePosition()

        self.collectDarkFrameButton = QtGui.QPushButton()
        self.collectDarkFrameButton.setText("Collect")
        self.spectralLayout.addWidget(self.collectDarkFrameButton, self.actualRow, self.actualColumn)
        self.calculatePosition()

        QtCore.QObject.connect(self.deleteSpectralColourButton, QtCore.SIGNAL(_fromUtf8("clicked()")),  mainGui.deleteSpectralColourWidget)
        QtCore.QObject.connect(self.collectDarkFrameButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.collectDarkFrame)
        QtCore.QObject.connect(self.collectFlatFieldButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.collectFlatField)

    def calculatePosition(self):
        if self.actualColumn == 7:
            self.actualRow = self.actualRow + 1
            self.actualColumn = 1
        else:
            self.actualColumn = self.actualColumn + 2

    def generateNewLine(self):
        self.actualColumn = 1
        self.actualRow = self.actualRow + 1

    def collectDarkFrame(self):
        self.session.capturedark(self.shotDescription)

    def collectFlatField(self):
        self.session.captureflat(self.shotDescription)
