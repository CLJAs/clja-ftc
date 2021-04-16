#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from source.ExcepcionesClja.CljaError import CljaError


class MoreThanLNaturals (CljaError):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.AVISO = 'Se ha intentado asociar mas de L naturales'

    def __str__(self):
        return self.AVISO + self.mensaje