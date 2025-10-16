class jugador():

    jugadores_creados = 0

    posiciones_validas = {'DEL', 'VOL', 'DEF', 'ARQ'}

    def __init__(self, nombre, edad, posicion, club, energia=100):
        #atributos privados
        self.__nombre = nombre 
        self.__edad = edad 
        self.__posicion = posicion
        self.__goles = 0
        #atributos publicos
        self.club = club
        self.energia = energia

        assert self.invariantes_clase

    #invariantes de clases
    def invariantes_clase(self):
        assert self.__edad >= 15, 'la edad debe ser mayor o igual a 15'
        assert self.posicion
        assert 0 <= self.energia <= 100, 'energia fuera de rango'
        assert self.goles >= 0, 'los goles no pueden ser menor de cero'
        assert self.club != ' ', 'club no puede estar vacio'


    #getters y setters
    @classmethod
    def creados(cls):
        return
    
    @staticmethod
    def posicion_valida(self):
        return

    @property
    def nombre(self):
        return self.__nombre


    @property
    def edad(self):
        return self.__edad


    @property
    def posicion(self):
        return self.__posicion


    @property
    def goles(self):
        return self.goles



    #metodos de clase 
    def entrenar(self, minutos):
        assert minutos > 0, 'los minutos deben ser cero'
        self.energia -= minutos


    def anotar_gol(self):
        self.__goles += 1



    #metodo magico
    def __str__(self):
        return f'El jugador: {self._nombre}, del club: {self.club}, con posición: {self._posicion}, tiene una energía de: {self.energia}, con  goles: {self._goles}'
    


#instancias de clase
jugador1 = jugador('romario', 25, 'DEL', 'deportes castro', 70)
jugador2 = jugador('juan', 18, 'DEF', 'deportes castro', 15)

print(jugador1)
print(jugador2)


jugador1.anotar_gol()
jugador2.entrenar()