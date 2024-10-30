import unittest
import traceback
from farmacia import Farmacia, Medicamento
from test_builder import TestBuilder9


def gen_lst_medicamentos(prb):
    """
    Función especial que permite la creación de medicamentos utilizados en las
    diferentes pruebas, devolviendo una lista de tuplas con el medicamento y un
    valor booleano que representa que el medicamento será adicionado a los
    diferentes estantes de la farmacia, especialmente en el test_1_registro. Para
    las demás pruebas, se devuelve una lista con los medicamentos que se
    deberían adicionar a la farmacia.
    """
    med1 = Medicamento("med_1", "comprimido", 800, 10)
    med2 = Medicamento("med_2", "comprimido", 500, 5)
    med3 = Medicamento("med_1", "jarabe", 2500, 5)
    med4 = Medicamento("med_1", "cápsula", 1200, 10)
    med5 = Medicamento("med_2", "cápsula", 900, 8)
    med6 = Medicamento("med_3", "comprimido", 750, 7)
    med7 = Medicamento("med_4", "comprimido", 200, 5)
    med8 = Medicamento("med_2", "jarabe", 2000, 10)
    med9 = Medicamento("med_3", "cápsula", 1100, 8)
    med10 = Medicamento("med_5", "comprimido", 600, 8)

    if prb == 0:
        lst_medicamento = [(med1, (927.9999999999999, 10)), (med2, (580.0, 5)),
                           (med3, (2950.0, 5)), (med4, (1404.0, 10)),
                           (med5, (1053.0, 8)), (med6, (869.9999999999999, 7)),
                           (med7, (231.99999999999997, 5)),
                           (med8, (2360.0, 10)), (med9, (1287.0, 8)),
                           (med10, (696.0, 8))]
    else:
        lst_medicamento = [med1, med2, med3, med4, med5, med6, med7, med8,
                           med9, med10]
    return lst_medicamento


class Droga:
    def __init__(self, nombre, presentación, psi, existencias):
        self.nombre = nombre
        self.presentacion = presentación
        self.psi = psi
        self.existencias = existencias


