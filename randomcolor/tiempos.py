# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
(modificaciones al codigo del profesor)
@author: karol
"""

import matplotlib.pyplot as plt
import time


def calcula_tiempos(funcion, instancias, descomprime=False):
    tiempos = list()

    for instancia in instancias:
        tiempo_ini = time.time()
        if not descomprime:
            funcion(instancias)
        else:
            funcion(*instancias)
        tiempo_fin = time.time()
        tiempos.append(tiempo_fin - tiempo_ini)

    return  tiempos


def visualiza_tiempos( tiempos, axs=None, label=""):
    if axs:
        grafica = axs.plot(tiempos, label=label)
    else:
        grafica = plt.plot(tiempos, label=label)
    return grafica
