__author__ = 'Venkatesh'

import random
import operator
from helper.Utility import Utility
from collections import OrderedDict

class ga():
    candidates = 100
    generations = 1000
    target = 0.00001
    mutate_prob = 0.05
    name = "ga"

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
        prev_era = []
        cur_era = []
        for i in range(self.generations):
            to_select_sample = self.select(mod,frontier) # binary denomination score of all pairs
            sorted_sample = OrderedDict(sorted(to_select_sample.items(), key=lambda t: t[1],reverse=True)) # sorted by the scores
            selected_sample = Utility.take(40, sorted_sample.iteritems()) # select 40% of the population
            selection_pool = []
            for key, value in selected_sample.iteritems():
                selection_pool.append(frontier[key])
            new_frontier = self.get_new_frontier(mod,selection_pool) # perform crossover
            mutated_frontier = self.do_mutation(mod,new_frontier) # mutated some candidates
            fitting
            print "hello"

    def iDominate(self,mod,left,right):
        if mod.score(left) > mod.score(right):
            return True
        return False

    def select(self,mod,frontier):
        binary_result = {}
        can_id = 0
        for left in frontier:
            count = 0
            can_id += 1
            for right in frontier:
                if self.iDominate(mod,left,right):
                    count += 1
            binary_result[can_id] = count
        return binary_result

    def get_new_frontier(self,mod,cur_frontier):
        new_frontier = []
        while len(new_frontier) == self.candidates:
            m_i = random.randint(0,cur_frontier)
            d_i = random.randint(0,cur_frontier)
            while m_i == d_i:
                 d_i = random.randint(0,cur_frontier)
            mom = cur_frontier[m_i]
            dad = cur_frontier[d_i]
            new_frontier.extend(self.crossover(mom,dad))
        return new_frontier

    def crossover(self,mom,dad):
        print "crossover"
        joint_pt = random.randint(0,len(mom)-1)
        children = []
        children.append(self.get_child(mom,dad,joint_pt))
        children.append(self.get_child(dad,mom,joint_pt))
        return children

    def get_child(self,chrom1,chrom2,joint_pt):
        child = []
        child.extend(chrom1[:joint_pt])
        child.extend(chrom2[joint_pt:])
        return child

    def do_mutation(self,mod,cur_frontier):
        for i,can in enumerate(cur_frontier):
            if random.random < self.mutate_prob:
                index = random.randint(0,mod.no_decisions)
                cur_frontier[i] = self.mutate(mod,can,index)

        return cur_frontier

    def mutate(mod,can,index):
        dec = mod.decisons[index]
        can[index] = random.uniform(dec.lo,dec.hi)
        return can

    def fitting(self,mod,cur_frontier):
        cur_fitting = []
        return cur_fitting