class TestFarmacia(TestBuilder9):
    # Es posible desactivar cualquiera de las pruebas colocando el valor de
    # cero a cualquiera de ellas en el siguiente diccionario:
    dict_pruebas = {"registro": 10, "colocar": 10, "quitar": 10, "venta": 10,
                    "consultar": 10}

    def setUp(self):
        # Creación de la Farmacia con un nombre inicial
        self.farmacia = Farmacia("Farmacia ACME")

    def test_0(self):
        self.presentación("Test Farmacia de Medicamentos")

    def test_1_registro(self):
        iTest = 1
        sTitle = "Ingreso de medicamentos a la Farmacia"
        fMax_nota = 1.0
        Nt1_1 = fMax_nota * 0.20 / 5
        Nt1_2 = fMax_nota * 0.30 / 7
        Nt1_3 = fMax_nota * 0.10 / 2
        Nt1_5 = fMax_nota * 0.10 / 3
        if self.dict_pruebas.get("registro"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Poner maxDiff a None para aceptar cadenas muy muy largas.
            self.maxDiff = None

            # Comprobación de la entrada de Medicamento ingresado a la farmacia
            # que debe ser de tipo comprimido, cápsula u jarabe
            lst_medicamento = gen_lst_medicamentos(0)
            Nt1_4 = fMax_nota * 0.30 / len(lst_medicamento)
            cr_i = 0
            le = (traceback.extract_stack()[-1])[1] + 2
            for med in lst_medicamento:
                self.comprobarAserción2(med[1],
                                        self.farmacia.registro, [med[0]],
                                        Nt1_4, le, cr_i)
                cr_i += 1

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, self.farmacia.cantidad_farmacia,
                                    [], Nt1_3, le)

            # Comprobación de la validación de precio sin iva y presentación de
            # objetos de tipo Medicamento
            try:
                # Medicamento con precio sin iva igual a 0
                med11 = Medicamento("med_6", "comprimido", 0, 10)
                self.farmacia.registro(med11)
            except ValueError as e:
                print(e)
                self.comprobarAserción(True, True, "Medicamento no creado!", Nt1_1, 0)
            try:
                # Medicamento con tipo de presentación no admitida
                med12 = Medicamento("med_1", "suspención", 1200, 10)
                self.farmacia.registro(med12)
            except ValueError as e:
                print(e)
                self.comprobarAserción(True, True, "Medicamento no creado!", Nt1_1, 0)

            # Medicamento con un valor de existencia negativo: se convierte en
            # existencias de 10 unidades
            med13 = Medicamento("med_1", "jarabe", 2000, -1)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2((2360.0, 15), self.farmacia.registro, [med13],
                                    Nt1_1, le)

            # Modificamos el precio sin IVA de un objeto de tipo medicamento
            # que tiene inicialente un valor correcto, superior a cero
            med11 = Medicamento("med_6", "comprimido", 600, 8)
            try:
                # Comprobamos si la clase Medicamento tiene el atributo de
                # precio sin IVA
                le = (traceback.extract_stack()[-1])[1] + 1
                if hasattr(med11, "psi"):
                    med11.psi = 0
                    input("nn")
                else:
                    print("ATENCION: Modificar las líneas " + str(le) +
                          " y " + str(le + 1) + " con el nombre del" +
                          " atributo de la clase Medicamento que guarda" +
                          " el 'precio sin IVA', para obtener una mejor" +
                          " calificación.\n\n")
                self.farmacia.registro(med11)
            except ValueError as e:
                print(e)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(696.0, med11.pvp, [], Nt1_1, le)

            # Modificamos el tipo de presentación de un objeto de tipo
            # medicamento que tiene inicialente un valor correcto: cápsula
            med12 = Medicamento("med_4", "cápsula", 1100, 8)
            try:
                # Comprobamos si la clase Medicamento tiene el atributo de
                # precio sin IVA
                le = (traceback.extract_stack()[-1])[1] + 1
                if hasattr(med12, "presentacion"):
                    med12.presentacion = "pastilla"
                else:
                    print("ATENCION: Modificar las líneas " + str(le) +
                          " y " + str(le + 1) + " con el nombre del" +
                          " atributo de la clase Medicamento que guarda" +
                          " la 'presentación', para obtener una mejor" +
                          " calificación.\n\n")
                self.farmacia.registro(med12)
            except ValueError as e:
                print(e)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción("cápsula", med12.presentacion,
                                       "Medicamento valida presentación de 'capsula' y no de 'pastilla'", Nt1_1, le)

            # Comprobación de la validación de medicamento ya existente en la
            # farmacia cuyos valores de precio sin IVA y existencias seran
            # modificados
            le = (traceback.extract_stack()[-1])[1] + 2
            med1 = Medicamento("med_1", "comprimido", 700, 9)  # 700, 19
            self.comprobarAserción2((812.0, 19), self.farmacia.registro, [med1],
                                    Nt1_2, le)
            c_p = "med_1/comprimido - $812.0 | 19"
            med1c = Medicamento("med_1", "comprimido")
            self.comprobarAserción2(c_p, self.farmacia.consultar, [med1c],
                                    Nt1_2, le + 3)

            le = (traceback.extract_stack()[-1])[1] + 2
            med5 = Medicamento("med_2", "cápsula", 1000, 18)  # 1000, 26
            self.comprobarAserción2((1053.0, 26), self.farmacia.registro, [med5],
                                    Nt1_2, le)
            c_p = "med_2/cápsula - $1053.0 | 26"
            med5 = Medicamento("med_2", "cápsula")
            self.comprobarAserción2(c_p, self.farmacia.consultar, [med5],
                                    Nt1_2, le + 3)

            le = (traceback.extract_stack()[-1])[1] + 2
            med3 = Medicamento("med_1", "jarabe", 1900, 5)  # 1900, 20
            self.comprobarAserción2((2242.0, 20), self.farmacia.registro, [med3],
                                    Nt1_2, le)
            c_p = "med_1/jarabe - $2242.0 | 20"
            med3c = Medicamento("med_1", "jarabe")
            self.comprobarAserción2(c_p, self.farmacia.consultar, [med3c],
                                    Nt1_2, le + 3)

            # Validación de la Homogeneidad de la Farmacia
            le = (traceback.extract_stack()[-1])[1] + 2
            med1x = Droga("med_4", "cápsula", 700, 15)
            self.comprobarAserción2((-1, -1), self.farmacia.registro, [med1x],
                                    Nt1_2, le)

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, self.farmacia.cantidad_farmacia,
                                    [], Nt1_3, le)

            # Comprobación de los estantes de la farmacia
            cad_com = """Presentación: comprimido
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                         700.0          812.0           19
med_2                         500.0          580.0            5
med_3                         750.0          870.0            7
med_4                         200.0          232.0            5
med_5                         600.0          696.0            8
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_com, self.farmacia.ver_estante,
                                    ['comprimido'], Nt1_5, le)
            cad_cap = """Presentación: cápsula
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          1200         1404.0           10
med_2                           900         1053.0           26
med_3                          1100         1287.0            8
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_cap, self.farmacia.ver_estante,
                                    ['cápsula'], Nt1_5, le)
            cad_jar = """Presentación: jarabe
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          1900         2242.0           20
med_2                          2000         2360.0           10
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_jar, self.farmacia.ver_estante,
                                    ['jarabe'], Nt1_5, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_2_colocar(self):
        iTest = 2
        sTitle = "Colocar el medicamento en un estante de la Farmacia"
        fMax_nota = 1.2
        Nt2_1 = fMax_nota * 0.25 / 6
        Nt2_2 = fMax_nota * 0.15 / 2
        Nt2_4 = fMax_nota * 0.15 / 6
        if self.dict_pruebas.get("colocar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Adición de medicamento cuando los estantes estan vacíos
            med11 = Medicamento("med_6", "comprimido", 500, 10)
            med12 = Medicamento("med_4", "cápsula", 1000, 10)
            med13 = Medicamento("med_3", "jarabe", 1900, 10)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.farmacia.colocar,
                                    [med11, -1], Nt2_1, le)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.farmacia.colocar,
                                    [med11, 0], Nt2_1, le)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.farmacia.colocar,
                                    [med12, 1], Nt2_1, le)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.farmacia.colocar,
                                    [med12, 0], Nt2_1, le)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.farmacia.colocar,
                                    [med13, 0], Nt2_1, le)

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(3, self.farmacia.cantidad_farmacia,
                                    [], Nt2_2, le)

            # Comprobación de los estantes de la farmacia
            cad_com = """Presentación: comprimido
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_6                         500.0          580.0           10
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_com, self.farmacia.ver_estante,
                                    ['comprimido'], Nt2_4, le)
            cad_cap = """Presentación: cápsula
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_4                          1000         1170.0           10
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_cap, self.farmacia.ver_estante,
                                    ['cápsula'], Nt2_4, le)
            cad_jar = """Presentación: jarabe
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_3                          1900         2242.0           10
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_jar, self.farmacia.ver_estante,
                                    ['jarabe'], Nt2_4, le)

            # Inserción de Medicamento en diferentes posiciones de los estantes
            lst_medicamento = gen_lst_medicamentos(1)
            Nt2_3 = fMax_nota * 0.45 / len(lst_medicamento)
            cr_i = 0
            posiciones = [(True, 1), (False, 3), (True, 0), (True, 1),
                          (False, -1), (True, 2), (True, 0), (False, 3),
                          (True, 2), (False, 5)]

            le = (traceback.extract_stack()[-1])[1] + 2
            for med in lst_medicamento:
                self.comprobarAserción2(posiciones[cr_i][0],
                                        self.farmacia.colocar,
                                        [med, posiciones[cr_i][1]],
                                        Nt2_3, le, cr_i)
                cr_i += 1

            # Validación de la Homogeneidad de la Farmacia
            le = (traceback.extract_stack()[-1])[1] + 2
            med1x = Droga("cápsula", "raza_x", 200, 6)
            self.comprobarAserción2(False,
                                    self.farmacia.colocar,
                                    [med1x, 0], Nt2_1, le)

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(9, self.farmacia.cantidad_farmacia,
                                    [], Nt2_2, le)

            # Comprobación de los estantes de la farmacia
            cad_com = """Presentación: comprimido
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_4                         200.0          232.0            5
med_6                         500.0          580.0           10
med_1                         800.0          928.0           10
med_3                         750.0          870.0            7
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_com, self.farmacia.ver_estante,
                                    ['comprimido'], Nt2_4, le)
            cad_cap = """Presentación: cápsula
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_4                          1000         1170.0           10
med_1                          1200         1404.0           10
med_3                          1100         1287.0            8
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_cap, self.farmacia.ver_estante,
                                    ['cápsula'], Nt2_4, le)
            cad_jar = """Presentación: jarabe
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          2500         2950.0            5
med_3                          1900         2242.0           10
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_jar, self.farmacia.ver_estante,
                                    ['jarabe'], Nt2_4, le)


            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_3_quitar(self):
        iTest = 3
        sTitle = "Quita medicamento de posiciones en estantes de la Farmacia"
        fMax_nota = 0.8
        Nt3_1 = fMax_nota * 0.20 / 2
        Nt3_2 = fMax_nota * 0.15 / 2
        Nt3_4 = fMax_nota * 0.15 / 6
        if self.dict_pruebas.get("quitar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Qiotar cuando no hay nada en los estantes de la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.farmacia.quitar,
                                    ["comprimido", 0], Nt3_1, le)

            # Adición de medicamentos a la Farmacia
            lst_medicamento = gen_lst_medicamentos(1)
            cr_i = 0
            for med in lst_medicamento:
                self.farmacia.registro(med)
                cr_i += 1

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, self.farmacia.cantidad_farmacia,
                                    [], Nt3_2, le)

            # Comprobación de los estantes de la farmacia
            cad_com = """Presentación: comprimido
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                         800.0          928.0           10
med_2                         500.0          580.0            5
med_3                         750.0          870.0            7
med_4                         200.0          232.0            5
med_5                         600.0          696.0            8
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_com, self.farmacia.ver_estante,
                                    ['comprimido'], Nt3_4, le)
            cad_cap = """Presentación: cápsula
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          1200         1404.0           10
med_2                           900         1053.0            8
med_3                          1100         1287.0            8
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_cap, self.farmacia.ver_estante,
                                    ['cápsula'], Nt3_4, le)
            cad_jar = """Presentación: jarabe
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          2500         2950.0            5
med_2                          2000         2360.0           10
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_jar, self.farmacia.ver_estante,
                                    ['jarabe'], Nt3_4, le)

            # Quitar cuando la presentación del medicamento no es correcta
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.farmacia.quitar,
                                    ["marrano", 0], Nt3_1, le)

            # Quitar con posiciones correctas e incorrectas
            cr_i = 0
            posiciones = [[True, "comprimido", 4], [False, "cápsula", 3],
                          [True, "jarabe", 1], [True, "comprimido", 1],
                          [False, "cápsula", -1], [True, "comprimido", 2],
                          [True, "jarabe", 0], [False, "comprimido", 2],
                          [False, "jarabe", 0], [True, "cápsula", 1]]
            Nt3_3 = fMax_nota * 0.5 / len(posiciones)
            le = (traceback.extract_stack()[-1])[1] + 3
            for pos_x in posiciones:
                self.comprobarAserción2(pos_x[0],
                                        self.farmacia.quitar,
                                        [pos_x[1], pos_x[2]], Nt3_3, le, cr_i)
                cr_i += 1

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(4, self.farmacia.cantidad_farmacia,
                                    [], Nt3_2, le)

            # Comprobación de los estantes de la farmacia
            cad_com = """Presentación: comprimido
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                         800.0          928.0           10
med_3                         750.0          870.0            7
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_com, self.farmacia.ver_estante,
                                    ['comprimido'], Nt3_4, le)
            cad_cap = """Presentación: cápsula
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          1200         1404.0           10
med_3                          1100         1287.0            8
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_cap, self.farmacia.ver_estante,
                                    ['cápsula'], Nt3_4, le)
            cad_jar = "Presentación: jarabe NE/SE"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_jar, self.farmacia.ver_estante,
                                    ['jarabe'], Nt3_4, le)


            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_4_venta(self):
        iTest = 4
        sTitle = "Venta de medicamentos en la farmacia"
        fMax_nota = 1.2
        Nt4_1 = fMax_nota * 0.6 / 7
        Nt4_2 = fMax_nota * 0.2 / 3
        Nt4_3 = fMax_nota * 0.2 / 6
        if self.dict_pruebas.get("venta"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Adición de medicamento a la Farmacia
            lst_medicamento = gen_lst_medicamentos(1)
            cr_i = 0
            for med in lst_medicamento:
                self.farmacia.registro(med)
                cr_i += 1

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, self.farmacia.cantidad_farmacia,
                                    [], Nt4_2, le)

            # Vender medicamento de los estantes de la farmacia
            m1 = Medicamento("med_1", "comprimido")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2((4639.999999999999, False),
                                    self.farmacia.venta, [m1, 5], Nt4_1, le)
            # quedan 5 existencias med_1

            m3 = Medicamento("med_3", "cápsula")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2((9009.0, False), self.farmacia.venta,
                                    [m3, 7], Nt4_1, le)
            # queda 1 existencia med_3

            m2 = Medicamento("med_2", "jarabe")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2((0, False), self.farmacia.venta, [m2, 11],
                                    Nt4_1, le)
            # quedan 10 existencias med_2, ninguno es vendido, porque la venta
            # excede la cantidad de existencias actuales

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2((23600.0, True), self.farmacia.venta,
                                    [m2, 10], Nt4_1, le)
            # quedan 0 existencias med_2 y por lo tanto se elimina [X]

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(9, self.farmacia.cantidad_farmacia,
                                    [], Nt4_2, le)

            # Comprobación de los estantes de la farmacia
            cad_com = """Presentación: comprimido
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                         800.0          928.0            5
med_2                         500.0          580.0            5
med_3                         750.0          870.0            7
med_4                         200.0          232.0            5
med_5                         600.0          696.0            8
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_com, self.farmacia.ver_estante,
                                    ['comprimido'], Nt4_3, le)
            cad_cap = """Presentación: cápsula
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          1200         1404.0           10
med_2                           900         1053.0            8
med_3                          1100         1287.0            1
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_cap, self.farmacia.ver_estante,
                                    ['cápsula'], Nt4_3, le)
            cad_jar = """Presentación: jarabe
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          2500         2950.0            5
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_jar, self.farmacia.ver_estante,
                                    ['jarabe'], Nt4_3, le)

            m9x = Medicamento("med_3", "cápsula")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2((0, False), self.farmacia.venta, [m9x, -1],
                                    Nt4_1, le)
            # cantidad negativa

            m7x = Medicamento("med_5", "jarabe")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2((0.0, False), self.farmacia.venta,
                                    [m7x, 1], Nt4_1, le)
            # medicamento no existe

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2((4639.999999999999, True),
                                    self.farmacia.venta, [m1, 5], Nt4_1, le)
            # quedan 0 existencias med1 y por lo tanto se elimina [X]

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(8, self.farmacia.cantidad_farmacia,
                                    [], Nt4_2, le)

            # Comprobación de los estantes de la farmacia
            cad_com = """Presentación: comprimido
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_2                         500.0          580.0            5
med_3                         750.0          870.0            7
med_4                         200.0          232.0            5
med_5                         600.0          696.0            8
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_com, self.farmacia.ver_estante,
                                    ['comprimido'], Nt4_3, le)
            cad_cap = """Presentación: cápsula
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          1200         1404.0           10
med_2                           900         1053.0            8
med_3                          1100         1287.0            1
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_cap, self.farmacia.ver_estante,
                                    ['cápsula'], Nt4_3, le)
            cad_jar = """Presentación: jarabe
