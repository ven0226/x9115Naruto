__author__ = 'Venkatesh'

import sys
from helper.sk import *

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
                return False
        return True

    @staticmethod
    def check_type1(mod,X,Y):
        objs_x = mod.objs(X)
        objs_y = mod.objs(Y)
        bettered = False
        for i, (Xi, Yi) in enumerate(zip(objs_x,objs_y)):
            if Utility.lt(Xi,Yi):
                bettered = True
            else:
                return False
        return  bettered

    @staticmethod
    def lt(x,y):
        return x < y

    @staticmethod
    def check_type2(era,era_1):
        val  = a12(era,era_1)
        if val > 0.56:
            return 5
        else:
            return -1