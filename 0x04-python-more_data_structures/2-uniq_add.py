#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)

    sum = 0
    for x in newlist:
        sum = sum + x
        return sum
