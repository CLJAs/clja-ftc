#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

"""
Se lanza cuando un camino finito no cumple sus condiciones para ser válido y usable. Consultar la clase CaminoFinito.
Cómo la calase se inicializa con un string, con una cadena, al pasarlo a lista no sólo pueden haber errores de memoria 
o formato, pueden haber números repetidos, no estar ordenados... etc...
"""

from source.ExcepcionesClja.CljaError import CljaError


class CaminoFinitoNoValido (CljaError):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.AVISO = 'Camino finito invalido: '

    def __str__(self):
        return self.AVISO + self.mensaje
