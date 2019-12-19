#optimal paths = [[peso,vertice a viajar 1. vertice a viajar 2],[]]

def dijkstra (A,B,matriz):
    C=len(matriz)
    i=0
    itera=0
    itera2=0
    optpath=list()
    while i<C:
        optpath.append(1)
    while i<C-1:
        if i==0:
            itera=0
            D=matriz[A]
            for j in D:
                if j!=None and j!=0:
                    porver.append(itera)
                    optpath[itera]=[D[itera],itera]
                itera+=1
        else:
            itera2=porver[i-1]
            D=matriz[itera2]
            itera=0
            for j in D:
                if j!=None and j!=0:
                    if itera in porver:
                        E=optpath[itera2]
                        F=E[0]+j
                        E[0]=F
                        E2=optpath[itera]
                        if E[0]<E2:
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
                
        
