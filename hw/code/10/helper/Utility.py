from __future__ import division
__author__ = 'Venkatesh'

from itertools import islice
import sys

class Utility:

    @staticmethod
    def printOutput(status,f1,f2,best_sn,best_sc):
        print
        print "Status = ",status
        print "F1 = ",f1
        print "F2 = ",f2
        print "Best Soln = ",best_sn
        print "Best Score = ",best_sc

    @staticmethod
    def say(x):
        sys.stdout.write(str(x))
        sys.stdout.flush()

    @staticmethod
    def mean(a):
        return sum(a) / len(a)

    @staticmethod
    def better(mod,prev,cur):
        cur_fitting = map(Utility.mean, zip(*cur))
        prev_fitting = map(Utility.mean, zip(*prev))
        if Utility.compare(mod,cur_fitting,prev_fitting):
           return True
        #print "failed"
        return False

    @staticmethod
    def compare(mod,cur,prev):
        bettered = True
        if cur == prev:
            return False
        for i in xrange(mod.no_objectives):
            if not cur[i] < prev[i]:
                bettered = False
        return bettered

    @staticmethod
    def take(n, iterable):
        "Return first n items of the iterable as a list"
        return list(islice(iterable, n))

    @staticmethod
    def write_to_file(mod,filename,frontier,min_objs,max_objs):
        #print max_objs
        #print min_objs
        name='Pareto_Fronts/'+filename +".out"
        f=open(name,'w')
        i=0

        for can in frontier:
            can_objs = mod.objs(can)

            for i in xrange(mod.no_objectives):
                norm_objs = (can_objs[i] - min_objs[i])/(max_objs[i] - min_objs[i])
                s=str(norm_objs)
                f.write(s)
                f.write(" ")
            f.write("\n")
        f.close()