class Trabajador():
    def __init__(self, nombre):
        self.nombre = nombre

    def tarea(self):
        return f'el {self.nombre} hace sus funciones normales '


class Chef(Trabajador):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre) #hereda de Trabajador
        self.especialidad = especialidad

    def tarea(self):
        return f'{self.nombre} hace las preparaciones {self.especialidad}'
    

class Mesero(Trabajador):
    def __init__(self, nombre, seccion):
        super().__init__(nombre) #hereda de Trabajador
        self.seccion = seccion

    def tarea(self):
        return f'{self.nombre} atiende en {self.seccion}'
    

class AyudanteChefMesero(Chef, Mesero):
    def __init__(self, nombre, especialidad, seccion):
        Chef.__init__(self, nombre, especialidad) #hereda de Chef
        Mesero.__init__(self, nombre, seccion) #hereda de Mesero

    def tarea(self):
        return f'{self.nombre} ayuda a preparar {self.especialidad} y ayuda en la seccion {self.seccion}'
    

#instancias

trabajador = Trabajador('Ysy-a')
chef = Chef('Pepe', 'Pastas')
mesero = Mesero('Maria', 'terraza')
ayudante = AyudanteChefMesero('Juan', 'Pastas', 'interior')
