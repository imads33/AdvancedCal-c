# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 643)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Equal.sizePolicy().hasHeightForWidth())
        self.Equal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Equal.setFont(font)
        self.Equal.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Equal.setObjectName("Equal")
        self.gridLayout.addWidget(self.Equal, 5, 3, 1, 1)
        self.Five = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Five.sizePolicy().hasHeightForWidth())
        self.Five.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Five.setFont(font)
        self.Five.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Five.setObjectName("Five")
        self.gridLayout.addWidget(self.Five, 3, 1, 1, 1)
        self.Six = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Six.sizePolicy().hasHeightForWidth())
        self.Six.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Six.setFont(font)
        self.Six.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Six.setObjectName("Six")
        self.gridLayout.addWidget(self.Six, 3, 2, 1, 1)
        self.Star = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Star.sizePolicy().hasHeightForWidth())
        self.Star.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Star.setFont(font)
        self.Star.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Star.setObjectName("Star")
        self.gridLayout.addWidget(self.Star, 3, 3, 1, 1)
        self.Four = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Four.sizePolicy().hasHeightForWidth())
        self.Four.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Four.setFont(font)
        self.Four.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Four.setObjectName("Four")
        self.gridLayout.addWidget(self.Four, 3, 0, 1, 1)
        self.Divide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Divide.sizePolicy().hasHeightForWidth())
        self.Divide.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Divide.setFont(font)
        self.Divide.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Divide.setObjectName("Divide")
        self.gridLayout.addWidget(self.Divide, 4, 3, 1, 1)
        self.Eight = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Eight.sizePolicy().hasHeightForWidth())
        self.Eight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Eight.setFont(font)
        self.Eight.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Eight.setObjectName("Eight")
        self.gridLayout.addWidget(self.Eight, 4, 1, 1, 1)
        self.Seven = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Seven.sizePolicy().hasHeightForWidth())
        self.Seven.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Seven.setFont(font)
        self.Seven.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Seven.setObjectName("Seven")
        self.gridLayout.addWidget(self.Seven, 4, 0, 1, 1)
        self.Nine = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Nine.sizePolicy().hasHeightForWidth())
        self.Nine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Nine.setFont(font)
        self.Nine.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Nine.setObjectName("Nine")
        self.gridLayout.addWidget(self.Nine, 4, 2, 1, 1)
        self.Minues = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Minues.sizePolicy().hasHeightForWidth())
        self.Minues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Minues.setFont(font)
        self.Minues.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Minues.setObjectName("Minues")
        self.gridLayout.addWidget(self.Minues, 2, 3, 1, 1)
        self.Dot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Dot.sizePolicy().hasHeightForWidth())
        self.Dot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Dot.setFont(font)
        self.Dot.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Dot.setObjectName("Dot")
        self.gridLayout.addWidget(self.Dot, 5, 2, 1, 1)
        self.Three = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Three.sizePolicy().hasHeightForWidth())
        self.Three.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Three.setFont(font)
        self.Three.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Three.setObjectName("Three")
        self.gridLayout.addWidget(self.Three, 2, 2, 1, 1)
        self.Del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Del.sizePolicy().hasHeightForWidth())
        self.Del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Del.setFont(font)
        self.Del.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Del.setObjectName("Del")
        self.gridLayout.addWidget(self.Del, 1, 2, 1, 1)
        self.Pluss = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Pluss.sizePolicy().hasHeightForWidth())
        self.Pluss.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Pluss.setFont(font)
        self.Pluss.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Pluss.setObjectName("Pluss")
        self.gridLayout.addWidget(self.Pluss, 1, 3, 1, 1)
        self.One = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.One.sizePolicy().hasHeightForWidth())
        self.One.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.One.setFont(font)
        self.One.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.One.setObjectName("One")
        self.gridLayout.addWidget(self.One, 2, 0, 1, 1)
        self.Two = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Two.sizePolicy().hasHeightForWidth())
        self.Two.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Two.setFont(font)
        self.Two.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Two.setObjectName("Two")
        self.gridLayout.addWidget(self.Two, 2, 1, 1, 1)
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Clear.sizePolicy().hasHeightForWidth())
        self.Clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Clear.setFont(font)
        self.Clear.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Clear.setObjectName("Clear")
        self.gridLayout.addWidget(self.Clear, 1, 0, 1, 2)
        self.Zero = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.Zero.sizePolicy().hasHeightForWidth())
        self.Zero.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Zero.setFont(font)
        self.Zero.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"    background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Zero.setObjectName("Zero")
        self.gridLayout.addWidget(self.Zero, 5, 0, 1, 2)
        self.Result = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.Result.sizePolicy().hasHeightForWidth())
        self.Result.setSizePolicy(sizePolicy)
        self.Result.setStyleSheet("font: 28pt \"Mongolian Baiti\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 148, 148);")
        self.Result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Result.setObjectName("Result")
        self.gridLayout.addWidget(self.Result, 0, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator (by Imad)"))
        self.Equal.setText(_translate("MainWindow", "="))
        self.Equal.setShortcut(_translate("MainWindow", "="))
        self.Five.setText(_translate("MainWindow", "5"))
        self.Five.setShortcut(_translate("MainWindow", "5"))
        self.Six.setText(_translate("MainWindow", "6"))
        self.Six.setShortcut(_translate("MainWindow", "6"))
        self.Star.setText(_translate("MainWindow", "x"))
        self.Star.setShortcut(_translate("MainWindow", "*"))
        self.Four.setText(_translate("MainWindow", "4"))
        self.Four.setShortcut(_translate("MainWindow", "4"))
        self.Divide.setText(_translate("MainWindow", "÷"))
        self.Divide.setShortcut(_translate("MainWindow", "/"))
        self.Eight.setText(_translate("MainWindow", "8"))
        self.Eight.setShortcut(_translate("MainWindow", "8"))
        self.Seven.setText(_translate("MainWindow", "7"))
        self.Seven.setShortcut(_translate("MainWindow", "7"))
        self.Nine.setText(_translate("MainWindow", "9"))
        self.Nine.setShortcut(_translate("MainWindow", "9"))
        self.Minues.setText(_translate("MainWindow", "-"))
        self.Minues.setShortcut(_translate("MainWindow", "-"))
        self.Dot.setText(_translate("MainWindow", "."))
        self.Dot.setShortcut(_translate("MainWindow", "."))
        self.Three.setText(_translate("MainWindow", "3"))
        self.Three.setShortcut(_translate("MainWindow", "3"))
        self.Del.setText(_translate("MainWindow", "Del"))
        self.Del.setShortcut(_translate("MainWindow", "Backspace"))
        self.Pluss.setText(_translate("MainWindow", "+"))
        self.Pluss.setShortcut(_translate("MainWindow", "+"))
        self.One.setText(_translate("MainWindow", "1"))
        self.One.setShortcut(_translate("MainWindow", "1"))
        self.Two.setText(_translate("MainWindow", "2"))
        self.Two.setShortcut(_translate("MainWindow", "2"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.Clear.setShortcut(_translate("MainWindow", "Q"))
        self.Zero.setText(_translate("MainWindow", "0"))
        self.Zero.setShortcut(_translate("MainWindow", "0"))
        self.Result.setText(_translate("MainWindow", ""))
