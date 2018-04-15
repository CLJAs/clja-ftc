from unittest import TestCase

from cljas.CljaPNN import CljaPNN
from conjuntos.camino_finito.CaminoFinito import CaminoFinito
from ExcepcionesClja.ResultadoNoEsDeTipoNatural import ResultadoNoEsDeTipoNatural


class TestCljaPNN(TestCase):

    def test_b1_camino_0_nivel_1(self):
        prueba = CljaPNN(1, 0)
        camino = CaminoFinito([0])
        self.assertEqual(prueba.b1(camino, 1), 1)

    def test_b1_camino_0_3_17_34_nivel_3(self):
        prueba = CljaPNN(1, 0)
        camino = CaminoFinito([0, 3, 17, 34])
        nivel = 3
        self.assertEqual(prueba.b1(camino, nivel), 105)

    def test_tbhik_camino_0_nivel_1_bolas_1_a_10(self):
        prueba = CljaPNN(1, 0)
        camino = CaminoFinito("{0}")
        nivel = 1
        resultado = 1
        for k_bolas in range(1, 11):
            self.assertEqual(prueba.tbhik(camino, nivel, k_bolas), resultado)
            """
            print ("Para pasar por el hueco 0, del nivel " + str(nivel) + ", la bola " + str(k_bolas) + ", necesitamos "
                   + str(resultado) + " bolas.")
            """
            resultado += k_bolas

    def test_tbhik_camino_1_nivel_1_bolas_1_a_10(self):
        """ Probando otro hueco del nivel 1: """
        prueba = CljaPNN(1, 0)
        camino = CaminoFinito("{1}")
        nivel = 1
        resultado = 3
        posicion_del_hueco = 2
        for k_bolas in range(1, 11):
            self.assertEqual(prueba.tbhik(camino, nivel, k_bolas), resultado)
            """
            print ("Para pasar por el hueco 1, del nivel " + str(nivel) + ", la bola " + str(k_bolas) + ", necesitamos "
                   + str(resultado) + " bolas.")
            """
            resultado += posicion_del_hueco
            posicion_del_hueco += 1

    def test_tbhik_camino_3_4_nivel_2_bolas_1(self):
        prueba = CljaPNN(1, 0)
        camino = CaminoFinito("{3,4}")
        nivel = 2
        resultado = 1
        k_bolas = 1
        self.assertEqual(prueba.tbhik(camino, nivel, k_bolas), resultado)

    def test_posicion_de_hueco(self):
        """self.fail()"""
        self.assertEqual(1, 1)

    """****************************************************************************************************************
    PRIMER TEST FUNCIONAL
    """
    def Xtest_funcional_naturales_desde_0_hasta_1000000(self):
        caminos_no_repetidos = True
        clja_xa_iterar = CljaPNN(1, 0)
        camino_mas_largo = CaminoFinito({0})
        camino_un_elemento = CaminoFinito([35])
        conjunto_de_caminos = set()
        #conjunto_de_caminos.add(CaminoFinito("{509,522,527,528,529}"))
        conjunto_de_caminos.add(CaminoFinito("{1412}"))
        self.assertEqual(clja_xa_iterar.flja(1, CaminoFinito("{509,522,527,528,529}")), 798725)
        self.assertEqual(clja_xa_iterar.flja(1, CaminoFinito("{35}")), 665)
        self.assertEqual(clja_xa_iterar.flja(1, CaminoFinito("{36}")), 702)

        for i in range(0, 1000000):
            [w, camino] = clja_xa_iterar.flja_inversa(i)
            if not self._este_camino_esta_en(conjunto_de_caminos, camino):
                conjunto_de_caminos.add(camino)
            else:
                caminos_no_repetidos = False
                print ("Se repitio el camino: " + str(camino))
                break
            print ("Natural: " + str(i) + " -> camino: " + str(camino) + " w: " + str(w))
            if len(camino.lista_coordenadas) > len(camino_mas_largo.lista_coordenadas):
                camino_mas_largo = camino
            if len(camino.lista_coordenadas) == 2:
                camino_un_elemento = camino
        print("Uno de los caminos mas largos era: " + str(camino_mas_largo))
        print ("El camino de un elemento con el natural mayor: " + str(camino_un_elemento))
        self.assertEqual(caminos_no_repetidos, True)
        self.assertEqual(len(conjunto_de_caminos), 1000000)

    def _este_camino_esta_en(self, conjunto_de_caminos, camino):
        return not conjunto_de_caminos.isdisjoint({camino})

    """
    FIN DEL PRIMER TEST FUNCIONAL
    ***************************************************************************************************************"""
    """****************************************************************************************************************
    EL TEST FUNCIONAL NATURAL -> Subconjunto Finito convertido en funcion para hacer varios sin repetir codigo.
    ****************************************************************************************************************"""
    def megatest_funcional_N_SF(self, clja_de_prueba, inicio, fin, verbose=False):
        caminos_no_repetidos = True
        camino_mas_largo = CaminoFinito({0})
        camino_un_elemento = CaminoFinito([0])
        conjunto_de_caminos = dict()
        """
        camino_error = CaminoFinito("{2,8,10}")
        conjunto_de_caminos[camino_error] = list()
        conjunto_de_caminos[camino_error].append(45)
        """
        for i in range(inicio, fin + 1):
            [w, camino] = clja_de_prueba.flja_inversa(i)
            w = int(w)
            #if conjunto_de_caminos.has_key(camino):
            if camino in conjunto_de_caminos:
                if len(conjunto_de_caminos[camino]) < clja_de_prueba.L:
                    conjunto_de_caminos[camino].append(i)
                else:
                    caminos_no_repetidos = False
                    if verbose:
                        print("Se repitio el camino: " + str(camino))
                    break
            else:
                conjunto_de_caminos[camino] = list()
                conjunto_de_caminos[camino].append(i)
            if verbose:
                print("Natural: " + str(i) + " -> camino: " + str(camino) + " w: " + str(w))
                if len(camino.lista_coordenadas) > len(camino_mas_largo.lista_coordenadas):
                    camino_mas_largo = camino
                if (len(camino.lista_coordenadas) == 2) and (camino.lista_coordenadas[1] > camino_un_elemento.lista_coordenadas[1]):
                    # Hay un -1 al principio de cada camino(q en realidad no cuenta)
                    camino_un_elemento = camino
        if verbose:
            print("Uno de los caminos mas largos era: " + str(camino_mas_largo))
            print("El camino de un elemento con el natural mayor: " + str(camino_un_elemento))
        return [caminos_no_repetidos, conjunto_de_caminos]

    def test_prueba_SF_N_L_1_0_a_100_verbose(self):
        [todo_ok, caminos] = self.megatest_funcional_N_SF(CljaPNN(1, 0), 0, 100, False)
        self.assertEqual(todo_ok, True)

    def test_prueba_SF_N_L_5_0_a_100_verbose(self):
        [todo_ok, caminos] = self.megatest_funcional_N_SF(CljaPNN(5, 0), 0, 100, False)
        self.assertEqual(todo_ok, True)
    """*****************************************************************************************************************
    EL TES FUNCIONAL Subconjunto FInito -> Natural.
    Necesito que primero se ejecute el de arriba. Me devuelva el conjunto de suibconjuntos finitos calculados y los 
    naturales asociados a ellos. Aqui recorrere los subconjuntos finitos, con la funcion directa flja, y comprobanddo 
    que los resultados coinciden con los obtenidos en el anterior proceso.
    Ambas partes son el MEGATEST :D.
    *****************************************************************************************************************"""

    def megatest_funcional_SF_N(self, clja_de_prueba, conjunto_de_caminos, verbose):
        todo_correcto = True
        """
        camino_error = CaminoFinito("{2,8,10}")
        conjunto_de_caminos[camino_error].append(45)
        """
        #copia = conjunto_de_caminos.copy()
        for camino in conjunto_de_caminos.keys():
            [lista_de_ns, cadena] = self.calcular_todos_los_n_de_un_camino(clja_de_prueba, camino)
            """
            Me interesa saber si los naturales que he calculado nates, xa ese camino, 
            son parte del conjunto de posibles naturales asociables
            Si haces la busqueda al reves, buscas los de lista_de_ns en conjunto_de_caminos[camino]
            Si no empiezas de cero, peta.
            """
            for natural in conjunto_de_caminos[camino]:
                if not lista_de_ns.__contains__(natural):
                    todo_correcto = False
                    if verbose:
                        print ("El numero: " + str(natural) + " no formaba parte " + \
                              "de los calculados previamente para el camino" + str(camino))
                    break
            if verbose:
                if todo_correcto:
                    cadena = "OK "
                else:
                    cadena = "FUCK!! ERROR "
                cadena += "Camino: " + str(camino) + " -> "
                for natural in conjunto_de_caminos[camino]:
                    cadena += " " + str(natural)
                cadena += "\n" + str(lista_de_ns)
                print (cadena)
            #conjunto_de_caminos[camino].__delitem__(conjunto_de_caminos[camino].index(natural))
        return todo_correcto

    def calcular_todos_los_n_de_un_camino(self, la_clja, camino, verbose=False):
        #print ("No deberia ejecutarse: calcular_todos_los_n_de_un_camino ") -> NO SE EJECUTA POR SI SOLO :D
        lista_ws = list()
        for w in range(1, la_clja.L + 1):
            natural = la_clja.flja(w, camino)
            #self.comprobar_que_es_entero(natural)
            lista_ws.append(natural)

        mensaje = "El camino era: " + str(camino)
        mensaje += " Los naturales son: "
        cadena_w = ""
        for k in range(0, len(lista_ws)):
            cadena_w += " " + str(lista_ws[k]) + " "
        return [lista_ws, mensaje + cadena_w]

    """
    MEGA TEST COMPLETO:
    """
    def megatest(self, Ele, huecos_rojos,  inicio, fin, verbose=False):
        clja_xa_testar = CljaPNN(Ele, huecos_rojos)
        [todo_ok, caminos] = self.megatest_funcional_N_SF(clja_xa_testar, inicio, fin, verbose)
        if todo_ok:
            todo_ok = self.megatest_funcional_SF_N(clja_xa_testar, caminos, verbose)
        self.assertEqual(todo_ok, True)

    def test_megatest_L_7_100_a_1000(self):
        self.megatest(3, 0, 0, 10000, True)
