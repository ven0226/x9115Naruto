from __future__ import division
__author__ = 'Venkatesh'

import math
from code8.optimizers.decs import Decisions
from model import Model

class Schaffer(Model):
    name = "Shaffer"
    def __init__(self):
        lo = [-math.pow(10,5)]
        hi = [math.pow(10,5)]
        decs = Decisions(lo[0],hi[0])
        self.decisons.append(decs)

    def objs(self,x):
        #print x
        f1 = (x[0]*x[0])
        f2 = (x[0]-2)**2
        return f1,f2