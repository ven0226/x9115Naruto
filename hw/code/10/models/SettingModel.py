from __future__ import division
__author__ = 'Venkatesh'

from optimizers.decs import Decisions
from model import Model
from Kursawe import Kursawe
from optimizers.ga import ga
from helper.Utility import *
from helper.hypervolume_runner import *

class GASetting(Model):
    name = "GASetting"
    no_objectives = 1
    no_decisions = 3
    decisons = []

    def __init__(self):
        lo = [50,100,0.01]
        hi = [150,300,0.15]
        for i in range(self.no_decisions):
            self.decisons.append(Decisions(lo[i],hi[i]))

    def objs(self,x):
        mod = Kursawe()
        min_objs,max_objs = mod.baseline_objs()
        frontier = ga(x[0],x[1],x[2]).run(mod)
        filename = "hyper.out"
        Utility.write_to_file(mod,filename,frontier,min_objs,max_objs)
        output = HyperVolume_wrapper()
        ## Will always
        hve = 0
        for out in output:
            hve = out.hypervolume
        return hve


    def score(self,can):
        hve = self.objs(can)
        return hve