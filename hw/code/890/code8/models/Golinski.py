from __future__ import division
__author__ = 'Venkatesh'

import random
import math
from code8.optimizers.decs import Decisions
from code8.models.model import Model

class Golinski(Model):
    decisons = []
    name = 'Golinski'
    def __init__(self):

        lo = [2.6,0.7,17.0,7.3,7.3,2.9,5.0]
        hi = [3.6,0.8,28.0,8.3,8.3,3.9,5.5]
        for i in range(7):
            self.decisons.append(Decisions(lo[i],hi[i]))

    def objs(self,can):
        obj1 = self.f1(can)
        obj2 = self.f2(can)
        return obj1,obj2

    def f2(self,can):

        x1 = can[0]
        x2 = can[1]
        x3 = can[2]
        x4 = can[3]
        x5 = can[4]
        x6 = can[5]
        x7 = can[6]

        return math.pow((math.pow(745*x4/(x2*x3),2) + (1.69*math.pow(10,7))),0.5)/(0.1*math.pow(x6,3))

    def f1(self,can):
        x1 = can[0]
        x2 = can[1]
        x3 = can[2]
        x4 = can[3]
        x5 = can[4]
        x6 = can[5]
        x7 = can[6]
        return 0.7854*x2*math.pow(x2,2)*((10*math.pow(x3,2)/3) + 14.933*x3 - 43.0934) \
               - 1.508*x1*(math.pow(x6,2) + math.pow(x7,2)) \
               + 7.477*(math.pow(x6,3) + math.pow(x7,3)) \
               + 0.7854*(x4*math.pow(x6,2) + x5*math.pow(x7,2))

    def checkconstraint(self,can):

        x1 = can[0]
        x2 = can[1]
        x3 = can[2]
        x4 = can[3]
        x5 = can[4]
        x6 = can[5]
        x7 = can[6]

        if not 1/(x1*math.pow(x2,2)*x3) - 1/27 <=0:
            return False
        '''
        print 1/(x1*math.pow(x2,2)*x3)
        print 1/397.5
        if not 1/(x1*math.pow(x2,2)*x3) - 1/397.5 <=0:
            print 2
            return False
        '''
        if not math.pow(x4,3)/(x2*math.pow(x3,2)*math.pow(x6,4)) - 1.0/1.93 <= 0:
            return False

        if not math.pow(x5,3)/(x2*x3*math.pow(x7,4)) - 1.0/1.93 <= 0:
            return False

        if not x2*x3 -40 <= 0:
            return False

        if not x1/x2 - 12 <= 0:
            return False

        if 5 - x1/x2 <= 0:
            return False

        if (1.9 - x4 + (1.5*x6)) <= 0:
            return False

        if 1.9 - x5 + 1.1*x7 <= 0:
            return False

        if not self.f2(can) <= 1300:
            return False

        a = 745*x5/(x2*x3)
        b = 1.575 * math.pow(10,8)

        if not math.pow(a**2+b,1/2)/(0.1*math.pow(x7,3)) <= 1100:
            return False

        return True
