class Libro():
    def __init__(self, titulo, autor, anio, stock):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._stock = stock

    def __str__(self):
        return f'{self.titulo} - {self.autor} ({self.anio}) | Cantidad: {self.cantidad}'
    

class libreria():
    def __init__(self, nombre):
        #diccionario: clave = titulo, valor = instancia de libro
        self.nombre = nombre


class carro():

    def __init__(self, lista, total, boleta):
        self.lista = lista
        self.total = total
        self.boleta = boleta
    

class catalogo():
    
    catalogo = {
        'harry potter' : {
            'precio' : 19990,
            'stock' : 2
        }
    }

