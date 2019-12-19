import grafo

#optimal paths = [[peso,vertice a viajar 1. vertice a viajar 2],[]]

def dijkstra (A,B,matriz):
    C=len(matriz)
    i=0
    itera=0
    itera2=0
    optpath=list()
    porver=list()
    optpath.append([0,0])
    while i<C:
        optpath.append([1])
        i+=1
    i=1
    
    porver.append(A)
    while i<C:
        if i==0:
            itera=0
            D=matriz[A]
            for j in D:
                if j!=None and j!=0:
                    porver.append(itera)
                    optpath[itera]=[D[itera],itera]
                itera+=1
            i+=1
        else:
            itera2=porver[i-1]
            D=matriz[itera2]
            itera=0
            for j in D:
                if j!=None and j!=0:
                    if j != itera and itera != 0:
                        
                        if itera in porver:
                            E=optpath[itera]
                            F=E[0]+j
                            E[0]=F
                            E2=optpath[itera]
                            if E[0]<E2[0]:
                                E.append(itera)
                                optpath[itera]=E
                        else:
                            porver.append(itera)
                            E=optpath[itera2]
                            F=E[0]+j
                            E[0]=F
                            E.append(itera)
                            optpath[itera]=E
                itera+=1
            i+=1
    print(optpath)       
             
               
 
dijkstra(1, 4, grafo.grafo2.getMatriz(grafo.grafo2.matriz))              
        
