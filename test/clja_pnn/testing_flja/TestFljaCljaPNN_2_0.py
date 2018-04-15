#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Juan Carlos Caso Alonso'
__project__ = 'clja'

import unittest
from unittest import TestCase
#from test.TrapichedTestCaseOnceSetup import TrapichedTestCaseOnceSetup
from source.cljas.CljaPNN import CljaPNN
from source.conjuntos.camino_finito.CaminoFinito import CaminoFinito


class TestFljaCljaPnn_2_0(TestCase):
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
        unittest.TestCase.setUp(self)
        print ("Ejecutando test de TestFljaCljaPNN_2_0.")
        """
        you want to have persistent things to test
        self.__class__.myclass = MyClass()
        (you can call this later with self.myclass)
        """
        self.__class__.clja_de_pruebas = CljaPNN(2, 0)
        self.__class__.camino_2_8_15 = CaminoFinito([2, 8, 15])

    # Este es el caso que se usa de ejemplo en la documentación teórica:
    def test_flja_2_8_15_w1_eq_182712(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, self.camino_2_8_15), 182712)

    def test_flja_2_8_15_w2_eq_378887(self):
        self.assertEqual(self.clja_de_pruebas.flja(2, self.camino_2_8_15), 378887)

    # Un caso facil de ver: el camino {0,1} sus w1 y w2 son la bola 3 y 4 del hueco "0" de la primera habitacion
    # Recuerda: 4 y 7 son sus indices de salida del saco magico, los naturales asociados son 3 y 6.

    def test_flja_0_1_w1_eq_3(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([0, 1])), 3)

    def test_flja_0_1_w2_eq_6(self):
        self.assertEqual(self.clja_de_pruebas.flja(2, CaminoFinito([0, 1])), 6)

    # Comprobando que ese ultimo caso no da otros valores:
    def test_flja_0_1_w2_no_eq_5(self):
        self.assertNotEqual(self.clja_de_pruebas.flja(2, CaminoFinito([0, 1])), 5)

    #Los w1 de cjtos. de un solo elemento deberían coincidir con la primera bolita, menos uno, de la primera habitación:
    #Los datos los saco de la tabla de ejemplo del documento "Cardinalidad de conjuntos infinitos: una nueva revisión"
    #pag 29 v 4.0
    def test_flja_0_w1_eq_0(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([0])), 0)

    def test_flja_1_w1_eq_2(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([1])), 2)

    def test_flja_2_w1_eq_5(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([2])), 5)

    def test_flja_3_w1_eq_9(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([3])), 9)

    def test_flja_4_w1_eq_14(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([4])), 14)

    def test_flja_5_w1_eq_20(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([5])), 20)

    def test_flja_6_w1_eq_27(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([6])), 27)

    def test_flja_7_w1_eq_35(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([7])), 35)

    def test_flja_8_w1_eq_44(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([8])), 44)

    def test_flja_9_w1_eq_54(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([9])), 54)

    def test_flja_10_w1_eq_65(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([10])), 65)

    def test_flja_11_w1_eq_77(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([11])), 77)

    def test_flja_12_w1_eq_90(self):
        self.assertEqual(self.clja_de_pruebas.flja(1, CaminoFinito([12])), 90)

    #Prueba chorra final:
    def test_flja_12_w1_no_eq_1(self):
        self.assertNotEqual(self.clja_de_pruebas.flja(1, CaminoFinito([12])), 1)

    #Comprobar que devuelve un natural, al menos en los casos extremos vistos por encima:
    def test_flja_is_always_one_natural(self):
        self.assertIsInstance(self.clja_de_pruebas.flja(2, CaminoFinito([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), int)

#FIN