# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""

"""En este programa, realizamos lo mismo que
en getCount1, con la diferencia que aquí
restringimos el espacio generado, así 
manteniendo la complejidad pero siendo más
eficiente. """

import math

#class RandomColoringDiv2:
def getCount2(maxR,maxG,maxB,startR,startG,startB,d1,d2):
    contador = 0
    for R in range(0,maxR):            #Se genera el espacio de color rojo, n. restringiéndolo
        if math.fabs(R-startR) <= d2:
            for G in range(0,maxG):         #Se intersecta el espacio de color azul con el espacio rojo, generando n*n, restrigiéndolo
                if math.fabs(G-startG) <= d2:
                    for B in range(0,maxB):     #Se vuelve a intersectar el espacio de color verde, en el espacio de color azul, generando n*n*n, restringiéndolo
                        """En este punto podemos determinar que la
                            complejidad del ejercicio es
                            O(n^3)."""
                        if math.fabs(B-startB) <= d2:
                            if((math.fabs(R-startR) >= d1 or math.fabs(G-startG) >= d1 or math.fabs(B-startB) >= d1)):
                                contador+=1
                
    return contador