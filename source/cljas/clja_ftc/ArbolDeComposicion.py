#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'


from source.ExcepcionesClja.CljaError import CljaError


class ArbolDeComposicionCljaFTC (object):

    def __init__(self, lista_cljas, lista_drs):
        self.lista_cljas = lista_cljas
        self.lista_drs = lista_drs
        raise CljaError("Método init ArbolDeComposicion no definido")

    """
    PROPERTIES:
    """
    def _get_lista_cljas(self):
        return self.__lista_cljas

    def _set_lista_cljas(self, nueva_lista):
        self.__lista_cljas = nueva_lista

    lista_cljas = property(_get_lista_cljas, _set_lista_cljas)

    def _get_drs(self):
        return self.__drs

    def _set_drs(self, nuevos_drs):
        self.__drs = nuevos_drs

    lista_drs = property (_get_drs, _set_drs)


if __name__ == "__main__":
    pass
