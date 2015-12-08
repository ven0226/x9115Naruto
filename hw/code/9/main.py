from __future__ import division
from models.DTLZ import DTLZ1
from models.DTLZ import DTLZ3
from models.DTLZ import DTLZ5
from models.DTLZ import DTLZ7
from optimizers.ga import ga
from helper.hypervolume_runner import HyperVolume_wrapper
import time
from helper.sk import *
if __name__ == '__main__':


    ######################### Start function to write to File
    def write_to_file(mod,filename,frontier,min_objs,max_objs):
        print max_objs
        print min_objs
        name='Pareto_Fronts/'+filename
        f=open(name,'w')
        i=0

        for can in frontier:
            can_objs = mod.objs(can)

            for i in xrange(mod.no_objectives):
                norm_objs = (can_objs[i] - min_objs[i])/(max_objs[i] - min_objs[i])
                s=str(norm_objs)
                f.write(s)
                f.write(" ")
            f.write("\n")
        f.close()
    ######################### End function to write to File
    repeats = 5
    objs = [2,4,6,8]
    decs = [10,20,40]
    for model in [DTLZ1,DTLZ3,DTLZ5,DTLZ7]:
        for obj in objs:
            for dec in decs:
                cur_e = []
                mod = model(dec,obj)
                min_objs,max_objs = mod.baseline_objs()
                for _ in range(repeats):
                    print("# Repeat: %d" % (_))
                    data = []
                    mod = model(dec,obj)
                    opt_rpt = []
                    g_algo = ga()
                    t1 = time.time()
                    frontier = ga().run(mod)
                    t2 = time.time()
                    filename = mod.name + "-" + str(mod) +"-" + str(dec) + "-PF-"+ str(_)
                    write_to_file(mod,filename,frontier,min_objs,max_objs)
                    print("# Runtime: %.3f secs" % (t2-t1))
                    opt_rpt.append(float(t2-t1))
                avg_time = sum(opt_rpt) / len(opt_rpt)
                #avg_energy = (avg_energy - min)/(max - min)
                print "="*50
                print "\nStarting Model = %s Optimizer = %s No. of Decision = %s No. of Objectives = %s \n" % (mod.name,str("GA"),str(dec),str(obj))
                print("# Average: %.3f secs" % (avg_time))
                print "="*50
    HyperVolume_wrapper()