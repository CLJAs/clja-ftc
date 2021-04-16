#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'


class TripletaHuecoPNN:
    # Constantes
    TIPO_DEL_NODO = 'source.arbol_busqueda.arbol_busqueda_pnn.nodo_ab_pnn_file'

    def __str__(self):
        cadena = ""
        cadena += "Hueco: " + self.nombre.__str__()
        cadena += " -> " + self.lista_naturales_asociados.__str__()
        if self.next is None:
            cadena += " CERRADO"
        else:
            cadena += " ENLAZADO"
        return cadena

    def __init__(self, nombre, natural=None, next=None):
        # Constants:

        self.nombre = nombre
        self.next = None
        self.lista_naturales_asociados = list()
        # Esto es un instrumento de inicialización, el caso de poder inicializar la lista debe ser posible.
        # Natural puede ser un solo numero o una lista...

        # TODO: Revisa esto
        if (natural is None) or natural == []:
            self.lista_naturales_asociados = list()
        elif isinstance(natural, list):
            self.lista_naturales_asociados = natural
        elif isinstance(natural, int):
            self.anadir_natural(natural)
        else:
            raise CljaError("El natural no es ni un int ni una lista de int!!!")

        if next is not None:
            self.next = next

    def anadir_natural(self, natural):
        self.lista_naturales_asociados.append(natural)

    def naturales_asociados(self):
        return len(self.lista_naturales_asociados)

    def enlazar_nodo(self, nodo):
        # No se como obtener la clase, pero la clase está sola en su fichero/modulo
        if nodo.__class__.__dict__['__module__'] == self.TIPO_DEL_NODO:
            self.next = nodo
        else:
            raise CljaError("No es un nodo de tipo NodoABPNN!! y lo intentas enlazar en un hueco azul.")

    def esta_vacia(self):
        if len(self.lista_naturales_asociados) == 0:
            return True
        else:
            return False

