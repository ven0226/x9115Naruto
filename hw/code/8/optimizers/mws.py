__author__ = 'Venkatesh'

import random
from helper.Utility import Utility


def mutate(mod,can,index):
    local = can[:]
    dec = mod.decisons[index]
    local[index] = random.uniform(dec.lo,dec.hi)
    return local

def maximizesolution(mod,sn,index,norm):
    bestSn = sn[:]
    steps = 10000
    changed = False

    moves = (mod.decisons[index].hi - mod.decisons[index].lo)/steps

    sn[index] = mod.decisons[index].lo
    for i in range(steps):
        sn[index] += moves
        if mod.checkconstraint(sn):
            norm, cur_score = mod.get_energy(sn,norm)
            norm, best_score = mod.get_energy(bestSn,norm)
            if cur_score < best_score:
                changed = True
                bestSn = sn[:]
    return changed, bestSn

def mws(mod):
    max_tries = 25
    max_changes = 100
    threshold = 0.01
    p = 0.05
    lives = 3
    best_sn = mod.generate()
    norm = mod.baseline_study()
    norm, best_sc = mod.get_energy(best_sn,norm)

    prev = []
    k = 1
    for i in range(max_tries):
        sn = mod.generate()
        cur = []
        Utility.say(str(k)+"|")
        for j in range(max_changes):
            norm,score = mod.get_energy(sn,norm)
            if score < threshold:
                f1,f2 = mod.objs(sn)
                norm,score = mod.get_energy(sn,norm)
                best_sn = sn[:]
                best_sc = score
                Utility.printOutput("Success", f1,f2,best_sn,f1+f2)
                return best_sn
            limit = len(mod.decisons)-1 if len(mod.decisons) > 0 else 0
            c = random.randint(0,limit)
            if p < random.random():
                temp = mutate(mod,sn,c)
                if mod.checkconstraint(temp):
                    sn = temp[:]
                    Utility.say('?')
                else:
                    Utility.say('.')
            else:
                changed, sn = maximizesolution(mod,sn,c,norm)
                if changed:
                    norm,local_sc = mod.get_energy(sn,norm)
                    if Utility.check_type1(mod,sn,best_sn):
                        best_sc = local_sc
                        best_sn = sn[:]
                    sn = sn[:]
                    Utility.say('+')
                else:
                    Utility.say('!')
            norm,local_sc = mod.get_energy(sn,norm)
            cur.append(local_sc)
        if not prev:
            prev = cur[:]
        else:
            lives += Utility.check_type2(prev,cur)
            prev = cur[:]
        if lives is 0:
            break
        k += max_changes
        Utility.say("\n")
    f1,f2 = mod.objs(sn)
    Utility.printOutput('Failure',f1,f2,best_sn,f1+f2)
    return best_sn