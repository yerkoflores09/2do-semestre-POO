class Animal:
    def __init__(self, nombre, edad, peso, genero):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.genero = genero

    def comer(self):
        print(f'{self.nombre} está comiendo')

    def dormir(self):
        print(f'{self.nombre} esta durmiendo')

    def mostrar_ficha(self):
        print(f'el nombre del animal {self.nombre}, la edad {self.edad}, su peso {self.peso} kg. y su genero es {self.genero}.')

class perro(Animal):
    def __init__(self, nombre, edad, raza, peso, genero):
        super().__init__(nombre, edad, peso, genero)
        self.raza = raza

    def ladrar(self):
        print(f'{self.nombre} esta ladrando')

    def mostrar_ficha(self):
        super().print()

class Gato(Animal):
    def __init__(self, nombre, edad, color_pelaje, peso, genero):
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_pelaje

    def maullar(self):
        print(f'{self.nombre} está maullando')
