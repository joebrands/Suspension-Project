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
    
    # Polynomial Fit
    # -------------------------------------------------------------------
    def polyfitgraph(self):
        n = len(self.xdata)
        print('Number of points in file:', n)
        x = np.zeros(n)
        y = np.zeros(n)
        
        for i in range(n):
            x[i] = self.xdata[0]
            y[i] = self.ydata[1]
        y = np.zeros(n)
        t = np.linspace(0, x[n - 1], n)
        z = np.polyfit(x, y, 20)
        
        def f(x, y):
            return (z[0] * t**20) + (z[1] * t**19) + (z[2] * t**18) + (z[3] * t**17) + (z[4] * t**16) + (z[5] * t**15) + (z[6] * t**14) + (z[7] * t**13) + (
                z[8] * t**12) + (z[9] * t**11) + (z[10] * t**10) + (z[11] * t**9) + (z[12] * t**8) + (z[13] * t**7) + (z[14] * t**6) + (z[15] * t**5) + (
                       z[16] * t**4) + (z[17] * t**3) + (z[18] * t**2) + (z[19] * t) + z[20]
        
        for i in range(len(t)):
            y[i] = (f(t[i], z))
        
        # print(z)
        plt.plot(t, y)
        plt.show()

# --------------------------------------------------------------------

def main():
    file = np.loadtxt('GroundDataExample1.txt', delimiter = ',', skiprows = 1, unpack = False)
    file = file.tolist()
    # print(file[0:3])
    Ground.getdata(file)
    
    # main()  # uncomment to test this file only
