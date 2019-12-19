# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:57:07 2019

@author: karol
"""

import random as r

from countinversionsslow import count_inversions_slow
from countinversions import count_inversions

N = 1000
MAX = 1000

for i in range(100):
    testsequence = [r.randint(0, MAX) for i in range(N)]
    v_1 = count_inversions_slow(testsequence)
    v_2 = count_inversions(testsequence)
    if v_1 == v_2:
        print("Test {} passed!".format(i))
    else:
        print(v_1)
        print(v_2)
        print("Test {} failed!".format(i))
