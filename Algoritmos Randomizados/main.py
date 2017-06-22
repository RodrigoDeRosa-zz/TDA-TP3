# -*- coding: utf-8 -*-

from creadorArchivos import CreadorArchivos
from lectorArchivos import LectorArchivos
from graph import Graph
from karger import Karger

def main():
    #Se crean los archivos
    print "Creando archivo..."
    creador = CreadorArchivos()
    creador.crearArchivo(100)
    #Se lee un archivo y se crea el grafo
    print "Leyendo grafo..."
    lector = LectorArchivos()
    grafo = lector.initGrafo()

    #Se crea el objeto que resuelve el problema
    karger = Karger(grafo)
    #Se resuelve el problema
    print "Ejecutando algoritmo de Karger con un grafo de 100 vértices y 200 aristas..."
    minimumCut = karger.findMinimumCut()
    print "El corte mínimo obtenido por el algoritmo tiene " + str(len(minimumCut)) + " aristas." \
    + " Las cuales son:"
    for edge in minimumCut:
        print edge
    print "\n"

    respuesta = raw_input("Ejecutar el algoritmo muchas veces para disminuir la probabilidad de error?[ENTER = NO]")
    if not respuesta: return

    print "Ejecutando el algoritmo de Karger [(100C2)ln(100)] veces... \t (22796 veces)"
    bestMinCut = [0]*100
    for i in xrange(22795):
        minCut = karger.findMinimumCut()
        if len(minCut) < len(bestMinCut): bestMinCut = minCut
    print "El corte más pequeño obtenido tiene " + str(len(bestMinCut)) + " aristas. Las cuales son:"
    for edge in bestMinCut:
        print edge

main()
