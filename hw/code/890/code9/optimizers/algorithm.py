__author__ = 'Venkatesh'

import random

class ga():
    candidates = 100
    generations = 1000
    target = 0.00001
    mutate_prob = 0.05

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
        print "Runnning optimizer"
        frontier = []
        for _ in range(self.candidates):
            frontier.append(mod.generate())
        eb = self.init_score(mod,frontier)
        can = []
        index = None
        for i in range(self.generations):

            if random.random < self.mutate_prob:
                self.mutate(mod,can,index)
            print "hello"

    def iDominate(self,mod,left,right):
        if mod.score(left) > mod.score(right):
            return True
        return False

    def select(self,frontier):
        binary_result = {}
        id = 0
        for left in frontier:
            count = 0
            id += 1
            for right in frontier:
                if self.iDominate(left,right):
                    count += 1
            binary_result[id] = count
        print "select"

    def crossover(self,mom,dad):
        print "crossover"
        joint_pt = random.randint(0,len(mom)-1)
        child = []
        child = dad[:joint_pt]
        child = mom[joint_pt:]
        return child