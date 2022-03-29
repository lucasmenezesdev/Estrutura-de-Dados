class Grafo():
    def __init__(self):
        self.grafo = {}

    def addVertice(self, vertice):
        self.grafo[vertice] = []

    def addAresta(self, vertice1, vertice2):
        self.grafo[vertice1].append(vertice2)
        
    def removeVertice(self, vertice):
        self.grafo.pop(vertice)

    def removeAresta(self, vertice1, vertice2):
        self.grafo[vertice1].remove(vertice2)
        
    def getGrau(self, vertice):
        return len(self.grafo[vertice])

    def getGrafo(self):
        return self.grafo
    
    def isEuleriano(self):
        grauImpar = 0
        for vertice in self.grafo:
            grau = self.getGrau(vertice)
            if (grau % 2) == 1:
                grauImpar += 1
        print(grauImpar)
        if grauImpar > 2:
            print("Não é euleriano")
            return False
        elif grauImpar == 2:
            print("É semi-euleriano")
            return False
        else:
            print("É euleriano")
            return True

    def imprimir(self):
        print(self.grafo)