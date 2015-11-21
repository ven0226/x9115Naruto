from code8.models.Schaffer import Schaffer
from code8.models.Kursawe import Kursawe
from code8.models.Osyczka2 import Osyczka2
from code8.models.Golinski import Golinski
from code8.optimizers.de import de
from code8.optimizers.mws import mws
from code8.optimizers.sa import sa

if __name__ == '__main__':
    for model in [Schaffer,Osyczka2,Kursawe,Golinski]:
        mod = model()
        for optimizer in [sa,mws,de]:
            print "="*100
            print "Starting Model = %s Optimizer = %s \n\n" % (model.name,str(optimizer.func_name))
            optimizer(mod)
            #print "\nFinished Model = %s Optimizer = %s" % (model.name,str(optimizer.func_name))
            print "="*100
