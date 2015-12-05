from models.DTLZ import DTLZ1
from models.DTLZ import DTLZ3
from models.DTLZ import DTLZ5
from models.DTLZ import DTLZ7
from optimizers.algorithm import ga
import time
from helper.sk import *
if __name__ == '__main__':
    repeats = 20
    for model in [DTLZ1,DTLZ3,DTLZ5,DTLZ7]:
        data = []
        mod = model()
        opt_rpt = []
        g_algo = ga()
        #opt_rpt.append(ga.name)
        for _ in range(repeats):
            print "\nStarting Model = %s Optimizer = %s \n" % (mod.name,str("ga"))
            t1 = time.time()
            ga().run(mod)
            t2 = time.time()
            print("# Runtime: %.3f secs" % (t2-t1))
            opt_rpt.append(float(t2-t1))
        avg_time = sum(opt_rpt) / len(opt_rpt)
        print("# Average: %.3f secs" % (avg_time))