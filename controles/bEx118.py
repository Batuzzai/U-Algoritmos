# -*- coding: utf-8 -*-
"""
EXAMEN 1-18
b
"""

def getEgo(X,A,pos):
    
    if len(A) == 3:
        if A[0] == X:
            return pos
        elif A[1] == X:
            return pos + 1
        elif A[2] == X:
            return pos + 2
        else:
            return -1
        
    elif len(A) == 2:
        if A[0] == X:
            return pos
        elif A[1] == X:
            return pos +1
        else:
            return -1
        
    elif len(A) == 1:
        if A[0] == 1:
            return pos
        else:
            return -1
    
    mitad = int((len(A)-1)/2)
    
    if A[mitad] == X:
        return pos + mitad
    elif A[mitad] > X:
        return getEgo(X,A[0:mitad],pos)
    else:
        B = A[mitad+1:len(A)]
        pos = pos + abs(len(A) - len(B))
        return getEgo(X,B,pos)
        
        
    
        
