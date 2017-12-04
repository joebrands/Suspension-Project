#-------------------------------------------------------------#
# All functions having to do with the vehicle go in this file #
#-------------------------------------------------------------#

class q_car:
    def __init__(self):
        self.bodyweight = None
        self.CG = None
        self.wheelweight = None
        self.tireradius = None
        self.wblength = None
        self.wishboneN = None
        self.shockdisp = None
        self.shockspring = None
        self.tirespring = None
        self.dampingfac = None
        self.initXvel = None
        self.initYvel = None
        self.sag = None
        self.tracklength = None
        self.resolution = None
        self.xdata = []
        self.ydata = []
        self.wheelpos = []
        self.wheelvel = []
        self.bodypos = []
        self.bodyvel = []
        self.file = []

    def printtest(self):
        print(self.bodyweight)
        print(self.shockdisp)
        print(self.xdata)