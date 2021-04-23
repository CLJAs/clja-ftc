###!/usr/bin/env python
#### -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from source.ExcepcionesClja.CljaError import CljaError
from source.cljas.CljaPNN import CljaPNN
from source.cljas.clja_ftc.CljaFtc import CljaFtc
from source.cljas.clja_ftc.ListaCFsCljaFtc import ListaCFsCljaFtc
from source.conjuntos.camino_finito.CaminoFinito import CaminoFinito

#*********************************************************************+
#           INICIALIZACIÓN
#**********************************************************************

def mostrar_un_resultado_inverso_v2_to_file (clja, numero_natural, test_de_fallo=False, falla_en=9978):
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


#*********************************************+
# Datos de prueba
#**********************************************

def imrpimir_la_lista(lista):
    for lcf in lista:
        natural = clja_ftc1.flja_absoluta(1, lcf)
        #Raruno pero los lcfs son solo listas de CaminosFinitos sin instanciar la clase ListaCFsCljaFtc
        cadena = str(ListaCFsCljaFtc(lcf, tipo_flja=ListaCFsCljaFtc.FLJA_ABSOLUTA)) + " --> " + str(natural)
        print(cadena)


lista_de_lcfs = list()

#----------- PRIMERA TIRA DE EJEMPLOS---------------------

cf_1_1_a = CaminoFinito("{0,3,5}", dr=0)
cf_1_2_b = CaminoFinito("{0}", dr=0)
cf_1_2_c = CaminoFinito("{0,3}", dr=0)
cf_1_2_d = CaminoFinito("{0,3,5}", dr=0)
cf_1_2_e = CaminoFinito("{5347,1000567648}", dr=0)

lcf_1_a = [cf_1_1_a]
lcf_1_b = [cf_1_1_a, cf_1_2_b]
lcf_1_c = [cf_1_1_a, cf_1_2_c]
lcf_1_d = [cf_1_1_a, cf_1_2_d]
lcf_1_e = [cf_1_1_a, cf_1_2_e]

lista_de_lcfs.append(lcf_1_a)
lista_de_lcfs.append(lcf_1_b)
lista_de_lcfs.append(lcf_1_c)
lista_de_lcfs.append(lcf_1_d)
lista_de_lcfs.append(lcf_1_e)

print("\nPRIMERA TANDA DE DATOS: \n")
imrpimir_la_lista(lista_de_lcfs)

#----------- SEGUNDA TIRA DE EJEMPLOS---------------------

cf_2_1_a = CaminoFinito("{0,3,5}", dr=1)

lcf_2_a = [cf_1_1_a]
lcf_2_b = [cf_2_1_a, cf_1_2_b]
lcf_2_c = [cf_2_1_a, cf_1_2_c]
lcf_2_d = [cf_2_1_a, cf_1_2_d]
lcf_2_e = [cf_2_1_a, cf_1_2_e]

lista_de_lcfs.clear()
lista_de_lcfs.append(lcf_2_a)
lista_de_lcfs.append(lcf_2_b)
lista_de_lcfs.append(lcf_2_c)
lista_de_lcfs.append(lcf_2_d)
lista_de_lcfs.append(lcf_2_e)

print("\nSEGUNDA TANDA DE DATOS: \n")
imrpimir_la_lista(lista_de_lcfs)

#----------- TERCERA TIRA DE EJEMPLOS---------------------

cf_3_1_a_dr0 = CaminoFinito("{1,3,5}", dr=0)
cf_3_1_a_dr1 = CaminoFinito("{1,3,5}", dr=1)


lcf_3_a = [cf_3_1_a_dr0]
lcf_3_b = [cf_3_1_a_dr1, cf_1_2_b]
lcf_3_c = [cf_3_1_a_dr1, cf_1_2_c]
lcf_3_d = [cf_3_1_a_dr1, cf_1_2_d]
lcf_3_e = [cf_3_1_a_dr1, cf_1_2_e]

lista_de_lcfs.clear()
lista_de_lcfs.append(lcf_3_a)
lista_de_lcfs.append(lcf_3_b)
lista_de_lcfs.append(lcf_3_c)
lista_de_lcfs.append(lcf_3_d)
lista_de_lcfs.append(lcf_3_e)

print("\nTERCERA TANDA DE DATOS: \n")
imrpimir_la_lista(lista_de_lcfs)

#----------- CUARTA TIRA DE EJEMPLOS---------------------

print("\nEsto es solo para recordarme mencionaros este caso:\n")
cf_4_1_a = CaminoFinito("{0,1,2,3,4,5,6,7}", dr=1)
cf_4_2_a = CaminoFinito("{1,2,3,4,5,6,7}", dr=0)

lcf_4_a = [cf_4_1_a, cf_4_2_a]
lista_de_lcfs.clear()
lista_de_lcfs.append(lcf_4_a)
imrpimir_la_lista(lista_de_lcfs)

print("\nAquí no sé si va a petar el código:\n")
cf_3_1_a_dr1 = CaminoFinito("{1,3,5}", dr=1)
lcf_4_b = [cf_3_1_a_dr1]
lista_de_lcfs.clear()
lista_de_lcfs.append(lcf_4_b)
imrpimir_la_lista(lista_de_lcfs)



