#!/usr/bin/env python3

# Maybe it would be a good idea to create a Particula class
# Maybe it would be a good idea to have already a variable that has the distancia 
# or method where returns the distance, I'm calculating the distance multiple times.

import pprint
import math
from collections import deque
from queue import PriorityQueue
from PySide2.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QGraphicsScene, QMessageBox, QPushButton
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from operator import itemgetter # I do not remember what is this for
import json

# Maybe this method should be in a class.
def calcDistEuclidiana(origenX, origenY, destinoX, destinoY):
    distancia = math.sqrt( (int(destinoX) - int(origenX))**2 + (int(destinoY) - int(origenY))**2)
    return int(distancia)

def getVelocidad(d):
    return d["velocidad"]

def getDistancia(d):
    return d["distancia"]

#####################################################################################

# For the moment, this class will have everything related about the graph representation.
# This is not correct, MainWindow only should do Ui things, not graphs things.
class MainWindow(QMainWindow):
    particulas = []

    # For the graph.
    grafo = dict()  # Non directed weighted.
    grafo2 = list() # Non directed weighted.
    isPrimActivate = False     # Flag that helps to push the same button and draw the new graph.
    isKruskalActivate = False  # Flag that helps to push the same button and draw the new graph.
    isDijkstraActivate = False # Flag that helps to push the same button and draw the new graph.

    destino = tuple()
    origen = tuple()
    aristaOrigenDestino = ()
    aristaDestinoOrigen = ()
    pila = deque()
    cola = deque()
    listaVisitados = list()
    priorityQueue = PriorityQueue()
    caminos = dict() # Arreglo de caminos para dijkstra.
    verticeDestino = tuple()

    dicOrigenOrigen = {}
    dicOrigenDestino = {}
    dicDestinoOrigen = {}
    dicDestinoDestino = {}

    minOrigenOrigen = 0
    minOrigenDestino = 0
    minDestinoOrigen = 0
    minDestinoDestino = 0

    isBtnVelocidadPressed = False
    isBtnDistanciaPressed = False
    isBtnPuntosCercanosPressed = False
    isBtnPuntosCercanosLimpiar = False
    isBtnMostrarPuntos = False 

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # To not modify the line edit.
        self.ui.lnEdtDistEucl.setReadOnly(True)

        # Graphicview
        self.scene = QGraphicsScene()
        self.sceneOrd = QGraphicsScene()
        self.scenePC = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)  # Set the scene, is blank,
        self.ui.graphicViewOrdenar.setScene(self.sceneOrd)
        self.ui.graphicsViewPuntosCercanos.setScene(self.scenePC)

        # Connecting slots.
        self.ui.btnEnviar.clicked.connect(self.enviar)
        self.ui.btnMostrar.clicked.connect(self.mostrarParticulas)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.btnMostrarTabla.clicked.connect(self.clickMostrarTabla)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnDibujar.clicked.connect(self.dibujar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnLimpiarPC.clicked.connect(self.limpiar)
        self.ui.btnVelocidad.clicked.connect(self.ordenarVelocidad)
        self.ui.btnDistancia.clicked.connect(self.ordenarDistancia)
        self.ui.btnMostrarOrd.clicked.connect(self.dibujar)
        self.ui.btnLimpiar_2.clicked.connect(self.limpiar)
        self.ui.btnMostrarPuntos.clicked.connect(self.dibujar)
        self.ui.btnMostrarPuntosCercanos.clicked.connect(self.dibujar)
        self.ui.btnMostrarGrafo.clicked.connect(self.mostrarGrafo)
        self.ui.btnRecorridoProfundidad.clicked.connect(self.recorridoProfundidad)
        self.ui.btnRecorridoAnchura.clicked.connect(self.recorridoAnchura)
        self.ui.btnPrim.clicked.connect(self.prim)
        self.ui.btnLimpiar_3.clicked.connect(self.limpiar)
        self.ui.btnKruskal.clicked.connect(self.kruskal)
        self.ui.btnDijkstra.clicked.connect(self.dijkstra)
        

    def __str__(self):
        pass
        # Placas 6 chars, Modelo 4 chars, marca 6 chars, km 5 chars
        #return "{0:6} {1:4} {2:6} {3:4}".format(self.placas, self.modelo, self.marca, self.km)

    # <
    def __lt__(self, other):
        pass
        #for particula in self.particulas:
        #    return particula["distancia"] < other.particula["distancia"]


    def wheelEvent(self, event):
        print(event.delta())  # El valor de la velocidad en la cual se giro la bola.
        if event.delta() > 0:
            self.ui.graphicsViewPuntosCercanos.scale(1.2, 1.2)
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsViewPuntosCercanos.scale(0.8, 0.8)
            self.ui.graphicsView.scale(0.8, 0.8)

    """Will show the graph representation of the particles as adjacency list in the QPlainTextEdit"""
    @Slot()
    def mostrarGrafo(self):
        # self.ui.plnTxtWdgtSalida.clear()
        msgBox = QMessageBox()
        primBtn = QPushButton()
        kruskalBtn = QPushButton()
        dijkstraBtn = QPushButton()
        abort = QPushButton()

        msgBox.setText("Seleccione sobre que algoritmo se construira el grafo")
        msgBox.setWindowTitle("Elegir algoritmo")
        primBtn = msgBox.addButton("Algoritmo Prim", QMessageBox.ActionRole)
        kruskalBtn = msgBox.addButton("Algoritmo Kruskal", QMessageBox.ActionRole)
        dijkstraBtn = msgBox.addButton("Algoritmo Dijkstra", QMessageBox.ActionRole)

        msgBox.exec()

        # Build a graph using the distance.
        if msgBox.clickedButton() == primBtn:
            for particula in self.particulas:
                distancia = calcDistEuclidiana(particula["origen"]["x"],
                                               particula["origen"]["y"],
                                               particula["destino"]["x"],
                                               particula["destino"]["y"])

                # Obtain origen and destino coordinates.
                for key, value in particula.items():
                    if key == "destino":
                        # Because value it's a dictionary, if we assign it directly to
                        # self.destino will become a dictionary, we don't want that.
                        # Obtain each value of the dic value and assign it.
                        self.destino = self.destino + (value["x"],)
                        self.destino = self.destino + (value["y"],)
                    
                        self.aristaOrigenDestino = (self.destino, distancia)
                    if key == "origen":
                        self.origen = self.origen + (value["x"],)
                        self.origen = self.origen + (value["y"],)
                        self.aristaDestinoOrigen = (self.origen, distancia)
                
                # Becase is a undirected weighted graph, we need to do two checks,
                # one to know if the origen it's in the graph and another one to know
                # if destino it's also in the graph, it's necessary to check destino
                # because it's an undirected weighted graph, origen-destino can be connected
                # as well destino-origen.
                if self.origen in self.grafo:
                    self.grafo[self.origen].append(self.aristaOrigenDestino)
                else:
                    self.grafo[self.origen] = [self.aristaOrigenDestino]

                if self.destino in self.grafo:
                    self.grafo[self.destino].append(self.aristaDestinoOrigen)
                else:
                    self.grafo[self.destino] = [self.aristaDestinoOrigen]

                self.origen = tuple()
                self.destino = tuple()

            str = pprint.pformat(self.grafo, width = 40, indent = 1)
            self.ui.plnTxtEdtGrafo.insertPlainText(str)

        # Building a graph using the speed.
        elif msgBox.clickedButton() == kruskalBtn:
            for particula in self.particulas:
                velocidad = particula["velocidad"]

                # Obtain origen and destino coordinates.
                for key, value in particula.items():
                    if key == "destino":
                        # Because value it's a dictionary, if we assign it directly to
                        # self.destino will become a dictionary, we don't want that.
                        # Obtain each value of the dic value and assign it.
                        self.destino = self.destino + (value["x"],)
                        self.destino = self.destino + (value["y"],)
                    
                        self.aristaOrigenDestino = (self.destino, velocidad)
                    if key == "origen":
                        self.origen = self.origen + (value["x"],)
                        self.origen = self.origen + (value["y"],)
                        self.aristaDestinoOrigen = (self.origen, velocidad)
                
                # Becase is a undirected weighted graph, we need to do two checks,
                # one to know if the origen it's in the graph and another one to know
                # if destino it's also in the graph, it's necessary to check destino
                # because it's an undirected weighted graph, origen-destino can be connected
                # as well destino-origen.
                if self.origen in self.grafo:
                    self.grafo[self.origen].append(self.aristaOrigenDestino)
                else:
                    self.grafo[self.origen] = [self.aristaOrigenDestino]

                if self.destino in self.grafo:
                    self.grafo[self.destino].append(self.aristaDestinoOrigen)
                else:
                    self.grafo[self.destino] = [self.aristaDestinoOrigen]

                self.origen = tuple()
                self.destino = tuple()

            str = pprint.pformat(self.grafo, width = 40, indent = 1)
            self.ui.plnTxtEdtGrafo.insertPlainText(str)
        # Build a directed graph.
        elif msgBox.clickedButton() == dijkstraBtn:
            for particula in self.particulas:
                distancia = calcDistEuclidiana(particula["origen"]["x"],
                                               particula["origen"]["y"],
                                               particula["destino"]["x"],
                                               particula["destino"]["y"])

                # Obtain origen and destino coordinates.
                for key, value in particula.items():
                    if key == "destino":
                        # Because value it's a dictionary, if we assign it directly to
                        # self.destino will become a dictionary, we don't want that.
                        # Obtain each value of the dic value and assign it.
                        self.destino = self.destino + (value["x"],)
                        self.destino = self.destino + (value["y"],)
                    
                        self.aristaOrigenDestino = (self.destino, distancia)
                    if key == "origen":
                        self.origen = self.origen + (value["x"],)
                        self.origen = self.origen + (value["y"],)
                        self.aristaDestinoOrigen = (self.origen, distancia)
                
                # Becase is a undirected weighted graph, we need to do two checks,
                # one to know if the origen it's in the graph and another one to know
                # if destino it's also in the graph, it's necessary to check destino
                # because it's an undirected weighted graph, origen-destino can be connected
                # as well destino-origen.
                if self.origen in self.grafo:
                    self.grafo[self.origen].append(self.aristaOrigenDestino)
                else:
                    self.grafo[self.origen] = [self.aristaOrigenDestino]

                if self.destino in self.grafo:
                    self.grafo[self.destino].append(self.aristaDestinoOrigen)
                else:
                    self.grafo[self.destino] = [self.aristaDestinoOrigen]

                self.origen = tuple()
                self.destino = tuple()

            str = pprint.pformat(self.grafo, width = 40, indent = 1)
            self.ui.plnTxtEdtGrafo.insertPlainText(str)


    # Maybe this method should be in a class Graph.
    """Will do the kruskal's algorithm"""
    @Slot()
    def kruskal(self):
        self.isKruskalActivate = True
        self.isPrimActivate = False
        listaVerticesOrdenada = list()

        # Create a disjoint set with n vertices.
        disjointSet = [[] for i in range(0, len(self.grafo.keys()))]

        if self.ui.lnEdtOrigX.text() == "" and self.ui.lnEdtDestY.text() == "":
            QMessageBox.critical(self, "ERROR", "Ingrese el vertice origen")
        else:
            # Obtain line edit values.
            origenX = int(self.ui.lnEdtOrigX.text())
            origenY = int(self.ui.lnEdtOrigY.text())

            verticeOrigen = (origenX, origenY)
            print("Vertice origen: ", verticeOrigen)

            if verticeOrigen in self.grafo:
                # Iterate through our graph to get our origin, destination, speed.
                for key, value in self.grafo.items():
                    longitudDestinos = len(value) # We can have n destinations, get how many we have. 
                    i = 0

                    # To get all the destinations.
                    while longitudDestinos:
                        velocidad = value[i][1]
                        origen = key
                        destino = value[i][0]

                        arista = (velocidad, (origen, destino))
                        print("arista: ", arista)

                        # Append to our list our vertex with this format (velocidad, (origen, destino))
                        listaVerticesOrdenada.append(arista)

                        longitudDestinos = longitudDestinos - 1
                        i = i + 1

                # Sort our list in descending order.
                listaVerticesOrdenada.sort(reverse=True)
                print("")
                
                # Do make-set, each vertex in our graph is inside a list.
                # Having this [[vertex], [vertex], [vertex], ..., [vertex]]
                i = 0
                for key in self.grafo.keys():
                    disjointSet[i].append(key)
                    i = i + 1
                print("disjoint set: ", disjointSet)

                # While my listaVerticesOrdenada is not empty.
                while len(listaVerticesOrdenada) != 0:
                    # Take the edge with the greater speed and remove it from our list.
                    aristaMayor = listaVerticesOrdenada.pop(0)
                    print("arsita mayor: ", aristaMayor)

                    origen = aristaMayor[1][0]
                    destino = aristaMayor[1][1]

                    # Iterate through our disjointSet.
                    for i in range(len(disjointSet)):
                        if origen in disjointSet[i] or destino in disjointSet[i]:
                            if destino not in disjointSet[i]:
                                for j in range(len(disjointSet)):
                                    if destino in disjointSet[j]:
                                        # Add our edge to our graph.
                                        self.grafo2.append(aristaMayor)

                                        # Union between destino and origen.
                                        disjointSet[i] = disjointSet[i] + disjointSet[j]
                                        # Once we did the union, just clear our destino.
                                        disjointSet[j].clear()
                                        print("disjoint set: ", disjointSet)
                                        break
                print("grafo 2: ", self.grafo2)                    

            else:
                QMessageBox.critical(self, "ERROR", "No se encontro el vertice origen")


    # Maybe this method should be in a class Graph.
    """Will do the prim's algorithm"""
    @Slot()
    def prim(self):
        self.isPrimActivate = True
        self.isKruskalActivate = False
        if self.ui.lnEdtOrigX.text() == "" and self.ui.lnEdtDestY.text() == "":
            QMessageBox.critical(self, "ERROR", "Ingrese el vertice origen")
        else:
            # Obtain line edit values.
            origenX = int(self.ui.lnEdtOrigX.text())
            origenY = int(self.ui.lnEdtOrigY.text())

            verticeOrigen = (origenX, origenY)
            print("Vertice origen: ", verticeOrigen)

            # Take the initial vertex and append it to our listaVisitados.
            self.listaVisitados.append(verticeOrigen)

            if verticeOrigen in self.grafo:
                # Get all the adjacents from our verticeOrigen and add them to our priority queue.
                for key, value in self.grafo.items():
                    if verticeOrigen == key:
                        nAjacentVertex = len(value)
                        i = 0

                        # While there are adjacents vertices. 
                        while nAjacentVertex:
                            # Get the correct values.
                            distancia = value[i][1]
                            origen = key
                            destino = value[i][0]

                            arista = (distancia, (origen, destino))
                            self.priorityQueue.put(arista)

                            nAjacentVertex = nAjacentVertex - 1
                            i = i + 1

                # While our priority queue is not empty.
                while not self.priorityQueue.empty():
                    print("Lista de visitados: ", self.listaVisitados)
                    # Get that edge with the minimum distance from our priority queue and
                    # delete it.
                    arista = self.priorityQueue.get()
                    destino = arista[1][1]
                    print("Arista eliminada: ", arista)
                    print("destino: ", destino)

                    # If destino is not in our listaVisitados.
                    if destino not in self.listaVisitados:
                        # Append our destino to our listaVisitados.
                        self.listaVisitados.append(destino)
                        
                        # Add the edge to the resultant graph.
                        self.grafo2.append(arista)

                        # Get all the adjacents from our destino and add them to our priority queue.
                        for key, value in self.grafo.items():
                            print("destino cambiante: ", destino)
                            print("key ", key)
                            if destino == key:
                                nAjacentVertex = len(value)
                                i = 0

                                # While there are adjacents vertices. 
                                while nAjacentVertex:
                                    # Get the correct values.
                                    distancia = value[i][1]
                                    origen = key
                                    destino2= value[i][0]

                                    print("nueva distancia: ", distancia)
                                    print("nuev origen: ", origen)
                                    print("nuevo destino: ", destino2)

                                    arista = (distancia, (origen, destino2))
                                    print("arista a agregar: ", arista)
                                    self.priorityQueue.put(arista)

                                    nAjacentVertex = nAjacentVertex - 1
                                    i = i + 1

                print("Lista de visitados: ", self.listaVisitados)
                print("Grafo 2: ", self.grafo2)
            else:
                QMessageBox.critical(self, "ERROR", "No se encontro el vertice origen")

    # Maybe this method should be in a class Graph.
    """Will do the Dijkstra algorithm, shortest path"""
    @Slot()
    def dijkstra(self):
        self.isDijkstraActivate = True
        self.isPrimActivate = False
        self.isKruskalActivate = False

        # Arreglar.
        if (self.ui.lnEdtOrigX.text() == "" and self.ui.lnEdtDestY.text() == "") and (self.ui.lnEdtDestX.text() == "" and self.ui.lnEdtDestY.text() == ""):
            QMessageBox.critical(self, "ERROR", "Ingrese el vertice origen/destino")
        else:
            distancias = dict()
            self.caminos = dict()
            distanciaTotal = 0
            
            # Obtain line edit values.
            origenX = int(self.ui.lnEdtOrigX.text())
            origenY = int(self.ui.lnEdtOrigY.text())
            destinoX = int(self.ui.lnEdtDestX.text())
            destinoY = int(self.ui.lnEdtDestY.text())

            verticeOrigen = (origenX, origenY)
            self.verticeDestino = (destinoX, destinoY)
            print("Vertice origen: ", verticeOrigen)
            print("Vertice destino: ", self.verticeDestino)
            print("")

            if verticeOrigen and self.verticeDestino in self.grafo:
                distancias[verticeOrigen] = 0
                self.caminos[verticeOrigen] = ""

                # Add our vertices to our distancias and self.caminos, only the origin vertex has distance 0
                # and camino ""
                # other ones have a big value, simulating inf and self.caminos "-"
                for keys in self.grafo.keys():
                    if verticeOrigen != keys:
                        distancias[keys] = 1000000
                        self.caminos[keys] = ""

                # Add our verticeOrigen with distance 0 to our priority queue.
                self.priorityQueue.put((0,verticeOrigen))

                # If our priority queue is not empty.
                while not self.priorityQueue.empty():
                    # Get the vertex with our minimum distance.
                    nodo = self.priorityQueue.get()
                    # print("minimo de la cola de prioridad: ", nodo)
                    # Obtain only our vertex.
                    verticePadre = nodo[1]
                    distanciaVertPadre = nodo[0]

                    # Get all the adjacents from our vertice padre.
                    for key, value in self.grafo.items():
                        # print("key ", key)

                        if verticePadre == key:
                            # Our vertex can have n adjacent vertices.
                            nAjacentVertex = len(value)
                            i = 0

                            # While there are adjacents vertices. 
                            while nAjacentVertex:
                                # Get the correct values.
                                distancia = value[i][1]
                                verticeAdjacente = value[i][0]

                                # For each vertex that is connected.
                                for vertice, dist in distancias.items():
                                    # Add the distance from our destination.                                    
                                    if verticeAdjacente == vertice:
                                        distanciaTotal = distancia + distanciaVertPadre 
                                    # If our distancia total is less than the distance that our vertex has.
                                    if vertice == verticeAdjacente and distanciaTotal < dist:
                                        # Add our new distance to our dictionary.
                                        distancias[vertice] = distanciaTotal

                                        # Add to our self.caminos dictionary our verticePadre 
                                        for key in self.caminos.keys():
                                            if key == vertice:
                                                # print("este es el vertice padreeee: ", verticePadre)
                                                self.caminos[key] = verticePadre
                                                break
                                        self.priorityQueue.put((distanciaTotal, vertice))
                                        distanciaTotal = 0
                                        break
                                nAjacentVertex = nAjacentVertex - 1
                                i = i + 1
                print("")
                str = pprint.pformat(distancias, width = 40, indent = 1)
                print("arreglo de distancias: ", str)
                print("")
                str2 = pprint.pformat(self.caminos, width = 40, indent = 1)
                print("arreglo de self.caminos: ", str2)
            else:
                QMessageBox.critical(self, "ERROR", "No se encontro el vertice origen/destino")

    # Maybe this method should be in a class Graph.
    """Will do depth first search to our particles graph"""
    @Slot()
    def recorridoProfundidad(self):
        # self.ui.plnTxtEdtGrafo.clear()
        self.listaVisitados.clear()

        if self.ui.lnEdtOrigX.text() == "" and self.ui.lnEdtDestY.text() == "":
            QMessageBox.critical(self, "ERROR", "Ingrese el vertice destino")
        else:
            # Obtain line edit values.
            origenX = int(self.ui.lnEdtOrigX.text())
            origenY = int(self.ui.lnEdtOrigY.text())

            verticeActual = tuple()

            verticeOrigen = (origenX, origenY)
            print("Vertice origen: ", verticeOrigen)

            # Append verticeOrigen to the stack.
            self.pila.append(verticeOrigen)

            if verticeOrigen in self.grafo:
                while len(self.pila) > 0:
                    # print("pila: ", self.pila)
                    verticeActual = self.pila.pop()
                    # print("vertice actual: ", verticeActual)
                    # print()

                    # If the verticeActual has not been visited.
                    if verticeActual not in self.listaVisitados:
                        # print("el vertice actual no esta en la lista de visitados")
                        # We put in our listaVisitados our verticeActual
                        self.listaVisitados.append(verticeActual)
                        # print("lista de visitados: ", self.listaVisitados)
                        # print()

                        for origen, destino in self.grafo.items():
                            # print("vertice origen: ", origen)
                            # print("vertice destino: ", destino)
                            if origen == verticeActual:
                                # Because our destino is a list of tuples, I only want to retrieve
                                # the vertice destino, not its weight, that's why [0].
                                for elem in destino:
                                    self.pila.append(elem[0])
                str = pprint.pformat(self.listaVisitados, width = 40, indent = 1)
                print("Profundidad")
                print(str) 
                # self.ui.plnTxtEdtGrafo.insertPlainText(str)
            else:
                QMessageBox.critical(self, "ERROR", "No se encontro el vertice origen/destino")
                # Clean the stack to not have the origin wrong vertex.
                self.pila.clear()

    # This should be a method from graph class.
    """Will do Breadth first search to our particles graph"""
    @Slot()
    def recorridoAnchura(self):
        # self.ui.plnTxtEdtGrafo.clear()
        self.listaVisitados.clear()
        
        if self.ui.lnEdtOrigX.text() == "" and self.ui.lnEdtDestY.text() == "":
            QMessageBox.critical(self, "ERROR", "Ingrese el vertice destino")
        else:
            # Obtain line edit values.
            origenX = int(self.ui.lnEdtOrigX.text())
            origenY = int(self.ui.lnEdtOrigY.text())

            verticeOrigen = (origenX, origenY)
            print("Vertice origen: ", verticeOrigen)

            # Append verticeOrigen to our queue.
            self.cola.append(verticeOrigen)

            if verticeOrigen in self.grafo:
                while len(self.cola) > 0:
                    verticeActual = self.cola.popleft()

                    # if the verticeActual has not been visited.
                    if verticeActual not in self.listaVisitados:
                        self.listaVisitados.append(verticeActual)

                        for origen, destino in self.grafo.items():
                            if origen == verticeActual:
                                # Because our destino is a list of tuples, I only want to 
                                # retrieve the vertice destino, no tis weight, that's why [0]
                                for elem in destino:
                                    self.cola.append(elem[0])
                str = pprint.pformat(self.listaVisitados, width = 40, indent = 1)
                print("Anchura")
                print(str)
            else:
                QMessageBox.critical(self, "ERROR", "No se encontro el vertice origen")
                # Clean the queue to not have the origin wrong vertex.
                self.cola.clear()


        
    """Will draw all the particles graphically"""
    @Slot()
    def dibujar(self):
        # Ancho de la pluma.
        penWidth = 3
        pen = QPen()
        pen.setWidth(penWidth)

        # To see what is the current tab selected.
        if self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()) == "Grafica":
            # To draw the new graph with red.
            if self.isPrimActivate == True:
                self.isKruskalActivate = False
                print("dibujando prim")
                r = 255
                g = 0
                b = 0
                color = QColor(r, g, b)
                pen.setColor(color)

                # Our new graph is a list of tuples with this format (distance, (origin, destination))
                # We want our origin and destination.
                for particula in self.grafo2:
                    print(particula)

                    # At this point origen will be (origin, destination), now we obtain each value 
                    # individually.
                    origen = particula[1][0]
                    origenX = origen[0]
                    origenY = origen[1]

                    # At this point destino will be (origin, destination), now we obtain each value 
                    # individually.
                    destino = particula[1][1]
                    destinoX = destino[0]
                    destinoY = destino[1]

                    # Dibujando circulos.
                    self.scene.addEllipse(origenX,
                                          origenY,
                                          6, 6, pen)
                    self.scene.addEllipse(destinoX,
                                          destinoY,
                                          6, 6, pen)

                    # Con +3 estará en el centro.
                    self.scene.addLine(origenX + 3,
                                       origenY + 3,
                                       destinoX + 3,
                                       destinoY  + 3, pen)
            # To draw the new graph with yellow.
            elif self.isKruskalActivate == True:
                self.isPrimActivate = False
                print("dibujando kruskal")
                r = 255
                g = 255
                b = 0
                color = QColor(r, g, b)
                pen.setColor(color)

                # Our new graph is a list of tuples with this format (speed, (origin, destination))
                # We want our origin and destination.
                for particula in self.grafo2:
                    print(particula)

                    # At this point origen will be (origin, destination), now we obtain each value 
                    # individually.
                    origen = particula[1][0]
                    origenX = origen[0]
                    origenY = origen[1]

                    # At this point destino will be (origin, destination), now we obtain each value 
                    # individually.
                    destino = particula[1][1]
                    destinoX = destino[0]
                    destinoY = destino[1]

                    # Dibujando circulos.
                    self.scene.addEllipse(origenX,
                                          origenY,
                                          6, 6, pen)
                    self.scene.addEllipse(destinoX,
                                          destinoY,
                                          6, 6, pen)

                    # Con +3 estará en el centro.
                    self.scene.addLine(origenX + 3,
                                       origenY + 3,
                                       destinoX + 3,
                                       destinoY  + 3, pen)
            # Will draw the shortest path using blue color.
            elif self.isDijkstraActivate == True:
                self.scene.clear()
                print("dgridLayoutijkstra")
                r = 0
                g = 255
                b = 0
                color = QColor(r, g, b)
                pen.setColor(color)

                # for vertice in self.caminos:
                print()
                print("verticeeeee: ", self.caminos)
                print("vertice destino: ", self.verticeDestino)

                while self.verticeDestino != '':
                    for destino, padre in self.caminos.items():
                        print("destino: ", destino)
                        if destino == '':
                            break
                        elif self.verticeDestino == destino:
                            destX = destino[0]
                            destY = destino[1]
                            print("destx: ", destX)
                            print("desty: ", destY)

                            fatherX = padre[0]
                            fatherY = padre[1]
                            print("fatherx: ", fatherX)
                            print("fathery: ", fatherY)


                            # Dibujando Circulos.
                            self.scene.addEllipse(destX,
                                                  destY,
                                                  6, 6, pen)
                            self.scene.addEllipse(fatherX,
                                                  fatherY,
                                                  6, 6, pen)

                            # Con +3 estará en el centro.
                            self.scene.addLine(destX + 3,
                                               destY + 3,
                                               fatherX + 3,
                                               fatherY  + 3, pen)
                            self.verticeDestino = padre
                            print("self vertice destino: ", self.verticeDestino)
                            break;
            else:
                print("grafica")
                for particula in self.particulas:
                    r = particula["color"]["red"]
                    g = particula["color"]["green"]
                    b = particula["color"]["blue"]
                    color = QColor(r, g, b)
                    pen.setColor(color)

                    # Dibujando circulos.
                    self.scene.addEllipse(particula["origen"]["x"],
                                          particula["origen"]["y"],
                                          6, 6, pen)
                    self.scene.addEllipse(particula["destino"]["x"],
                                          particula["destino"]["y"],
                                          6, 6, pen)

                    # Con +3 estará en el centro.
                    self.scene.addLine(particula["origen"]["x"] + 3,
                                       particula["origen"]["y"] + 3,
                                       particula["destino"]["x"] + 3,
                                       particula["destino"]["y"] + 3, pen)
        elif self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()) == "Ordenamiento":
                j = 0
                print("ordenamiento")
                if self.isBtnDistanciaPressed == False and self.isBtnVelocidadPressed == False:
                    for particula in self.particulas:
                        r = particula["color"]["red"]
                        g = particula["color"]["green"]
                        b = particula["color"]["blue"]
                        color = QColor(r, g, b)
                        pen.setColor(color)

                        # j it's here because we want to increment y position, if you
                        # don't increment it, the lines will be on top of each other.
                        self.sceneOrd.addLine(0, j, particula["velocidad"],j, pen)

                        # To have a rational space between lines, we increment depending
                        # of the pen size.
                        j = j + penWidth 
                    j = 0
                if self.isBtnVelocidadPressed == True:
                    for particula in self.particulas:
                        distanciaP = calcDistEuclidiana(particula["origen"]["x"],
                                                       particula["origen"]["y"],
                                                       particula["destino"]["x"],
                                                       particula["destino"]["y"])
                        particula["distancia"] = distanciaP
                    # self.particulas.sort(key=getVelocidad)
                    
                    for particula in self.particulas:
                        r = particula["color"]["red"]
                        g = particula["color"]["green"]
                        b = particula["color"]["blue"]
                        color = QColor(r, g, b)
                        pen.setColor(color)

                        # j it's here because we want to increment y position, if you
                        # don't increment it, the lines will be on top of each other.
                        self.sceneOrd.addLine(0, j, particula["distancia"],j, pen)

                        # To have a rational space between lines, we increment depending
                        # of the pen size.
                        j = j + penWidth 
                        del particula["distancia"]
                    j = 0
                if self.isBtnDistanciaPressed == True:
                    for particula in self.particulas:
                        distanciaP = calcDistEuclidiana(particula["origen"]["x"],
                                                       particula["origen"]["y"],
                                                       particula["destino"]["x"],
                                                       particula["destino"]["y"])
                        particula["distancia"] = distanciaP
                    # self.particulas.sort(reverse=True, key=getDistancia)
                    
                    for particula in self.particulas:
                        r = particula["color"]["red"]
                        g = particula["color"]["green"]
                        b = particula["color"]["blue"]
                        color = QColor(r, g, b)
                        pen.setColor(color)

                        # j it's here because we want to increment y position, if you
                        # don't increment it, the lines will be on top of each other.
                        self.sceneOrd.addLine(0, j, particula["distancia"],j, pen)

                        # To have a rational space between lines, we increment depending
                        # of the pen size.
                        j = j + penWidth 
                        del particula["distancia"]
                    j = 0
        elif self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()) == "Puntos Cercanos":
            if self.isBtnPuntosCercanosPressed == False: 
                # self.isBtnMostrarPuntos = True 
                self.isBtnPuntosCercanosPressed = True
                # print(self.mostrarPuntosCercanos())
                #print(self.mostrarPuntosCercanos())
                print("Mostrando puntos")
                penWidth = 2
                pen = QPen()
                pen.setWidth(penWidth)
                for particula in self.particulas:
                    r = particula["color"]["red"]
                    g = particula["color"]["green"]
                    b = particula["color"]["blue"]
                    color = QColor(r, g, b)

                    # Dibujando cuadrados.
                    self.scenePC.addEllipse(particula["origen"]["x"],
                                          particula["origen"]["y"],
                                          6, 6, pen, color)
                    self.scenePC.addEllipse(particula["destino"]["x"],
                                          particula["destino"]["y"],
                                          6, 6, pen, color)
            if self.isBtnPuntosCercanosPressed == True:
                print("Mostrando los puntos cercanos")
                self.mostrarPuntosCercanos()
                penWidth = 2
                pen = QPen()
                pen.setWidth(penWidth)
                for particula in self.particulas:
                    r = particula["color"]["red"]
                    g = particula["color"]["green"]
                    b = particula["color"]["blue"]
                    color = QColor(r, g, b)
                    pen.setColor(color)

                    # Dibujando cuadrados.
                    self.scenePC.addEllipse(particula["origen"]["x"],
                                          particula["origen"]["y"],
                                          6, 6, pen, color)
                    self.scenePC.addEllipse(particula["destino"]["x"],
                                          particula["destino"]["y"],
                                          6, 6, pen, color)

    """Mostrar los puntos mas cercanos usando fuerza bruta, la manera en como los analiza
       es usando dicionarios, calculando las distancias de origen-origen, origen-destino,
       destino-origen, destino-destino, pues cada punto o es un origen o un destino"""
    @Slot()
    def mostrarPuntosCercanos(self):
        penWidth = 5
        pen = QPen()
        pen.setWidth(penWidth)

        for part in self.particulas:
            print("Particula dentro del for: ", part)
            for particula in self.particulas:
                print("Particula del for anidado:", particula)
                distanciaOrigenOrigen = calcDistEuclidiana(part["origen"]["x"],
                                                part["origen"]["y"],
                                                particula["origen"]["x"],
                                                particula["origen"]["y"])
                distanciaOrigenDestino = calcDistEuclidiana(part["origen"]["x"],
                                                part["origen"]["y"],
                                                particula["destino"]["x"],
                                                particula["destino"]["y"])
                distanciaDestinoDestino= calcDistEuclidiana(part["destino"]["x"],
                                                part["destino"]["y"],
                                                particula["destino"]["x"],
                                                particula["destino"]["y"])
                distanciaDestinoOrigen= calcDistEuclidiana(part["destino"]["x"],
                                                part["destino"]["y"],
                                                particula["origen"]["x"],
                                                particula["origen"]["y"])
                print("origen origen: ", distanciaOrigenOrigen)
                print("origen destino: ", distanciaOrigenDestino)
                print("desitno origen: ", distanciaDestinoOrigen)
                print("destino destino: ", distanciaDestinoDestino)

                # Each dictionary will have {distance:particle}
                self.dicOrigenOrigen[distanciaOrigenOrigen] = particula
                self.dicOrigenDestino[distanciaOrigenDestino] = particula
                self.dicDestinoOrigen[distanciaDestinoOrigen] = particula
                self.dicDestinoDestino[distanciaDestinoDestino] = particula

                print("dic origen origen", self.dicOrigenOrigen)
                print("dic origen destino", self.dicOrigenDestino)
                print("dic destino origen", self.dicDestinoOrigen)
                print("dic destino destino", self.dicDestinoDestino)

                # There is a case, where two points (origen-destino, destino-origen) their distance it's
                # 0, this it's because one point it's above one another. The problem it's when I'm obtaining
                # the minimum distance, because of this, the program doesn't draw anything, so...
                # Just delete the key value 0.0 from the dictionary to not get the min value 0. Again, this is
                # not efficient because I add the 0.0 before and I delete 0.0 right know, doing two operations,
                # that depends of how many iterations I will do, INEFFICIENT.
                if distanciaOrigenDestino == 0.0:
                    del self.dicOrigenDestino[0.0]
                if distanciaDestinoOrigen == 0.0:
                    del self.dicDestinoOrigen[0.0]
                
            # If you don't delete 0, it will take it as the min distance and will not draw nothing
            # because, well it's zero. 
            del self.dicOrigenOrigen[0.0]
            del self.dicDestinoDestino[0.0]

            # Get the minimum distance from each point.
            self.minOrigenOrigen = min(self.dicOrigenOrigen.keys())
            self.minOrigenDestino = min(self.dicOrigenDestino.keys())
            self.minDestinoOrigen = min(self.dicDestinoOrigen.keys())
            self.minDestinoDestino= min(self.dicDestinoDestino.keys())

            print("minOrigenOrigen: ", self.minOrigenOrigen)
            print("minOrigenDestino: ", self.minOrigenDestino)
            print("minDestinoOrigen: ", self.minDestinoOrigen)
            print("minDestinoDestino: ", self.minDestinoDestino)

            # Origen-origen
            if self.minOrigenOrigen < self.minOrigenDestino:
                r = part["color"]["red"]
                g = part["color"]["green"]
                b = part["color"]["blue"]
                color = QColor(r, g, b)
                pen.setColor(color)

                self.scenePC.addLine(part["origen"]["x"] + 3,
                                     part["origen"]["y"] + 3,
                                     self.dicOrigenOrigen[self.minOrigenOrigen]["origen"]["x"] + 3,
                                     self.dicOrigenOrigen[self.minOrigenOrigen]["origen"]["y"] + 3, color)

            # Origen-destino
            else:
                r = part["color"]["red"]
                g = part["color"]["green"]
                b = part["color"]["blue"]
                color = QColor(r, g, b)
                pen.setColor(color)

                self.scenePC.addLine(part["origen"]["x"] + 3,
                                     part["origen"]["y"] + 3,
                                     self.dicOrigenDestino[self.minOrigenDestino]["destino"]["x"] + 3,
                                     self.dicOrigenDestino[self.minOrigenDestino]["destino"]["y"] + 3, color)
                

            # Destino-origen
            if self.minDestinoOrigen < self.minDestinoDestino:
                r = part["color"]["red"]
                g = part["color"]["green"]
                b = part["color"]["blue"]
                color = QColor(r, g, b)
                pen.setColor(color)

                self.scenePC.addLine(part["destino"]["x"] + 3,
                                     part["destino"]["y"] + 3,
                                     self.dicDestinoOrigen[self.minDestinoOrigen]["origen"]["x"] + 3,
                                     self.dicDestinoOrigen[self.minDestinoOrigen]["origen"]["y"] + 3, color)

            # Destino-destino
            else:
                r = part["color"]["red"]
                g = part["color"]["green"]
                b = part["color"]["blue"]
                color = QColor(r, g, b)
                pen.setColor(color)

                self.scenePC.addLine(part["destino"]["x"] + 3,
                                     part["destino"]["y"] + 3,
                                     self.dicDestinoDestino[self.minDestinoDestino]["destino"]["x"] + 3,
                                     self.dicDestinoDestino[self.minDestinoDestino]["destino"]["y"] + 3, color)

            # Cleaning the dictionaries, we don't want the previous values for the next points.
            self.dicOrigenOrigen.clear()
            self.dicOrigenDestino.clear()
            self.dicDestinoDestino.clear()
            self.dicDestinoOrigen.clear()

    """Will sort by speed, but will draw by dstance"""
    @Slot()
    def ordenarVelocidad(self):
        self.isBtnVelocidadPressed = True
        self.isBtnDistanciaPressed= False
        self.sceneOrd.clear()
        print("Particulas ordenadas de manera ascendente\n")
        self.particulas.sort(key=getVelocidad)

        for particulas in self.particulas:
            print(particulas)

        self.dibujar()

    """Will sort by distance"""
    @Slot()
    def ordenarDistancia(self):
        self.isBtnDistanciaPressed = True
        self.isBtnVelocidadPressed= False
        self.sceneOrd.clear()
        print("Particulas ordenadas de manera descendente\n")
        for particula in self.particulas:
            distanciaP = calcDistEuclidiana(particula["origen"]["x"],
                                           particula["origen"]["y"],
                                           particula["destino"]["x"],
                                           particula["destino"]["y"])
            particula["distancia"] = distanciaP

        self.particulas.sort(reverse=True, key=getDistancia)
        for particula in self.particulas:
            distanciaP = calcDistEuclidiana(particula["origen"]["x"],
                                           particula["origen"]["y"],
                                           particula["destino"]["x"],
                                           particula["destino"]["y"])
            del particula["distancia"]
            print(particula)
            print("Distancia de la particula", distanciaP)
        self.dibujar()
            
    @Slot()
    def limpiar(self):
        if self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()) == "Grafica":
            self.scene.clear()
            self.isPrimActivate = False
            self.isKruskalActivate = False
            self.isDijkstraActivate = False
        elif self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()) == "Ordenamiento":
            self.sceneOrd.clear()
        elif self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()) == "Puntos Cercanos":
            self.scenePC.clear()
        elif self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()) == "Grafos":
            # self.isPrimActivate = False
            self.ui.plnTxtEdtGrafo.clear()
            self.listaVisitados.clear()
            self.grafo2.clear()
            self.grafo.clear()
            self.priorityQueue = PriorityQueue()

        self.dicOrigenOrigen.clear()
        self.dicOrigenDestino.clear()
        self.dicDestinoDestino.clear()
        self.dicDestinoOrigen.clear()
        self.ui.graphicsView.setTransform(QTransform())
        self.ui.graphicsViewPuntosCercanos.setTransform(QTransform())

    @Slot()
    def buscar(self):
        particulas = []
        id = int(self.ui.lnEdtBuscar.text())

        for particula in self.particulas:
            if id == particula["id"]:
                particulas.append(particula)

        # There is not book.
        if len(particulas) == 0:
            QMessageBox.critical(self, "Particulas", "NO se encontro la particula")
        else:
            self.particulasTabla(particulas)

        self.ui.lnEdtBuscar.clear()

    @Slot()
    def clickMostrarTabla(self):
        self.particulasTabla(self.particulas)

    def particulasTabla(self, particulas):
        self.ui.tblWdgtTabla.clear()
        self.ui.tblWdgtTabla.setColumnCount(10)             # How many columns we need.
        self.ui.tblWdgtTabla.setRowCount(len(particulas))   # How many particles we have.

        labels = ["ID", "Origen x", "Origen y", "Destino x", "Destino y", "Velocidad",
                  "R", "G", "B", "Distancia"]
        self.ui.tblWdgtTabla.setHorizontalHeaderLabels(labels)

        row = 0 # This variable will help us to know in which row we are.
        for particula in particulas:
            distanciaP = calcDistEuclidiana(particula["origen"]["x"],
                                           particula["origen"]["y"],
                                           particula["destino"]["x"],
                                           particula["destino"]["y"])

            id = QTableWidgetItem(str(particula["id"]))
            origenX = QTableWidgetItem(str(particula["origen"]["x"]))
            origenY = QTableWidgetItem(str(particula["origen"]["y"]))
            destinoX = QTableWidgetItem(str(particula["destino"]["x"]))
            destinoY = QTableWidgetItem(str(particula["destino"]["y"]))
            velocidad = QTableWidgetItem(str(particula["velocidad"]))
            colorR = QTableWidgetItem(str(particula["color"]["red"]))
            colorG = QTableWidgetItem(str(particula["color"]["green"]))
            colorB = QTableWidgetItem(str(particula["color"]["blue"]))
            distancia = QTableWidgetItem(str(round(distanciaP, 3)))

            self.ui.tblWdgtTabla.setItem(row, 0, id)
            self.ui.tblWdgtTabla.setItem(row, 1, origenX)
            self.ui.tblWdgtTabla.setItem(row, 2, origenY)
            self.ui.tblWdgtTabla.setItem(row, 3, destinoX)
            self.ui.tblWdgtTabla.setItem(row, 4, destinoY)
            self.ui.tblWdgtTabla.setItem(row, 5, velocidad)
            self.ui.tblWdgtTabla.setItem(row, 6, colorR)
            self.ui.tblWdgtTabla.setItem(row, 7, colorG)
            self.ui.tblWdgtTabla.setItem(row, 8, colorB)
            self.ui.tblWdgtTabla.setItem(row, 9, distancia)

            row += 1

    @Slot()
    def enviar(self):
        # Get data.
        id = int(self.ui.lnEdtID.text())
        origenX = int(self.ui.lnEdtOrigX.text())
        origenY = int(self.ui.lnEdtOrigY.text())
        destinoX = int(self.ui.lnEdtDestX.text())
        destinoY = int(self.ui.lnEdtDestY.text())
        velocidad = float(self.ui.lnEdtVel.text())
        colorR = int(self.ui.spBxR.value())
        colorG = int(self.ui.spBxG.value())
        colorB = int(self.ui.spBxB.value())

        distancia = calcDistEuclidiana(origenX, origenY, destinoX, destinoY)
        self.ui.lnEdtDistEucl.setText(str(round(distancia, 3)))

        origen = {
            "y": origenY,
            "x": origenX,
        }

        destino = {
            "y": destinoY,
            "x": destinoX,
        }

        color = {
            "blue": colorB,
            "green": colorG,
            "red": colorR,
        }

        # With JSON structure.
        particula = {
            "color":color,
            "destino":destino,
            "origen":origen,
            "id": id,
            "velocidad": velocidad,
        }

        self.particulas.append(particula)
        print("Particula agregada", particula)
        print("Distancia: ", distancia)

        # Clear data from the line edit.
        self.ui.lnEdtID.clear()
        self.ui.lnEdtOrigX.clear()
        self.ui.lnEdtOrigY.clear()
        self.ui.lnEdtDestX.clear()
        self.ui.lnEdtDestY.clear()
        self.ui.lnEdtVel.clear()
        self.ui.spBxG.setValue(0)
        self.ui.spBxR.setValue(0)
        self.ui.spBxB.setValue(0)

    @Slot()
    def mostrarParticulas(self):
        self.ui.plnTxtWdgtSalida.clear()
        contador = 0;
        for particula in self.particulas:
            distancia = calcDistEuclidiana(particula["origen"]["x"],
                                           particula["origen"]["y"],
                                           particula["destino"]["x"],
                                           particula["destino"]["y"])
            contador = contador + 1
            print("Mostrando particula ", contador, ":", particula)
            print("Distancia de la particula ", contador, ":", distancia)

            for key, value in particula.items():
                if type(value) is int or float:
                    value = str(value)
                self.ui.plnTxtWdgtSalida.insertPlainText(key + ": " + value + "\n")
            self.ui.plnTxtWdgtSalida.insertPlainText("Distancia: " + str(round(distancia, 3)) + "\n\n")

    @Slot()
    def guardar(self):
        # With self, it will be the main window.
        # Third parameter its where the file will be saved.
        # Last parameter it will be the extension.
        ubicacion = QFileDialog.getSaveFileName(self, "Guardar particulas", ".",
                                                "JSON (*.json)")

        with open(ubicacion[0], "w") as archivo:
            # Volcar o vaciar la información a un archivo.
            json.dump(self.particulas, archivo, indent=5)

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self, "Abrir archivo", ".",
                                                "JSON (*.json)")

        with open(ubicacion[0], "r") as archivo:
            self.particulas = json.load(archivo)

