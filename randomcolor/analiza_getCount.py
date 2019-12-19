# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""

"""Aquí se realiza el análisis del tiempo
de ejecución de los tres programas, además
es posible ver la diferencia entre
getCount1 y getCount2 """
import random

from tiempos import calcula_tiempos, visualiza_tiempos
from RandomColoringDiv21 import getCount1
from RandomColoringDiv22 import getCount2
from RandomColoringDiv23 import getCount3

a = random.randrange(1, 100)
b = random.randrange(1, 100)
c = random.randrange(1, 100)
d = random.randrange(0, a-1)
e = random.randrange(0, b-1)
f = random.randrange(0, c-1)
g = random.randrange(0, 100)
h = random.randrange(0, 100)

while g>h:
    g = random.randrange(0, 100)
    
    
    

instancias = [a,b,c,d,e,f,g,h]

tiempos1 = calcula_tiempos(getCount1, instancias, True)
tiempos2 = calcula_tiempos(getCount2, instancias, True)
tiempos3 = calcula_tiempos(getCount3, instancias, True)


#RandomColoringDiv2 O(n^3):
print("O(n^3) AZUL")
visualiza_tiempos(tiempos1)
#RandomColoringDiv2 O(n^3) optimizado
print("O(n^3) optimizado NARANJO")
visualiza_tiempos(tiempos2)
#RandomColoringDiv2 O(k)
print("O(k) VERDE")
visualiza_tiempos(tiempos3)