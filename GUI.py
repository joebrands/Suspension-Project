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
        Dialog.resize(541, 421)
        Dialog.setAutoFillBackground(False)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_getdata = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_getdata.setGeometry(QtCore.QRect(10, 20, 211, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_getdata.setFont(font)
        self.pushButton_getdata.setObjectName("pushButton_getdata")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.spinBox_tracklength = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_tracklength.setEnabled(False)
        self.spinBox_tracklength.setGeometry(QtCore.QRect(150, 60, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_tracklength.setFont(font)
        self.spinBox_tracklength.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_tracklength.setObjectName("spinBox_tracklength")
        self.textEdit_filepath = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_filepath.setEnabled(False)
        self.textEdit_filepath.setGeometry(QtCore.QRect(230, 40, 281, 41))
        self.textEdit_filepath.setObjectName("textEdit_filepath")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(230, 20, 101, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 110, 261, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(-10, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(50, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(80, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.spinBox_shockdisp = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_shockdisp.setGeometry(QtCore.QRect(180, 20, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_shockdisp.setFont(font)
        self.spinBox_shockdisp.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_shockdisp.setObjectName("spinBox_shockdisp")
        self.spinBox_shockspring = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_shockspring.setGeometry(QtCore.QRect(180, 50, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_shockspring.setFont(font)
        self.spinBox_shockspring.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_shockspring.setObjectName("spinBox_shockspring")
        self.spinBox_tirespring = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_tirespring.setGeometry(QtCore.QRect(180, 80, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_tirespring.setFont(font)
        self.spinBox_tirespring.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_tirespring.setObjectName("spinBox_tirespring")
        self.spinBox_dampingfac = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_dampingfac.setGeometry(QtCore.QRect(180, 110, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_dampingfac.setFont(font)
        self.spinBox_dampingfac.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_dampingfac.setObjectName("spinBox_dampingfac")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 110, 251, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(40, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.spinBox_bodyweight = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_bodyweight.setGeometry(QtCore.QRect(170, 20, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_bodyweight.setFont(font)
        self.spinBox_bodyweight.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_bodyweight.setObjectName("spinBox_bodyweight")
        self.spinBox_tireradius = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_tireradius.setGeometry(QtCore.QRect(170, 110, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_tireradius.setFont(font)
        self.spinBox_tireradius.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_tireradius.setObjectName("spinBox_tireradius")
        self.spinBox_wheelweight = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_wheelweight.setGeometry(QtCore.QRect(170, 80, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_wheelweight.setFont(font)
        self.spinBox_wheelweight.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_wheelweight.setObjectName("spinBox_wheelweight")
        self.spinBox_CG = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_CG.setGeometry(QtCore.QRect(170, 50, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_CG.setFont(font)
        self.spinBox_CG.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_CG.setObjectName("spinBox_CG")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 260, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(30, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.spinBox_wblength = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_wblength.setGeometry(QtCore.QRect(170, 20, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_wblength.setFont(font)
        self.spinBox_wblength.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_wblength.setObjectName("spinBox_wblength")
        self.spinBox_wishboneN = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_wishboneN.setGeometry(QtCore.QRect(170, 50, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_wishboneN.setFont(font)
        self.spinBox_wishboneN.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_wishboneN.setObjectName("spinBox_wishboneN")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(270, 260, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(30, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(40, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.spinBox_initXvel = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_initXvel.setGeometry(QtCore.QRect(180, 20, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_initXvel.setFont(font)
        self.spinBox_initXvel.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_initXvel.setObjectName("spinBox_initXvel")
        self.spinBox_initYvel = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_initYvel.setGeometry(QtCore.QRect(180, 50, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_initYvel.setFont(font)
        self.spinBox_initYvel.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_initYvel.setObjectName("spinBox_initYvel")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 350, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_solve = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_solve.setGeometry(QtCore.QRect(10, 20, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_solve.setFont(font)
        self.pushButton_solve.setObjectName("pushButton_solve")
        self.spinBox_sag = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_sag.setEnabled(False)
        self.spinBox_sag.setGeometry(QtCore.QRect(440, 20, 71, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_sag.setFont(font)
        self.spinBox_sag.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_sag.setObjectName("spinBox_sag")
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(250, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Ground Data"))
        self.pushButton_getdata.setText(_translate("Dialog", "Load Ground Coords"))
        self.label_9.setText(_translate("Dialog", "Track Length [m]"))
        self.label_11.setText(_translate("Dialog", "Filepath Chosen"))
        self.groupBox_2.setTitle(_translate("Dialog", "Suspension Data"))
        self.label_8.setText(_translate("Dialog", "Max Shock Displacement [m]"))
        self.label_6.setText(_translate("Dialog", "Tire Stiffness [N m]"))
        self.label_5.setText(_translate("Dialog", "Shock Springrate [N m]"))
        self.label_7.setText(_translate("Dialog", "Shock Damping Factor"))
        self.groupBox_3.setTitle(_translate("Dialog", "Vehicle Data"))
        self.label.setText(_translate("Dialog", "Body Weight [kg]"))
        self.label_2.setText(_translate("Dialog", "CG Location [m]"))
        self.label_3.setText(_translate("Dialog", "Wheel & Tire Weight [kg]"))
        self.label_4.setText(_translate("Dialog", "Tire Radius [m]"))
        self.groupBox_4.setTitle(_translate("Dialog", "Wishbone Data"))
        self.label_10.setText(_translate("Dialog", "Wishbone Length [m]"))
        self.label_12.setText(_translate("Dialog", "Number of Wishbones"))
        self.groupBox_5.setTitle(_translate("Dialog", "Initial Conditions"))
        self.label_13.setText(_translate("Dialog", "Velocity in the X [m/s]"))
        self.label_14.setText(_translate("Dialog", "Velocity in the Y [m/s]"))
        self.groupBox_6.setTitle(_translate("Dialog", "Calculated Data"))
        self.pushButton_solve.setText(_translate("Dialog", "Solve"))
        self.label_15.setText(_translate("Dialog", "Calculated Suspension Sag [m]"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

