# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:37:00 2019

@author: karol
"""


def count_inversions_slow(ts):
    n = len(ts)
    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if ts[i] > ts[j]:
                inv += 1
    return inv
