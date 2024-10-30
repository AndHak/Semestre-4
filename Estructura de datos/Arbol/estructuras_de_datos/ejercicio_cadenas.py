# class Cadena:
#     # tamano = 100
#     mayusculas = 'TABCDEFGHIJKLMNÑOPQRSRUVWXYZ '
#     minusculas = 'tabcdefghijklmnñopqrsruvwxyz '
#     def _init_(self,cadena):
#         if len(cadena) > 16:
#             raise ValueError(f"La cadena no puede exceder {16} caracteres.")
#         self.cadena = cadena
#     def asignar(self,nueva_cadena):
#         self.cadena = nueva_cadena
#     def concat(self,otra_cadena):
#         self.cadena = self.cadena+otra_cadena
#     def a_may(self):
#         nueva = ''
#         #if self.cadena.isupper():
#         for w in self.cadena:
#             j=0
#             for j in range(len(self.mayusculas)):
#                 if self.mayusculas[j] == w or self.minusculas[j] == w:
#                     nueva += self.mayusculas[j]
#         self.cadena = nueva
#     def a_min(self):
#         nueva = ''
#         #if self.cadena.islower():
#         for w in self.cadena:
#             j=0
#             for j in range(len(self.minusculas)):
#                 if self.minusculas[j] == w or self.mayusculas[j] == w:
#                     nueva += self.minusculas[j]
#         self.cadena = nueva

#     def tamaño(self):
#         i = 0
#         for w in self.cadena:
#             i +=1
#         return i

# hola = Cadena('HOLA COMO ESTAS')
# hola = Cadena('hola como estas')
# # hola.asignar()
# # print(hola.cadena)

# # hola.concat(', bien?')
# # print(hola.cadena)

# hola.a_may()
# hola.a_min()
# print(hola.tamaño())

# hola.tamaño()
# print(hola.tamaño())

class Cadena:
    mayusculas = 'TABCDEFGHIJKLMNÑOPQRSRUVWXYZ '
    minusculas = 'tabcdefghijklmnñopqrsruvwxyz '
    def __init__(self):
        self.max_tamaño = 50
        self.cadena = ""
    
    def __str__(self):
        return self.cadena

    def asignar(self, nueva_cadena):
        if len(nueva_cadena) < self.max_tamaño:
            self.cadena = nueva_cadena
        else:
            print(f"la cadena que intenta asignar es mayor a el tamaño maximo de {self.max_tamaño} caracteres")
    
    def concat(self, otra_cadena):
        nueva = self.cadena + otra_cadena
        if len(nueva) < self.max_tamaño:
            self.cadena = nueva
        else:
            print(f"la cadena que intenta concatenar se pasa del tamaño maximo permitido de {self.max_tamaño} caracteres")

    def a_may(self):
        nueva = ''
        #if self.cadena.isupper():
        for w in self.cadena:
            j=0
            for j in range(len(self.mayusculas)):
                if self.mayusculas[j] == w or self.minusculas[j] == w:
                    nueva += self.mayusculas[j]
        self.cadena = nueva

    def a_min(self):
        nueva = ''
        #if self.cadena.islower():
        for w in self.cadena:
            j=0
            for j in range(len(self.minusculas)):
                if self.minusculas[j] == w or self.mayusculas[j] == w:
                    nueva += self.minusculas[j]
        self.cadena = nueva

    def tamaño(self):
        i = 0
        for w in range(len(self.cadena)):
            i += 1
        return i 


may = Cadena()
may.asignar("HOLA COMO ")
may.a_min()
print(may)
print(may.tamaño())


min = Cadena()
min.asignar("hola como estas gilipollo")
min.a_may()
print(min)
print(min.tamaño())





    
    


    

