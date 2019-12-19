# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:57:07 2019

@author: karol
"""

import random as r

from countinversions import count_inversions
from countinversions2 import count_inversions_2

N = 10000
MAX = 1000

for i in range(100):
    testsequence_1 = [r.randint(0, MAX) for i in range(N)]
    testsequence_2 = testsequence_1.copy()
    v_1 = count_inversions(testsequence_1)
    v_2 = count_inversions_2(testsequence_2)
    if v_1 == v_2:
        print("Test {} passed!".format(i))
    else:
        print(v_1)
        print(v_2)
        print("Test {} failed!".format(i))
