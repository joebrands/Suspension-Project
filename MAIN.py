import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
import numpy as np
from GUI import Ui_Dialog
import VEHICLE
from GROUND import Ground
import SUSPENSION

class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ground = Ground()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.filename = None
        self.datafreq = None
        self.solverun = False
        self.defaultparams()
        self.ui.doubleSpinBox_datafreq.clear()
        self.show()
        self.ui.textEdit_output.append('INITIALIZING...')

    def assign_widgets(self):
        self.ui.pushButton_exit.clicked.connect(self.Exit)
        self.ui.pushButton_getdata.clicked.connect(self.loaddata)
        self.ui.pushButton_clear.clicked.connect(self.Clear)
        self.ui.pushButton_solve.clicked.connect(self.Solve)
        self.ui.pushButton_graphtrack.clicked.connect(self.graphtrack)
        self.ui.pushButton_optimizespring.clicked.connect(self.optimizespring)
    
    def datafreqcalc(self):
        deltaT = self.ground.tracklength / self.ui.doubleSpinBox_initXvel.value()
        self.datafreq = len(VEHICLE.q_car.xdata) / deltaT
        self.ui.doubleSpinBox_datafreq.setValue(self.datafreq)
    
    def loaddata(self):
        self.filename = QFileDialog.getOpenFileName(self)[0]

        if len(self.filename) == 0:
            no_file()
            return
        self.ui.textEdit_filepath.setText(self.filename)

        file = np.loadtxt(self.filename, delimiter=',', skiprows=1, unpack=False)
        file = file.tolist()
        self.data = file
        VEHICLE.q_car.file = self.data
        self.ui.textEdit_output.append('FILE READING...')

        try:
            self.ground.getdata(self.data)
            self.ui.doubleSpinBox_tracklength.setValue(self.ground.tracklength)
            self.ui.doubleSpinBox_resolution.setValue(self.ground.resolution)
            VEHICLE.q_car.tracklength = self.ground.tracklength
            VEHICLE.q_car.resolution = self.ground.resolution
            VEHICLE.q_car.xdata = self.ground.xdata
            VEHICLE.q_car.ydata = self.ground.ydata
            self.ui.spinBox_dataN.setValue(len(VEHICLE.q_car.xdata))
            self.datafreqcalc()
            self.ui.textEdit_output.append('DATA PROCESSED SUCESSFULLY')

        except:
            bad_file()
            self.ui.textEdit_output.append('ERROR: BAD DATA FILE')
            
    def graphtrack(self):
        if self.filename is None:
            no_file()
            self.ui.textEdit_output.append('WARNING: NO DATA FILE GIVEN')
        else: self.ground.polyfitgraph()

    def defaultparams(self):
        self.ui.doubleSpinBox_bodyweight.setValue(100)
        self.ui.doubleSpinBox_CG.setValue(0)
        self.ui.doubleSpinBox_wheelweight.setValue(10)
        self.ui.doubleSpinBox_tireradius.setValue(0.1)

        self.ui.doubleSpinBox_shockdisp.setValue(1)
        self.ui.doubleSpinBox_shockspring.setValue(2000)
        self.ui.doubleSpinBox_tirespring.setValue(5000)
        self.ui.spinBox_dampingfac.setValue(2)

        self.ui.doubleSpinBox_wblength.setValue(1)
        self.ui.spinBox_wishboneN.setValue(2)

        self.ui.doubleSpinBox_initYvel.setValue(0)
        self.ui.doubleSpinBox_initXvel.setValue(5)

    def Exit(self):
        app.exit()

    def Solve(self):
        if self.filename is None:
            no_file()
            self.ui.textEdit_output.append('WARNING: NO DATA FILE GIVEN')
            return
        VEHICLE.q_car.bodyweight = self.ui.doubleSpinBox_bodyweight.value()
        VEHICLE.q_car.CG = self.ui.doubleSpinBox_CG.value()
        VEHICLE.q_car.wheelweight = self.ui.doubleSpinBox_wheelweight.value()
        VEHICLE.q_car.tireradius = self.ui.doubleSpinBox_tireradius.value()
        VEHICLE.q_car.wblength = self.ui.doubleSpinBox_wblength.value()
        VEHICLE.q_car.wishboneN = self.ui.spinBox_wishboneN.value()
        VEHICLE.q_car.shockdisp = self.ui.doubleSpinBox_shockdisp.value()
        VEHICLE.q_car.shockspring = self.ui.doubleSpinBox_shockspring.value()
        VEHICLE.q_car.tirespring = self.ui.doubleSpinBox_tirespring.value()
        VEHICLE.q_car.dampingfac = self.ui.spinBox_dampingfac.value()
        VEHICLE.q_car.initXvel = self.ui.doubleSpinBox_initXvel.value()
        VEHICLE.q_car.initYvel = self.ui.doubleSpinBox_initYvel.value()
        SUSPENSION.solvesag()
        self.ui.doubleSpinBox_sag.setValue(VEHICLE.q_car.shockSagPercent)
        self.ui.doubleSpinBox_maxsag.setValue(VEHICLE.q_car.sag)
        self.ui.textEdit_output.append('SUSPENSION SAG SOLVED SUCESSFULLY')
        SUSPENSION.ODEsolve()
        self.ui.textEdit_output.append('ODESOLVE RUN SUCESSFUL')
        self.ui.textEdit_output.append('GRAPHING...')
        self.ui.textEdit_output.append('SUSPENSION DATA PROCESSED SUCESSFULLY')
        self.solverun = True
    
    def optimizespring(self):
        if self.solverun is True:
            self.ui.doubleSpinBox_shockspringoptimized.setValue(SUSPENSION.optimizesag())
            self.ui.textEdit_output.append('SHOCK SPRINGRATE OPTIMIZED SUCESSFULLY')
        else:
            solve_not_run()
            self.ui.textEdit_output.append('ERROR: SOLVE NOT RUN YET')
            return
        
    def Clear(self):
        self.ui.doubleSpinBox_resolution.clear()
        self.ui.spinBox_wishboneN.clear()
        self.ui.spinBox_dataN.clear()
        self.ui.doubleSpinBox_datafreq.clear()
        self.ui.doubleSpinBox_shockspringoptimized.clear()
        self.ui.doubleSpinBox_maxsag.clear()
        self.ui.spinBox_dampingfac.clear()
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
        self.ui.textEdit_output.append('DATA CLEARED SUCESSFULLY')

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

def solve_not_run():
    msg = QMessageBox()
    msg.setText('Solve has not been run yet.')
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
