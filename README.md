# ProyectoSemAlgoritmia
Proyecto de la materia seminario de algoritmia.

El programa es una recopilcación de pequeños programas que se hicieron a lo largo del semestre de la matería de seminario de algoritmia, donde el propósito será visualizar partículas utilizando archivos .json y pyside2.

Como características del programa contiene:

*Interfaz gráfica para capturar partículas, las cuales tienes los siguientes atributos:
- id
- origen (x,y)
- destino (x,y)
- velocidad
- color (r,g,b)
- distancia (calcular la distancia euclidiana)

*Capacidad para recuperar las particulas guardadas en un .json así como su respectivo respaldo.
*Un QPlainTextEdit para mostrar las partículas (todos sus atributos incluyendo la distancia).
*Un QTableWidget para mostrar las partículas (todos sus atributos incluyendo la distancia).
*Un campo de búsqueda por id.
*Dibujado de partículas en un QGraphicsScene usando "addLine", tomando en consideración: origen, destino y color.
*Capacidad de ordenar las partículas por velocidad (ascendente), por distancia (descendente) y mostrar las partículas.
*Algoritmo de fuerza bruta para encontrar los puntos más cercanos en las partículas, graficando dichos puntos.
*Capacidad de convertir las partículas a un grafo no dirigido ponderado (usando diccionarios).
*Recorridos sobre el grafo, profundidad y amplitud.
*Implementación del algoritmo Prim sobre el grafo de partículas, mostrando de un color diferente el recorrido.
*Implementación del algoritmo Kruskal sobre el grafo de partículas, mostrando de un color diferente el recorrido.
*Implementación del algoritmo Dijkstra sobre el grafo de partículas, siendo mostrado gráficamente.

Este programa contiene bugs, y el código presentado puede ser optimizado aún más, pues para el momento de la elaboración de este pequeño programa, no había programado en python.

Recordar, se usó pyside2-uic para convertir el archivo .ui a .py. Escrito en python3.



