#+----------------------------------------------------------------#
# All functions having to do with the suspension go in this file #
#----------------------------------------------------------------#
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class q_car_suspension():
    def __init__(self):
        self.bodyweight = None


#---------------------------------------------------------------
    # def odefunc(self, disp, t, carparams, groundparams):
    #     bodyweight = carparams[0]
    #     wheelweight = carparams[1]
    #     dampingfac = carparams[2]
    #     shockspring = carparams[3]
    #     tirespring = carparams[4]
    #
    #     yNow = groundparams[0]
    #
    #     x1, x1dot, x2, x2dot = [disp[0], disp[1], disp[2], disp[3]]
    #
    #     x1ddot = (dampingfac*(x2dot - x1dot) + shockspring*(x2 - x1))
    #     # x2ddot =
# ---------------------------------------------------------------

    def odesolve(self):
        # t = 1
        # ic = []

        # self.bodyweight = 100
        # wheelweight = 10
        # dampingfac = 1
        # shockspring = 100
        # tirespring = 500
        # yNow = 1
        # yLast = 0
        # carparams = [bodyweight, wheelweight, dampingfac, shockspring, tirespring]
        # groundparams = [yNow]
        #
        # # x = odeint()
        print('ODESOLVE IS RUN')
        print(self.bodyweight)

def main():
    q_car_suspension.odesolve()
# main()  # uncomment to test this file