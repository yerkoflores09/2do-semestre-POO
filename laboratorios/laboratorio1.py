class Gatos():
    def __init__(self, nombre, edad, energia, hambre):
        self.nombre = nombre
        self.edad = int(edad)
        self.energia = int(energia)
        self.hambre = int(hambre)

    #metodo para que los gatos jueguen en el cafe
    def gatos_juegan(self, correr, perseguir):
        if self.nombre in self.correr:
            self.energia -= 30
            self.hambre -= 15
        elif self.nombre in self.perseguir:
            self.energia -= 40
            self.hambre -= 15
        else:
            print('los gatos están acostados, no quieren jugar...')
        
    #metodo para alimentar a los gatos
    def alimentar_gatos(self, alimentar):
        if self.nombre in self.hambre < 100 and self.energia < 100:
            self.nombre + self.alimentar()
            return self.energia() 
        
    #metodo magico para imprimir el estado del gato
    def __str__(self):
        return f'El gato: {self.nombre} que tiene la edad de {self.edad} años, tiene {self.energia} puntos de energia y {self.hambre} puntos de hambre'
    

#clase del cafe
class CafeGatuno():
    def __init__(self, salon, terraza, jardin):
        self.salon = salon
        self.terraza = terraza
        self.jardin = jardin
        self.capacidad = []

    #metodo para agrgar gatos al cafe
    def agregar_gato(self, gato):
        if self.gato():
            self.gato

    #metodo para mostrar informacion de los gatos en los espacios del cafe
    def __srt__(self):
        return f''
        




gato1 = Gatos('pepe')
gato2 = Gatos('mishi')
gato3 = Gatos('efrain')
print(gato1)

#finalizador
del gato1('pepe')
print(f'El gato pepe ha salido del cafe')