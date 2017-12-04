import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

file = np.loadtxt("GroundDataExample3.txt", delimiter=',', skiprows=1, unpack=False)
file = file.tolist()
h = len(file)
r = np.zeros(h)
print(file)
for i in range(h):
    r[i] = file[i][1]
print(r)
x = []

def ode_system(X, t, carparams, roadparams):
    m1 = carparams[0];
    m2 = carparams[1];
    c1 = carparams[2];
    k1 = carparams[3];
    k2 = carparams[4];

    ymag = roadparams[0];

    if t < np.pi / 2:
        y = ymag * np.sin(2 * t)
    else:
        y = 0

    x1 = X[0];
    x1dot = X[1];
    x2 = X[2];
    x2dot = X[3]

    x1ddot = (1 / m1) * (c1 * (x2dot - x1dot) + k1 * (x2 - x1))
    x2ddot = (1 / m2) * (-c1 * (x2dot - x1dot) - k1 * (x2 - x1) + k2 * (y - x2))

    return [x1dot, x1ddot, x2dot, x2ddot]

t = np.linspace(0, 20, 200)
ic = [0, 0, 0, 0]

m1 = 1
m2 = 1
c1 = 2
k1 = 1
k2 = 4
ymag = 1
carparams = [m1, m2, c1, k1, k2]
roadparams = [ymag]
# roadparams = r
print(roadparams)
x = odeint(ode_system, ic, t, args=(carparams, roadparams))

plt.plot(t, x[:, 0], 'b-', label='Body Position')
plt.plot(t, x[:, 1], 'g-', label='Body velocity')
plt.show()
plt.plot(t, x[:, 2], 'b-', label='Wheel Position')
plt.plot(t, x[:, 3], 'g-', label='Wheel velocity')
plt.show()
