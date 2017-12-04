import numpy as np
import matplotlib.pyplot as plt



file = np.loadtxt("GroundDataExample3.txt", delimiter=',', skiprows=1, unpack=False)
file = file.tolist()
h = len(file)
u = np.zeros(h)
r = np.zeros(h)

#print(file)
for i in range(h):
    u[i] = file[i][0]
    r[i] = file[i][1]
#print(u)
#print(r)
y = np.zeros(h)
t = np.linspace(0, u[h-1], len(file))

z = np.polyfit(u, r, 20)


def f(z, t):
    # return (z[0] * t ** 4) + (z[1] * t ** 3) + (z[2] * t ** 2) + (z[3] * t) + z[4]
    # return (z[0] * t ** 6) + (z[1] * t ** 5) + (z[2] * t ** 4) + (z[3] * t ** 3) + (z[4] * t ** 2) + (z[5] * t) + z[6]
    return (z[0] * t ** 20) + (z[1] * t ** 19) + (z[2] * t ** 18) + (z[3]* t ** 17) + (z[4] * t ** 16) + (z[5] * t ** 15) + (z[6] * t ** 14) + (z[7] * t ** 13) + (z[8] * t ** 12) + (z[9] * t**11) + (z[10]*t**10) + (z[11]*t**9) + (z[12]*t**8) + (z[13] * t**7) + (z[14] * t**6) + (z[15]*t**5) + (z[16]*t**4) + (z[17]*t**3) + (z[18] * t**2) + (z[19]*t) + z[20]


for i in range(len(t)):
    y[i] = (f(z, t[i]))
# print(t)
# for i in range(h):
#     if r[i] == 0:
#         y[i] = 0
#     elif r[i] == r[i-1] and r[i] != 0:
#         y[i] = r[i]


print(z)
plt.plot(t,y)
plt.show()
#print(z)
