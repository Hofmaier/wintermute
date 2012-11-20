
import os
from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class CollectSpectralWidget(QtGui.QWidget):
    def __init__(self, shotDescription, session):
        super(CollectSpectralWidget, self).__init__()
        self.setMinimumWidth(640)
        self.shotDescription = shotDescription
        self.session = session

        self.actualColumn = 1
        self.actualRow = 2

        self.spectralConfigLayout = QtGui.QGridLayout(self)
        self.spectralConfigFrame = QtGui.QFrame()
        self.spectralConfigFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.spectralConfigFrame.setFrameShadow(QtGui.QFrame.Raised)

        self.spectralConfigLayout.setRowMinimumHeight(1, 7)
        self.spectralConfigLayout.setColumnMinimumWidth(0, 7)
        self.spectralConfigLayout.setColumnMinimumWidth(2, 7)
        self.spectralConfigLayout.setColumnMinimumWidth(4, 7)
        self.spectralConfigLayout.setColumnMinimumWidth(6, 7)

        self.imageTypeLabel = QtGui.QLabel()
        self.imageTypeLabel.setText("Image Type:")
        self.spectralConfigLayout.addWidget(self.imageTypeLabel, self.actualRow, self.actualColumn)
        self.calculateActualPosition()

        self.imageTypeLineEdit = QtGui.QLineEdit()
        self.imageTypeLineEdit.setEnabled(False)
        self.imageTypeLineEdit.setText(self.shotDescription.imagetype)
        self.spectralConfigLayout.addWidget(self.imageTypeLineEdit, self.actualRow, self.actualColumn)
        self.calculateActualPosition()

        if self.session.currentProject.cameraconfiguration.hasFilterWheel:
            self.spectralColourLabel = QtGui.QLabel()
            self.spectralColourLabel.setText("Spectral:")
            self.spectralConfigLayout.addWidget(self.spectralColourLabel, self.actualRow, self.actualColumn)
            self.calculateActualPosition()

            self.spectralLineEdit = QtGui.QLineEdit()
            self.spectralLineEdit.setEnabled(False)
            imagetype = self.shotDescription.imagetype
            imaginFunctions = self.shotDescription.cameraconfiguration.imagingfunctions[imagetype]
            self.spectralLineEdit.setText()
            self.spectralConfigLayout.addWidget(self.spectralLineEdit, self.actualRow, self.actualColumn)
            self.calculateActualPosition()

        self.durationLabel = QtGui.QLabel()
        self.durationLabel.setText("Duration:")
        self.spectralConfigLayout.addWidget(self.durationLabel, self.actualRow, self.actualColumn)
        self.calculateActualPosition()

        self.durationLineEdit = QtGui.QLineEdit()
        self.durationLineEdit.setEnabled(False)
        self.durationLineEdit.setText(str(self.shotDescription.duration))
        self.spectralConfigLayout.addWidget(self.durationLineEdit, self.actualRow, self.actualColumn)
        self.calculateActualPosition()

        self.spectralTimesLabel = QtGui.QLabel()
        self.spectralTimesLabel.setText("Times:")
        self.spectralConfigLayout.addWidget(self.spectralTimesLabel, self.actualRow, self.actualColumn)
        self.calculateActualPosition()

        self.spectralTimesLineEdit = QtGui.QLineEdit()
        self.spectralTimesLineEdit.setEnabled(False)
        self.spectralTimesLineEdit.setText(str(len(self.shotDescription.shots)))
        self.spectralConfigLayout.addWidget(self.spectralTimesLineEdit, self.actualRow, self.actualColumn)
        self.calculateActualPosition()

        self.calculateNewRow()
        self.spectralStatusLabel = QtGui.QLabel()
        self.spectralStatusLabel.setPixmap(QtGui.QPixmap(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.spectralConfigLayout.addWidget(self.spectralStatusLabel, self.actualRow, self.actualColumn)
        self.calculateActualPosition()

        self.spectralTakeButton = QtGui.QPushButton()
        self.spectralTakeButton.setText("Take All")
        self.spectralConfigLayout.addWidget(self.spectralTakeButton, self.actualRow, self.actualColumn)
        self.calculateActualPosition()

        self.spectralConfigLayout.setRowMinimumHeight(self.actualRow + 1, 7)
        self.spectralConfigLayout.setColumnMinimumWidth(8, 8)
        self.spectralConfigLayout.addWidget(self.spectralConfigFrame, 0, 0, 20, 20)

        QtCore.QObject.connect(self.spectralTakeButton, QtCore.SIGNAL("clicked()"), self.captureClicked)

    def captureClicked(self):
        self.session.capture(self.shotDescription)

    def calculateActualPosition(self):
        if self.actualColumn == 7 :
            self.actualRow = self.actualRow + 1
            self.actualColumn = 1
        else:
            self.actualColumn = self.actualColumn + 2

    def calculateNewRow(self):
        self.actualRow = self.actualRow + 1
        self.actualColumn = 5
