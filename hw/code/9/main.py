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
    for model in [DTLZ5,DTLZ7]:
        #opt_rpt.append(ga.name)

        for obj in objs:
            for dec in decs:
                for _ in range(repeats):
                    data = []
                    mod = model(dec,obj)
                    opt_rpt = []
                    g_algo = ga()
                    print "\nStarting Model = %s Optimizer = %s No. of Decision = %s No. of Objectives = %s \n" % (mod.name,str("GA"),str(dec),str(obj))
                    t1 = time.time()
                    ga().run(mod)
                    t2 = time.time()
                    print("# Runtime: %.3f secs" % (t2-t1))
                    opt_rpt.append(float(t2-t1))
                avg_time = sum(opt_rpt) / len(opt_rpt)
                print("# Average: %.3f secs" % (avg_time))