# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4 import QtCore, QtGui
from astrophoto.gui.CollectSpectralWidget import CollectSpectralWidget
from astrophoto import imageprocessing
import os

class CollectWidget(QtGui.QWidget):
    def __init__(self, session):
        super(CollectWidget, self).__init__()
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)

        self.session = session
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignRight)

    def updateCollectWidget(self):
        self.verticalLayoutWidget.deleteLater()
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        for shotDescription in self.session.currentProject.shotdescriptions:
            collectSpectralWidget = CollectSpectralWidget(shotDescription, self.session)
            self.verticalLayout.addWidget(collectSpectralWidget)

        self.calibrateButtonLayout = QtGui.QGridLayout()
        self.calibrateButtonLayout.setColumnMinimumWidth(0, 16)
        self.calibrateButtonLayout.setColumnMinimumWidth(4, 8)
        self.verticalLayout.addLayout(self.calibrateButtonLayout)

        self.calibrationButton = QtGui.QPushButton()
        self.calibrationButton.setText("Calibrate")
        self.calibrationButton.setMaximumWidth(200)
        self.calibrateButtonLayout.addWidget(self.calibrationButton, 0, 3)

        self.calibrateStatusLabel = QtGui.QLabel()
        self.calibrateStatusLabel.setPixmap(QtGui.QPixmap(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.calibrateButtonLayout.addWidget(self.calibrateStatusLabel, 0, 1)

        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.calibrateButtonLayout.addItem(spacerItem, 0, 2)
        QtCore.QObject.connect(self.calibrationButton, QtCore.SIGNAL("clicked()"), self.calibrate)

    def calibrate(self):
        print("Calibrate")


