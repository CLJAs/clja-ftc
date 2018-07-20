#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

"""
Devuelve dos valores:
La raiz y si es exacta o no.
La raiz es un número natural pero:
True: significa que no tiene decimales.
False: significa que tiene decimales, cuales? Te da igual... pero el tipo es int, sólo te avisa que los "tiene".
Redondea a floor()
"""

import math
from source.ExcepcionesClja.FalloEnSqrt import FalloEnSqrt


class MathClja(object):

    @staticmethod
    def clja_sqrt(numero):
        raiz_entera = int(math.sqrt(numero))
        cuadrado_aprox = raiz_entera ** 2

        if numero == cuadrado_aprox:
            return raiz_entera, True
        elif cuadrado_aprox < numero:
            if ((raiz_entera + 1) ** 2) > numero:
                return raiz_entera, False
            else:
                raise FalloEnSqrt(str(numero))
        elif cuadrado_aprox > numero:
            raiz_entera -= 1
            if (raiz_entera ** 2) < numero:
                return raiz_entera, False
            else:
                raise FalloEnSqrt(str(numero))
        else:
            raise FalloEnSqrt("Fallo totalmente inesperado!!")


if __name__ == "__main__":
    a = 999999999
    a2 = a ** 2
    raiz, exacta = MathClja.clja_sqrt(a2)
    print("a2 es exacta?  raiz: " + str(raiz) + " es exacta?: " + str(exacta))

    raiz, exacta = MathClja.clja_sqrt(a2 - 1)
    print("a2 es exacta?  raiz: " + str(raiz) + " es exacta?: " + str(exacta))

    raiz, exacta = MathClja.clja_sqrt(a2 + 1)
    print("a2 es exacta?  raiz: " + str(raiz) + " es exacta?: " + str(exacta))