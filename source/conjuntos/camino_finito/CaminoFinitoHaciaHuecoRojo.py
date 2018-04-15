#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from conjuntos.camino_finito.CaminoFinito import CaminoFinito


class CaminoFinitoHaciaHuecoRojo (CaminoFinito):

    def __init__(self, camino,  posicion_hueco_rojo):
        super().__init__(camino)
        self._posicion_relativa = posicion_hueco_rojo

    """
    PROPIEDAD: posicion del hueco rojo respecto al hueco azul pauntado por ese camino.
    """

    def _set_posicion_relativa(self, nueva_pos):
        self._posicion_relativa = nueva_pos

    def _get_posicion_relativa(self):
        return self._posicion_relativa

    posicion_relativa = property(_get_posicion_relativa, _set_posicion_relativa)

    """
    REDEFINICIONES
    """

    def __str__(self):
        cadena = super().__str__()
        return cadena + "R" + str(self.posicion_relativa)


if __name__ == "__main__":
    caminoR1 = CaminoFinitoHaciaHuecoRojo("{1,2,3}", 1)
    print(caminoR1)
