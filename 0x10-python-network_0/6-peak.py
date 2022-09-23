#!/usr/bin/python3
"""
this module contains a function that finds the peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """function to find peak , uses binary search"""
    i = 0
    j = len(list_of_integers) - 1
    while i <= j:
        m = int((i + j)/2)
        if list_of_integers[m] > list_of_integers[m+1]:
            j = m
        else:
            i = m + 1
    return list_of_integers[i]
