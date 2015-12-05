__author__ = 'Venkatesh'

import random
from helper.Utility import Utility


def mutate(mod,can,index):
    dec = mod.decisons[index]
    can[index] = random.uniform(dec.lo,dec.hi)
    return can

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
    max_tries = 100
    max_changes = 100
    threshold = 0.001
    p = 0.05
    lives = 3
    best_sn = mod.generate()
    norm = mod.baseline_study()
    norm, best_sc = mod.get_energy(best_sn,norm)

    prev = mod.default_objs()
    k = 1
    Utility.say(str(k)+"|")
    for i in range(max_tries):
        sn = mod.generate()
        cur = []
        for j in range(max_changes):
            norm,score = mod.get_energy(sn,norm)
            if score < threshold:
                f1,f2 = mod.objs(sn)
                norm,score = mod.get_energy(sn,norm)
                best_sn = sn[:]
                best_sc = score
                Utility.printOutput("Success", f1,f2,best_sn,best_sc)
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
                changed, local_sn = maximizesolution(mod,sn,c,norm)
                if changed:
                    norm,local_sc = mod.get_energy(local_sn,norm)
                    if local_sc < best_sc:
                        best_sc = local_sc
                        best_sn = local_sn[:]
                    sn = local_sn[:]
                    Utility.say('+')
                else:
                    Utility.say('.')
            cur.append(mod.objs(sn))
        cur = map(Utility.mean, zip(*cur))
        if Utility.better(prev,cur):
            lives -= 1
        if lives is 0:
            break
        else:
            prev = cur[:]
        k += max_changes
        Utility.say("\n"+str(int(k))+"|")
    f1,f2 = mod.objs(sn)
    Utility.printOutput('Failure',f1,f2,best_sn,best_sc)
    return best_sn