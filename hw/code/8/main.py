from models.Schaffer import Schaffer
from models.Kursawe import Kursawe
from models.Osyczka2 import Osyczka2
from models.Golinski import Golinski
from models.DTLZ7 import DTLZ7
from optimizers.de import de
from optimizers.mws import mws
from optimizers.sa import sa
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