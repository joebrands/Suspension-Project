#------------------------------------------------------------#
# All functions having to do with the ground go in this file #
#------------------------------------------------------------#
import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt

def getdata(data): # interpret the ground .txt and plot ground profile
    # x, y = np.loadtxt('GroundDataExample1.txt', skiprows=1, unpack=True)
    for lineN in data:
        line = lineN.strip().split()

        x = line[0]
        y=line[1]

        arr = np.arange(np.amin(x), np.amax(x), 0.01)
        s = interpolate.CubicSpline(x, y)

        fig, ax = plt.subplots(1, 1)
        # ax.hold(True)
        ax.plot(x, y, 'bo', label='Data Point')
        ax.plot(arr, s(arr), 'k-', label='Cubic Spline', lw=1)

        for i in range(x.shape[0] - 1):
            segment_x = np.linspace(x[i], x[i + 1], 100)
            # A (4, 100) array, where the rows contain (x-x[i])**3, (x-x[i])**2 etc.
            exp_x = (segment_x - x[i])[None, :] ** np.arange(4)[::-1, None]
            # Sum over the rows of exp_x weighted by coefficients in the ith column of s.c
            segment_y = s.c[:, i].dot(exp_x)
            ax.plot(segment_x, segment_y, label='Segment {}'.format(i), ls='--', lw=3)

        # ax.legend()
        plt.show()

getdata()