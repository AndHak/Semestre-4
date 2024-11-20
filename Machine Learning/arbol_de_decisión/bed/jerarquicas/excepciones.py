
class DuplicatedKeyError(Exception):
    def __init__(self, nueva_clave):
        super().__init__(f"La clave : {nueva_clave} se encuentra duplicada!")

class HomogeneityError(Exception):
    def __init__(self, nueva_clave):
        super().__init__(f"La clave : {nueva_clave} no es homogenea!")

class NodoNoEncontradoError(Exception):
    """Se lanza cuando un nodo no se encuentra en el árbol de decisión."""
    def __init__(self, mensaje="El nodo especificado no se encontró en el árbol."):
        super().__init__(mensaje)

class ArbolVacioError(Exception):
    """Se lanza cuando se intenta acceder o modificar un árbol vacío."""
    def __init__(self, mensaje="El árbol está vacío. No se puede realizar esta operación."):
        super().__init__(mensaje)

class NodoYaExisteError(Exception):
    """Se lanza cuando se intenta agregar un nodo que ya existe en el árbol."""
    def __init__(self, mensaje="El nodo ya existe en el árbol."):
        super().__init__(mensaje)

class ClasificacionInvalidaError(Exception):
    """Se lanza cuando se intenta clasificar un nodo con un valor inválido."""
    def __init__(self, mensaje="La clasificación proporcionada es inválida para este nodo."):
        super().__init__(mensaje)

class ValorInvalidoError(Exception):
    """Se lanza cuando el valor proporcionado para un nodo es inválido."""
    def __init__(self, mensaje="El valor especificado para el nodo no es válido."):
        super().__init__(mensaje)
