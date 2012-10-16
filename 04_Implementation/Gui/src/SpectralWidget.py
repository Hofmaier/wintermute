# To change this template, choose Tools | Templates
# and open the template in the editor.
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
        
        
        #self.horizontalLayout = QtGui.QVBoxLayout()
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setMinimumHeight(560)
        self.scrollArea.setMinimumWidth(600)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 640, 560))
        #self.scrollAreaWidgetContents.setMinimumHeight(550)
        #self.scrollAreaWidgetContents.setMinimumWidth(580)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QtGui.QGridLayout()
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        #self.horizontalLayout.addWidget(self.scrollArea)
       
        
        
        widget = QtGui.QWidget()
        widget.setMinimumWidth(200)
        widget.setMinimumHeight(200)
        
        frame = QtGui.QFrame(widget)
        frame.setFrameShape(QtGui.QFrame.StyledPanel)
        frame.setFrameShadow(QtGui.QFrame.Raised)
        frame.setGeometry(QtCore.QRect(0, 0, 200, 200))
        textLabel = QtGui.QLineEdit(frame) 
        self.gridLayout.addWidget(widget)
        
        
     
       
