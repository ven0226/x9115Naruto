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
        for x in can[self.no_objectives-1:]:
            g_val += math.pow((x-0.5),2) - math.cos(20*math.pi*(x-0.5))
        g_val += self.no_decisions-self.no_objectives+1
        g_val *= 100

        return g_val

    def objs(self,can):
        objectives = []
        g_val = self.g(can)

        for i in range(self.no_objectives):
            val = 0.5*(1 + g_val)
            x = 0
            for _ in range(self.no_objectives - 1 - i):
                val *= can[_]
                x += 1
            if not i == 0:
                val *= (1-can[self.no_objectives - i])
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
        for x in can[self.no_objectives-1:]:
            g_val += math.pow((x-0.5),2) - math.cos(20*math.pi*(x-0.5))
        g_val += self.no_decisions-self.no_objectives+1
        g_val *= 100
        return g_val

    def score(self,can):
        return sum(self.objs(can))

    def objs(self,can):
        objectives = []
        g_val = self.g(can)
        for i in range(self.no_objectives):
            val = (1 + g_val)
            for x in range(self.no_objectives - 1 - i):
                val *= math.cos(can[x]*(math.pi/2))
            if i > 0:
                val *= math.sin(can[self.no_objectives - i]*(math.pi/2))
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
        for x in can[self.no_objectives-1:]:
            g_val += math.pow((x-0.5),2)
        return g_val

    def score(self,can):
        return sum(self.objs(can))

    def theta(self,x,g_val):
        return (math.pi/(4 * (1 + g_val))) * (1 + (2 * g_val * x))

    def objs(self,can):
        objectives = []
        g_val = self.g(can)
        for i in range(self.no_objectives):
            val = (1 + g_val)
            for x in range(self.no_objectives - 1 - i):
                val *= math.cos(self.theta(can[x],g_val)*(math.pi/2))
            if i > 0:
                val *= math.sin(self.theta(can[self.no_objectives - i],g_val)*(math.pi/2))
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

        g = 1 + 9/(self.no_decisions-self.no_objectives+1) * sum(can[self.no_objectives-1:])

        for i in range(self.no_objectives - 1):
            objectives.append(can[i])
        def calch():
            h = self.no_objectives
            for x in range(self.no_objectives-1): # no of objectives
                h += (objectives[x]/(1+g))*(1 + math.sin(3*math.pi*objectives[x]))
            return h

        objectives.append((1+g)*calch())

        return objectives

    def objs(self,can):
        return self.fm(can)
