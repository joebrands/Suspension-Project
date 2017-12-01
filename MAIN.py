import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
import numpy as np

from GUI import Ui_Dialog
import GROUND

class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.Clear()
        self.show()

    def assign_widgets(self):
        self.ui.pushButton_exit.clicked.connect(self.Exit)
        self.ui.pushButton_getdata.clicked.connect(self.loaddata)
        self.ui.pushButton_clear.clicked.connect(self.Clear)

    def loaddata(self):
        filename = QFileDialog.getOpenFileName(self)[0]

        if len(filename) == 0:
            no_file()
            return
        self.ui.textEdit_filepath.setText(filename)

        file = np.loadtxt(filename, delimiter=',', skiprows=1, unpack=False)
        file = file.tolist()
        print(file[0:3])
        data = file
        # file = open(filename, 'r')
        # data = file.readlines()
        # file.close()

        try:
            GROUND.getdata(data)
            print('DATA PROCESSED SUCESSFULLY')
        except:
            bad_file()

    def Exit(self):
        app.exit()

    # def Solve(self):

    def Clear(self):
        self.ui.doubleSpinBox_tracklength.clear()
        self.ui.textEdit_filepath.clear()
        self.ui.doubleSpinBox_bodyweight.clear()
        self.ui.doubleSpinBox_CG.clear()
        self.ui.doubleSpinBox_wheelweight.clear()
        self.ui.doubleSpinBox_tireradius.clear()
        self.ui.doubleSpinBox_wblength.clear()
        self.ui.doubleSpinBox_initYvel.clear()
        self.ui.doubleSpinBox_initXvel.clear()
        self.ui.doubleSpinBox_shockdisp.clear()
        self.ui.doubleSpinBox_shockspring.clear()
        self.ui.doubleSpinBox_tirespring.clear()
        self.ui.doubleSpinBox_sag.clear()

def no_file():
    msg = QMessageBox()
    msg.setText('No file selected')
    msg.setWindowTitle('No File')
    retval = msg.exec_()
    return None

def bad_file():
    msg = QMessageBox()
    msg.setText('Unable to process selected file')
    msg.setWindowTitle('Bad File')
    retval = msg.exec_()
    return None

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())

class q_car:
    def __init__(self):
        self.bodyweight = None
        self.CG = None
        self.wheelweight = None
        self.tireradius = None
        self.wblength = None
        self.wishboneN = 1
        self.shockdisp = None
        self.shockspring = None
        self.tirespring = None
        self.dampingfac = 0
        self.initXvel = None
        self.initYvel = 0
        self.sag = None
        self.tracklength = 0
        self.xdata = []
        self.ydata = []

car = q_car()

