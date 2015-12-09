from __future__ import division
from models.DTLZ import *
from optimizers.ga import ga
from helper.Utility import *
from helper.sk import *
from helper.hypervolume_runner import *
import time

if __name__ == '__main__':
    opt_trials = 5
    repeats = 20
    data = []
    settingList = []
    candidates = 95
    generations = 109
    m_p = 0.12
    repeats = 20
    objs = [2]
    decs = [10]
    facts = ["untuned","tuned"]
    sets = [[100,1000,0.1],[95,109,0.12]]
    to_rdiv = []
    s = 0
    for setting in sets:
        local = []
        local.append(facts[s])
        for model in [DTLZ7]:
            data = []
            opt_rpt = []
            #opt_rpt.append(ga.name)
            for obj in objs:
                for dec in decs:
                    cur_e = []
                    mod = model(dec,obj)
                    min_objs,max_objs = mod.baseline_objs()
                    for _ in range(repeats):
                        #print "Starting Model = %s Optimizer = %s \n" % (mod.name,str("ga"))
                        print "-"*50
                        t1 = time.time()
                        frontier = ga(setting[0],setting[1],setting[2]).run(mod)
                        t2 = time.time()
                        filename = mod.name + "-" + str(obj)
                        Utility.write_to_file(mod,filename,frontier,min_objs,max_objs)
                        print("# Runtime: %.3f secs" % (t2-t1))
                        output = HyperVolume_wrapper()
                        for out in output:
                            local.append(out.hypervolume)
                        opt_rpt.append(float(t2-t1))
                        print "-"*50
                    avg_time = sum(opt_rpt) / len(opt_rpt)
                    print "="*50
                    print "\nModel = %s Optimizer = %s No. of Decision = %s No. of Objectives = %s \n" % (mod.name,str("GA"),str(dec),str(obj))
                    print "min = ", min_objs
                    print "max = ", max_objs
                    print("# Average: %.3f secs" % (avg_time))
                    print "="*50
        to_rdiv.append(local)
        s += 1
    rdivDemo(to_rdiv)