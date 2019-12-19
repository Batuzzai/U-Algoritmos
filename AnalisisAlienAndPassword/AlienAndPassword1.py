# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:52:04 2019

@author: karol
"""


def getNumber1(S):
    """Solución de AlienAndPassword usando la clase set estándar de Python
    para el manejo de elementos únicos.

    Complejidad O(n^2), porque el manejo de las contraseñas candidatas no
    permite evitarlo, pero en la práctica mucho mejor que la de la versión
    implementada en AlienAndPassword2."""

    unicas = set()
    for i in range(len(S)):
        candidata = S[:i] + S[i+1:]
        unicas.add(candidata)
    return len(unicas)
