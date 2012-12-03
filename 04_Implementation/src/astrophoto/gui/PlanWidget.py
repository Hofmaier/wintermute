# To change this template, choose Tools | Templates
# and open the template in the editor.
import os
from PyQt4 import QtCore, QtGui
from astrophoto.gui.NewItems import *
from astrophoto.gui.SelectCameraInterface import SelectCameraInterface
from astrophoto.gui.BiasCollect import BiasCollect

class PlanWidget(QtGui.QWidget):
    def __init__(self, session, mainWindow):
        super(PlanWidget, self).__init__()
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
        self.session = session
        self.mainWindow = mainWindow

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
        self.opticalSystemLayout.setColumnMinimumWidth(4, 10)

        self.opticalSystemLayout.setRowMinimumHeight(1, 7)
        self.opticalSystemLayout.setRowMinimumHeight(5, 7)

        self.opticalSystemLayout.addWidget(self.opticalSystemLabel, 0, 1)
        self.opticalSystemLayout.addWidget(self.opticalSystemFrame, 1, 0, 7, 5)

#        self.confNameLabel = QtGui.QLabel()
#        self.confNameLabel.setText("Configuration Name:")
#        self.opticalSystemLayout.addWidget(self.confNameLabel, 2, 1)
#        self.confNameLineEdit = QtGui.QLineEdit()
#        self.opticalSystemLayout.addWidget(self.confNameLineEdit, 2, 3)
        
        self.deviceLabel = QtGui.QLabel()
        self.deviceLabel.setText("Select Device:")
        self.opticalSystemLayout.addWidget(self.deviceLabel, 2, 1)
        self.deviceComboBox = QtGui.QComboBox()
        self.opticalSystemLayout.addWidget(self.deviceComboBox, 2, 2)
        self.addDeviceButton = QtGui.QPushButton()
        self.addDeviceButton.setText("Add Device")
        self.addDeviceButton.setMaximumWidth(180)
        self.opticalSystemLayout.addWidget(self.addDeviceButton, 2, 3)
    
        self.telescopeLabel = QtGui.QLabel()
        self.telescopeLabel.setText("Select Telescope:")
        self.opticalSystemLayout.addWidget(self.telescopeLabel, 3, 1)
        self.telescopeComboBox = QtGui.QComboBox()
        self.opticalSystemLayout.addWidget(self.telescopeComboBox, 3, 2)
        self.addTelescopeButton = QtGui.QPushButton()
        self.addTelescopeButton.setText("Add Telescope")
        self.addDeviceButton.setMaximumWidth(180)
        self.opticalSystemLayout.addWidget(self.addTelescopeButton, 3, 3)

        self.adapterLabel = QtGui.QLabel()
        self.adapterLabel.setText("Select Adapter:")
        self.opticalSystemLayout.addWidget(self.adapterLabel, 4, 1)
        self.adapterComboBox = QtGui.QComboBox()
        self.opticalSystemLayout.addWidget(self.adapterComboBox, 4, 2)
        self.addAdapterButton = QtGui.QPushButton()
        self.addAdapterButton.setText("Add Adapter")
        self.addDeviceButton.setMaximumWidth(180)
        self.opticalSystemLayout.addWidget(self.addAdapterButton, 4, 3)

