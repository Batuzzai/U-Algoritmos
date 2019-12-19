import operator

class Nodo: #EL NÚMERO DE HOJAS ES IGUAL AL NÚMERO DE LETRAS DEL ALFABETO
    def __init__(self,letra,peso):
        self.Izq = None
        self.Der = None
        self.letra = letra
        self.peso = peso
        self.esLetra = False
        self.bit = None

    def hijo(self):
        return ((self.Izq, self.Der))

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

    def setPesoArbol(self):
        self.raiz.setPeso(self.raiz.Izq.getPeso() + self.raiz.Der.getPeso())

    def insertarHotfix(self): #PARA SOLUCIONAR PROBLEMA DE LETRA EN RAIZ
        if self.raiz.getLetra() is not None:
            temp = self.raiz
            if self.raiz.Izq is None:
                self.raiz = Nodo(None,Arbol.setPesoArbol())
                self.raiz.Izq = temp
            elif self.raiz.Der is None:
                self.raiz = Nodo(None,Arbol.setPesoArbol())
                self.raiz.Der = temp

    def insertarNodo(self, Nodo):
        if self.raiz.Izq is None:
            self.raiz.Izq = Nodo
            print("0")
            self.raiz.Izq.bit = '0'
            #self.insertarHotfix()
        elif self.raiz.Der is None:
            self.raiz.Der = Nodo
            print("1")
            self.raiz.Der.bit = '1'
            self.insertarHotfix()
        else:
            self.setPesoArbol()
            temp = self.raiz.Der
            nuevo = Arbol()
            nuevo.raiz = self.raiz.Der
            print("0")
            nuevo.raiz.Izq = temp
            nuevo.raiz.setLetra(None)
            nuevo.raiz.setPeso(0)
            #self.insertarHotfix()
            nuevo.insertarNodo(Nodo)
        



def probabilidad(letra,repeticion,total):
    prob = (repeticion/total)*100
    return prob

palabra = input("Inserte palabra a comprimir: ")
lista = list(palabra)
print(lista)
tamaño = len(lista)
print("Número de letras: ", tamaño)
print("La palabra pesa: ", tamaño * 8, " bits.")
alfabeto = []

for letra in lista:
    if letra not in alfabeto:
        alfabeto.append(letra)

print("Alfabeto: ",alfabeto)

frecuencias = {i:lista.count(i) for i in lista}
ordenado = sorted(frecuencias.items(), key=operator.itemgetter(1))
ordenadoV2 = ordenado[::-1]

print(ordenadoV2)

print("PROBABILIDADES: ")
for i in alfabeto:
    print(i, ": ",probabilidad(i,lista.count(i),tamaño),' %')

huffman = Arbol()

for i in range(len(ordenadoV2)):
    elemento = Nodo(ordenadoV2[i][0],ordenadoV2[i][1])
    huffman.insertarNodo(elemento)
    #print(ordenadoV2[i][0])
    #print(ordenadoV2[i][1])
#print(huffman.raiz.getPeso()) #PESO DEBUG





