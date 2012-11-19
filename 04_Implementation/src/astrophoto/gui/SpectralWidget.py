# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys
from PyQt4 import QtCore, QtGui
from astrophoto.gui.SpectralColourWidget import SpectralColourWidget
from astrophoto.gui.SpectralAddButtonWidget import SpectralAddButtonWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SpectralWidget(QtGui.QWidget):
    def __init__(self, planWidget, session):
        super(SpectralWidget, self).__init__()
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
        self.spectralColourWidgetList = []
        self.spacerItem = QtGui.QSpacerItem(0,0,QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.session = session
        self.planWidget = planWidget

        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setMinimumHeight(560)
        self.scrollArea.setMinimumWidth(630)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_2 = QtGui.QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.horizontalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

#        shotDescription = self.session.createShotDescription(0, 0, self.session.currentProject, "")
#        spectralColourWidget = SpectralColourWidget(self, self.session, shotDescription)
        self.spectralAddButtonWidget = SpectralAddButtonWidget(self)

#        self.horizontalLayout_2.addWidget(spectralColourWidget)
        self.horizontalLayout_2.addWidget(self.spectralAddButtonWidget)
#        self.spectralColourWidgetList.append(spectralColourWidget)
        self.horizontalLayout_2.addItem(self.spacerItem)

    def addSpectralColourWidget(self):
        self.horizontalLayout_2.removeItem(self.spacerItem)
        self.horizontalLayout_2.removeWidget(self.spectralAddButtonWidget)
        shotDescription = self.session.createShotDescription(0, 0, self.session.currentProject, "")
        spectralColourWidget = SpectralColourWidget(self, self.session, shotDescription)
        self.spectralColourWidgetList.append(spectralColourWidget)
        self.horizontalLayout_2.addWidget(spectralColourWidget)
        self.horizontalLayout_2.addWidget(self.spectralAddButtonWidget)
        self.horizontalLayout_2.addItem(self.spacerItem)

    def deleteSpectralColourWidget(self):
        self.session.currentProject.shotdescriptions.remove(self.sender().parent().shotDescription)
        self.horizontalLayout_2.removeWidget(self.sender().parent())
        self.spectralColourWidgetList.pop(self.spectralColourWidgetList.index(self.sender().parent()))
        self.sender().parent().deleteLater()

    def checkAllVariablesSet(self):
        print("checkAllVariablesSet")
#        for spectralColourWidget in self.spectralColourWidgetList:
#            if spectralColourWidget.numberOfImagesLineEdit.text() == "":
#                return False
#            elif spectralColourWidget.durationLineEdit.text() == "":
#                return False
#            elif spectralColourWidget.imageTypeComboBox.currentText() == "":
#                return False
#            elif spectralColourWidget.spectralComboBox.currentText() == "":
#                return False
#            elif not spectralColourWidget.binning2Radio.isChecked() and not spectralColourWidget.binning4Radio.isChecked():
#                return False
        return True

    def saveAllSpectralColourWidgets(self):
        print("saveAllSpectralColourWidgets")
        for spectralColourWidget in self.spectralColourWidgetList:
            nrOfShots = int(spectralColourWidget.numberOfImagesLineEdit.text())
            duration = int(spectralColourWidget.durationLineEdit.text())
            imageTyp = spectralColourWidget.imageTypeComboBox.currentText()
            spectralColourWidget.shotDescription.duration =  duration
            spectralColourWidget.shotDescription.imagetype = imageTyp
            spectralColourWidget.shotDescription.setNrOfShots(nrOfShots)

    def loadAllSpectralColourWidgets(self):
        self.horizontalLayout_2.removeItem(self.spacerItem)
        self.horizontalLayout_2.removeWidget(self.spectralAddButtonWidget)
        for shotdesc in self.session.currentProject.shotdescriptions:
            spectralColourWidget = SpectralColourWidget(self, self.session, shotdesc)
            self.spectralColourWidgetList.append(spectralColourWidget)
            self.horizontalLayout_2.addWidget(spectralColourWidget)
        self.horizontalLayout_2.addWidget(self.spectralAddButtonWidget)
        self.horizontalLayout_2.addItem(self.spacerItem)