#        self.tempLabel = QtGui.QLabel()
#        self.tempLabel.setText("Chip Temperatur:")
#        self.opticalSystemLayout.addWidget(self.tempLabel, 5, 1)
#        self.tempLineEdit = QtGui.QLineEdit()
#        self.opticalSystemLayout.addWidget(self.tempLineEdit, 5, 2, 1, 2)

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
        self.biasResult.setPixmap(QtGui.QPixmap(os.getcwd() + "/astrophoto/gui/icons/delete-icon.png"))
        self.configImagesLayout.addWidget(self.biasResult, 2,3)
        self.takeBiasButton = QtGui.QPushButton()
        self.takeBiasButton.setText("Collect")
        self.configImagesLayout.addWidget(self.takeBiasButton, 2, 5)

        self.verticalLayout.addWidget(self.opticalSystemWidget)
        self.verticalLayout.addWidget(self.configImagesWidget)

        self.fillComboBoxes()

        QtCore.QObject.connect(self.addDeviceButton, QtCore.SIGNAL("clicked()"), self.addNewCamera)
        QtCore.QObject.connect(self.addAdapterButton, QtCore.SIGNAL("clicked()"), self.addNewAdapter)
        QtCore.QObject.connect(self.addTelescopeButton, QtCore.SIGNAL("clicked()"), self.addNewTelescope)
        QtCore.QObject.connect(self.takeBiasButton, QtCore.SIGNAL("clicked()"), self.takeBias)
        QtCore.QObject.connect(self.deviceComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.saveCameraConfiguration)
        QtCore.QObject.connect(self.adapterComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.saveOpticalSystem)
        QtCore.QObject.connect(self.telescopeComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.saveOpticalSystem)

    def fillComboBoxes(self):
        for adapter in self.session.workspace.adapterList:
            self.adapterComboBox.addItem(adapter.name, adapter)
        for telescope in self.session.workspace.telescopeList:
            self.telescopeComboBox.addItem(telescope.name, telescope)
        for cameraConfiguration in self.session.workspace.cameraconfigurations:
            self.deviceComboBox.addItem(cameraConfiguration.name, cameraConfiguration)
        self.deviceComboBox.setCurrentIndex(-1)
        self.adapterComboBox.setCurrentIndex(-1)
        self.telescopeComboBox.setCurrentIndex(-1)

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
        interFaceName = str(currentItem.text())
        camConfig = self.session.createCameraConfiguration(cameraName, interFaceName)
        print(self.session.currentProject.cameraconfiguration.name)
        self.deviceComboBox.clear()
        for configuration in self.session.workspace.cameraconfigurations:
            self.deviceComboBox.addItem(configuration.name, configuration)
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

    def checkAllVariablesSet(self):
#        if self.deviceComboBox.currentText() == "":
#            return False
#        elif self.telescopeComboBox.currentText() == "":
#            return False
#        elif self.adapterComboBox.currentText() == "":
#            return False
#        elif self.tempLineEdit.text() == "":
#            return False
        return True

    def saveCameraConfiguration(self):
        print("Saving CameraConfiguration")
        cameraConfiguration = self.getCameraConfigurationByName(self.deviceComboBox.currentText())
        self.session.currentProject.cameraconfiguration = cameraConfiguration

    def saveOpticalSystem(self):
        print("Saving OpticalSystem")
        adapter = self.getAdapterByName(self.adapterComboBox.currentText())
        telescope = self.getTelescopeByName(self.telescopeComboBox.currentText())
        opticalSystem = self.session.currentProject.opticalSystem
        if opticalSystem == None:
            opticalSystem = self.session.createOpticalSystem("testing", adapter, telescope)
            self.session.currentProject.opticalSystem = opticalSystem
        else:
            opticalSystem.adapter = adapter
            opticalSystem.telescope = telescope

    def getOpticalSystem(self, adapter, telescope):
        for opticalSystem in self.session.workspace.opticalSystemList:
            if opticalSystem.adapter is adapter and opticalSystem.telescope is telescope:
                return opticalSystem

    def getCameraConfigurationByName(self, cameraName):
        for cameraConf in self.session.workspace.cameraconfigurations:
            if cameraConf.name == cameraName:
                return cameraConf

    def getAdapterByName(self, adapterName):
        for adapter in self.session.workspace.adapterList:
            if adapter.name == adapterName:
                return adapter

    def getTelescopeByName(self, telescopeName):
        for telescope in self.session.workspace.telescopeList:
            if telescope.name == telescopeName:
                return telescope

    def loadProject(self):
        opticalSystem = self.session.currentProject.opticalSystem
        if not opticalSystem is None:
            if opticalSystem.telescope is not None:
                telescopeName = opticalSystem.telescope.name
            if opticalSystem.adapter is not None:
                adapterName = opticalSystem.adapter.name
        self.adapterComboBox.setCurrentIndex(self.adapterComboBox.findText(adapterName))
        self.telescopeComboBox.setCurrentIndex(self.telescopeComboBox.findText(telescopeName))
        cameraConfiguration = self.session.currentProject.cameraconfiguration
        if not cameraConfiguration is None:
            self.deviceComboBox.setCurrentIndex(self.deviceComboBox.findText(cameraConfiguration.name))

    def takeBias(self):
        if self.session.currentProject.cameraconfiguration is None:
            self.mainWindow.statusBar.showMessage("No Camera selected! Please select a camera before taking a bias!")
        else:
            self.mainWindow.statusBar.showMessage("")
            self.biasCollect = BiasCollect(self.session)
            self.biasCollect.show()

