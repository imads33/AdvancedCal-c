import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from Calculator import Ui_MainWindow


class Myapp(QMainWindow):
    def __init__(self):
        super(Myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Zero.clicked.connect(self.ButtonZero)
        self.ui.One.clicked.connect(self.ButtonOne)
        self.ui.Two.clicked.connect(self.ButtonTwo)
        self.ui.Three.clicked.connect(self.ButtonThree)
        self.ui.Four.clicked.connect(self.ButtonFour)
        self.ui.Five.clicked.connect(self.ButtonFive)
        self.ui.Six.clicked.connect(self.ButtonSix)
        self.ui.Seven.clicked.connect(self.ButtonSeven)
        self.ui.Eight.clicked.connect(self.ButtonEight)
        self.ui.Nine.clicked.connect(self.ButtonNine)
        self.ui.Minues.clicked.connect(self.ButtonMinues)
        self.ui.Pluss.clicked.connect(self.ButtonPluss)
        self.ui.Star.clicked.connect(self.ButtonStar)
        self.ui.Divide.clicked.connect(self.ButtonDivide)
        self.ui.Dot.clicked.connect(self.ButtonDot)
        self.ui.Equal.clicked.connect(self.ButtonEqual)
        self.ui.Clear.clicked.connect(self.ButtonClear)
        self.ui.Del.clicked.connect(self.ButtonDel)


    def ButtonZero (self):
        text=self.ui.Result.text()
        self.ui.Result.setText(text+"0")

    def ButtonOne (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "1")

    def ButtonTwo (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "2")

    def ButtonThree (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "3")

    def ButtonFour (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "4")

    def ButtonFive (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "5")

    def ButtonSix (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "6")

    def ButtonSeven (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "7")

    def ButtonEight (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "8")

    def ButtonNine (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "9")

    def ButtonStar (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "*")

    def ButtonPluss (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "+")

    def ButtonMinues (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "-")

    def ButtonDivide (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + "/")

    def ButtonDot (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text + ".")

    def ButtonDel (self):
        text = self.ui.Result.text()
        self.ui.Result.setText(text[:len(text)-1])

    def ButtonClear (self):
        self.ui.Result.setText("")

    def ButtonEqual (self):
        text = self.ui.Result.text()
        try:
            answer = eval(text)
            self.ui.Result.setText(str(answer))
        except:
            self.ui.Result.setText("Wrong Input")


def App():
    app = QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())


App()
