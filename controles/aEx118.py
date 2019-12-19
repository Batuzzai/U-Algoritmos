# -*- coding: utf-8 -*-
"""
EXAMEN 1-18
a
"""

def Repartir(N,X):
    cabeza = N/(X-1) #CANTIDAD DE MONEDAS POR CABEZA SIN CAPITÁN
    
    base = cabeza + 1 #CANTIDAD DE MONEDAS +1 PARA HACER FELIZ A TRIPULACIÓN
    
    MC = N - base * (N/2) #TOTAL MONEDAS - MONEDAS DE TRIPULACIÓN x % APROB REQ
    
    return MC

