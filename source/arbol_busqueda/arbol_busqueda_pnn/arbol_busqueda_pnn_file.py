#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source.arbol_busqueda.arbol_busqueda_pnn.nodo_ab_pnn_file import NodoABPNN

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'


class ArbolBusquedaPNN:
    def __init__(self):
        self.raiz = NodoABPNN()


# """
if __name__ == "__main__":
    nodo01 = NodoABPNN(0, 0, 3)
    nodo01.anadir_natural(0, 3)
    nodo01.anadir_natural(0, 5)
    print(nodo01)

    nodo02 = NodoABPNN(0, 0, 3)
    nodo02.anadir_natural(0, 21)
    nodo02.anadir_natural(0, 57)

    nodo02.anadir_natural(1, 345)
    nodo02.anadir_natural(0, 102546)
    # Con esta linea salta la excepcion de L:
    # nodo02.anadir_natural(0, 23456789)

    # Con esta linea salta la excepcion de no crear los huecos en orden:
    # nodo02.anadir_natural(3, 1234567890)

    print(nodo02)
    nodo03 = NodoABPNN(1, dr=0, l_del_nodo=3)
    nodo01.enlazar_nodo(0, nodo03)
    nodo03.anadir_natural(1,1023)
    print(nodo03)
    print(nodo01)
# """
