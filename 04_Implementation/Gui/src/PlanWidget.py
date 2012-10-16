# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4 import QtCore, QtGui

class PlanWidget(QtGui.QWidget):
    def __init__(self):
        super(PlanWidget, self).__init__()
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
        
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		
        self.opticalSystemLabel = QtGui.QLabel()
        self.opticalSystemLabel.setStyleSheet("font: 7pt")
        self.opticalSystemLabel.setText("Optical System")
        self.opticalSystemWidget = QtGui.QWidget()
        self.opticalSystemWidget.setMinimumWidth(610)
        self.opticalSystemFrame = QtGui.QFrame()
        self.opticalSystemFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.opticalSystemFrame.setFrameShadow(QtGui.QFrame.Raised)
		
		
		
        self.gridFrameLayout = QtGui.QGridLayout(self.opticalSystemWidget)
        self.gridFrameLayout.setColumnMinimumWidth(0, 0)
        self.gridFrameLayout.setColumnMinimumWidth(2, 10)
        self.gridFrameLayout.setColumnMinimumWidth(4, 10)
        self.gridFrameLayout.setColumnMinimumWidth(6, 10)
        self.gridFrameLayout.setRowMinimumHeight(1, 7)
        self.gridFrameLayout.setRowMinimumHeight(3, 2)
        self.gridFrameLayout.setRowMinimumHeight(5, 2)
        self.gridFrameLayout.setRowMinimumHeight(7, 2)
        self.gridFrameLayout.setRowMinimumHeight(9, 7)
        self.gridFrameLayout.addWidget(self.opticalSystemLabel, 0, 1)
        self.gridFrameLayout.addWidget(self.opticalSystemFrame, 1, 0, 9, 8)
        
        self.cameraLabel = QtGui.QLabel(self.opticalSystemFrame)
        self.cameraLabel.setText("Select Camera:")
        self.gridFrameLayout.addWidget(self.cameraLabel, 2, 1)
        self.cameraComboBox = QtGui.QComboBox(self.opticalSystemFrame)
        self.gridFrameLayout.addWidget(self.cameraComboBox, 2, 3)
        self.addCameraButton = QtGui.QPushButton(self.opticalSystemFrame)
        self.addCameraButton.setText("Add Camera")
        self.addCameraButton.setMinimumWidth(150)
        self.gridFrameLayout.addWidget(self.addCameraButton, 2, 5)
    
        self.telescopeLabel = QtGui.QLabel(self.opticalSystemFrame)
        self.telescopeLabel.setText("Select Telescope:")
        self.gridFrameLayout.addWidget(self.telescopeLabel, 4, 1)
        self.telescopeComboBox = QtGui.QComboBox(self.opticalSystemFrame)
        self.gridFrameLayout.addWidget(self.telescopeComboBox, 4, 3)
        self.addTelescopeButton = QtGui.QPushButton(self.opticalSystemFrame)
        self.addTelescopeButton.setText("Add Telescope")
        self.addTelescopeButton.setMinimumWidth(150)
        self.gridFrameLayout.addWidget(self.addTelescopeButton, 4, 5)
        
        self.adapterLabel = QtGui.QLabel(self.opticalSystemFrame)
        self.adapterLabel.setText("Select Adapter:")
        self.gridFrameLayout.addWidget(self.adapterLabel, 6, 1)
        self.adapterComboBox = QtGui.QComboBox(self.opticalSystemFrame)
        self.gridFrameLayout.addWidget(self.adapterComboBox, 6, 3)
        self.addAdapterButton = QtGui.QPushButton(self.opticalSystemFrame)
        self.addAdapterButton.setText("Add Adapter")
        self.addAdapterButton.setMinimumWidth(150)
        self.gridFrameLayout.addWidget(self.addAdapterButton, 6, 5)
        
        self.tempLabel = QtGui.QLabel(self.opticalSystemFrame)
        self.tempLabel.setText("Chip Temperatur:")
        self.gridFrameLayout.addWidget(self.tempLabel, 8, 1)
        self.tempLineEdit = QtGui.QLineEdit(self.opticalSystemFrame)
        self.gridFrameLayout.addWidget(self.tempLineEdit, 8, 3)
	
        self.verticalLayout.addWidget(self.opticalSystemWidget)
