#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

"""
Esta clase intenta representar un camino finito, un subconjunto con elementos finitos de N, el conjunto de los números 
naturales. Las condiciones que hay son:

1.- Deben ser número s naturales obviamente.
2.- Deben estar ordenados de menor a mayor (por exigencias del proyecto que estamos representando: el grafo de caminos
de números naturales que representa a P(N)
3.- No pueden haber elementos repetidos.
4.- Se puede inicializar con un string con formato:
     {[número natural, ]+ número natural}
     4a) sin espacios en blanco.
5.- Cómo deben estar ordenadas, el sieguiente siempre es mayor que el anterior. (Cualquier subconjunto de N, infinito 
o no, tiene la propiedad de estar "bien ordenado" - ver wikipedia -.

La propiedad se llama "lista de coordenadas", pq debe guardarse en una lista, según el algoritmo de cálculo de la 
CljaPNN. Cada número, cada natural de esa lista, es un nodo que se "escoge"! en cada nivel del grafo, y siguiendo la
list, seguimos el camino finito qeu nos lleva al nodo que representa un subconjunto de N con elementos finitos.
"""

from source.ExcepcionesClja.CaminoFinitoNoValido import CaminoFinitoNoValido


class CaminoFinito(object):
    """ En toda lista de coordenadas, que empiezan en la posción uno, en la posición cero, SIEMPRE, está el valor
    lambda cero. En realidad es una constante y debería ser estática... cosas de no dominar pyhton :D."""

    LAMBDA_CERO = -1

    def __init__(self, camino, dr=0):

        """ No uso la asignacion directa de la propiedad por miedo a llamadas infinitas de _set_lista_coordenadas"""
        self._set_lista_coordenadas(camino)
        self.dr = dr

    def m(self):
        # el "-1" es por culpa de LAMBDA_CERO
        return len(self.lista_coordenadas) - 1

    @staticmethod
    def _convertir_a_lista(nueva_lista):
        """ Quito el primer y el último elemento, que son "{" y "}" """

        lista_coordenadas = nueva_lista
        lista_coordenadas = lista_coordenadas[1:-1]
        """
        del(lista_coordenadas[0])
        del(lista_coordenadas[-1])
        
        str no soporta borrado de elementos
        """

        lista_coordenadas = lista_coordenadas.split(",")
        if len(lista_coordenadas) == 0:
            raise CaminoFinitoNoValido("Al separar la cadena, no obtuvimos ningun elemento que chequear.")
        for indice in range(0, len(lista_coordenadas)):
            if lista_coordenadas[indice].isdigit():
                try:
                    lista_coordenadas[indice] = int(lista_coordenadas[indice])
                except ValueError:
                    raise CaminoFinitoNoValido("En el string hay algun numero que no es un entero!! PETADA MORTAL")
            else:
                raise CaminoFinitoNoValido("Se te escapo algun símbolo no numerico (para naturales) " +
                                           "en la definición de algun subconjunto | camino finito")
        return lista_coordenadas

    def _checker(self):
        """Lista de cosas que comprobamos, si fallan lanzan un raise de CaminoFinitoNoValido"""
        self._hay_elementos()
        self._son_todos_naturales()
        self._hay_elementos_repetidos()
        self._estan_ordenados()

    def _hay_elementos(self):
        if not len(self.lista_coordenadas) > 0:
            raise CaminoFinitoNoValido("No hay elementos en la lista de coordenadas")

    def _hay_elementos_repetidos(self):
        """ Comprobando que son únicos todos: """
        for i in range(0, len(self.lista_coordenadas)):
            for j in range(i + 1, len(self.lista_coordenadas)):
                if self.lista_coordenadas[i] == self.lista_coordenadas[j]:
                    raise CaminoFinitoNoValido("Hay elementos repetidos en un camino finito")

    def _estan_ordenados(self):
        """ Quiero parar cuando compare el penultimo con el ultimo, de ahi el menos uno"""
        for indice in range(0, len(self.lista_coordenadas) - 1):
            if self.lista_coordenadas[indice] > self.lista_coordenadas[indice + 1]:
                raise CaminoFinitoNoValido("Los elementos de un camino finito no estan ordenados")

    def _son_todos_naturales(self):
        for numero in self.lista_coordenadas:
            if not (isinstance(numero, int) or isinstance(numero, long)):
                raise CaminoFinitoNoValido("No sé que es pero no es un entero eso que has tratado de meter en un camino")
            if numero < 0:
                raise CaminoFinitoNoValido("Estas intentando meter un numero negativo en algun camino")

    def _set_lista_coordenadas(self, nuevo_camino):
        if isinstance(nuevo_camino, str):
            self.__lista_coordenadas = self._convertir_a_lista(nuevo_camino)
        elif isinstance(nuevo_camino, list):
            self.__lista_coordenadas = nuevo_camino
        elif isinstance(nuevo_camino, set):
            lista = list(nuevo_camino)
            """ 
            Al pasar de un set a un list, los elementos vienen en orden, si no, checker petará
            new comment: ...y vaya que si petaba... de ahí el "sorted"
            """
            self.__lista_coordenadas = sorted(lista)
        else:
            raise CaminoFinitoNoValido("La lista de lambdas no es de ningún tipo admitido")
        self._checker()
        if self.lista_coordenadas[0] != self.LAMBDA_CERO: #LAMBDA_CERO = -1
            self.__lista_coordenadas.insert(0, self.LAMBDA_CERO)
        """ El checker no hace falta en este caso, ya se hizo al crear el otro CaminoFinito"""
        if isinstance(nuevo_camino, CaminoFinito):
            self.__lista_coordenadas = nuevo_camino.lista_coordenadas

    def _get_lista_coordenadas(self):
        return self.__lista_coordenadas

    lista_coordenadas = property(_get_lista_coordenadas, _set_lista_coordenadas)

    def __str__(self):
        # Siempre al menos hay un elemento
        cadena = "{" + str(self.lista_coordenadas[1])
        for i in range(2, len(self.lista_coordenadas)):
            cadena += "," + str(self.lista_coordenadas[i])
        cadena += "}"
        cadena += "DR" + str(self.dr)
        return cadena

    def __eq__(self, other):
        # funciona tal cual esta, vamos bien...
        if not type(other) is CaminoFinito:
            raise TypeError("Estas comparando el tipo :" + str(type(self)) + " un supuesto CaminoFinito con: " + str(type(other)))
        if len(self.lista_coordenadas) != len(other.lista_coordenadas):
            return False
        for i in range(0, len(self.lista_coordenadas)):
            if self.lista_coordenadas[i] != other.lista_coordenadas[i]:
                return False
        return True

    def __hash__(self):
        from source.cljas.CljaPNN import CljaPNN
        aux = CljaPNN(ele=1, hr=0, previos=[], compuesta=False, dr=self.dr)
        resultado = aux.flja(1, self)
        return resultado


if __name__ == "__main__":
    pass
    # el codigo que estba aqui ya esta en los tests.

