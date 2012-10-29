# To change this template, choose Tools | Templates
# and open the template in the editor.
import os
from PyQt4 import QtCore, QtGui
from astrophoto.gui.NewItems import *
from astrophoto.gui.SelectCameraInterface import SelectCameraInterface

class PlanWidget(QtGui.QWidget):
    def __init__(self, session):
        super(PlanWidget, self).__init__()
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
        self.session = session
        
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		
        self.opticalSystemLabel = QtGui.QLabel()
        self.opticalSystemLabel.setStyleSheet("font: 7pt")
        self.opticalSystemLabel.setText("Optical System")
        self.opticalSystemWidget = QtGui.QWidget()
        self.opticalSystemWidget.setMinimumWidth(640)
        self.opticalSystemFrame = QtGui.QFrame()
        self.opticalSystemFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.opticalSystemFrame.setFrameShadow(QtGui.QFrame.Raised)
			
        self.opticalSystemLayout = QtGui.QGridLayout(self.opticalSystemWidget)
        self.opticalSystemLayout.setColumnMinimumWidth(0, 10)
        self.opticalSystemLayout.setColumnMinimumWidth(2, 10)
        self.opticalSystemLayout.setColumnMinimumWidth(4, 10)
        self.opticalSystemLayout.setColumnMinimumWidth(6, 10)
        self.opticalSystemLayout.setRowMinimumHeight(1, 7)
        self.opticalSystemLayout.setRowMinimumHeight(3, 2)
        self.opticalSystemLayout.setRowMinimumHeight(5, 2)
        self.opticalSystemLayout.setRowMinimumHeight(7, 2)
        self.opticalSystemLayout.setRowMinimumHeight(9, 2)
        self.opticalSystemLayout.setRowMinimumHeight(11, 7)
        self.opticalSystemLayout.addWidget(self.opticalSystemLabel, 0, 1)
        self.opticalSystemLayout.addWidget(self.opticalSystemFrame, 1, 0, 11, 8)

        self.confNameLabel = QtGui.QLabel()
        self.confNameLabel.setText("Configuration Name:")
        self.opticalSystemLayout.addWidget(self.confNameLabel, 2, 1)
        self.confNameLineEdit = QtGui.QLineEdit()
        self.opticalSystemLayout.addWidget(self.confNameLineEdit, 2, 3)
        
        self.deviceLabel = QtGui.QLabel()
        self.deviceLabel.setText("Select Device:")
        self.opticalSystemLayout.addWidget(self.deviceLabel, 3, 1)
        self.deviceComboBox = QtGui.QComboBox()
        self.opticalSystemLayout.addWidget(self.deviceComboBox, 3, 3)
        self.addDeviceButton = QtGui.QPushButton()
        self.addDeviceButton.setText("Add Device")
        self.addDeviceButton.setMinimumWidth(150)
        self.opticalSystemLayout.addWidget(self.addDeviceButton, 3, 5)
    
        self.telescopeLabel = QtGui.QLabel()
        self.telescopeLabel.setText("Select Telescope:")
        self.opticalSystemLayout.addWidget(self.telescopeLabel, 4, 1)
        self.telescopeComboBox = QtGui.QComboBox()
        self.opticalSystemLayout.addWidget(self.telescopeComboBox, 4, 3)
        self.addTelescopeButton = QtGui.QPushButton()
        self.addTelescopeButton.setText("Add Telescope")
        self.addTelescopeButton.setMinimumWidth(150)
        self.opticalSystemLayout.addWidget(self.addTelescopeButton, 4, 5)
        
        self.adapterLabel = QtGui.QLabel()
        self.adapterLabel.setText("Select Adapter:")
        self.opticalSystemLayout.addWidget(self.adapterLabel, 5, 1)
        self.adapterComboBox = QtGui.QComboBox()
        self.opticalSystemLayout.addWidget(self.adapterComboBox, 5, 3)
        self.addAdapterButton = QtGui.QPushButton()
        self.addAdapterButton.setText("Add Adapter")
        self.addAdapterButton.setMinimumWidth(150)
        self.opticalSystemLayout.addWidget(self.addAdapterButton, 5, 5)
        
        self.tempLabel = QtGui.QLabel()
        self.tempLabel.setText("Chip Temperatur:")
        self.opticalSystemLayout.addWidget(self.tempLabel, 6, 1)
        self.tempLineEdit = QtGui.QLineEdit()
        self.opticalSystemLayout.addWidget(self.tempLineEdit, 6, 3)

        self.configImagesWidget = QtGui.QWidget()
        self.configImagesWidget.setMinimumWidth(640)
        self.configImagesFrame = QtGui.QFrame()
        self.configImagesFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.configImagesFrame.setFrameShadow(QtGui.QFrame.Raised)

        self.configImagesLayout = QtGui.QGridLayout(self.configImagesWidget)
        self.configImagesLayout.setRowMinimumHeight(1, 7)
        self.configImagesLayout.setRowMinimumHeight(3, 2)
        self.configImagesLayout.setRowMinimumHeight(5, 7)
        self.configImagesLayout.setColumnMinimumWidth(0, 10)
        self.configImagesLayout.setColumnMinimumWidth(2, 10)
        self.configImagesLayout.setColumnMinimumWidth(4, 10)
        self.configImagesLayout.setColumnMinimumWidth(6, 10)
	
        self.configImagesLayout.addWidget(self.configImagesFrame, 1, 0, 6, 7)

        self.configImagesLabel = QtGui.QLabel()
        self.configImagesLabel.setText("Configuration Frames")
        self.configImagesLabel.setStyleSheet("font: 7pt")
        self.configImagesLayout.addWidget(self.configImagesLabel, 0, 1)

        self.biasLabel = QtGui.QLabel()
        self.biasLabel.setText("Bias:")
        self.configImagesLayout.addWidget(self.biasLabel, 2,1)
        self.biasResult = QtGui.QLabel()
        print(os.getcwd())
        self.biasResult.setPixmap(QtGui.QPixmap(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.configImagesLayout.addWidget(self.biasResult, 2,3)
        self.takeBiasButton = QtGui.QPushButton()
        self.takeBiasButton.setText("Collect")
        self.configImagesLayout.addWidget(self.takeBiasButton, 2, 5)

        self.darkFrameLabel = QtGui.QLabel()
        self.darkFrameLabel.setText("Dark Frame:")
        self.configImagesLayout.addWidget(self.darkFrameLabel, 3,1)
        self.darkFrameResult = QtGui.QLabel()
        self.darkFrameResult.setPixmap(QtGui.QPixmap(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.configImagesLayout.addWidget(self.darkFrameResult, 3,3)
        self.takeDarkFrameButton = QtGui.QPushButton()
        self.takeDarkFrameButton.setText("Collect")
        self.configImagesLayout.addWidget(self.takeDarkFrameButton, 3, 5)
	
        self.verticalLayout.addWidget(self.opticalSystemWidget)
        self.verticalLayout.addWidget(self.configImagesWidget)
		
        self.fillComboBoxes()

        QtCore.QObject.connect(self.addDeviceButton, QtCore.SIGNAL("clicked()"), self.addNewCamera)
        QtCore.QObject.connect(self.addAdapterButton, QtCore.SIGNAL("clicked()"), self.addNewAdapter)
        QtCore.QObject.connect(self.addTelescopeButton, QtCore.SIGNAL("clicked()"), self.addNewTelescope)
		
    def fillComboBoxes(self):
        for adapter in self.session.workspace.adapterList:
            self.adapterComboBox.addItem(adapter.name)
			
        for telescope in self.session.workspace.telescopeList:
            self.telescopeComboBox.addItem(telescope.name)

        for cameraConfiguration in self.session.workspace.cameraconfigurations:
            self.deviceComboBox.addItem(cameraConfiguration.name)

    def addNewAdapter(self):
        self.newAdapterDialog = NewAdapter(self)
        self.newAdapterDialog.show()

    def addNewTelescope(self):
        self.newTelescopeDialog = NewTelescope(self)
        self.newTelescopeDialog.show()

    def addNewCamera(self):
        self.selectCameraDialog = SelectCameraInterface(self, self.session)
        self.selectCameraDialog.show()

    def createCameraConfiguration(self, cameraName, currentItem):
        print(currentItem.text())
        self.session.createCameraConfiguration(cameraName, currentItem.text())
        self.deviceComboBox.clear()
        for configuration in self.session.workspace.cameraconfigurations:
            self.deviceComboBox.addItem(self.session.workspace.cameraconfigurations.name)
        self.deviceComboBox.setCurrentIndex(self.deviceComboBox.findText(cameraName))

    def createAdapter(self, name):
        self.session.createAdapter(name)
        self.adapterComboBox.clear()
        for adapter in self.session.workspace.adapterList:
            self.adapterComboBox.addItem(adapter.name)
        self.adapterComboBox.setCurrentIndex(self.adapterComboBox.findText(name))

    def createTelescope(self, name):
        self.session.createTelescope(name)
        self.telescopeComboBox.clear()
        for telescope in self.session.workspace.telescopeList:
            self.telescopeComboBox.addItem(telescope.name)
        self.telescopeComboBox.setCurrentIndex(self.telescopeComboBox.findText(name))
