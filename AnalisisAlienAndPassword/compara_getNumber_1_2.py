# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:26:30 2019

@author: karol
"""

import matplotlib.pyplot as plt
import random


from tiempos import calcula_tiempos, visualiza_tiempos


def getNumber1alt(candidatas):
    """Solución de AlienAndPassword, pero con la creación de las contraseñas
    candidatas manejada en otra parte, usando la clase set estándar de Python
    para el manejo de elementos únicos.

    Al tener la creación de contraseñas manejada en otra parte, se nota
    claramente la ventaja por sobre el uso de la list. Sin embargo, la
    comlpejidad en caso promedio de hacer add en tiempo costante
    (https://wiki.python.org/moin/TimeComplexity) no se aprecia bien aquí
    - con add en tiempo constante el crecimiento de tiempos de ejecución
    de la función sería lineal. La observación de tiempos de ejecución
    empíricos sugiere más bien algo de tipo n^a, con a levemente superior
    a 1.
    """

    unicas = set()
    for candidata in candidatas:
        unicas.add(candidata)
    return len(unicas)


def getNumber2alt(candidatas):
    """Solución de AlienAndPassword, pero con la creación de las contraseñas
    candidatas manejada en otra parte, usando la clase list estándar de Python
    para el manejo de elementos únicos.

    Al tener la creación de contraseñas manejada en otra parte, se nota
    claramente la complejidad cuadrática del manejo de duplicados con la list.
    """

    unicas = list()
    for candidata in candidatas:
        if candidata not in unicas:
            unicas.append(candidata)
    return len(unicas)


# Los parámetros MAX_CANT y STEP controlan los tamaños de instancias
# sobre las cuales se evaluará los algoritmos.
MAX_CANT = 5000
STEP = 100

instancias = list()
letras = [chr(i) for i in range(ord('A'), ord('Z')+1)]

for tamanho in range(1, MAX_CANT+1, STEP):
    S = (letras[random.randrange(0, len(letras))]
         for i in range(tamanho))
    S = "".join(S)
    instancia = [S[:i] + S[i+1:] for i in range(len(S))]
    instancias.append(instancia)

plt.ioff()
fig, axs = plt.subplots(2, 1, constrained_layout=True)

tamanhos, tiempos = calcula_tiempos(getNumber1alt, instancias)
plot1 = visualiza_tiempos(tamanhos, tiempos, axs[0])
axs[0].set_xlabel('tamaño de instancia')
axs[0].set_ylabel('tiempo de ejecución')
axs[0].set_title('versión con set')


tamanhos, tiempos = calcula_tiempos(getNumber2alt, instancias)
plot2 = visualiza_tiempos(tamanhos, tiempos, axs[1])
axs[1].set_xlabel('tamaño de instancia')
axs[1].set_ylabel('tiempo de ejecución')
axs[1].set_title('versión con list')

plt.show()
plt.ion()
