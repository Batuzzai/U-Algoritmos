# -*- coding: utf-8 -*-
"""
Fibonacci Áureo
"""
import math

def FibAu(n):
    
    au1 = math.pow(((1+math.sqrt(5))/2),n)
    au2 = math.pow(((1-math.sqrt(5))/2),n)
    
    fib = (1/(math.sqrt(5)))*(au1+au2)
    
    return round(fib)