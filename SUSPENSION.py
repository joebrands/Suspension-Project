#----------------------------------------------------------------#
# All functions having to do with the suspension go in this file #
#----------------------------------------------------------------#
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from MAIN import *

def odefunc(disp, t, carparams, groundparams):
    bodyweight = carparams[0]
    wheelweight = carparams[1]
    dampingfac = carparams[2]
    shockspring = carparams[3]
    tirespring = carparams[4]

    yNow = groundparams[0]

    x1, x1dot, x2, x2dot = [disp[0], disp[1], disp[2], disp[3]]

    x1ddot = (dampingfac*(x2dot - x1dot) + shockspring*(x2 - x1))
    x2ddot =

def odesolve():
    t = 1
    ic = []

    # bodyweight = getattr(main_window, 'bodyweight')
    # print(bodyweight)

    bodyweight = 100
    wheelweight = 10
    dampingfac = 1
    shockspring = 100
    tirespring = 500
    yNow = 1
    yLast = 0
    carparams = [bodyweight, wheelweight, dampingfac, shockspring, tirespring]
    groundparams = [yNow]

    x = odeint()

def main():
    odedata()
main()  # uncomment to test this file