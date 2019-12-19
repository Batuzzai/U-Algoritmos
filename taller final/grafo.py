# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""
import math

class Arista:
    def __init__(self,nodo1,nodo2):
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.peso = 0
        
    def setPeso(self,peso):
        self.peso = peso
        
    def getPeso(self):
        return self.peso
    
    def getNodo1(self):
        return self.nodo1
    
    def getNodo2(self):
        return self.nodo2

class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = []
        self.aristas = []
        
    def vExiste(self,vertice):
        if self.vertices.count(vertice) == 0:
            return False
        else:
            return True
        
        
    def putVertice(self,vertice):
        if self.vExiste(vertice) == True:
            return False
        else:
            self.vertices.append(vertice)
            filas = len(self.matriz)
            columnas = filas
            matriz_aux = [[None]*(filas+1) for i in range(columnas+1)]
            
            for i in range(filas):
                for j in range(columnas):
                    matriz_aux[i][j] = self.matriz[i][j]
                    
            self.matriz = matriz_aux
            return True
    def getVertices(self):
        return self.vertices
        
    def putArista(self,desde, hasta, peso):
        A= Arista(desde, hasta)
        if (self.vExiste(desde) or self.vExiste(hasta)) == False:
            return False
        else:
            A.setPeso(peso)
            self.matriz[self.vertices.index(desde)][self.vertices.index(hasta)] = peso
            self.aristas.append(A)
            
    def getAristas(self):
        return self.aristas
            
            
    
        
    def drawMatriz(self,matriz): #IMPRIME LA MATRIZ CON MEJORAS VISUALES PARA UNA MEJOR COMPRENSIÓN
        cadena = "\n"
        
        for i in range(len(matriz)):
            cadena += "\t" + str(self.vertices[i])
            
        cadena += "\n" + (" " * len(matriz))
        
        for i in range(len(matriz)):
            cadena += "\n" + str(self.vertices[i]) + " |"
            
            for j in range(len(matriz)):
                if i == j and matriz[i][j] == None or matriz[i][j]== 0:
                    cadena += "\t" + "\\"
                
                else:
                    if matriz[i][j] == None:
                        cadena += "\t" + str(matriz[j][i])
                    elif math.isinf(matriz[i][j]):
                        cadena += "\t" + "inf"
                    else:
                        cadena += "\t" + str(matriz[i][j])
        cadena += "\n"
        print(cadena)
        
    def getMatriz(self,matriz): #RETORNA LA MATRIZ CORREGIDA DEL GRAFO, PARA SU POSTERIOR ANÁLISIS EN EL ALGORITMO
        matrix = [None] * len(self.vertices) #SE GENERA LA MATRIZ CUADRADA DE TAMAÑO len(vertices) CON ELEMENTOS "None" PARA SU POSTERIOR USO
        for i in range(len(self.vertices)):
            matrix[i] = [None]* len(self.vertices)
            
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if i == j and matriz[i][j] == None:
                    matrix[i][j] = 0 #DIAGONAL PESO 0
    
                else:
                    if matriz[i][j] == None:
                        matrix[i][j] = matriz[j][i] #ASIGNA LOS VALORES DE LA MATRIZ PROPIA A LA NUEVA MATRIZ
                        if matrix[i][j] == None:
                            matrix[i][j] = 0 #CORRIGE LOS VALORES "None" PARA QUE LA MATRIZ PUEDA USARSE COMO INT[]
                    elif math.isinf(matriz[i][j]):
                        matrix[i][j] = float("inf") #RETORNA LOS POSIBLES BUCLES DE LA MATRIZ (no en todos los casos)
                    else:
                        matrix[i][j] = matriz[i][j] #TRANSFORMA LA MATRIZ TRIANGULAR SUPERIOR A UNA MATRIZ SIMÉTRICA
        
            
        return matrix
        
grafoCorrecto = Grafo() #GRAFO CON TODOS SUS PESOS POSITIVOS

grafoCorrecto.putVertice(0)
grafoCorrecto.putVertice(1)
grafoCorrecto.putVertice(2)
grafoCorrecto.putVertice(3)
grafoCorrecto.putVertice(4)
grafoCorrecto.putVertice(5)
grafoCorrecto.putVertice(6)

grafoCorrecto.putArista(0, 1, 7)
grafoCorrecto.putArista(0, 3, 5)
grafoCorrecto.putArista(1, 2, 8)
grafoCorrecto.putArista(2, 4, 5)
grafoCorrecto.putArista(3, 4, 15)
grafoCorrecto.putArista(1, 3, 9)
grafoCorrecto.putArista(1, 4, 7)
grafoCorrecto.putArista(4, 6, 8)
grafoCorrecto.putArista(3, 6, 6)
grafoCorrecto.putArista(5, 6, 11)
grafoCorrecto.putArista(5, 4, 9)

grafoCorrecto.drawMatriz(grafoCorrecto.matriz)


grafoNegativo = Grafo() #GRAFO CON UN PESO NEGATIVO PARA DEMOSTRAR

grafoNegativo.putVertice(0)
grafoNegativo.putVertice(1)
grafoNegativo.putVertice(2)
grafoNegativo.putVertice(3)
grafoNegativo.putVertice(4)
grafoNegativo.putVertice(5)
grafoNegativo.putVertice(6)

grafoNegativo.putArista(0, 1, 7)
grafoNegativo.putArista(0, 3, -5) #<- NEGATIVO
grafoNegativo.putArista(1, 2, 8)
grafoNegativo.putArista(2, 4, 5)
grafoNegativo.putArista(3, 4, 15)
grafoNegativo.putArista(1, 3, 9)
grafoNegativo.putArista(1, 4, 7)
grafoNegativo.putArista(4, 6, 8)
grafoNegativo.putArista(3, 6, 6)
grafoNegativo.putArista(5, 6, 11)
grafoNegativo.putArista(5, 4, 9)

grafoNegativo.drawMatriz(grafoNegativo.matriz)


grafoINF = Grafo() #GRAFO CON UN PESO NEGATIVO Y SIN UNA ARISTA, EN DONDE NO ALCANZA A FINALIZAR

grafoINF.putVertice(0)
grafoINF.putVertice(1)
grafoINF.putVertice(2)
grafoINF.putVertice(3)
grafoINF.putVertice(4)
grafoINF.putVertice(5)
grafoINF.putVertice(6)

grafoINF.putArista(0, 1, 7)
grafoINF.putArista(0, 3, 5)
grafoINF.putArista(1, 2, 8)
grafoINF.putArista(2, 4, 5)
grafoINF.putArista(3, 4, 15)
grafoINF.putArista(1, 3, 9)
grafoINF.putArista(1, 4, 7)
grafoINF.putArista(4, 6, 8)
grafoINF.putArista(3, 6, 6)
grafoINF.putArista(5, 4, -9) #<-NEGATIVO

grafoINF.drawMatriz(grafoINF.matriz)



                 
        
            
            
            