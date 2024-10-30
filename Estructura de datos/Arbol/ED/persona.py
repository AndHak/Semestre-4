class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    def __gt__(self, otra_persona):
        #en el caso de que self y otra_pewrsona
        #sean de diferente tipo, lanzar: raise HomogeneityError
        return self.nombre > otra_persona.nombre or (self.nombre == otra_persona.nombre and self.edad > otra_persona.edad)
    
    def __lt__(self, otra_persona):
        return self.nombre < otra_persona.nombre
    
    def __str__(self):
        return f"Nombre: {self.nombre}; Edad: {self.edad} Años"
        
    