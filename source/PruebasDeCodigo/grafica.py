#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

import matplotlib.pyplot as plt

from source.ExcepcionesClja.CljaError import CljaError
from source.cljas.CljaPNN import CljaPNN
from source.cljas.clja_ftc.CljaFtc import CljaFtc
from source.cljas.clja_ftc.ListaCFsCljaFtc import ListaCFsCljaFtc


# import numpy as np


def mostrar_un_resultado_inverso(clja, numero_natural, test_de_fallo=False, falla_en=9978):
    valor = numero_natural
    w_inverso, camino_inverso = clja.flja_inversa(valor)
    cadena_resultado = str(valor) + " --> " + str(camino_inverso)

    if isinstance(camino_inverso, ListaCFsCljaFtc):
        if isinstance(camino_inverso, str):
            if camino_inverso == "vacio":
                valor2 = 0
            elif camino_inverso == "yogurB":
                valor2 = 1
        else:
            valor2 = clja.flja_absoluta(w_inverso, camino_inverso.lista)
        if (numero_natural == falla_en) and test_de_fallo:
            valor2 += 1
        if valor == valor2:
            # print("COINCIDEN DIRECTO E INVERSO!!")
            cadena_resultado += " OK!! "
        else:
            raise CljaError("No coinciden la función directa y la inversa!!")
    else:
        # print("Es un miembro de previos")
        cadena_resultado += " Es un miembro de previos."
    print(cadena_resultado)


def valores_iniciales ():
    cljapnn1  = CljaPNN(1, 1, ["vacio", "yogurB"], False, clja_hash_value=1)
    cljapnn2a = CljaPNN(1, 0, [], True, clja_hash_value=2)
    cljapnn2b = CljaPNN(1, 1, [], True, clja_hash_value=3)
    cljapnn3  = CljaPNN(1, 0, [], True, clja_hash_value=4)

    arbol_ftc = {
        cljapnn1: {
            0: None,
            1: {
                cljapnn2a: {
                    0: None
                }
            }
        }
    }

    arbol_ftc_plus = {
        cljapnn1: {
            0: None,
            1: {
                cljapnn2b: {
                    0: None,
                    1: {
                        cljapnn3: {
                            0: None
                        }
                    }
                }
            }
        }
    }

    clja_ftc1 = CljaFtc(arbol_ftc)
    clja_ftc_plus = CljaFtc(arbol_ftc_plus)


def es_util (n, clja):
    w, lcf = clja.flja_inversa(n)
    if (type(lcf) is str) or lcf.check_lcf1() or lcf.check_lcf2p():
        return lcf, True
    return lcf, False


def crear_valores_x_y(tope, clja):
    # EL vacio y el yogur dan 1 en la formula
    #valores_y = [1, 1]
    valores_y = []
    # Creo la lista de numeros naturales hasta el tope.
    valores_x = list()
    for nat in range(0, tope+1):
        valores_x.append(float(nat))
    n_utiles = 0 # el vacio y el yogur
    ultimo_util = None
    lista_parcial = list()
    for natural in range(0, tope+1):
        lcf, respuesta = es_util(natural, clja)
        if respuesta:
            n_utiles += 1
            if (type(lcf) is not str) and len(lcf.lista) == 2:
                ultimo_util = [natural, n_utiles, lcf]
        y = n_utiles / (natural + 1)
        valores_y.append(y)
        print(natural, "[", n_utiles, "] -> ", str(lcf))
        if natural == 100 or natural == 1000 or natural == 1000000 or natural == 10000000 or natural == 30000000:
            lista_parcial.append([natural, n_utiles, lcf])
    lista_parcial.append(ultimo_util)
    for resultado in lista_parcial:
        print(resultado[0], "[", resultado[1], "] -> ", str(resultado[2]))
    return valores_x, valores_y

def crear_valores_x_y_v2(tope, clja, salto=1):
    # EL vacio y el yogur dan 1 en la formula
    #valores_y = [1, 1]
    valores_y = []
    # Creo la lista de numeros naturales hasta el tope.
    valores_x = list()
    for nat in range(0, tope + 1, salto):
        valores_x.append(float(nat))
    n_utiles = 0 # el vacio y el yogur
    ultimo_util = None
    lista_parcial = list()
    for natural in range(0, tope + 1):
        lcf, confirmado = es_util(natural, clja)
        if confirmado:
            n_utiles += 1
            if (type(lcf) is not str) and len(lcf.lista) == 2:
                ultimo_util = [natural, n_utiles, lcf]
        y = n_utiles / (natural + 1)
        if (natural % salto) == 0:
            valores_y.append(y)
        print(natural, "[", n_utiles, "] -> ", str(lcf))
        if natural == 100 or natural == 1000 or natural == 1000000 or natural == 10000000 or natural == 30000000:
            lista_parcial.append([natural, n_utiles, lcf])
    lista_parcial.append(ultimo_util)
    for resultado in lista_parcial:
        print(resultado[0], "[", resultado[1], "] -> ", str(resultado[2]))
    return valores_x, valores_y
