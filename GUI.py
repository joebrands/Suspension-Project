# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1125, 488)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 231))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 104, 71))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 250, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(50, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(60, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(160, 20, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 50, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_3.setGeometry(QtCore.QRect(160, 80, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_4.setGeometry(QtCore.QRect(160, 110, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_4.setObjectName("spinBox_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 250, 221, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.spinBox_8 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_8.setGeometry(QtCore.QRect(140, 20, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_8.setFont(font)
        self.spinBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_7.setGeometry(QtCore.QRect(140, 110, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_7.setFont(font)
        self.spinBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_6.setGeometry(QtCore.QRect(140, 80, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_6.setFont(font)
        self.spinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_5.setGeometry(QtCore.QRect(140, 50, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_5.setFont(font)
        self.spinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_5.setObjectName("spinBox_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Ground Data"))
        self.groupBox_2.setTitle(_translate("Dialog", "Suspension Data"))
        self.label_8.setText(_translate("Dialog", "Max Shock Displacement"))
        self.label_6.setText(_translate("Dialog", "Tire Springrate"))
        self.label_5.setText(_translate("Dialog", "Shock Springrate"))
        self.label_7.setText(_translate("Dialog", "Shock Damping Factor"))
        self.groupBox_3.setTitle(_translate("Dialog", "Vehicle Data"))
        self.label.setText(_translate("Dialog", "Body Weight"))
        self.label_2.setText(_translate("Dialog", "CG Location"))
        self.label_3.setText(_translate("Dialog", "Wheel & Tire Weight"))
        self.label_4.setText(_translate("Dialog", "Tire Radius"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

