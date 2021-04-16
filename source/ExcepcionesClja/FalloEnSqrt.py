#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

"""
Se lanza cuando math.sqrt falla "demasiado" redondeando un long demasiado largo. Se supone que el error no debe 
sobrepasar +-1... si el error supera este error se lanza ésta excepción. La creo sólo por si acaso, en algún caso 
concreto sucede y debo cambiar la implementación.

Hay que tener en cuenta que quiero llevar al límite el tamaño long/int de python con números muy largos.

"""

from source.ExcepcionesClja.CljaError import CljaError


class FalloEnSqrt (CljaError):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.AVISO = 'Math.sqrt añade demasiado error: '

    def __str__(self):
        return self.AVISO + self.mensaje
