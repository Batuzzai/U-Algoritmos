# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:52:04 2019

@author: karol
"""


def getNumber3(S):
    """Solución de AlienAndPassword usando una observación de que la cantidad
    de contraseñas únicas generadas al eliminar un caracter es igual a la
    cantidad de grupos de elementos consecutivos iguales.

    Naturalmente, la complejidad de este algoritmo es mucho mejor que la
    de las soluciones basadas en búsqueda exhaustiva.
    Complejidad O(n)"""

    cant_cambios = 0

    for i in range(1, len(S)):
        if not S[i] == S[i-1]:
            cant_cambios += 1
    return cant_cambios + 1
