class automovil():
    # Constructor de la clase automovil
    # Atributos de la clase automovil (caracteristicas compartidas por todos los objetos de la clase)
    def __init__(self, marca, gasolina, modelo, anio, color):
        self.marca = marca
        self.gasolina = float(gasolina)
        self.modelo = modelo
        self.año = anio
        self.color = color

    # Métodos de la clase automovil (comportamientos)
    def arrancar(self):
        print(f'El {self.marca} {self.modelo} está arrancando')

    def frenar(self):
        print(f'El {self.marca} {self.modelo} está frenando')

    def acelerar(self):
        print(f'El {self.marca} {self.modelo} está acelerando')

# Creando objetos de la clase automovil

auto1 = automovil('Toyota', 'Corolla', 2020, '')
auto2 = automovil('Ford', 'Mustang', 2021, 'azul')
auto3 = automovil('Honda', 'Civic', 2019, 'negro')

print(f'El auto 1 es un {auto1.marca}, {auto1.modelo} del año {auto1.año}')
