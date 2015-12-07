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
    def better(prev,cur):
        for i in range(len(prev)):
            if not cur[i] < prev[i]:
                return -1
        return 0

    @staticmethod
    def compare(mod,prev,cur):
        prev_objs = mod.objs(prev)
        cur_objs = mod.objs(cur)
        for i in range(len(prev_objs)):
            if not prev_objs[i] < cur_objs[i]:
                return False
        return True

    @staticmethod
    def take(n, iterable):
        "Return first n items of the iterable as a list"
        return list(islice(iterable, n))