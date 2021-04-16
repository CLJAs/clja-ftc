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
    def clja_sqrt_old(numero):
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
                respuesta = "\n"
                respuesta += "Raiz flotante:  " + str(math.sqrt(numero)) + "\n"
                respuesta += "Raiz entera:    " + str(raiz_entera) + "\n"
                respuesta += "Raiz entera +1: " + str(raiz_entera + 1) + "\n"
                respuesta += "Numero:         " + str(numero) + "\n"
                respuesta += "Cuadrado aprox: " + str(cuadrado_aprox) + "\n"
                respuesta += "Error:          " + str(numero - cuadrado_aprox) + "\n"
                respuesta += "E raiz + 1 **2: " + str(((raiz_entera + 1) ** 2) - numero) + "\n"
                raise FalloEnSqrt(str(respuesta))
        else:
            raise FalloEnSqrt("Fallo totalmente inesperado!!")

    @staticmethod
    def clja_sqrt(numero):
        residuo_final_es_cero = False
        raiz_parcial = 0

        # Separo el radicando en grupos de dos digitos en base 10.
        lista_de_dos_digitos = []
        resto_de_numero = numero
        while resto_de_numero > 0:
            resto_de_numero, resto_actual = divmod(resto_de_numero, 100)
            lista_de_dos_digitos.append(resto_actual)

        lista_de_dos_digitos.reverse()
        primer_par = True
        radicando_parcial = 0
        for par_de_digitos in lista_de_dos_digitos:
            radicando_parcial = (radicando_parcial * 100) + par_de_digitos
            digito09 = MathClja.encontrar_un_nuevo_digito_de_la_raiz(radicando_parcial, raiz_parcial)

            if not primer_par:
                radicando_parcial -= (((raiz_parcial * 2) * 10) + digito09) * digito09
            else:
                radicando_parcial -= digito09 ** 2
                primer_par = False
            raiz_parcial = (raiz_parcial * 10) + digito09

        if radicando_parcial == 0:
            residuo_final_es_cero = True  # Es exacta
        return raiz_parcial, residuo_final_es_cero

    @staticmethod
    def encontrar_un_nuevo_digito_de_la_raiz(rad_parcial, raiz_actual):
        # TODO: reducir el número de operaciones al mínimo posible.
        maximo = 9
        minimo = 0
        raiz_doble_extendida_acabada_en_cero = (raiz_actual * 2) * 10  # Desplazo a la izq el doble de la raiz actual.
        intento_de_digito = 4  # (maximo + minimo) // 2

        while (maximo - minimo) > 1:
            intento_de_raiz = raiz_doble_extendida_acabada_en_cero + intento_de_digito
            intento_de_resultado = intento_de_raiz * intento_de_digito
            if intento_de_resultado == rad_parcial:
                return intento_de_digito
            elif intento_de_resultado > rad_parcial:
                maximo = intento_de_digito - 1
            else:
                minimo = intento_de_digito
            intento_de_digito = (maximo + minimo) // 2

        if ((raiz_doble_extendida_acabada_en_cero + maximo) * maximo) > rad_parcial:
            return minimo
        else:
            return maximo


if __name__ == "__main__":
    a = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    a2 = a ** 2

    raiz, exacta = MathClja.clja_sqrt(a2)
    print("a2 es exacta?  raiz: " + str(raiz) + " es exacta?: " + str(exacta))

    raiz, exacta = MathClja.clja_sqrt(a2 - 1)
    print("a2 es exacta?  raiz: " + str(raiz) + " es exacta?: " + str(exacta))

    raiz, exacta = MathClja.clja_sqrt(a2 + 1)
    print("a2 es exacta?  raiz: " + str(raiz) + " es exacta?: " + str(exacta))

    raiz, exacta = MathClja.clja_sqrt(3)
    print("a2 es exacta?  raiz: " + str(raiz) + " es exacta?: " + str(exacta))

    raiz, exacta = MathClja.clja_sqrt(301)
    print("a2 es exacta?  raiz: " + str(raiz) + " es exacta?: " + str(exacta))

    radicando_p = 139
    raiz_p = 2
    digito = MathClja.encontrar_un_nuevo_digito_de_la_raiz(radicando_p, raiz_p)
    print("Radicando parcial: ", radicando_p, " raiz_parcial: ", raiz_p, " digito propuesto: ", digito)

    radicando_p = 1001
    raiz_p = 23
    digito = MathClja.encontrar_un_nuevo_digito_de_la_raiz(radicando_p, raiz_p)
    print("Radicando parcial: ", radicando_p, " raiz_parcial: ", raiz_p, " digito propuesto: ", digito)

    radicando_p = 159
    raiz_p = 1
    digito = MathClja.encontrar_un_nuevo_digito_de_la_raiz(radicando_p, raiz_p)
    print("Radicando parcial: ", radicando_p, " raiz_parcial: ", raiz_p, " digito propuesto: ", digito)

    radicando_p = 351
    raiz_p = 16
    digito = MathClja.encontrar_un_nuevo_digito_de_la_raiz(radicando_p, raiz_p)
    print("Radicando parcial: ", radicando_p, " raiz_parcial: ", raiz_p, " digito propuesto: ", digito)

    radicando_p = 3037
    raiz_p = 161
    digito = MathClja.encontrar_un_nuevo_digito_de_la_raiz(radicando_p, raiz_p)
    print("Radicando parcial: ", radicando_p, " raiz_parcial: ", raiz_p, " digito propuesto: ", digito)
