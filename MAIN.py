import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
import numpy as np
from GUI import Ui_Dialog
from SUSPENSION import q_car_suspension
from VEHICLE import q_car
import GROUND

class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.suspension = q_car_suspension()
        self.car = q_car
        self.ui.setupUi(self)
        self.assign_widgets()
        self.defaultparams()
        self.show()

    def assign_widgets(self):
        self.ui.pushButton_exit.clicked.connect(app.exit())
        self.ui.pushButton_getdata.clicked.connect(self.loaddata)
        self.ui.pushButton_clear.clicked.connect(self.Clear)
        self.ui.pushButton_graphtrack.clicked.connect(GROUND.graphtrack)

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
            GROUND.getdata(data)
            print('DATA PROCESSED SUCESSFULLY')
            self.ui.doubleSpinBox_tracklength.setValue(GROUND.tracklength)
            self.ui.doubleSpinBox_resolution.setValue(GROUND.resolution)

            # self.suspension.bodyweight = self.ui.doubleSpinBox_bodyweight.value()
            # self.suspension.odesolve()
            # print('SUSPENSION DATA PROCESSED SUCESSFULLY')
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

    # def Exit(self): app.exit()

    # def Solve(self):

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

main_win = main_window()

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
