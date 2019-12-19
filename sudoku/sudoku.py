# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""

"""
El programa pide los valores de la matriz 'tablero'
donde se encuentran los valores de referencia
iniciales
"""

def eliminar(Matriz,fila,columna,valor):
    listanueva=[]
    lista2=Matriz[fila][columna]
    if len(lista2)!=1:
        for i in Matriz[fila][columna]:
            if valor!=i:
                listanueva.append(i)
        Matriz[fila][columna]=listanueva
        if len(listanueva)==1:
            b= listanueva[0]
            corrector(Matriz,fila,columna,b,contador)
    return


def corrector(Matriz,fila,columna,valor,contador):
    contador[0] = contador[0] + 1
    f=0
    c=0
    while f<9:
        if fila!=f:
            eliminar(Matriz,f,columna,valor)
        f+=1
    while c<9:
        if columna!=c:
            eliminar(Matriz,fila,c,valor)
        c+=1
    a1=[0,1,2]
    a2=[3,4,5]
    a3=[6,7,8]
    interf=[]
    for i in a1:
        if fila==i:
            interf=a1
    for i in a2:
        if fila==i:
            interf=a2
    for i in a3:
        if fila==i:
            interf=a3
    interc=[]
    for i in a1:
        if columna==i:
            interc=a1
    for i in a2:
        if columna==i:
            interc=a2
    for i in a3:
        if columna==i:
            interc=a3
    for i in interf:
        for j in interc:
            if i!=fila:
                if j!=columna:
                    eliminar(Matriz,i,j,valor)
    return

'''def comprobarResuelto(tablero):
    contador = 0
    for filas in range(0,9):
        for columnas in range(0,9):
            if len(tablero[filas][columnas]) == 1:
                contador += 1
    if contador == 81:
        return False
    else:
        return True'''                
                
            
tablero = list([ list([1,2,3,4,5,6,7,8,9]) for filas in range(0, 9) ] for columnas in range(0, 9))

contador = [0]

while contador[0]<81:
    
    a= 0
    while a == 0:
        
        fila= int(input("Fila: "))-1
        if fila < 9:
            a=1
        elif fila > -1:
            a=1
            
    a= 0
    while a == 0:
        
        columna= int(input("Columna: "))-1
        if columna < 9:
            a=1
        elif columna > -1:
            a=1         
    a= 0
    while a == 0:
        
        valor= int(input("Valor: "))
        if valor < 10:
            a=1
        elif valor > 0:
            a=1        
            
    listaNew = [valor]

    tablero[fila][columna] = listaNew
    
    corrector(tablero,fila,columna,valor,contador)
    
    #print(tablero)
    
print(tablero)

        
         
        
        