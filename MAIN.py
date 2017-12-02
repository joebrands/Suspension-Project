import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
import numpy as np
from GUI import Ui_Dialog
from SUSPENSION import q_car_suspension
from VEHICLE import q_car
from GROUND import Ground

class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.suspension = q_car_suspension()
        self.car = q_car()
        self.ground = Ground()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.defaultparams()
        self.show()

    def assign_widgets(self):
        self.ui.pushButton_exit.clicked.connect(self.Exit)
        self.ui.pushButton_getdata.clicked.connect(self.loaddata)
        self.ui.pushButton_clear.clicked.connect(self.Clear)
        self.ui.pushButton_solve.clicked.connect(self.Solve)
        self.ui.pushButton_graphtrack.clicked.connect(self.ground.graphtrack)

    def loaddata(self):
        filename = QFileDialog.getOpenFileName(self)[0]

        if len(filename) == 0:
            no_file()
            return
        self.ui.textEdit_filepath.setText(filename)

        file = np.loadtxt(filename, delimiter=',', skiprows=1, unpack=False)
        file = file.tolist()
        data = file

        try:
            self.ground.getdata(data)
            self.ui.doubleSpinBox_tracklength.setValue(self.ground.tracklength)
            self.ui.doubleSpinBox_resolution.setValue(self.ground.resolution)
            self.car.tracklength = self.ground.tracklength
            self.car.resolution = self.ground.resolution
            self.car.xdata = self.ground.xdata
            self.car.ydata = self.ground.ydata
            print('DATA PROCESSED SUCESSFULLY')

        except:
            bad_file()

    def defaultparams(self):
        self.ui.doubleSpinBox_bodyweight.setValue(100)
        self.ui.doubleSpinBox_CG.setValue(0)
        self.ui.doubleSpinBox_wheelweight.setValue(10)
        self.ui.doubleSpinBox_tireradius.setValue(0.5)

        self.ui.doubleSpinBox_shockdisp.setValue(0.3)
        self.ui.doubleSpinBox_shockspring.setValue(100)
        self.ui.doubleSpinBox_tirespring.setValue(500)
        self.ui.spinBox_dampingfac.setValue(1)

        self.ui.doubleSpinBox_wblength.setValue(1)
        self.ui.spinBox_wishboneN.setValue(2)

        self.ui.doubleSpinBox_initYvel.setValue(0)
        self.ui.doubleSpinBox_initXvel.setValue(5)

    def Exit(self):
        app.exit()

    def Solve(self):
        self.car.bodyweight = self.ui.doubleSpinBox_bodyweight.value()
        self.car.CG = self.ui.doubleSpinBox_CG.value()
        self.car.wheelweight = self.ui.doubleSpinBox_wheelweight.value()
        self.car.tireradius = self.ui.doubleSpinBox_tireradius.value()
        self.car.wblength = self.ui.doubleSpinBox_wblength.value()
        self.car.wishboneN = self.ui.spinBox_wishboneN.value()
        self.car.shockdisp = self.ui.doubleSpinBox_shockdisp.value()
        self.car.shockspring = self.ui.doubleSpinBox_shockspring.value()
        self.car.tirespring = self.ui.doubleSpinBox_tirespring.value()
        self.car.dampingfac = self.ui.spinBox_dampingfac.value()
        self.car.initXvel = self.ui.doubleSpinBox_initXvel.value()
        self.car.initYvel = self.ui.doubleSpinBox_initYvel.value()
        print(self.car.xdata)
        print(self.car.initXvel)
        self.suspension.odesolve()
        print('SUSPENSION DATA PROCESSED SUCESSFULLY')

    def Clear(self):
        self.ui.doubleSpinBox_resolution.clear()
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
    msg.setText('An error occurred while processing your file.')
    msg.setWindowTitle('Process Error')
    retval = msg.exec_()
    return None

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())
