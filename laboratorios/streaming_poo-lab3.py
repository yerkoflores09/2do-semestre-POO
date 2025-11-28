#clase Principal
class Contenido():

    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio

    def mostrar_detalle(self):
        print(f'Titulo: {self.titulo}, año: {self.anio}')
    

#Estructura de clases     
class Reproducible(Contenido):

    def __init__(self, titulo, anio):
        super().__init__(titulo, anio)

    def reproducir(self):
        pass

class Calificable():
    def __init__(self, capacidad):
        float(rating) = 0.0
        self.capacidad = capacidad
    
    def calificar(self, puntuacion):
        self.rating = puntuacion
        print(f'calificación: {self.rating}')


#Subclases

class Pelicula(Contenido, Reproducible):
    
    def __init__(self, titulo, anio, duracion_minutos):
        super().__init__(titulo, anio)
        self.duracion_minutos = duracion_minutos

    def reproducir(self):
        print(f'reproduciendo pelicula: {self.titulo}, (de duracion: {self.duracion_minutos})')


class Documental(Contenido):
    
    def __init__(self, titulo, anio, tema):
        super().__init__(titulo, anio)
        self.tema = tema

    def mostrar_detalle(self):
        print(f'el documental, Titulo: {self.titulo}, año: {self.anio}, tema: {self.tema}')
    

class Miniserie(Contenido, Reproducible, Calificable):

    def __init__(self, titulo, anio, num_episodios):
        super().__init__(titulo, anio)
        self.num_episodios = num_episodios

    def reproducir(self):
        print(f'reproduciendo miniserie: {self.titulo} (tiene {self.num_episodios} episodios')


def lista_reproduccion(lista_contenidos):
    pass



#instancias de clase

pelicula = Pelicula('home alone', 1990, )
documental = Documental('chiloe salmones', 2010, 'naturaleza')
miniserie = Miniserie('Chernobyl', 2020, 6)

miniserie.mostrar_detalle()
miniserie.reproducir()
miniserie.calificar(4.8)