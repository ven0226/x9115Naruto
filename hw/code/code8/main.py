from code8.models.Schaffer import Schaffer
from code8.models.Kursawe import Kursawe
from code8.models.Osyczka2 import Osyczka2
from code8.models.Golinski import Golinski
from code8.models.DTLZ7 import DTLZ7
from code8.optimizers.de import de
from code8.optimizers.mws import mws
from code8.optimizers.sa import sa
from helper.sk import *
if __name__ == '__main__':
    repeats = 20
    for model in [DTLZ7]:
        data = []
        mod = model()
        for i,optimizer in enumerate([sa,mws,de]):
            opt_rpt = []
            opt_rpt.append(optimizer.func_name)
            for _ in range(repeats):
                print "\nStarting Model = %s Optimizer = %s \n" % (mod.name,str(optimizer.func_name))
                baseline = optimizer(mod)
                opt_rpt.append(mod.score(baseline))
            data.append(opt_rpt)
        rdivDemo(data)