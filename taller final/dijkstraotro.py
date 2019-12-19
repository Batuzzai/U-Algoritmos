# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 19:54:58 2019

@author: chali
"""
import grafo

def dijkstra2(G,desde,hasta):
    vertices = G.getVertices()
    aristas = G.getAristas()
    distancia = list()
    memoria= []
    pesotemp = int()
    pesoaux = int()
    
    if desde or hasta not in vertices:
        return ("Vertices no válidos")
    
    elif desde == hasta:
        return(0)
    
    
    else:
        for aris in range (len(aristas)):
            if aristas[aris].grafo.getNodo1() or aristas[aris].grafo.getNodo2() == desde:
                memoria[aris] = aristas[aris].grafo.getPeso()
                
                
                
                
            
        
    
    