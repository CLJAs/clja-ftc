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

camino_01 = CaminoFinito("{1,2,3,4,13}", dr=0)
camino_02 = CaminoFinito("{1,2,3,12,13}", dr=0)
camino_03 = CaminoFinito("{1,2,11,12,13}", dr=0)
camino_04 = CaminoFinito("{1,10,11,12,13}", dr=0)

lcf_01 = ListaCFsCljaFtc([camino_01])
lcf_02 = ListaCFsCljaFtc([camino_02])
lcf_03 = ListaCFsCljaFtc([camino_03])
lcf_04 = ListaCFsCljaFtc([camino_04])

print(str(lcf_01) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_01.lista)))
print(str(lcf_02) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_02.lista)))
print(str(lcf_03) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_03.lista)))
print(str(lcf_04) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_04.lista)))


camino_01_dr1 = CaminoFinito("{0}", dr=0)
camino_02_dr1 = CaminoFinito("{1}", dr=0)

camino_01b = CaminoFinito("{1,2,3,4,13}", dr=1)
camino_02b = CaminoFinito("{1,2,3,12,13}", dr=1)
camino_03b = CaminoFinito("{1,2,11,12,13}", dr=1)
camino_04b = CaminoFinito("{1,10,11,12,13}", dr=1)

lcf_01b = ListaCFsCljaFtc([camino_01b, camino_02_dr1])
lcf_02b = ListaCFsCljaFtc([camino_02b, camino_02_dr1])
lcf_03b = ListaCFsCljaFtc([camino_03b, camino_02_dr1])
lcf_04b = ListaCFsCljaFtc([camino_04b, camino_02_dr1])

print(str(lcf_01b) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_01b.lista)))
print(str(lcf_02b) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_02b.lista)))
print(str(lcf_03b) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_03b.lista)))
print(str(lcf_04b) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_04b.lista)))

lcf_01c = ListaCFsCljaFtc([camino_01b, camino_01_dr1], tipo_flja=ListaCFsCljaFtc.FLJA_ABSOLUTA)
lcf_02c = ListaCFsCljaFtc([camino_02b, camino_01_dr1], tipo_flja=ListaCFsCljaFtc.FLJA_ABSOLUTA)
lcf_03c = ListaCFsCljaFtc([camino_03b, camino_01_dr1], tipo_flja=ListaCFsCljaFtc.FLJA_ABSOLUTA)
lcf_04c = ListaCFsCljaFtc([camino_04b, camino_01_dr1], tipo_flja=ListaCFsCljaFtc.FLJA_ABSOLUTA)

print(str(lcf_01c) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_01c.lista)))
print(str(lcf_02c) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_02c.lista)))
print(str(lcf_03c) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_03c.lista)))
print(str(lcf_04c) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_04c.lista)))

w1 = 0
camino_inverso_01 = None
valor = 28383939492029372829
w1, camino_inverso_01 = clja_ftc1.flja_inversa(valor)
print(str(valor) + " -> " + str(camino_inverso_01))


valor = 23271000000
w1, camino_inverso_01 = clja_ftc1.flja_inversa(valor)
print("Km:" + str(valor) + " -> " + str(camino_inverso_01))

valor = 14460000000
w1, camino_inverso_01 = clja_ftc1.flja_inversa(valor)
print("Miles:" + str(valor) + " -> " + str(camino_inverso_01))


camino_ovejas = CaminoFinito("{435,436,437,438,439}", dr=0)
lcf_ovejas = ListaCFsCljaFtc([camino_ovejas], tipo_flja=ListaCFsCljaFtc.FLJA_ABSOLUTA)
print(str(lcf_ovejas) + " -> " + str(clja_ftc1.flja_absoluta(1, lcf_ovejas.lista)))
