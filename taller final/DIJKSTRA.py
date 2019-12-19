# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:16:55 2019

@author: chali
"""
import grafo

def DIJKSTRA(G,nodo):
    distancia = list()
    recorrido = []
    
    for vertice in G.vertices:
        if grafo.Arista(nodo,vertice).getPeso() == 0 and nodo != vertice:
            distancia.append(float("inf"))
            
        else:
            distancia.append(grafo.Arista(nodo,vertice).getPeso())
            
    distancia.append(0)
    recorrido.append(True)
    
    while len(recorrido) != len(G.vertices):
        vertice = min(distancia)
        pos = distancia.index(vertice)
        recorrido[pos] = True
        for i in range(0,len(G.vertices)):
            if G.vertices[i+1] is not None: 
                sig = G.vertices[i+1]
                if distancia[i]>distancia[pos] + grafo.Arista(sig,G.vertices[i]).getPeso():
                    distancia[i] = distancia[pos] + grafo.Arista(sig,G.vertices[i]).getPeso()
                
    print(distancia)            
        
DIJKSTRA(grafo.grafo1, "B")           
            
        