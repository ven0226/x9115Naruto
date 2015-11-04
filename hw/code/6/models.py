from __future__ import division
__author__ = 'Venkatesh'

import random
import sys
import math

class Osyczka2:
    name = "Osyczka2"
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
            can.append(random.randrange(dec[0],dec[1]))
        return can

    def generate(self):
        while True:
            can = self.getcandidate(self.decs)
            if self.checkconstraint(can):
                return can

    def checkconstraint(self,can):
        if not can[0] + can[1] - 2 >= 0:
            return False

        if not 6 - can[0] - can[1] >= 0:
            return False

        if not 2 - can[1] + can[0] >= 0:
            return False

        if not 2 - can[0] + 3*can[1] >= 0:
            return False

        if not 4 - can[3] - (can[2] - 3)**2 >= 0:
            return False

        if not (can[4]-3)**3 + can[5] - 4 >= 0:
            return False

        return True

    def objs(self,can):
        f1 = -(25*(can[0]-2)**2 + (can[1] - 2)**2 + ((can[2]-1)**2)*((can[3]-4)**2) + (can[4]-1)**2 )
        f2 = sum([i**2 for i in can])
        return f1,f2

    def score(self,can):
        f1,f2 = self.objs(can)
        return f1+f2 if f1+f2 > 0 else 0

    def get_energy(self,can,norm):
        sc = self.score(can)
        norm[1] = norm[1] if norm[1] > sc else sc
        return norm,(sc/(norm[1] - norm[0]))

    def mutate(self,can,index):
        dec = self.decs[index]
        can[index] = random.randrange(dec[0],dec[1])
        return can

    def maximizesolution(self,sn,index,norm):
        bestSn = sn[:]
        steps = 10000
        changed = False

        moves = (self.decs[index][1] - self.decs[index][0])/steps

        sn[index] = self.decs[index][0]
        for i in range(steps):
            sn[index] += moves
            if self.checkconstraint(sn):
                norm, cur_score = self.get_energy(sn,norm)
                norm, best_score = self.get_energy(bestSn,norm)
                if cur_score > best_score:
                    changed = True
                    bestSn = sn[:]
        return changed, bestSn

    def baseline_study(self):
        min_value = sys.maxint
        max_value = -sys.maxint - 1
        for i in range(1000):
            sn = self.generate()
            sc = self.score(sn)
            if sc < min_value:
                min_value = sc
            if sc > max_value:
                max_value = sc
        return [min_value, max_value]

    def prob(self,old, new, k):
        return math.exp((old-new)/k)

class Schaffer():
    name = "Shaffer"
    decs = []
    def score(self,x):
        #print x
        f1,f2 = self.objs(x)
        return f1 + f2

    def objs(self,x):
        #print x
        f1 = (x[0]*x[0])
        f2 = (x[0]-2)**2
        return f1,f2

    def baseline_study(self):
        f1f2sum = []
        for i in range(100):
            x = []
            x.append(random.random())
            f1f2sum.append(self.score(x))
        return [min(f1f2sum), max(f1f2sum)]

    def get_energy(self,x,norm):
        #print x,"in get energy"
        return norm,(self.score(x)-norm[0])/(norm[1]-norm[0])

    def prob(self,old, new, k):
        return math.exp((old-new)/k)

    def generate(self):
        can = []
        can.append(random.random())
        return can

    def mutate(self,can,index):
        can[index] = random.random()
        return can

    def maximizesolution(self,sn,index,norm):
        bestSn = sn[:]
        steps = 1000
        changed = True
        for i in range(steps):
            sn[index] = random.random()
            self.get_energy(sn,norm)
            norm, cur_score = self.get_energy(sn,norm)
            norm, best_score = self.get_energy(bestSn,norm)
            if cur_score > best_score:
                changed = True
                bestSn = sn[:]
        return changed,bestSn

    def checkconstraint(self,can):
        return True

