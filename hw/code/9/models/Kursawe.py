from __future__ import division
__author__ = 'Venkatesh'

import math
from optimizers.decs import Decisions
from models.model import Model

class Kursawe(Model):
    name = "Kursawe"
    #decs = []
    decisons = []
    def __init__(self):

        lo = [-5,-5,-5]
        hi = [5,5,5]
        for i in range((len(hi))):
            self.decisons.append(Decisions(lo[i],hi[i]))

    def objs(self,can = []):
        objcs = []

        f1 = 0
        f2 = 0
        for x in range(len(can)-1):
            f1 += ( -10*math.exp(-0.2*math.sqrt( math.pow( can[x], 2) + math.pow( can[x+1], 2))))
            f2 += ( math.pow( abs(can[x]), 0.8 ) + 5 * math.sin(math.pow( can[x], 1)))
        objcs.append(f1)
        objcs.append(f2)