# ------------------------------------------------------
# GRAFICA
# ------------------------------------------------------


# def dibujar_grafica (v_x, v_y):
#     # ------------------------------------------------------
#     # VENTANA VACIA
#     # -----------------------------------------------------
#     # plt.plot([1, 2, 3, 4, 5])
#     # plt.show()
#
#     # ------------------------------------------------------
#     # VENTANA POR DEFECTO
#     # -----------------------------------------------------
#     plt.ioff()  # Nos ponemos en modo interactivo
#     plt.figure('valores por defecto')  # Creamos una ventana donde dibujamos el gráfico con la configuración por defecto
#     plt.suptitle('Titulo valores por defecto')  # Esto sirve para poner título dentro de la ventana
#     # plt.plot((1,2,3,4,5), (0, 0.5, 1, 1.5, 2), label = 'por defecto')  # Hacemos el plot
#     plt.plot(v_x, v_y, label='por defecto')
#     plt.legend(loc=2)  # Colocamos la leyenda en la esquina superior izquierda
#     plt.rc('lines', linewidth = 2)  # A partir de aquí todas las líneas que dibujemos irán con ancho doble
#     plt.rc('font', size=18)  # A partir de aquí las fuentes que aparezcan en cualquier gráfico en la misma sesión tendrán mayor tamaño
#
#
#     # ------------------------------------------------------
#     # VENTANA CON PROPIEDADES MODIFICADAS
#     # # -----------------------------------------------------
#     # plt.figure('valores modificados')  # Creamos una ventana donde dibujamos el gráfico con la configuración por defecto
#     # plt.suptitle('Titulo valores modificados')  # Esto sirve para poner título dentro de la ventana
#     # plt.plot((1,2,3,4,5), label = u'linea más ancha y letra más grande')  # Hacemos el plot
#     # plt.legend(loc = 2)  # Colocamos la leyenda en la esquina superior izquierda
#
#     plt.show()


if __name__ == '__main__':
    cljapnn1  = CljaPNN(1, 1, ["vacio", "yogurB"], False, clja_hash_value=1)
    cljapnn2a = CljaPNN(1, 0, [], True, clja_hash_value=2)
    cljapnn2b = CljaPNN(1, 1, [], True, clja_hash_value=3)
    cljapnn3  = CljaPNN(1, 0, [], True, clja_hash_value=4)

    arbol_ftc = {
        cljapnn1: {
            0: None,
            1: {
                cljapnn2a: {
                    0: None
                }
            }
        }
    }

    arbol_ftc_plus = {
        cljapnn1: {
            0: None,
            1: {
                cljapnn2b: {
                    0: None,
                    1: {
                        cljapnn3: {
                            0: None
                        }
                    }
                }
            }
        }
    }

    clja_ftc1 = CljaFtc(arbol_ftc)
    clja_ftc_plus = CljaFtc(arbol_ftc_plus)

    vector_x, vector_y = crear_valores_x_y_v2(1000, clja_ftc1, salto=1)
    # dibujar_grafica(vector_x, vector_y)

    plt.ioff()  # Nos ponemos en modo interactivo
    plt.figure('Función h(x)')  # Creamos una ventana donde dibujamos el gráfico con la configuración por defecto
    plt.axes([0.1, 0.2, 0.8, 0.65])
    plt.suptitle('Naturales útiles vs Naturales totales')  # Esto sirve para poner título dentro de la ventana
    # plt.plot((1,2,3,4,5), (0, 0.5, 1, 1.5, 2), label = 'por defecto')  # Hacemos el plot
    #plt.plot(vector_x, vector_y, label='valores útiles (tanto por uno)')
    plt.plot(vector_x, vector_y)
    plt.legend(loc=2)  # Colocamos la leyenda en la esquina superior izquierda
    plt.rc('lines', linewidth = 2)  # A partir de aquí todas las líneas que dibujemos irán con ancho doble
    plt.rc('font', size=18)  # A partir de aquí las fuentes que aparezcan en cualquier gráfico en la misma sesión tendrán mayor tamaño

    plt.show()
