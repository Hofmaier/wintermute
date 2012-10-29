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
    def __init__(self, collectWidget):
        super(SpectralWidget, self).__init__()
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
        self.spectralColourWidgetList = []
        self.spacerItem = QtGui.QSpacerItem(0,0,QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.collectWidget = collectWidget

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
             
        spectralColourWidget = SpectralColourWidget(self)
        self.spectralAddButtonWidget = SpectralAddButtonWidget(self)

        self.horizontalLayout_2.addWidget(spectralColourWidget)
        self.horizontalLayout_2.addWidget(self.spectralAddButtonWidget)
        self.spectralColourWidgetList.append(spectralColourWidget)
        self.horizontalLayout_2.addItem(self.spacerItem)
        self.collectWidget.updateCollectWidget(self)

    def addSpectralColourWidget(self):
        self.horizontalLayout_2.removeItem(self.spacerItem)
        self.horizontalLayout_2.removeWidget(self.spectralAddButtonWidget)
        spectralColourWidget = SpectralColourWidget(self)
        self.spectralColourWidgetList.append(spectralColourWidget)
        self.horizontalLayout_2.addWidget(spectralColourWidget)
        self.horizontalLayout_2.addWidget(self.spectralAddButtonWidget)
        self.horizontalLayout_2.addItem(self.spacerItem)
        self.collectWidget.updateCollectWidget(self)

    def deleteSpectralColourWidget(self):
        self.horizontalLayout_2.removeWidget(self.sender().parent())
        self.spectralColourWidgetList.pop(self.spectralColourWidgetList.index(self.sender().parent()))
        self.collectWidget.updateCollectWidget(self)
        self.sender().parent().deleteLater()
