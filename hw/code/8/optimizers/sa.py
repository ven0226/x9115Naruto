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
    kmax = 999.0
    lives = 5
    Utility.say("1|")
    prev = []
    cur = []
    while k < kmax:
      sn = mod.generate()
      norm, en = mod.get_energy(sn,norm)

      if Utility.check_type1(mod,sn,sb):
        sb = sn[:]
        eb = en
        Utility.say("!")
      if Utility.check_type1(mod,sn,s):
        s = sn[:]
        e = en
        Utility.say("+")
      elif mod.prob(e, en, k*7/(kmax)) < random.random():
        s = sn
        e = en
        Utility.say("?")
      Utility.say(".")
      cur.append(en)

      k = k + 1
      if k % 50 == 0:
        #cur = map(Utility.mean, zip(*cur))
        if not prev:
            prev = cur[:]
        else:
            lives += Utility.check_type2(prev,cur)
            prev = cur[:]
        if lives is 0:
            break
        cur = []
        Utility.say("\n"+str(int(k))+"|")

    f1,f2 = mod.objs(sb)
    Utility.printOutput('Success',f1,f2,sb,f1+f2)
    return sb
