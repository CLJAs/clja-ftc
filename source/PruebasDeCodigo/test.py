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
            raise CljaError("No coinciden la función directa y la inversa!!")
    else:
        # print("Es un miembro de previos")
        cadena_resultado += " Es un miembro de previos."
    print(cadena_resultado)

#TODO: Estas segunda version es mejor, hay que borrar la de arriba
def mostrar_un_resultado_inverso_V2_to_file (clja, numero_natural, test_de_fallo=False, falla_en=9978):
    valor = numero_natural
    w_inverso, camino_inverso = clja.flja_inversa(valor)
    cadena_resultado = str(valor) + " --> " + str(camino_inverso)

    if isinstance(camino_inverso, ListaCFsCljaFtc):
        if isinstance(camino_inverso, str):
            if camino_inverso in clja.previos:
                valor2 = clja.previos.index(camino_inverso)
        else:
            valor2 = clja.flja_absoluta(w_inverso, camino_inverso.lista)
        if (numero_natural == falla_en) and test_de_fallo:
            valor2 += 1
        if valor == valor2:
            # print("COINCIDEN DIRECTO E INVERSO!!")
            cadena_resultado += " OK!!"
        else:
            raise CljaError("No coinciden la función directa y la inversa!!")
    else:
        # print("Es un miembro de previos")
        cadena_resultado += " Es un miembro de previos."
    return cadena_resultado


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

#-------------------------------------
# {1}DR1, {1| 1,2 | 1,2,3}DR0
#-------------------------------------

cf1_1a = CaminoFinito("{1}", dr=1)
cf1_1b = CaminoFinito("{1}", dr=0)
lcf_1 = [cf1_1a, cf1_1b]

cf12_1a = CaminoFinito("{1,2}", dr=1)
cf12_1b = CaminoFinito("{1}", dr=0)
lcf_2 = [cf12_1a, cf12_1b]

cf123_1a = CaminoFinito("{1,2,3}", dr=1)
cf123_1b = CaminoFinito("{1}", dr=0)
lcf_3 = [cf123_1a, cf123_1b]

#-------------------------------------
# {0}DR1, {0| 0,1 | 0,1,2}DR0
#-------------------------------------

cf0_2a = CaminoFinito("{0}", dr=1)
cf0_2b = CaminoFinito("{2}", dr=0)
lcf_4 = [cf0_2a, cf0_2b]

cf01_2a = CaminoFinito("{0,1}", dr=1)
cf01_2b = CaminoFinito("{2}", dr=0)
lcf_5 = [cf01_2a, cf01_2b]

cf012_2a = CaminoFinito("{0,1,2}", dr=1)
cf012_2b = CaminoFinito("{2}", dr=0)
lcf_6 = [cf012_2a, cf012_2b]

#-------------------------------------
# {0}DR1, {0| 0,1 | 0,1,2}DR0
#-------------------------------------

cf0_0a = CaminoFinito("{0}", dr=1)
cf0_0b = CaminoFinito("{0}", dr=0)
lcf_7 = [cf0_0a, cf0_0b]

cf0_01a = CaminoFinito("{0}", dr=1)
cf0_01b = CaminoFinito("{0,1}", dr=0)
lcf_8 = [cf0_01a, cf0_01b]

cf0_012a = CaminoFinito("{0}", dr=1)
cf0_012b = CaminoFinito("{0,1,2}", dr=0)
lcf_9 = [cf0_012a, cf0_012b]

#-------------------------------------
# {1}DR1, {0| 0,1 | 0,1,2}DR0
#-------------------------------------

cf1_0a = CaminoFinito("{1}", dr=1)
cf1_0b = CaminoFinito("{0}", dr=0)
lcf_10 = [cf1_0a, cf1_0b]

cf1_01a = CaminoFinito("{1}", dr=1)
cf1_01b = CaminoFinito("{0,1}", dr=0)
lcf_11 = [cf1_01a, cf1_01b]

cf1_012a = CaminoFinito("{1}", dr=1)
cf1_012b = CaminoFinito("{0,1,2}", dr=0)
lcf_12 = [cf1_012a, cf1_012b]

#-------------------------------------
# Variantes de un solo camino finito
#-------------------------------------

