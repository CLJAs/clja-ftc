#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from source.ExcepcionesClja.LsitaCFsNoValida import ListaCFsNoValida
from source.conjuntos.camino_finito.CaminoFinito import CaminoFinito


class ListaCFsCljaFtc(object):
    FLJA_ABSOLUTA = False
    FLJA_PRACTICA = True

    #EL tipo solo se aplica a los chequeos y las restricciones, los cálculos son idénticos en ambos casos.
    def __init__(self, lista, tipo_flja=FLJA_PRACTICA):
        self.lista = lista.copy()
        self.__check_lista(tipo_flja)
        #Quito todos los cfs más allá del primero con dr=0
        self.__clean()

    def __check_lista(self, tipo):
        if len(self.lista) > 0:
            """
            Cada Clja diferente tiene un método para chequear si un camino es "correcto" para ella.
            Este código sobra.
            for cf in self.lista:
                if not isinstance(cf, CaminoFinito):
                    raise ListaCFsNoValida ("Hay un miembro de la lista que no es un CaminoFinito")
            """

            if tipo == self.FLJA_PRACTICA:
                if len(self.lista) == 1:
                    if self.lista[0].dr != 0: #Ya se seguro que es un CaminoFinito
                        raise ListaCFsNoValida("Solo hay un CF y no tiene dr=0")
                elif (len(self.lista) == 2) or (len(self.lista) == 3):
                    elem1 = self.lista[0].lista_coordenadas[1]
                    elem2 = self.lista[len(self.lista) - 1].lista_coordenadas[1]
                    #Sirve para Lista de 2 CFs y de 3 CFs... pq el CF de en medio(3), puede ser cualquiera!
                    if not elem1 == elem2:
                        raise ListaCFsNoValida("No son inicio del mismo SNEI!!")
                else:
                    raise ListaCFsNoValida("Es flja PRACTICA y tiene tres o más CFs en la lista")
        else:
            raise ListaCFsNoValida("Error inesperado.")

    def check_lcf2p(self, tipo=FLJA_PRACTICA):
        if len(self.lista) == 2:
            this_cf1 = self.lista[0]
            this_cf2 = self.lista[1]
            lambdas1 = len(this_cf1.lista_coordenadas)
            lambdas2 = len(this_cf2.lista_coordenadas)
            if this_cf1.dr == 1 and this_cf2.dr == 0:
                if lambdas1 <= lambdas2:
                    longitud_mas_corta = lambdas1
                else:
                    longitud_mas_corta = lambdas2
                for i in range(0, longitud_mas_corta):
                    if this_cf1.lista_coordenadas[i] != this_cf2.lista_coordenadas[i]:
                        return False
        return True

    def check_lcf1(self):
        if (len(self.lista) == 1) and (self.lista[0].dr == 0):
            return True
        return False

    def __clean(self):
        #Borramos todos los caminos después del primero con dr=0
        #Sea práctica o absoluta, después de un dr=0, no hay vida :D.
        pos_xa_borrar = len(self.lista)
        encontrada_posicion = False
        pos = 0
        for cf in self.lista:
            if (cf.dr == 0) and (not encontrada_posicion):
                encontrada_posicion = True
                pos_xa_borrar = pos + 1
            pos += 1
        if pos_xa_borrar < len(self.lista):
            del self.lista[pos_xa_borrar:len(self.lista)]

    def _get_lista(self):
        return self.__lista

    def _set_lista(self, nueva_lista):
        self.__lista = nueva_lista

    lista = property(_get_lista, _set_lista)

    def __len__(self):
        return len(self.lista)

    def __getitem__(self, item):
        return self.lista[item]

    def __str__(self):
        cadena = '('
        if len(self.lista) > 1:
            cadena += str(self.lista[0])
            for i in range(1, len(self.lista)):
                cadena += ", " + str(self.lista[i])
            cadena += ')'
        else:
            if len(self.lista) == 1:
                cadena += str(self.lista[0]) + ')'
        return cadena


if __name__ == "__main__":
    cf1 = CaminoFinito("{1,2,3,4,5,6}", dr=0)
    cf2 = CaminoFinito("{1,2,3,4,5,7}", dr=0)
    cf3 = CaminoFinito("{1,2,3}", dr=1)
    cf4 = CaminoFinito("{7,11,1024}", dr=0)

    lista_cfs_1 = ListaCFsCljaFtc([cf1, cf2], ListaCFsCljaFtc.FLJA_ABSOLUTA)

    # lista_cfs_2 = ListaCFsCljaFtc([cf3])
    lista_cfs_3 = ListaCFsCljaFtc([cf2, cf1])
    # lista_cfs_4 = ListaCFsCljaFtc([cf1, cf4])
    lista_cfs_5 = ListaCFsCljaFtc([cf1, cf4, cf2])
    # lista_cfs_6 = ListaCFsCljaFtc([cf1, cf2, cf4])
    lista_cfs_7 = ListaCFsCljaFtc([cf3, cf3, cf3, cf4], ListaCFsCljaFtc.FLJA_ABSOLUTA)
    # lista_cfs_8 = ListaCFsCljaFtc([cf1, cf2, cf3, cf4], ListaCFsCljaFtc.FLJA_PRACTICA)
