from models.DTLZ import DTLZ1
from models.DTLZ import DTLZ3
from models.DTLZ import DTLZ5
from models.DTLZ import DTLZ7
from optimizers.algorithm import ga
from helper.sk import *
if __name__ == '__main__':
    repeats = 20
    for model in [DTLZ1]:
        data = []
        mod = model()
        opt_rpt = []
        g_algo = ga()
        opt_rpt.append(ga.name)
        for _ in range(repeats):
            print "\nStarting Model = %s Optimizer = %s \n" % (mod.name,str("ga"))
            baseline = ga().run(mod)
            opt_rpt.append(mod.score(baseline))
        data.append(opt_rpt)