#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from source.ExcepcionesClja.CljaError import CljaError


class Clja(object):

    def __init__(self, L=1, hr=0, previos=[], compuesta=False, clja_hash_value=-1):
        self.L = L
        self.huecos_rojos = hr
        self.compuesta = compuesta
        self.previos = previos
        self.__clja_hash_value = clja_hash_value

    def tbhik(self, camino, nivel, k_bolas):
        pass

    def flja(self, w, lista_de_etiquetas):
        pass

    def flja_inversa(self, natural):
        pass

    def posicion_de_hueco(self, camino, nivel):
        pass

    def etiqueta_del_hueco(self, posicion):
        pass

    def check_cf(self, camino):
        pass

    def nw_inversa(self, natural):
        raise CljaError("No deberías llamar nunca a este metodo! <nw_inversa() de la clase abuela>")

    def b1(self, camino, nivel):
        raise CljaError("No deberías llamar nunca a este metodo! <b1() de la clase abuela>")
    # PROPERTIES:

    def set_L(self, nuevo_valor):
        self.L = nuevo_valor

    def get_L(self):
        return self.L

    def get_huecos_rojos(self):
        return self.huecos_rojos

    def set_huecos_rojos(self, nuevo_valor):
        self.huecos_rojos = nuevo_valor

    def _set_clja_hash_value(self, new_value):
        self.__hash_value = new_value

    def _get_clja_hash_value(self):
        return self.__clja_hash_value

    clja_hash_value = property (_get_clja_hash_value, _set_clja_hash_value)

    def __hash__(self):
        if self.clja_hash_value == -1:
            raise CljaError("Se consulta el valor hash y todavía no se ha definido: ahora es -1, indefinido")
        return self.clja_hash_value
