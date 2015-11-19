from __future__ import division
__author__ = 'Venkatesh'

import random
import sys
import math
from code8.optimizers.decs import Decisions

class Kursawe():
    name = "Kursawe"
    #decs = []
    decisons = []
    def __init__(self):

        lo = [-5,-5,-5]
        hi = [5,5,5]
        for i in range((len(hi))):
            self.decisons.append(Decisions(lo[i],hi[i]))

    def objs(self,can = []):
        f1 = 0
        f2 = 0
        for x in range(len(can)-1):
            f1 += ( -10*math.exp(-0.2*math.sqrt( math.pow( can[x], 2) + math.pow( can[x+1], 2))))
            f2 += ( math.pow( abs(can[x]), 0.8 ) + 5 * math.sin(math.pow( can[x], 1)))
        return f1,f2

    def score(self,can):
        f1,f2 = self.objs(can)
        return f1+f2

    def get_energy(self,can,norm):
        sc = self.score(can)
        norm[1] = norm[1] if norm[1] > sc else sc
        return norm,((sc-norm[0])/(norm[1] - norm[0]))

    def generate(self):
        can = []
        for dec in self.decisons:
            can.append(random.randrange(dec.lo,dec.hi))
        return can

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

    def checkconstraint(self,can):
        return True