from lse import Lista_SE
class Estudiante:
    """La clase Estudiante implementa un estudiante que posee código, nombre
    y una nota global
    """
    def __init__(self, codigo, nombre="", nota=0.0):
        """Constructor del Estudiante. El código del estudiante deben ser
        todos números y con un tamaño de 4 dígitos. La nota debe estar
        entre 0.0 y 5.0.

        Parameters
        ----------
        codigo : str
            código del estudiante
        nombre : str, optional
            nombre del estudiante, por defecto ""
        nota : int, optional
            nota del estudiante, por defecto 0.0
        """
        self.codigo = codigo
        self.nombre = nombre
        self.nota = nota
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo_valido):
        if codigo_valido.isdigit() and len(codigo_valido) == 4:
            self.__codigo = codigo_valido
        else:
            raise ValueError("No se pudo crear el estudiante por su codigo incorrecto")
        
    @property
    def nota(self):
        return self.__nota 

    @nota.setter
    def nota(self, nota_valida):
        try:
            nota_valida = float(nota_valida)  # Convertimos a float primero
            if 0.0 <= nota_valida <= 5.0:
                self.__nota = nota_valida
            else:
                raise ValueError("La nota debe estar entre 0.0 y 5.0")
        except ValueError:
            raise ValueError("No se pudo crear el estudiante por su nota incorrecta")

    def __str__(self):
        """Método de presentación del Estudiante.

        Returns
        -------
        str
            cadena que representa al estudiante con el formato:
                        "código|nombre|nota"
        """
        return f"{self.codigo}|{self.nombre}|{self.nota}"

    def __eq__(self, otro_estudiante):
        """Método que compara si dos Estudiantes son iguales, teniendo en
        cuenta únicamente el código del estudiante.
        ------------------------------ TAREA ----------------------------
        Validar que el tipo de dato de otro_estudiante corresponda a
        Estudiante. Si no es un Estudiante, devolver False
        -----------------------------------------------------------------

        Parameters
        ----------
        otro_estudiante : Estudiante
            el otro estudiante con el cual se van ha realizar las
            comparaciones de igualdad

        Returns
        -------
        bool
            True si los dos estudiantes son el mismo. False en caso
            contrario
        """
        return type(self) is type(otro_estudiante) and self.codigo is otro_estudiante.codigo
    


