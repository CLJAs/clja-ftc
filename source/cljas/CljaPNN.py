#!/usr/bin/env python
# -*- coding: utf-8 -*-
from source.ExcepcionesClja.CaminoFinitoNoValido import CaminoFinitoNoValido
from conjuntos.camino_finito import CaminoFinito

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from cljas.Clja import Clja
import math
from source.ExcepcionesClja.PosibleErrorDePrecision import PosibleErrorDePrecision


class CljaPNN(Clja):

    def __init__(self, ele=1, hr=0, previos=[],  compuesta=False):
        Clja.__init__(self, ele, hr, previos, compuesta)


    """ Cantidad de bolas necesarias para que por el hueco, de ese nivel del camino, pase la primera bola"""
    def b1(self, camino, nivel):
        """etiqueta = camino.lista_coordenadas[nivel]"""
        posicion = self.posicion_de_hueco(camino, nivel)
        return int(((posicion + 1) * posicion) // 2)

    def tbhik(self, camino, nivel, k_bolas):
        if k_bolas == 1:
            resultado = self.b1(camino, nivel)
        else:
            resultado = self.b1(camino, nivel) + \
                   (
                       ((2 * self.posicion_de_hueco(camino, nivel)) + (k_bolas - 2))
                       *
                       (k_bolas - 1)
                   ) // 2
        return resultado

    def posicion_de_hueco(self, camino, posicion_etiqueta):
        etiqueta = camino.lista_coordenadas[posicion_etiqueta]
        etiqueta_nivel_anterior = camino.lista_coordenadas[posicion_etiqueta - 1]
        posicion = etiqueta - etiqueta_nivel_anterior

        if posicion_etiqueta == camino.m():
            resultado = (posicion * (self.huecos_rojos + 1)) - camino.dr
        else:
            resultado = posicion * (self.huecos_rojos + 1)
        return int(resultado)

    # TODO: la "L" sobra como parámetro, es una propiedad de la CLJA.
    def flja(self, w, camino):
        if self.huecos_rojos < camino.dr:
            raise CaminoFinitoNoValido("Hr=" + str(self.huecos_rojos) + " y " + "camino.dr=" + str(camino.dr))
        # Cada camino tiene LAMBDA_CERO al principio... por eso le restamos uno
        total_de_niveles = len(camino.lista_coordenadas) - 1
        total_de_bolas = w
        for nivel in range(total_de_niveles, 0, -1):
            total_de_bolas = self.tbhik(camino, nivel, total_de_bolas)
            # EL saco mágico no tiene L bolitas grises asociadas como los huecos.
            if nivel > 1:
                total_de_bolas += self.L

        # El total de bolas del nivel uno... menos uno, nos da el natural a la posicion w en el hueco de ese camino
        if self.compuesta:
            return total_de_bolas
        else:
            return self.nw(total_de_bolas)

    def nw(self, total_de_bolas):
        return total_de_bolas - 1 + len(self.previos)


    """*****************************************************************************************************************
    FLJA INVERSA:
    Dado un natural, una bolita gris, devuelve el Camino finito al que está emparejada.
    Funciones:
    
    posicion_de_hueco_inversa()
    
    ese_mayuscula(): el "primer hueco" (su posicion, no su etiqueta) creado, anterior a la iteración donde se reparete
                     nuestra bolita en ese nivel
                     
    total_de_bolas_siguiente_nivel(): calculo del total de bolas que pasan al siguiente nivel.
    
    doble_uve(): nos indica, en caso de que la CLja tenga L > 1, a que "concepto" w del hueco está emparejado el natural
    *****************************************************************************************************************"""
    def flja_inversa(self, natural):
        lista_etiquetas_huecos = list()
        total_de_bolas_en_este_nivel = natural + 1
        # Salgo del while al hacer returns... es feo pero crear una variable que no voy a usar es estupido.
        while (True):
            [ese, es_natural] = self.ese_mayuscula(total_de_bolas_en_este_nivel)
            ese = int(ese)
            # S es un valor natural, no tiene decimales. Nuestro natural es la primera bolita emparejada a un hueco.
            if es_natural:
                lista_etiquetas_huecos.append(
                    int(
                        self.etiqueta_del_hueco_modo_inverso(ese, lista_etiquetas_huecos)
                    )
                )
                # lista_etiquetas_huecos.append(int(ese))
                return [1, CaminoFinito.CaminoFinito(lista_etiquetas_huecos)]
            # S tiene decimales, no es una bolita de primer hueco.
            else:
                posicion_del_hueco_de_este_nivel = total_de_bolas_en_este_nivel - (((ese + 1) * ese) // 2)
                lista_etiquetas_huecos.append(
                    int(
                        self.etiqueta_del_hueco_modo_inverso(posicion_del_hueco_de_este_nivel, lista_etiquetas_huecos)
                    )
                )
                # Calculamos las bolas que pasan al siguiente nivel
                total_de_bolas_en_este_nivel = ese + 1 - posicion_del_hueco_de_este_nivel + 1 - self.L
                if total_de_bolas_en_este_nivel > 0:
                    #Seguimos iterando
                    pass
                else:
                    # El hueco tiene emparejadas L bolas, y nos quedan las mismas o menos, hemos acabado.
                    doble_uve = (ese + 1 - posicion_del_hueco_de_este_nivel + 1)
                    return [int(doble_uve), CaminoFinito.CaminoFinito(lista_etiquetas_huecos)]

    # TODO:
    """
    ESE MAYUSCULA
    
    Esta funcion tiene un problema muy gordo. La precisión decimal de python tiene un límite donde empieza a redondear.
    13.0000000000000000000000000000007
    Es igual a 13.0 y ese redondeo da un falso positivo de primer hueco.
    Habría que rehacer todas las operaciones matemáticas y los tipos para asegurarnos la precisión dentro de la
    capacidad de memoria del ordenador ejecutante.
    TRUCO: solo interesa saber si tienbe decimales o no, podemos hacer a mano la raíz cuadrada, qeu darnos con el 
    resultado natural y a la primera pista de si va a tener o no decimales... devolvemos una variable boolean, no hace 
    falta calcular tooodooos los decimales del resultado.
    """
    @staticmethod
    def ese_mayuscula(total_de_bolas):
        if total_de_bolas > 100000000:
            raise PosibleErrorDePrecision("He decidido recortar a naturales de 8 cifras para evitar que python " +
                                          "redondee resultados.\n" +
                                          "Sin garantías de que esto sea suficiente. La cantidad de decimales de los " +
                                          "resultados decimales no dependen de las cifras de los operandos. \n")
        total_de_bolas *= 1.0 # Necesito que las operaciones conserven los decimales """
        resultado = (
            (
                math.sqrt(1 + (8 * total_de_bolas)) - 1
            ) / 2
        )
        return [int(resultado), (resultado - math.floor(resultado) == 0)]

    @staticmethod
    def etiqueta_del_hueco_modo_inverso(posicion_del_hueco, lista_etiquetas_hasta_el_momento):
        if len(lista_etiquetas_hasta_el_momento) == 0:
            etiqueta_anterior = CaminoFinito.CaminoFinito.LAMBDA_CERO
        else:
            etiqueta_anterior = lista_etiquetas_hasta_el_momento[len(lista_etiquetas_hasta_el_momento) - 1]
        return etiqueta_anterior + posicion_del_hueco


if __name__ == "__main__":
    clja_xa_iterar = CljaPNN(1, 0)
    camino_mas_largo = CaminoFinito({0})
    for i in range(0, 100000):
        [w, camino] = clja_xa_iterar.flja_inversa(i)
        print ("Natural: i: " + str(i) + " -> camino: " + str(camino) + " w: " + str(w))
        if len(camino.lista_coordenadas) > len (camino_mas_largo.lista_coordenadas):
            camino_mas_largo = camino
    print ("Uno de los caminos más largos era: " + str(camino_mas_largo))

    def prueba_iterada_SF_to_N(la_clja, maximo_elementos):
        for i in range(0, maximo_elementos):
            lista_etiquetas = range(0, i + 1)
            camino = CaminoFinito.CaminoFinito(lista_etiquetas)
            calcular_todos_los_n_de_un_camino(la_clja, camino)

    def calcular_todos_los_n_de_un_camino (la_clja, camino):
        lista_ws = list()
        for w in range(1, la_clja.L + 1):
            lista_ws.append(la_clja.flja(w, camino))
        mensaje = "El camino era: " + str(camino)
        mensaje += " Los naturales son: "
        cadena_w = ""
        for k in range(0, len(lista_ws)):
            cadena_w += " " + str(lista_ws[k]) + " "
        print (mensaje + cadena_w)

    prueba_iterada_SF_to_N(clja_xa_iterar, 10)
    calcular_todos_los_n_de_un_camino(clja_xa_iterar, CaminoFinito.CaminoFinito([309, 325]))
    calcular_todos_los_n_de_un_camino(clja_xa_iterar, CaminoFinito.CaminoFinito([315, 325, 327]))
    calcular_todos_los_n_de_un_camino(clja_xa_iterar, CaminoFinito.CaminoFinito([2]))
    calcular_todos_los_n_de_un_camino(clja_xa_iterar, CaminoFinito.CaminoFinito([1]))




