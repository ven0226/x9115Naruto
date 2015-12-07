from __future__ import division
__author__ = 'Venkatesh'

from optimizers.decs import Decisions
from models.model import Model

class Osyczka2(Model):
    name = "Osyczka2"
    decisons = []
    def __init__(self):

        lo = [0,0,1,0,1,0]
        hi = [10,10,5,6,5,10]
        for i in range(6):
            self.decisons.append(Decisions(lo[i],hi[i]))

    def checkconstraint(self,can):
        #print "Entering contraint"
        x1 = can[0]
        x2 = can[1]
        x3 = can[2]
        x4 = can[3]
        x5 = can[4]
        x6 = can[5]
        if not (can[0] + can[1] - 2 >= 0):
            #print 1
            return False

        if not (6 - can[0] - can[1] >= 0):
            #print 2
            return False

        if not (2 - can[1] + can[0] >= 0):
            #print 3
            return False

        if not 2 - can[0] + 3*can[1] >= 0:
            #print 4
            return False

        if not 4 - can[3] - (can[2] - 3)**2 >= 0:
            #print 5
            return False

        if not (can[4]-3)**3 + can[5] - 4 >= 0:
            #print 6
            return False

        #print ">>>> True contraint"
        return True

    def objs(self,can):
        f1 = -(25*(can[0]-2)**2 + (can[1] - 2)**2 + ((can[2]-1)**2)*((can[3]-4)**2) + (can[4]-1)**2 )
        f2 = sum([i**2 for i in can])
        return f1,f2