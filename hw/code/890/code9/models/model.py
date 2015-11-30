from __future__ import division
__author__ = 'Venkatesh'

import random
import sys
import math

class Model:
    decisons = []
    def getcandidate(self):
        can = []
        for dec in self.decisons:
            can.append(random.uniform(dec.lo,dec.hi))
        return can

    def generate(self):
        while True:
            can = self.getcandidate()
            if self.checkconstraint(can):
                return can

    def score(self,can):
        f1,f2 = self.objs(can)
        return f1 + f2

    def objs(self,x):
        return 1

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

    def get_energy(self,can,norm):
        sc = self.score(can)
        norm[1] = norm[1] if norm[1] > sc else sc
        e = ((sc-norm[0])/(norm[1] - norm[0]))
        return norm,e

    def checkconstraint(self,can):
        return True