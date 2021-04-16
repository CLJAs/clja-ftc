#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

from unittest import TestCase
from source.cljas.CljaPNN import CljaPNN
from source.conjuntos.camino_finito.CaminoFinito import CaminoFinito
from source.ExcepcionesClja.CljaError import CljaError
from source.ExcepcionesClja.CaminoFinitoNoValido import CaminoFinitoNoValido


class TestCaminoFinito(TestCase):
    """
    http://stezz.blogspot.com.es
    # First define a class variable that determines
    # if setUp was ever run
    """
    ClassIsSetup = False

    def setUp(self):
        # If it was not setup yet, do it
        if not self.ClassIsSetup:
            #print "Initializing testing environment"
            # run the real setup
            self.setupClass()
            # remember that it was setup already
            self.__class__.ClassIsSetup = True

    def setupClass(self):
        # Do the real setup
        TestCase.setUp(self)
        print ("Ejecutando tests de TestCaminoFinito.")
        """
        you want to have persistent things to test
        self.__class__.myclass = MyClass()
        (you can call this later with self.myclass)
        """
        self.__class__.clja_de_pruebas = CljaPNN(2, 0)
        self.__class__.cadena1 = "{1,2,3}"
        self.__class__.lista1 = [4, 19, 23]


    """
    Probando la sobrecarga del operador EQUALS
    """
    def test_equals_1_2_3_eq_1_2_3(self):
        self.assertEqual(CaminoFinito([1, 2, 3]), CaminoFinito([1, 2, 3]))

    def test_equals_1_2_3_eq_1_2_3_4(self):
        self.assertNotEqual(CaminoFinito([1, 2, 3]), CaminoFinito([1, 2, 3, 4]))

    def test_equals_1_2_3_4_eq_1_2_3_5(self):
        self.assertNotEqual(CaminoFinito([1, 2, 3, 4]), CaminoFinito([1, 2, 3, 5]))

    """
    Probando los chequeos de datos
    """
    def _probando_excepciones(self, dato_inicio):
        ha_saltado_una_excepcion = False
        try:
            CaminoFinito(dato_inicio)
        except CaminoFinitoNoValido as error:
            ha_saltado_una_excepcion = True
        except CljaError as error:
            ha_saltado_una_excepcion = True
        return ha_saltado_una_excepcion

    def test_all_ok_cadena_1_2_3(self):
        self.assertEqual(self._probando_excepciones("{1,2,3}"), False)

    def test_all_ok_lista_4_19_23(self):
        self.assertEqual(self._probando_excepciones([4, 19, 23]), False)

    def test_all_no_ok_lista_21_113_67_234(self):
        self.assertEqual(self._probando_excepciones("{21,113,67,234}"), True)

    def test_all_no_ok_lista_21_113_67_234_by_assertRaises(self):
        self.assertRaises(CaminoFinitoNoValido, CaminoFinito, '{21,113,67,234}')

    def test_all_no_ok_space_in_string_1__2_by_assertRaises(self):
        self.assertRaises(CaminoFinitoNoValido, CaminoFinito, '{1, 2}')

    def test_all_no_ok_space_in_string_1__2(self):
        self.assertEqual(self._probando_excepciones("{1, 2}"), True)

    def test_set_all_ok_1_2_3(self):
        self.assertEqual(self._probando_excepciones({1, 2, 3}), False)

    def test_set_all_ok_3_2_1(self):
        self.assertEqual(self._probando_excepciones({3, 2, 1}), False)

    def test_set_all_ok_1024_13_7_1789233546(self):
        self.assertEqual(self._probando_excepciones({1024, 13, 7, 1789233546}), False)

    def test_set_all_ok_7_13_1024_1789233546(self):
        self.assertEqual(self._probando_excepciones({7, 13, 71024, 1789233546}), False)

    def test_no_elementos_repetidos_2_3_17_17_234_by_assertRaises(self):
        self.assertRaises(CaminoFinitoNoValido, CaminoFinito, "{2,3,17,17,234}")

    def test_no_elementos_repetidos_2_3_17_17_234(self):
        self.assertEqual(self._probando_excepciones("{2,3,17,17,234}"), True)
#FIN
