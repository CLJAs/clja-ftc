#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from source.cljas.CljaPNN import CljaPNN
from source.cljas.clja_ftc.ListaCFsCljaFtc import ListaCFsCljaFtc
from source.conjuntos.camino_finito.CaminoFinito import CaminoFinito


class CljaFtc(object):

    def __init__(self, arbol_de_composicion):
        self.arbol = arbol_de_composicion

    # *****************************************************************
    # FLJA DIRECTA:
    # *****************************************************************
    def flja_abosluta(self, w, lista_de_caminos):
        lista_cfs = ListaCFsCljaFtc(lista_de_caminos, tipo_flja=ListaCFsCljaFtc.FLJA_ABSOLUTA)
        return self._flja(w, lista_cfs)

    def flja_practica(self, w, lista_de_caminos):
        lista_cfs = ListaCFsCljaFtc(lista_de_caminos, tipo_flja=ListaCFsCljaFtc.FLJA_PRACTICA)
        return self._flja(w, lista_cfs)

    # Esta es la que hace el calculo de la flja directa
    def _flja(self, w, caminos):
        cljas = self.__extraer_lista_cljas(caminos)
        self.__chequear_cljas_vs_caminos(cljas, caminos)

        # Estamos en las condiciones idóneas para ejecutar la flja directa:
        tb = 0
        k_iteration = w
        for pos in range(len(caminos) - 1, -1, -1):
            clja = cljas[pos]
            camino = caminos[pos]
            tb = clja.flja(k_iteration, camino)
            k_iteration = tb
        # La constante compuesta de cada clja nos dice si añade o no el cardinal de previos o si aplica NW().
        return tb

    def __extraer_lista_cljas(self, caminos):
        lista_cljas = []

        # keys no permite indexacion, de ahi pasarlo a list.
        clja = list(self.arbol.keys())[0]

        # Cojo la lista de opciones para diferentes DRs: pares de un numero y una clja.
        opciones_dr = self.arbol[clja]

        camino = caminos[0]

        indice = 0
        while (indice < len(caminos)) and (camino.dr > 0) and (clja is not None):
            lista_cljas.append(clja)
            clja = list(opciones_dr[camino.dr].keys())[0]
            opciones_dr = opciones_dr[camino.dr]
            indice += 1
            camino = caminos[indice]
        if clja is not None:
            lista_cljas.append(clja)
        return lista_cljas

    def __chequear_cljas_vs_caminos(self, lista_cljas, caminos):
        for indice in range(0, len(lista_cljas)):
            lista_cljas[indice].check_cf(caminos[indice])

    # *****************************************************************
    # FLJA INVERSA:
    # *****************************************************************


    # *****************************************************************
    # PROPERTIES:
    # *****************************************************************
    def _get_arbol(self):
        return self.__arbol

    def _set_arbol(self, nuevo_arbol_de_composicion):
        self.__arbol = nuevo_arbol_de_composicion

    arbol = property(_get_arbol, _set_arbol)


if __name__ == "__main__":
    cljapnn1 = CljaPNN(1, 1, ["vacio", "yogurB"], False, clja_hash_value=1)
    cljapnn2a = CljaPNN(1, 0, [], True, clja_hash_value=2)
    cljapnn2b = CljaPNN(1, 1, [], True, clja_hash_value=2)
    # La 2a y la 3 son del mismo "tipo"... pero por dejarlo más claro, creo la nueva variable 3:
    cljapnn3 = CljaPNN(1, 0, [], True, clja_hash_value=3)

    # TODO:
    # El arbol debe crearse a mano. He pensado en definirlo con json o algo parecido en un fichero:
    # El valor 0 no sé si quitarlo, no debería consultarse nunca.
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

    cf1  = CaminoFinito("{0}", 1)
    cf2a = CaminoFinito("{0}", 0)
    cf2b = CaminoFinito("{0}", 1)
    cf3  = CaminoFinito("{0}", 0)

    cf1b = CaminoFinito("{35,39}", 1)
    cf2b = CaminoFinito("{0}", 0)

    lista_de_caminos_001 = [cf1, cf2a]
    lista_de_caminos_002 = [cf1, cf2b, cf3]
    lista_de_caminos_003 = [cf1b, cf2b]

    clja_ftc1 = CljaFtc(arbol_ftc)
    valor = clja_ftc1.flja_abosluta(1, lista_de_caminos_003)
    print (valor)