class Kursawe():
    name = "Kursawe"
    decs = []
    def __init__(self):
        for i in range(3):
            self.decs.append([-5,5])

    def objs(self,can = []):
        f1 = 0
        f2 = 0
        for x in range(len(can)-1):
            f1 += ( -10*math.exp(-0.2*math.sqrt( math.pow( can[x], 2) + math.pow( can[x+1], 2))))
            f2 += ( math.pow( abs(can[x]), 0.8 ) + 5 * math.sin(math.pow( can[x], 1)))
        return f1,f2

    def score(self,can):
        f1,f2 = self.objs(can)
        return f1+f2

    def get_energy(self,can,norm):
        sc = self.score(can)
        norm[1] = norm[1] if norm[1] > sc else sc
        return norm,(sc/(norm[1] - norm[0]))

    def generate(self):
        can = []
        for dec in self.decs:
            can.append(random.randrange(dec[0],dec[1]))
        return can

    def maximizesolution(self,sn,index,norm):
        bestSn = sn[:]
        steps = 1000
        changed = False

        moves = (self.decs[index][1] - self.decs[index][0])/steps

        sn[index] = self.decs[index][0]
        for i in range(steps):
            sn[index] += moves
            norm, cur_score = self.get_energy(sn,norm)
            norm, best_score = self.get_energy(bestSn,norm)
            if cur_score > best_score:
                changed = True
                bestSn = sn[:]
        return changed, bestSn

    def mutate(self,can,index):
        dec = self.decs[index]
        can[index] = random.randrange(dec[0],dec[1])
        return can

    def baseline_study(self):
        min_value = sys.maxint
        max_value = -sys.maxint - 1
        for i in range(1000):
            sn = self.generate()
            sc = self.score(sn)
            if sc < min_value:
                min_value = sc
            if sc > max_value:
                max_value = sc
        return [min_value, max_value]

    def prob(self,old, new, k):
        return math.exp((old-new)/k)

    def checkconstraint(self,can):
        return True

def sa(mod):
    s = mod.generate()
    norm = mod.baseline_study()
    norm,e = mod.get_energy(s,norm)
    sb = s[:]
    eb = e
    k = 1.0
    kmax = 999.0
    say("1|")
    while k < kmax:
      sn = mod.generate()
      norm, en = mod.get_energy(sn,norm)
      if en < eb:
           sb = sn[:]
           eb = en
           say("!")
      if en < e:
          s = sn[:]
          e = en
          say("+")
      elif mod.prob(e, en, k*7/(kmax)) < random.random():
          s = sn
          e = en
          say("?")
      say(".")

      k = k + 1
      if k % 25 == 0:
          say("\n"+str(int(k))+"|")

    f1,f2 = mod.objs(sb)
    printOutput('Success',f1,f2,sb,f1+f2)

def mws(mod):
    max_tries = 50
    max_changes = 100
    threshold = 0.99
    p = 0.5
    best_sn = []
    best_sc = 0
    norm = mod.baseline_study()
    for i in range(max_tries):
        sn = mod.generate()
        for j in range(max_changes):
            norm,score = mod.get_energy(sn,norm)
            if score > threshold:
                f1,f2 = mod.objs(sn)
                norm,score = mod.get_energy(sn,norm)
                best_sn = sn[:]
                best_sc = score
                return printOutput("Success", f1,f2,best_sn,best_sc)
            limit = len(mod.decs)-1 if len(mod.decs) > 0 else 0
            c = random.randint(0,limit)
            if p < random.random():
                temp = mod.mutate(sn,c)
                if mod.checkconstraint(temp):
                    sn = temp[:]
                    say('?')
                else:
                    say('.')
            else:
                changed, local_sn = mod.maximizesolution(sn,c,norm)
                if changed:
                    norm,local_sc = mod.get_energy(local_sn,norm)
                    if local_sc > best_sc:
                        best_sc = local_sc
                        best_sn = local_sn[:]

                    sn = local_sn[:]
                    say('+')
                else:
                    say('.')
        say('\n')
    f1,f2 = mod.objs(sn)
    return printOutput('Failure',f1,f2,best_sn,best_sc)

def printOutput(status,f1,f2,best_sn,best_sc):
    print
    print "Status = ",status
    print "F1 = ",f1
    print "F2 = ",f2
    print "Best Soln = ",best_sn
    print "Best Score = ",best_sc

def say(x):
    sys.stdout.write(str(x))
    sys.stdout.flush()

if __name__ == '__main__':
    for model in [Kursawe]:
        for optimizer in [sa,mws]:
            print "="*50
            print "Starting Model = %s Optimizer = %s \n\n" % (model.name,str(optimizer.func_name))
            optimizer(model())
            #print "\nFinished Model = %s Optimizer = %s" % (model.name,str(optimizer.func_name))
            print "="*50