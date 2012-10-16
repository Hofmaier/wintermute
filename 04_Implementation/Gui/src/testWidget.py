# To change this template, choose Tools | Templates
# and open the template in the editor.


# To change this template, choose Tools | Templates
# and open the template in the editor.

from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
class TestWidget(QtGui.QWidget):
    def __init__(self, scrollLayout, position):
        super(TestWidget, self).__init__(scrollLayout)
        self.setGeometry(QtCore.QRect(10, position, 580, 150))
        self.setObjectName(_fromUtf8("widget"))
        self.frame = QtGui.QFrame()
        self.frame.setGeometry(QtCore.QRect(0, 0, 580, 150))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame.show()
        self.show()


