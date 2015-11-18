__author__ = 'Venkatesh'

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