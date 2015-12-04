from code9.models.DTLZ import DTLZ1
from code9.models.DTLZ import DTLZ3
from code9.models.DTLZ import DTLZ5
from code9.models.DTLZ import DTLZ7
from code9.optimizers.algorithm import ga
from code9.helper.sk import *
if __name__ == '__main__':
    repeats = 20
    for model in [DTLZ1]:
        data = []
        mod = model()
        opt_rpt = []
        opt_rpt.append(ga.name)
        for _ in range(repeats):
            print "\nStarting Model = %s Optimizer = %s \n" % (mod.name,str(optimizer.func_name))
            baseline = ga().run(mod)
            opt_rpt.append(mod.score(baseline))
        data.append(opt_rpt)