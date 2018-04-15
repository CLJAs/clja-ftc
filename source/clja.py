#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from source.cljas.CljaPNN import CljaPNN
from source.conjuntos.camino_finito.CaminoFinito import CaminoFinito


def leer_opciones():
    print ("Numero de parametros: ", len (sys.argv))
    print ("Lista de parametros: ", sys.argv)
    return 0


def informacion_clja (una_clja, nombre="CLJAPNN: "):
    cadena = nombre + " L=" + str(una_clja.L) + \
                    " HR=" + str(una_clja.get_huecos_rojos()) + \
                    " Previos=" + str(una_clja.previos) + \
                    " CardinalPrevios=" + str(len(una_clja.previos)) + \
                    " Compuesta=" + str(una_clja.compuesta)
    return cadena


def todos_los_w(clja, camino):
    resultados_ws = list()
    for w_actual in range(1, clja.L + 1):
        resultados_ws.append(clja.flja(w_actual, camino))
    return resultados_ws


def imprimir_resultados_de_camino(clja, cf):
    cadena = "Camino: " + str(cf)  + " -> " + str(todos_los_w(clja, cf))
    return cadena

# *********************************************************************************************************************
# MAIN:
# *********************************************************************************************************************


cljapnn1 = CljaPNN(ele=2, hr=0, previos=["vacio", "yogurB"], compuesta=False)
cljapnn2 = CljaPNN(ele=2, hr=1, previos=["vacio", "yogurB"], compuesta=False)



w = 1
print(informacion_clja(cljapnn1, "CLJAPNN1: "))
print(informacion_clja(cljapnn2, "CLJAPNN2: "))

print("\nNIVEL 1: ****************************************************************************************************")
print("CLJAPNN1: " + imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{0}")))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{0}", dr=1)))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{0}", dr=0)) + "\n")

print("CLJAPNN1: " + imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{1}")))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{1}", dr=1)))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{1}", dr=0)) + "\n")

print("CLJAPNN1: " + imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2}")))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{2}", dr=1)))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{2}", dr=0)) + "\n")


print("CLJAPNN1: " + imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{3}")))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{3}", dr=1)))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{3}", dr=0)) + "\n")

print("\nNIVEL 2: ****************************************************************************************************")
print("CLJAPNN1: " + imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,3}")))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{2,3}", dr=1)))
print("CLJAPNN2: " + imprimir_resultados_de_camino(cljapnn2, CaminoFinito("{2,3}", dr=0)) + "\n")

print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,4}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,6}")))

print("\nNIVEL 3: ****************************************************************************************************")
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,6}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,7}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,8}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,9}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,10}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11}")))

print("\nNIVEL 4: ****************************************************************************************************")
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,12}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,13}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,14}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,15}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,16}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,17}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,18}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,19}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,20}")))
print(imprimir_resultados_de_camino(cljapnn1, CaminoFinito("{2,5,11,21}")))



"""
def mierda():
    leer_opciones()
    compuesta = True
    clja1_compuesta = CljaPNN(3, 1, [], compuesta)
    clja1_no_compuesta = CljaPNN(3, 1)  # compuesta = False
    # clja1_compuesta.compuesta = False



    ejemplo_corto = CaminoFinito([0])
    pares = CaminoFinito([0, 2, 4, 6, 8, 10, 12, 14, 16])
    multiplos_4 = CaminoFinito([4, 8, 12, 16, 20, 24, 28, 32, 36])

    natural = clja1_compuesta.flja(1, ejemplo_corto)
    print("Si el camino " + str(ejemplo_corto) + " estuviese compuesto el w1 de su hueco rojo es: " + str(natural))
    natural = clja1_no_compuesta.flja(1, ejemplo_corto)
    print("Si el camino " + str(ejemplo_corto) + " estuviese compuesto su w1 seria: " + str(natural))

    n_pares = list()
    n_pares.append(clja1_compuesta.flja(clja2.flja(1, pares) + 1, CaminoFinito("{0}")))
    n_pares.append(
        clja1_compuesta.flja(clja2.flja(1, CaminoFinito([0, 2, 4, 6, 8, 10, 12, 14, 16])), CaminoFinito("{0,2}")))
    n_pares.append(
        clja1_compuesta.flja(clja2.flja(1, CaminoFinito([0, 2, 4, 6, 8, 10, 12, 14, 16])), CaminoFinito("{0,2,4}")))
    n_pares.append(clja1_compuesta.flja(clja2.flja(1, CaminoFinito([0, 2, 4, 6, 8, 10, 12, 14, 16])),
                                        CaminoFinito("{0,2,4,6,8,10,12}")))

    n_multiplos_4 = list()
    n_multiplos_4.append(clja1_compuesta.flja(clja2.flja(1, multiplos_4), CaminoFinito("{4}")))
    n_multiplos_4.append(clja1_compuesta.flja(clja2.flja(1, multiplos_4), CaminoFinito("{4,8}")))
    n_multiplos_4.append(clja1_compuesta.flja(clja2.flja(1, multiplos_4), CaminoFinito("{4,8,12,16,20}")))

    print(str(n_pares))
    print("Natural asociado a 3 5 7: " + str(clja3.flja(1, CaminoFinito("{3,5,7}"))))
    print(str(n_multiplos_4))
"""