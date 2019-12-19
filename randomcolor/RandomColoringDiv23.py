# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""

"""En este programa generamos el espacio
de las intersecciones de los tres espacios,
resultando así el espacio solución"""

import math

#class RandomColoringDiv2:
def getCount3(maxR,maxG,maxB,startR,startG,startB,d1,d2):
    contador = 0
    Rsup = max(0, startR - d2)
    Rinf = min(maxR - 1, startR + d2)
    Gsup = max(0, startG - d2)
    Ginf = min(maxG - 1, startG + d2)
    Bsup = max(0, startB - d2)
    Binf = min(maxB - 1, startB + d2)
    contador = (Binf - Bsup + 1)*(Ginf - Gsup + 1)*(Rinf - Rsup + 1)
        
    """ Aquí realizamos solo operaciones simples,
        en todos los procedimientos del programa
        con lo que obtenemos solo operaciones de
        orden constante, con lo que finalmente
        O(k)"""
        
    if (d1 > 0):
        d1-=1
        Rsup = max(0, startR - d1)
        Rinf = min(maxR - 1, startR + d1)
        Gsup = max(0, startG - d1)
        Ginf = min(maxG - 1, startG + d1)
        Bsup = max(0, startB - d1)
        Binf = min(maxB - 1, startB + d1)
        contador -= (Binf - Bsup + 1)*(Ginf - Gsup + 1)*(Rinf - Rsup + 1)
        
    return contador