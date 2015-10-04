__author__ = 'Bhashwanth'

import random
import math
import sys

def schaffer(x):
    return (x*x)+(x-2)**2

def baseline_study():
    f1f2sum = []
    for i in range(100):
        x = random.random()
        f1f2sum.append(schaffer(x))
    return [min(f1f2sum), max(f1f2sum)]
    
def get_energy(x,min,max):
    return (schaffer(x)-min)/(max-min)
    
def prob(old, new, k):
    return math.exp((old-new)/k)

def say(x):
    sys.stdout.write(str(x)); sys.stdout.flush()
    
def simulated_annealing():
    s = random.random()
    [min,max] = baseline_study()
    e = get_energy(s,min,max)
    
    sb = s
    eb = e                      
    k = 1.0
    kmax = 999.0
    say("1|")
    while k < kmax:                       
      sn = random.random()
      en = get_energy(sn,min,max)                       
      if en < eb:
           sb = sn
           eb = en          
           say("!")
      if en < e:
          s = sn
          e = en
          say("+")                        
      elif prob(e, en, k*7/(kmax)) < random.random():
          s = sn
          e = en
          say("?")
      say(".")
      
      k = k + 1
      if k % 25 == 0:
          say("\n"+str(int(k))+"|")
          
    print "\nBest solution: ",sb
    print "Energy of best solution: ",eb
    
simulated_annealing()

