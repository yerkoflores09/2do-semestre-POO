class automovil():
    # Constructor de la clase automovil
    def __init__(self, marca, modelo, anio, __disponible):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.__disponible = True(__disponible)

    #metodo para cambiar el estado del vehiculo
    def marcar_vendido(self):
        self.__disponible = self.__disponible(False)


    #mostrar los detalles del vehiculo
    def __str__(self):
        return (f'marca del auto: {self.marca}'
                f'modelo del auto: {self.modelo}'
                f'año: {self.anio}'
                f'disponibilidad: {self.__disponible}')


    class consecionaria():

        def __init__(self, cantidad):
            self.cantidad = int(cantidad)

        #añadir nuevos vehículos a la concesionaria.
        def agregar_vehiculo(self):
            return


        # listar todos los vehículos disponibles en la concesionaria.
        def mostrar_vehiculos(self):
            return
        
        #cambiar estado de disponibilidad de un vehiculo cuando sea vendido
        def vender_vehiculos(self):
            return




# Creando objetos de la clase automovil

auto1 = automovil('Toyota', 'Corolla', 2020)
auto2 = automovil('Ford', 'Mustang', 2021)
auto3 = automovil('Honda', 'Civic', 2019)

print(f'El auto 1 es un {auto1.marca}, {auto1.modelo} del año {auto1.año}')
