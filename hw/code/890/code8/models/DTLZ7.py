from __future__ import division
__author__ = 'Venkatesh'

import random
import math
import sys
from code8.optimizers.decs import Decisions

class DTLZ7:
    no_decisions = 10
    decisions = []
    def __init__(self):
        lo = [0]
        hi = [1]
        for i in range(self.no_decisions):
            self.decisons.append(Decisions(lo[0],hi[0]))

    def f1(self,can):
        return can[0]

    def f2(self,can):
        g = 1 + 9/len(can) * sum(x for x in can)
        def calch():
            total = 0
            for x in range(1): # no of objectives
                total += (self.f1(can)/(1+g))*(1 + math.sin(3*math.pi*self.f1(can)))
            total = len(can) - total
            return total

        return (1+g)*calch()

