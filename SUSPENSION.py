#+----------------------------------------------------------------#
# All functions having to do with the suspension go in this file #
#----------------------------------------------------------------#
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import VEHICLE

def solve_ODE(filename, m1, m2, c1, k1, k2):
    #Read file or pull folr from data
    file = np.loadtxt(filename, delimiter=',', skiprows=1, unpack=False)
    file = file.tolist()
    #Create empty arrays for x and y variables
    h = len(file)
    u = np.zeros(h)
    r = np.zeros(h)

    for i in range(h):
        u[i] = file[i][0]#x column
        r[i] = file[i][1]#y column
    #Establish t-space using length of file and total time from x column
    t = np.linspace(0, u[h-1], len(file))
    #Find polynomial fit
    z = np.polyfit(u, r, 20)


    def f(z, t):#Creating equation from polyfit to establish forcing function of the ground
        return (z[0] * t ** 20) + (z[1] * t ** 19) + (z[2] * t ** 18) + (z[3]* t ** 17) + (z[4] * t ** 16) + (z[5] * t ** 15) + (z[6] * t ** 14) + (z[7] * t ** 13) + (z[8] * t ** 12) + (z[9] * t**11) + (z[10]*t**10) + (z[11]*t**9) + (z[12]*t**8) + (z[13] * t**7) + (z[14] * t**6) + (z[15]*t**5) + (z[16]*t**4) + (z[17]*t**3) + (z[18] * t**2) + (z[19]*t) + z[20]

    def ode_system(X, t, m1, m2,c1,k1,k2):


        y = f(z, t) #forcing function of the ground

    #Establishing ODE equations
        x1 = X[0]; x1dot = X[1]; x2 = X[2]; x2dot = X[3]

        x1ddot = (1/m1) * (c1*(x2dot - x1dot) + k1*(x2 - x1))
        x2ddot = (1/m2) * (-c1*(x2dot - x1dot) - k1 * (x2 - x1) + k2* (y-x2))

        return [x1dot, x1ddot, x2dot, x2ddot]

    ic = [0,0,0,0] #Initial conditions of no velocity and no displacement from the no spring force position. BIG ASSUMPTION

    # m1 = 100   #establishing car parameters. Must pull from GUI instead of here
    # m2 = 10    #uncomment this part to run it without GUI, must comment our arguements up top as well and put in own filename
    # c1 = 2000
    # k1 = 1000
    # k2 = 5000

    x = odeint(ode_system, ic, t, args = (m1, m2,c1,k1,k2)) #Solving ODE using car parameters
    plt.title("Wheel")  #Plot the wheel
    plt.plot(t,x[:,0], 'b-', label = 'Wheel Position')
    plt.plot(t,x[:,1], 'g-', label = 'Wheel velocity')
    plt.show()
    plt.title("Body")  #Plot the body
    plt.plot(t,x[:,2], 'b-', label = 'Body Position')
    plt.plot(t,x[:,3], 'g-', label = 'Body velocity')
    plt.show()

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