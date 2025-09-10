class Gato:
    def __init__(self, nombre, edad, nivel_energia=100, nivel_hambre=0):
        self.nombre = nombre
        self.edad = edad
        self.nivel_energia = int(nivel_energia)
        self.nivel_hambre = int(nivel_hambre)

    #metodo para cuando los gatos jueguen en el cafe
    def jugar(self, duracion=10):
        #por cada unidad de duracion, se resta energia y aumenta el hambre
        self.nivel_energia = max(0, self.nivel_energia - duracion * 2)
        self.nivel_hambre = min(100, self.nivel_hambre + duracion * 1.5)
        print(f'{self.nombre} ha jugado por {duracion} min. Energia: {self.nivel_energia}, Hambre: {self.nivel_hambre}')

    #metodo para alimentar a los gatos
    def alimentar(self, comida=20):
        self.nivel_hambre = max(0, self.nivel_hambre - comida)
        self.nivel_energia = min(100, self.nivel_energia + comida * 1.2)
        print(f"{self.nombre} ha sido alimentado. Energia: {self.nivel_energia}, Hambre: {self.nivel_hambre}")

    #metodo magico para imprimir el estado del gato
    def __str__(self):
        return (f"Gato {self.nombre}: Edad {self.edad}, Energía {self.nivel_energia:.1f}, "
            f"Hambre {self.nivel_hambre:.1f}") # ':.1f' indica que un número de punto flotante debe mostrarse con exactamente un dígito después del punto decimal, redondeando el número si es necesario
    
    #finalizador
    def __del__(self):
        print(f"El gato {self.nombre} ha salido del café")



class CafeGatuno():
    def __init__(self, nombre, capacidad_maxima):
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.gatos_presentes = []

    #metodo para agrgar gatos al cafe
    def agregar_gato(self, gato):
        if len(self.gatos_presentes) < self.capacidad_maxima:
            self.gatos_presentes.append(gato)
            print(f"{gato.nombre} ha sido agregado al espacio {self.nombre}")
        else:
            print(f"No se puede agregar a {gato.nombre}: capacidad máxima de {self.nombre} alcanzada")

    #metodo para mostrar informacion de los gatos en los espacios del cafe
    def listar_gatos(self):
        if not self.gatos_presentes:
            print(f"No hay gatos en {self.nombre}")
        else:
            print(f"Gatos en {self.nombre}:")
            for gato in self.gatos_presentes:
                print(f" - {gato.nombre}, Edad: {gato.edad}")

#finalizador
def __del__(self):
    print(f"El gato {self.nombre} ha salido del café")


gato1 = Gato("Luna", 2)
gato2 = Gato("Michi", 3)
gato3 = Gato("Efrain", 1.5)

# Crear espacios
salon = CafeGatuno("Salón", capacidad_maxima=2)
terraza = CafeGatuno("Terraza", capacidad_maxima=3)

# Agregar gatos a los espacios
salon.agregar_gato(gato1)
salon.agregar_gato(gato2)
salon.agregar_gato(gato3)  # Debería indicar que ya no hay espacio

# Listar gatos en cada espacio
salon.listar_gatos()
terraza.listar_gatos()

# Interaccion con los gatos
print(gato1)
gato1.jugar(duracion=15)
gato1.alimentar(comida=30)
print(gato1)