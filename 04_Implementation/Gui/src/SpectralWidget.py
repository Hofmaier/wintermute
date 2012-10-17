# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SpectralWidget(QtGui.QWidget):
    def __init__(self):
        self.buttonPosition = 170
        self.framePosition = 10
        super(SpectralWidget, self).__init__()
        #self.setGeometry(QtCore.QRect(150, 4, 640, 580))
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
        self.spacerItem = QtGui.QSpacerItem(0,0,QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        
        
        #self.horizontalLayout = QtGui.QVBoxLayout()
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setMinimumHeight(560)
        self.scrollArea.setMinimumWidth(640)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 640, 560))
        self.scrollAreaWidgetContents.setMinimumHeight(550)
        self.scrollAreaWidgetContents.setMinimumWidth(620)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_2 = QtGui.QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.horizontalLayout_2)
        #self.gridLayout = QtGui.QGridLayout()
        #self.horizontalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        #self.horizontalLayout.addWidget(self.scrollArea)
       
        
        
        self.spectralWidget = QtGui.QWidget()
        #self.spectralWidget.setMinimumWidth(200)
        #self.spectralWidget.setMaximumHeight(200)
        self.spectralLayout = QtGui.QGridLayout()

        self.spectralWidget.setLayout(self.spectralLayout)
        self.spectralLayout.setRowMinimumHeight(1, 7)
        self.spectralLayout.setRowMinimumHeight(3, 2)
        self.spectralLayout.setRowMinimumHeight(5, 7)
        self.spectralLayout.setColumnMinimumWidth(0, 10)
        self.spectralLayout.setColumnMinimumWidth(2, 10)
        self.spectralLayout.setColumnMinimumWidth(4, 10)
        
        self.frame = QtGui.QFrame()
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.spectralLayout.addWidget(self.frame, 0, 0, 7, 5)

        self.spectralLabel = QtGui.QLabel()
        self.spectralLabel.setText("Spectral:")
        self.spectralLayout.addWidget(self.spectralLabel, 2, 1)
        self.spectralLineEdit = QtGui.QLineEdit()
        self.spectralLayout.addWidget(self.spectralLineEdit, 2, 3)
        
        self.numberOfImagesLabel = QtGui.QLabel()
        self.numberOfImagesLabel.setText("Number of Images:")
        self.spectralLayout.addWidget(self.numberOfImagesLabel, 4, 1)
        self.numberOfImagesLineEdit = QtGui.QLineEdit()
        self.spectralLayout.addWidget(self.numberOfImagesLineEdit, 4, 3)
		
        self.horizontalLayout_2.addWidget(self.spectralWidget)
        self.horizontalLayout_2.addItem(self.spacerItem)
        
        
     
       
