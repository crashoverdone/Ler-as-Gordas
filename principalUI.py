from PyQt5 import QtCore, QtGui, QtWidgets
from gordas1UI import Ui_MainWindow
from cmUI import Ui_MainWindow1
from recordUI import Ui_MainWindow2
import subprocess

class Ui_principal(object):
    def setupUi(self, principal):
        principal.setObjectName("principal")
        principal.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(principal)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 301, 191))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("abola.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(320, 180))
        self.pushButton.setObjectName("pushButton")
        self.cm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cm_btn.setGeometry(QtCore.QRect(10, 210, 621, 251))
        self.cm_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cm_btn.setIcon(icon1)
        self.cm_btn.setIconSize(QtCore.QSize(300, 300))
        self.cm_btn.setObjectName("cm_btn")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 10, 311, 191))
        self.pushButton_3.setObjectName("pushButton_3")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("record.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(320, 180))
        self.pushButton_3.setText("")
        principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(principal)
        self.statusbar.setObjectName("statusbar")
        principal.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.bolaLoad)
        self.cm_btn.clicked.connect(self.cmLoad)
        self.pushButton_3.clicked.connect(self.recordLoad)

        self.retranslateUi(principal)
        QtCore.QMetaObject.connectSlotsByName(principal)

    def retranslateUi(self, principal):
        _translate = QtCore.QCoreApplication.translate
        principal.setWindowTitle(_translate("principal", "Lêr as Gordas"))

    def bolaLoad(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def cmLoad(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.show()

    def recordLoad(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    subprocess.call(["python","abolascrape.py"])
    subprocess.call(["python","cmscrape.py"])
    subprocess.call(["python","recordscrape.py"])
    app = QtWidgets.QApplication(sys.argv)
    principal = QtWidgets.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec_())

