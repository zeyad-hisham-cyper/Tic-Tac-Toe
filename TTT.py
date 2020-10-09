from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

play_Flag = 0
playerX = 0
playerO = 0
tie = 0

class Ui_MainWindow(object):


    def reset(self):
        self.Pb1.setEnabled(True)
        self.Pb2.setEnabled(True)
        self.Pb3.setEnabled(True)
        self.Pb4.setEnabled(True)
        self.Pb5.setEnabled(True)
        self.Pb6.setEnabled(True)
        self.Pb7.setEnabled(True)
        self.Pb8.setEnabled(True)
        self.Pb9.setEnabled(True)
        self.Pb1.setText("")
        self.Pb2.setText("")
        self.Pb3.setText("")
        self.Pb4.setText("")
        self.Pb5.setText("")
        self.Pb6.setText("")
        self.Pb7.setText("")
        self.Pb8.setText("")
        self.Pb9.setText("")

    def but_click(self, pos):
        mark = ''
        global play_Flag

        if play_Flag % 2 == 0:
            mark = 'X'

        else:
            mark = 'O'

        if pos == 1:
            self.Pb1.setText(mark)
            self.Pb1.setEnabled(False)
        if pos == 2:
            self.Pb2.setText(mark)
            self.Pb2.setEnabled(False)
        if pos == 3:
            self.Pb3.setText(mark)
            self.Pb3.setEnabled(False)
        if pos == 4:
            self.Pb4.setText(mark)
            self.Pb4.setEnabled(False)
        if pos == 5:
            self.Pb5.setText(mark)
            self.Pb5.setEnabled(False)
        if pos == 6:
            self.Pb6.setText(mark)
            self.Pb6.setEnabled(False)
        if pos == 7:
            self.Pb7.setText(mark)
            self.Pb7.setEnabled(False)
        if pos == 8:
            self.Pb8.setText(mark)
            self.Pb8.setEnabled(False)
        if pos == 9:
            self.Pb9.setText(mark)
            self.Pb9.setEnabled(False)
        play_Flag += 1
        self.check_win()

    def check_win(self):
        winner = ""
        global tie
        global playerX
        global playerO

        msg = QMessageBox()
        msg.setWindowTitle("Alert")

        if self.Pb1.text() == self.Pb2.text() == self.Pb3.text():
            winner = self.Pb1.text()
        if self.Pb4.text() == self.Pb5.text() == self.Pb6.text():
            winner = self.Pb4.text()
        elif self.Pb7.text() == self.Pb8.text() == self.Pb9.text():
            winner = self.Pb7.text()
        elif self.Pb1.text() == self.Pb4.text() == self.Pb7.text():
            winner = self.Pb7.text()
        elif self.Pb2.text() == self.Pb5.text() == self.Pb8.text():
            winner = self.Pb2.text()
        elif self.Pb3.text() == self.Pb6.text() == self.Pb9.text():
            winner = self.Pb3.text()
        elif self.Pb1.text() == self.Pb5.text() == self.Pb9.text():
            winner = self.Pb9.text()
        elif self.Pb3.text() == self.Pb5.text() == self.Pb7.text():
            winner = self.Pb3.text()
        if winner == 'X':
            playerX += 1
            self.label.setText('playerX: ' + str(playerX))
            msg.setText('PlayerX is the winner')
            msg.exec_()
            self.reset()
        elif winner == 'O':
            playerO += 1
            self.label_2.setText('PlayerO: ' + str(playerO))
            msg.setText('PlayerO is the winner')
            msg.exec_()
            self.reset()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 570)
        MainWindow.setWindowIcon(QIcon("icon-rounded.png"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 9, 361, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Button 7
        self.Pb7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb7.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb7.setFont(font)
        self.Pb7.setText("")
        self.Pb7.setObjectName("Pb7")
        self.gridLayout.addWidget(self.Pb7, 2, 0, 1, 1)
        self.Pb7.clicked.connect(lambda: self.but_click(7))

        # Button 4
        self.Pb4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb4.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb4.setFont(font)
        self.Pb4.setText("")
        self.Pb4.setObjectName("Pb4")
        self.gridLayout.addWidget(self.Pb4, 1, 0, 1, 1)
        self.Pb4.clicked.connect(lambda: self.but_click(4))

        # Button 5
        self.Pb5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb5.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb5.setFont(font)
        self.Pb5.setText("")
        self.Pb5.setObjectName("Pb5")
        self.gridLayout.addWidget(self.Pb5, 1, 1, 1, 1)
        self.Pb5.clicked.connect(lambda: self.but_click(5))

        # Button 8
        self.Pb8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb8.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb8.setFont(font)
        self.Pb8.setText("")
        self.Pb8.setObjectName("Pb8")
        self.gridLayout.addWidget(self.Pb8, 2, 1, 1, 1)
        self.Pb8.clicked.connect(lambda: self.but_click(8))

        # Button 1
        self.Pb1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb1.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb1.setFont(font)
        self.Pb1.setText("")
        self.Pb1.setObjectName("Pb1")
        self.gridLayout.addWidget(self.Pb1, 0, 0, 1, 1)
        self.Pb1.clicked.connect(lambda: self.but_click(1))

        # Button 2
        self.Pb2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb2.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb2.setFont(font)
        self.Pb2.setText("")
        self.Pb2.setObjectName("Pb2")
        self.gridLayout.addWidget(self.Pb2, 0, 1, 1, 1)
        self.Pb2.clicked.connect(lambda: self.but_click(2))

        # Button 3
        self.Pb3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb3.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb3.setFont(font)
        self.Pb3.setText("")
        self.Pb3.setObjectName("Pb3")
        self.gridLayout.addWidget(self.Pb3, 0, 2, 1, 1)
        self.Pb3.clicked.connect(lambda: self.but_click(3))

        # Button 6
        self.Pb6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb6.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb6.setFont(font)
        self.Pb6.setText("")
        self.Pb6.setObjectName("Pb6")
        self.gridLayout.addWidget(self.Pb6, 1, 2, 1, 1)
        self.Pb6.clicked.connect(lambda: self.but_click(6))

        # Button 9
        self.Pb9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Pb9.setMinimumSize(QtCore.QSize(93, 93))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pb9.setFont(font)
        self.Pb9.setText("")
        self.Pb9.setObjectName("Pb9")
        self.gridLayout.addWidget(self.Pb9, 2, 2, 1, 1)
        self.Pb9.clicked.connect(lambda: self.but_click(9))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 430, 71, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 430, 71, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(175, 430, 71, 41))
        self.label_3.setObjectName("label_3")


        # RESET
        self.res = QtWidgets.QPushButton(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(150, 500, 91, 41))
        self.res.setObjectName("res")
        self.res.clicked.connect(self.reset)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Tic Tac Toe", "Tic Tac Toe"))
        self.label.setText(_translate("MainWindow", "Player'X':"))
        self.label_2.setText(_translate("MainWindow", "Player'O':"))
        self.res.setText(_translate("MainWindow", "Reset"))
        self.centralwidget.setStyleSheet("background-color : pink;")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
