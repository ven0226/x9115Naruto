from __future__ import division
__author__ = 'Venkatesh'

import random
from helper.Utility import Utility

def sa(mod):
    s = mod.generate()
    norm = mod.baseline_study()
    norm,e = mod.get_energy(s,norm)
    sb = s[:]
    eb = e
    k = 1.0
    kmax = 1499.0
    lives = 5
    Utility.say("1|")
    prev = mod.default_objs()
    cur = []
    status = "Success"
    while k < kmax:
      sn = mod.generate()
      norm, en = mod.get_energy(sn,norm)
      if en < eb:
        sb = sn[:]
        eb = en
        Utility.say("!")
      if en < e:
        s = sn[:]
        e = en
        Utility.say("+")
      elif mod.prob(e, en, k*7/(kmax)) < random.random():
        s = sn
        e = en
        Utility.say("?")
      Utility.say(".")
      cur.append(mod.objs(sb))

      k = k + 1
      if k % 100 == 0:
        cur = map(Utility.mean, zip(*cur))
        if Utility.better(prev,cur):
            lives -= 1
        if lives is 0:
            status = "Terminated"
            break
        else:
            prev = cur[:]
        cur = []
        Utility.say("\n"+str(int(k))+"|")

    f1,f2 = mod.objs(sb)
    Utility.printOutput(status,f1,f2,sb,f1+f2)
    return sb
