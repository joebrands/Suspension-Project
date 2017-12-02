#----------------------------------------------------------------#
# All functions having to do with the suspension go in this file #
#----------------------------------------------------------------#
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from VEHICLE import q_car

class q_car_suspension:
    def __init__(self):
        self.car = q_car()

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

    def odesolve(self):
        l = len(self.car.xdata)
        print(self.car.xdata)
        print(self.car.initXvel)
        for n in range(l):
            t = [self.car.xdata[n]*self.car.resolution]
            ic = [0,0,0,0]

            yNow = self.car.ydata[n]
            yLast = self.car.ydata[n-1]
            carparams = [self.car.bodyweight, self.car.wheelweight, self.car.dampingfac, self.car.shockspring, self.car.tirespring]
            groundparams = [yNow]

            x = odeint(self.odefunc, ic, t, args = (carparams, groundparams))

        tTotal = l/self.car.initXvel
        tLen = np.linspace(0, tTotal, 100)
        plt.plot(tLen, x[:,0])
        print('ODESOLVE RUN SUCESSFUL')

def main():
    q_car_suspension.odesolve()
# main()  # uncomment to test this file