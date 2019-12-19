# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:26:30 2019

@author: karol
"""

import random

from tiempos import calcula_tiempos, visualiza_tiempos
from AlienAndPassword1 import getNumber1

# Los parámetros MAX_CANT y STEP controlan los tamaños de instancias
# sobre las cuales se evaluará los algoritmos.
MAX_CANT = 5000
STEP = 100

instancias = list()
letras = [chr(i) for i in range(ord('A'), ord('Z')+1)]

for tamanho in range(1, MAX_CANT+1, STEP):
    instancia = (letras[random.randrange(0, len(letras))]
                 for i in range(tamanho))
    instancia = "".join(instancia)
    instancias.append(instancia)

tamanhos, tiempos = calcula_tiempos(getNumber1, instancias)
visualiza_tiempos(tamanhos, tiempos)
