#Guia rapida de clases en python

class Animal():

    #constructor de la clase animal 
    #atributos de la clase animal (caracteristicas compartidas por todos los objetos de la clase) 
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.edad = 0

    #metodos de la calse animal (comportamientos)
    def correr(self):
        print(f'{self.nombre} está corriendo')

    def dormir(self):
        print(f'{self.nombre} está durmiendo')

    def volar(self):
        print(f'{self.nombre} está volando')    

#self permite acceder a los atributos que están más arriba


#creando un objeto de la clase animal 
gatito = Animal('michi', 'gato', 4)
perrito = Animal('firulais', 'perro', 2)
loro = Animal('lorito', 'ave', 1)

print(f'el nombre del animal es: {gatito.nombre}')
print(f'la especie del animal es: {perrito.nombre}')
print(f'la especie del animal es: {loro.nombre}')

#llamado a los metodos de los objetos

gatito.correr()
perrito.dormir()
loro.volar()