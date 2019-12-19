# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""
import math

#class RandomColoringDiv2:
def getCount2(maxR,maxG,maxB,startR,startG,startB,d1,d2):
    contador = 0
    M=[maxR,maxR,maxG,maxG,maxB,maxB]
    S=[startR,startR,startG,startG,startB,startB]
    x=[0,0,0,0,0,0]
    a=0
    for i in S:
        if (a%2==0):
            if (S[a]-d2<0):
                x[a]=0
            else:
                x[a]=S[a]-d2
        if (a%2==1):
            if (S[a]+d2>maxR):
                x[a]=M[a]
            else:
                x[a]=S[a]+d2  #definen los límites inferiores y superiores de los intervalos
        a+=1            
            
            
            
    for R in range(x[0],x[1]):             #Se genera el espacio de color rojo, n
        for G in range(x[2],x[3]):         #Se intersecta el espacio de color azul con el espacio rojo, generando n*n
            for B in range(x[4],x[5]):     #Se vuelve a intersectar el espacio de color verde, en el espacio de color azul, generando n*n*n
                """En este punto podemos determinar que la
                complejidad del ejercicio es
                O(n^3)."""
                if(math.fabs(R-startR) <= d2 and math.fabs(G-startG) <= d2 and math.fabs(B-startB) <= d2 ):
                    if((math.fabs(R-startR) >= d1 or math.fabs(G-startG) >= d1 or math.fabs(B-startB) >= d1)):
                        contador+=1
            
    return contador


print(getCount2(5,1,1,2,0,0,0,1))
print(getCount2(4,2,2,0,0,0,3,3))
