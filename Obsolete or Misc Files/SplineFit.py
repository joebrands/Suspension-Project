import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt


# x = np.array([1, 2, 4, 5])  # sort data points by increasing x value
# y = np.array([2, 1, 4, 3])a

x, y = np.loadtxt('GroundDataExample1.txt', skiprows = 1, unpack = True)

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
