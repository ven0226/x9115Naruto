from __future__ import division
__author__ = 'Venkatesh'

import random
import math
import sys
from code8.optimizers.decs import Decisions

class Schaffer():
    name = "Shaffer"
    #decs = []
    decisons = []

    def __init__(self):
        lo = [-math.pow(10,5)]
        hi = [math.pow(10,5)]
        decs = Decisions(lo[0],hi[0])
        self.decisons.append(decs)

    def score(self,x):
        #print x
        f1,f2 = self.objs(x)
        return f1 + f2

    def objs(self,x):
        #print x
        f1 = (x[0]*x[0])
        f2 = (x[0]-2)**2
        return f1,f2

    def baseline_study(self):
        f1f2sum = []
        for i in range(100):
            x = []
            x.append(random.random())
            f1f2sum.append(self.score(x))
        return [min(f1f2sum), max(f1f2sum)]

    def get_energy(self,x,norm):
        #print x,"in get energy"
        return norm,(self.score(x)-norm[0])/(norm[1]-norm[0])

    def prob(self,old, new, k):
        return math.exp((old-new)/k)

    def generate(self):
        can = []
        can.append(random.random())
        return can

    def checkconstraint(self,can):
        return True