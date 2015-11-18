from __future__ import division
__author__ = 'Venkatesh'

import random
from Utility import Utility

class DiffEvol:

    def generate_frontier(self,size,mod):
        frontier = []
        for i in range(size):
            frontier.append(mod.generate())
        return frontier

    def update(self,mod,f,cf,frontier,eb, total=0.0, n=0):
        ib = -1
        for i,x in enumerate(frontier):
            sc = mod.score(x)
            new = self.extrapolate(frontier,x,f,cf,i,mod)
            new_sc = mod.score(new)
            if new_sc < eb:
                Utility.say('?')
                eb = sc = new_sc
                frontier[i] = x[:]
                ib = i
            elif new_sc < sc:
                Utility.say('+')
                sc = new_sc
                frontier[i] = x[:]
            else:
                Utility.say('.')
            total += sc
            n += 1
        return total,n,eb,ib,frontier

    def extrapolate(self,frontier,one,f,cf,id,mod):
        out = one[:]
        two,three,four = self.threeOthers(frontier,id)
        ok = False
        while not ok:
            changed = False
            for d in range(len(mod.decisons)):
                x,y,z = two[d], three[d], four[d]
                if random.random() < cf:
                    changed = True
                    new = x + f*(y - z)
                    out[d]  = self.trim(new,d,mod) # keep in range
                if not changed:
                    mut_index = random.randint(0, len(mod.decisons)-1)
                    out[mut_index] = two[mut_index]
                ok = mod.checkconstraint(out)
        return out

    def trim(self,val,index,mod):
        res = val
        while res > mod.decisons[index].hi:
          res = res - mod.decisons[index].hi + mod.decisons[index].lo
        while res < mod.decisons[index].lo:
          res = mod.decisons[index].hi - (mod.decisons[index].lo - res)
        return res

    def threeOthers(self,frontier, avoid):
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

    def init_score(self,mod,frontier):
        total = 0
        n = 0
        for x in frontier:
            sc = mod.score(x)
            total += sc
            n += 1
        return total/n

    def de(self,mod):
        frontier_size = 50
        max_tries = 40
        f = 0.75
        cf = 0.3
        epsilon = 0.1
        ib = -1
        frontier = self.generate_frontier(frontier_size,mod)
        eb = self.init_score(mod,frontier)
        for k in range(max_tries):
            total,n,eb,ib,frontier = self.update(mod,f,cf,frontier,eb)
            Utility.say("\n")
            #en = total/n

            #if total/n > (1 - epsilon):
             #   break
        f1,f2 = mod.objs(frontier[ib])
        Utility.printOutput("Success",f1,f2,frontier[ib],eb)
        return frontier

