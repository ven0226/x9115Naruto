from __future__ import division
__author__ = 'Venkatesh'

import random
from code8.helper.Utility import Utility

def sa(mod):
    s = mod.generate()
    norm = mod.baseline_study()
    norm,e = mod.get_energy(s,norm)
    sb = s[:]
    eb = e
    k = 1.0
    kmax = 999.0
    Utility.say("1|")
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

      k = k + 1
      if k % 25 == 0:
          Utility.say("\n"+str(int(k))+"|")

    f1,f2 = mod.objs(sb)
    Utility.printOutput('Success',f1,f2,sb,f1+f2)
    return sb
