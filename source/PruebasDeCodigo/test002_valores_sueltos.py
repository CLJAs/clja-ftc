#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from source.ExcepcionesClja.CljaError import CljaError
from source.cljas.CljaPNN import CljaPNN
from source.cljas.clja_ftc.CljaFtc import CljaFtc
from source.cljas.clja_ftc.ListaCFsCljaFtc import ListaCFsCljaFtc


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
    #Este else está mal aquí, es una herencia vieja, hay que repensarlo.
    else:
        # print("Es un miembro de previos")
        cadena_resultado += " Es un miembro de previos."
    print(cadena_resultado)


cljapnn1  = CljaPNN(1, 1, ["vacio", "yogurB"], False, clja_hash_value=1)
cljapnn2a = CljaPNN(1, 0, [],                  True,  clja_hash_value=2)
cljapnn2b = CljaPNN(1, 1, [],                  True,  clja_hash_value=3)
cljapnn3  = CljaPNN(1, 0, [],                  True,  clja_hash_value=4)

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

mostrar_un_resultado_inverso(clja_ftc1, 2385948034093, test_de_fallo=False)
mostrar_un_resultado_inverso(clja_ftc1, 2385948034094, test_de_fallo=False)
mostrar_un_resultado_inverso(clja_ftc1, 2385948034095, test_de_fallo=False)
mostrar_un_resultado_inverso(clja_ftc1, 3554738929236363, test_de_fallo=False)

