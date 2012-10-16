# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4 import QtCore, QtGui

class ConfigWidget(QtGui.QWidget):
    def __init__(self):
        super(ConfigWidget, self).__init__()
        #self.setGeometry(QtCore.QRect(150, 10, 640, 560))
        self.setMinimumHeight(560)
        self.setMinimumWidth(640)
        self. button = QtGui.QPushButton(self)
        self.button.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.button.setText("Config")