class Colegio:
    """La clase Colegio implementa el funcionamiento de un establecimiento
    educativo, el cual tiene un nombre y una lista de estudiantes matriculados
    """
    def __init__(self, nombre):
        """Constructor del Colegio. Aún no se han matriculado ningún
        estudiante al colegio

        Parameters
        ----------
        nombre : str
            nombre del colegio
        """
        self.nombre = nombre
        self.estudiantes_matriculados = Lista_SE()


    def matricular(self, nuevo_est, becado=False, pos_beca=0):
        """Método que realiza la matrícula de nuevos estudiantes al colegio.
        Validar que el estudiante no se encuentre ya matriculado en el colegio.
        En caso afirmativo, el nuevo estudiante no será matriculado

        Parameters
        ----------
        nuevo_est : Estudiante
            el nuevo estudiante a ser matriculado
        becado : bool, optional
            indica si un estudiante va a ser becado o no. En caso de ser
            becado, ubicarlo en una determinada posición de la lista., por
            defecto False
        pos_beca : int, optional
            posición a ocupar en la lista de estudiante, en el caso de que el
            estudiante fuese becado, por defecto 0

        Returns
        -------
        bool
            True si el estudiante es matriculado. False en caso contrario
        """
        encontrado = self.estudiantes_matriculados.encontrar(nuevo_est)
        
        if encontrado is None:  # Si no está matriculado
            if becado:
                if pos_beca >= 0:
                    # Matricular en la posición indicada si es becado
                    return self.estudiantes_matriculados.posicionar(nuevo_est, pos_beca)
            else:
                # Matricular al final de la lista
                return self.estudiantes_matriculados.adicionar(nuevo_est)
        else:
            # El estudiante ya está matriculado
            return False

    def expulsar(self, pos_est, por_estudiante=False):
        """Método que expulsa a un estudiante ya sea por estudiante o posición
        en la lista de estudiantes matriculados

        Parameters
        ----------
        pos_est : int|Estudiante
            representa la posición o el objeto de tipo estudiante a ser
            expulsado del colegio, siempre y cuando exista
        por_estudiante : bool, optional
            bandera que representa si se expulsa por estudiante (True) o por
            posición (False), por defecto False

        Returns
        -------
        bool
            True si el estudiante pudo ser expulsado. False en caso contrario
        """
        # if por_estudiante:
        #     # Expulsar por objeto Estudiante
        #     if pos_est in self.estudiantes_matriculados:
        #         return self.estudiantes_matriculados.remover(pos_est, por_estudiante)
        #     else:
        #         return False
        # else:
        #     # Expulsar por índice
        #     if 0 <= pos_est < len(self.estudiantes_matriculados):
        #         return self.estudiantes_matriculados.remover(pos_est, por_estudiante)
        #     else:
        #         return False
        if por_estudiante:
            for estudiante in self.estudiantes_matriculados:
                if estudiante.codigo == pos_est.codigo:
                    return self.estudiantes_matriculados.remover(estudiante, por_pos=False)
            return False  # Esto solo se ejecuta si no encontró al estudiante.
        
        else:
            encontrado = self.estudiantes_matriculados.ubicar(pos_est)
            if encontrado:
                return self.estudiantes_matriculados.remover(pos_est, por_pos=True)
            return False



        


    def ver_estudiantes(self):
        """Método que permite visualizar los estudiante matriculados en el
        colegio
        """
        return self.estudiantes_matriculados.recorrer()

    def computar_nueva_nota(self, estud, nueva_nota):
        """Método que computa una nueva nota para un estudiante matriculado.
        Actualizar la nota, recalculando la nota del estudiante, promediando
        la nota que ya tiene con la nueva nota

        Parameters
        ----------
        estud : Estudiante
            el estudiante al cual se le va a calcular la nota
        nueva_nota : float
            nueva nota a ser registrada a un estudiante matriculado

        Returns
        -------
        bool
            True si se pudo asignar la nueva nota. False en caso contrario
        """
        for estudiante in self.estudiantes_matriculados:
            if estudiante.codigo == estud.codigo:
                # Promediamos la nueva nota con la nota existente
                estudiante.nota = (estudiante.nota + nueva_nota) / 2
                return True
        return False  # Si no se encontró el estudiante, retornamos False
                


    def ubicar_estudiante(self, pos_loc):
        """Método que permite ubicar un estudiante matriculado dada una
        posición.

        Parameters
        ----------
        pos_loc : int
            valor de la posición en la lista de estudiantes matriculados

        Returns
        -------
        Estudiante|None
            el estudiante si está matriculado. None en caso contrario
        """
        return self.estudiantes_matriculados.ubicar(pos_loc) 

    def informe(self):
        """Método que genera una cadena a modo de Informe de todos los estudiantes
        matriculados en el colegio.

        Returns
        -------
        str
            cadena con el formato:
                "Informe del Colegio ABC / (estudiante_0) :>: (estudiante_1) :>: (estudiante_2) :>: (estudiante_n)"
        """
        estudiantes_info = [f"({estudiante})" for estudiante in self.estudiantes_matriculados]
    
        # Unir todas las representaciones con " :>: "
        cadena_final = " :>: ".join(estudiantes_info)

        return f"Informe del Colegio {self.nombre} / {cadena_final}"
        

    def promedio(self):
        """Método que calcula y retorna el promedio de todas las notas de los estudiantes
        actualmente matriculados

        Returns
        -------
        float
            promedio de todas las notas de los estudiantes matriculados en el colegio
        """
        suma = 0
        bandera = 0
        for estudiantes in self.estudiantes_matriculados:
            suma += estudiantes.nota
            bandera += 1
        
        promedio = suma / bandera
        return promedio



