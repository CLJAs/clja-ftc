#!/usr/bin/env python
# -*- coding: utf-8 -*-
from source.ExcepcionesClja.CljaError import CljaError
from source.ExcepcionesClja.MoreThanLNaturals import MoreThanLNaturals
from source.arbol_busqueda.arbol_busqueda_pnn.tripleta_hueco_pnn_file import TripletaHuecoPNN

# from source.arbol_busqueda.arbol_busqueda_pnn.arbol_busqueda_pnn_file import ArbolBusquedaPNN
# from source.arbol_busqueda.arbol_busqueda_pnn.tripleta_hueco_pnn_file import TripletaHuecoPNN

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

"""
Clase NodoABPNN: Nodo del Árbol de Búsqueda para la función f:P(N) -> N

Cada nodo contiene una lista de huecos (conlas tripletas de su información:
TripletaHuecoPNN
Su lista de "posibles" cljas:
lista_drs: lista de referencias medidas por distancia al rojo(dr).

Deben dar la opción de consultar:
esta_vacio() SI/NO
la lista de DR es una constante que se clona al crear cada uno.
"""


class NodoABPNN:
    def __init__(self, nombre_del_nodo, dr=0, l_del_nodo=1):
        # Recordemos que lambda 0 es -1, y en la lista de coordenadas la lambda anterior es hueco_inicial -1
        self.nombre_del_nodo = nombre_del_nodo
        self.lambda_anterior = nombre_del_nodo - 1
        self.lista_de_huecos = list()
        self.L_DEL_NODO = l_del_nodo
        self.lista_drs = list()
        self.DR = None # necesito inicializarlo fuera del if para que entre dentro de la clase
        if isinstance(dr, list):
            self.lista_drs = dr
            self.DR = len(dr)
        elif isinstance(dr, int):
            self.DR = dr
            for i in range(0, dr):
                self.dr.append(ArbolBusquedaPNN())

        # Las posiciones en la lista de dr empiezan en dr, pero dr=1 corresponde a la pos=0, la dr=2 a la pos=1...

    def esta_vacio(self):
        if len(self.lista_de_huecos) == 0:
            return True

        else:
            return False

    # ANADIR_NATURAL: hueco, natural.
    # 1: ver si el hueco existe, si no, crearlo.
    # 2: da igual si la tripleta del hueco tiene una lista vacia de naturales (usamos append())
    # 3: ANTES de añadir el natural a la lista del hueco, ver si acabaremos teniendo mas de L.
    def anadir_natural(self, hueco, natural):
        # Hay que mirar si el hueco existe antes de preguntar por sus naturales:
        pos_en_array = self.pos_hueco(hueco)
        cantidad_de_huecos = self.huecos_anadidos()
        if cantidad_de_huecos <= pos_en_array:
            # Esto está orientado al test... los huecos se crean por orden porque empezamos por
            # f: N -> P(N)... o sea, los caminos a insertar en el arbol estan "ordenados"
            # No se puede crear un hueco sin crear antes los anteriores porque recorremos los naturales de menor a mayor

            # SOLO por si acaso no se crean en orden (0 es el caso donde creando solo una tripleta vamos bien):
            if (pos_en_array - cantidad_de_huecos) > 0:
                raise CljaError("Te has saltado un hueco a la hora de crearlos en orden!!")
            nueva_tripleta = TripletaHuecoPNN(hueco)
            self.lista_de_huecos.append(nueva_tripleta)
        # La tripleta del hueco ya existe en este punto.
        # Hay que mirar si vamos a meter mas naturales que L -> fallo catastrófico!!
        if self.hay_L_o_mas(hueco):
            raise MoreThanLNaturals(" :: En NodoABPNN anadir_natural...")
        else:
            # El hueco existe y no vamos a añadir mas de L:
            self.lista_de_huecos[self.pos_hueco(hueco)].anadir_natural(natural)

    def hay_L_o_mas(self, hueco):
        if self.lista_de_huecos[self.pos_hueco(hueco)].naturales_asociados() >= self.L_DEL_NODO:
            return True
        else:
            return False

    def huecos_anadidos(self):
        return len(self.lista_de_huecos)

    def pos_hueco(self, hueco):
        # hueco es el nombre, su posicion es el nombre del hueco menos el hueco inicial de la habitacion.
        # El - 1 es para que me de la posicion en la lista con indice empezando en cero.
        return hueco - self.lambda_anterior - 1

    def lista_drs_vacia(self):
        pass
        # for i in range (0, self.DR

    def __str__(self):
        cadena = "NODO\n"
        cadena += "Lista de huecos:\n"
        for i in range(0, self.huecos_anadidos()):
            cadena += "NOMBRE: " + self.lista_de_huecos[i].__str__() + "\n"
        return cadena

    def enlazar_nodo(self, hueco, nuevo_nodo):
        if nuevo_nodo.nombre_del_nodo <= self.lambda_anterior:
            raise CljaError("Estas enlazando un hueco con nombre igual o inferior al actual.")
        if self.hueco_existe(hueco):
            self.lista_de_huecos[self.pos_hueco(hueco)].enlazar_nodo(nuevo_nodo)
        else:
            raise CljaError("Intentas enlazar unnuevo nodo a un nodo que no existe!!!")

    def hueco_existe(self, hueco):
        pos_en_array = self.pos_hueco(hueco)
        cantidad_de_huecos = self.huecos_anadidos()
        if cantidad_de_huecos <= pos_en_array:
            # El hueco no existiría todavia, aunque fuese el que iba en la última posicion.
            return False
        else:
            return True






