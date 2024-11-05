
class DuplicatedKeyError(Exception):
    def __init__(self, nueva_clave):
        super().__init__(f"La clave : {nueva_clave} se encuentra duplicada!")

class HomogeneityError(Exception):
    def __init__(self, nueva_clave):
        super().__init__(f"La clave : {nueva_clave} no es homogenea!")
