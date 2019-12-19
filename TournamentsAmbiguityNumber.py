# -*- coding: utf-8 -*-
"""
Gonzalo Salazar
Alejandro Álvarez
"""

class TournamentsAmbiguityNumber:
    def scrutinizeTable(table = list() ):
        contador = 0
        
        for i in range(0,len(table)): #COMBINATORIA PARA GENERAR LA TABLA BRUTEFORCE
            for j in range(0,len(table)):
                for k in range(0,len(table)):
                    if table[i][j] == "1" and table[j][k] == "1" and table[k][i] == "1": #CONDICIÓN
                        contador+=1
                    
                        
        return contador
	

