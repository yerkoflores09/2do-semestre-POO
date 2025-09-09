class Libro():
    def __init__(self, titulo, autor, anio, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.titulo} - {self.autor} ({self.anio}) | Cantidad: {self.cantidad}'



class Biblioteca():
    def __init__(self):
        #diccionario: clave = titulo, valor = instancia de libro
        self.libros = {}

    def agregar_libros(self, libro):
        if libro.titulo in self.libros:
            #si ya existe, solo se actualiza la cantidad
            self.libros[libro.titulo].cantidad += libro.cantidad
        else:
            self.libros[libro.titulo] = libro

    def buscar_libro(self, titulo):
        return self.libros.get(titulo, None) # "get" se usa para recuperar un valor de un diccionario por su clave, devolviendo None
    
    def actualizar_libro(self, titulo, nueva_cantidad):
        if titulo in self.libros:
            self.libros[titulo].cantidad = nueva_cantidad
            return True
        return False
    
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros.values():
                print(libro)

biblio = Biblioteca()

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 3)
libro2 = Libro("El Quijote", "Miguel de Cervantes", 1605, 5)

biblio.agregar_libros(libro1)
biblio.agregar_libros(libro2)

biblio.mostrar_libros()

print('buscando libros')
resultado = biblio.buscar_libro('El Quijote')
if resultado:
    print('Encontrado:', resultado)

print('Actualizado cantidad:')
biblio.actualizar_libro('Cien Años de Soledad', 10)
biblio.mostrar_libros()