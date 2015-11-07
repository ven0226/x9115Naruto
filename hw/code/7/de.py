from __future__ import division
__author__ = 'Venkatesh'

import random
import math

class decs:
    hi = 0
    lo = 0
    def __init__(self,lo,hi):
        self.hi = hi
        self.lo = lo

class de:
    decisons = []
    def __init__(self):
        lo = [2.6,0.7,17.0,7.3,7.3,2.9,5.0]
        hi = [3.6,0.8,28.0,8.3,8.3,3.9,5.5]
        for i in range((len(hi))):
            self.decisons.append(decs(lo[i],hi[i]))

    def generate(self):
        while True:
            can = self.getcandidate(self.decs)
            if self.checkconstraint(can):
                return can

    def getcandidate(self):
        can = []
        for dec in self.decs:
            can.append(random.randrange(dec.lo,dec.hi))
        return can

    def f2(self,can):

        return math.pow(math.pow(745*can[3]/can[1]*can[2],2) + 1.69*math.pow(10,7),1/2)/0.1*math.pow(can[5],3)

    def f1(self,can):

        return 0.7854*can[1]*math.pow(can[1],2)*(10*math.pow(can[2],2)/3 + 14.933*can[2] - 43.0934) \
               - 1.508*can[0]*(math.pow(can[5],2) + math.pow(can[6],2)) \
               + 7.477*(math.pow(can[5],3) + math.pow(can[6],3)) \
               + 0.7854*(can[3]*math.pow(can[5],2) + can[4]*math.pow(can[6],2))

    def checkconstraint(self,can):
        if not 1/(can[0]*math.pow(can[1],2)*can[2]) - 1/27 <=0:
            return False

        if not math.pow(can[3],3)/can[1]*math.pow(can[2],2)*math.pow(can[5],4) - 1.0/1.93 <= 0:
            return False

        if not math.pow(can[4],3)/can[1]*can[2]*math.pow(can[6],4) - 1/1.93 <= 0:
            return False

        if not can[1]*can[2] -40 <= 0:
            return False

        if not can[0]/can[1] - 12 <= 0:
            return False

        if 5 - can[0]/can[1] <= 0:
            return False

        if 1.9 - can[3] + 1.5*can[5] <= 0:
            return False

        if 1.9 - can[4] + 1.1*can[6] <= 0:
            return False

        if not self.f2(can) <= 1300:
            return False

        a = 745*can[4]/can[1]*can[2]
        b = 1.575 * math.pow(10,8)

        if not math.pow(a**2+b,1/2)/0.1*math.pow(can[6],3) <= 1100:
            return False

        return True