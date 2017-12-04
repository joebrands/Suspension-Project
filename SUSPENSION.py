#+----------------------------------------------------------------#
# All functions having to do with the suspension go in this file #
#----------------------------------------------------------------#
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import VEHICLE

class q_car_suspension:
    def __init__(self):
         self.wheeldisp = []

    def odefunc(self, disp, t, carparams, groundparams):
        bodyweight = carparams[0]
        wheelweight = carparams[1]
        dampingfac = carparams[2]
        shockspring = carparams[3]
        tirespring = carparams[4]

        yNow = groundparams[0]

        x1, x1dot, x2, x2dot = [disp[0], disp[1], disp[2], disp[3]]

        x1ddot = (dampingfac*(x2dot - x1dot) + shockspring*(x2 - x1)) / bodyweight
        x2ddot = (-dampingfac*(x2dot - x1dot) - shockspring*(x2 - x1) + tirespring*(yNow - x2)) / bodyweight
        return [x1dot, x1ddot, x2dot, x2ddot]

    def odesolve(self):
        l = len(VEHICLE.q_car.xdata)
        for n in range(l):
            t = [VEHICLE.q_car.xdata[n]*VEHICLE.q_car.resolution]
            ic = [1,1,1,1]

            yNow = VEHICLE.q_car.ydata[n]
            yLast = VEHICLE.q_car.ydata[n-1]
            carparams = [VEHICLE.q_car.bodyweight, VEHICLE.q_car.wheelweight, VEHICLE.q_car.dampingfac, VEHICLE.q_car.shockspring, VEHICLE.q_car.tirespring]
            groundparams = [yNow]

            x = odeint(self.odefunc, ic, t, args = (carparams, groundparams))
            self.wheeldisp.append(x[0][0])

        tTotal = l/VEHICLE.q_car.initXvel
        tLen = VEHICLE.q_car.xdata
        plt.plot(tLen, self.wheeldisp)
        plt.show()
        print('ODESOLVE RUN SUCESSFUL')

# SOLVING WITH JUST ONE POINT
# ---------------------------------------------------------------------
def odefunctest(disp, t, carparamstest, groundparamstest):
    bodyweight = carparamstest[0]
    wheelweight = carparamstest[1]
    dampingfac = carparamstest[2]
    shockspring = carparamstest[3]
    tirespring = carparamstest[4]

    yNow = groundparamstest[0]

    x1, x1dot, x2, x2dot = [disp[0], disp[1], disp[2], disp[3]]

    x1ddot = (dampingfac*(x2dot - x1dot) + shockspring*(x2 - x1)) / bodyweight
    x2ddot = (-dampingfac*(x2dot - x1dot) - shockspring*(x2 - x1) + tirespring*(yNow - x2)) / bodyweight
    return [x1dot, x1ddot, x2dot, x2ddot]

def odesolvetest():
    l = 20 # [points]
    initXvel = 5 # [m/s]
    tTotal = l/initXvel
    t = np.linspace(0, 20, 4)  # [sec] into the sim
    ic = [1,.2,0,0]

    yNow = np.sin(2*t) # [m]
    carparamstest = [100, 10, 1, -100, -500]
    groundparamstest = yNow  # [m] yNow

    x = odeint(odefunctest, ic, t, args = (carparamstest, groundparamstest))
    wheeldisp = x[0]

    plt.plot(t, wheeldisp)
    plt.show()
    print('Wheel Disp. is ', wheeldisp)
    print('ODESOLVE RUN SUCESSFUL')
#---------------------------------------------------------------------

def main():
    odesolvetest()
# main()  # uncomment to test this file