from __future__ import division
__author__ = 'Venkatesh'

import random
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
        #print("############")
        for dec in d:
            #print dec[0],dec[1]
            #print(dec)
            can.append(random.randrange(dec[0],dec[1]))
        #print(can)
        #print("############")
        return can

    def generate(self):
        while True:
            can = self.getcandidate(self.decs)
            if self.checkconstraint(can):
                return can

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
        return f1+f2 if f1+f2 > 0 else 0

    def norm_score(self,can,norm):
        sc = self.score(can)
        #print(sc)
        #print(norm)
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
        # print("moves=%s min=%s max=%s steps=%s" % (moves,self.decs[index][0],self.decs[index][1],steps))
        # print "BEFORE SN:", sn


        sn[index] = self.decs[index][0]
        # print "INDEX :", index


        # print "AFTER SN:", sn
        # print "new sn:",sn
        # print "new bestsn:", bestSn
        # exit()
        for i in range(steps):
            # print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
            sn[index] += moves
            if self.checkconstraint(sn):
                # print("Solution",sn)
                # print("BestSn",bestSn)
                # print "===================================================================================="
                norm, cur_score = self.norm_score(sn,norm)
                norm, best_score = self.norm_score(bestSn,norm)

                # if cur_score == best_score:
                    # print "BOTH ARE EQUAL"
                    # exit()

                # print("Current Score",cur_score,"Best Score",best_score)
                if cur_score > best_score:
                    # print("changed")
                    # exit()
                    # print("Exit")
                    changed = True
                    #bestSn = sn
        return changed, bestSn

    def baseline_study(self):
        min_value = sys.maxint
        max_value = -sys.maxint - 1
        for i in range(1000):
            sn = self.generate()
            sc = self.score(sn)
            #print("Score",sc)
            if sc < min_value:
                #print("minvalue",min_value)
                min_value = sc
            if sc > max_value:
                max_value = sc
        return [min_value, max_value]

def say(x):
    sys.stdout.write(str(x))
    sys.stdout.flush()

def compare_listcomp(x, y):
    return [i for i, j in zip(x, y) if i == j]

def maxwalksat(mod):
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
            norm,score = mod.norm_score(sn,norm)
            if score > threshold:
                f1,f2 = mod.osycska_func(sn)
                norm,score = mod.norm_score(sn,norm)
                best_sn = sn[:]
                best_sc = score
                return "Success", best_sn, f1,f2,best_sc

            c = random.randint(0,len(mod.decs)-1)
            if p < random.random():
                temp = mod.mutate(sn,c)
                if(mod.checkconstraint(temp)):
                    sn = temp[:]
                    say('?')
                else:
                    say('.')
            else:
                changed, local_sn = mod.maximizesolution(sn,c,norm)
                if changed:
                    norm,local_sc = mod.norm_score(local_sn,norm)
                    if local_sc > best_sc:
                        best_sc = local_sc
                        best_sn = local_sn[:]

                    sn = local_sn[:]
                    say('+')
                else:
                    say('.')
        say('\n')
    f1,f2 = mod.osycska_func(sn)
    norm,score = mod.norm_score(sn,norm)
    return 'Failure',best_sn,f1,f2,best_sc

if __name__ == '__main__':
    model = Osyczka2()
    status,sn,f1,f2,best_score = maxwalksat(model)
    print
    print("Status: ",status)
    print("Best Solution: ",sn)
    print("F1: ",f1)
    print("F2: ", f2)
    print("Best Score:",best_score)
