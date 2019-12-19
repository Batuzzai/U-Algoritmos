# -*- coding: utf-8 -*-
"""
CONTROL 1 S1
"""

def MinNumber(S):
    menor = 0
    
    if len(S) == 1:
        if S[0] == 1:
            return 2
        else:
            return 1
    
    for numero in S:
        if 1 not in S:
            return 1
        
    for numero in S:
        if S.index(numero) <= len(S) - 2:
             if numero <= S[S.index(numero+1)]:
                 menor = numero
                 return menor - 1
            
        
        
        
        
            
            
