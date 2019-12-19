# -*- coding: utf-8 -*-
"""
CONTROL 2 S1
"""

def getCost(kingdom,build,destroy):
    N = len(kingdom)
    val = 0
    val2 = 0
    costo = 0
    
    for i in range(N):
        for j in range(N):
               if kingdom[i][j] == 0:
                   val = build[i][j]
               else:
                   val2 = destroy[i][j]
               if val <= val2:
                   kingdom[i][j] = 1
                   costo += val
               else:
                   kingdom[i][j] = 0
                   costo += val2
                   
            
    return costo              
                   
