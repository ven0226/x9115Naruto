__author__ = 'Venkatesh & bhashwanth'

from random import randint

def has_duplicates(years):
    has_dups = False
    for i in years:
        if years.count(i) > 1:
            has_dups = True
    return has_dups

def prob_same_birthday():
    dup_count = 0
    for i in range(0,1000):
        birthday = []
        for i in range(1,24):
            birthday.append(randint(1,365))
        if has_duplicates(birthday) == True:
            dup_count += 1
    print "With 1000 simulations, the probability that a simulation has duplicates is ",dup_count/1000.0
    
prob_same_birthday()

