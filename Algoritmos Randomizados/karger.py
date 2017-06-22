# -*- coding: utf-8 -*-

from graph import Graph
import copy
import random

class Karger():
    """
        Algoritmo randomizado de Karger para hallar cortes mínimos de un
        grafo conexo no dirigido.
    """
    def __init__(self, graph):
        self.graph = graph

    def findMinimumCut(self):
        """
            Devuelve una lista con las aristas que componen el corte mínimo
            del grafo.
        """
        #Se hace una copia del grafo original para modificarlo
        contractedGraph = copy.deepcopy(self.graph)

        #Se eliminan las aristas que unen a un vertice con él mismo
        contractedGraph.removeSelfEdges()
        #Se itera hasta que queden solo dos vertices
        while (len(contractedGraph) > 2):
            #Se elige una arista al azar
            randomEdge = random.choice(contractedGraph.getEdges())
            #Se obtienen los vertices que componen esa arista
            couple = contractedGraph.getEdge(randomEdge)
            #Se elimina la arista elegida al azar
            contractedGraph.removeEdge(randomEdge)
            #Se unen los vertices de la anterior arista. En caso de que alguna
            #arista resultante sea una selfEdge, es eliminada automaticamente
            contractedGraph.joinVertices(couple[0], couple[1])

        #Se obtienen las aristas que quedaron al final de la iteracion
        survivingEdges = contractedGraph.getEdges()
        minimumCut = []
        #A partir de las aristas obtenidas del grafo modificado, se obtienen las
        #aristas del grafo original, que representan el corte minimo
        for survivingEdge in survivingEdges:
            edge = self.graph.getEdge(survivingEdge)
            minimumCut.append( [edge[0], edge[1]] )

        return minimumCut
