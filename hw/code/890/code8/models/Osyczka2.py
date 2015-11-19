from __future__ import division
__author__ = 'Venkatesh'

import random
import sys
import math
from code8.optimizers.decs import Decisions

class Osyczka2:
    name = "Osyczka2"
    #decs = []
    decisons = []
    def __init__(self):

        lo = [0,0,1,0,1,0]
        hi = [10,10,5,6,5,10]
        for i in range((len(hi))):
            self.decisons.append(Decisions(lo[i],hi[i]))

    def getcandidate(self):
        can = []
        for dec in self.decisons:
            can.append(random.randrange(dec.lo,dec.hi))
        return can

    def generate(self):
        while True:
            can = self.getcandidate()
            if self.checkconstraint(can):
                return can

    def checkconstraint(self,can):
        if not can[0] + can[1] - 2 >= 0:
            return False

        if not 6 - can[0] - can[1] >= 0:
            return False

        if not 2 - can[1] + can[0] >= 0:
            return False

        if not 2 - can[0] + 3*can[1] >= 0:
            return False

        if not 4 - can[3] - (can[2] - 3)**2 >= 0:
            return False

        if not (can[4]-3)**3 + can[5] - 4 >= 0:
            return False

        return True

    def objs(self,can):
        f1 = -(25*(can[0]-2)**2 + (can[1] - 2)**2 + ((can[2]-1)**2)*((can[3]-4)**2) + (can[4]-1)**2 )
        f2 = sum([i**2 for i in can])
        return f1,f2

    def score(self,can):
        f1,f2 = self.objs(can)
        return f1+f2 if f1+f2 > 0 else 0

    def get_energy(self,can,norm):
        sc = self.score(can)
        norm[1] = norm[1] if norm[1] > sc else sc
        return norm,((sc-norm[0])/(norm[1] - norm[0]))

    def baseline_study(self):
        min_value = sys.maxint
        max_value = -sys.maxint - 1
        for i in range(1000):
            sn = self.generate()
            sc = self.score(sn)
            if sc < min_value:
                min_value = sc
            if sc > max_value:
                max_value = sc
        return [min_value, max_value]

    def prob(self,old, new, k):
        return math.exp((old-new)/k)