from __future__ import division
__author__ = 'Venkatesh'

import random
import math
import sys
from code9.optimizers.decs import Decisions
from code9.models.model import Model

class DTLZ1(Model):
    no_decisions = 10
    no_objectives = 2
    decisions = []
    name = "DTLZ1"
    def __init__(self):
        lo = [0]
        hi = [1]
        for i in range(self.no_decisions):
            self.decisons.append(Decisions(lo[0],hi[0]))

    def g(self,can):
        g_val = 0
        for x in can:
            g_val += math.pow((x-0.5),2) - math.cos(20*math.pi*(x-0.5))
        g_val += len(can)

        g_val *= 100

        return g_val

    def f1(self,can):
        val = 0.5 * (1 * self.g(can))

        for x in can[:-1]:
            val *= x

    def f2(self,can):
        return 0.5 *  (1 - can[0]) * (1.0 + self.g(can))

    def objs(self,can):
        obj1 = self.f1(can)
        obj2 = self.f2(can)
        return obj1,obj2


class DTLZ3(Model):
    no_decisions = 20
    no_objectives = 4
    decisions = []
    name = "DTLZ3"
    def __init__(self):
        lo = [0]
        hi = [1]
        for i in range(self.no_decisions):
            self.decisons.append(Decisions(lo[0],hi[0]))

    def f1(self,can):
        return can[0]

    def f2(self,can):
        g = 1 + 9/len(can) * sum(can)
        def calch():
            total = 0
            for x in range(1): # no of objectives
                total += (self.f1(can)/(1+g))*(1 + math.sin(3*math.pi*self.f1(can)))
            total = len(can) - total
            return total

        return (1+g)*calch()

    def objs(self,can):
        obj1 = self.f1(can)
        obj2 = self.f2(can)
        return obj1,obj2


class DTLZ5(Model):
    no_decisions = 30
    no_objectives = 6
    decisions = []
    name = "DTLZ5"
    def __init__(self):
        lo = [0]
        hi = [1]
        for i in range(self.no_decisions):
            self.decisons.append(Decisions(lo[0],hi[0]))

    def f1(self,can):
        return can[0]

    def f2(self,can):
        g = 1 + 9/len(can) * sum(can)
        def calch():
            total = 0
            for x in range(1): # no of objectives
                total += (self.f1(can)/(1+g))*(1 + math.sin(3*math.pi*self.f1(can)))
            total = len(can) - total
            return total

        return (1+g)*calch()

    def objs(self,can):
        obj1 = self.f1(can)
        obj2 = self.f2(can)
        return obj1,obj2


class DTLZ7(Model):
    no_decisions = 40
    no_objectives = 8
    decisions = []
    name = "DTLZ7"
    def __init__(self):
        lo = [0]
        hi = [1]
        for i in range(self.no_decisions):
            self.decisons.append(Decisions(lo[0],hi[0]))

    def f1(self,can):
        return can[0]

    def f2(self,can):
        g = 1 + 9/len(can) * sum(can)
        def calch():
            total = 0
            for x in range(1): # no of objectives
                total += (self.f1(can)/(1+g))*(1 + math.sin(3*math.pi*self.f1(can)))
            total = len(can) - total
            return total

        return (1+g)*calch()

    def objs(self,can):
        obj1 = self.f1(can)
        obj2 = self.f2(can)
        return obj1,obj2
