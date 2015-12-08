from __future__ import division
__author__ = 'Venkatesh'

import random
import operator
from helper.Utility import Utility
from collections import OrderedDict

class ga():
    target = 0.00001
    name = "Standard GA"
    
    def __init__(self,candidates,generations,mutate_prob):
        self.candidates = int(candidates)
        self.generations = int(generations)
        self.mutate_prob = mutate_prob
        #print("# Seting: Candidates = %d ,Generations = %d ,Mutate_prob = %f" % (candidates,generations,mutate_prob))

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
        generations = 0
        lives = 5
        baseline = frontier[:]
        prev_era = self.fitting(mod,baseline)
        #print "Optimizer"
        for i in range(self.generations):
            #print "Start generation"
            to_select_sample = self.select(mod,frontier) # binary denomination score of all pairs
            sorted_sample = OrderedDict(sorted(to_select_sample.items(), key=lambda t: t[1],reverse=True)) # sorted by the scores
            slice = int(0.5 * self.candidates)
            selected_sample = Utility.take(slice, sorted_sample.iteritems()) # select 50% of the population
            selection_pool = []
            for key, value in selected_sample:
                selection_pool.append(frontier[key])
            new_frontier = self.get_new_frontier(mod,selection_pool) # perform crossover
            mutated_frontier = self.do_mutation(mod,new_frontier) # mutated some candidates
            cur_era = self.fitting(mod,mutated_frontier) #average
            generations += 1
            if Utility.better(mod,prev_era,cur_era):
                prev_era = cur_era[:]
                lives += 0
            else:
                lives += -1
            if lives is 0:
                return prev_era

            #print "Generations : ", generations
        #print "Best Solution : ", sum(cur_era)

        return cur_era

    def iDominate(self,mod,left,right):
        if mod.score(left) > mod.score(right):
            return True
        return False

    def select(self,mod,frontier):
        binary_result = {}
        can_id = 0
        for left in frontier:
            count = 0
            for right in frontier:
                if Utility.compare(mod,mod.objs(left),mod.objs(right)):
                    count += 1
            binary_result[can_id] = count
            can_id += 1
        return binary_result

    def get_new_frontier(self,mod,cur_frontier):
        new_frontier = []
        #print "new frontier"
        count = 0
        while count < self.candidates:
            m_i = random.randint(0,len(cur_frontier)-1)
            d_i = random.randint(0,len(cur_frontier)-1)
            while m_i == d_i:
                 d_i = random.randint(0,len(cur_frontier)-1)
            mom = cur_frontier[m_i]
            dad = cur_frontier[d_i]
            children = self.crossover(mom,dad)
            for child in children:
                if count < self.candidates:
                    new_frontier.append(child)
                count += 1
            #print "trying next"
        #print "finished frontier"
        return new_frontier

    def crossover(self,mom,dad):
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
        mutate_count = 0
        for i,can in enumerate(cur_frontier):
            rand_num = random.uniform(0,1)
            if rand_num < self.mutate_prob:
                index = random.randint(0,mod.no_decisions-1)
                cur_frontier[i] = self.mutate(mod,can,index)
                mutate_count += 1
        #print("# Mutate Count: %d" % (mutate_count))
        return cur_frontier

    def mutate(self,mod,can,index):
        dec = mod.decisons[index]
        can[index] = random.uniform(dec.lo,dec.hi)
        return can

    def fitting(self,mod,cur_frontier):
        cur_fitting = []
        for can in cur_frontier:
            objs_c = mod.objs(can)
            cur_fitting.append(objs_c)
        #cur_fitting = map(Utility.mean, zip(*cur_fitting))
        return cur_fitting