Nombre medicamento              PSI            PVP  Existencias
--------------------   ------------   ------------  -----------
med_1                          2500         2950.0            5
"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(cad_jar, self.farmacia.ver_estante,
                                    ['jarabe'], Nt4_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_5_consultar(self):
        iTest = 5
        sTitle = "Comprobación de la consulta de un medicamento en la Farmacia"
        fMax_nota = 0.8
        Nt5_1 = fMax_nota * 0.8 / 10
        Nt5_2 = fMax_nota * 0.2 / 2
        if self.dict_pruebas.get("consultar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Adición de medicamento a la Farmacia
            lst_medicamento = gen_lst_medicamentos(1)
            cr_i = 0
            for med in lst_medicamento:
                self.farmacia.registro(med)
                cr_i += 1

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, self.farmacia.cantidad_farmacia,
                                    [], Nt5_2, le)

            # Busca medicamento en uno de los 3 estantes de la farmacia
            m2 = Medicamento("med_2", "comprimido")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("med_2/comprimido - $580.0 | 5",
                                    self.farmacia.consultar, [m2], Nt5_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("cápsula:med_2:$1053.0",
                                    self.farmacia.localizar, ["cápsula", 1], Nt5_1, le)

            m3 = Medicamento("med_1", "jarabe")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("med_1/jarabe - $2950.0 | 5",
                                    self.farmacia.consultar, [m3], Nt5_1, le)

            # Cuando el medicamento NO existe
            m7x = Medicamento("med_6", "comprimido")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("X/X - $X | X", self.farmacia.consultar, [m7x],
                                    Nt5_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("X:X:$X", self.farmacia.localizar, [2, "jarabe"],
                                    Nt5_1, le)

            m8x = Medicamento("med_3", "jarabe")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("X/X - $X | X", self.farmacia.consultar, [m8x],
                                    Nt5_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("X:X:$X", self.farmacia.localizar, ["cápsula", -1],
                                    Nt5_1, le)

            # Despues de un registro de medicamento
            med5c = Medicamento("med_2", "cápsula", 1000, 18)
            self.farmacia.registro(med5c)

            m5 = Medicamento("med_2", "cápsula")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("med_2/cápsula - $1053.0 | 26",
                                    self.farmacia.consultar, [m5], Nt5_1, le)

            # Después de una salida de medicamento
            self.farmacia.venta(m5, 20)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("med_2/cápsula - $1053.0 | 6",
                                    self.farmacia.consultar, [m5], Nt5_1, le)

            m3c = Medicamento("med_3", "cápsula")
            self.farmacia.venta(m3c, 8)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("X:X:$X", self.farmacia.localizar, ["cápsula", 2],
                                    Nt5_1, le)

            # Comprobación del número de medicamentos en la farmacia
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(9, self.farmacia.cantidad_farmacia,
                                    [], Nt5_2, le)
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_nota(self):
        """
        INFORME DE LA NOTA FINAL
        """
        self.nota_final()


if __name__ == "__main__":
    unittest.main(verbosity=0)
