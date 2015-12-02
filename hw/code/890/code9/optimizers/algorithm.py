__author__ = 'Venkatesh'

import random

class ga():
    candidates = 100
    generations = 1000

    def mutate(mod,can,index):
        dec = mod.decisons[index]
        can[index] = random.uniform(dec.lo,dec.hi)
        return can

    def init_score(self,mod,frontier):
        total = 0
        n = 0
        for x in frontier:
            sc = mod.score(x)
            total += sc
            n += 1
        return total/n

    def run(self,mod):
        frontier = []
        for _ in range(self.candidates):
            frontier.append(mod.generate())
        eb = self.init_score(mod,frontier)

        for i in range(self.generations):
            print "hello"
        print "Runnning optimizer"

    def select(self):
        print "select"

    def crossover(self,mom,dad):
        random.randint
        print "crossover"