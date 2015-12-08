import random as r
from models.Schaffer import Schaffer
from models.DTLZ import *
from optimizers.de import de
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
    repeats = 20
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
    print("# Optimal Seting: Candidates = %d ,Generations = %d ,Mutate_prob = %f" % (optimalSetting[0],optimalSetting[1],optimalSetting[2]))
    repeats = 4
    objs = [2,4,6,8]
    decs = [10,20,40]
    for model in [DTLZ1]:
        data = []
        mod = model()
        opt_rpt = []
        #opt_rpt.append(ga.name)
        for obj in objs:
            for dec in decs:
                cur_e = []
                mod = model(dec,obj)
                min,max = mod.baseline_study()
                for _ in range(repeats):
                    #print "\nStarting Model = %s Optimizer = %s \n" % (mod.name,str("ga"))
                    print "-"*50
                    t1 = time.time()
                    e = ga(optimalSetting[0],optimalSetting[1],optimalSetting[2]).run(mod)
                    t2 = time.time()
                    print "energy = ", e
                    if e > max:
                        norm = 1
                    else:
                        norm = (e - min)/(max - min)
                    print "norm", norm
                    cur_e.append(norm)
                    print("# Runtime: %.3f secs" % (t2-t1))
                    opt_rpt.append(float(t2-t1))
                    print "-"*50
                avg_time = sum(opt_rpt) / len(opt_rpt)
                avg_energy = sum(cur_e) / len(cur_e)
                print "="*50
                print "\nModel = %s Optimizer = %s No. of Decision = %s No. of Objectives = %s \n" % (mod.name,str("GA"),str(dec),str(obj))
                print "min = ", min
                print "max = ", max
                print("# Average: %.3f secs" % (avg_time))
                print("# Average Energy: %.5e " % (avg_energy))
                print "="*50
    
