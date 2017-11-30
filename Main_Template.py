import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from GUI import Ui_Dialog

class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.Clear()
        self.show()

    def assign_widgets(self):
        # self.ui.pushButton_exit.clicked.connect(self.Exit)
        # self.ui.pushButton_solve.clicked.connect(self.Solve)
        # self.ui.pushButton_clear.clicked.connect(self.Clear)

    def Exit(self):
        app.exit()

    def Solve(self):

    def Clear(self):

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())