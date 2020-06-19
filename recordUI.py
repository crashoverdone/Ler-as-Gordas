from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import csv

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(10, 30, 611, 17))
        self.titulo.setScaledContents(True)
        self.titulo.setObjectName("titulo")
        self.hora = QtWidgets.QLabel(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(10, 10, 151, 17))
        self.hora.setScaledContents(True)
        self.hora.setObjectName("hora")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 70, 311, 261))
        self.photo.setObjectName("photo")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(500, 420, 89, 25))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(30, 420, 89, 25))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(260, 420, 89, 25))
        self.btn3.setObjectName("btn3")
        self.texto = QtWidgets.QTextBrowser(self.centralwidget)
        self.texto.setGeometry(QtCore.QRect(340, 70, 281, 261))
        self.texto.setObjectName("texto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.news_group = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Record"))
        self.titulo.setText(_translate("MainWindow", "TextLabel"))
        self.hora.setText(_translate("MainWindow", "TextLabel"))
        self.photo.setText(_translate("MainWindow", "TextLabel"))
        self.btn1.setText(_translate("MainWindow", "Próxima"))
        self.btn2.setText(_translate("MainWindow", "Anterior"))
        self.btn3.setText(_translate("MainWindow", "Primeira"))

        self.i = 0
        self.readFile()
        self.getNews()

        self.btn1.clicked.connect(self.goNext)
        self.btn2.clicked.connect(self.goBack)
        self.btn3.clicked.connect(self.goFirst)

    def readFile(self):
        with open('record.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                self.news_group.append(row)
    
    def getNews(self):
        self.populate(self.news_group[self.i])

    def goNext(self):
        if self.i < len(self.news_group)-2:
            self.i+=1
            self.populate(self.news_group[self.i])
        else:
            pass
            

    def goBack(self):
        if self.i -1 < 0:
            pass
        else:
            self.i-=1
            self.populate(self.news_group[self.i])

    def goFirst(self):
        self.i = 0
        self.populate(self.news_group[0])


    def populate(self,noticia):
        self.hora.setText(noticia[0])
        self.hora.setScaledContents(True)
        self.titulo.setText(noticia[1])
        self.titulo.setScaledContents(True)
        self.texto.setText(noticia[2])
        self.loadPhoto(noticia[3])

    def loadPhoto(self,photo):
        response = requests.get(photo)
        image = QtGui.QImage()
        image.loadFromData(response.content)
        self.photo.setPixmap(QtGui.QPixmap(image)) 
        self.photo.setScaledContents(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

