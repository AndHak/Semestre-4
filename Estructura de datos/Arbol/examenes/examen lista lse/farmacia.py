"""MODULE: farmacia.py
   DATE: 25-09-2024
   AUTHORS:
   SEBASTIAN DAVID ORDOÑEZ BOLAÑOS
   ANDRES FELIPE MARTINEZ GUERRA
"""

from bed.lineales.lse import Lista_SE

class Medicamento:
    """Un Medicamento se caracteriza porque debe tener en cuenta:
    + el nombre
    + la presentación (ATENCIÓN: puede ser únicamente: 'comprimido', 'cápsula'
      o 'jarabe')
    + precio sin IVA (ATENCIÓN: debe ser superior siempre a $0).
    + existencias, que por defecto será 10 cuando el valor ingresado es
      cero o negativo, solamente en el constructor del medicamento.
    """
    # Escriba y documente el constructor de la clase AQUI, con el mismo orden
    # para los parámetros requeridos por el constructor de las caracteristicas
    # de la clase, donde los paráMetros para el precio sin iva y de existencias
    # tienen un valor por defecto de 1 respectivamente cuando no son pasados.
    def __init__(self, nombre, presentacion, precio_sin_iva=None, existencias=10):
        self.nombre = nombre
        self.presentacion = presentacion
        self.precio_sin_iva = precio_sin_iva if precio_sin_iva is not None else 0.1
        self.existencias = existencias if existencias > 0 else 10

    # @property
    # def precio_sin_iva(self):
    #     return self.__precio_sin_iva

    # @precio_sin_iva.setter
    # def precio_sin_iva(self, precio_valido):
    #     if precio_valido is None:
    #         self.__precio_sin_iva = 0.1 
    #     elif precio_valido > 0:
    #         self.__precio_sin_iva = precio_valido
    #     else:
    #         raise ValueError("El precio sin IVA debe ser mayor a $0.")    
    
    @property
    def presentacion(self):
        return self.__presentacion

    @presentacion.setter
    def presentacion(self, presentacion_valida):
        if presentacion_valida not in ['comprimido', 'cápsula', 'jarabe']:
            raise ValueError("La presentación debe ser 'comprimido', 'cápsula' o 'jarabe'.")
        else:
            self.__presentacion = presentacion_valida
        
    # @property
    # def existencias(self):
    #     return self.__existencias
    
    # @existencias.setter
    # def existencias(self, existencias_validas):
    #     if existencias_validas > 0 or existencias_validas is None:
    #         self.__existencias = existencias_validas
    #     else:
    #         self.__existencias = 10


        

    # Método M # 1
    def pvp(self):
        """Método que calcula el precio del medicamento con IVA, para la venta
        al público. Tener en cuenta que se aplicará un IVA diferenciado del:
        - 16% más sobre el precio sin IVA si es 'comprimido'
        - 17% más sobre el precio sin IVA si es 'cápsula'
        - 18% más sobre el precio sin IVA si es 'jarabe'

        Por ejemplo, si el medicamento es de tipo 'jarabe' y el precio sin IVA
        es de $100, entonces el valor de venta al público será de $118.0

        Returns
        -------
        float
            El precio de venta al público del medicamento calculado el IVA
        """
        iva_por_presentacion = {
            'comprimido': 0.16,
            'cápsula': 0.17,
            'jarabe': 0.18
        }
        
        return self.precio_sin_iva * (1 + iva_por_presentacion[self.presentacion])


    # Método M # 2
    def __eq__(self, otro):
        """Método de comparción de medicamentos, teniendo en cuenta el nombre y
        la presentacion

        Parameters
        ----------
        otro : Medicamento
            El otro medicamento con el cual se van a ser las comparaciones

        Returns
        -------
        bool
            True si el medicamento comparado es igual. False en caso contrario
        """
        return (self.nombre == otro.nombre and self.presentacion == otro.presentacion)

    # Método M # 3
    def __str__(self):
        """Método de presentacion de un medicamento

        Returns
        -------
        str
            Una cadena con el formato:
            "nombre/presentacion - $PVP | existencias"
            Por ejemplo:
            "Aspirina/cápsula - $234.0 | 5"
        """
        return f"{self.nombre}/{self.presentacion} - ${self.pvp():.1f} | {self.existencias}"



