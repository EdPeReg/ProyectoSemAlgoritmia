# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(718, 848)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionVer = QAction(MainWindow)
        self.actionVer.setObjectName(u"actionVer")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabAgregar = QWidget()
        self.tabAgregar.setObjectName(u"tabAgregar")
        self.gridLayout = QGridLayout(self.tabAgregar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.tabAgregar)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)

        self.spBxR = QSpinBox(self.tabAgregar)
        self.spBxR.setObjectName(u"spBxR")
        self.spBxR.setMaximum(255)

        self.gridLayout.addWidget(self.spBxR, 6, 1, 1, 1)

        self.btnMostrar = QPushButton(self.tabAgregar)
        self.btnMostrar.setObjectName(u"btnMostrar")

        self.gridLayout.addWidget(self.btnMostrar, 8, 1, 1, 1)

        self.lnEdtDestX = QLineEdit(self.tabAgregar)
        self.lnEdtDestX.setObjectName(u"lnEdtDestX")

        self.gridLayout.addWidget(self.lnEdtDestX, 3, 1, 1, 3)

        self.lnEdtDistEucl = QLineEdit(self.tabAgregar)
        self.lnEdtDistEucl.setObjectName(u"lnEdtDistEucl")

        self.gridLayout.addWidget(self.lnEdtDistEucl, 7, 1, 1, 3)

        self.label = QLabel(self.tabAgregar)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lnEdtOrigX = QLineEdit(self.tabAgregar)
        self.lnEdtOrigX.setObjectName(u"lnEdtOrigX")

        self.gridLayout.addWidget(self.lnEdtOrigX, 1, 1, 1, 3)

        self.label_9 = QLabel(self.tabAgregar)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_2 = QLabel(self.tabAgregar)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.tabAgregar)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lnEdtVel = QLineEdit(self.tabAgregar)
        self.lnEdtVel.setObjectName(u"lnEdtVel")

        self.gridLayout.addWidget(self.lnEdtVel, 5, 1, 1, 3)

        self.btnEnviar = QPushButton(self.tabAgregar)
        self.btnEnviar.setObjectName(u"btnEnviar")

        self.gridLayout.addWidget(self.btnEnviar, 8, 0, 1, 1)

        self.plnTxtWdgtSalida = QPlainTextEdit(self.tabAgregar)
        self.plnTxtWdgtSalida.setObjectName(u"plnTxtWdgtSalida")

        self.gridLayout.addWidget(self.plnTxtWdgtSalida, 9, 0, 2, 5)

        self.spBxG = QSpinBox(self.tabAgregar)
        self.spBxG.setObjectName(u"spBxG")
        self.spBxG.setMaximum(255)

        self.gridLayout.addWidget(self.spBxG, 6, 2, 1, 2)

        self.spBxB = QSpinBox(self.tabAgregar)
        self.spBxB.setObjectName(u"spBxB")
        self.spBxB.setMaximum(255)

        self.gridLayout.addWidget(self.spBxB, 6, 4, 1, 1)

        self.label_7 = QLabel(self.tabAgregar)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.lnEdtID = QLineEdit(self.tabAgregar)
        self.lnEdtID.setObjectName(u"lnEdtID")

        self.gridLayout.addWidget(self.lnEdtID, 0, 1, 1, 3)

        self.lnEdtOrigY = QLineEdit(self.tabAgregar)
        self.lnEdtOrigY.setObjectName(u"lnEdtOrigY")

        self.gridLayout.addWidget(self.lnEdtOrigY, 1, 4, 1, 1)

        self.lnEdtDestY = QLineEdit(self.tabAgregar)
        self.lnEdtDestY.setObjectName(u"lnEdtDestY")

        self.gridLayout.addWidget(self.lnEdtDestY, 3, 4, 1, 1)

        self.tabWidget.addTab(self.tabAgregar, str())
        self.tabTabla = QWidget()
        self.tabTabla.setObjectName(u"tabTabla")
        self.gridLayout_2 = QGridLayout(self.tabTabla)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lnEdtBuscar = QLineEdit(self.tabTabla)
        self.lnEdtBuscar.setObjectName(u"lnEdtBuscar")

        self.horizontalLayout_2.addWidget(self.lnEdtBuscar)

        self.btnBuscar = QPushButton(self.tabTabla)
        self.btnBuscar.setObjectName(u"btnBuscar")

        self.horizontalLayout_2.addWidget(self.btnBuscar)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.tblWdgtTabla = QTableWidget(self.tabTabla)
        self.tblWdgtTabla.setObjectName(u"tblWdgtTabla")

        self.gridLayout_2.addWidget(self.tblWdgtTabla, 1, 0, 1, 1)

        self.btnMostrarTabla = QPushButton(self.tabTabla)
        self.btnMostrarTabla.setObjectName(u"btnMostrarTabla")

        self.gridLayout_2.addWidget(self.btnMostrarTabla, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tabTabla, str())
        self.tabGrafica = QWidget()
        self.tabGrafica.setObjectName(u"tabGrafica")
        self.gridLayout_3 = QGridLayout(self.tabGrafica)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.graphicsView = QGraphicsView(self.tabGrafica)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.btnDibujar = QPushButton(self.tabGrafica)
        self.btnDibujar.setObjectName(u"btnDibujar")

        self.gridLayout_3.addWidget(self.btnDibujar, 1, 0, 1, 1)

        self.btnLimpiar = QPushButton(self.tabGrafica)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.gridLayout_3.addWidget(self.btnLimpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tabGrafica, str())
        self.tabOrdenamiento = QWidget()
        self.tabOrdenamiento.setObjectName(u"tabOrdenamiento")
        self.gridLayout_4 = QGridLayout(self.tabOrdenamiento)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnVelocidad = QPushButton(self.tabOrdenamiento)
        self.btnVelocidad.setObjectName(u"btnVelocidad")

        self.horizontalLayout.addWidget(self.btnVelocidad)

        self.btnDistancia = QPushButton(self.tabOrdenamiento)
        self.btnDistancia.setObjectName(u"btnDistancia")

        self.horizontalLayout.addWidget(self.btnDistancia)

        self.btnMostrarOrd = QPushButton(self.tabOrdenamiento)
        self.btnMostrarOrd.setObjectName(u"btnMostrarOrd")

        self.horizontalLayout.addWidget(self.btnMostrarOrd)

        self.btnLimpiar_2 = QPushButton(self.tabOrdenamiento)
        self.btnLimpiar_2.setObjectName(u"btnLimpiar_2")

        self.horizontalLayout.addWidget(self.btnLimpiar_2)


        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.graphicViewOrdenar = QGraphicsView(self.tabOrdenamiento)
        self.graphicViewOrdenar.setObjectName(u"graphicViewOrdenar")

        self.gridLayout_4.addWidget(self.graphicViewOrdenar, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tabOrdenamiento, str())
        self.tabPuntosCercanos = QWidget()
        self.tabPuntosCercanos.setObjectName(u"tabPuntosCercanos")
        self.gridLayout_6 = QGridLayout(self.tabPuntosCercanos)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btnLimpiarPC = QPushButton(self.tabPuntosCercanos)
        self.btnLimpiarPC.setObjectName(u"btnLimpiarPC")

        self.gridLayout_6.addWidget(self.btnLimpiarPC, 1, 0, 1, 1)

        self.btnMostrarPuntosCercanos = QPushButton(self.tabPuntosCercanos)
        self.btnMostrarPuntosCercanos.setObjectName(u"btnMostrarPuntosCercanos")

        self.gridLayout_6.addWidget(self.btnMostrarPuntosCercanos, 1, 1, 1, 1)

        self.btnMostrarPuntos = QPushButton(self.tabPuntosCercanos)
        self.btnMostrarPuntos.setObjectName(u"btnMostrarPuntos")

        self.gridLayout_6.addWidget(self.btnMostrarPuntos, 1, 2, 1, 1)

        self.graphicsViewPuntosCercanos = QGraphicsView(self.tabPuntosCercanos)
        self.graphicsViewPuntosCercanos.setObjectName(u"graphicsViewPuntosCercanos")

        self.gridLayout_6.addWidget(self.graphicsViewPuntosCercanos, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tabPuntosCercanos, str())
        self.tabGrafos = QWidget()
        self.tabGrafos.setObjectName(u"tabGrafos")
        self.verticalLayout = QVBoxLayout(self.tabGrafos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plnTxtEdtGrafo = QPlainTextEdit(self.tabGrafos)
        self.plnTxtEdtGrafo.setObjectName(u"plnTxtEdtGrafo")

        self.verticalLayout.addWidget(self.plnTxtEdtGrafo)

        self.btnMostrarGrafo = QPushButton(self.tabGrafos)
        self.btnMostrarGrafo.setObjectName(u"btnMostrarGrafo")

        self.verticalLayout.addWidget(self.btnMostrarGrafo)

        self.btnDijkstra = QPushButton(self.tabGrafos)
        self.btnDijkstra.setObjectName(u"btnDijkstra")

        self.verticalLayout.addWidget(self.btnDijkstra)

        self.btnKruskal = QPushButton(self.tabGrafos)
        self.btnKruskal.setObjectName(u"btnKruskal")

        self.verticalLayout.addWidget(self.btnKruskal)

        self.btnPrim = QPushButton(self.tabGrafos)
        self.btnPrim.setObjectName(u"btnPrim")

        self.verticalLayout.addWidget(self.btnPrim)

        self.btnRecorridoAnchura = QPushButton(self.tabGrafos)
        self.btnRecorridoAnchura.setObjectName(u"btnRecorridoAnchura")

        self.verticalLayout.addWidget(self.btnRecorridoAnchura)

        self.btnRecorridoProfundidad = QPushButton(self.tabGrafos)
        self.btnRecorridoProfundidad.setObjectName(u"btnRecorridoProfundidad")

        self.verticalLayout.addWidget(self.btnRecorridoProfundidad)

        self.btnLimpiar_3 = QPushButton(self.tabGrafos)
        self.btnLimpiar_3.setObjectName(u"btnLimpiar_3")

        self.verticalLayout.addWidget(self.btnLimpiar_3)

        self.tabWidget.addTab(self.tabGrafos, str())

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 718, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Grafo  (Algoritmo Dijkstra) - Act 13", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"&Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"&Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionVer.setText(QCoreApplication.translate("MainWindow", u"&Ver", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Distancia Euclidiana", None))
        self.btnMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen (X,Y)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino (X,Y)", None))
        self.btnEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color (R,G,B)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAgregar), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnMostrarTabla.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTabla), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.btnDibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGrafica), QCoreApplication.translate("MainWindow", u"Grafica", None))
        self.btnVelocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.btnDistancia.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.btnMostrarOrd.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.btnLimpiar_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOrdenamiento), QCoreApplication.translate("MainWindow", u"Ordenamiento", None))
        self.btnLimpiarPC.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnMostrarPuntosCercanos.setText(QCoreApplication.translate("MainWindow", u"Mostrar Puntos Cercanos", None))
        self.btnMostrarPuntos.setText(QCoreApplication.translate("MainWindow", u"Mostrar Puntos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPuntosCercanos), QCoreApplication.translate("MainWindow", u"Puntos Cercanos", None))
        self.btnMostrarGrafo.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.btnDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.btnKruskal.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.btnPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.btnRecorridoAnchura.setText(QCoreApplication.translate("MainWindow", u"Recorrido Anchura", None))
        self.btnRecorridoProfundidad.setText(QCoreApplication.translate("MainWindow", u"Recorrido Profundidad", None))
        self.btnLimpiar_3.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGrafos), QCoreApplication.translate("MainWindow", u"Grafos", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"&Archivo", None))
    # retranslateUi

