# -*- coding: utf-8 -*-
"""
CONTROL 2 S3
"""
import math

def verificadorRecorrido(recorrido):
    for nodos in recorrido:
        if nodos == False:
            return False
    return True

def minimoRecorrido(distancia,recorrido):
    index = -1
    minimo = float("inf")
    for i in range(len(distancia)):
        if not recorrido[i]:
            if distancia[i]< minimo:
                minimo = distancia[i]
                index = i
                
    return index

def MinDistance(W,u,v):
    vertices = int(math.sqrt(len(W)))
    distancia = list()
    trayectoria = list()
    recorrido = list()
    
    for i in range(len(W)):
        distancia.append(float("inf"))
        trayectoria.append(0)
        recorrido.append(False)
    distancia[u] = 0
    recorrido[u] = True
    
    for i in range(len(W)):
        if i != u:
            if W[u][i] > 0:
                distancia[i] = W[u][i]
                trayectoria[i] = i
                
    while not verificadorRecorrido(recorrido):
        index = minimoRecorrido(distancia, recorrido)
        recorrido[index] = True
        
        for i in range(len(distancia)):
            if i != index and W[index][i] > 0:
                if distancia[i] > distancia[index] + W[index][i]:
                    distancia[i] = distancia[index] + W[index][i]
                    trayectoria[i] = index
                    
    print (trayectoria,distancia)
        