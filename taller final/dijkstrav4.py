# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez

"""

import grafo

def verificadorRecorrido(recorrido): #PARA VERIFICAR ELEMENOS BOOLEANOS EN UNA LISTA
    for nodos in recorrido:
        if nodos == False:
            return False
    return True

def minimoRecorrido(distancia,recorrido): #PARA ENCONTRAR LA DISTANCIA MÁS CORTA Y QUE NO ESTÉ RECORRIDA
    index = -1
    minimo = float("inf")
    for i in range(len(distancia)):
        if not recorrido[i]:
            if distancia[i]< minimo:
                minimo = distancia[i]
                index = i
                
    return index

def dijkstra(M, desde): #UTILIZAMOS LA MATRIZ DE ADYACENCIA OBTENIDA EN LA CLASE GRAFO Y UN NODO DESDE DONDE REALIZAR EL ANÁLISIS
    distancia = list()
    trayectoria = list()
    recorrido = list()
    
    for i in range(len(M)):
        distancia.append(float("inf"))
        trayectoria.append(-1)          # SE ESTABLECE -1 COMO PUNTO DE INICIO EN TRAYECTORIA
        recorrido.append(False)
    distancia[desde] = 0
    recorrido[desde] = True
    
    for i in range(len(M)):
        if i != desde:
            if M[desde][i] > 0:
                distancia[i] = M[desde][i]
                trayectoria[i] = i
                
    while not verificadorRecorrido(recorrido):
        index = minimoRecorrido(distancia, recorrido)
        recorrido[index] = True
        
        for i in range(len(distancia)):
            if i != index and M[index][i] > 0:
                if distancia[i] > distancia[index] + M[index][i]:
                    distancia[i] = distancia[index] + M[index][i]
                    trayectoria[i] = index
                    
    print (trayectoria,distancia) # TRAYECTORIA = LISTA QUE CONTIENE EL ID DE LOS NODOS POR LOS CUALES DEBE PASAR PARA LLEGAR AL NODO SIGUIENTE
                                  # DISTANCIA = LISTA QUE CONTIENE LOS PESOS ACUMULADOS RELACIONADOS CON LA TRAYECTORIA PARA REVISAR CADA NODO DESDE EL ORIGEN
#PARA UNA MEJOR COMPRENSIÓN, ANALIZAR LOS RESULTADOS TRAYECTORIA[i] CON DISTANCIA[i] Y COMPARAR CON EL DIBUJO O CON LA MATRIZ DE ADYACENCIA EN GRAFO.py
    
dijkstra(grafo.grafoCorrecto.getMatriz(grafo.grafoCorrecto.matriz), 0)
dijkstra(grafo.grafoNegativo.getMatriz(grafo.grafoNegativo.matriz), 0)
#dijkstra(grafo.grafoINF.getMatriz(grafo.grafoINF.matriz), 0) #<- ELIMINAR "#" PARA VERIFICAR QUE EL CICLO NO TERMINA"

                
        