# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:52:04 2019

@author: karol
"""


def getNumber2(S):
    """Solución de AlienAndPassword usando la clase list estándar de Python
    para el manejo de elementos únicos.

    Naturalmente, revisar "a mano" todos los elementos vistos en el pasado
    para detectar duplicados es muy lento.
    Complejidad O(n^2), pero en la práctica mucho peor que la de la versión
    implementada en AlienAndPassword1."""

    unicas = list()
    for i in range(len(S)):
        candidata = S[:i] + S[i+1:]
        if candidata not in unicas:
            unicas.append(candidata)
    return len(unicas)
