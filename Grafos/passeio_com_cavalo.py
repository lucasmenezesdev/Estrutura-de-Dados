from grafo import Grafo

#Cria os vértices de um tabuleiro de xadrez 8x8 com a função "adicionarVertices"
def criarGrafo():
    grafo = adicionarVertices()
    #Verifica todas as casas vizinhas de cada casa do tabuleiro e adiciona em uma lista
    for vertice in grafo.getGrafo():
        listaPassos = []
        aresta1 = (vertice[0]-2, vertice[1]+1)
        aresta2 = (vertice[0]-1, vertice[1]+2)
        aresta3 = (vertice[0]+1, vertice[1]+2)
        aresta4 = (vertice[0]+2, vertice[1]+1)
        aresta5 = (vertice[0]-2, vertice[1]-1)
        aresta6 = (vertice[0]-1, vertice[1]-2)
        aresta7 = (vertice[0]+1, vertice[1]-2)
        aresta8 = (vertice[0]+2, vertice[1]-1)
        listaPassos.append(aresta1)
        listaPassos.append(aresta2)
        listaPassos.append(aresta3)
        listaPassos.append(aresta4)
        listaPassos.append(aresta5)
        listaPassos.append(aresta6)
        listaPassos.append(aresta7)
        listaPassos.append(aresta8)
        
        #Após verificar os casos, a lista passa por uma condicional para verificar se
        #cada elemento vai entrar ou não como vizinho do vértice.
        for aresta in listaPassos:
            if aresta[0] <= 8 and aresta[0] >= 1 and aresta[1] <= 8 and aresta[1] >= 1:
                grafo.addAresta(vertice, aresta)
    return grafo

def adicionarVertices():
    grafo = Grafo()
    linha = 1
    coluna = 1
    for vertice in range(64):
        if coluna == 9:
            coluna = 1
            linha += 1
        grafo.addVertice((coluna, linha))
        coluna += 1
    return grafo


#Implementação do algoritmo de busca em profundidade com uma modificação para que
#encontre um caminho em que a partir de uma casa do tabuleiro o cavalo passe em todas
#as casas sem repetir.
def busca(grafo, vertice):
    visitados = []
    def buscaRec(grafo, vertice):
        visitados.append(vertice)
        grau = 10
        arestaMenor = False
        for aresta in grafo[vertice]:
            if aresta not in visitados:
                if len(grafo[aresta]) < grau:
                    grau = len(grafo[aresta])
                    arestaMenor = aresta
        if arestaMenor != False:
            buscaRec(grafo, arestaMenor)
    buscaRec(grafo, vertice)
    print(visitados)


#Chamada para teste
grafo = criarGrafo()
grafo.imprimir()
busca(grafo.getGrafo(), (1, 1))