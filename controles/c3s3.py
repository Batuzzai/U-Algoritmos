# -*- coding: utf-8 -*-
"""
CONTROL 3 S3
"""

def Donar(Paciente,Donante):
    print("DONADO", Paciente, Donante)

def donantesCruzados(parejas):
    Tparejas = len(parejas)
    
    if Tparejas == 2:
        Donar(parejas[0][0],parejas[1][1])
        Donar(parejas[1][0],parejas[0][1])
    
    elif Tparejas <= 1:
        print("No se puede realizar transplante", parejas[0][0], parejas[0][1])
    
    elif Tparejas == 3:
        Donar(parejas[0][0],parejas[1][1])
        Donar(parejas[1][0],parejas[2][1])
        Donar(parejas[2][0],parejas[0][1])
    
    else:
        Pmedio = int((len(parejas)-1)/2)
        
        izqParejas = parejas[0:Pmedio]
        derParejas = parejas[Pmedio+1:len(parejas)]
        
        donantesCruzados(izqParejas)
        donantesCruzados(derParejas)
        
        
        
    
    
