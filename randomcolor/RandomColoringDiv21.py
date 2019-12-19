# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""

"""En este programa generamos el
espacio de todos los colores por
separado, y ahí aplicamos las
condiciones, resultando en bruteforce """
import math

#class RandomColoringDiv2:
def getCount1(maxR,maxG,maxB,startR,startG,startB,d1,d2):
    contador = 0
    for R in range(0,maxR):             #Se genera el espacio de color rojo, n
        for G in range(0,maxG):         #Se intersecta el espacio de color azul con el espacio rojo, generando n*n
            for B in range(0,maxB):     #Se vuelve a intersectar el espacio de color verde, en el espacio de color azul, generando n*n*n
                """En este punto podemos determinar que la
                    complejidad del ejercicio es
                    O(n^3)."""
                if(math.fabs(R-startR) <= d2 and math.fabs(G-startG) <= d2 and math.fabs(B-startB) <= d2 ):
                    if((math.fabs(R-startR) >= d1 or math.fabs(G-startG) >= d1 or math.fabs(B-startB) >= d1)):
                        contador+=1
                
    return contador