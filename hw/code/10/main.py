import random as r
from models.Schaffer import Schaffer
from models.DTLZ import *
from optimizers.de import de
from optimizers.ga import ga
from helper.sk import *
import time

def getRandomSetting():
    setting = []
    setting.append(r.randrange(50,150,1))
    setting.append(r.randrange(100,1000,9))
    setting.append(r.uniform(0.01,0.15))
    return setting

if __name__ == '__main__':
    opt_trials = 5
    repeats = 5
    data = []
    settingList = []
    for _ in range(opt_trials):
        setting = getRandomSetting()
        settingList.append(setting)
        for model in [Schaffer]:
            mod = model()
            for i,optimizer in enumerate([de]):
                opt_rpt = []
                opt_rpt.append(str(_))
                for j in range(repeats):                   
                    print "\nStarting Model = %s Optimizer = %s \n" % (mod.name,str(optimizer.func_name))
                    baseline = optimizer(mod,setting[0],setting[1],setting[2])
                    opt_rpt.append(mod.score(baseline))
                data.append(opt_rpt)
    ranks = rdivDemo(data)
    opt_i = 0
    for _, __, x in sorted(ranks):
        opt_i =  x.name
        break
    optimalSetting = settingList[int(opt_i)]
    
    objs = [2,4,6,8]
    decs = [10,20,40]
    for model in [DTLZ1,DTLZ7]:
        data = []
        mod = model()
        opt_rpt = []
        #opt_rpt.append(ga.name)
        for obj in objs:
            for dec in decs:
                for _ in range(repeats):
                    print "\nStarting Model = %s Optimizer = %s \n" % (mod.name,str("ga"))
                    t1 = time.time()
                    ga(optimalSetting[0],optimalSetting[1],optimalSetting[2]).run(mod)
                    t2 = time.time()
                    print("# Runtime: %.3f secs" % (t2-t1))
                    opt_rpt.append(float(t2-t1))
                avg_time = sum(opt_rpt) / len(opt_rpt)
                print("# Average: %.3f secs" % (avg_time))
    
    