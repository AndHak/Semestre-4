from bed.jerarquicas.abin_bus import ArbolBinario_Bus
from bed.jerarquicas.recorrido import str_pre_orden, str_in_orden, str_post_orden
class Libro:
    def __init__(self, titulo, isbn, autor="", num_paginas=0):
        if len(titulo) < 3:
            raise ValueError("El título debe tener al menos 3 caracteres.")
        if not (10 <= len(isbn) <= 13 and isbn.isdigit()):
            raise ValueError("El ISBN debe ser numérico y contener entre 10 y 13 dígitos.")
        
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.num_paginas = num_paginas

    def __str__(self):
        return f"{{ 📖 :{self.titulo}:{self.autor}:{self.isbn}:{self.num_paginas} pags.}}"

    def __eq__(self, otro):
        return self.titulo == otro.titulo and self.isbn == otro.isbn

    def __lt__(self, otro):
        return (self.titulo, self.isbn) < (otro.titulo, otro.isbn)

    def __gt__(self, otro):
        return (self.titulo, self.isbn) > (otro.titulo, otro.isbn)

class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.bodega_libros = ArbolBinario_Bus()

    def agregar_libro(self, libro):
        """Agrega un libro a la bodega."""
        self.bodega_libros.adicionar(libro)

    def buscar_libro(self, titulo, isbn):
        """Busca un libro usando título e ISBN."""
        libro_buscado = Libro(titulo, isbn)
        return self.bodega_libros.encontrar(libro_buscado)

    def eliminar_libro(self, titulo, isbn, mayor=True):
        """Elimina un libro usando título e ISBN, y el tipo de reemplazo."""
        libro_eliminar = Libro(titulo, isbn)
        self.bodega_libros.remover(libro_eliminar, mayor)

    def libro_menor(self):
        """Retorna el libro con menor valor."""
        return self.bodega_libros.encontrar_minimo()

    def libro_mayor(self):
        """Retorna el libro con mayor valor."""
        return self.bodega_libros.encontrar_maximo()

    def estadisticas(self):
        """Calcula estadísticas del árbol."""
        hojas = self.bodega_libros.hojas()  # Método hipotético para contar hojas
        internos = self.bodega_libros.internos()  # Método para contar nodos internos
        altura = self.bodega_libros.altura()  # Método para calcular altura
        total = hojas + internos
        return f"""
        +--------------------------------------------------------------------+
        | No. Libros Hoja  | No. Libros Internos  | Altura | Total de libros |
        ----------------------------------------------------------------------
        | {hojas:<17}| {internos:<20}| {altura:<7}| {total:<15}|
        +--------------------------------------------------------------------+
        """

    def __str__(self):
        """Devuelve una representación en cadena de la biblioteca con los libros en preorden."""
        libros_preorden = str_pre_orden(self.bodega_libros, sep="|")
        return f"Biblioteca: {self.nombre} 🌲 📖 ]{{ Dirección: {self.direccion} Teléfono: {self.telefono} {libros_preorden}"

def menu_biblioteca():
    biblioteca = Biblioteca("ACME", "Clle. 8 # 15 - 78 Torobajo", "6027845931")
    while True:
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Eliminar libro")
        print("4. Mostrar libro menor")
        print("5. Mostrar libro mayor")
        print("6. Mostrar estadísticas")
        print("7. Mostrar biblioteca")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Ingrese título del libro: ")
            isbn = input("Ingrese ISBN del libro: ")
            autor = input("Ingrese autor(es) del libro: ")
            num_paginas = int(input("Ingrese número de páginas: "))
            try:
                libro = Libro(titulo, isbn, autor, num_paginas)
                biblioteca.agregar_libro(libro)
                print("Libro agregado exitosamente.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "2":
            titulo = input("Ingrese título del libro a buscar: ")
            isbn = input("Ingrese ISBN del libro a buscar: ")
            libro = biblioteca.buscar_libro(titulo, isbn)
            if libro:
                print(f"Libro encontrado: {libro}")
            else:
                print("Libro no encontrado.")

        elif opcion == "3":
            titulo = input("Ingrese título del libro a eliminar: ")
            isbn = input("Ingrese ISBN del libro a eliminar: ")
            mayor = input("Reemplazo por MENOR de hijos mayores (True/False): ").lower() == "true"
            try:
                biblioteca.eliminar_libro(titulo, isbn, mayor)
                print("Libro eliminado exitosamente.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            menor_libro = biblioteca.libro_menor()
            print(f"Libro menor: {menor_libro}")

        elif opcion == "5":
            mayor_libro = biblioteca.libro_mayor()
            print(f"Libro mayor: {mayor_libro}")

        elif opcion == "6":
            print(biblioteca.estadisticas())

        elif opcion == "7":
            print(biblioteca)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")
