from __future__ import division
__author__ = 'Venkatesh'

import random
from helper.Utility import Utility

def generate_frontier(size,mod):
    frontier = []
    for i in range(size):
        frontier.append(mod.generate())
    return frontier

def update(mod,f,cf,ib,frontier,eb, total=0.0, n=0):
    cur = []
    for i,x in enumerate(frontier):
        sc = mod.score(x)
        new = extrapolate(frontier,x,f,cf,i,mod)
        new_sc = mod.score(new)
        if Utility.check_type1(mod,new,frontier[ib]):
            Utility.say('?')
            eb = sc = new_sc
            frontier[i] = new[:]
            ib = i
        elif Utility.check_type1(mod,new,x):
            Utility.say('+')
            sc = new_sc
            frontier[i] = new[:]
        else:
            Utility.say('.')
        total += sc
        n += 1
        cur.append(sc)
    return total,n,eb,ib,frontier,cur

def extrapolate(frontier,one,f,cf,id,mod):
    out = one[:]
    two,three,four = threeOthers(frontier,id)
    ok = False
    while not ok:
        changed = False
        for d in range(len(mod.decisons)):
            x,y,z = two[d], three[d], four[d]
            if random.random() < cf:
                changed = True
                new = x + f*(y - z)
                out[d]  = trim(new,d,mod) # keep in range
            if not changed:
                mut_index = random.randint(0, len(mod.decisons)-1)
                out[mut_index] = two[mut_index]
            ok = mod.checkconstraint(out)
    return out

def trim(val,index,mod):
    res = val
    while res > mod.decisons[index].hi:
      res = res - mod.decisons[index].hi + mod.decisons[index].lo
    while res < mod.decisons[index].lo:
      res = mod.decisons[index].hi - (mod.decisons[index].lo - res)
    return res

def threeOthers(frontier, avoid):
    seen = []
    seen.append(avoid)
    i = 0
    selected = []
    while i < 3:
        picked = random.randint(0, len(frontier)-1)
        if picked not in seen:
            seen.append(picked)
            selected.append(frontier[picked])
            i += 1
    return selected[0],selected[1],selected[2]

def init_score(mod,frontier):
    total = 0
    n = 0
    for x in frontier:
        sc = mod.score(x)
        total += sc
        n += 1
    return total/n

def de(mod):
    frontier_size = 50
    max_tries = 40
    f = 0.75
    cf = 0.3
    epsilon = 0.1
    ib = 0
    frontier = generate_frontier(frontier_size,mod)
    eb = init_score(mod,frontier)
    prev = []
    lives = 5
    p = 1
    for k in range(max_tries):
        Utility.say(str(p)+"|")
        total,n,eb,ib,frontier,cur = update(mod,f,cf,ib,frontier,eb)
        if not prev:
            prev = cur[:]
        else:
            lives += Utility.check_type2(prev,cur)
            prev = cur[:]
        if lives is 0:
            break
        p += max_tries
        Utility.say("\n")
    f1,f2 = mod.objs(frontier[ib])
    Utility.printOutput("Success",f1,f2,frontier[ib],eb)
    return frontier[ib]

