import operator

global bites
bites = []

class Nodo: #EL NÚMERO DE HOJAS ES IGUAL AL NÚMERO DE LETRAS DEL ALFABETO
    def __init__(self,letra,peso):
        self.Izq = None
        self.Der = None
        self.letra = letra
        self.peso = peso
        self.esLetra = False
        self.bit = None

    def getLetra(self):
        return self.letra

    def setLetra(self,letra):
        self.letra = letra

    def getPeso(self):
        return self.peso

    def setPeso(self,peso):
        self.peso = peso

    def getNodo(self):
        return self

    def getBit(self):
        return self.bit
    

class Arbol:
    def __init__(self):
        self.raiz= Nodo(None,0)

    def setPesoArbol(self): #PESO DE LA RAIZ = SUM(PESO HIJOS)
        self.raiz.setPeso(self.raiz.Izq.getPeso() + self.raiz.Der.getPeso())

    #NO FUNCIONA, PROBLEMA AL HACERLO RECURSIVO :c
    '''def insertarHotfix(self,Nodo): #PARA SOLUCIONAR PROBLEMA DE LETRA EN RAIZ 
        hotfix = Arbol()
        if self.raiz.Der.getLetra() is not None:
            default = self.raiz
            temp = self.raiz.Der
            hotfix.raiz = self.raiz.Der
            if hotfix.raiz.Izq is None:
                hotfix.raiz.Der = temp
                self.raiz.Izq = default 
                #print("0")
                bites.append('0')
                hotfix.insertarNodo(Nodo)
                hotfix.setPesoArbol()
            elif hotfix.raiz.Der is None:
                hotfix.insertarNodo(Nodo)
                bites.append('1')
                #print("1")'''

    def insertarNodo(self, Nodo):
        if self.raiz.Izq is None:
            self.raiz.Izq = Nodo
            self.raiz.Izq.bit = '0'
            bites.append('0')
            Nodo.esLetra = True
                
            #self.insertarHotfix(Nodo)
        elif self.raiz.Der is None:
            self.raiz.Der = Nodo
            self.raiz.Der.bit = '1'
            bites.append('1')
            #self.insertarHotfix(Nodo)
        else:
            self.setPesoArbol()
            temp = self.raiz.Der
            nuevo = Arbol()
            nuevo.raiz = self.raiz.Der
            nuevo.raiz.Izq = temp
            bites.append('0')
            Nodo.esLetra = True
            nuevo.raiz.setLetra(None)
            nuevo.raiz.setPeso(0)
            #self.insertarHotfix(Nodo)
            nuevo.insertarNodo(Nodo)
        



def probabilidad(letra,repeticion,total):
    prob = (repeticion/total)*100
    return prob

palabra = input("Inserte palabra a comprimir: ")
lista = list(palabra)
print(lista)
tamaño = len(lista)
print("Número de letras: ", tamaño)
print("La palabra pesa: ", tamaño * 8, " bites.")
alfabeto = []

for letra in lista: #STRING -> LIST
    if letra not in alfabeto:
        alfabeto.append(letra)

print("Alfabeto: ",alfabeto)

frecuencias = {i:lista.count(i) for i in lista} #LIST -> MAP
ordenado = sorted(frecuencias.items(), key=operator.itemgetter(1)) #ORDENA POR PESO Y MAP -> LISTA DE TUPLA
ordenadoV2 = ordenado[::-1] #INVERTIR LISTA DE TUPLA

print(ordenadoV2)

print("PROBABILIDADES: ") #DERIVADAS DE FRECUENCIAS
for i in alfabeto:
    print(i, ": ",probabilidad(i,lista.count(i),tamaño),' %')

huffman = Arbol() #NUEVO ÁRBOL PARA RECURSIVIDAD

for i in range(len(ordenadoV2)):
    elemento = Nodo(ordenadoV2[i][0],ordenadoV2[i][1])
    huffman.insertarNodo(elemento)
    #print(ordenadoV2[i][0])
    #print(ordenadoV2[i][1])
#print(huffman.raiz.getPeso()) #PESO DEBUG, HAY PROBLEMAS EN LOS PESOS

#print(bites)
codigo = ''.join(str(chars) for chars in bites)
print("Huffman code: ",codigo)                      #NO PUDE HACER QUE LOS NODOS FUESEN INDIVIDUALES POR LO TANTO PUEDE QUE FALTEN ALGUNOS BITES UWU
print("el código pesa: ", len(bites), " bites."     #IBA A SOLUCIONARLO CONCATENANDO LISTAS PERO NO SE GUARDABAN AL FINALIZAR






