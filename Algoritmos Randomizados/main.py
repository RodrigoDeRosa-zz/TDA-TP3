# -*- coding: utf-8 -*-

from creadorArchivos import CreadorArchivos
from lectorArchivos import LectorArchivos
from graph import Graph
from karger import Karger

def main():
    #Se crean los archivos
    creador = CreadorArchivos()
    creador.crearArchivo(100)
    #Se lee un archivo y se crea el grafo
    lector = LectorArchivos()
    grafo = lector.initGrafo()
    #Se crea el objeto que resuelve el problema
    karger = Karger(grafo)
    #Se resuelve el problema
    minimumCut = karger.findMinimumCut()

    print minimumCut

main()
