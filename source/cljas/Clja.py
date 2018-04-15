#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'


class Clja(object):

    def __init__(self, L=1, hr=0, previos=None,  compuesta=False):
        self.L = L
        self.huecos_rojos = hr
        self.compuesta = compuesta
        self.previos = previos

    def tbhik(self, camino, nivel, k_bolas):
        pass

    def flja(self, w, lista_de_etiquetas):
        pass

    def flja_inversa(self):
        pass

    def posicion_de_hueco(self, camino, nivel):
        pass

    def etiqueta_del_hueco(self, posicion):
        pass

    # PROPERTIES:

    def set_L(self, nuevo_valor):
        self.L = nuevo_valor

    def get_L(self):
        return self.L

    def get_huecos_rojos(self):
        return self.huecos_rojos

    def set_huecos_rojos(self, nuevo_valor):
        self.huecos_rojos = nuevo_valor

