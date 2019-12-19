class Nodo:
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
    

class Arbol:
    def __init__(self):
        self.raiz= Nodo(None,peso)

    def setPesoArbol(self):
        self.raiz.setPeso(self.raiz.Izq.getPeso() + self.raiz.Der.getPeso())

    def insertarNodo(self, Nodo):
        if self.raiz.Izq is None:
            self.raiz.Izq = Nodo
            self.raiz.Izq.bit = '0'
        else:
            self.raiz.Der = Nodo
            self.raiz.Der.bit = '1'
            Arbol()
        
