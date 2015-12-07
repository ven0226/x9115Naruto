from __future__ import division
from models.DTLZ import DTLZ1
from models.DTLZ import DTLZ3
from models.DTLZ import DTLZ5
from models.DTLZ import DTLZ7
from optimizers.algorithm import ga
import time
from helper.sk import *
if __name__ == '__main__':

    repeats = 1
    objs = [2,4,6,8]
    decs = [10,20,40]
    for model in [DTLZ1,DTLZ3,DTLZ5,DTLZ7]:
        #opt_rpt.append(ga.name)

        for obj in objs:
            for dec in decs:
                cur_e = []
                mod = model(dec,obj)
                min,max = mod.baseline_study()
                print "min = ", min
                print "max = ", max
                for _ in range(repeats):
                    print("# Repeat: %d" % (_))
                    data = []
                    mod = model(dec,obj)
                    opt_rpt = []
                    g_algo = ga()
                    t1 = time.time()
                    e = ga().run(mod)
                    print "energy = ", e
                    norm = (e - min)/(max - min)
                    print "norm", norm
                    cur_e.append(norm)
                    t2 = time.time()
                    print("# Runtime: %.3f secs" % (t2-t1))
                    opt_rpt.append(float(t2-t1))
                avg_time = sum(opt_rpt) / len(opt_rpt)
                avg_energy = sum(cur_e) / len(cur_e)
                #avg_energy = (avg_energy - min)/(max - min)
                print "="*50
                print "\nStarting Model = %s Optimizer = %s No. of Decision = %s No. of Objectives = %s \n" % (mod.name,str("GA"),str(dec),str(obj))
                print("# Average: %.3f secs" % (avg_time))
                print("# Average Energy: %.5e " % (avg_energy))
                print "="*50