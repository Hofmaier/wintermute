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
        
        self.frameWidget = QtGui.QWidget()
        self.frameWidget.setMinimumWidth(610)
        self.frame = QtGui.QFrame()
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
	self.opticalSystemLabel = QtGui.QLabel()
	self.opticalSystemLabel.setStyleSheet("font: 10pt")
	self.opticalSystemLabel.setText("Optical System")
	
        self.gridFrameLayout = QtGui.QGridLayout(self.frameWidget)
        self.gridFrameLayout.setColumnMinimumWidth(0, 0)
        self.gridFrameLayout.setColumnMinimumWidth(2, 10)
        self.gridFrameLayout.setColumnMinimumWidth(4, 10)
        self.gridFrameLayout.setColumnMinimumWidth(6, 10)
        self.gridFrameLayout.setRowMinimumHeight(0, 2)
        self.gridFrameLayout.setRowMinimumHeight(2, 2)
        self.gridFrameLayout.setRowMinimumHeight(4, 2)
        self.gridFrameLayout.setRowMinimumHeight(6, 2)
        self.gridFrameLayout.setRowMinimumHeight(8, 2)
        self.gridFrameLayout.addWidget(self.frame, 0, 0, 0, 7)
        
        self.cameraLabel = QtGui.QLabel(self.frame)
        self.cameraLabel.setText("Select Camera:")
        self.gridFrameLayout.addWidget(self.cameraLabel, 1, 1)
        self.cameraComboBox = QtGui.QComboBox(self.frame)
        self.gridFrameLayout.addWidget(self.cameraComboBox, 1, 3)
        self.addCameraButton = QtGui.QPushButton(self.frame)
        self.addCameraButton.setText("Add Camera")
        self.addCameraButton.setMinimumWidth(150)
        self.gridFrameLayout.addWidget(self.addCameraButton, 1, 5)
    
        self.telescopeLabel = QtGui.QLabel(self.frame)
        self.telescopeLabel.setText("Select Telescope:")
        self.gridFrameLayout.addWidget(self.telescopeLabel, 3, 1)
        self.telescopeComboBox = QtGui.QComboBox(self.frame)
        self.gridFrameLayout.addWidget(self.telescopeComboBox, 3, 3)
        self.addTelescopeButton = QtGui.QPushButton(self.frame)
        self.addTelescopeButton.setText("Add Telescope")
        self.addTelescopeButton.setMinimumWidth(150)
        self.gridFrameLayout.addWidget(self.addTelescopeButton, 3, 5)
        
        self.adapterLabel = QtGui.QLabel(self.frame)
        self.adapterLabel.setText("Select Adapter:")
        self.gridFrameLayout.addWidget(self.adapterLabel, 5, 1)
        self.adapterComboBox = QtGui.QComboBox(self.frame)
        self.gridFrameLayout.addWidget(self.adapterComboBox, 5, 3)
        self.addAdapterButton = QtGui.QPushButton(self.frame)
        self.addAdapterButton.setText("Add Adapter")
        self.addAdapterButton.setMinimumWidth(150)
        self.gridFrameLayout.addWidget(self.addAdapterButton, 5, 5)
        
        self.tempLabel = QtGui.QLabel(self.frame)
        self.tempLabel.setText("Chip Temperatur:")
        self.gridFrameLayout.addWidget(self.tempLabel, 7, 1)
        self.tempLineEdit = QtGui.QLineEdit(self.frame)
        self.gridFrameLayout.addWidget(self.tempLineEdit, 7, 3)
	
	self.verticalLayout.addWidget(self.opticalSystemLabel)
        self.verticalLayout.addWidget(self.frameWidget)
