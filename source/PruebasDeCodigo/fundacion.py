###!/usr/bin/env python
#### -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from source.cljas.CljaPNN import CljaPNN
from source.cljas.clja_ftc.CljaFtc import CljaFtc
from source.cljas.clja_ftc.ListaCFsCljaFtc import ListaCFsCljaFtc
from source.conjuntos.camino_finito.CaminoFinito import CaminoFinito

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
            #raise CljaError("No coinciden la función directa y la inversa!!")
            print("No coinciden la función directa y la inversa!!")
    else:
        # print("Es un miembro de previos")
        cadena_resultado += " Es un miembro de previos."
    print(cadena_resultado)


cljapnn1  = CljaPNN(1, 1, ["vacio", "yogurB"], False, clja_hash_value=1)
cljapnn2a = CljaPNN(1, 0, [], True, clja_hash_value=2)

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

clja_ftc1 = CljaFtc(arbol_ftc)

fundacion_prime_1 = 86982331
fundacion_prime_2 = 86982341
mostrar_un_resultado_inverso(clja_ftc1, fundacion_prime_1, test_de_fallo=False, falla_en=2)
mostrar_un_resultado_inverso(clja_ftc1, fundacion_prime_2, test_de_fallo=False, falla_en=2)

fundacion_prime_3 = 86982342
mostrar_un_resultado_inverso(clja_ftc1, fundacion_prime_3, test_de_fallo=False, falla_en=2)

fundacion_prime_4 = 86982343
mostrar_un_resultado_inverso(clja_ftc1, fundacion_prime_4, test_de_fallo=False, falla_en=2)

fundacion_prime_5 = 86982344
mostrar_un_resultado_inverso(clja_ftc1, fundacion_prime_5, test_de_fallo=False, falla_en=2)

cat_number = 1093742257065
mostrar_un_resultado_inverso(clja_ftc1, cat_number, test_de_fallo=False, falla_en=2)
