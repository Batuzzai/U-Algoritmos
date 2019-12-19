# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:29:29 2019

@author: chali
"""
import math

class BoundingBox:
    x = [0,-2,-1]
    y = [-1,-1,-2]

    x.sort()
    y.sort()
    
    mayorx = x[len(x)-1]
    mayory = y[len(y)-1]
    menorx = x[0]
    menory = y[0]
    
    
            
    def smallestArea(self):
        
        ancho = math.sqrt((self.menory*self.menory)+(self.mayory*self.mayory))
        alto = math.sqrt((self.menory*self.menory)+(self.mayory*self.mayory))
        area = alto*ancho
        
        return area
    
box = BoundingBox
box.smallestArea()

        
        