# ------------------------------------------------------------#
# All functions having to do with the ground go in this file #
# ------------------------------------------------------------#
import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt
from VEHICLE import q_car

class Ground:
    def __init__(self):
        self.car = q_car()
        self.tracklength = None
        self.resolution = None
        self.xdata = []
        self.ydata = []

    def getdata(self, data):  # interpret the ground .txt and plot ground profile
        n = len(data)
        for lineN in data:
            self.xdata.append(lineN[0])
            self.ydata.append(lineN[1])
        self.tracklength = data[n - 1][0]
        self.resolution = self.xdata[1] - self.xdata[0]

    def graphtrack(self):
        plt.plot(self.xdata, self.ydata)
        plt.show()
        print('GROUND DATA PLOTTED SUCESSFULLY')

# Spline Function
# ---------------------------------------------------------
# arr = np.arange(np.amin(x), np.amax(x), 0.01)
# s = interpolate.CubicSpline(x, y)
#
# fig, ax = plt.subplots(1, 1)
# # ax.hold(True)
# ax.plot(x, y, 'bo', label='Data Point')
# ax.plot(arr, s(arr), 'k-', label='Cubic Spline', lw=1)
#
# for i in range(x.shape[0] - 1):
#     segment_x = np.linspace(x[i], x[i + 1], 100)
#     # A (4, 100) array, where the rows contain (x-x[i])**3, (x-x[i])**2 etc.
#     exp_x = (segment_x - x[i])[None, :] ** np.arange(4)[::-1, None]
#     # Sum over the rows of exp_x weighted by coefficients in the ith column of s.c
#     segment_y = s.c[:, i].dot(exp_x)
#     ax.plot(segment_x, segment_y, label='Segment {}'.format(i), ls='--', lw=3)
# # ax.legend()
# plt.show()
# ----------------------------------------------------------

def main():
    file = np.loadtxt('GroundDataExample1.txt', delimiter=',', skiprows=1, unpack=False)
    file = file.tolist()
    # print(file[0:3])
    Ground.getdata(file)

# main()  # uncomment to test this file only