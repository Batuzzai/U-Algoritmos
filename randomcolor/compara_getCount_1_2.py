# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""

"""Aquí realizamos la comparación
entre getCount1 y getCount2, mostrando
sus gráficas y la diferencia de tiempo
de ejecución """
import random

from tiempos import calcula_tiempos, visualiza_tiempos
from RandomColoringDiv21 import getCount1
from RandomColoringDiv22 import getCount2

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

tiempodif = list()

for i in range(len(tiempos1)):
    tiempodif.append(tiempos1[i])
for i in range(len(tiempos2)):
    tiempodif[i] = tiempodif[i] - tiempos2[i]
    
visualiza_tiempos(tiempos1)
visualiza_tiempos(tiempos2)

print("la diferencia entre getCount1 y getCount2 es de:",sum(tiempodif))