if __name__ == "__main__":

    school = Colegio("ABC")
    if school.matricular(Estudiante(codigo="1001", nombre="Pepito", nota=3.0)):
        print("Pepito fue matriculado!")
    
    cod = "1002"
    nomb = "María"
    if school.matricular(Estudiante(cod, nomb, 4.5)):
        print(f"{nomb} fue matriculad@!")

    cod = "1003"
    nomb = "Juanito Alimaña"
    try:
        school.matricular(Estudiante(cod, nomb, -1.0))
    except ValueError as e:
        print(f"Para el estudiante de código {cod} y nombre {nomb}: {e}")

    cod = "1004"
    nomb = "Pedro"
    if school.matricular(Estudiante(cod, nomb)):
        print(f"{nomb} fue matriculad@!")

    cod = "105"
    nomb = "Vanesa"
    try:
        school.matricular(Estudiante(cod, nomb))
    except ValueError as e:
        print(f"Para {nomb} con código {cod}: {e}")

    cod = "16X"
    nomb = "Carlos"
    try:
        school.matricular(Estudiante(cod, nomb, 2.5))
    except ValueError as e:
        print(f"Para {nomb} con código {cod}: {e}")


    cod = "1007"
    nomb = "Alejandra"
    if school.matricular(Estudiante(cod, nomb, 4.5)):
        print(f"{nomb} fue matriculad@!")

    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    info = school.informe()
    print(info)
    assert info == "Informe del Colegio ABC / (1001|Pepito|3.0) :>: "\
        "(1002|María|4.5) :>: (1004|Pedro|0.0) :>: (1007|Alejandra|4.5)",\
        "ERROR: Informe Incorrecto"
    
    # Prueba de matriculación de un estudiante becado con una posición correcta
    print("\n--- Prueba de matrícula de un estudiante becado con posición válida ---")
    becado = Estudiante(codigo="2001", nombre="Laura", nota=5.0)
    if school.matricular(becado, becado=True, pos_beca=3):
        print(f"El estudiante becado {becado.nombre} fue matriculad@ correctamente en una posición válida!")
    else:
        print(f"El estudiante becado {becado.nombre} no pudo ser matriculado!")

    # Prueba de matriculación de un estudiante becado con una posición incorrecta (negativa)
    print("\n--- Prueba de matrícula de un estudiante becado con posición negativa ---")
    try:
        becado_incorrecto = Estudiante(codigo="2002", nombre="José", nota=4.8)
        # Aquí simulamos la matrícula con una posición negativa
        school.matricular(becado_incorrecto, becado=True, pos_beca=-1)
        print(f"El estudiante becado {becado_incorrecto.nombre} No fue matriculad@")
    except ValueError as e:
        print(f"No se pudo matricular a {becado_incorrecto.nombre} debido a un error: {e}")


    cod = input("Código del estudiante a expulsar:")
    if school.expulsar(pos_est=Estudiante(cod), por_estudiante=True):
        print(f"El estudiante de código {cod} fue EXPULSADO del colegio")
    else:
        print(f"El estudiante de código {cod} no pudo ser EXPULSADO del colegio")

    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    pos = int(input("Posición del estudiante a expulsar:"))
    if school.expulsar(pos_est=pos):
        print(f"El estudiante de posición {pos} fue EXPULSADO del colegio")
    else:
        print(f"El estudiante de posición {pos} no pudo ser EXPULSADO del colegio")

    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    if school.computar_nueva_nota(Estudiante("1001"), nueva_nota=5.0):
        print("Actualización de notas EXITOSA!")
    else:
        print("NO pudo asignarse la nota!")
    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    if school.computar_nueva_nota(Estudiante("1007"), nueva_nota=1.5):
        print("Actualización de notas EXITOSA!")
    else:
        print("NO pudo asignarse la nota!")
    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    pos = int(input("Posición del estudiante a ubicar:"))
    estud = school.ubicar_estudiante(pos)
    if estud:
        print("Estudiante localizado:")
        print(estud)
    else:
        print(f"El estudiante en la posición {pos} no fue econtrado!")

    for i in range(4):
        cod = input("Código del estudiante a calificar:")
        nota = float(input("Nueva nota:"))
        if school.computar_nueva_nota(Estudiante(cod), nueva_nota=nota):
            print("Actualización de notas EXITOSA!")
        else:
            print(f"El estudiante de código {cod} no pudo ser calificado!")

    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    print(school.informe())

    print(f"El promedio del Colegio es {school.promedio()}")
    




    # Pruebas
    try:
        estudiante = Estudiante("1234", "Pepe", 4.5)
        print(f"Código: {estudiante.codigo}, Nota: {estudiante.nota}")  # Código: 1234, Nota: 4.5

        estudiante.codigo = "5678"
        estudiante.nota = 3.0  # Actualiza correctamente
        print(f"Código: {estudiante.codigo}, Nota: {estudiante.nota}")  # Código: 5678, Nota: 3.0

        estudiante.nota = 6.0  # Esto lanzará una excepción
    except ValueError as e:
        print(e)
        



