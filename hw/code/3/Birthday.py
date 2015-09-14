__author__ = 'Venkatesh'

from random import randint

def has_duplicates(years):
    uniq_years = {}
    dup = False
    chances = 0
    for i in years:
        if i in uniq_years.keys():
            chances += 1
            dup = True
        else:
            uniq_years[i] = 1
    return dup

def prob_same_birthday():
    birthday = []
    for i in range(1,24):
        birthday.append(randint(1,31))
    print has_duplicates(birthday)

print

year_list = [200,133,123,123]

print prob_same_birthday()


