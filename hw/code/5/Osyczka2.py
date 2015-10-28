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
        #print("Entering generate")
        while True:
            can = self.getcandidate(self.decs)
            #print(can)
            if self.checkconstraint(can):
                #print("passed")
                return can
        #exit()

    def checkconstraint(self,can):
        #print(can)
        #exit()
        if not can[0] + can[1] - 2 >= 0:
            #print(1)
            return False

        if not 6 - can[0] - can[1] >= 0:
            #print (2)
            return False

        if not 2 - can[1] + can[0] >= 0:
            #print (3)
            return False

        if not 2 - can[0] + 3*can[1] >= 0:
            #print (4)
            return False

        if not 4 - can[3] - (can[2] - 3)**2 >= 0:
            #print (5)
            return False

        if not (can[4]-3)**3 + can[5] - 4 >= 0:
            #print (6)
            return False

        return True

    def osycska_func(self,can):
        f1 = -(25*(can[0]-2)**2 + (can[1] - 2)**2 + ((can[2]-1)**2)*((can[3]-4)**2) + (can[4]-1)**2 )
        f2 = sum([i**2 for i in can])
        #print(f1,f2)
        return f1,f2

    def score(self,can):
        f1,f2 = self.osycska_func(can)
        return f1+f2

    def mutate(self,can,index):
        dec = self.decs[index]
        can[index] = random.randrange(dec[0],dec[1])
        return can

    def maximizesolution(self,sn,index):
        bestSn = sn
        steps = 10
        for i in range(steps):
            sn = self.mutate(sn,index)
            if self.checkconstraint(sn):
                if self.score(sn) > self.score(bestSn):
                    bestSn = sn
        return bestSn

    def say(x):
        sys.stdout.write(str(x)); sys.stdout.flush()

def say(x):
    sys.stdout.write(str(x)); sys.stdout.flush()

def maxwalksat(mod):
    max_tries = 100
    max_changes = 50
    threshold = 150
    p = 0.5
    for i in range(max_tries):
        sn = mod.generate()
        #print("Solution = ",sn)
        for j in range(max_changes):
            if mod.score(sn) > threshold:
                f1,f2 = mod.osycska_func(sn)
                return "Success", sn, f1,f2
            c = random.randint(0,len(mod.decs)-1)
            if p < random.random():
                #print(sn)
                temp = mod.mutate(sn,c)
                if(mod.checkconstraint(temp)):
                    #print("mutated ",temp)
                    say('?')
                else:
                    say('.')
            else:
                bestSn = mod.maximizesolution(sn,c)
                if bestSn != sn:
                    sn = bestSn
                    say('+')
                else:
                    say('.')
        say('\n')
    f1,f2 = mod.osycska_func(sn)
    print(f1,f2)
    return 'failure',sn,f1,f2

if __name__ == '__main__':
    model = Osyczka2()
    #print(maxwalksat(model))
    status,sn,f1,f2 = maxwalksat(model)
    print
    print("Status: ",status)
    print("Best Solution: ",sn)
    print("F1: ",f1)
    print("F2: ", f2)
