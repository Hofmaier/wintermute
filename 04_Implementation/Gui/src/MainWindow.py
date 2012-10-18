# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Oct 12 21:49:15 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from SpectralWidget import SpectralWidget
from PlanWidget import PlanWidget
from ConfigWidget import ConfigWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.centralWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        #self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        #self.horizontalLayoutWidget.setMinimumHeight(600)
        #self.horizontalLayoutWidget.setMinimumWidth(800)
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))

        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        
        self.listWidget = QtGui.QListWidget()
        #self.listWidget.setGeometry(QtCore.QRect(0, 0, 140, 560))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.setMinimumHeight(560)
        self.listWidget.setMinimumWidth(140)
        self.listWidget.setMaximumWidth(140)
        self.horizontalLayout.addWidget(self.listWidget)
        
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setFont(font)
        self.listWidget.addItem(item)
    
        
 
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.planWidget = PlanWidget()
        self.planWidget.show()
        self.listWidget.setCurrentItem(self.listWidget.item(0))
        self.horizontalLayout.addWidget(self.planWidget)
        self.spectralWidget = SpectralWidget()
        self.spectralWidget.hide()
        self.horizontalLayout.addWidget(self.spectralWidget)
        self.configWidget = ConfigWidget()
        self.configWidget.hide()
        self.horizontalLayout.addWidget(self.configWidget)
      
        
        

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.menuEntryChanged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Plan", None, QtGui.QApplication.UnicodeUTF8))
        item = self.listWidget.item(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Spectrals", None, QtGui.QApplication.UnicodeUTF8))
        item = self.listWidget.item(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def menuEntryChanged(self, item):
        if item.text() == "Plan":
            self.planWidget.show()
            self.spectralWidget.hide()
            self.configWidget.hide()
        elif item.text() == "Spectrals":
            self.spectralWidget.show()
            self.planWidget.hide()
            self.configWidget.hide()
        elif item.text() == "Configuration":
            self.configWidget.show()
            self.spectralWidget.hide()
            self.planWidget.hide()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