cfp_0  = CaminoFinito("{2,3,5,7,11,13,17}", dr=0)
cfp_0a = CaminoFinito("{2,3,5,7,11,13,17}", dr=1)
cfp_0b = CaminoFinito("{2}", dr=0)
cfp_0c = CaminoFinito("{2,3}", dr=0)
lcfp_1 = [cfp_0a, cfp_0b]
lcfp_2 = [cfp_0a, cfp_0c]
lcfp    = [cfp_0]

cfp_1  =  CaminoFinito("{2,3,5,8,11,13,17}", dr=0)
cfp_2  =  CaminoFinito("{2,3,5,9,11,13,17}", dr=0)
cfp_3  =  CaminoFinito("{2,3,5,10,11,13,17}", dr=0)
cfp_3b =  CaminoFinito("{2,3,5,10,11,13,17}", dr=1)

lcfp_3 = [cfp_1]
lcfp_4 = [cfp_2]
lcfp_5 = [cfp_3]
lcfp_6 = [cfp_3b, cfp_0b]

cf30kk_1 = CaminoFinito("{0,59,61}", dr=1)
cf30kk_2 = CaminoFinito("{0,59}", dr= 0)
lcf_30kk = [cf30kk_1, cf30kk_2]

cf_2_6 = CaminoFinito("{2,6}", dr=1)
cf_3_4 = CaminoFinito("{3,4}", dr=0)
lcf_mario_4 = [cf_2_6, cf_3_4]
lcf_mario_3 = [cf_3_4]


#**************************************
# TEST:
#**************************************

lista = [lcf_1, lcf_2, lcf_3, lcf_4, lcf_5, lcf_6, lcf_7, lcf_8, lcf_9, lcf_10, lcf_11, lcf_12, lcfp_1,
        lcfp_2, lcfp, lcfp_1, lcfp_2, lcfp_3, lcfp_4, lcfp_5, lcfp_6, lcf_30kk, lcf_mario_4, lcf_mario_3]


def formatear_natural (numero, cantidad_digitos):
    cadena = str(numero)
    digitos_que_faltan = cantidad_digitos - len(cadena)
    for i in range (0, digitos_que_faltan):
        cadena = "0" + cadena
    return cadena


def prueba_sin_fichero (inicio, final):
    for i in range(inicio, final):
        linea = mostrar_un_resultado_inverso_V2_to_file(clja_ftc1, i, test_de_fallo=False, falla_en=2)
        print(linea)


def prueba_a_fichero(inicio, final):
    cantidad_por_fichero = 1000000
    index_fichero = 0
    contador_de_lineas = 0
    fichero = open("salida_test_" + formatear_natural(index_fichero, cantidad_digitos=5) + ".txt", "w")

    for i in range(inicio, final):
        linea = mostrar_un_resultado_inverso_V2_to_file(clja_ftc1, i, test_de_fallo=False, falla_en=2)
        fichero.writelines([linea + "\n"])
        print(linea)
        contador_de_lineas += 1
        if contador_de_lineas == cantidad_por_fichero:
            contador_de_lineas = 0
            fichero.close()
            index_fichero += 1
            fichero = open("salida_test_" + formatear_natural(index_fichero, cantidad_digitos=5) + ".txt", "w")
    fichero.close()

#********** EJECUCION DEL TEST *************************
prueba_sin_fichero(1,60000)
#*******************************************************


for lcf in lista:
    natural = clja_ftc1.flja_absoluta(1, lcf)
    cadena = str(ListaCFsCljaFtc(lcf, tipo_flja=ListaCFsCljaFtc.FLJA_ABSOLUTA)) + " : -> " + str(natural)
    print(cadena)

numero = 1872623783828828877
mostrar_un_resultado_inverso(clja_ftc1, numero, test_de_fallo=False, falla_en=2)

cf_nice_str = "{69,420}"
test_cf_nice = CaminoFinito(cf_nice_str)
natural = clja_ftc1.flja_absoluta(1, [test_cf_nice])
print("\nEl resultado de: ", test_cf_nice, " es - > ", natural, "\n")

mostrar_un_resultado_inverso(clja_ftc1, 183, test_de_fallo=False, falla_en=2)
mostrar_un_resultado_inverso(clja_ftc1, 96, test_de_fallo=False, falla_en=2)
mostrar_un_resultado_inverso(clja_ftc1, 188, test_de_fallo=False, falla_en=2)
print("\n\n Neil pi test: ")
neil_number = 14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664
mostrar_un_resultado_inverso(clja_ftc1, neil_number, test_de_fallo=False, falla_en=2)
