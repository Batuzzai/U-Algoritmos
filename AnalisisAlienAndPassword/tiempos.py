# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:11:48 2019

@author: karol
"""

import matplotlib.pyplot as plt
import time


def calcula_tiempos(funcion, instancias, descomprime=False):
    tiempos = list()
    tamanhos = list()

    for instancia in instancias:
        if not descomprime:
            tamanhos.append(len(instancia))
        else:
            tamanhos.append(sum(map(len, instancia)))

    for instancia in instancias:
        tiempo_ini = time.time()
        if not descomprime:
            funcion(instancia)
        else:
            funcion(*instancia)
        tiempo_fin = time.time()
        tiempos.append(tiempo_fin - tiempo_ini)

    return tamanhos, tiempos


def visualiza_tiempos(tamanhos, tiempos, axs=None, label=""):
    if axs:
        grafica = axs.plot(tamanhos, tiempos, label=label)
    else:
        grafica = plt.plot(tamanhos, tiempos, label=label)
    return grafica
