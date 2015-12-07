from __future__ import division
__author__ = 'Venkatesh'

import math
from optimizers.decs import Decisions
from models.model import Model

class DTLZ1(Model):
    no_decisions = 10
    no_objectives = 2
    decisions = []
    name = "DTLZ1"
    def __init__(self,decs=10,objs=2):
        self.no_decisions = decs
        self.no_objectives = objs
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

    def objs(self,can):
        objectives = []
        g_val = self.g(can)
        for i in range(self.no_objectives):
            val = (1 + g_val)
            x = 0
            for _ in range(len(can) - 1 - i):
                val *= can[x]
                x += 1
            if (x + 1) < len(can):
                val *= (1-can[x+1])
            objectives.append(val)
        return objectives

    def score(self,can):
        return sum(self.objs(can))


class DTLZ3(Model):
    no_decisions = 20
    no_objectives = 4
    decisions = []
    name = "DTLZ3"
    def __init__(self,decs=10,objs=2):
        self.no_decisions = decs
        self.no_objectives = objs
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

    def score(self,can):
        return sum(self.objs(can))

    def objs(self,can):
        objectives = []
        for i in range(self.no_objectives):
            val = (1 + self.g(can))
            for x in range(len(can) - 1 - i):
                val *= math.cos(x*(math.pi/2))
            if i > 0:
                val *= math.sin(x*(math.pi/2))
            objectives.append(val)
        return objectives


class DTLZ5(Model):
    no_decisions = 30
    no_objectives = 6
    decisions = []
    name = "DTLZ5"
    def __init__(self,decs=10,objs=2):
        self.no_decisions = decs
        self.no_objectives = objs
        lo = [0]
        hi = [1]
        for i in range(self.no_decisions):
            self.decisons.append(Decisions(lo[0],hi[0]))

    def g(self,can):
        g_val = 0
        for x in can:
            g_val += math.pow((x-0.5),2)
        return g_val

    def score(self,can):
        return sum(self.objs(can))

    def theta(self,x,g_val):
        return (math.pi/(4 * (1 + g_val))) * (1 + (2 * g_val * x))

    def objs(self,can):
        objectives = []
        for i in range(self.no_objectives):
            g_val = self.g(can)
            val = (1 + g_val)
            for x in range(len(can) - 1 - i):
                val *= math.cos(self.theta(x,g_val)*(math.pi/2))
            if i > 0:
                val *= math.sin(self.theta(x,g_val)*(math.pi/2))
            objectives.append(val)
        return objectives


class DTLZ7(Model):
    no_decisions = 40
    no_objectives = 8
    decisions = []
    name = "DTLZ7"
    def __init__(self,decs=10,objs=2):
        self.no_decisions = decs
        self.no_objectives = objs
        lo = [0]
        hi = [1]
        for i in range(self.no_decisions):
            self.decisons.append(Decisions(lo[0],hi[0]))

    def score(self,can):
        return abs(sum(self.objs(can)))

    def fm(self,can):
        objectives = []
        for i in range(self.no_objectives - 1):
            objectives.append(can[i])
        g = 1 + 9/len(can) * sum(can)

        def calch():
            total = 0
            for x in range(1): # no of objectives
                total += (objectives[0]/(1+g))*(1 + math.sin(3*math.pi*objectives[0]))
            total = len(can) - total
            return total

        objectives.append((1+g)*calch())

        return objectives

    def objs(self,can):
        return self.fm(can)
