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
        self.wishboneN = 1
        self.shockdisp = None
        self.shockspring = None
        self.tirespring = None
        self.dampingfac = 0
        self.initXvel = None
        self.initYvel = 0
        self.sag = None
        self.tracklength = 0
        self.xdata = []
        self.ydata = []
        self.wheeldisp = []
        self.wheelpos = []
        self.wheelvel = []