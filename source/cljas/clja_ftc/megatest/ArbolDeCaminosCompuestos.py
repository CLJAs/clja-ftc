#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

"""
ARBOL DE CAMINOS COMPUESTOS:

Es una estructura en arbol que intenta guardar todos los caminos generados por el test
natural [1..limite] -> ListaCFsCjaFtc
Así que guardamos la lista en una serie de árboles de caminos como si fuesen de búsqueda léxica, 
enlazados por los huecos rojos (DR>0) para no repetir nodos.

"""

from source.ExcepcionesClja.ExcepcionDeAsignacionIncorrecta import ExcepcionDeAsignacionIncorrecta
from source.cljas.clja_ftc.ListaCFsCljaFtc import ListaCFsCljaFtc


class ArbolDeCaminosCompuestos(object):

    def __init__(self, arbol_de_composicion=None):
        self.arbol_de_composicion = arbol_de_composicion
        self.clja_raiz
        self.arbol_cf_raiz = None
        # Voy contando los elementos que caerían en previos, si hay mas que el cardinal de previos: ERROR.
        self.chequeo_de_previos = list()

    def esta_vacio(self):
        return self.arbol_cf_raiz is None

    def actualizar_clja(self):
        pass

    def actualizar_lista_drs(self):
        pass

    def insertar(self, lista_de_caminos, natural):
        clja_actual = self.clja_raiz
        ya_estaba_dentro = False
        tiene_mas_naturales_que_ele = False
        todo_ok = True



        return ya_estaba_dentro, tiene_mas_naturales_que_ele, todo_ok

    def _insertar_en_chequeo_de_previos(self, miembro, clja_actual):
        """
        Aqui hay dos previos: la lista que voy guardando y el previos de la clja actual de la composicion

        Primero hay que buscarlo en previos de la clja, por si es un elemento aberrante y no tiene sentido en la clja

        Luego hay que buscarlo en la lista de chequeo de previos, por si lo repetimos: Los previos
        SOLO RECIBEN un natural.
        :param miembro:
        :return:
        """
        # Ahora lo busco en chequeo de previos de la clja a ver si es algo válido a buscar:
        if ArbolDeCaminosCompuestos._esta_en_previos(miembro, clja_actual):
            # Ahora miro si ya lo he visto antes y ya esta en la lista de chequeo de previos
            for elemento in self.chequeo_de_previos:
                if elemento == miembro:
                    raise ExcepcionDeAsignacionIncorrecta("Se ha detectado dos veces el mismmo elemento de previos.")
        elif miembro is not isinstance(ListaCFsCljaFtc):

        else:
            mensaje = "No es ni una lista de caminos ni un miembro de previos: "
            mensaje += str(lista_de_caminos)
            raise ExcepcionDeAsignacionIncorrecta(mensaje)




    @staticmethod
    def _esta_en_previos(elemento, clja_a_testar):
        resultado = False
        if clja_a_testar.previos is not None:
            for miembro in clja_a_testar.previos:
                if miembro == elemento:
                    return True
        return resultado


if __name__ == "__main__":
    pass

