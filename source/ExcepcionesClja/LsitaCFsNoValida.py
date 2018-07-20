#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

"""
Se lanza cuando una lista de caminos finitos no corresponde con el tipo de flja
Si la flja es absoluta, vale cualquier combinación.
Si la flja es práctica, ambos CaminosFinitos deben tener al menos, el primere elemento en común.

No se comprueba si SOLO el DR del últimmo es cero pq la propia flja ignora caminos más allá del que tiene DR = 0.
"""

from source.ExcepcionesClja.CljaError import CljaError


class ListaCFsNoValida (CljaError):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.AVISO = 'Lista de Caminos finitos inválida: '

    def __str__(self):
        return self.AVISO + self.mensaje