class Farmacia:
    """Una farmacia que gestiona varios medicamentos, teniendo en cuenta que
    debe:
    + tener un nombre que la identifique
    + manejar de forma separada, según la presentacion del medicamento, en
    diferentes estantes de la farmacia
    """
    # Escriba y documente el constructor de la clase AQUI, con el mismo orden
    # para los parámetros requeridos por el constructor de las caracteristicas
    # de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.estantes = {
            'comprimido': Lista_SE(),
            'cápsula': Lista_SE(),
            'jarabe': Lista_SE()
        }

    # Método FM # 1
    def registro(self, un_medicamento):
        """Método que adiciona un medicamento a la farmacia, en un determinado
        estante, de acuerdo a su presentación.
        - Si el nombre y presentación del medicamento ya existe en la farmacia,
        se deberá modificar las existencias de medicamento, adicionando el
        número de existencias del nuevo medicamento, y además, el precio sin
        iva del medicamento se modificará al del medicamento de menor valor

        Por ejemplo, si el medicamento a dar de alta es Ibuprofeno, en
        presentacion de comprimido, con un precio sin IVA de $400 y un número
        de existencias de 15, y éste ya se encuentra en la farmacia con 30
        existencias y un precio sin IVA de $500, entonces se deberá modificar
        el medicamento existente ahora con un número de existencias de 45 y un
        precio sin IVA de $400

        Parameters
        ----------
        un_medicamento : Medicamento
            El medicamento a ser adicionado a un estante de la farmacia

        Returns
        -------
        tuple
            El precio con IVA (PVP) y las existencias del medicamento
            actualizados, como una tupla, si el medicamento fue
            agregado/modificado de forma satisfactoria:
                (PVP, existencias)
            En caso contrario retornar una tupla con valores de (-1) para el
            PVP y las existencias:
                (-1, -1)
        """
        if isinstance(un_medicamento, Medicamento):
            estante = self.estantes[un_medicamento.presentacion]
            for medicamento in estante:
                if medicamento == un_medicamento:
                    medicamento.existencias += un_medicamento.existencias
                    medicamento.precio_sin_iva = min(medicamento.precio_sin_iva, un_medicamento.precio_sin_iva)
                    return (medicamento.pvp(), medicamento.existencias)

            estante.adicionar(un_medicamento)
            return (un_medicamento.pvp(), un_medicamento.existencias)
        return False

    # Método FM # 2
    def colocar(self, un_medicamento, pos):
        """Método que ingresa un medicamento a un determinado estante de la
        farmacia, en una posición determinada del estante. Se deberá validar
        que el medicamento que ingresa sea único en el estante

        Parameters
        ----------
        un_medicamento : Medicamento
            El medicamento a ser colocado en una posición de un estante de la
            farmacia
        pos : int
            Un valor con la posición en el estante correspondiente a ser
            colocado el medicamento

        Returns
        -------
        bool
            True si se pudo colocar el medicamento en uno de los estantes
        de la farmacia. False en caso contrario
        """
        estante = self.estantes[un_medicamento.presentacion]
        if pos < 0 or pos > len(estante) or un_medicamento in estante:
            return False

        estante.posicionar(un_medicamento, pos)
        return True

    # Método FM # 3
    def quitar(self, presentacion, pos):
        """Método que quita un medicamento de la farmacia en una posición
        determinada, de uno de los estantes de la farmacia

        Parameters
        ----------
        presentacion : str
            Corresponde a la presentacion del medicamento: "comprimido",
            "cápsula" o "jarabe".
        pos : int
            Un valor con la posición en el estante correspondiente a ser
            quitado el medicamento

        Returns
        -------
        bool
            True si se pudo quitar/eliminar el medicamento de la farmacia.
            False en caso contrario
        """
        estante = self.estantes.get(presentacion)
        if estante and 0 <= pos < len(estante):
            estante.remover(pos)
            return True
        return False

    # Método FM # 4
    def venta(self, un_medicamento, cantidad):
        """Método que realiza la venta de un medicamento de la farmacia,
        según la cantidad solicitada para la venta.
        Validar que exista al menos la cantidad de existencias suficientes del
        medicamento solicitado, siendo la cantidad un valor mayor que cero. Si
        la venta es exitosa, se debe calcular el precio de venta al público
        total, de acuerdo al PVP del medicamento. Si la cantidad a vender agota
        exactamente todas las existencias del medicamento, éste se deberá dar
        de baja/eliminar del estante de la farmacia.

        Parameters
        ----------
        un_medicamento : Medicamento
            El medicamento a ser vendido de uno de los estantes de la farmacia
        cantidad : int
            El número de unidades del medicamento a ser vendida

        Returns
        -------
        tuple
            Una tupla con el precio de venta total y un valor booleano True,
            si el medicamento fue quitado del estante o False si no fue
            quitado:
                (venta_total, True/False)
            En el caso de que no se pueda vender la cantidad de medicamento
            solicitada devolverá un precio de venta total igual a 0 y False al
            no poder ser quitado el medicamento, ya que no se produjo una
            venta
                (0, False)
        """
        if cantidad <= 0:
            return (0, False)

        estante = self.estantes.get(un_medicamento.presentacion)
        if not estante:
            return (0, False)  

        for medicamento in estante:
            if medicamento == un_medicamento:  
                if medicamento.existencias >= cantidad:
                    total_venta = medicamento.pvp() * cantidad
                    medicamento.existencias -= cantidad  
                    se_agoto = medicamento.existencias == 0
                    if se_agoto:
                        estante.remover(medicamento, por_pos=False) 
                    return (total_venta, se_agoto)  
                return (0, False)  
        return (0, False)

    # Método FM # 5
    def consultar(self, un_medicamento):
        """Método que permite averiguar si un determinado medicamento se
        encuentra presente en algún estante de la farmacia

        Parameters
        ----------
        un_medicamento : Medicamento
            El medicamento a ser buscado en los estantes de la farmacia

        Returns
        -------
        str
            Una cadena con la descripción del medicamento en el formato:
            "nombre_medicamento/presentacion - $PVP | existencias"
            En el caso de que el medicamento no exista en la farmacia, se
            retornará la siguiente cadena:
            "X/X - $X | X"
        """
        for estante in self.estantes.values():
            for medicamento in estante:
                if medicamento == un_medicamento:
                    return str(medicamento) 
        return "X/X - $X | X"

    # Método FM # 6
    def localizar(self, presentacion, pos):
        """Método que busca un medicamento en uno de los diferentes estantes
        de la farmacia, según la presentación y una determinada posición

        Parameters
        ----------
        presentacion : str
            La presentación del medicamento utilizada para seleccionar un
            determinado estante de la farmacia
        pos : int
            Posición del medicamente en el estante correspondiente

        Returns
        -------
        str
            Si el medicamento existe, una cadena con la información del
            medicamento encontrado según el siguiente formato:
                "presentacion:nombre:$PVP"
            Si no existe, una cadena con el siguiente formato:
                "X:X:$X"
        """
        estante = self.estantes.get(presentacion)
        if estante and 0 <= pos < len(estante):
            medicamento = estante.ubicar(pos)
            return f"{medicamento.presentacion}:{medicamento.nombre}:${medicamento.pvp():.1f}"
        return "X:X:$X"

    # Método FM # 7
    def ver_estante(self, presentacion):
        """Método que permite generar una cadena, en formato de tabla, de los
        medicamentos de un estante, según la presentación, organizados por
        nombre, psi, pvp y existencias

        Parameters
        ----------
        presentacion : str
            Corresponde a la presentacion de medicamento "comprimido",
            "cápsula" o "jarabe"

        Returns
        -------
        str
            Una cadena con el siguiente formato:
           "Presentación: tipo_presentación
            Nombre medicamento              PSI            PVP  Existencias
            --------------------   ------------   ------------  -----------
            nombre_med_1                psi_1.0        pvp_1.0            #
            nombre_med_2                psi_2.0        pvp_2.0            #
            nombre_med_3                psi_3.0        pvp_3.0            #
           "

            por ejemplo:
           "Presentación: comprimido
            Nombre medicamento              PSI            PVP  Existencias
            --------------------   ------------   ------------  -----------
            Ibuprofeno                    570.0          661.2            2
            Aspirina                      820.0          951.2            5
            Buscapina                    1380.0         1600.8           10
           "

            Notar que el psi y el pvp se debe mostrar con 1 cifra decimal.
            En el caso de que la presentacion no exista, retornar una cadena
            que diga:
            "Presentación: tipo_presentación NE/SE"

            por ejemplo:
            "Presentación: jarabe NE/SE"
            que indicaría que la presentación solicitada no existe o está sin
            existencias
        """
        estante = self.estantes.get(presentacion)
        if not estante or estante.es_vacia():
            return f"Presentación: {presentacion} NE/SE"
        
        cadena = f"Presentación: {presentacion}\n"
        cadena += f"Nombre medicamento              PSI            PVP  Existencias\n"
        cadena += f"--------------------   ------------   ------------  -----------\n"

        # nodo_actual = estante.ubicar(0)
        # while nodo_actual:
        #     cadena += f"{nodo_actual.nombre:<30} {nodo_actual.presentacion:<15} {nodo_actual.pvp():<10.1f} {nodo_actual.existencias:<10}\n"
        #     nodo_actual = nodo_actual.sig
        
        # return cadena
        for med in estante:
            cadena += f"{med.nombre}                          {med.precio_sin_iva if len(str(med.precio_sin_iva)) == 4 else f" {med.precio_sin_iva}"}         {med.pvp():.1f}           {med.existencias if len(str(med.existencias)) == 2 else f" {med.existencias}"}\n"

        return cadena


    # Método FM # 8
    def cantidad_farmacia(self):
        """Método que calcula la cantidad de medicamentos existentes en toda
        la farmacia, no de existencias.

        Returns
        -------
        int
            Retorna el número total de medicamentos actualmente registrados en
            la farmacia
        """
        total = 0
        for estante in self.estantes.values():
            total += len(estante) 
        return total