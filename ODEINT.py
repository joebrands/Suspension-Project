import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t, y = np.loadtxt("GroundDataExample4.txt", delimiter=',', skiprows=1, unpack=True)

def plotfile(t, y):
    # file = file.tolist()
    n = len(t)
    print('Number of Points is', n)
    plt.plot(t, y)
    plt.show()

def slopecalc(t1, t2, y1, y2):
    slope = (y2 - y1) / (t2 - t1)
    return slope

# def pw(t1, t2, y1, y2):
#     ymag = []
#     ymag.append(slopecalc(t1, t2, y1, y2))
#     # print(ymag)
#     return ymag

# piecewise(t, y)

def ode(t, y):
    # print(len(t))
    xperm = [[0, 0, 0, 0]]
    for i in range(len(t) - 1):
        def ode_system(X, tODE, carparams):
            t, y = np.loadtxt("GroundDataExample4.txt", delimiter=',', skiprows=1, unpack=True)
            m1 = carparams[0]
            m2 = carparams[1]
            c1 = carparams[2]
            k1 = carparams[3]
            k2 = carparams[4]

            print(slopecalc(t[i], t[i + 1], y[i], y[i + 1]), i, tODE)
            y = slopecalc(t[i], t[i + 1], y[i], y[i + 1]) * tODE

            x1 = X[0]
            x1dot = X[1]
            x2 = X[2]
            x2dot = X[3]

            x1ddot = (1 / m1) * (c1 * (x2dot - x1dot) + k1 * (x2 - x1))
            x2ddot = (1 / m2) * (-c1 * (x2dot - x1dot) - k1 * (x2 - x1) + k2 * (y - x2))

            return [x1dot, x1ddot, x2dot, x2ddot]

        tODE = t[i]
        # tODE = np.linspace(0, len(t) - 1, len(t))
        # print(tODE)
        print(xperm[0][3])
        if i == 0:
            ic = [xperm[i][0], xperm[i][1], xperm[i][2], xperm[i][3]]
        else:
            ic = [xperm[i - 1][0], xperm[i - 1][1], xperm[i - 1][2], xperm[i - 1][3]]

        m1 = 1
        m2 = 1
        c1 = 2
        k1 = 1
        k2 = 4
        carparams = [m1, m2, c1, k1, k2]
        x = odeint(ode_system, ic, tODE, args=(carparams,))
        xperm.extend(x)
        print(xperm)

    print(xperm[1][])
    # plt.plot(t, xperm[0], 'b-', label='Body Position')
    # #plt.plot(t, xperm[:, 1], 'g-', label='Body velocity')
    # plt.show()
    # # plt.plot(t, x[:, 2], 'b-', label='Wheel Position')
    # # plt.plot(t, x[:, 3], 'g-', label='Wheel velocity')
    # # plt.show()

ode(t, y)
