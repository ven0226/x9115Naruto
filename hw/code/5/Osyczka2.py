__author__ = 'Venkatesh'

import random
import math
import sys



class Osyczka2:
    decs = []
    def __init__(self):
        self.decs.append([0,10])
        self.decs.append([0,10])
        self.decs.append([1,5])
        self.decs.append([0,6])
        self.decs.append([1,5])
        self.decs.append([0,10])

    def getcandidate(self,d):
        can = []
        for dec in d:
            #print dec[0],dec[1]
            can.append(random.randint(dec[0],dec[1]))
        #print(can)
        return can

    def generate(self):
        i=0
        print("Entering generate")
        while True:
            can = self.getcandidate(self.decs)
            print(can)
            if self.checkconstraint(can):
                print("passed")
                #return can
                exit()
            else:
                print("constraint failed")
                i += 1
        #exit()

    def checkconstraint(self,can):
        if not can[0] + can[1] - 2 >= 0:
            print 1
            return False

        if not 6 - can[0] - can[1] >= 0:
            print 6 - can[0] - can[1]
            return False

        if not 2 - can[0] + can[1] >= 0:
            print 2 - can[0] + can[1]
            return False

        if not 2 - can[0] + 3*can[1] >= 0:
            print 4
            return False

        if not 4 - (can[2]-3)**2 - can[3] >= 0:
            print 5
            return False

        if not (can[4]-3)**3 + can[5] - 4 >= 0:
            print 6
            return False

    def score(self,can):
        f1 = -(25*(can[0]-2)**2 + (can[1] - 2)**2 + ((can[2]-1)**2)*((can[3]-4)**2) + (can[4]-1)**2 )
        f2 = sum([i**2 for i in can])
        return f1+f2

    def mutate(self,can,index):
        dec = self.decs[index]
        can[index] = random.randrange(dec[0],dec[1])

    def get_energy(self,can,min,max):
        return (self.score(can)-min)/(max-min)

    def prob(old, new, k):
        return math.exp((old-new)/k)

    def say(x):
        sys.stdout.write(str(x)); sys.stdout.flush()

def maxwalksat(mod):
    max_tries = 2
    max_changes = 2
    threshold = 0
    p = 0.5
    for i in range(max_tries):
        sn = mod.generate()
        print(sn)
        for j in range(max_changes):
            if mod.score(sn) > threshold:
                return sn
            c = random.randint(0,len(mod.decs)-1)
            if p < random.random():
                sn = mod.mutate(mod.can,c)
    return 'failure',sn

if __name__ == '__main__':
    model = Osyczka2();
    maxwalksat(model)
